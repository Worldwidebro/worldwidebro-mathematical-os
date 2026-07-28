---
title: IZA OS Master Execution Plan — 6-Week Roadmap
subtitle: 712-Venture Autonomous Studio via Local AI Stack + OmniRouter Control Plane
date: 2026-07-20
status: Active
---

# STORAGE REALITY (2026-07-20)

| Device | Used | Total | Free | Status | Action |
|--------|------|-------|------|--------|--------|
| **MacBook Air SSD** | 169GB | 228GB | **19GB** | 🔴 CRITICAL | Free 100GB today (Phase 2) |
| **T7 Shield** | 779GB | 1.8TB | **1.1TB** | 🟢 Healthy | Use as data lake |
| **LaCie 4TB** | Unknown | 4TB | ? | ⏳ TBD | Mount + catalog |

**Decision Point:** Mac SSD is at 90%. Must clean storage BEFORE adding code/models.

---

# SIX-WEEK EXECUTION PLAN

## WEEK 1: Infrastructure + Storage Cleanup (Parallel)

### Phase 1: Infrastructure-as-Code (Mon–Wed)
**Owner:** CTO (You)  
**Goal:** `docker compose up` → everything lives.

**Deliverable:** Complete `docker-compose.yml` with:
- Neo4j, Qdrant, Redis, PostgreSQL, Langfuse, Prometheus, Grafana, MinIO
- Ollama (Mac Studio GPU), LiteLLM (routing), n8n (workflows), AnythingLLM (UI)
- All services discoverable + persistent across reboot

**Milestone:** `docker ps` shows 12+ healthy containers. One reboot. No manual restarts.

### Phase 2: Storage Cleanup (Mon–Fri) — PARALLEL
**Owner:** You (SysAdmin)  
**Goal:** Free 100GB on Mac SSD. T7 becomes primary data lake.

**Move to T7/Shield/14_INFRASTRUCTURE/:**
```
/data/
  ├── models/              ← Ollama models (qwen2.5:32b, etc.)
  ├── embeddings/          ← Qdrant snapshots
  ├── videos/              ← Generated media
  ├── logs/                ← All logs (Docker, PostgreSQL, Ollama, n8n)
  ├── backups/             ← DB backups
  ├── repositories/        ← All 1600 cloned repos (symlink on Mac: ~/repos → T7)
  └── cache/               ← LLM caches
```

**Keep on Mac SSD:**
- `~/Documents/` (active projects + git work)
- Docker Desktop storage
- `~/.config/`, `~/.local/`

**Effort:** 3-4 hours (copy + symlinks)  
**Milestone:** Mac SSD <60GB. All services still access T7 data via Tailscale paths.

### Phase 3: Network Topology (Wed–Fri)
**Owner:** You (Infrastructure)  
**Goal:** Every service has a name, port, and documented connection path.

**Deliverable:** `NETWORK-MAP.md` + `NETWORK-DIAGRAM.svg`

```
MacBook Air (100.121.17.63)
├─ Port 3000: TwentyHQ (CRM)
├─ Port 5432: PostgreSQL
├─ Port 6379: Redis
├─ Port 3001: Grafana
├─ Port 7474: Neo4j (browser)
├─ Port 6333: Qdrant (vector DB)
└─ Port 8080: OmniRouter (central control plane)

Mac Studio (100.87.214.70) — GPU Worker
├─ Port 11434: Ollama (inference + embeddings)
├─ Port 4000: LiteLLM (model routing proxy)
├─ Port 5678: n8n (workflow orchestration)
└─ Port 3004: TwentyHQ (secondary CRM instance)

Both connected via Tailscale VPN (private network layer)
```

**Milestone:** One network diagram. Every service addressable. Zero manual IP lookups.

---

## WEEK 2: Knowledge Graph + Repository Indexing

### Phase 4: Knowledge Graph (Mon–Wed)
**Owner:** Data Engineer (You)  
**Goal:** 712 ventures become queryable nodes + relationships in Neo4j.

**Node Types:**
- Ventures (712) — venture_id, name, sector, stage, status, owner
- Products (1000+) — product_id, name, venture_id, revenue
- Customers/Leads — customer_id, venture_id, status, value
- Repositories (1600) — repo_id, name, owner, language, dependencies
- Playbooks, Contracts, Marketing Assets

**Relationships:**
- `(Venture)-[:PRODUCES]->(Product)`
- `(Venture)-[:SERVES]->(Customer)`
- `(Venture)-[:USES]->(Repository)`
- `(Repository)-[:DEPENDS_ON]->(Repository)`
- `(Product)-[:GENERATES]->(Revenue)`
- `(Playbook)-[:APPLIES_TO]->(Venture)`

**Milestone:** Neo4j browser shows 712 ventures. One Cypher query: "All CON ventures + their products".

### Phase 5: Repository Indexing (Wed–Fri)
**Owner:** Repo Intel Agent (You)  
**Goal:** Every repo has metadata. Every repo knows its venture.

**Metadata per repo:**
```json
{
  "repo_id": "repo-123",
  "name": "vex-hero-site",
  "purpose": "Portfolio landing pages for ventures",
  "owner": "TECH-050",
  "language": "typescript",
  "dependencies": ["react", "next.js", "tailwind"],
  "agent": "portfolio_generator",
  "company": "TECH-050",
  "product": "vex-portfolio",
  "sector": "technology",
  "status": "active",
  "last_updated": "2026-07-20"
}
```

**Output:** `REPOSITORY-REGISTRY-COMPLETE.json` (1600 repos fully indexed)

**Milestone:** Graphify + Neo4j synced. Query: "All active repos for CON sector".

---

## WEEK 3: Sector Engines Deployment (Sales Automation)

### Phase 6: Sector Landing Pages + Lead Capture (Mon–Fri)

**Goal:** Each sector becomes an automated sales engine (not just a website).

**For each sector: CON, STA, RE, EDU, FIN, LOG**

```
Landing Page (lead capture form)
  ↓
CRM (venture_classifier agent routes lead)
  ↓
Estimator (estimator_gen1 agent generates quote)
  ↓
Proposal Generator (LLM creates proposal)
  ↓
Scheduling (project_scheduler reserves capacity)
  ↓
Invoicing (n8n workflow creates invoice)
  ↓
Customer Portal (self-serve status + document upload + payment)
  ↓
Knowledge Base + Email Sequences
```

**Deploy this week (already have templates):**
1. **CON** (Construction) — vex-hero-site integration → lead form → venture_classifier
2. **EDU** (Education) — ET-011 landing kit → course sign-up → enrollment_optimizer
3. **TECH** (Technology) — Securify hero page → contact form → triage agent

**Follow next week (Weeks 4):**
4. **STA** (Staffing) → contractor application → candidate_matcher
5. **RE** (Real Estate) → property inquiry → lead_qualifier
6. **LOG** (Logistics) → freight quote → route_optimizer

**Milestone:** 3 sector engines live. Each captures leads → agent workflow → CRM. $5K+ in pipeline captured.

---

## WEEK 4–6: Scaling + Revenue Generation

### Week 4: Complete Sector Engines (3 more sectors)
**Goal:** All 6 sectors operational with agent automation.

### Week 5: Delegation Model Live
**Goal:** CEO Agent + organization hierarchy.

```
CEO Agent (You)
  ├─ COO (Operations) → CON/STA/RE directors (TIER 1 revenue)
  ├─ CTO (Infrastructure) → IZA OS health
  ├─ CMO (Marketing) → Sector engines + content
  ├─ CFO (Finance) → FIN OPCO + risk monitoring
  └─ Data Officer → Neo4j curation + Qdrant indexing
```

**Milestone:** 12 agents live. Autonomy ratios tracked. 70%+ agents at >90% success rate.

### Week 6: Revenue Phase
**Goal:** First ventures generating $5K-15K/month via automation.

**Milestone:** Layer 1 ventures profitable. Zero manual work. CEO Agent makes decisions.

---

# MISSION CONTROL FILES (Open First)

These 12 files guide all decisions. Keep them open in tabs.

| # | File | Purpose | Status |
|---|------|---------|--------|
| 1 | `AGENTS.md` | Agent registry + authority levels | ✅ Exists |
| 2 | `TEAMS.md` | Team structure + escalation paths | ✅ Exists |
| 3 | `DEPARTMENTS.md` | Economic models + 100+ principles | ✅ Exists |
| 4 | `TECH-STACK-ARCHITECTURE.md` | Tools inventory + readiness % | ✅ Exists |
| 5 | `docker-compose.yml` | All services as code | ⏳ Week 1 |
| 6 | `.env` | Configuration (from .env.example) | ⏳ Week 1 |
| 7 | `REPOSITORY-REGISTRY.json` | All 1600 repos metadata | ⏳ Week 2 |
| 8 | `VENTURE-REGISTRY.csv` | All 712 ventures | ✅ Exists |
| 9 | `NETWORK-MAP.md` | Every port, every service, every path | ⏳ Week 1 |
| 10 | `OMNIROUTER-CONFIG.yaml` | Central routing rules | ⏳ Week 1 |
| 11 | `MCP-REGISTRY.json` | All MCP servers + tools + triggers | ⏳ Week 1 |
| 12 | `PROMPT-LIBRARY-150.md` | All 150+ prompts by domain | ⏳ Week 2 |

---

# ALTERNATIVES TO n8n (Code-First Approach)

Use n8n for visual automation (marketing, sales) only. Infrastructure runs on:

| Use Case | Tool | Trigger | Executor | Log |
|----------|------|---------|----------|-----|
| **Scheduled jobs** | Python `schedule` lib | Cron | CLI | PostgreSQL |
| **Webhook handlers** | FastAPI | HTTP POST | Async function | Supabase |
| **Event streams** | Redis Streams | Consumer group | Python listener | Neo4j |
| **Durable workflows** | Temporal | Scheduled workflow | Workflow engine | Temporal UI |
| **MCP triggers** | MCP server | Event from MCP | Handler function | Langfuse |
| **GitHub integration** | GitHub Actions | Push/schedule | Python script | Supabase |

**Why?** Code is version-controlled, auditable, and testable. n8n becomes UI for non-technical teams (marketing sequences, sales follow-ups).

---

# DISCOVERY: Tools + MCPs + Triggers + Crons Currently Mentioned

| Tool/MCP | Trigger Method | Scheduling | Owner | Status |
|----------|---|---|---|---|
| CrewAI | CLI / webhook | Manual/scheduled | con_crew_orchestrator.py | ⏳ Wire to n8n |
| n8n | UI workflow | Cron inside workflow | Zapier zaps + workflows | ✅ Running |
| Langfuse | LLM call | Auto-capture | Instrumented agents | 🔴 No app instrumentation |
| Temporal | Workflow API | Durable workflows | Not yet integrated | ⏳ Week 5 |
| GitHub Actions | git push / schedule | `.github/workflows/*.yml` | Not yet integrated | ⏳ Week 5 |
| MCP servers | Register in .claude/mcp-config.json | Via Claude Code | 11 MCPs live | ✅ Ready |
| Redis Streams | Event publish | Consumer groups | Not yet integrated | ⏳ Week 4 |
| FastAPI webhooks | HTTP POST | Manual/external trigger | Not yet integrated | ⏳ Week 3 |

---

# 150+ PROMPT LIBRARY (Structured)

**10 Domains × 15 prompts each = 150 prompts**

Each prompt produces a document/dataset for the next stage. All prompts reference AGENTS.md + MASTER-EXECUTION-PLAN.md.

## Domain 1: Infrastructure & Networking (Prompts 1–15)
- Prompt 1: Inventory all running services (docker ps)
- Prompt 2: Generate network topology diagram
- Prompt 3: Audit Docker volumes + bind mounts
- Prompt 4: Validate OmniRouter routing rules
- Prompt 5: Verify Tailscale network security
- ... 6–15 (detailed infra automation)

## Domain 2: Storage & Data Lifecycle (Prompts 16–30)
- Prompt 16: Audit Mac SSD by folder
- Prompt 17: Plan T7 folder structure
- Prompt 18: Create symlink strategy for repos
- Prompt 19: Backup validation script
- ... 20–30 (storage automation)

## Domain 3: Repository Audit (Prompts 31–45)
- Prompt 31: Classify 1600 repos by purpose
- Prompt 32: Identify duplicates + archived
- Prompt 33: Map repos to ventures
- ... 34–45 (repo indexing)

## Domain 4: Knowledge Graph (Prompts 46–75)
- Prompt 46: Design venture schema
- Prompt 47: Load 712 ventures to Neo4j
- Prompt 48: Create relationship types
- ... 49–75 (graph expansion)

## Domain 5: Agent Orchestration (Prompts 76–105)
- Prompt 76: Wire CrewAI ✅ Done 07/20
- Prompt 77: Create agent trigger system
- Prompt 78: Design delegation pyramid
- ... 79–105 (agent automation)

## Domain 6: Sector Engines (Prompts 106–150)
- Prompt 106: Deploy CON landing page
- Prompt 107: Deploy STA landing page
- Prompt 108: Deploy RE landing page
- ... 109–150 (sales + marketing engines)

---

# OMNIROUTER CONFIGURATION (Mac Studio Control Plane)

```yaml
# omnirouter-config.yaml
# Central routing logic for all requests

router:
  name: "IZA OS OmniRouter"
  listen_port: 8080
  log_destination: "/Volumes/T7/Shield/14_INFRASTRUCTURE/logs/omnirouter.log"

model_selection:
  rules:
    - if: "task == 'code_generation'"
      then: "qwen2.5:32b (Mac Studio Ollama)"
      fallback: "gpt-4 (Claude API)"
    
    - if: "task == 'embeddings'"
      then: "nomic-embed-text (Ollama local)"
      fallback: "none (local only)"
    
    - if: "task == 'complex_reasoning'"
      then: "claude-opus (via LiteLLM)"
      fallback: "gpt-4"

routing_table:
  # Agent requests → appropriate service
  agent_request:
    - destination: "Neo4j:7474"
      purpose: "Knowledge graph query"
    
    - destination: "Qdrant:6333"
      purpose: "Vector search"
    
    - destination: "PostgreSQL:5432"
      purpose: "Transactional data"
    
    - destination: "Ollama:11434"
      purpose: "Local inference"
    
    - destination: "LiteLLM:4000"
      purpose: "Model routing + fallback"

failover:
  - primary: "Ollama:11434"
    secondary: "LiteLLM:4000 → Claude API"
    timeout_ms: 5000

scheduling:
  - cron: "0 6 * * *"
    task: "Knowledge graph sync"
    executor: "populate_venture_knowledge_graph.py"
  
  - cron: "0 12 * * *"
    task: "Storage health check"
    executor: "storage-validation.sh"
  
  - cron: "0 */4 * * *"
    task: "Agent success rate recalculation"
    executor: "agent-metrics-update.py"
```

---

# SUCCESS METRICS (End of Week 6)

| Metric | Target | Status |
|--------|--------|--------|
| Mac SSD free space | >100GB | 🔴 19GB → 🟢 120GB |
| Docker containers healthy | 12+ | ⏳ Week 1 |
| Services on Tailscale | 100% | ⏳ Week 1 |
| Ventures in Neo4j | 712 | ⏳ Week 2 |
| Repos fully indexed | 1600 | ⏳ Week 2 |
| Sector engines live | 6 | ⏳ Week 3–4 |
| Agents at >90% autonomy | 70%+ | ⏳ Week 5 |
| Monthly revenue (Layer 1) | $5K–15K | ⏳ Week 6 |
| Manual work required | 0 hours | ⏳ Week 6 |

---

**NEXT ACTION:** Start Week 1, Phase 2 (Storage Cleanup) TODAY.
Goal: Free 100GB on Mac SSD by EOD.
