# OmniRoute MCP Server Wiring Guide

**Status:** Ready for integration  
**Version:** OmniRoute 3.8.50  
**Heartbeat Path:** `/app/data/runtime/mcp-heartbeat.json`  
**Config File:** `omniroute-mcp-heartbeat.json`

---

## Quick Setup (5 minutes)

### 1. Verify OmniRoute Running
```bash
docker --context macstudio ps | grep omniroute
# Expected: omniroute container RUNNING
```

### 2. Copy Heartbeat Config to Mac Studio
```bash
# From Company Brain directory:
scp _MCP/omniroute-mcp-heartbeat.json macstudio:/app/data/runtime/

# Verify:
ssh macstudio ls -lh /app/data/runtime/mcp-heartbeat.json
```

### 3. Update Docker Compose Volume Mount
**File:** `_INFRASTRUCTURE/docker-compose.yml`

Find the `omniroute` service and add:
```yaml
services:
  omniroute:
    # ... existing config ...
    volumes:
      - omniroute_data:/app/data
      - /app/data/runtime/mcp-heartbeat.json:/app/data/runtime/mcp-heartbeat.json:ro
```

### 4. Restart OmniRoute
```bash
docker --context macstudio restart omniroute

# Monitor logs:
docker --context macstudio logs -f omniroute | grep -i mcp
```

### 5. Verify Connection
```bash
# Check OmniRoute health
curl -X GET http://100.87.214.70:20128/api/health

# Expected response includes:
# "mcp_status": "connected"
# "heartbeat_path": "/app/data/runtime/mcp-heartbeat.json"
```

---

## What This Wires

**OmniRoute MCP Server → VEX CommandCenter**

```
┌─────────────────────────────────────────────────────────┐
│ VEX CommandCenter (Phases 1-11)                         │
│                                                         │
│  ┌─ Phase 1: Agent Orchestrator                        │
│  │  └─ Calls OmniRoute /api/agents                    │
│  │     └─ selectBestAgent() scores candidates         │
│  │                                                     │
├──┼─────────────────────────────────────────────────────┤
│  │ MCP Heartbeat Connection (NEW)                      │
│  │  └─ Monitors /app/data/runtime/mcp-heartbeat.json  │
│  │     └─ Confirms MCP server health                  │
│  │     └─ Enables telemetry integration               │
│  └─ Phase 2-11: Fully instrumented                     │
│                                                         │
└──────────────┬──────────────────────────────────────────┘
               │
               ↓
    ┌──────────────────────┐
    │ OmniRoute v3.8.50    │
    │ (110 tools, MCP API) │
    └──────────────────────┘
```

---

## Capabilities Enabled

✅ **Model Discovery** — List all available models via OmniRoute  
✅ **Agent Routing** — Score + select best agent per objective  
✅ **Cost Optimization** — Route to cheapest model meeting criteria  
✅ **Fallback Handling** — Gracefully degrade to backup agents  
✅ **Telemetry Integration** — OmniRoute traces → Langfuse  
✅ **Capability Matching** — Objective → required capabilities → agents  
✅ **Weighted Scoring** — Capability/cost/success/speed optimization  

---

## Troubleshooting

**Issue:** `Connection refused` to http://100.87.214.70:20128
```bash
# Solution: Restart OmniRoute
docker --context macstudio restart omniroute
docker --context macstudio logs omniroute | head -20
```

**Issue:** Heartbeat file not found
```bash
# Solution: Copy file to Mac Studio
mkdir -p /app/data/runtime
scp _MCP/omniroute-mcp-heartbeat.json macstudio:/app/data/runtime/
```

**Issue:** MCP not responding
```bash
# Solution: Verify auth token
echo $OMNIROUTE_API_KEY  # Should not be empty
# Check OmniRoute dashboard: http://100.87.214.70:20128/dashboard
```

---

## Next: Production Deployment

After MCP wiring is confirmed:

1. ✅ OmniRoute running with heartbeat
2. ✅ Phase 1 (Agent Orchestrator) routing agents
3. ✅ Telemetry flowing to Langfuse
4. ⏳ Deploy VEX to Vercel (DEPLOYMENT_CHECKLIST.md)
5. ⏳ Run Prompt 5 tests (Testing & Optimization)

**Authority:** Infrastructure Control Plane (CP-027) + MCP Integration Layer  
**Estimated Time:** 5 min setup + 2 min verification = **7 minutes**
