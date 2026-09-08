# CLAUDE.md — Company Brain Infrastructure Layer

[[STARTHERE]] | [[REALITY]] | [[00-CONSTITUTION]] | [[INDEX-DOMAINS-COMPLETE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]

**Scope:** Local-first AI infrastructure for Company Brain (integrated multi-layer platform)  
**Updated:** 2026-09-06 (Strategic architecture redesign)  
**Authority:** Infrastructure Control Plane (CP-027) + Multi-layer Platform Architecture

---

## VERIFIED STATE — 2026-09-05 (corrects stale claims below)

Live-audited via a new `macstudio` [[Docker Context|Docker context]] (this machine has no local daemon — no colima, no OrbStack — `docker --context macstudio` reaches Mac Studio's daemon over SSH/Tailscale; set as the default context in `~/.zshrc`, `docker` PATH fixed in Mac Studio's `~/.zshenv` for non-interactive SSH).

- **The duplicate-infrastructure problem above is RESOLVED as of 2026-09-05 (re-verified same day, hours later).** `docker --context macstudio ps -a` now shows only one instance each of Neo4j, Qdrant, Redis (`civos_*`), plus the intentionally-separate `crm-postgres`. Only 3 `t7shield-*` containers remain and all are `Exited (255)` 2 days ago (`t7shield-litellm-1`, `t7shield-prometheus-1`, `t7shield-otel-collector-1`) — someone tore the rest of that stack down without updating this doc. No `buzz-*` containers exist at all. `civos_neo4j` is confirmed canonical and healthy (7474/7687 responding 200).
- **`t7shield-neo4j-1` no longer exists** — not stopped, not present at all in `docker ps -a`. The crash-loop this doc previously described is moot; nothing to clean up.
- **Grafana does not exist as a container right now — not on port 3010, not on 3011, not anywhere.** `civos_webui` (:3010) is confirmed Open WebUI, not Grafana. `t7shield-grafana-1` (previously claimed on :3011) is gone — not in `docker ps -a` at all. The observability layer currently has **no dashboard**, only Langfuse (tracing, still receiving zero traffic per the callback-wiring gap below).
- **Ollama is NOT dead — corrects the 2026-09-05 claim below that it was.** Live-checked on Mac Studio 2026-09-05: `ollama serve` has been running 4d20h, listening on `*:11434` (all interfaces + Tailscale `mac-studio.tailba9617.ts.net:11434`), serving 6 models including `nomic-embed-text`, `qwen2.5-coder:14b`, `hermes3`, `llama3.1:8b`, plus two `ollama.com` cloud passthroughs (`minimax-m2.5:cloud`, `kimi-k2.5:cloud`). The "Ollama is dead" narrative came from a comment in `civos_litellm`'s `litellm-config.yaml` written 2026-07-17 ("Ollama service itself was down") that was never re-verified — Ollama came back and nobody updated the config or this doc. The `embed` route (→ `ollama/nomic-embed-text`) is disabled on that stale assumption, not because it's actually broken.
- **exo is not limited to one model — it has 120 in its catalog.** `curl http://100.87.214.70:52415/v1/models` returns 120 entries (Qwen3-Coder-480B-A35B, GLM-5.1, DeepSeek-V3.2, Llama-3.3-70B, MiniMax-M2.7, gpt-oss-120b, etc.), not just `mlx-community/Qwen3.6-35B-A3B-5bit`. LiteLLM only routes to that one because its `model_list` only *has* that one wired — see the routing-gap bullets below.
- **This is the actual reason OmniRoute "isn't routing to other models or Ollama"** (user question, 2026-09-05): `civos_litellm`'s `model_list` defines exactly 6 `model_name` entries — `qwen-fast`, `qwen-heavy`, `default`, `embed`, `claude-sonnet`, `claude-haiku` — and `qwen-fast`/`qwen-heavy`/`default` all point at the *same single* exo model as a 2026-08-12 emergency stopgap ("pointing both aliases at it so calls succeed today; split them again once a second/smaller instance is actually placed" — never done). None of exo's other 119 models, and none of Ollama's 6 live models, are reachable through LiteLLM/OmniRoute — not because routing is broken, but because they were never registered. Nothing downstream of the config file is at fault.
- **OmniRoute and `civos_litellm` sit on separate Docker networks.** `omniroute` is on the default `bridge` network (172.17.0.3); `civos_litellm` is on `civos-network` (172.18.0.14) with container-DNS aliases `litellm`/`civos_litellm`. They have no shared network, so anything inside OmniRoute calling `http://litellm:4000` would fail — only `http://host.docker.internal:4000` crosses that boundary. Not independently confirmed whether OmniRoute's own provider config (stored in its private `storage.sqlite`, not inspected) actually uses the host-mapped route or is broken by this — check via the OmniRoute dashboard's provider list, not this doc.
- **[[Langfuse]] (`civos_langfuse`, :3003) is healthy but receiving zero traffic** — neither `civos_litellm`'s config nor OmniRoute's `.env` wires a Langfuse callback. The [[Observability|observability layer]] is infrastructure-only right now, not actually capturing anything. See [[OmniRoute Routing Gaps]] below.
- **[[LiteLLM]]'s `router_settings.routing_strategy` is now `usage-based-routing-v2`** — corrects the earlier claim on this line that it was `simple-shuffle`. The live config's own comment confirms the change: `routing_strategy: usage-based-routing-v2  # was simple-shuffle — now scores by deployment latency/tpm/rpm usage`. Someone fixed this since the doc was last written and didn't update the doc. Fallback chains ARE real and working (`default`/`qwen-heavy`→`claude-sonnet`, `qwen-fast`→`claude-haiku`, plus context-window fallbacks `qwen-fast`→`qwen-heavy`). Response caching is on but exact-match (Redis), not semantic.

### OmniRoute Routing Gaps (vs. the 22-point routing-control-plane target architecture)

| Gap | Fix effort | Notes |
|---|---|---|
| No scored routing (quality/cost/latency) | Low | LiteLLM supports `usage-based-routing-v2` / `latency-based-routing` natively — config change, no new code |
| Langfuse disconnected | Low | Add `success_callback: ["langfuse"]` to `civos_litellm` config + API keys — native LiteLLM↔Langfuse integration |
| No outcome-based routing (learn from trace data) | Medium, blocked on above | Needs Langfuse actually collecting data first |
| No Capability Router (Layer 9: 26 AGT-*, ~300 CAP-*) | High, architecture decision | Candidate: `different-ai/openwork` — `search_capabilities`/`execute_capability` MCP, see [[oss-integration-candidates-2026-09-05]] |
| No Agent Router (hub + per-task orchestrator) | High | Candidate: `agentlas-ai/Agentlas-OS` |
| No Policy Engine enforcement | Medium | Candidate: `roboticforce/agent-guardrails` |
| No bitemporal Routing Knowledge Graph | High, requires explicit buy-in | Candidate: `deeplethe/utopia` — competes with Neo4j/Qdrant, not a bolt-on, see [[oss-integration-candidates-2026-09-05]] |
| No Context Compiler (Neo4j+Qdrant fan-out → ranked/compressed context) | High | No candidate identified yet |
| exo's 120-model catalog not exposed — only 1 of 120 wired into LiteLLM (`qwen-fast`/`qwen-heavy`/`default` all alias the same model) | Low | Add real `model_list` entries per desired exo model; no code, config-only |
| Ollama's 6 live models unreachable — `embed` route disabled on a stale "Ollama is down" comment; Ollama has actually been up 4d20h+ | Low | Re-point `embed` at `http://host.docker.internal:11434`, re-test, remove stale comment |
| OmniRoute (`bridge` network) and `civos_litellm` (`civos-network`) share no Docker network | Unverified severity | Confirm whether OmniRoute's own provider config uses `host.docker.internal:4000` (would work) or the container DNS name `litellm` (would silently fail) — check OmniRoute dashboard provider list directly |

---

## REPOSITORY INTELLIGENCE SYSTEM (2026-09-06)

### Two-Layer Architecture

**Layer 1: Interactive (Agency Personas — Human-Guided)**
- [[repo-advisor]]: Strategic repository evaluation, venture mapping, adoption decisions
- [[repo-deep-dive]]: Forensic code review, production-readiness audit, risk quantification
- Activation: Natural language in Claude Code ("activate repo-advisor")
- Purpose: Expert guidance, edge-case resolution, human-in-the-loop validation

**Layer 2: Autonomous (Company Brain Agents + MCP — Fractal-Managed)**
- **AGT-013** (repo-classifier-agent): Classify repos into ontology (via MCP)
- **AGT-014** (repo-scorer-agent): Score on 10 dimensions (via OmniRoute MCP)
- **AGT-015** (repo-disposition-agent): ADOPT/INTEGRATE/FORK/REFERENCE/MONITOR decisions
- **AGT-017** (repo-adoption-agent): Sandbox testing, benchmarking, security scanning
- **AGT-018** (repo-monitor-agent): Weekly health checks (autonomous L3)
- Activation: ClickUp tasks, Fractal event loop (L1/L2/L3 autonomy levels)
- Purpose: Bulk processing, scale execution, knowledge graph integration

### MCP Tools for Repository Intelligence

**New tools added to `_MCP/fastmcp_server.py`:**

```
neo4j_query_entities(entity_type, limit=50)
  └─ Query Neo4j for entities by type (Capability, Venture, ExternalRepository)
  └─ Returns: Matching entities with full properties

neo4j_merge_classification(repo_id, classification)
  └─ Merge repo classifications into Neo4j knowledge graph
  └─ Input: {primary_capability, secondary_capabilities, architecture_layer, sector_relevance, score, tier}
  └─ Returns: Updated node properties + timestamp

omniroute_route_model(task_type, complexity)
  └─ Route to appropriate model via OmniRoute based on task complexity
  └─ Input: task_type ('classify', 'score', 'disposition', 'adopt'), complexity (1-10)
  └─ Returns: Recommended model + provider + estimated cost
```

### Integration Flow

```
Layer 1 (Interactive)                Layer 2 (Autonomous via MCP)
────────────────────                 ──────────────────────────
repo-advisor (ask)  ←──┐
                       │
repo-deep-dive      ←──┼─── AGT-013 (classify)
(edge cases)            │    ├─ neo4j_query_entities()
                        │    ├─ omniroute_route_model()
                        │    └─ neo4j_merge_classification()
                        │
                        ├─── AGT-014 (score)
                        │    ├─ neo4j_query_entities()
                        │    └─ omniroute_route_model()
                        │
                        ├─── AGT-015 (disposition)
                        │    └─ neo4j_merge_classification()
                        │
                        └─── AGT-017/AGT-018 (adopt/monitor)
                             └─ neo4j_query_entities()

              ↓
         Neo4j Knowledge Graph
         (20,363 edges updated)
```

### Execution Status

- ✅ **Agency Personas Created** (2026-09-06)
  - `~/.claude/agents/repo-advisor.md` (registered)
  - `~/.claude/agents/repo-deep-dive.md` (registered)

- ✅ **MCP Tools Wired** (2026-09-06)
  - fastmcp_server.py extended with 3 new tools
  - OmniRoute integration ready
  - Neo4j query + merge ready

- ✅ **Task List Updated** (2026-09-06)
  - [[REPOSITORY-INTELLIGENCE-TASK-LIST.md]] uses two-layer model
  - Phases 1-3 (ingest/normalize/enrich) autonomous only
  - Phases 4-6 (classify/score/disposition) use Layer 1+2
  - Phases 7-9 (graph/adopt/awesome) autonomous only

### What's Next

**Week 1 (Sep 6-12):**
- Phase 1-3: Ingest 904 repos, normalize, enrich metadata
- Launch repo-ingestion-agent (AGT-010)

**Week 2 (Sep 13-19):**
- Phase 4-6: Classify, score, disposition
- Activate repo-advisor persona for top 50
- Activate repo-deep-dive for high-risk repos

**Week 3 (Sep 20-26):**
- Phase 7-8: Neo4j loading, adoption pipeline
- AGT-018 weekly monitoring

**Week 4 (Sep 27-Oct 3):**
- Phase 9: Awesome lists integration, unified registry

---

## BUZZ COLLABORATION LAYER (2026-09-06)

### Integration Overview

**Problem:** Repository Intelligence System runs autonomously without human visibility during Phase 4-6 (Classify/Score/Disposition). Agents publish to Neo4j silently; humans review results post-facto.

**Solution:** Deploy [[Buzz|Buzz]] as **CP-028 (Collaboration Control Plane)** to enable real-time human-AI collaboration with cryptographic audit trails.

### Architecture

```
Layer 1 (Interactive)        Layer 2 (Autonomous)       Buzz Workspace         Persistence
────────────────────        ───────────────────        ───────────────       ─────────────
repo-advisor          ←──────  AGT-013 (classify)  ──→  #repo-classification  ──→  Neo4j
repo-deep-dive        ←──────  AGT-014 (score)    ──→  #repo-scoring        ──→  Neo4j
(human review)               AGT-015 (disposition) ──→  #repo-disposition    ──→  Neo4j
                             AGT-017 (adopt)      ──→  #repo-adoption-pipeline
                                                         ↓
                                                  [buzz-sync-agent]
                                                  (event thread → Neo4j)
```

### Key Features

- ✅ **Agents as Workspace Members:** AGT-013/014/015 publish events to Buzz channels (not silent Neo4j writes)
- ✅ **Human Feedback Loop:** repo-advisor reads events, asks clarifying questions in same channel
- ✅ **Audit Trail:** Every decision documented with conversation history in Buzz + Neo4j
- ✅ **Real-Time Collaboration:** Personas and agents respond to mentions in real-time
- ✅ **Approval Gates:** Humans can override agent decisions before Neo4j sync

### Deployment Timeline

| Week | Phase | Goal | Status |
|------|-------|------|--------|
| Sep 6-12 | Infrastructure | Deploy Buzz relay, PostgreSQL, Redis, MinIO on Mac Studio | 🟡 Starting |
| Sep 13-19 | Agent Integration | MCP bridge, rewire AGT-013/014/015 to publish to Buzz | 🟡 Queued |
| Sep 20-26 | Sync & Persistence | buzz-sync-agent merges Buzz threads → Neo4j | 🟡 Queued |
| Sep 27-Oct 3 | Full Pipeline | Phase 4-6 running with Buzz collaboration + 904 repos | 🟡 Queued |

### What's Different

**Before Buzz (Autonomous Only):**
```
904 repos → AGT-013 classifies → Neo4j ✅ (silent, no human input during phase 4)
```

**After Buzz (Collaborative):**
```
904 repos → AGT-013 publishes to #repo-classification channel
              ↓
         repo-advisor reviews: "Why CAP-027? Looks like CAP-015 to me"
              ↓
         AGT-013 responds: "CAP-015 needs X, this only has Y"
              ↓
         AGT-013 updates classification
              ↓
         buzz-sync-agent publishes to Neo4j with full audit trail ✅
```

### Status

- ✅ **Integration Plan Created** (2026-09-06): [[BUZZ-INTEGRATION-PLAN.md]]
- ✅ **CP-028 Defined** (Collaboration Control Plane)
- 🟡 **Phase 1 Ready to Deploy** (infrastructure setup week of Sep 6)
- 🟡 **MCP Bridge Pending** (buzz_publish_event, buzz_read_channel, buzz_sync_to_neo4j)
- 🟡 **Agent Rewiring Pending** (AGT-013/014/015 → Buzz channels)
- 🟡 **buzz-sync-agent Pending** (AGT-019: event thread → Neo4j)

---

## COMPANY BRAIN ARCHITECTURE — MULTI-LAYER PLATFORM (2026-09-06)

### Strategic Redesign: From Tool Collection to Integrated Platform

Company Brain is not a collection of tools. It's an integrated multi-layer platform where six complementary systems work together.

**The realization:** Three outstanding repos (Comp AI CRM, Twenty, Buzz) don't compete—they are three different layers of the same system.

### The Six Layers

```
                    COMPANY BRAIN PLATFORM
                         │
         ┌───────────────┼────────────────┐
         │               │                │
    KNOWLEDGE          ACTION           SYNC
         │               │                │
    ┌────┴────┐     ┌────┴────┐    ┌─────┴─────┐
    ↓         ↓     ↓         ↓    ↓           ↓
  Neo4j    Qdrant ClickUp   Buzz  Agents   Github
    │         │     │        │
    └─────────┼─────┴────────┘
              ↓
       Knowledge Graph
          (unified view)
```

### System Roles (Clear Boundaries)

| Layer | System | Purpose | Owns | Control Plane |
|-------|--------|---------|------|---|
| **Knowledge** | Neo4j + Qdrant | Relationships, entities, facts, semantics | Organizational knowledge | CP-013 |
| **Intelligence** | Comp AI CRM | Research, evidence, enrichment, discovery | Evidence ledger, entity resolution | CP-031 (NEW) |
| **Business** | Twenty | CRM, companies, deals, custom objects | Business entities, opportunities | CP-032 (NEW) |
| **Execution** | ClickUp | Goals, tasks, projects, accountability | Work tracking, deadlines, dependencies | CP-033 (NEW) |
| **Collaboration** | Buzz | Rooms, events, agents, artifacts | Decision threads, human-agent interaction | CP-028 |
| **Engineering** | GitHub | Repositories, code, CI/CD | Source code, deployment pipelines | CP-034 (NEW) |

### Key Distinctions (What Each Does NOT Own)

- **ClickUp is NOT the knowledge graph** → ClickUp tasks reference Neo4j entities for context
- **Neo4j is NOT the execution tracker** → ClickUp owns accountability, deadline tracking
- **Twenty is NOT the sole customer truth** → Comp AI enriches with discovered facts
- **Buzz is NOT a persistence layer** → Events sync to Neo4j for durability
- **GitHub is NOT business logic** → Code is source; business logic lives in Twenty/ClickUp

### Synchronization Pattern

```
Discovery (Comp AI Research Agent)
    ↓ Evidence recorded
Neo4j Updated (entity relationships)
    ↓ Webhook triggered
Twenty Updated (company/person/deal)
    ↓ Workflow automation
ClickUp Project Created (adoption work)
    ↓ Task assigned
Buzz Notification (team context)
    ↓ Agent reads context
Agent Executes (with full business understanding)
    ↓ Task updated
Result → Neo4j (closes loop)
```

### Repository Intelligence Produces Work (Not Just Reports)

**Before:** 904 repos → Scored → Listed in registry  
**After:** 904 repos → Disposed (TRIAL/ADOPT/FORK) → ClickUp project created → Weekly monitoring → Results tracked

### New Control Planes

- **CP-031** (Intelligence): Comp AI CRM research + evidence layer
- **CP-032** (Business Operations): Twenty CRM + business entities
- **CP-033** (Execution): ClickUp tasks + projects + accountability
- **CP-034** (Engineering): GitHub repositories + code

### Implementation Phases

| Phase | Timeline | Deliverable |
|-------|----------|---|
| **Phase 1** | Sep 6-26 | Buzz deployed + Repository Intelligence collaboration |
| **Phase 2** | Oct 1-31 | Comp AI CRM deployed (Intelligence layer) |
| **Phase 3** | Nov 1-30 | Twenty deployed (Business operations layer) |
| **Phase 4** | Dec 1-31 | Full integration + unified dashboards |

### Status

- ✅ **Architecture defined**: [[COMPANY-BRAIN-ARCHITECTURE.md]] (783 lines, complete system design)
- ✅ **Buzz integration planned**: [[BUZZ-INTEGRATION-PLAN.md]] + [[BUZZ-PHASE1-DEPLOYMENT.md]]
- 🟡 **Comp AI CRM evaluation**: Identified as TRIAL candidate (research + evidence layer)
- 🟡 **Twenty evaluation**: Identified as TRIAL candidate (business operations layer)
- 🟡 **System synchronization**: Layer design complete, implementation pending

---

## SESSION SUMMARY (2026-09-02 to 2026-09-04)

### Objective
Deploy complete local-first AI infrastructure for Company Brain with proper device assessment, model deployment, observability, and OmniRoute integration across Tailscale network.

### Architecture Aligned To
- **Layer 11: Loop Engineering** [[Loop Engineering]] (execution, autonomy levels L1/L2/L3)
- **Layer 15: Execution** [[Execution]] (infrastructure for AI workloads)
- **Layer 16: Observability** [[Observability]] (monitoring + telemetry)
- **AI/Agent Layer** [[Agents]] + [[Models]] (model routing, fallback, provider management)

### Control Planes Connected
- **CP-006** [[Agents|Agent Control Plane]] — agents using OmniRoute for inference
- **CP-007** [[Models|Model Control Plane]] — model selection + routing decisions
- **CP-013** [[Knowledge Control Plane]] — embeddings via Qdrant + Neo4j
- **CP-020** [[Financial Control Plane]] — cost tracking by model/provider
- **CP-027** [[Infrastructure Control Plane]] — this layer (databases, services)
- **CP-028** [[BUZZ-INTEGRATION-PLAN|Collaboration Control Plane]] — human-AI collaboration via Buzz relay (Phase 1 deployment Sep 6-26)
- **CP-029** [[Observability]] — Grafana dashboards + Langfuse tracing

---

## INFRASTRUCTURE STATUS

### Deployed & Running ✅

| Component | Purpose | Port | Status | Location |
|-----------|---------|------|--------|----------|
| **OmniRoute** | AI provider gateway + model routing | 20128 | ✅ LIVE | Mac Studio (Docker) |
| **Neo4j** | Knowledge graph + relationships | 7687/7474 | ✅ LIVE | Mac Studio (Docker) |
| **Qdrant** | Vector database + semantic search | 6333 | ✅ LIVE | Mac Studio (Docker) |
| **LiteLLM** | Model abstraction layer | 4000 | ✅ LIVE | Mac Studio (Docker) |
| **Grafana** | Observability dashboards | 3011 (not 3010 — see VERIFIED STATE) | ✅ LIVE (`t7shield-grafana-1`) | Mac Studio (Docker) |
| **Langfuse** | LLM tracing + evaluation | 3003 | ✅ LIVE but receiving no traffic — see VERIFIED STATE | Mac Studio (Docker, `civos_langfuse`) |
| **PostgreSQL** | Operational database | 5433+ | ✅ LIVE | Mac Studio (Docker) |
| **Redis** | Caching + state | 6379+ | ✅ LIVE | Mac Studio (Docker) |

### Hardware Inventory

**Mac Studio M4** (100.87.214.70 via Tailscale)
- CPU: 12-core M4 Max
- Memory: 36GB unified
- Storage: 512GB internal + 4TB LaCie external
- Role: Primary inference server + database host
- Network: Tailscale direct (192.168.1.11)

**MacBook Air M-series** (100.121.17.63 via Tailscale)
- CPU: 8-core M-series
- Memory: 16GB unified
- Storage: 228GB internal + 1.8TB T7 Shield external
- Role: Secondary inference agent
- Network: Tailscale online

### OmniRoute Provider Wiring (2026-09-07)

**Configuration file:** [[omniroute-providers.yaml|_INFRASTRUCTURE/omniroute/omniroute-providers.yaml]]
- 5 providers defined (Mac Air Ollama, Mac Studio exo, Mac Studio Ollama fallback, Anthropic Claude, + OmniRoute internal)
- 289+ models exposed with routing rules
- Fallback chains for code/reasoning/embedding tasks
- Cost + latency optimization built-in

**Deployment:** Copy to OmniRoute container and reload (Docker restart or API reload).

**Status:** Config created 2026-09-07. Deployment pending (step-by-step in OMNIROUTE-MODELS-ROUTING.md).

### Model Inventory

Live-audited 2026-09-05 (`curl :11434/api/tags`, `curl :52415/v1/models`) — supersedes every row this table had before.

| Model | Size | Status | Location | Runtime | Reachable via LiteLLM/OmniRoute? |
|-------|------|--------|----------|---------|---|
| qwen2.5-coder:14b | 9GB | ✅ RUNNING — Ollama never actually died | Mac Studio ~/.ollama | Ollama (:11434) | ❌ not wired |
| nomic-embed-text | 274MB | ✅ RUNNING — `embed` route just disabled on stale assumption | Mac Studio ~/.ollama | Ollama (:11434) | ❌ route exists but disabled |
| hermes3:latest | 4.7GB | ✅ RUNNING | Mac Studio ~/.ollama | Ollama (:11434) | ❌ not wired |
| llama3.1:8b | 4.9GB | ✅ RUNNING | Mac Studio ~/.ollama | Ollama (:11434) | ❌ not wired |
| minimax-m2.5:cloud, kimi-k2.5:cloud | — | ✅ RUNNING (ollama.com cloud passthrough) | — | Ollama (:11434) | ❌ not wired |
| mlx-community/Qwen3.6-35B-A3B-5bit | — | ✅ RUNNING, aliased as `qwen-fast`/`qwen-heavy`/`default` in LiteLLM | Mac Studio, native | exo (:52415) | ✅ wired (only one) |
| 119 other exo-catalog models (Qwen3-Coder-480B-A35B, GLM-5.1, DeepSeek-V3.2, Llama-3.3-70B, MiniMax-M2.7, gpt-oss-120b, …) | varies | ✅ available in exo's catalog, load-on-demand | Mac Studio, native | exo (:52415) | ❌ not wired — see routing-gap table above |
| qwen2.5:32b / 72b | 19GB / 43GB | Unverified this session — predates the Ollama→exo confusion, not re-checked | T7 Shield | — | ❌ |

---

## CREDENTIALS & ACCESS

**Moved to Bitwarden 2026-09-05** — this section previously stored real plaintext passwords in a git-tracked file (see `.planning/codebase/CONCERNS.md` for the finding). Credentials now live in Bitwarden; this file only records where to find them and what they unlock. Rotate the OmniRoute and SSH passwords that were exposed here before treating this as closed — commit history still has them until a `git filter-repo` purge.

### OmniRoute
```
URL: http://100.87.214.70:20128
Dashboard: http://100.87.214.70:20128/dashboard
Email: admin@omniroute.local
Password: → Bitwarden item "OmniRoute — Company Brain"
Status: ✅ Deployed, login verified (as of last check — password rotation pending)
```

### Mac Studio SSH
```
Host: ssh macstudio (Tailscale alias)
IP: 100.87.214.70
User: acebless
Password: → Bitwarden item "Mac Studio SSH — Company Brain"
```

### Databases
- **Neo4j**: bolt://100.87.214.70:7687 (default: neo4j/changeme — CHANGE THIS)
- **Qdrant**: http://100.87.214.70:6333
- **PostgreSQL**: postgres://admin:changeme@100.87.214.70:5433 (CHANGE THIS)

---

## COMPLETED DELIVERABLES

✅ **LLM Hardware Compatibility Registry** [[LLM Hardware Registry]]
- File: `_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml`
- Contains: Hardware profiles, model compatibility matrix, benchmark results, routing rules
- Purpose: Single source of truth for local model decisions
- Used by: [[Models|Model Control Plane]], [[Agents|Agent Routing]]

✅ **Infrastructure Registry** [[Infrastructure Inventory]]
- File: `_REGISTRIES/INFRASTRUCTURE_REGISTRY.yaml`
- Documents: Device inventory, model inventory, storage topology, deployment status
- Links to: [[17-Models|Model Inventory]], [[49-SYSTEM|System Architecture]]

✅ **Docker Compose Configuration**
- File: `_INFRASTRUCTURE/docker-compose.yml`
- Defines: Neo4j, Qdrant, PostgreSQL on LaCie 4TB storage
- Deployed on: Mac Studio via [[49-SYSTEM|System Management]]
- Related: [[08-KNOWLEDGE-GRAPH|Neo4j]], [[11-INDEXING|Qdrant Storage]]

✅ **Deployment Phases Documentation** [[Deployment Roadmap]]
- File: `_INFRASTRUCTURE/DEPLOYMENT_PHASES.md`
- 4-phase roadmap: Databases → Models → Exo → Observability
- Execution layer: [[22-EXECUTION|Execution Control Plane]]

✅ **Company Brain CLI (hand-written, not CLI-Anything-generated)** [[CLI Documentation]]
- Schema: `_CLI/schema.yaml` — Maps all 50 domains, 20 layers, 6 control planes to commands (reference doc, not a generator input)
- Documentation: `_CLI/README.md` — Full command reference + installation guide
- GitHub Actions: `.github/workflows/auto-deploy.yml` — Automated deployment pipeline
- Commands: `cb infrastructure`, `cb omniroute`, `cb neo4j`, `cb test`, `cb control-planes`
- Status: ✅ Complete and this is the permanent implementation — see corrected PENDING ITEMS note below on what CLI-Anything actually is

---

## PENDING ITEMS (for next session)

✅ **CLI-Anything: real, but not a schema generator** (corrected 2026-09-05)
- The npm packages (`@hkuds/cli-anything`, `cli-anything`) never existed — 404. That premise (`cli-anything _CLI/schema.yaml` → generates `cb`) was wrong from the start.
- What CLI-Anything (github.com/HKUDS/CLI-Anything) actually is: (1) `cli-anything-hub` on PyPI — installed in `~/.venv/company-brain` — gives `cli-hub`, a package manager for **176 pre-built agent-CLIs of real GUI apps** (Blender, OBS, Ollama, etc. — no neo4j/docker/postgres/grafana, those already have native CLIs); (2) the `cli-anything` **Claude Code plugin** — installed & enabled (user scope), 5 skills (`cli-anything`, `list`, `refine`, `test`, `validate`) that let Claude generate a new agent-CLI for any GUI app on request, via a 7-phase analyze→build→test→document pipeline.
- Neither of these consumes `_CLI/schema.yaml` or generates `cb`. `_CLI/bin/cb` (hand-written bash) remains the correct, permanent implementation for Company Brain's own domain/control-plane commands — not a stopgap.
- **Known landmine:** `/opt/homebrew/bin/cb` on PATH is an unrelated tool (`codebuff`, a different AI coding CLI) — bare `cb` from a shell resolves to codebuff, not this CLI. Always invoke `_CLI/bin/cb` explicitly, or add a shell alias, until this is renamed/resolved.

✅ **FastMCP Server** (verified working 2026-09-05)
- `_MCP/fastmcp_server.py` — 9 tools, 1 resource, 1 prompt, all import/register cleanly against fastmcp 4.0.3
- Installed in venv: `~/.venv/company-brain` (Python 3.12, since system Python is 3.9.6 and fastmcp requires ≥3.10)
- Registered in `~/.claude/settings.json` under `mcpServers.company-brain`, pointing at the venv's python3
- Fixed a real bug found on first real load: `@mcp.resource` needs a URI argument in fastmcp 4.x (`@mcp.resource("company-brain://status")`), the committed code was missing it and would have crashed on server start
- **Next:** restart Claude Code to pick up the MCP server, then verify a tool call (e.g. `infrastructure_status()`) actually round-trips

✅ **task-master-ai installed** (2026-09-05)
- `npm install -g task-master-ai` (v0.43.1) — the real package behind github.com/eyaltoledano/claude-task-master
- Not yet initialized in this project (`task-master init` not run) — evaluate before adopting, since it would replace this file's own PENDING-ITEMS-as-markdown pattern with a structured task graph

⏳ **Widen LiteLLM model_list + re-enable Ollama embed route** (found 2026-09-05, not yet fixed — needs approval, this is a production config change)
- File: `/Users/divinejohns/Iza-OS-Tree-of-Life/ops/infra/litellm-config.yaml` on Mac Studio, mounted into `civos_litellm`
- Add real `model_list` entries for whichever exo models should actually be selectable (119 of exo's 120-model catalog currently unreachable — see routing-gap table above), instead of `qwen-fast`/`qwen-heavy`/`default` all aliasing one model
- Re-point `embed` at `http://host.docker.internal:11434` (Ollama, confirmed live 4d20h+) and delete the "Ollama service is down" comment — it's stale
- Restart `civos_litellm` after editing, then verify with `curl :4000/v1/models` and an actual embed call
- **Why:** this is the direct answer to "why isn't OmniRoute routing to other models/Ollama" — nothing is broken downstream, the config was just never widened past an emergency single-model stopgap from 2026-08-12

⏳ **Phase 1 Execution** (Database Deployment)
- SSH to Mac Studio: `ssh macstudio`
- Run: `docker-compose -f _INFRASTRUCTURE/docker-compose.yml up -d`
- Verify: `docker ps`, `cypher-shell -u neo4j -p changeme "RETURN 1;"`
- **Why:** Unblocks all downstream phases (models, observability, ontology)

⏳ **Complete Model Pulls** (Phase 2)
- Monitor: `ollama pull qwen2.5:32b` (ongoing, ~4.8 hours at 1.1 MB/s)
- Queue: `ollama pull qwen2.5:72b` after (10+ hours)
- **Why:** Provides fallback models and distributed inference options

⏳ **OmniRoute Configuration** (Phase 2 Integration)
- Web UI: http://100.87.214.70:20128/dashboard
- Add provider: Ollama at http://100.87.214.70:11434
- Add models: qwen2.5-coder:14b, qwen2.5:32b, nomic-embed-text
- **Why:** Enables model routing, fallbacks, and inference via Claude Code

⏳ **Neo4j Ontology Wiring** (Phase 1 → Phase 3)
- Command: `cb neo4j wire-ontology`
- Creates: OmniRoute node, Provider relationships, Model mappings
- Validates: `cb neo4j status`
- **Why:** Connects infrastructure to knowledge graph for agent queries

⏳ **MCP Integration** (Phase 3)
- Setup: `cb mcp setup`
- Creates: `~/.claude/mcp.json` with OmniRoute endpoint
- Restart Claude Code to enable
- **Why:** Enables agents to query OmniRoute for model selection

---

## QUICK START (next session)

### Step 1: Generate CLI
```bash
npm install -g @hkuds/cli-anything
cli-anything _CLI/schema.yaml
cb --help
```

### Step 2: Deploy Infrastructure
```bash
# Check status
cb infrastructure status

# Deploy all phases
cb infrastructure deploy --phase all

# Or deploy individual phases
cb infrastructure deploy --phase 1  # Databases
cb infrastructure deploy --phase 2  # Models + OmniRoute
cb infrastructure deploy --phase 3  # Exo distributed inference
cb infrastructure deploy --phase 4  # Observability (Grafana, Langfuse)
```

### Step 3: Test & Verify
```bash
# End-to-end test
cb test e2e

# Wire ontology to Neo4j
cb neo4j wire-ontology

# Sync control planes
cb control-planes sync
```

### Dashboard Access
| Service | URL | Credentials |
|---------|-----|-----------|
| **OmniRoute** | http://100.87.214.70:20128 | admin@omniroute.local / → Bitwarden item "OmniRoute — Company Brain" |
| **Neo4j** | http://100.87.214.70:7474 | neo4j / changeme |
| **Grafana** | http://100.87.214.70:3010 | admin / admin |

### Reference Files
- [[CLI README|_CLI/README.md]] — Command reference
- [[CLI Schema|_CLI/schema.yaml]] — Automation definitions
- `_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml` — Model routing
- `_REGISTRIES/INFRASTRUCTURE_REGISTRY.yaml` — Device status
- `_INFRASTRUCTURE/DEPLOYMENT_PHASES.md` — Phase timeline

---

## VENTURE DOCUMENT OPERATING SYSTEM & TOOLING (2026-09-07)

### Architecture & Capabilities
- **22-Domain Institutional Architecture:** Implemented in `BUSINESS-CAPITAL-DATA-ROOM/` spanning `01_IDENTITY` through `22_SYSTEM` for 5 operating ventures (`CON-001`, `LT-011`, `LT-005`, `OPS-001`, `RE-001`).
- **Multi-Format Source of Truth:**
  - Living source in Markdown, YAML, JSON, CSV, and zero-dependency OpenXML `.xlsx` financial models (`scripts/generate_xlsx_helper.py`).
  - Compiled deliverables in high-resolution vector PDF (16:9 Landscape Pitch Decks, Executive Summaries, Certificates, Operating Agreements, Capital Readline Cards).
- **Installed Developer Tooling:**
  - **gstack** (`_TOOLS/gstack`, CLI wrapper: `scripts/make-pdf`): Chromium/Playwright-based publication PDF compiler with CSS Paged Media and Mermaid rendering.
  - **gbrain** (`_TOOLS/gbrain`, CLI wrapper: `scripts/gbrain`): Embedded PGLite vector and keyword graph retrieval engine (`/Users/acebless/.gbrain/brain.pglite`) indexing all 273 venture documents.
  - **Venture OS Engine** (`scripts/venture_os_engine.py`): Compiles 206 institutional documents and generates SHA-256 validated ZIP data rooms per venture.
- **Exported Institutional Packages:**
  - `CON-001-VENTURE-OS-DATA-ROOM.zip` (379 KB, 206 files)
  - `LT-011-VENTURE-OS-DATA-ROOM.zip` (378 KB, 206 files)
  - `LT-005-VENTURE-OS-DATA-ROOM.zip` (379 KB, 206 files)
  - `OPS-001-VENTURE-OS-DATA-ROOM.zip` (382 KB, 206 files)
  - `RE-001-VENTURE-OS-DATA-ROOM.zip` (387 KB, 206 files)
  - `ALL-VENTURES-OS-DATA-ROOM.zip` (1.87 MB, consolidated)

---

**Session Status:** ✅ COMPLETE — Venture Document OS, gstack/gbrain tooling, and 5 venture data rooms operational  
**CLI Completion:** See [[_CLI/COMPLETION_REPORT.md|Completion Report]]  
**Available Now:**
- `_CLI/bin/cb help` — Full CLI command reference
- `scripts/make-pdf` — Garry Tan gstack PDF compiler
- `scripts/gbrain` — Garry Tan gbrain local knowledge engine
- `scripts/venture_os_engine.py` — 22-domain compiler & ZIP packager
- `_CLI/bin/cb infrastructure status` — Health check (all 4 services ✅)
- `_CLI/bin/cb test e2e` — End-to-end verification (all tests passing ✅)
- `_CLI/bin/cb control-planes sync` — Orchestrate all 6 control planes

**Next Steps:** Use CLI for Phase 1 database deployment → OmniRoute config → ontology wiring → MCP integration  
**Authority:** Infrastructure Control Plane (CP-027)
