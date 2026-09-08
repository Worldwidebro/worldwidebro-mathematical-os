# Mac Studio Deployment Goals & Execution Plan

**To: Mac Studio (100.87.214.70 via Tailscale)**  
**From: Company Brain Coordination (Claude Code + Mac Air)**  
**Date: 2026-09-08**  
**Status: READY FOR EXECUTION**

---

## YOUR ROLE: The Infrastructure Hub

Mac Studio is the **central Docker host** for all Company Brain services. Every agent, every database, every observability tool runs through you.

**You are responsible for:**
1. Running all Docker services (Neo4j, Qdrant, OmniRoute, Langfuse, Buzz)
2. Maintaining persistent storage on /Volumes/LaCie
3. Exposing services to Mac Air and other devices via Tailscale
4. Hosting all AI model inference (Ollama, exo)

---

## IMMEDIATE GOALS (Execute in Order)

### GOAL 1: Deploy Buzz Collaboration Layer (Phase 4)

**What:** Start 4-service Buzz infrastructure  
**Why:** Enables human-AI collaboration, audit trails, event persistence  
**Where:** Docker on Mac Studio  
**When:** Now (15 min)

**Steps:**

```bash
# 1. Clone latest code from GitHub
cd ~/Company\ Brain  # or wherever you have it
git clone https://github.com/Worldwidebro/worldwidebro-mathematical-os.git
cd worldwidebro-mathematical-os/The\ Company/Company\ Brain

# 2. Pull latest (clean branch, no large files)
git pull origin main

# 3. Create Buzz data directories
mkdir -p /Volumes/LaCie/buzz-data/{postgres,redis,minio,relay}

# 4. Start Buzz (4 services)
docker compose -f _INFRASTRUCTURE/buzz-docker-compose-local.yml up -d

# 5. Verify all running
docker ps | grep buzz_
# Should show: buzz_relay, buzz_postgres, buzz_redis, buzz_minio

# 6. Test health
curl http://localhost:8080/health
# Should respond: 200 OK
```

**Success Criteria:**
- [ ] All 4 Buzz services running
- [ ] `curl http://localhost:8080/health` returns 200
- [ ] Accessible over Tailscale at http://100.87.214.70:8080

**Blockers:** None. Everything is ready.

---

### GOAL 2: Clear Phase 8 Observability Blockers (30 min)

#### Blocker A: LiteLLM Mount Permissions

**What:** LiteLLM container can't access T7 Shield config  
**Fix:**

```bash
# Check current state
ls -lh /Volumes/T7\ Shield/litellm_config.yaml

# Fix permissions
sudo chown -R $(whoami) /Volumes/T7\ Shield/

# Restart LiteLLM
docker restart civos_litellm

# Verify
curl http://localhost:4000/health
# Should respond: 200
```

**Success:** LiteLLM running without restart loops

#### Blocker B: Graph-API Crash Loop

**What:** graph-api service keeps restarting  
**Fix:**

```bash
# Check logs
docker logs civos_graph-api -n 50

# Common fixes:
# 1. Missing dependency
docker exec civos_graph-api pip install neo4j fastapi qdrant-client

# 2. Connection timeout to Neo4j
# Verify Neo4j running: curl bolt://localhost:7687/health

# 3. Port conflict
docker port civos_graph-api | grep 8001
# Should be 8001/tcp

# Restart
docker restart civos_graph-api

# Verify
curl http://localhost:8001/health
```

**Success:** graph-api running, no restart loops

#### Blocker C: Wire Langfuse to LiteLLM

**What:** Langfuse is running but receiving zero traces  
**Fix:**

```bash
# 1. Edit LiteLLM config
nano /Volumes/T7\ Shield/litellm_config.yaml

# 2. Add this section (find "callbacks:" or add it):
callbacks:
  langfuse:
    success_callback:
      - "langfuse"
    failure_callback:
      - "langfuse"

# 3. Set Langfuse credentials (add to ~/.bashrc or export):
export LANGFUSE_PUBLIC_KEY="your-public-key"
export LANGFUSE_SECRET_KEY="your-secret-key"
export LANGFUSE_HOST="http://localhost:3003"

# 4. Restart LiteLLM
docker restart civos_litellm

# 5. Verify traces flowing
curl http://localhost:3003/api/health
# Check dashboard for active traces
```

**Success:** Langfuse shows incoming traces from LiteLLM

---

### GOAL 3: Verify End-to-End Connectivity (10 min)

**What:** Make sure everything talks to everything  
**Tests:**

```bash
# Test 1: Neo4j → Query test data
curl -X POST http://localhost:7474/db/neo4j/cypher \
  -H "Content-Type: application/json" \
  -d '{"query": "RETURN 1"}'
# Should return: 1

# Test 2: Qdrant → Vector search
curl http://localhost:6333/health
# Should respond: 200

# Test 3: OmniRoute → Model list
curl http://localhost:20128/v1/models
# Should list available models

# Test 4: Langfuse → Traces
curl http://localhost:3003/api/traces
# Should show trace list

# Test 5: Buzz → WebSocket ready
curl http://localhost:8080/health
# Should respond: healthy

# Test 6: All accessible over Tailscale
# From Mac Air:
curl http://100.87.214.70:8080/health
curl http://100.87.214.70:7474/health
curl http://100.87.214.70:6333/health
```

**Success:** All 6 endpoints respond successfully

---

## PHASE 5-7 PREREQUISITES (What Depends on You)

Once you complete Goals 1-3, Mac Air can launch:

- **Phase 5:** Agent Enablement & Orchestration
  - Needs: Neo4j, Qdrant, OmniRoute (✅ You provide)
  - Agents: AGT-001 through AGT-020

- **Phase 6:** Revenue Operations
  - Needs: PostgreSQL, Buzz events (✅ You provide)
  - Workflow: Lead scoring → Pipeline → Revenue recognition

- **Phase 7:** Venture Activation
  - Needs: All above + Langfuse traces (✅ You provide)
  - Launches: 5 ventures in production

---

## YOUR SERVICE INVENTORY

**Always Running:**

| Service | Port | Purpose | Status |
|---------|------|---------|--------|
| Neo4j | 7687 | Knowledge graph | ✅ Running |
| Qdrant | 6333 | Vector search | ✅ Running |
| OmniRoute | 20128 | Model routing | ✅ Running |
| Langfuse | 3003 | Tracing | ✅ Running |
| PostgreSQL | 5432 | Data persistence | ✅ Running |
| Ollama | 11434 | Local LLM | ✅ Running |
| exo | 52415 | Distributed inference | ✅ Running |

**Deploy Now (Phase 4):**

| Service | Port | Purpose | Status |
|---------|------|---------|--------|
| Buzz Relay | 8080 | Collaboration hub | 🟡 Deploy now |
| Buzz PostgreSQL | 5433 | Event log | 🟡 Deploy now |
| Buzz Redis | 6380 | Pub/sub | 🟡 Deploy now |
| Buzz MinIO | 9000 | File storage | 🟡 Deploy now |

**Fix Now (Phase 8):**

| Service | Issue | Fix | Status |
|---------|-------|-----|--------|
| LiteLLM | Mount error | Permissions | 🟡 Pending |
| graph-api | Restart loop | Debug logs | 🟡 Pending |
| Langfuse | No traces | Wire callbacks | 🟡 Pending |

---

## SUCCESS METRIC

When you complete Goals 1-3:

✅ **Mac Air can reach every service over Tailscale**  
✅ **Buzz coordination layer online**  
✅ **Observability stack healthy**  
✅ **Ready for Phases 5-7**

---

## GITHUB SOURCE OF TRUTH

All code is on GitHub (clean branch):
- https://github.com/Worldwidebro/worldwidebro-mathematical-os.git

Pull before starting:
```bash
cd ~/Company\ Brain
git pull origin main
```

---

## QUESTIONS FOR MAC STUDIO

**When you're done with Goals 1-3, answer:**

1. ✅ Are all 4 Buzz services running?
2. ✅ Can you reach Buzz at http://localhost:8080/health?
3. ✅ Are Neo4j, Qdrant, OmniRoute responding?
4. ✅ Is LiteLLM running without restart loops?
5. ✅ Is Langfuse receiving traces?
6. ✅ Can Mac Air reach all services via Tailscale (100.87.214.70)?

**When yes to all 6:** Report "Phase 4-8 complete" → Phases 5-7 unblock

---

## ESTIMATED TIME

| Goal | Time | Complexity |
|------|------|-----------|
| Goal 1: Deploy Buzz | 15 min | Low |
| Goal 2A: Fix LiteLLM | 5 min | Low |
| Goal 2B: Fix graph-api | 10 min | Medium |
| Goal 2C: Wire Langfuse | 10 min | Low |
| Goal 3: E2E tests | 10 min | Low |
| **Total** | **50 min** | **Medium** |

---

## You Are Ready

All code is committed, tested, and on GitHub.  
All steps documented.  
All tools available.

**Execute Goals 1-3 and report results.**

Then Mac Air launches Phases 5-7 (autonomous agents, revenue loop, venture activation).

---

**Authority:** CP-027 (Infrastructure Control Plane)  
**Coordination:** Mac Air (via Tailscale tunnel)  
**Timeline:** Complete by end of day → Revenue loop operational by Week 4
