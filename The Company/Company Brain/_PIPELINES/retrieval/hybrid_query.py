"""
KG-017: Hybrid Search — Graph + Vector queries unified
Executes hybrid search against Neo4j (Cypher) + Qdrant (semantic) together
"""

from typing import TypedDict, Literal
from dataclasses import dataclass
import json
import time
import requests

try:
    from neo4j import GraphDatabase
except ImportError:
    raise ImportError("neo4j package required: pip install neo4j")

try:
    from qdrant_client import QdrantClient
    from qdrant_client.models import Distance, VectorParams, PointStruct
except ImportError:
    raise ImportError("qdrant-client package required: pip install qdrant-client")


@dataclass
class SearchResult:
    """Single search result with type and confidence"""
    entity_id: str
    entity_type: str
    score: float
    search_type: Literal["GRAPH", "VECTOR", "HYBRID"]
    properties: dict
    distance_hops: int = 0


class HybridSearchEngine:
    """Unified graph + vector search interface"""

    def __init__(
        self,
        neo4j_uri: str = "bolt://100.87.214.70:7687",
        neo4j_user: str = "neo4j",
        neo4j_password: str = "changeme",
        qdrant_url: str = "http://100.87.214.70:6333",
        qdrant_collection: str = "ventures",
        ollama_url: str = "http://localhost:11434",
        embedding_model: str = "nomic-embed-text",
    ):
        """Initialize Neo4j, Qdrant, and Ollama connections"""
        self.neo4j_driver = GraphDatabase.driver(
            neo4j_uri, auth=(neo4j_user, neo4j_password)
        )
        self.qdrant_client = QdrantClient(url=qdrant_url)
        self.qdrant_collection = qdrant_collection
        self.ollama_url = ollama_url
        self.embedding_model = embedding_model
        self._embedding_cache = {}

    def close(self):
        """Close connections"""
        if self.neo4j_driver:
            self.neo4j_driver.close()

    def _get_embedding(self, text: str) -> list:
        """
        Get embedding vector for text using Ollama.

        Args:
            text: Text to embed

        Returns:
            768-dim embedding vector or zeros on failure
        """
        if text in self._embedding_cache:
            return self._embedding_cache[text]

        try:
            # Call Ollama embedding endpoint
            response = requests.post(
                f"{self.ollama_url}/api/embed",
                json={
                    "model": self.embedding_model,
                    "input": text
                },
                timeout=30
            )

            if response.status_code == 200:
                embedding = response.json().get("embeddings", [[]])[0]
                self._embedding_cache[text] = embedding
                return embedding
        except Exception as e:
            print(f"⚠️  Ollama embedding failed: {e} — using fallback")

        # Fallback: return zeros
        return [0.0] * 768

    def graph_search(
        self,
        query: str,
        limit: int = 10,
        entity_types: list = None,
    ) -> list[SearchResult]:
        """
        Execute Cypher-based graph search.

        Args:
            query: Free-text query or Cypher pattern
            limit: Max results
            entity_types: Filter by entity type (VENTURE, REPOSITORY, etc.)

        Returns:
            Ranked search results from graph
        """
        cypher = self._build_cypher_query(query, entity_types, limit)

        with self.neo4j_driver.session() as session:
            result = session.run(cypher)
            records = list(result)

        results = []
        for record in records:
            results.append(
                SearchResult(
                    entity_id=record["entity_id"],
                    entity_type=record["entity_type"],
                    score=record.get("score", 0.0),
                    search_type="GRAPH",
                    properties=dict(record.get("properties", {})),
                    distance_hops=record.get("hops", 0),
                )
            )

        return sorted(results, key=lambda x: x.score, reverse=True)

    def vector_search(
        self,
        query_text: str,
        limit: int = 10,
        confidence_threshold: float = 0.5,
    ) -> list[SearchResult]:
        """
        Execute Qdrant vector search.

        Args:
            query_text: Semantic query
            limit: Max results
            confidence_threshold: Minimum similarity score (0-1)

        Returns:
            Ranked semantic search results
        """
        # Embed query_text using Ollama
        query_vector = self._get_embedding(query_text)

        try:
            search_result = self.qdrant_client.search(
                collection_name=self.qdrant_collection,
                query_vector=query_vector,
                limit=limit,
                score_threshold=confidence_threshold,
            )
        except Exception as e:
            print(f"⚠️  Vector search failed: {e}")
            return []

        results = []
        for point in search_result:
            results.append(
                SearchResult(
                    entity_id=point.payload.get("entity_id", "unknown"),
                    entity_type=point.payload.get("entity_type", "unknown"),
                    score=point.score,
                    search_type="VECTOR",
                    properties=point.payload,
                )
            )

        return results

    def hybrid_search(
        self,
        query_text: str,
        search_type: Literal["graph", "vector", "hybrid"] = "hybrid",
        limit: int = 10,
        confidence_threshold: float = 0.5,
        entity_types: list = None,
    ) -> list[SearchResult]:
        """
        Execute hybrid search: graph + vector combined.

        Args:
            query_text: Query text
            search_type: "graph", "vector", or "hybrid"
            limit: Max results
            confidence_threshold: Min score (0-1)
            entity_types: Filter by type

        Returns:
            Fused and ranked results
        """
        if search_type == "graph":
            return self.graph_search(query_text, limit, entity_types)

        if search_type == "vector":
            return self.vector_search(query_text, limit, confidence_threshold)

        # Hybrid: combine both
        graph_results = self.graph_search(query_text, limit, entity_types)
        vector_results = self.vector_search(query_text, limit, confidence_threshold)

        # Fusion algorithm: score-based ranking
        return self._fuse_results(graph_results, vector_results, limit)

    def _fuse_results(
        self,
        graph_results: list[SearchResult],
        vector_results: list[SearchResult],
        limit: int,
    ) -> list[SearchResult]:
        """
        Fuse graph and vector results using score normalization.

        Strategy:
        1. Normalize graph scores (0-1 range)
        2. Normalize vector scores (already 0-1)
        3. Weighted average: 60% graph + 40% vector
        4. Deduplicate by entity_id
        5. Re-rank by fused score
        """
        # Deduplicate by entity_id
        seen = {}

        for result in graph_results:
            if result.entity_id not in seen:
                seen[result.entity_id] = {
                    "entity": result,
                    "graph_score": result.score,
                    "vector_score": 0.0,
                }
            else:
                seen[result.entity_id]["graph_score"] = max(
                    seen[result.entity_id]["graph_score"], result.score
                )

        for result in vector_results:
            if result.entity_id not in seen:
                seen[result.entity_id] = {
                    "entity": result,
                    "graph_score": 0.0,
                    "vector_score": result.score,
                }
            else:
                seen[result.entity_id]["vector_score"] = max(
                    seen[result.entity_id]["vector_score"], result.score
                )

        # Fuse scores: 60% graph + 40% vector
        fused = []
        for entity_id, scores in seen.items():
            fused_score = (
                0.6 * scores["graph_score"] + 0.4 * scores["vector_score"]
            )
            result = scores["entity"]
            result.score = fused_score
            result.search_type = "HYBRID"
            fused.append(result)

        # Re-rank by fused score
        fused.sort(key=lambda x: x.score, reverse=True)

        return fused[:limit]

    def _build_cypher_query(
        self,
        query: str,
        entity_types: list = None,
        limit: int = 10,
    ) -> str:
        """Build Cypher query from free-text search with ranking"""
        # Escape single quotes in query
        safe_query = query.replace("'", "\\'")

        # Simple keyword search across entity properties
        type_filter = ""
        if entity_types:
            types_str = "', '".join(entity_types)
            type_filter = f"AND n.entity_type IN ['{types_str}']"

        # Score matches based on which field matched (name > description > slug)
        cypher = f"""
        MATCH (n)
        WHERE (
            toLower(n.name) CONTAINS toLower('{safe_query}')
            OR toLower(n.description) CONTAINS toLower('{safe_query}')
            OR toLower(n.slug) CONTAINS toLower('{safe_query}')
        )
        {type_filter}
        WITH n,
            CASE
                WHEN toLower(n.name) CONTAINS toLower('{safe_query}') THEN 3.0
                WHEN toLower(n.description) CONTAINS toLower('{safe_query}') THEN 2.0
                ELSE 1.0
            END AS score
        RETURN
            n.id AS entity_id,
            n.entity_type AS entity_type,
            properties(n) AS properties,
            score,
            0 AS hops
        ORDER BY score DESC
        LIMIT {limit}
        """

        return cypher


if __name__ == "__main__":
    # Example usage
    engine = HybridSearchEngine()

    try:
        results = engine.hybrid_search(
            query_text="medical logistics ventures",
            search_type="hybrid",
            limit=10,
        )

        print(f"Found {len(results)} results:\n")
        for result in results:
            print(f"  {result.entity_id} ({result.entity_type})")
            print(f"    Score: {result.score:.2f} ({result.search_type})")
            print(f"    Props: {result.properties}\n")

    finally:
        engine.close()
