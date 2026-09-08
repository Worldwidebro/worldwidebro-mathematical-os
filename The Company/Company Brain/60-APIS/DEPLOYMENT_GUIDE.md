# Phase 1 Deployment Guide

[[STARTHERE]] | [[PHASE_1_EXECUTION_PLAN]] | [[_MCP/omniroute_registration.yaml|OmniRoute Registration]]

**Date:** 2026-09-06  
**Objective:** Deploy KG-017/028/048 (Graph API + MCP Tools) to Docker + OmniRoute  
**Timeline:** Sep 16-19  
**Authority:** CP-027 (Infrastructure Control Plane)

---

## Quick Start (5 minutes)

### Option A: Automated Deployment

```bash
cd /Users/acebless/Documents/The\ Company/Company\ Brain/60-APIS
bash deploy.sh --build --test
```

This will:
1. ✅ Build Docker image
2. ✅ Start graph-api service on port 8000
3. ✅ Wait for health check
4. ✅ Run smoke tests
5. ✅ Print next steps

### Option B: Manual Deployment

```bash
# 1. Navigate to API directory
cd /Users/acebless/Documents/The\ Company/Company\ Brain/60-APIS

# 2. Build and start service
docker-compose up -d

# 3. Wait for health check
sleep 5
curl http://localhost:8000/health

# 4. View logs
docker-compose logs -f graph-api
```

---

## Verification (5 minutes)

### Test 1: Health Check

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "OK",
  "timestamp": "2026-09-06T...",
  "version": "1.0.0"
}
```

### Test 2: Hybrid Search (KG-017)

```bash
curl -X POST http://localhost:8000/api/graph/query \
  -H "Authorization: Bearer changeme" \
  -H "Content-Type: application/json" \
  -d '{
    "query_text": "medical logistics ventures",
    "search_type": "hybrid",
    "limit": 5,
    "confidence_threshold": 0.5
  }'
```

Expected response:
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
  "count": 1,
  "search_time_ms": 234,
  "execution": "HYBRID",
  "query_text": "medical logistics ventures"
}
```

### Test 3: Agent Context (KG-028)

```bash
curl -X POST http://localhost:8000/api/graph/context \
  -H "Authorization: Bearer changeme" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "AGT-001",
    "focal_entity_id": "LT-005",
    "depth": 2,
    "include_types": "VENTURE,REPOSITORY,CUSTOMER"
  }'
```

Expected response:
```json
{
  "agent_id": "AGT-001",
  "focal_entity_id": "LT-005",
  "focal_entity_type": "VENTURE",
  "depth_limit": 2,
  "entities": [...],
  "relationships": [...],
  "risks": [...],
  "opportunities": [...],
  "metadata": {...}
}
```

---

## OmniRoute Integration (10 minutes)

### Step 1: Copy MCP Tools

```bash
# Determine OmniRoute MCP tools directory
# Typically: ~/.omniroute/tools or /path/to/omniroute/mcp/

cp /Users/acebless/Documents/The\ Company/Company\ Brain/_MCP/hybrid_query_tool.py ~/.omniroute/tools/
cp /Users/acebless/Documents/The\ Company/Company\ Brain/_MCP/context_assembly_tool.py ~/.omniroute/tools/
```

### Step 2: Restart OmniRoute

```bash
# If OmniRoute is running via Docker
docker restart omniroute

# If OmniRoute is running locally
pkill omniroute
sleep 2
omniroute serve
```

### Step 3: Verify Tool Discovery

```bash
# Check if MCP tools are discoverable
curl http://localhost:20128/tools | grep -E "hybrid_search|build_agent_context"

# Should output:
# "name": "hybrid_search"
# "name": "build_agent_context"
```

### Step 4: Test via OmniRoute

```bash
# Hybrid search via OmniRoute
curl -X POST http://localhost:20128/execute \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "hybrid_search",
    "args": {
      "query_text": "ventures",
      "search_type": "hybrid",
      "limit": 5
    }
  }'

# Context assembly via OmniRoute
curl -X POST http://localhost:20128/execute \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "build_agent_context",
    "args": {
      "agent_id": "AGT-001",
      "focal_entity_id": "LT-005",
      "depth": 2
    }
  }'
```

---

## Agent Integration (15 minutes)

### Step 1: Update AGT-001 (Venture PM)

Edit `16-AGENTS/AGT-001-venture-pm.md` to add tool calls:

```markdown
## Tools

- [[_PIPELINES/retrieval/hybrid_query|Hybrid Search]]: Query ventures + repos
- [[12-CONTEXT/agent_context_builder|Agent Context]]: Get venture context + risks

## Example Usage

```python
# Query ventures
results = omniroute.call_tool("hybrid_search", query_text="medical logistics")

# Get context
context = omniroute.call_tool("build_agent_context", 
  agent_id="AGT-001", 
  focal_entity_id="LT-005", 
  depth=2)
```
```

### Step 2: Test AGT-001 Integration

```bash
# Create a simple test script
cat > /tmp/test_agt001.py << 'EOF'
import requests

# Simulate AGT-001 calling hybrid search
response = requests.post(
    "http://localhost:8000/api/graph/query",
    headers={"Authorization": "Bearer changeme"},
    json={
        "query_text": "medical logistics ventures",
        "search_type": "hybrid",
        "limit": 10
    }
)

print(f"Results: {len(response.json()['results'])} entities found")
print(f"Time: {response.json()['search_time_ms']}ms")

# Simulate AGT-001 calling context assembly
response = requests.post(
    "http://localhost:8000/api/graph/context",
    headers={"Authorization": "Bearer changeme"},
    json={
        "agent_id": "AGT-001",
        "focal_entity_id": "LT-005",
        "depth": 2
    }
)

print(f"Context: {len(response.json()['entities'])} entities")
print(f"Risks: {len(response.json()['risks'])}")
print(f"Opportunities: {len(response.json()['opportunities'])}")
EOF

python /tmp/test_agt001.py
```

### Step 3: Wire Up All Agents (AGT-002 through AGT-009)

For each agent file in `16-AGENTS/AGT-*.md`:
1. Add Tools section
2. Add example usage
3. Update README to reference hybrid search + context assembly

---

## Troubleshooting

### Issue: "Connection refused" on http://localhost:8000

**Solution:**
```bash
# Check if service is running
docker-compose -f 60-APIS/docker-compose.yml ps

# If not running, start it
docker-compose -f 60-APIS/docker-compose.yml up -d

# View logs for errors
docker-compose -f 60-APIS/docker-compose.yml logs graph-api
```

### Issue: "Neo4j connection failed"

**Solution:**
```bash
# Verify Neo4j is running on Mac Studio
ssh macstudio "docker --context macstudio ps | grep neo4j"

# Verify connectivity from host
nc -zv 100.87.214.70 7687

# Update docker-compose.yml with correct Neo4j address
```

### Issue: "Qdrant connection failed"

**Solution:**
```bash
# Verify Qdrant is running
curl http://100.87.214.70:6333/health

# Check Qdrant collection exists
curl http://100.87.214.70:6333/collections/ventures
```

### Issue: "MCP tools not discoverable by OmniRoute"

**Solution:**
```bash
# Ensure files copied to correct location
ls -la ~/.omniroute/tools/hybrid_query_tool.py
ls -la ~/.omniroute/tools/context_assembly_tool.py

# Restart OmniRoute
pkill omniroute
sleep 2
omniroute serve

# Check discovery again
curl http://localhost:20128/tools | jq '.[] | select(.name | contains("hybrid_search"))'
```

---

## Rollback (if needed)

```bash
# Stop service
docker-compose -f 60-APIS/docker-compose.yml down

# Remove image (optional)
docker rmi company-brain-graph-api:latest

# Revert Git changes (if any)
git checkout 60-APIS/
```

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `GRAPH_API_KEY` | `changeme` | API bearer token (rotate before production) |
| `NEO4J_URI` | `bolt://100.87.214.70:7687` | Neo4j connection URI |
| `NEO4J_USER` | `neo4j` | Neo4j username |
| `NEO4J_PASSWORD` | `changeme` | Neo4j password (from Bitwarden) |
| `QDRANT_URL` | `http://100.87.214.70:6333` | Qdrant base URL |
| `QDRANT_COLLECTION` | `ventures` | Qdrant collection name |

### Override for local testing:

```bash
# In terminal
export GRAPH_API_KEY="your-test-key"
docker-compose -f 60-APIS/docker-compose.yml up -d

# Or in .env file
echo "GRAPH_API_KEY=your-test-key" > 60-APIS/.env
docker-compose -f 60-APIS/docker-compose.yml up -d
```

---

## Performance Targets

| Metric | Target | Current |
|--------|--------|---------|
| Hybrid search latency | < 500ms | ⏳ TBD |
| Context assembly latency | < 1000ms | ⏳ TBD |
| API endpoint availability | > 99.9% | ⏳ TBD |
| Memory usage | < 512MB | ⏳ TBD |

---

## Success Checklist

- [ ] Docker image builds successfully
- [ ] Service starts on port 8000
- [ ] Health check responds with 200 OK
- [ ] `/api/graph/query` endpoint works
- [ ] `/api/graph/context` endpoint works
- [ ] Hybrid search returns results < 500ms
- [ ] Context assembly returns subgraph + risks + opportunities
- [ ] MCP tools discoverable by OmniRoute
- [ ] AGT-001 can call tools via OmniRoute
- [ ] All agents (AGT-001-009) routable
- [ ] Logs show no errors

---

## Next Steps

1. **Sep 16** — Deploy to Docker + OmniRoute (this guide)
2. **Sep 17** — Test all 5 routing agents (AGT-001-005)
3. **Sep 18** — Test all 4 education agents (AGT-006-009)
4. **Sep 19** — Activate 12 specialized agents + 280+ skills

---

**Authority:** CP-027 (Infrastructure Control Plane)  
**Updated:** 2026-09-06  
**Next Checkpoint:** Sep 19 (all 301+ agents routable)
