[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# Deployment & Observability Integration Guide

**Status:** All code committed locally. Infrastructure deployment requires user action.  
**Date:** 2026-09-08  
**Authority:** CP-027 (Infrastructure) + CP-028 (Collaboration) + CP-016 (Observability)

---

## PART 1: PHASE 4 DEPLOYMENT (Buzz via Tailscale Docker)

### Step 1: Verify Tailscale & SSH Access

```bash
# On this machine (Mac Air):
tailscale ip -4
# Should output: 100.121.17.63

# Verify Mac Studio reachable over Tailscale:
ping mac-studio.tailba9617.ts.net
# Should succeed

# Test SSH connectivity:
ssh acebless@mac-studio.tailba9617.ts.net "uname -a"
# If auth fails: check Bitwarden for Mac Studio SSH password
```

### Step 2: Deploy Buzz Infrastructure on Mac Studio

```bash
# Copy Buzz compose to Mac Studio:
scp _INFRASTRUCTURE/buzz-docker-compose-local.yml \
  acebless@mac-studio.tailba9617.ts.net:/tmp/buzz-docker-compose.yml

# SSH into Mac Studio and start Buzz:
ssh acebless@mac-studio.tailba9617.ts.net

# On Mac Studio:
cd /tmp
docker compose -f buzz-docker-compose.yml up -d

# Verify all 4 services running:
docker ps | grep buzz_
# Expected: buzz_relay, buzz_postgres, buzz_redis, buzz_minio

# Check health:
docker compose -f buzz-docker-compose.yml ps
```

### Step 3: Access Buzz Over Tailscale

Once running on Mac Studio, access from anywhere via Tailscale:

```bash
# From Mac Air or any Tailscale device:
curl http://100.87.214.70:8080/health
# Should respond: {"status":"healthy"}

# Buzz WebSocket: ws://100.87.214.70:8080
# MinIO Console: http://100.87.214.70:9001
# PostgreSQL: psql -h 100.87.214.70 -p 5433 -U postgres buzz
# Redis: redis-cli -h 100.87.214.70 -p 6380
```

---

## PART 2: PHASE 8 BLOCKERS - CRITICAL PATH

### Blocker 1: Fix LiteLLM T7 Shield Mount

**Problem:** LiteLLM container can't access `/host_mnt/Volumes/T7 Shield/litellm-config.yaml`

**Solution (on Mac Studio):**

```bash
# Check current mount:
ls -lh /Volumes/T7\ Shield/
# If permission denied: need to fix ownership

# Fix 1: Make writable
sudo chown -R $(whoami) /Volumes/T7\ Shield/

# Fix 2: Or restart LiteLLM with explicit mount:
docker run -d \
  --name civos_litellm \
  -p 4000:4000 \
  -v /Volumes/T7\ Shield/litellm_config.yaml:/app/config.yaml:ro \
  ghcr.io/berriai/litellm:latest

# Fix 3: Or edit docker-compose and use local path instead
```

### Blocker 2: Debug graph-api Crash Loop

**Problem:** `civos_graph-api` constantly restarting

**Solution:**

```bash
# On Mac Studio:
docker logs civos_graph-api -n 50

# Common fixes:
# 1. Missing Python dependency: pip install neo4j fastapi qdrant-client
# 2. Connection timeout: verify Neo4j running on bolt://100.87.214.70:7687
# 3. Port conflict: graph-api expects port 8001 free

# Restart with verbose logging:
docker restart civos_graph-api
docker logs -f civos_graph-api
```

### Blocker 3: Wire Langfuse to LiteLLM

**Problem:** Langfuse running but not receiving traces from LiteLLM

**Solution:**

```bash
# On Mac Studio, edit LiteLLM config:
nano /Volumes/T7\ Shield/litellm_config.yaml

# Add this section:
callbacks:
  langfuse:
    success_callback:
      - "langfuse"
    failure_callback:
      - "langfuse"

# Set Langfuse credentials:
export LANGFUSE_PUBLIC_KEY="your-key"
export LANGFUSE_SECRET_KEY="your-secret"
export LANGFUSE_HOST="http://100.87.214.70:3003"

# Restart LiteLLM:
docker restart civos_litellm

# Verify traces flowing:
curl http://100.87.214.70:3003/api/health
# Should show active traces in Langfuse dashboard
```

---

## PART 3: OBSERVABILITY STACK INTEGRATION

### Architecture: Langfuse + LangGraph + LangChain + OmniRoute

```
┌─────────────────────────────────────────────────────────────┐
│                    Claude Code (This Machine)                │
│  ┌──────────────┐  ┌─────────────┐  ┌──────────────────┐   │
│  │ LangChain    │  │ LangGraph   │  │ Company Brain    │   │
│  │ (Executor)   │  │ (Workflow)  │  │ MCP Tools        │   │
│  └──────────────┘  └─────────────┘  └──────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                           │
                    Tailscale Tunnel
                           │
┌─────────────────────────────────────────────────────────────┐
│                Mac Studio Docker (Services)                  │
│  ┌─────────────┐  ┌────────────────┐  ┌─────────────────┐  │
│  │ OmniRoute   │  │ Langfuse       │  │ Buzz Relay      │  │
│  │ :20128      │  │ :3003          │  │ :8080           │  │
│  └─────────────┘  └────────────────┘  └─────────────────┘  │
│  ┌──────────────┐  ┌────────────────┐  ┌─────────────────┐  │
│  │ LiteLLM      │  │ Neo4j + Qdrant │  │ PostgreSQL      │  │
│  │ :4000        │  │ :7687, :6333   │  │ :5433           │  │
│  └──────────────┘  └────────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Integration Points

#### 1. **LangChain → OmniRoute → LiteLLM**

```python
from langchain_community.llms import OpenAI
from langchain.callbacks import LangChainTracer

# Route through OmniRoute via LiteLLM
llm = OpenAI(
    api_key="sk-",
    api_base="http://100.87.214.70:4000/v1",  # LiteLLM endpoint
    model="gpt-4"  # LiteLLM routes to OmniRoute
)

# Enable Langfuse tracing
tracer = LangChainTracer(
    project_name="Company Brain",
    client_url="http://100.87.214.70:3003"
)
```

#### 2. **LangGraph Workflow Persistence** (Buzz Channels)

```python
from langgraph.graph import StateGraph
from buzz_integration import buzz_publish_event

class AgentState:
    messages: list
    agent_id: str

def agent_node(state: AgentState):
    # Publish to Buzz channel
    buzz_publish_event(
        channel=f"#agent-{state.agent_id}",
        event={
            "type": "agent_step",
            "state": state,
            "timestamp": now()
        }
    )
    return state

# Build graph with Buzz audit trail
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
# ... wire to Buzz for persistence
```

#### 3. **MCP Tools → Langfuse Traces**

All MCP tool calls are captured by Langfuse:

```
MCP Tool Call (e.g., neo4j_query_entities)
    ↓ (through LiteLLM)
OmniRoute (routes to correct provider)
    ↓ (callback)
Langfuse (captures trace with:
  - tool name
  - inputs
  - duration
  - output
  - errors if any)
```

#### 4. **Neo4j Knowledge Graph + Langfuse Analytics**

```sql
-- Query: Which tools are called most frequently?
SELECT 
    tool_name, 
    COUNT(*) as calls,
    AVG(duration_ms) as avg_latency
FROM langfuse.traces
WHERE tool_name IS NOT NULL
GROUP BY tool_name
ORDER BY calls DESC
```

---

## PART 4: OBSERVABILITY DASHBOARDS (Post-Deployment)

### Dashboard 1: Agent Health (Langfuse)

**URL:** http://100.87.214.70:3003/dashboard

Tracks:
- Agent execution traces (real-time)
- LLM token usage by agent
- Error rates by agent type
- Latency P50/P95/P99

### Dashboard 2: Infrastructure Health (Grafana)

**URL:** http://100.87.214.70:3011 (when deployed)

Tracks:
- Neo4j query latency
- Qdrant search latency
- PostgreSQL connections
- Buzz WebSocket connections
- OmniRoute model routing decisions

### Dashboard 3: Collaboration Activity (Buzz)

**URL:** http://100.87.214.70:8080/dashboard (when wired)

Tracks:
- AGT-013/014/015 classification events
- Human feedback in collaboration channels
- Sync to Neo4j audit trail

---

## PART 5: QUICK REFERENCE - Infrastructure Addresses

| Service | Local | Tailscale | Purpose |
|---------|-------|-----------|---------|
| OmniRoute | :20128 | 100.87.214.70:20128 | AI model routing |
| Neo4j | bolt://localhost:7687 | bolt://100.87.214.70:7687 | Knowledge graph |
| Qdrant | :6333 | 100.87.214.70:6333 | Vector search |
| LiteLLM | :4000 | 100.87.214.70:4000 | LLM abstraction |
| Langfuse | :3003 | 100.87.214.70:3003 | Tracing & observability |
| Buzz Relay | :8080 | 100.87.214.70:8080 | Collaboration layer |
| PostgreSQL | :5433 | 100.87.214.70:5433 | Data persistence |
| Grafana | :3011 | 100.87.214.70:3011 | Dashboards (pending) |

---

## PART 6: NEXT STEPS SEQUENCE

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Fix SSH auth to Mac Studio | User | Now |
| 2 | Deploy Buzz (Phase 4.1) | SSH/Docker | 5 min |
| 3 | Clear 3 Phase 8 blockers | SSH/Config | 30 min |
| 4 | Wire Langfuse callbacks | Config edit | 10 min |
| 5 | Test end-to-end trace flow | curl/browser | 10 min |
| 6 | Deploy Grafana dashboards | Docker | 20 min |
| 7 | Launch Phases 5-7 (sequential) | Agents | 48+ hours |

---

## PART 7: Code Ready for Execution

**All Phase 1-4 code is committed and waiting:**

```
_PIPELINES/retrieval/hybrid_query.py         # KG-017 ✅
12-CONTEXT/agent_context_builder.py          # KG-028 ✅
60-APIS/graph_api.py                         # KG-048 ✅
_PIPELINES/ingestion/github_ingest.py        # Phase 2.1 ✅
_PIPELINES/ingestion/normalize_repos.py      # Phase 2.2 ✅
_MCP/dealflow_postgres_api.py                # Phase 3 ✅
_INFRASTRUCTURE/buzz-docker-compose.yml      # Phase 4.1 ✅
_MCP/buzz_integration.py                     # Phase 4.2 ✅
_MCP/buzz_sync_agent.py                      # Phase 4.3 ✅
```

**Ready to run. Execute in this order:**
1. Deploy Buzz (Phase 4.1)
2. Clear Phase 8 blockers
3. Launch remaining agents (Phases 5-7)

---

**Git Status:** Code committed locally; push blocked by 606 MB graph file (git-lfs requires GitHub configuration)

**Next Action:** Fix SSH → Deploy Buzz → Clear blockers → Execute Phases 5-7
