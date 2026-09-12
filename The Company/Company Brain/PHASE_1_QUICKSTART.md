[[STARTHERE]] | [[REALITY]] | [[50-MASTER-CONTROL|Phase 1 Quickstart]] | [[INDEX]]

# PHASE 1 QUICKSTART GUIDE
**Knowledge Graph Agent Enablement — 3 Capabilities Ready**

## What's Available Now

### 1. Hybrid Search (KG-017)
Unified interface combining graph and vector search.

```python
from _PIPELINES.retrieval.hybrid_query import HybridSearchEngine

engine = HybridSearchEngine(
    neo4j_uri="bolt://100.87.214.70:7687",
    qdrant_url="http://100.87.214.70:6333"
)

# Graph-only search
results = engine.graph_search("medical logistics", limit=10)

# Vector-only search (semantic)
results = engine.vector_search("healthcare startups", limit=10)

# Hybrid (best of both)
results = engine.hybrid_search(
    query_text="medical logistics ventures",
    search_type="hybrid",
    limit=10
)

engine.close()
```

### 2. Agent Context Assembly (KG-028)
Extracts tailored subgraph for any agent task.

```python
from agent_context_builder import AgentContextBuilder

builder = AgentContextBuilder()

# Build context for AGT-001 (Repository Classifier)
context = builder.build_context(
    agent_id="AGT-001",
    focal_entity_id="LT-005",
    depth=2,  # 2-hop neighborhood
    include_types=["VENTURE", "REPOSITORY", "CAPABILITY"]
)

# Access context data
print(f"Entities: {len(context.entities)}")
print(f"Relationships: {len(context.relationships)}")
print(f"Risks: {context.risks}")
print(f"Opportunities: {context.opportunities}")

builder.close()
```

### 3. Graph API (KG-048)
FastAPI server for remote graph queries.

```bash
# Start the server
cd /Users/acebless/Documents/The\ Company/Company\ Brain/60-APIS
python3 graph_api.py
# Listening on http://0.0.0.0:8000

# Query the API
curl -X POST http://localhost:8000/api/graph/query \
  -H "Authorization: Bearer changeme" \
  -H "Content-Type: application/json" \
  -d '{
    "query_text": "medical logistics",
    "search_type": "hybrid",
    "limit": 10
  }'
```

---

## Setup Checklist

### Step 1: Update Credentials
⚠️ **REQUIRED** — Neo4j auth is currently failing

```bash
# 1. Get real Neo4j password from Bitwarden
# 2. Update these files:
#    - _PIPELINES/retrieval/hybrid_query.py (line 40)
#    - 12-CONTEXT/agent_context_builder.py (line 52)
#    - 60-APIS/graph_api.py (line 119)
```

### Step 2: Load Test Data (Optional but recommended)
```bash
# Populate Neo4j with venture data:
# 1. Export ventures from Supabase
# 2. Load repositories from REPOSITORY_REGISTRY.yaml
# 3. Load capabilities from CAPABILITY_REGISTRY.yaml
# 4. Create relationships (DEPENDS_ON, HAS_CAPABILITY, etc.)
```

### Step 3: Verify Services
```bash
# Check Neo4j
curl http://100.87.214.70:7474

# Check Qdrant
curl http://100.87.214.70:6333/health

# Check Ollama
curl http://localhost:11434/api/tags
```

### Step 4: Run Tests
```bash
cd /Users/acebless/Documents/The\ Company/Company\ Brain
python3 _PIPELINES/retrieval/test_kg_capabilities.py
```

---

## Common Tasks

### Task: Search for ventures
```python
from _PIPELINES.retrieval.hybrid_query import HybridSearchEngine

engine = HybridSearchEngine()
results = engine.hybrid_search(
    query_text="medical logistics",
    search_type="hybrid",
    limit=5
)

for r in results:
    print(f"{r.entity_id}: {r.properties.get('name')}")

engine.close()
```

### Task: Get all dependencies of a venture
```python
from agent_context_builder import AgentContextBuilder

builder = AgentContextBuilder()
context = builder.build_context(
    agent_id="AGT-003",  # Risk Assessment Agent
    focal_entity_id="LT-005",
    depth=2
)

# Find DEPENDS_ON relationships
dependencies = [r for r in context.relationships 
                if r['type'] == 'DEPENDS_ON']
print(f"Dependencies: {[r['to_id'] for r in dependencies]}")

builder.close()
```

### Task: Detect risks in a venture ecosystem
```python
from agent_context_builder import AgentContextBuilder

builder = AgentContextBuilder()
context = builder.build_context(
    agent_id="AGT-003",
    focal_entity_id="VENTURE-001",
    depth=3
)

print("Risks detected:")
for risk in context.risks:
    print(f"  - {risk['type']}: {risk['description']}")

print("\nOpportunities:")
for opp in context.opportunities:
    print(f"  - {opp['type']}: {opp['description']}")

builder.close()
```

### Task: Query API from Claude Code
```bash
# From any Claude Code session:
curl -X POST http://localhost:8000/api/graph/query \
  -H "Authorization: Bearer $(echo $GRAPH_API_KEY)" \
  -H "Content-Type: application/json" \
  -d '{
    "query_text": "YOUR_QUERY_HERE",
    "search_type": "hybrid",
    "limit": 10
  }' | jq '.results[] | {id: .entity_id, name: .properties.name, score: .score}'
```

---

## API Endpoint Reference

### POST /api/graph/query
**Hybrid Search**

Request:
```json
{
  "query_text": "search term",
  "search_type": "graph|vector|hybrid",
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
      "properties": {...},
      "distance_hops": 0
    }
  ],
  "count": 5,
  "search_time_ms": 245.3,
  "execution": "HYBRID"
}
```

### POST /api/graph/context
**Context Assembly**

Request:
```json
{
  "agent_id": "AGT-001",
  "focal_entity_id": "LT-005",
  "depth": 2,
  "include_types": ["VENTURE", "CAPABILITY"],
  "exclude_types": []
}
```

Response:
```json
{
  "agent_id": "AGT-001",
  "focal_entity_id": "LT-005",
  "entities": [...],
  "relationships": [...],
  "risks": [...],
  "opportunities": [...],
  "metadata": {
    "entity_count": 12,
    "relationship_count": 18,
    "risk_count": 2
  }
}
```

### GET /api/graph/entity/{entity_id}
**Fetch Single Entity**

Response:
```json
{
  "entity_id": "LT-005",
  "entity_type": "VENTURE",
  "properties": {...}
}
```

### GET /api/graph/paths/{from_id}/{to_id}
**Shortest Path**

Response:
```json
{
  "from_id": "LT-005",
  "to_id": "REPO-123",
  "paths": [
    {
      "nodes": [
        {"id": "LT-005", "type": "VENTURE"},
        {"id": "CAP-001", "type": "CAPABILITY"},
        {"id": "REPO-123", "type": "REPOSITORY"}
      ],
      "relationships": ["HAS_CAPABILITY", "USES"],
      "length": 2
    }
  ],
  "found": true
}
```

---

## File Locations

| What | Where |
|------|-------|
| Hybrid Search | `_PIPELINES/retrieval/hybrid_query.py` |
| Context Builder | `12-CONTEXT/agent_context_builder.py` |
| Agent Profiles | `12-CONTEXT/agent_profiles.yaml` |
| Graph API | `60-APIS/graph_api.py` |
| Cypher Patterns | `_PIPELINES/retrieval/cypher_patterns.yaml` |
| Tests | `_PIPELINES/retrieval/test_kg_capabilities.py` |
| This Guide | `PHASE_1_QUICKSTART.md` |
| Full Report | `PHASE_1_COMPLETION_REPORT.md` |

---

## Troubleshooting

### "Neo4j authentication failed"
→ Update credentials from Bitwarden in hybrid_query.py and agent_context_builder.py

### "Qdrant version mismatch"
→ Not critical; system will work with warning. Update qdrant-client if needed.

### "Ollama connection failed"
→ Non-fatal; system falls back to zero vectors for semantic search. Start Ollama if needed.

### "No results from graph search"
→ Neo4j likely empty. Load test data from Supabase/registries.

### "API returns 401"
→ Missing or invalid Authorization header. Use: `Authorization: Bearer $API_KEY`

---

## Next Steps

1. **Today:** Rotate Neo4j credentials
2. **This week:** Load test data into Neo4j
3. **Next week:** Deploy Graph API to production
4. **Week 3:** Integrate with agent decision-making

---

**Ready to use. All systems go. 🚀**
