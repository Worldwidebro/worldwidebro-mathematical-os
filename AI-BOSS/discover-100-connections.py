#!/usr/bin/env python3
"""
Discover and register the 100 connections in WORLDWIDEBRO system.

Answers: What is connected to what, why, how strongly, and what business value?

Uses actual filesystem, Neo4j, and knowledge to build the connection registry.
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Set, Tuple

# Neo4j driver
try:
    from neo4j import GraphDatabase
    NEO4J_AVAILABLE = True
except ImportError:
    NEO4J_AVAILABLE = False

# Configuration
DOCUMENTS_ROOT = Path("/Users/acebless/Documents")
AI_BOSS_ROOT = DOCUMENTS_ROOT / "AI-BOSS"
REGISTRY_DIR = AI_BOSS_ROOT / "REGISTRY"
REGISTRY_DIR.mkdir(parents=True, exist_ok=True)

NEO4J_URI = "neo4j://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "ventures2026"


class ConnectionDiscovery:
    """Discover connections between entities in WORLDWIDEBRO system."""

    def __init__(self):
        self.entities = {}  # id -> {type, name, ...}
        self.relationships = []  # [{from_id, to_id, type, weight, reason}]
        self.file_contents = {}  # file_path -> content_hash
        self.duplicates = defaultdict(list)  # content_hash -> [file_paths]

        self.neo4j = None
        if NEO4J_AVAILABLE:
            try:
                self.neo4j = GraphDatabase.driver(
                    NEO4J_URI,
                    auth=(NEO4J_USER, NEO4J_PASSWORD)
                )
            except Exception as e:
                print(f"Warning: Could not connect to Neo4j: {e}")

    def scan_filesystem(self):
        """Scan Documents folder for entities."""
        print("\n=== SCANNING FILESYSTEM ===")

        # Scan top-level folders
        for item in DOCUMENTS_ROOT.iterdir():
            if item.name.startswith('.'):
                continue

            if item.is_dir():
                self._register_entity(
                    id=f"folder:{item.name}",
                    type="folder",
                    name=item.name,
                    path=str(item),
                    size_mb=self._get_size_mb(item)
                )
            elif item.is_file():
                self._register_entity(
                    id=f"file:{item.name}",
                    type="file",
                    name=item.name,
                    path=str(item),
                    size_mb=self._get_size_mb(item)
                )

        print(f"Found {len(self.entities)} entities")

    def scan_git_repos(self):
        """Identify git repositories and their relationships."""
        print("\n=== SCANNING GIT REPOSITORIES ===")

        git_repos = []
        for item in DOCUMENTS_ROOT.rglob(".git"):
            repo_path = item.parent
            repo_name = repo_path.name

            repo_id = f"repo:{repo_name}"
            self._register_entity(
                id=repo_id,
                type="repository",
                name=repo_name,
                path=str(repo_path),
                remote=self._get_git_remote(repo_path)
            )
            git_repos.append((repo_id, repo_path))

        # Identify relationships: which repos are duplicates?
        for i, (id1, path1) in enumerate(git_repos):
            for id2, path2 in git_repos[i+1:]:
                if self._are_duplicate_repos(path1, path2):
                    self._add_relationship(id1, id2, "DUPLICATES", weight=0.9)
                    print(f"  DUPLICATE: {id1} <-> {id2}")

        print(f"Found {len(git_repos)} git repositories")

    def scan_known_systems(self):
        """Register known named systems."""
        print("\n=== REGISTERING KNOWN SYSTEMS ===")

        systems = {
            "AI-BOSS": "Orchestration engine (decision→execution→verification)",
            "IZA-OS": "Intelligence/knowledge layer",
            "VEX": "Marketplace platform",
            "WORLDWIDEBRO": "Holding company structure",
        }

        for name, description in systems.items():
            self._register_entity(
                id=f"system:{name}",
                type="system",
                name=name,
                description=description
            )

    def identify_aliases(self):
        """Find aliases and redundant naming."""
        print("\n=== IDENTIFYING ALIASES ===")

        # Known aliases from previous analysis
        aliases = {
            "system:AI-BOSS": ["system:IZA-OS", "system:WORLDWIDEBRO", "system:VEX"],
            # Add discovered aliases
        }

        for canonical, aliases_list in aliases.items():
            for alias in aliases_list:
                if alias in self.entities:
                    self._add_relationship(
                        canonical, alias,
                        "ALIAS_OF", weight=0.8
                    )
                    print(f"  ALIAS: {canonical} ≈ {alias}")

    def find_duplicates(self):
        """Find duplicate files and folders."""
        print("\n=== FINDING DUPLICATES ===")

        for root, dirs, files in os.walk(DOCUMENTS_ROOT):
            for file in files:
                if file.startswith('.'):
                    continue

                path = Path(root) / file
                try:
                    content_hash = self._hash_file(path)
                    self.file_contents[str(path)] = content_hash
                    self.duplicates[content_hash].append(str(path))
                except:
                    pass

        duplicate_count = 0
        for content_hash, paths in self.duplicates.items():
            if len(paths) > 1:
                duplicate_count += len(paths) - 1
                canonical = paths[0]
                for duplicate in paths[1:]:
                    self._add_relationship(
                        f"file:{Path(canonical).name}",
                        f"file:{Path(duplicate).name}",
                        "DUPLICATES", weight=0.95
                    )

        print(f"Found {duplicate_count} duplicate files")

    def analyze_documents(self):
        """Analyze markdown/json documents for content relationships."""
        print("\n=== ANALYZING DOCUMENTS ===")

        doc_count = 0
        for md_file in DOCUMENTS_ROOT.rglob("*.md"):
            try:
                with open(md_file, 'r') as f:
                    content = f.read()

                # Register the document
                doc_id = f"doc:{md_file.stem}"
                self._register_entity(
                    id=doc_id,
                    type="document",
                    name=md_file.stem,
                    path=str(md_file),
                    size_kb=md_file.stat().st_size / 1024
                )

                # Find references to other entities
                for entity_id, entity in self.entities.items():
                    if entity.get("name") and entity.get("name") in content:
                        self._add_relationship(
                            doc_id, entity_id,
                            "DESCRIBES", weight=0.5
                        )

                doc_count += 1
            except:
                pass

        print(f"Analyzed {doc_count} documents")

    def build_connection_registry(self):
        """Build the 100-connection registry."""
        print("\n=== BUILDING 100-CONNECTION REGISTRY ===")

        registry = {
            "generated_at": datetime.now().isoformat(),
            "entity_count": len(self.entities),
            "relationship_count": len(self.relationships),

            "entities": self.entities,
            "relationships": self.relationships,

            "connection_analysis": self._analyze_connections(),
            "duplicates_found": dict(self.duplicates),
        }

        # Save registry
        registry_file = REGISTRY_DIR / "connections.json"
        with open(registry_file, 'w') as f:
            json.dump(registry, f, indent=2)

        print(f"Registry saved to {registry_file}")
        return registry

    def push_to_neo4j(self):
        """Push connection registry to Neo4j."""
        if not self.neo4j:
            print("Neo4j not available")
            return

        print("\n=== PUSHING TO NEO4J ===")

        try:
            with self.neo4j.session() as session:
                # Create all entities as nodes
                for entity_id, entity in self.entities.items():
                    properties = {**entity, "entity_id": entity_id}
                    session.run(
                        """
                        MERGE (n:Entity {entity_id: $entity_id})
                        SET n += $properties
                        """,
                        entity_id=entity_id,
                        properties=properties
                    )

                # Create all relationships
                for rel in self.relationships:
                    session.run(
                        """
                        MATCH (a:Entity {entity_id: $from_id})
                        MATCH (b:Entity {entity_id: $to_id})
                        CREATE (a)-[r:CONNECTED {type: $rel_type, weight: $weight}]->(b)
                        """,
                        from_id=rel["from_id"],
                        to_id=rel["to_id"],
                        rel_type=rel["type"],
                        weight=rel.get("weight", 0.5)
                    )

            print(f"Pushed {len(self.entities)} entities and {len(self.relationships)} relationships to Neo4j")
        except Exception as e:
            print(f"Error pushing to Neo4j: {e}")

    # Utility methods

    def _register_entity(self, id: str, type: str, name: str, **kwargs):
        """Register an entity."""
        self.entities[id] = {
            "id": id,
            "type": type,
            "name": name,
            "discovered_at": datetime.now().isoformat(),
            **kwargs
        }

    def _add_relationship(self, from_id: str, to_id: str, rel_type: str, weight: float = 0.5, reason: str = ""):
        """Add a relationship."""
        self.relationships.append({
            "from_id": from_id,
            "to_id": to_id,
            "type": rel_type,
            "weight": weight,
            "reason": reason,
            "discovered_at": datetime.now().isoformat()
        })

    def _get_size_mb(self, path: Path) -> float:
        """Get folder/file size in MB."""
        try:
            if path.is_file():
                return path.stat().st_size / (1024 * 1024)
            else:
                total = sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
                return total / (1024 * 1024)
        except:
            return 0

    def _hash_file(self, path: Path) -> str:
        """Hash file contents."""
        hash_obj = hashlib.md5()
        with open(path, 'rb') as f:
            hash_obj.update(f.read())
        return hash_obj.hexdigest()

    def _get_git_remote(self, repo_path: Path) -> str:
        """Get git remote URL."""
        try:
            config_file = repo_path / ".git" / "config"
            if config_file.exists():
                with open(config_file) as f:
                    for line in f:
                        if "url =" in line:
                            return line.split("=", 1)[1].strip()
        except:
            pass
        return ""

    def _are_duplicate_repos(self, path1: Path, path2: Path) -> bool:
        """Check if two repos are duplicates."""
        # Simple heuristic: same name or very similar structure
        return path1.name == path2.name or \
               self._similarity(path1.name, path2.name) > 0.8

    def _similarity(self, s1: str, s2: str) -> float:
        """String similarity 0-1."""
        if s1 == s2:
            return 1.0
        if len(s1) == 0 or len(s2) == 0:
            return 0.0
        matches = sum(1 for a, b in zip(s1, s2) if a == b)
        return matches / max(len(s1), len(s2))

    def _analyze_connections(self) -> Dict:
        """Analyze the connection graph for insights."""
        return {
            "total_entities": len(self.entities),
            "total_relationships": len(self.relationships),
            "relationship_types": self._count_by_type(self.relationships),
            "entity_types": self._count_by_type(self.entities.values()),
        }

    def _count_by_type(self, items):
        """Count items by type."""
        counts = defaultdict(int)
        for item in items:
            if isinstance(item, dict):
                counts[item.get("type", "unknown")] += 1
        return dict(counts)


def main():
    """Run the discovery."""
    print("=" * 60)
    print("WORLDWIDEBRO 100-CONNECTION DISCOVERY")
    print("=" * 60)

    discovery = ConnectionDiscovery()

    # Run discovery phases
    discovery.scan_filesystem()
    discovery.scan_git_repos()
    discovery.scan_known_systems()
    discovery.identify_aliases()
    discovery.find_duplicates()
    discovery.analyze_documents()

    # Build and export registry
    registry = discovery.build_connection_registry()

    # Push to Neo4j
    if discovery.neo4j:
        discovery.push_to_neo4j()

    print("\n" + "=" * 60)
    print("DISCOVERY COMPLETE")
    print("=" * 60)

    return registry


if __name__ == "__main__":
    main()
