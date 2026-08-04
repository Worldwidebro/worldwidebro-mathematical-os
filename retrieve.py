#!/usr/bin/env python3
import sys
import json
import urllib.request
import urllib.error
from qdrant_client import QdrantClient

OLLAMA_URL = "http://127.0.0.1:11434/api/embeddings"
QDRANT_URL = "http://127.0.0.1:6333"
COLLECTION_NAME = "repositories"

class RetrievalResult(list):
    """
    Subclass of list that allows dictionary-style access to 'repos' key.
    This satisfies both:
      1. results = retrieve("query") -> len(results), results[:3] (list format)
      2. bundle = retrieve(trigger) -> bundle["repos"] (dictionary format)
    """
    def __getitem__(self, item):
        if item == "repos":
            return self
        return super().__getitem__(item)

def get_embedding(text: str) -> list:
    try:
        data = json.dumps({
            "model": "nomic-embed-text",
            "prompt": text
        }).encode("utf-8")
        
        req = urllib.request.Request(
            OLLAMA_URL,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data.get("embedding", [])
    except Exception as e:
        print(f"⚠️ Error generating embedding: {e}", file=sys.stderr)
        return []

def retrieve(query: str, k: int = 5) -> RetrievalResult:
    # 1. Generate embedding
    vector = get_embedding(query)
    if not vector:
        return RetrievalResult()

    # 2. Search Qdrant via query_points
    try:
        client = QdrantClient(url=QDRANT_URL, check_compatibility=False)
        response = client.query_points(
            collection_name=COLLECTION_NAME,
            query=vector,
            limit=k
        )
        
        # 3. Format results
        repos = []
        for hit in response.points:
            payload = hit.payload or {}
            # Ensure name exists
            repo_name = payload.get("name") or payload.get("repo_name") or "unknown"
            repos.append({
                "name": repo_name,
                "url": payload.get("url") or "",
                "purpose": payload.get("purpose") or "",
                "completion_percent": payload.get("reusability_score") or 0,
                "score": hit.score
            })
            
        return RetrievalResult(repos)
    except Exception as e:
        print(f"⚠️ Qdrant search error: {e}", file=sys.stderr)
        return RetrievalResult()

if __name__ == "__main__":
    # If run as script, perform test query
    query_str = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "FastAPI service patterns"
    print(f"Searching for: '{query_str}'...")
    results = retrieve(query_str)
    print(f"Found {len(results)} repos:")
    for i, r in enumerate(results, 1):
        print(f"  {i}. {r['name']} (score: {r['score']:.4f}) - {r['purpose']}")
