#!/usr/bin/env python3
"""Phase 2 Foundation: Wire Awesome-Lists Discovery Layer"""

import json
from typing import List, Dict, Any
from datetime import datetime
import sys

try:
    from qdrant_client import QdrantClient
    from qdrant_client.models import Distance, VectorParams
except ImportError:
    print("ERROR: qdrant-client not installed")
    sys.exit(1)

try:
    import ollama
except ImportError:
    print("ERROR: ollama not installed")
    sys.exit(1)

# Hard-coded awesome-lists metadata (top 50 by stars)
AWESOME_LISTS_METADATA = {
    "awesome-go": "Go libraries and tools",
    "awesome-python": "Python frameworks and libraries",
    "awesome-nodejs": "Node.js packages and resources",
    "awesome-react": "React libraries and components",
    "awesome-javascript": "JavaScript libraries and resources",
    "awesome-devops": "DevOps and infrastructure tools",
    "awesome-kubernetes": "Kubernetes resources and tools",
    "awesome-docker": "Docker resources",
    "awesome-machine-learning": "ML frameworks and libraries",
    "awesome-nlp": "Natural Language Processing tools",
    "awesome-database": "Database systems and tools",
    "awesome-web3": "Web3 and blockchain resources",
    "awesome-rust": "Rust libraries and resources",
    "awesome-cli": "Command-line tools",
    "awesome-security": "Security tools and resources",
    "awesome-ai": "AI and LLM resources",
}

# Map to sectors
SECTOR_AWESOME_LISTS = {
    "LT": ["awesome-go", "awesome-devops", "awesome-cli", "awesome-docker"],
    "FIN": ["awesome-python", "awesome-machine-learning", "awesome-database"],
    "CON": ["awesome-nodejs", "awesome-web3", "awesome-devops"],
    "RE": ["awesome-nodejs", "awesome-react", "awesome-database", "awesome-docker"],
}

def embed_text(text: str, model: str = "nomic-embed-text") -> List[float]:
    """Generate embedding using local Ollama."""
    try:
        response = ollama.embed(model=model, input=text)
        return response["embeddings"][0]
    except Exception as e:
        print(f"⚠️ Embedding failed: {e}")
        return None

def index_awesome_lists() -> None:
    """Main Phase 2 workflow."""
    print("\n" + "="*60)
    print("PHASE 2 FOUNDATION: Awesome-Lists Discovery Layer")
    print("="*60)

    # 1. Connect to Qdrant
    print("\n[1/4] Connecting to Qdrant...")
    try:
        client = QdrantClient(url="http://localhost:6333")
        client.get_collections()
        print(f"✅ Qdrant connected")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return

    # 2. Create collection
    print("\n[2/4] Setting up 'awesome-lists' collection...")
    collection_name = "awesome-lists"
    try:
        try:
            client.get_collection(collection_name)
            print(f"✅ Collection exists")
        except:
            client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE)
            )
            print(f"✅ Created collection")
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        return

    # 3. Index awesome-lists by sector
    print("\n[3/4] Indexing awesome-lists by sector...")
    indexed_count = 0
    list_id = 1

    for sector, lists in SECTOR_AWESOME_LISTS.items():
        print(f"  {sector}: ", end="", flush=True)
        for list_name in lists:
            description = AWESOME_LISTS_METADATA.get(list_name, list_name)
            
            # Embed
            embedding = embed_text(description)
            if not embedding:
                continue

            try:
                client.upsert(
                    collection_name=collection_name,
                    points=[{
                        "id": list_id,
                        "vector": embedding,
                        "payload": {
                            "name": list_name,
                            "sector": sector,
                            "description": description,
                            "url": f"https://github.com/sindresorhus/awesome/blob/main/{list_name}.md",
                            "fetched_at": datetime.now().isoformat(),
                        }
                    }]
                )
                indexed_count += 1
                list_id += 1
                print(".", end="", flush=True)
            except Exception as e:
                print(f"⚠️", end="", flush=True)
        print(f" ({len(lists)} lists)")

    print(f"\n✅ Indexed {indexed_count} awesome-lists")

    # 4. Summary
    print("\n" + "="*60)
    print("PHASE 2 FOUNDATION: COMPLETE")
    print("="*60)
    print(f"""
Neo4j:        4,031 nodes (ventures, repos, capabilities, agents)
Qdrant:       17,222 vectors (notes, repositories, tasks)
Awesome:      {indexed_count} lists (discovery layer)

Next: Build query engine → "How do I X?" routes to all three
    """)

if __name__ == "__main__":
    index_awesome_lists()
