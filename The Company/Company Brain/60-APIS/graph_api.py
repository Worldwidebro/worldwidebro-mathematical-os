"""
KG-048: Graph API Endpoint — FastAPI server for agent graph queries
Exposes /api/graph/* endpoints for KG-017 (Hybrid Search) and KG-028 (Context)
"""

from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
import os
from datetime import datetime

# Import capabilities from sibling modules
import sys
import os

brain_dir = "/Users/acebless/Documents/The Company/Company Brain"
sys.path.insert(0, brain_dir)
sys.path.insert(0, os.path.join(brain_dir, "12-CONTEXT"))

from _PIPELINES.retrieval.hybrid_query import HybridSearchEngine, SearchResult
from agent_context_builder import AgentContextBuilder, AgentContext


# ============================================================================
# SCHEMAS (Pydantic Models)
# ============================================================================


class QueryRequest(BaseModel):
    """Request for hybrid graph search"""

    query_text: str = Field(..., description="Search query text")
    search_type: Literal["graph", "vector", "hybrid"] = Field(
        "hybrid", description="Type of search"
    )
    limit: int = Field(10, ge=1, le=100, description="Max results")
    confidence_threshold: float = Field(
        0.5, ge=0.0, le=1.0, description="Minimum confidence score"
    )
    entity_types: Optional[List[str]] = Field(
        None, description="Filter by entity type (VENTURE, REPOSITORY, etc.)"
    )


class SearchResultResponse(BaseModel):
    """Single search result"""

    entity_id: str
    entity_type: str
    score: float
    search_type: str
    properties: dict
    distance_hops: int


class QueryResponse(BaseModel):
    """Response from hybrid search"""

    results: List[SearchResultResponse]
    count: int
    search_time_ms: float
    execution: str
    query_text: str


class ContextRequest(BaseModel):
    """Request for agent context assembly"""

    agent_id: str = Field(..., description="Agent ID (AGT-001, etc.)")
    focal_entity_id: str = Field(..., description="Primary entity ID")
    depth: int = Field(2, ge=1, le=3, description="Relationship hop depth")
    include_types: Optional[List[str]] = Field(
        None, description="Entity types to include"
    )
    exclude_types: Optional[List[str]] = Field(
        None, description="Entity types to exclude"
    )


class ContextEntityResponse(BaseModel):
    """Entity in agent context"""

    entity_id: str
    entity_type: str
    properties: dict
    distance_hops: int
    confidence_score: float


class ContextResponse(BaseModel):
    """Response from context assembly"""

    agent_id: str
    focal_entity_id: str
    focal_entity_type: str
    depth_limit: int
    entities: List[ContextEntityResponse]
    relationships: List[dict]
    risks: List[dict]
    opportunities: List[dict]
    metadata: dict


# ============================================================================
# AUTHENTICATION
# ============================================================================


def verify_api_key(authorization: Optional[str] = Header(None)) -> str:
    """
    Verify API key from Authorization header.
    Expected format: Authorization: Bearer <api_key>
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid Authorization format")

    api_key = parts[1]
    expected_key = os.getenv("GRAPH_API_KEY", "changeme")  # TODO: Load from Bitwarden

    if api_key != expected_key:
        raise HTTPException(status_code=403, detail="Invalid API key")

    return api_key


# ============================================================================
# INITIALIZE APP & SERVICES
# ============================================================================

app = FastAPI(
    title="Company Brain Graph API",
    description="KG-017/028/048: Hybrid search, context assembly, graph endpoints",
    version="1.0.0",
)

# Initialize search engine and context builder
search_engine = HybridSearchEngine()
context_builder = AgentContextBuilder()


@app.on_event("shutdown")
async def shutdown():
    """Cleanup on shutdown"""
    search_engine.close()
    context_builder.close()


# ============================================================================
# ENDPOINTS
# ============================================================================


@app.get("/health")
async def health() -> dict:
    """Health check"""
    return {
        "status": "OK",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
    }


@app.post("/api/graph/query", response_model=QueryResponse)
async def hybrid_query(
    request: QueryRequest,
    api_key: str = Depends(verify_api_key),
) -> dict:
    """
    Execute hybrid search against graph + vectors.

    Example:
    ```bash
    curl -X POST http://localhost:8000/api/graph/query \\
      -H "Authorization: Bearer $API_KEY" \\
      -H "Content-Type: application/json" \\
      -d '{
        "query_text": "medical logistics ventures",
        "search_type": "hybrid",
        "limit": 10
      }'
    ```
    """
    import time

    start_time = time.time()

    try:
        results = search_engine.hybrid_search(
            query_text=request.query_text,
            search_type=request.search_type,
            limit=request.limit,
            confidence_threshold=request.confidence_threshold,
            entity_types=request.entity_types,
        )

        elapsed_ms = (time.time() - start_time) * 1000

        return {
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
            "count": len(results),
            "search_time_ms": elapsed_ms,
            "execution": request.search_type.upper(),
            "query_text": request.query_text,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.post("/api/graph/context", response_model=ContextResponse)
async def build_context(
    request: ContextRequest,
    api_key: str = Depends(verify_api_key),
) -> dict:
    """
    Build agent-specific context by pulling relevant subgraph.

    Example:
    ```bash
    curl -X POST http://localhost:8000/api/graph/context \\
      -H "Authorization: Bearer $API_KEY" \\
      -H "Content-Type: application/json" \\
      -d '{
        "agent_id": "AGT-001",
        "focal_entity_id": "LT-005",
        "depth": 2,
        "include_types": ["VENTURE", "REPOSITORY"]
      }'
    ```
    """
    try:
        context = context_builder.build_context(
            agent_id=request.agent_id,
            focal_entity_id=request.focal_entity_id,
            depth=request.depth,
            include_types=request.include_types,
            exclude_types=request.exclude_types,
        )

        return {
            "agent_id": context.agent_id,
            "focal_entity_id": context.focal_entity_id,
            "focal_entity_type": context.focal_entity_type,
            "depth_limit": context.depth_limit,
            "entities": [
                {
                    "entity_id": e.entity_id,
                    "entity_type": e.entity_type,
                    "properties": e.properties,
                    "distance_hops": e.distance_hops,
                    "confidence_score": e.confidence_score,
                }
                for e in context.entities
            ],
            "relationships": context.relationships,
            "risks": context.risks,
            "opportunities": context.opportunities,
            "metadata": context.metadata,
        }

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Context build failed: {str(e)}")


@app.get("/api/graph/entity/{entity_id}")
async def get_entity(
    entity_id: str,
    api_key: str = Depends(verify_api_key),
) -> dict:
    """
    Fetch single entity by ID with all properties.

    Example: `GET /api/graph/entity/LT-005`
    """
    try:
        entity = context_builder._fetch_entity(entity_id)
        if not entity:
            raise HTTPException(status_code=404, detail=f"Entity not found: {entity_id}")

        return {
            "entity_id": entity.get("entity_id"),
            "entity_type": entity.get("entity_type"),
            "properties": entity.get("properties", {}),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/graph/paths/{from_id}/{to_id}")
async def find_paths(
    from_id: str,
    to_id: str,
    max_length: int = 3,
    api_key: str = Depends(verify_api_key),
) -> dict:
    """
    Find shortest paths between two entities.

    Example: `GET /api/graph/paths/LT-005/REPO-123`
    """
    cypher = f"""
    MATCH path = shortestPath((a)-[*..{max_length}]-(b))
    WHERE a.id = '{from_id}' AND b.id = '{to_id}'
    RETURN
        [node IN nodes(path) | {{id: node.id, type: node.entity_type}}] AS node_path,
        [rel IN relationships(path) | type(rel)] AS relationship_types,
        length(path) AS path_length
    LIMIT 1
    """

    try:
        with context_builder.neo4j_driver.session() as session:
            result = session.run(cypher)
            record = result.single()

            if not record:
                return {
                    "from_id": from_id,
                    "to_id": to_id,
                    "paths": [],
                    "found": False,
                }

            return {
                "from_id": from_id,
                "to_id": to_id,
                "paths": [
                    {
                        "nodes": record["node_path"],
                        "relationships": record["relationship_types"],
                        "length": record["path_length"],
                    }
                ],
                "found": True,
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# ERROR HANDLERS
# ============================================================================


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "timestamp": datetime.now().isoformat(),
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
