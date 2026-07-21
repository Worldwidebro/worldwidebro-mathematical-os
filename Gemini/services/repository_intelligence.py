#!/usr/bin/env python3
import os
import sys
import ast
import re
import json
import hashlib
import requests
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
from neo4j import GraphDatabase

# Add parent path to allow importing os_env
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from os_env import OLLAMA_EMBED as OLLAMA, EMBED_MODEL, QDRANT, NEO4J_URI, NEO4J_AUTH
except ImportError:
    OLLAMA = "http://100.87.214.70:11434/api/embeddings"
    EMBED_MODEL = "nomic-embed-text"
    QDRANT = "http://100.87.214.70:6333"
    NEO4J_URI = "bolt://100.87.214.70:7687"
    NEO4J_AUTH = ("neo4j", "ventures2026")

class RepoScanner:
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
    
    def _should_scan(self, path: Path) -> bool:
        parts = path.parts
        # Skip node_modules, .git, venv, and binary files
        if any(p.startswith('.') or p in ('node_modules', 'venv', '__pycache__', 'dist', 'build') for p in parts):
            return False
        return path.suffix in ('.py', '.js', '.ts', '.jsx', '.tsx', '.json', '.txt', '.md', '.yaml', '.yml')

    def scan(self) -> Dict[str, Any]:
        if not self.repo_path.exists():
            return {"error": f"Repository path {self.repo_path} does not exist"}
        
        files = []
        for file_path in self.repo_path.rglob('*'):
            if file_path.is_file() and self._should_scan(file_path):
                try:
                    rel_path = file_path.relative_to(self.repo_path)
                    files.append(self._analyze_file(file_path, str(rel_path)))
                except Exception as e:
                    print(f"Error scanning {file_path}: {e}")
        
        return {
            'metadata': self._get_metadata(),
            'files': files,
            'dependencies': self._extract_deps(),
            'structure': self._build_tree()
        }
    
    def _get_metadata(self) -> Dict[str, Any]:
        return {
            'name': self.repo_path.name,
            'path': str(self.repo_path),
            'last_updated': str(datetime.now())
        }

    def _analyze_file(self, path: Path, rel_path: str) -> Dict[str, Any]:
        content = path.read_text(encoding='utf-8', errors='ignore')
        ext = path.suffix
        if ext == '.py':
            return self._analyze_python(rel_path, content)
        elif ext in ('.js', '.ts', '.jsx', '.tsx'):
            return self._analyze_js(rel_path, content)
        else:
            return {
                'path': rel_path,
                'type': 'doc' if ext in ('.md', '.txt') else 'config',
                'size': len(content),
                'docstring': content[:400] if ext in ('.md', '.txt') else ''
            }
    
    def _analyze_python(self, rel_path: str, content: str) -> Dict[str, Any]:
        try:
            tree = ast.parse(content)
        except SyntaxError:
            return {'path': rel_path, 'type': 'python', 'valid': False, 'imports': [], 'functions': [], 'classes': []}
        
        imports = []
        functions = []
        classes = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                for alias in node.names:
                    imports.append(f"{module}.{alias.name}")
            elif isinstance(node, ast.FunctionDef):
                functions.append(node.name)
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
        
        return {
            'path': rel_path,
            'type': 'python',
            'imports': imports,
            'functions': functions,
            'classes': classes,
            'docstring': ast.get_docstring(tree) or '',
            'valid': True
        }
    
    def _analyze_js(self, rel_path: str, content: str) -> Dict[str, Any]:
        imports = re.findall(r"(?:import|require)\s*\(?['\"]([^'\"]+)['\"]", content)
        functions = re.findall(r"function\s+([a-zA-Z0-9_]+)", content)
        classes = re.findall(r"class\s+([a-zA-Z0-9_]+)", content)
        return {
            'path': rel_path,
            'type': 'javascript',
            'imports': imports,
            'functions': functions,
            'classes': classes,
            'docstring': content[:300] if len(content) > 300 else content,
            'valid': True
        }

    def _extract_deps(self) -> List[str]:
        deps = []
        package_json = self.repo_path / "package.json"
        requirements_txt = self.repo_path / "requirements.txt"
        if package_json.exists():
            try:
                data = json.loads(package_json.read_text(encoding='utf-8', errors='ignore'))
                deps.extend(data.get("dependencies", {}).keys())
                deps.extend(data.get("devDependencies", {}).keys())
            except Exception:
                pass
        if requirements_txt.exists():
            try:
                for line in requirements_txt.read_text(encoding='utf-8', errors='ignore').split('\n'):
                    line = line.strip()
                    if line and not line.startswith('#'):
                        name = re.split(r'[=<>~]', line)[0].strip()
                        if name:
                            deps.append(name)
            except Exception:
                pass
        return list(set(deps))

    def _build_tree(self) -> Dict[str, Any]:
        return {"tree": "flat"}


class RepoIndexer:
    def __init__(self):
        self.qdrant_url = QDRANT
        self.collection_name = 'code_intelligence'
        self._ensure_collection()
    
    def _ensure_collection(self):
        try:
            r = requests.get(f"{self.qdrant_url}/collections/{self.collection_name}", timeout=10)
            if r.status_code != 200:
                body = {
                    "vectors": {
                        "size": 768 if EMBED_MODEL == "nomic-embed-text" else 384,
                        "distance": "Cosine"
                    }
                }
                requests.put(f"{self.qdrant_url}/collections/{self.collection_name}", json=body, timeout=10)
        except Exception as e:
            print(f"Warning: could not initialize Qdrant collection: {e}")

    def embed_text(self, text: str) -> List[float]:
        try:
            r = requests.post(OLLAMA, json={"model": EMBED_MODEL, "prompt": text}, timeout=30)
            r.raise_for_status()
            return r.json()["embedding"]
        except Exception as e:
            print(f"Embedding failed: {e}. Fallback to dummy vector.")
            size = 768 if EMBED_MODEL == "nomic-embed-text" else 384
            return [0.0] * size

    def index_file(self, file_info: Dict[str, Any], repo_name: str):
        text_to_embed = f"Repo: {repo_name}\nPath: {file_info['path']}\nType: {file_info.get('type', '')}\nDocs: {file_info.get('docstring', '')}"
        vector = self.embed_text(text_to_embed)
        point_id = hashlib.md5(f"{repo_name}:{file_info['path']}".encode()).hexdigest()
        
        point = {
            "points": [{
                "id": point_id,
                "vector": vector,
                "payload": {
                    "repo": repo_name,
                    "path": file_info['path'],
                    "type": file_info.get('type', 'unknown'),
                    "imports": file_info.get('imports', []),
                    "functions": file_info.get('functions', []),
                    "classes": file_info.get('classes', [])
                }
            }]
        }
        try:
            requests.post(f"{self.qdrant_url}/collections/{self.collection_name}/points?wait=true", json=point, timeout=10)
        except Exception as e:
            print(f"Failed to upsert to Qdrant: {e}")

    def search(self, query: str, limit=10) -> List[Dict[str, Any]]:
        vector = self.embed_text(query)
        body = {
            "vector": vector,
            "limit": limit,
            "with_payload": True
        }
        try:
            r = requests.post(f"{self.qdrant_url}/collections/{self.collection_name}/points/search", json=body, timeout=10)
            r.raise_for_status()
            return [hit["payload"] for hit in r.json().get("result", [])]
        except Exception as e:
            print(f"Search failed: {e}")
            return []


class KnowledgeGraphBuilder:
    def __init__(self):
        self.uri = NEO4J_URI
        self.auth = NEO4J_AUTH
    
    def build_from_scan(self, scan_result: Dict[str, Any], repo_name: str):
        try:
            driver = GraphDatabase.driver(self.uri, auth=self.auth)
            with driver.session() as session:
                session.run("""
                    MERGE (r:Repository {name: $name})
                    SET r.path = $path, r.last_updated = $updated
                """, name=repo_name, path=scan_result['metadata'].get('path'), updated=scan_result['metadata'].get('last_updated'))
                
                for file in scan_result.get('files', []):
                    session.run("""
                        MATCH (r:Repository {name: $repo})
                        MERGE (f:File {path: $path, repo: $repo})
                        SET f.type = $type
                        MERGE (r)-[:CONTAINS]->(f)
                    """, repo=repo_name, path=file['path'], type=file.get('type', 'unknown'))
                    
                    for func in file.get('functions', []):
                        session.run("""
                            MATCH (f:File {path: $path, repo: $repo})
                            MERGE (fn:Function {name: $func, repo: $repo})
                            MERGE (f)-[:DEFINES]->(fn)
                        """, path=file['path'], repo=repo_name, func=func)
                    
                    for cls in file.get('classes', []):
                        session.run("""
                            MATCH (f:File {path: $path, repo: $repo})
                            MERGE (c:Class {name: $cls, repo: $repo})
                            MERGE (f)-[:DEFINES]->(c)
                        """, path=file['path'], repo=repo_name, cls=cls)
            driver.close()
        except Exception as e:
            print(f"Neo4j graph building failed: {e}")

    def get_dependents(self, file_path: str) -> List[str]:
        try:
            driver = GraphDatabase.driver(self.uri, auth=self.auth)
            with driver.session() as session:
                result = session.run("""
                    MATCH (f:File {path: $path})<-[:DEPENDS_ON]-(d:File)
                    RETURN d.path AS dependent
                """, path=file_path)
                dependents = [record['dependent'] for record in result]
            driver.close()
            return dependents
        except Exception:
            return []

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
        scanner = RepoScanner(path)
        print(json.dumps(scanner.scan(), indent=2))
