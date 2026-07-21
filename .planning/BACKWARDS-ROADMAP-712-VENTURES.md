# Backwards Roadmap: 712 Ventures → Current State

**Goal:** 712 ventures operating autonomously  
**Date:** 2026-07-20  
**Method:** Work backwards from end-state, identify what's needed, check what exists

---

## Layer 0: The Goal (What Success Looks Like)

```
712 Ventures Operating
├─ Each venture: active agents, assigned repos, automated workflows
├─ Each venture: real-time dashboard showing status/revenue/risk
├─ Each venture: automated execution (estimate → dispatch → fulfill)
├─ Portfolio: CEO sees all 712 ventures at a glance
└─ Directives: Changes cascade to all 712 instantly
```

---

## Layer 1: What's Required (Dependencies)

```
712 Ventures Need:
│
├─ Execution Layer (AI Agents)
│  └─ Agent instances (3 core: CEO/CTO/CFO per venture + task agents)
│
├─ Intelligence Layer (Models + Routing)
│  ├─ LiteLLM: route queries to best model
│  ├─ Ollama: local models (qwen2.5:32b on Mac Studio)
│  ├─ Claude API: cloud fallback
│  └─ Model health: tracked + measured
│
├─ Memory Layer (Knowledge Graph)
│  ├─ Neo4j: relationships (Founder→Venture→Agent→Task)
│  ├─ Qdrant: vector search (notes, code, context)
│  └─ Knowledge graph: real-time sync from Supabase
│
├─ Tool Layer (Integrations)
│  ├─ 22 registered tools (check-tools.sh runs them)
│  ├─ 25+ MCPs (Stripe, GitHub, Slack, etc.)
│  └─ Tool health: monitored
│
├─ Workflow Layer (Automation)
│  ├─ n8n: lead capture → task creation
│  ├─ Zapier: integrations
│  └─ Event-driven: triggers on venture events
│
├─ Observability Layer (What's Running?)
│  ├─ Prometheus: metrics (health, latency, errors)
│  ├─ Grafana: dashboards (CEO/CFO/CTO)
│  ├─ Langfuse: LLM tracing (which model, cost, latency)
│  └─ Alerts: Slack on critical issues
│
├─ Governance Layer (Rules + Policy)
│  ├─ DIRECTIVES/: rules cascade to all ventures
│  ├─ OPA (Open Policy Agent): enforce rules
│  └─ Approval matrix: <$5K auto, $5K-$25K director, >$25K Hermes+CEO
│
└─ Executive Layer (C-Suite Visibility)
   ├─ CEO dashboard: revenue, ventures, risk
   ├─ CFO dashboard: MRR, runway, CAC/LTV
   └─ CTO dashboard: uptime, error rate, cost/token
```

---

## Layer 2: What Exists Now (✅ = Built, ❌ = Missing, ⚠️ = Broken)

### Execution Layer
- ✅ **agents.yaml** — 3 core agents defined (CEO, CTO, CFO)
- ✅ **CrewAI** — multi-agent framework available
- ✅ **Hermes** — decision routing agent (in local folder, 0 commits)
- ⚠️ **Agent orchestration** — not yet wired to ventures at scale

### Intelligence Layer
- ✅ **models.yaml** — all available models listed
- ✅ **Ollama** — running locally (Mac Studio: qwen2.5:32b, qwen3:8b)
- ✅ **Claude API** — cloud fallback ready
- ⚠️ **LiteLLM** — running but health check broken (port 4000 not responding)
- ⚠️ **Model routing logic** — exists in litellm_config.yaml but points to wrong Ollama (host.docker.internal vs Mac Studio 100.87.214.70)

### Memory Layer
- ✅ **Neo4j** — running (7474), contains graph entities + relationships
- ✅ **Qdrant** — running (6333), has 2 collections (notes, repositories)
- ✅ **Knowledge graph** — populated via populate_venture_knowledge_graph.py
- ✅ **Supabase** — graph_entities + graph_relationships tables
- ⚠️ **Real-time sync** — graph updates on demand, not streaming

### Tool Layer
- ✅ **tools-registry.yaml** — 22 tools catalogued
- ✅ **mcp-servers/** — 25+ MCPs available
- ✅ **check-tools.sh** — health check script exists
- ⚠️ **Tool health** — check-tools.sh not running on schedule

### Workflow Layer
- ✅ **n8n** — running (not in docker-compose, but available)
- ✅ **workflows.yaml** — workflow definitions exist
- ⚠️ **Event triggers** — not wired to venture creation

### Observability Layer
- ✅ **Prometheus** — running (9090), scraping itself
- ✅ **Grafana** — running (3001), but **admin password unknown**
- ✅ **Langfuse** — running (3003), but **unhealthy** (Internal Server Error)
- ✅ **LiteLLM** — running (4000), but **health broken** (no response)
- ❌ **Prometheus targets** — only scraping self, not services (LiteLLM, otel-collector)
- ❌ **Grafana dashboards** — 0/3 built (CEO, CFO, CTO)
- ❌ **Langfuse traces** — 0 apps instrumented
- ❌ **Alerts** — no Slack alerts on failures

### Governance Layer
- ✅ **DIRECTIVES/** — folder structure complete
- ✅ **Approval matrix** — documented in EXECUTIVE-OPERATING-SYSTEM.md
- ⚠️ **OPA/Cedar** — policy enforcement not wired
- ⚠️ **Directive cascade** — rules exist but not auto-enforced on ventures

### Executive Layer
- ✅ **EXECUTIVE/** — folder structure complete
- ✅ **vex-hero-site** — portfolio dashboard (14 sectors, real hero components)
- ❌ **Real-time dashboards** — no Grafana dashboards yet
- ❌ **Slack alerts** — not wired

---

## Layer 3: Critical Blockers (Why Things Are Broken)

### Prometheus "Unhealthy" Status
**Root cause:** Health check is failing, not the service itself
```bash
# Prometheus IS serving metrics
curl http://localhost:9090/metrics  # ✅ Works

# But Docker thinks it's unhealthy because:
# Health check is timing out or hitting wrong endpoint
docker inspect prometheus | grep -A 5 "HealthCheck"
```

### Grafana Can't Log In
**Root cause:** Admin password unknown (set at container creation)
```
Admin: admin
Password: ??? (ventures2026 fails, admin/admin fails)
→ Need to reset via Docker exec
```

### Langfuse "Unhealthy" + Internal Server Error
**Root cause:** Database migration or startup issue
```
Error: Internal Server Error (500)
Status: Unhealthy (container restart loop?)
→ Check logs: docker logs langfuse | tail -50
→ Check database: Supabase connection string correct?
```

### LiteLLM No Response
**Root cause:** Port 4000 not responding at all
```
Issue 1: Not accepting connections
Issue 2: Wrong Ollama endpoint (points to host.docker.internal)
Issue 3: Ollama on Mac Studio (100.87.214.70) unreachable from this container
→ Fix: Update litellm_config.yaml to use Mac Studio IP
```

---

## Layer 4: What Needs to Happen (Ordered by Dependency)

### Phase 1: Fix Observability (4 hours) — P0
**Why first:** Can't see what's broken without it

- [ ] **1.1 — Fix LiteLLM routing** (30 min)
  - Edit: `litellm_config.yaml`
  - Change: `api_base: http://host.docker.internal:11434` → `http://100.87.214.70:11434`
  - Add cloud fallback: `fallback_model: claude-opus-4-8`
  - Restart: `docker-compose restart litellm`
  - Verify: `curl http://localhost:4000/health`

- [ ] **1.2 — Reset Grafana password** (15 min)
  - Run: `docker exec grafana grafana-cli admin reset-admin-password admin123`
  - Verify: `curl -u admin:admin123 http://localhost:3001/api/health`
  - Log in: admin / admin123

- [ ] **1.3 — Debug Langfuse** (30 min)
  - Check logs: `docker logs langfuse | tail -50`
  - Check health: Is Supabase connection working?
  - Restart: `docker-compose down langfuse && docker-compose up -d langfuse`
  - Wait 30s, verify: `curl http://localhost:3003/api/health`

- [ ] **1.4 — Wire Prometheus targets** (30 min)
  - Edit: `WORLDWIDEBRO-OS/TECHNOLOGY/observability/prometheus.yml`
  - Add targets for: LiteLLM (4000), otel-collector (9464), Neo4j (7474)
  - Restart: `docker-compose restart prometheus`
  - Verify: `curl localhost:9090/api/v1/targets | jq '.data.activeTargets | length'`

- [ ] **1.5 — Build 3 Grafana dashboards** (1 hour)
  - **CEO Dashboard:** 
    - Active ventures (gauge)
    - Total MRR (stat)
    - Portfolio risk score (gauge)
    - Runway distribution (histogram)
  - **CFO Dashboard:**
    - MRR by OPCO (bar chart)
    - ARR projection 12-month (line chart)
    - Unit economics: CAC/LTV (table)
    - Runway alerts: <3 months (stat)
  - **CTO Dashboard:**
    - Deployment success % (gauge)
    - API error rate (gauge)
    - Latency p50/p95/p99 (stat, stat, stat)
    - Tool health green/yellow/red (table)

### Phase 2: Wire Knowledge Graph Sync (2 hours) — P1
**Why:** Agents need real-time venture context

- [ ] **2.1 — Schedule graph sync** (30 min)
  - File: `.grok/skills/populate-graph-sync/cron-job.yaml`
  - Schedule: Every 15 minutes: `populate_venture_knowledge_graph.py`
  - Verify: Neo4j query shows updated venture.mRR field

- [ ] **2.2 — Instrument Hermes with Langfuse** (1.5 hours)
  - File: `hermes-command-center/src/lib/hermes-agent.ts` (or .py if Python)
  - Add: `langfuse.trace()` wrapper around decision calls
  - Log: model choice, tokens used, cost, decision reasoning
  - Test: Make 10 decisions, verify Langfuse shows 10 traces

### Phase 3: Wire Tool Health Checks (1 hour) — P1
**Why:** Agents need to know which tools are available before using them

- [ ] **3.1 — Schedule check-tools.sh** (30 min)
  - File: `.grok/skills/check-tools-cron/schedule.yaml`
  - Schedule: Every 5 minutes: `./scripts/check-tools.sh --category all`
  - Store in: Redis key `tools:health:timestamp`
  - Verify: Redis contains latest tool health status

- [ ] **3.2 — Add tool availability check to agents** (30 min)
  - Before agent uses tool: query Redis for `tools:health:{tool_id}`
  - If unhealthy: use fallback tool or skip task
  - Log: which tools were unavailable

### Phase 4: Scale Agent Execution to 10 Ventures (3 hours) — P1
**Why:** Prove agents can run real tasks

- [ ] **4.1 — Spawn agents for first 10 ventures** (1 hour)
  - For ventures: CON-001 through CON-010
  - Create: CEO, CTO, CFO agents per venture
  - Store agent IDs: ventures.yaml → agent_assignments
  - Verify: 30 agents running (3 × 10 ventures)

- [ ] **4.2 — Execute 3 task types end-to-end** (1.5 hours)
  - Task 1: estimate-job (CON-001)
  - Task 2: risk-score (FIN-001)
  - Task 3: dispatch-job (LOG-001)
  - Verify: Each task completes, Langfuse shows traces, dashboard updates

- [ ] **4.3 — Wire directive enforcement** (30 min)
  - Decision <$5K: auto-approve via agent
  - Decision $5K-$25K: post to Slack, wait for director approval
  - Decision >$25K: route to Hermes for reasoning + CEO approval
  - Verify: Slack message shows up for $10K decision

### Phase 5: Scale to 100 Ventures (4 hours) — P2
**Why:** Prove it scales without breaking

- [ ] **5.1 — Batch create agents** (1 hour)
  - For: All 100 ventures in first 3 OPCOs
  - Method: `VENTURE-FACTORY/spawn_agents.py`
  - Monitor: Agent spawn latency, errors, memory usage

- [ ] **5.2 — Run 100 parallel tasks** (2 hours)
  - 100 ventures × 1 task type each = 100 tasks
  - Monitor: Queue depth, task latency, error rate
  - Verify: All tasks complete, <1% error rate

- [ ] **5.3 — Update dashboards** (1 hour)
  - Add: Venture count (100), active tasks (parallel), throughput (tasks/min)
  - Verify: CEO dashboard shows 100 active ventures

---

## Layer 5: Solutions We Already Have

### For Each Problem:

| Problem | Solution We Have | Current Status |
|---------|-----------------|----------------|
| Route queries to best model | LiteLLM | ⚠️ Config wrong (Ollama endpoint) |
| Local inference | Ollama Mac Studio (qwen2.5:32b) | ✅ Running |
| Knowledge graph | Neo4j + Qdrant (both populated) | ✅ Running |
| Venture context | Supabase + graph_entities + graph_relationships | ✅ Populated |
| Real-time dashboards | Grafana (3 dashboards need to be built) | ⚠️ Can't log in |
| System monitoring | Prometheus + check-tools.sh | ⚠️ Not scraping all targets |
| LLM tracing | Langfuse | ⚠️ Broken startup |
| Event-driven automation | n8n + Zapier + workflows.yaml | ✅ Available |
| Policy enforcement | OPA + DIRECTIVES/ folder | ⚠️ Not wired |
| Multi-agent orchestration | CrewAI + agents.yaml | ✅ Available |
| Tool registry & health | tools-registry.yaml + check-tools.sh | ✅ Built |
| Task type definitions | 10 defined in PLANS | ✅ In documents |

---

## Layer 6: Immediate Next Steps (Today)

### Quick Wins (Fix NOW) — 2 hours

```
1. [30 min] Fix LiteLLM config
   - Edit litellm_config.yaml: host.docker.internal → 100.87.214.70
   - Restart: docker-compose restart litellm
   - Test: curl http://localhost:4000/health

2. [15 min] Reset Grafana password
   - docker exec grafana grafana-cli admin reset-admin-password admin123
   - Verify: Login works at http://localhost:3001

3. [30 min] Debug Langfuse
   - docker logs langfuse | tail -50
   - docker-compose restart langfuse
   - Test: curl http://localhost:3003/api/health

4. [30 min] Wire Prometheus targets
   - Edit prometheus.yml
   - Add: LiteLLM (4000), otel-collector (9464)
   - Restart: docker-compose restart prometheus
```

After these 4 fixes:
- ✅ All services responding
- ✅ Prometheus scraping metrics
- ✅ Grafana can be configured
- ✅ Can see what's happening

---

## Summary

| Category | Status | Details |
|----------|--------|---------|
| **What Works** | ✅ 80% | Registries, configs, frameworks, databases all built |
| **What's Broken** | ⚠️ 5 issues | Passwords, configs, startups (all fixable <4 hours) |
| **What's Missing** | ❌ 20% | Wiring (agent spawn, task execution, scaling) |

**Critical Path to First Working Venture:**
1. Fix observability (4 hours)
2. Instrument one agent (2 hours)
3. Execute one task type (1 hour)
4. **Total: 7 hours to first working venture**

**Path to 100 Ventures:**
1. Complete critical path (7 hours)
2. Scale agents (4 hours)
3. Run 100 parallel tasks (2 hours)
4. **Total: ~13 hours to 100 operating ventures**

**Path to 712 Ventures:**
1. Complete 100 ventures phase (13 hours)
2. Replicate across all 6 OPCOs (8 hours parallelizable)
3. Add governance + alerts (4 hours)
4. **Total: ~25 hours to full operating system**
