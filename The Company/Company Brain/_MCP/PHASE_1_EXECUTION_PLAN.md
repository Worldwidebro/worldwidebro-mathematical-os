---
id: PHASE-1-EXECUTION-001
title: KG Phase 1 Execution Plan — Agent Enablement
scope: Next 2 weeks (Agent Context, Hybrid Search, API Endpoint)
authority: CP-027 (Infrastructure) + CP-008 (Graph Architecture)
updated: 2026-09-06
status: ACTIVE
---

# Phase 1 Execution Plan — Agent Enablement

[[STARTHERE]] | [[FILE_FORMAT_REGISTRY]] | [[FILE_CONVERSION_SERVICE]] | [[_REGISTRIES/CANONICAL/NAVIGATION_ALIASES.yaml|NAVIGATION_ALIASES]]

**Goal:** Enable agents to query Company Brain intelligently (graph + semantic).

**Timeline:** 2 weeks (Sep 6 - Sep 19)

---

## STATE OF THE CODE (What Exists)

### ✅ Folder Structure in Place

```
12-CONTEXT/
  └── README.md (skeleton, needs implementation)

11-INDEXING/
  ├── README.md (skeleton)
  ├── phase2-query-engine.py (PARTIAL: Neo4j + Qdrant + Awesome, not complete)
  └── phase2-awesome-lists-indexer.py

60-APIS/
  ├── 60-APIS.md (skeleton gateway)
  └── README.md (skeleton)

_PIPELINES/
  ├── retrieval/ (skeleton README only)
  ├── indexing/ (skeleton README only)
  ├── reasoning/ (skeleton README only)
  └── [9 other pipeline folders, mostly stubs]
```

### ❌ What's MISSING

| Capability | Status | Location | Need |
|-----------|--------|----------|------|
| **KG-028: Agent Context Assembly** | ❌ MISSING | 12-CONTEXT/ | Service to build |
| **KG-017: Hybrid Search** | 🟡 PARTIAL | 11-INDEXING/phase2-query-engine.py | Needs completion + FastMCP wrapper |
| **KG-048: API Endpoint** | ❌ MISSING | 60-APIS/ | FastAPI server to build |

---

## PHASE 1 TASKS (3 CAPABILITIES)

### TASK 1: KG-017 — Hybrid Search (GRAPH + VECTOR)

**File:** `_PIPELINES/retrieval/hybrid_query.py`

**What to build:**
- Unified query interface accepting: `query_text`, `search_type` (graph/vector/hybrid), `limit`, `confidence_threshold`
- Neo4j Cypher execution layer
- Qdrant vector search layer
- Result fusion + ranking algorithm
- MCP tool wrapper

**Depends on:**
- Neo4j (civos_neo4j, bolt://100.87.214.70:7687) ✅ LIVE
- Qdrant (http://100.87.214.70:6333) ✅ LIVE
- FastMCP server framework ✅ INSTALLED

**Existing code to reference:**
- `11-INDEXING/phase2-query-engine.py` (partial implementation)

**Example:**
```python
# Hybrid query example
results = hybrid_query(
    query_text="medical courier dispatch software",
    search_type="hybrid",  # graph + vector combined
    limit=10
)

# Returns:
# [
#   {venture_id: "LT-005", score: 0.95, type: "GRAPH_MATCH"},
#   {venture_id: "LT-011", score: 0.87, type: "VECTOR_MATCH"},
#   ...
# ]
```

**Files to create/modify:**
- `_PIPELINES/retrieval/hybrid_query.py` (NEW)
- `_PIPELINES/retrieval/cypher_patterns.yaml` (NEW - common queries)
- `_PIPELINES/retrieval/fusion_algorithm.py` (NEW - rank/merge results)
- `_MCP/hybrid_query_tool.py` (NEW - FastMCP wrapper)

---

### TASK 2: KG-028 — Agent Context Assembly

**File:** `12-CONTEXT/agent_context_builder.py`

**What to build:**
- Function to pull **relevant subgraph** for a specific agent
- Given agent type + task context → return graph neighborhood
- Filter by distance (1-hop, 2-hop, 3-hop)
- Include entity properties, relationships, and confidence scores

**Depends on:**
- Neo4j (for graph traversal)
- Existing ontology (entity types, relationship types)

**Example:**
```python
# Agent context example
context = build_agent_context(
    agent_id="agent-staffing-001",
    focus_entity="OPS-001",  # Staffing venture
    depth=2,  # How many relationship hops
    include_types=["VENTURE", "CUSTOMER", "CONTRACT", "CAPABILITY"]
)

# Returns:
# {
#   "focal_venture": {...},
#   "customers": [...],
#   "capabilities": [...],
#   "risks": [...],
#   "opportunities": [...],
#   "relationships": [...]
# }
```

**Files to create/modify:**
- `12-CONTEXT/agent_context_builder.py` (NEW)
- `12-CONTEXT/agent_profiles.yaml` (NEW - which entities matter to which agents)
- `12-CONTEXT/distance_policies.yaml` (NEW - what distance = useful vs noise)
- `_MCP/context_assembly_tool.py` (NEW - FastMCP wrapper)

---

### TASK 3: KG-048 — Graph API Endpoint

**File:** `60-APIS/graph_api.py`

**What to build:**
- FastAPI server exposing graph queries
- Standard endpoints for agents to call
- Request validation + response schema
- Error handling + logging
- Authentication (via API key in Bitwarden)

**Endpoints to expose:**
```
POST /api/graph/query
  → Execute hybrid search (KG-017)

POST /api/graph/entity/{entity_id}
  → Fetch single entity + properties

POST /api/graph/context
  → Build agent context (KG-028)

GET /api/graph/relationships/{from_id}/{to_id}
  → Find paths between two entities

POST /api/graph/impact
  → Blast-radius analysis (KG-020, phase 2)
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/graph/query \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query_text": "ventures with active repos",
    "search_type": "hybrid",
    "limit": 10
  }'

# Returns:
# {
#   "results": [...],
#   "count": 10,
#   "search_time_ms": 234,
#   "execution": "GRAPH_VECTOR_FUSION"
# }
```

**Files to create/modify:**
- `60-APIS/graph_api.py` (NEW - FastAPI server)
- `60-APIS/schemas.py` (NEW - Pydantic models)
- `60-APIS/auth.py` (NEW - API key validation)
- `60-APIS/docker-compose.yml` (NEW - container spec)
- `60-APIS/README.md` (UPDATE with endpoints)

---

## INTEGRATION: OMNIROUTE EXPOSURE

All three Phase 1 capabilities should be exposed **via OmniRoute** as MCP tools:

```
OmniRoute (localhost:20128)
    ↓
FastMCP Tools
    ├── /api/graph/query (KG-017)
    ├── /api/graph/context (KG-028)
    └── /api/graph/endpoint (KG-048)
    ↓
Claude Code Agents
    ↓
Company Brain Queries
```

**MCP tool wrappers to create:**
- `_MCP/hybrid_query_tool.py` (KG-017)
- `_MCP/context_assembly_tool.py` (KG-028)
- `_MCP/graph_api_client.py` (KG-048 wrapper for agents)

---

## IMPLEMENTATION SEQUENCE

### Week 1 (Sep 6-12)

**Day 1-2: Hybrid Search (KG-017)**
1. Complete `_PIPELINES/retrieval/hybrid_query.py`
2. Write Cypher query patterns (`cypher_patterns.yaml`)
3. Implement result fusion algorithm
4. Test against live Neo4j + Qdrant

**Day 3-4: Agent Context (KG-028)**
1. Design agent profiles (which entities matter to which agents)
2. Implement graph traversal for context building
3. Add distance policies (1/2/3-hop filtering)
4. Test with sample agents (Staffing, Medical Courier, etc.)

**Day 5: API Endpoint (KG-048) - Part 1**
1. Create FastAPI server skeleton
2. Wire endpoints to KG-017 + KG-028
3. Add authentication layer
4. Deploy locally

### Week 2 (Sep 13-19)

**Day 1-2: Testing & Integration**
1. E2E tests for all three capabilities
2. MCP tool wrappers for OmniRoute exposure
3. Performance profiling (query latency)

**Day 3-4: Documentation & Rollout**
1. API documentation (swagger/openapi)
2. Agent integration guide
3. Example queries for agents
4. Deployment to Mac Studio + OmniRoute

**Day 5: Polish & Observation**
1. Fix any bugs from early use
2. Set up monitoring (Langfuse/OpenObserve)
3. Ready for Phase 2

---

## DEPENDENCIES & ASSUMPTIONS

### Must-Have
- ✅ Neo4j live and healthy (civos_neo4j)
- ✅ Qdrant live and indexed (17,236 vectors)
- ✅ OmniRoute daemon running (localhost:20128)
- ✅ FastMCP installed in venv
- ⚠️ PostgreSQL for audit logging (conversion_audit table exists)

### Nice-to-Have (Phase 2)
- Langfuse for tracing graph queries
- OpenObserve for performance monitoring
- Redis caching for frequent queries

---

## SUCCESS CRITERIA

### KG-017: Hybrid Search ✅
- Can query "medical logistics ventures with active repos"
- Returns results ranked by relevance (graph + vector)
- Latency < 500ms for typical queries

### KG-028: Agent Context ✅
- Can call `build_agent_context(agent_id="X", entity_id="Y")`
- Returns relevant subgraph (entities, relationships, confidence scores)
- No orphaned or irrelevant entities in context

### KG-048: API Endpoint ✅
- `/api/graph/query` accessible and responds correctly
- `/api/graph/context` builds agent-specific subgraphs
- API key auth working
- Errors handled gracefully
- Documented and discoverable by agents

---

## ROLLBACK PLAN

If Phase 1 doesn't work:
1. Keep old query methods (`11-INDEXING/phase2-query-engine.py`)
2. Fall back to manual Cypher queries
3. Don't break existing agent workflows
4. Iterate on Phase 1 design before Phase 2

---

## PHASE 2 PREVIEW (Weeks 4+)

Once Phase 1 is solid:
- **KG-019-021:** Dependency analysis + blast radius
- **KG-022/046:** Change detection + propagation
- **KG-032:** Financial intelligence (revenue, contracts)
- **KG-030:** Opportunity discovery (pattern matching)

---

## FILES TO CREATE/MODIFY (Master List)

| File | Type | Status | Owner |
|------|------|--------|-------|
| `_PIPELINES/retrieval/hybrid_query.py` | NEW | TODO | Engineer |
| `_PIPELINES/retrieval/cypher_patterns.yaml` | NEW | TODO | Architect |
| `_PIPELINES/retrieval/fusion_algorithm.py` | NEW | TODO | Engineer |
| `12-CONTEXT/agent_context_builder.py` | NEW | TODO | Engineer |
| `12-CONTEXT/agent_profiles.yaml` | NEW | TODO | Architect |
| `60-APIS/graph_api.py` | NEW | TODO | Engineer |
| `60-APIS/schemas.py` | NEW | TODO | Engineer |
| `60-APIS/auth.py` | NEW | TODO | Engineer |
| `_MCP/hybrid_query_tool.py` | NEW | TODO | Engineer |
| `_MCP/context_assembly_tool.py` | NEW | TODO | Engineer |
| `11-INDEXING/README.md` | UPDATE | TODO | Architect |
| `12-CONTEXT/README.md` | UPDATE | TODO | Architect |
| `60-APIS/README.md` | UPDATE | TODO | Architect |

---

**Status:** ✅ READY TO BUILD | **Authority:** CP-027 | **Next:** Start with KG-017 (Hybrid Search)
