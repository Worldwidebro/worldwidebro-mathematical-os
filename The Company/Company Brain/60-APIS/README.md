# 60-APIS — Graph API Endpoint

[[STARTHERE]] | [[08-KNOWLEDGE-GRAPH]] | [[_PIPELINES/retrieval]] | [[12-CONTEXT]] | [[16-AGENTS]]

**Layer:** 60/50  
**Status:** ✅ ACTIVE  
**Authority:** [[CP-027|Infrastructure Control Plane]]  
**Updated:** 2026-09-06

---

## Overview

**KG-048: Graph API Endpoint** — FastAPI server exposing all graph queries to agents.

This domain hosts the production Graph API that agents call to:
- Execute hybrid search (KG-017)
- Build context (KG-028)
- Fetch entities
- Find paths between entities
- Get health status

**Language:** Python (FastAPI)  
**Port:** 8000  
**Auth:** Bearer token (Bitwarden "GRAPH_API_KEY")  
**Database:** Neo4j + Qdrant

---

## Phase 1 Implementation

### Core Files

| File | Purpose | Status |
|------|---------|--------|
| `graph_api.py` | FastAPI server with all endpoints | ✅ COMPLETE |
| `schemas.py` | Pydantic request/response models | ⏳ PLANNED |
| `auth.py` | API key validation | ⏳ PLANNED |
| `docker-compose.yml` | Container specification | ⏳ PLANNED |
| `README.md` | This file | ✅ UPDATED |

---

## API Endpoints

### Health Check
```bash
GET /health
```

Response:
```json
{
  "status": "OK",
  "timestamp": "2026-09-06T12:00:00",
  "version": "1.0.0"
}
```

---

### 1. Hybrid Search (KG-017)

```bash
POST /api/graph/query
Authorization: Bearer $GRAPH_API_KEY
Content-Type: application/json
```

Request:
```json
{
  "query_text": "medical logistics ventures with active repos",
  "search_type": "hybrid",
  "limit": 10,
  "confidence_threshold": 0.5,
  "entity_types": ["VENTURE", "REPOSITORY"]
}
```

Response:
```json
{
  "results": [
    {
      "entity_id": "LT-005",
      "entity_type": "VENTURE",
      "score": 0.95,
      "search_type": "HYBRID",
      "properties": { "name": "HealthRoute Medical Courier", ... },
      "distance_hops": 0
    },
    ...
  ],
  "count": 10,
  "search_time_ms": 234,
  "execution": "HYBRID",
  "query_text": "medical logistics ventures with active repos"
}
```

---

### 2. Agent Context (KG-028)

```bash
POST /api/graph/context
Authorization: Bearer $GRAPH_API_KEY
Content-Type: application/json
```

Request:
```json
{
  "agent_id": "AGT-001",
  "focal_entity_id": "LT-005",
  "depth": 2,
  "include_types": ["VENTURE", "REPOSITORY", "CUSTOMER"],
  "exclude_types": null
}
```

Response:
```json
{
  "agent_id": "AGT-001",
  "focal_entity_id": "LT-005",
  "focal_entity_type": "VENTURE",
  "depth_limit": 2,
  "entities": [
    {
      "entity_id": "REPO-123",
      "entity_type": "REPOSITORY",
      "distance_hops": 1,
      "confidence_score": 0.87,
      "properties": { ... }
    },
    ...
  ],
  "relationships": [
    {
      "from_id": "LT-005",
      "to_id": "REPO-123",
      "type": "OWNS",
      "properties": { ... }
    },
    ...
  ],
  "risks": [
    {
      "type": "HIGH_DEPENDENCY",
      "severity": "MEDIUM",
      "description": "LT-005 has 7 dependencies",
      "entities_affected": [...]
    }
  ],
  "opportunities": [
    {
      "type": "CAPABILITY_SYNERGY",
      "potential": "HIGH",
      "description": "Ventures share capabilities: Python, PostgreSQL, React",
      "entities_affected": [...]
    }
  ],
  "metadata": {
    "query_timestamp": "2026-09-06T12:00:00",
    "entity_count": 15,
    "relationship_count": 22,
    "risk_count": 2,
    "opportunity_count": 3
  }
}
```

---

### 3. Fetch Entity

```bash
GET /api/graph/entity/LT-005
Authorization: Bearer $GRAPH_API_KEY
```

Response:
```json
{
  "entity_id": "LT-005",
  "entity_type": "VENTURE",
  "properties": {
    "name": "HealthRoute Medical Courier",
    "sector": "LT",
    "stage": "MVP",
    "revenue_mRR": 12500,
    ...
  }
}
```

---

### 4. Find Paths

```bash
GET /api/graph/paths/LT-005/REPO-123?max_length=3
Authorization: Bearer $GRAPH_API_KEY
```

Response:
```json
{
  "from_id": "LT-005",
  "to_id": "REPO-123",
  "found": true,
  "paths": [
    {
      "nodes": [
        { "id": "LT-005", "type": "VENTURE" },
        { "id": "REPO-123", "type": "REPOSITORY" }
      ],
      "relationships": ["OWNS"],
      "length": 1
    }
  ]
}
```

---

## Authentication

All endpoints require an API key in the `Authorization` header:

```bash
Authorization: Bearer $GRAPH_API_KEY
```

**API Key Location:**
- Bitwarden item: "GRAPH_API_KEY"
- Environment variable: `GRAPH_API_KEY` (in Docker deployment)

**Default (development):**
```
GRAPH_API_KEY=changeme
```

**Rotate before production.** See [[27-SECURITY|Security Control Plane]].

---

## Infrastructure

### Dependencies

| Component | Address | Status |
|-----------|---------|--------|
| **Neo4j** | bolt://100.87.214.70:7687 | ✅ LIVE |
| **Qdrant** | http://100.87.214.70:6333 | ✅ LIVE |

### Requirements

```
fastapi
uvicorn
pydantic
neo4j
qdrant-client
python-dotenv
```

### Installation

```bash
pip install -r requirements.txt
python 60-APIS/graph_api.py
```

Server starts on `http://localhost:8000`

### Docker

```bash
docker build -t company-brain-graph-api .
docker run -e GRAPH_API_KEY=$GRAPH_API_KEY -p 8000:8000 company-brain-graph-api
```

---

## Integration

### With OmniRoute

The FastAPI endpoints are exposed via MCP tools:
- `_MCP/hybrid_query_tool.py` — KG-017 wrapper
- `_MCP/context_assembly_tool.py` — KG-028 wrapper

**Discovery:**
```bash
curl http://localhost:20128/tools
```

### With Agents

All agents (AGT-001 through AGT-009) can call:

```python
# Via FastAPI directly
import requests

response = requests.post(
    "http://localhost:8000/api/graph/query",
    json={"query_text": "..."},
    headers={"Authorization": f"Bearer {API_KEY}"}
)

# Or via OmniRoute MCP tool
result = omniroute.call_tool("hybrid_search", query_text="...")
```

---

## Monitoring

### Logs

```bash
# FastAPI logs to stdout
tail -f /var/log/graph_api.log
```

### Performance

Track via [[_MEMORY/observability|Langfuse]] or [[_DOCS/monitoring|OpenObserve]]:
- Query latency (P50, P95, P99)
- Token usage (Neo4j + Qdrant)
- Error rate by endpoint

### Health

```bash
curl http://localhost:8000/health
```

---

## Testing

### Manual

```bash
# Hybrid search
curl -X POST http://localhost:8000/api/graph/query \
  -H "Authorization: Bearer changeme" \
  -H "Content-Type: application/json" \
  -d '{
    "query_text": "medical logistics ventures",
    "search_type": "hybrid",
    "limit": 5
  }'

# Agent context
curl -X POST http://localhost:8000/api/graph/context \
  -H "Authorization: Bearer changeme" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "AGT-001",
    "focal_entity_id": "LT-005",
    "depth": 2
  }'
```

### Automated

See `tests/` directory for pytest suite (TBD).

---

## Related Documentation

- [[PHASE_1_EXECUTION_PLAN|Phase 1 Roadmap]] — Complete timeline
- [[COMPANY_BRAIN_KG_ASSESSMENT|KG Assessment]] — 50 capabilities status
- [[08-KNOWLEDGE-GRAPH|Knowledge Graph]] — Neo4j architecture
- [[_PIPELINES/retrieval|Retrieval Pipeline]] — KG-017 Hybrid Search
- [[12-CONTEXT|Context Assembly]] — KG-028 details
- [[16-AGENTS|Routing Agents]] — Agent definitions
- [[_MCP|MCP Tools]] — Tool wrappers and registration
- [[27-SECURITY|Security Control Plane]] — Auth & credentials

---

**Status:** ✅ Core implementation complete | Ready for deployment  
**Next:** Deploy to Docker, register in OmniRoute, test with agents  
**Authority:** [[CP-027|Infrastructure Control Plane]]  
**Updated:** 2026-09-06
