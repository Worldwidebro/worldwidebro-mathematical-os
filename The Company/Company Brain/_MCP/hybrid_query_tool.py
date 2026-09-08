"""
KG-017 FastMCP Tool Wrapper — Expose Hybrid Search to OmniRoute
"""

import json
from fastmcp import mcp
from _PIPELINES.retrieval.hybrid_query import HybridSearchEngine

# Initialize search engine
search_engine = HybridSearchEngine()


@mcp.tool()
def hybrid_search(
    query_text: str,
    search_type: str = "hybrid",
    limit: int = 10,
    confidence_threshold: float = 0.5,
    entity_types: str = None,
) -> str:
    """
    Execute hybrid graph + vector search.

    Args:
        query_text: What to search for
        search_type: "graph", "vector", or "hybrid"
        limit: Max results
        confidence_threshold: Min score (0-1)
        entity_types: Comma-separated types to filter (VENTURE, REPOSITORY, etc.)

    Returns:
        JSON with results, count, execution type
    """
    types_list = None
    if entity_types:
        types_list = [t.strip() for t in entity_types.split(",")]

    try:
        results = search_engine.hybrid_search(
            query_text=query_text,
            search_type=search_type,
            limit=limit,
            confidence_threshold=confidence_threshold,
            entity_types=types_list,
        )

        response = {
            "success": True,
            "count": len(results),
            "results": [
                {
                    "entity_id": r.entity_id,
                    "entity_type": r.entity_type,
                    "score": r.score,
                    "search_type": r.search_type,
                    "properties": r.properties,
                    "distance_hops": r.distance_hops,
                }
                for r in results
            ],
        }

        return json.dumps(response, indent=2)

    except Exception as e:
        return json.dumps(
            {"success": False, "error": str(e)},
            indent=2,
        )


@mcp.resource("company-brain://search/doc")
def search_documentation() -> str:
    """Documentation for hybrid search capability"""
    return """
    # KG-017: Hybrid Search

    Execute combined graph + vector search against Company Brain.

    ## Queries
    - Graph search: "medical logistics ventures with active repos"
    - Vector search: "semantic similarity to venture description"
    - Hybrid: Best match from both methods combined

    ## Example
    ```python
    results = hybrid_search(
        query_text="construction software ventures",
        search_type="hybrid",
        limit=10
    )
    ```

    ## Returns
    List of entities ranked by relevance score (0-1).
    Hybrid search combines:
    - Graph matches (structure, relationships)
    - Vector matches (semantic similarity)
    - Fusion score: 60% graph + 40% vector
    """


if __name__ == "__main__":
    # Test
    print(hybrid_search("medical logistics ventures", limit=5))
