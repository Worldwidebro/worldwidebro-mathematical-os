#!/usr/bin/env python3
import os
import sys
import json
import hashlib
import requests
from typing import Dict, List, Any
from neo4j import GraphDatabase

# Add parent path to allow importing os_env
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from os_env import OLLAMA_EMBED as OLLAMA, OLLAMA_CHAT, EMBED_MODEL, CHAT_MODEL, QDRANT, NEO4J_URI, NEO4J_AUTH
except ImportError:
    OLLAMA = "http://100.87.214.70:11434/api/embeddings"
    OLLAMA_CHAT = "http://100.87.214.70:11434/v1/chat/completions"
    EMBED_MODEL = "nomic-embed-text"
    CHAT_MODEL = "qwen3:8b"
    QDRANT = "http://100.87.214.70:6333"
    NEO4J_URI = "bolt://100.87.214.70:7687"
    NEO4J_AUTH = ("neo4j", "ventures2026")

class HybridRetriever:
    def __init__(self):
        self.qdrant_url = QDRANT
        self.collection_name = 'knowledge_chunks'
        self.uri = NEO4J_URI
        self.auth = NEO4J_AUTH
        self._ensure_collection()
    
    def _ensure_collection(self):
        try:
            r = requests.get(f"{self.qdrant_url}/collections/{self.collection_name}", timeout=5)
            if r.status_code != 200:
                body = {
                    "vectors": {
                        "size": 768 if EMBED_MODEL == "nomic-embed-text" else 384,
                        "distance": "Cosine"
                    }
                }
                requests.put(f"{self.qdrant_url}/collections/{self.collection_name}", json=body, timeout=5)
        except Exception as e:
            print(f"Warning: could not initialize Qdrant knowledge collection: {e}")

    def embed_text(self, text: str) -> List[float]:
        try:
            r = requests.post(OLLAMA, json={"model": EMBED_MODEL, "prompt": text}, timeout=30)
            r.raise_for_status()
            return r.json()["embedding"]
        except Exception:
            size = 768 if EMBED_MODEL == "nomic-embed-text" else 384
            return [0.0] * size

    def retrieve(self, query: str, top_k=10) -> List[Dict[str, Any]]:
        candidates = []
        seen = set()

        # 1. Vector search via Qdrant
        try:
            vector = self.embed_text(query)
            body = {
                "vector": vector,
                "limit": top_k * 2,
                "with_payload": True
            }
            r = requests.post(f"{self.qdrant_url}/collections/{self.collection_name}/points/search", json=body, timeout=5)
            if r.status_code == 200:
                for hit in r.json().get("result", []):
                    payload = hit.get("payload", {})
                    text = payload.get("text", "")
                    if text and text not in seen:
                        seen.add(text)
                        candidates.append({
                            "text": text,
                            "score": hit.get("score", 0.5),
                            "metadata": payload.get("metadata", {})
                        })
        except Exception as e:
            print(f"Qdrant retrieval error: {e}")

        # 2. Graph concept search via Neo4j
        try:
            driver = GraphDatabase.driver(self.uri, auth=self.auth)
            with driver.session() as session:
                # Query concept entities matching keywords
                result = session.run("""
                    MATCH (c:Concept)-[:MENTIONED_IN]->(chunk:Chunk)
                    WHERE toLower(c.name) CONTAINS toLower($query)
                    RETURN chunk.text as text, chunk.metadata as metadata, c.name as concept
                    LIMIT 20
                """, query=query)
                for record in result:
                    text = record["text"]
                    if text and text not in seen:
                        seen.add(text)
                        # Load metadata dynamically if stringified
                        metadata = record["metadata"]
                        if isinstance(metadata, str):
                            try:
                                metadata = json.loads(metadata)
                            except Exception:
                                metadata = {}
                        candidates.append({
                            "text": text,
                            "score": 0.6,  # Baseline keyword match score
                            "metadata": metadata
                        })
            driver.close()
        except Exception as e:
            print(f"Neo4j retrieval error: {e}")
            
        return candidates[:top_k]


class Reranker:
    def __init__(self):
        # We can implement a local cross-encoder if installed,
        # otherwise we calculate cosine similarity scoring locally using embeddings.
        self.has_ce = False
        try:
            from sentence_transformers import CrossEncoder
            self.model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
            self.has_ce = True
        except ImportError:
            pass

    def rerank(self, query: str, candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if not candidates:
            return []
        
        if self.has_ce:
            try:
                pairs = [(query, c['text']) for c in candidates]
                scores = self.model.predict(pairs)
                for c, s in zip(candidates, scores):
                    c['score'] = float(s)
                return sorted(candidates, key=lambda x: x['score'], reverse=True)
            except Exception:
                pass
        
        # Fallback to current score
        return sorted(candidates, key=lambda x: x.get('score', 0), reverse=True)


class LLMAdapter:
    def __init__(self):
        # Try redis cache connection, fallback to in-memory dictionary cache
        self.redis_conn = None
        self.local_cache = {}
        try:
            import redis
            self.redis_conn = redis.Redis(host='localhost', port=6379, db=0, socket_timeout=2, decode_responses=True)
            self.redis_conn.ping()
        except Exception:
            self.redis_conn = None
            self.local_cache = {}
            
        # Load env variables from fcc env file
        self.env_vars = {}
        fcc_env_path = os.path.expanduser('~/.fcc/.env')
        if os.path.exists(fcc_env_path):
            try:
                with open(fcc_env_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line_strip = line.strip()
                        if line_strip and not line_strip.startswith('#') and '=' in line_strip:
                            k, v = line_strip.split('=', 1)
                            self.env_vars[k.strip()] = v.strip().strip('"').strip("'")
            except Exception as e:
                print(f"Error loading ~/.fcc/.env: {e}")

    def generate(self, prompt: str, model=CHAT_MODEL, use_cache=True) -> str:
        cache_key = hashlib.md5(f"{prompt}:{model}".encode()).hexdigest()
        
        if use_cache:
            if self.redis_conn:
                try:
                    cached = self.redis_conn.get(cache_key)
                    if cached:
                        return cached
                except Exception:
                    pass
            elif cache_key in self.local_cache:
                return self.local_cache[cache_key]
        
        answer = None
        errors = []

        # 1. Try NVIDIA NIM if configured
        nim_key = self.env_vars.get("NVIDIA_NIM_API_KEY")
        if nim_key:
            try:
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {nim_key}"
                }
                body = {
                    "model": "meta/llama-3.1-70b-instruct",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.2,
                    "max_tokens": 1000
                }
                r = requests.post("https://integrate.api.nvidia.com/v1/chat/completions", json=body, headers=headers, timeout=10)
                r.raise_for_status()
                answer = r.json()["choices"][0]["message"]["content"]
            except Exception as e:
                errors.append(f"NIM error: {e}")

        # 2. Try OpenRouter if configured
        or_key = self.env_vars.get("OPENROUTER_API_KEY")
        if not answer and or_key:
            try:
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {or_key.strip()}"
                }
                body = {
                    "model": "google/gemini-2.5-flash" if "gemini" in model.lower() else "meta-llama/llama-3.1-8b-instruct:free",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.2
                }
                r = requests.post("https://openrouter.ai/api/v1/chat/completions", json=body, headers=headers, timeout=12)
                r.raise_for_status()
                answer = r.json()["choices"][0]["message"]["content"]
            except Exception as e:
                errors.append(f"OpenRouter error: {e}")

        # 3. Fallback direct call to Ollama
        if not answer:
            try:
                headers = {"Content-Type": "application/json"}
                body = {
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.2,
                    "stream": False
                }
                ollama_endpoint = OLLAMA_CHAT
                if "100.87.214.70" in OLLAMA_CHAT:
                    ollama_endpoint = "http://127.0.0.1:11434/v1/chat/completions"
                r = requests.post(ollama_endpoint, json=body, headers=headers, timeout=15)
                r.raise_for_status()
                answer = r.json()["choices"][0]["message"]["content"]
            except Exception as e:
                errors.append(f"Ollama v1 error: {e}")
                try:
                    body = {
                        "model": "nomic-embed-text",
                        "messages": [{"role": "user", "content": prompt}],
                        "stream": False
                    }
                    r = requests.post("http://127.0.0.1:11434/api/chat", json=body, headers=headers, timeout=15)
                    r.raise_for_status()
                    answer = r.json()["message"]["content"]
                except Exception as e2:
                    errors.append(f"Ollama local error: {e2}")
                    answer = f"Error generating answer. Attempts failed: {'; '.join(errors)}"

        # Cache result
        if use_cache and answer and not answer.startswith("Error generating"):
            if self.redis_conn:
                try:
                    self.redis_conn.setex(cache_key, 3600, answer)
                except Exception:
                    pass
            else:
                self.local_cache[cache_key] = answer
                
        return answer


class KnowledgeEngine:
    def __init__(self):
        self.retriever = HybridRetriever()
        self.reranker = Reranker()
        self.llm = LLMAdapter()
        
    def ask(self, query: str, context_sources: List[str] = None, use_rag=True, max_tokens=1000) -> Dict[str, Any]:
        if not use_rag:
            answer = self.llm.generate(query)
            return {"answer": answer, "sources": []}
            
        candidates = self.retriever.retrieve(query, top_k=15)
        
        # Filter by context_sources (e.g. wildcards match like 'ec-*')
        if context_sources:
            filtered = []
            for c in candidates:
                repo_name = c.get("metadata", {}).get("repo", "")
                # Simple wildcard matching
                matched = False
                for pattern in context_sources:
                    pattern_regex = pattern.replace("*", ".*")
                    if re.match(pattern_regex, repo_name, re.IGNORECASE):
                        matched = True
                        break
                if matched:
                    filtered.append(c)
            candidates = filtered
            
        reranked = self.reranker.rerank(query, candidates)
        top_chunks = reranked[:5]
        
        if not top_chunks:
            # Fallback to direct model query if no context was found
            answer = self.llm.generate(query)
            return {"answer": answer, "sources": []}

        context = "\n---\n".join([c['text'] for c in top_chunks])
        prompt = f"""Answer the question based on the following retrieved context. 
If the context doesn't contain the answer, say so plainly.

Context:
{context}

Question: {query}
Answer:"""
        answer = self.llm.generate(prompt)
        return {
            "answer": answer,
            "sources": [c.get('metadata', {}) for c in top_chunks]
        }

if __name__ == '__main__':
    engine = KnowledgeEngine()
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        res = engine.ask(query)
        print(json.dumps(res, indent=2))
