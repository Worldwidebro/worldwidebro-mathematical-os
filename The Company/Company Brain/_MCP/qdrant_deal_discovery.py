#!/usr/bin/env python3
"""
Qdrant Semantic Deal Discovery Engine

Wire Qdrant (http://100.87.214.70:6333) for semantic deal discovery and similarity scoring.

Features:
  - Search similar companies/deals by vector embedding
  - Score deal similarity using cosine distance
  - Embed company profiles using Ollama
  - Find comparable deals for deal structuring

Collections available:
  - construction_bids: Indexed bid data
  - construction_documents: Construction project docs
  - construction_projects: Project metadata
  - knowledge_chunks: General knowledge base
"""

import json
import requests
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from math import sqrt


@dataclass
class DealMatch:
    """Result from similarity search"""
    deal_id: str
    company_name: str
    score: float
    similarity_pct: float
    context: Dict[str, Any]


class QdrantDealDiscovery:
    """Qdrant semantic search for deal discovery and similarity scoring"""

    def __init__(self, qdrant_url: str = "http://100.87.214.70:6333",
                 ollama_url: str = "http://localhost:11434"):
        self.qdrant_url = qdrant_url
        self.ollama_url = ollama_url
        self.embedding_model = "nomic-embed-text"
        self.collection_name = "construction_bids"

        # Verify Qdrant connectivity
        try:
            resp = requests.get(f"{self.qdrant_url}/collections", timeout=5)
            resp.raise_for_status()
            self.collections = {c['name'] for c in resp.json()['result']['collections']}
            print(f"✅ Qdrant online: {len(self.collections)} collections")
        except Exception as e:
            raise RuntimeError(f"❌ Qdrant unreachable: {e}")

    def embed_company_profile(self, company_data: Dict[str, Any]) -> List[float]:
        """
        Generate vector embedding for company profile using Ollama.

        Args:
            company_data: Dict with fields:
              - name: Company name
              - description: Business description
              - industry: Industry/sector
              - location: Geographic location
              - capabilities: List of services

        Returns:
            768-dim vector (nomic-embed-text)
        """
        # Construct semantic text for embedding
        parts = [
            company_data.get("name", ""),
            company_data.get("description", ""),
            company_data.get("industry", ""),
            f"Located in {company_data.get('location', '')}",
            f"Capabilities: {', '.join(company_data.get('capabilities', []))}",
        ]
        text = " ".join(p for p in parts if p).strip()

        if not text:
            raise ValueError("Company data missing required fields for embedding")

        try:
            resp = requests.post(
                f"{self.ollama_url}/api/embed",
                json={"model": self.embedding_model, "input": text},
                timeout=30
            )
            resp.raise_for_status()
            data = resp.json()
            embedding = data.get("embeddings", [[]])[0]

            if not embedding:
                raise ValueError("Empty embedding returned from Ollama")

            return embedding
        except Exception as e:
            raise RuntimeError(f"Embedding failed: {e}")

    def search_similar_companies(self,
                                company_vector: List[float],
                                limit: int = 10,
                                score_threshold: float = 0.5) -> List[DealMatch]:
        """
        Search for similar companies/deals by vector similarity.

        Args:
            company_vector: 768-dim embedding from embed_company_profile()
            limit: Max results to return
            score_threshold: Min similarity score (0-1)

        Returns:
            List of DealMatch objects ranked by similarity
        """
        try:
            resp = requests.post(
                f"{self.qdrant_url}/collections/{self.collection_name}/points/search",
                json={
                    "vector": company_vector,
                    "limit": limit,
                    "score_threshold": score_threshold,
                    "with_payload": True
                },
                timeout=10
            )
            resp.raise_for_status()
            data = resp.json()

            matches = []
            for result in data.get("result", []):
                score = result.get("score", 0)
                similarity_pct = round(max(0, score) * 100, 1)

                payload = result.get("payload", {})
                match = DealMatch(
                    deal_id=result.get("id", "unknown"),
                    company_name=payload.get("company_name", "Unknown"),
                    score=score,
                    similarity_pct=similarity_pct,
                    context={
                        "industry": payload.get("industry"),
                        "location": payload.get("location"),
                        "deal_size": payload.get("deal_size"),
                        "deal_type": payload.get("deal_type"),
                        "created": payload.get("created_at"),
                    }
                )
                matches.append(match)

            return matches
        except Exception as e:
            raise RuntimeError(f"Search failed: {e}")

    def score_deal_similarity(self,
                             deal_a_id: str,
                             deal_b_id: str) -> Dict[str, Any]:
        """
        Calculate similarity score between two deals using cosine distance.

        Args:
            deal_a_id: First deal point ID in Qdrant
            deal_b_id: Second deal point ID in Qdrant

        Returns:
            Dict with:
              - similarity_score: 0-1 (1 = identical)
              - similarity_pct: 0-100
              - interpretation: Human readable
              - deal_a: Deal A metadata
              - deal_b: Deal B metadata
        """
        try:
            # Fetch both points with their vectors
            resp_a = requests.post(
                f"{self.qdrant_url}/collections/{self.collection_name}/points",
                json={"ids": [deal_a_id], "with_vectors": True},
                timeout=10
            )
            resp_a.raise_for_status()
            points_a = resp_a.json().get("result", [])

            resp_b = requests.post(
                f"{self.qdrant_url}/collections/{self.collection_name}/points",
                json={"ids": [deal_b_id], "with_vectors": True},
                timeout=10
            )
            resp_b.raise_for_status()
            points_b = resp_b.json().get("result", [])

            if not points_a or not points_b:
                return {
                    "error": "One or both deals not found",
                    "deal_a_id": deal_a_id,
                    "deal_b_id": deal_b_id
                }

            vec_a = points_a[0].get("vector", [])
            vec_b = points_b[0].get("vector", [])

            if not vec_a or not vec_b or len(vec_a) != len(vec_b):
                return {"error": "Vector mismatch or missing vectors"}

            # Cosine similarity
            dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
            mag_a = sqrt(sum(x**2 for x in vec_a))
            mag_b = sqrt(sum(x**2 for x in vec_b))

            if mag_a == 0 or mag_b == 0:
                similarity = 0
            else:
                similarity = dot_product / (mag_a * mag_b)

            # Clamp to [0, 1]
            similarity = max(0, min(1, similarity))
            similarity_pct = round(similarity * 100, 1)

            # Interpretation
            if similarity >= 0.9:
                interpretation = "Nearly identical"
            elif similarity >= 0.75:
                interpretation = "Very similar (strong comparables)"
            elif similarity >= 0.6:
                interpretation = "Similar (fair comparables)"
            elif similarity >= 0.4:
                interpretation = "Moderately similar"
            else:
                interpretation = "Dissimilar"

            return {
                "similarity_score": round(similarity, 4),
                "similarity_pct": similarity_pct,
                "interpretation": interpretation,
                "deal_a": {
                    "id": deal_a_id,
                    "company": points_a[0].get("payload", {}).get("company_name"),
                    "deal_type": points_a[0].get("payload", {}).get("deal_type")
                },
                "deal_b": {
                    "id": deal_b_id,
                    "company": points_b[0].get("payload", {}).get("company_name"),
                    "deal_type": points_b[0].get("payload", {}).get("deal_type")
                }
            }
        except Exception as e:
            return {"error": f"Scoring failed: {e}"}

    def search_by_text(self,
                      query_text: str,
                      limit: int = 10,
                      score_threshold: float = 0.5) -> List[DealMatch]:
        """
        Search deals by text query (auto-embeds).

        Args:
            query_text: Natural language search (e.g., "construction companies in Texas")
            limit: Max results
            score_threshold: Min similarity

        Returns:
            List of DealMatch results
        """
        # Embed the query
        try:
            resp = requests.post(
                f"{self.ollama_url}/api/embed",
                json={"model": self.embedding_model, "input": query_text},
                timeout=30
            )
            resp.raise_for_status()
            query_vector = resp.json().get("embeddings", [[]])[0]
        except Exception as e:
            raise RuntimeError(f"Query embedding failed: {e}")

        # Search with embedded query
        return self.search_similar_companies(query_vector, limit, score_threshold)


# ============================================================================
# MCP Tool Exports (for fastmcp_server.py integration)
# ============================================================================

def get_qdrant_client():
    """Factory for Qdrant client (singleton-like)"""
    global _qdrant_client
    if '_qdrant_client' not in globals():
        _qdrant_client = QdrantDealDiscovery()
    return _qdrant_client


if __name__ == "__main__":
    # Example usage
    print("🔍 Qdrant Deal Discovery - Local Test")
    print("=" * 60)

    try:
        client = QdrantDealDiscovery()

        # Test 1: Embed company profile
        print("\n1️⃣  Embedding company profile...")
        company = {
            "name": "BuildCorp Construction",
            "description": "Heavy civil construction specializing in bridges and highways",
            "industry": "Civil Engineering & Construction",
            "location": "Austin, Texas",
            "capabilities": ["bridge construction", "highway design", "project management"]
        }
        embedding = client.embed_company_profile(company)
        print(f"   ✅ Generated {len(embedding)}-dim embedding")

        # Test 2: Search for similar companies
        print("\n2️⃣  Searching for similar companies...")
        matches = client.search_similar_companies(embedding, limit=5)
        print(f"   ✅ Found {len(matches)} similar deals:")
        for m in matches:
            print(f"      - {m.company_name}: {m.similarity_pct}% match (ID: {m.deal_id})")

        # Test 3: Score deal similarity (if data exists)
        if len(matches) >= 2:
            print("\n3️⃣  Scoring deal similarity...")
            score = client.score_deal_similarity(matches[0].deal_id, matches[1].deal_id)
            print(f"   ✅ {score.get('interpretation', 'Unknown')}: {score.get('similarity_pct', 0)}%")

        print("\n✅ All tests passed!")

    except Exception as e:
        print(f"\n❌ Error: {e}")
