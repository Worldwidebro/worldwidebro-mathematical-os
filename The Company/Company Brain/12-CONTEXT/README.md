# 12-CONTEXT — Agent Context Assembly

[[STARTHERE]] | [[08-KNOWLEDGE-GRAPH]] | [[_PIPELINES/retrieval]] | [[16-AGENTS]] | [[60-APIS]]

**Layer:** 12/50  
**Status:** ✅ ACTIVE  
**Authority:** [[CP-027|Infrastructure Control Plane]]  
**Updated:** 2026-09-06

---

## Overview

**KG-028: Agent Context Assembly** — Build task-specific subgraph contexts for agents.

Given an agent + focal entity, this domain:
1. Fetches the focal entity from Neo4j
2. Walks relationships N hops away
3. Filters by entity type
4. Calculates confidence scores by distance
5. Detects **risks** (dependencies, bottlenecks)
6. Detects **opportunities** (partnerships, synergies)
7. Returns complete context packet

**Result:** Every agent gets only the entities that matter to its task, dramatically reducing noise.

---

## Phase 1 Implementation

### Core Files

| File | Purpose | Status |
|------|---------|--------|
| `agent_context_builder.py` | Context assembly engine (KG-028) | ✅ COMPLETE |
| `agent_profiles.yaml` | Agent type filters + distance policies | ⏳ PLANNED |
| `_MCP/context_assembly_tool.py` | FastMCP wrapper for OmniRoute | ✅ COMPLETE |

### Endpoints

- **MCP Tool:** `build_agent_context` — Available via OmniRoute discovery
- **FastAPI:** `POST /api/graph/context` — In 60-APIS/graph_api.py
- **Auth:** Bearer token (Bitwarden "GRAPH_API_KEY")

### Example Usage

```python
context = build_agent_context(
    agent_id="AGT-001",  # Venture PM
    focal_entity_id="LT-005",  # HealthRoute Medical Courier
    depth=2,  # Walk 2 hops away
    include_types="VENTURE,REPOSITORY,CUSTOMER,CAPABILITY"
)

# Returns:
# {
#   "entities": [...],  # All connected entities with distance scores
#   "relationships": [...],  # How they're connected
#   "risks": [...],  # Detected problems (dependencies, bottlenecks)
#   "opportunities": [...],  # Detected synergies (partnerships)
#   "metadata": {...}  # Counts, timestamps
# }
```

---

## Agent Use Cases

| Agent | Use Case | Depth | Include Types |
|-------|----------|-------|---------------|
| **AGT-001** Venture PM | Project context | 2 | VENTURE, REPOSITORY, TEAM, MILESTONE |
| **AGT-002** Financial | Revenue context | 2 | VENTURE, CUSTOMER, CONTRACT, DEAL |
| **AGT-003** Technical | Tech stack context | 2 | VENTURE, REPOSITORY, TECHNOLOGY, INTEGRATION |
| **AGT-004** Sales | Deal context | 2 | VENTURE, CUSTOMER, OPPORTUNITY, COMPETITOR |
| **AGT-005** Operations | Dependency context | 3 | VENTURE, REPOSITORY, SERVICE, DEPENDENCY |

---

## Risk Detection

Automatically identifies:
- **HIGH_DEPENDENCY** — Entity depends on 5+ other entities
- **SHARED_TECH_RISK** — Single tech is shared by multiple ventures (bottleneck)
- **STALE_DATA** — Facts older than X days (when metadata available)
- **MISSING_RELATIONSHIPS** — Expected connections that don't exist

---

## Opportunity Detection

Automatically identifies:
- **CAPABILITY_SYNERGY** — Ventures share capabilities (partnership potential)
- **PARTNERSHIP** — Ventures could combine to solve customer problems
- **INTEGRATION_READY** — Tech stacks are compatible
- **COST_SHARING** — Multiple ventures could share infrastructure

---

## Integration Points

### [[08-KNOWLEDGE-GRAPH|Knowledge Graph (Neo4j)]]
- **Connection:** bolt://100.87.214.70:7687
- **Query:** Multi-hop traversal (depth 1-3)
- **Auth:** See Bitwarden "Neo4j Company Brain"

### [[_PIPELINES/retrieval|Retrieval Pipeline]]
- **Status:** Integrated with KG-017 (Hybrid Search)
- **Combined:** KG-017 finds entities, KG-028 builds context

### [[16-AGENTS|Routing Agents]]
- **Status:** All agents (AGT-001 through AGT-009) can call `/api/graph/context`
- **Pattern:** Agent calls before executing task

### [[60-APIS|API Gateway]]
- **Endpoint:** POST /api/graph/context
- **Server:** 60-APIS/graph_api.py
- **Port:** 8000 (localhost)

---

## Related Documentation

- [[PHASE_1_EXECUTION_PLAN|Phase 1 Roadmap]] — Complete timeline
- [[COMPANY_BRAIN_KG_ASSESSMENT|KG Assessment]] — 50 capabilities status
- [[08-KNOWLEDGE-GRAPH|Knowledge Graph Overview]] — Neo4j architecture
- [[_PIPELINES/retrieval|Retrieval Pipeline]] — KG-017 Hybrid Search
- [[16-AGENTS|Routing Agents]] — Agent definitions
- [[60-APIS|API Gateway]] — FastAPI endpoints
- [[_MCP|MCP Tools]] — Tool wrappers and registration

---

## Next Steps

1. ✅ Build `agent_context_builder.py` (DONE)
2. ✅ Build `_MCP/context_assembly_tool.py` wrapper (DONE)
3. ⏳ Create `agent_profiles.yaml` with agent type policies
4. ⏳ Wire to FastAPI endpoint in 60-APIS/graph_api.py
5. ⏳ Deploy with Docker
6. ⏳ Register in OmniRoute
7. ⏳ Test end-to-end with AGT-001 through AGT-009

---

**Status:** ✅ Core implementation complete | Ready for deployment  
**Authority:** [[CP-027|Infrastructure Control Plane]]  
**Next:** Deploy to OmniRoute
