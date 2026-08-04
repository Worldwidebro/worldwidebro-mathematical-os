# Civilization OS — System Topology

## 7-Layer Architecture

The Worldwidebro OS is built as a 7-layer stack, each with specific responsibilities, canonical repos, and tech stack.

---

## Layer 1: Experience

**Purpose:** User-facing interfaces for venture discovery, task management, and real-time dashboards.

**Components:**
- **Worldwidebro Venture Portal** — Sector navigation, venture discovery, lead capture
- **Agent Command Center** — Operations dashboard, agent performance, decision tracking
- **Mobile/Web Apps** — Venture-specific user experiences
- **Voice Interface** — VAPI-powered voice agents for sales and support

**Tech Stack:**
- Frontend: Next.js 15, React 19, TypeScript
- Hosting: Vercel, Cloudflare Workers
- Real-time: WebSockets, Server-Sent Events
- Mobile: React Native, Expo, Flutter (sector-specific)

**Canonical Repo:** `worldwidebro-venture-portal`

**Key Files:**
- `src/pages/sectors/[sector].tsx` — Sector hero pages
- `src/components/venture-grid.tsx` — Venture discovery
- `src/api/ventures/[id].ts` — Venture details endpoint
- `src/dashboard/agent-performance.tsx` — Real-time agent metrics

**Data Flows:**
- Reads from Layer 3 (Knowledge Graph) for venture metadata
- Reads from Layer 4 (Redis cache) for real-time agent performance
- Writes to Layer 4 (Redis) user activity logs
- Calls Layer 2 agents for task creation

---

## Layer 2: Agent Operating System

**Purpose:** Orchestrate AI agent decision-making, task execution, and learning.

**Components:**
- **Fractal Agent Spawn** — Multi-level agent hierarchies (6 OPCOs → 22 agents)
- **CrewAI Pipelines** — 4-agent orchestration for CON (classifier → estimator → risk → scheduler)
- **Agent Roster** — 22 agents across 6 OPCOs with success rates and authority levels
- **Decision Authority Model** — AUTONOMOUS / MONITORED / TRAINING classification

**Tech Stack:**
- Agent Framework: CrewAI, LangChain
- LLM: Claude 3.x via Anthropic API, Ollama (local fallback)
- Orchestration: Python asyncio, Temporal (for long-running workflows)
- Monitoring: Langfuse, Grafana

**Canonical Repo:** `worldwidebro-os-business-engine`

**Key Files:**
- `.fractal_agent_spawn.py` — Spawn 6 parallel OPCO agent trees
- `crewai-agent-orchestrator.py` — CON 4-agent pipeline
- `.planning/AGENTS.md` — All 22 agents with success rates and authority
- `AGENT-OPERATING-SYSTEM.md` — Standards, KPIs, decision authority thresholds

**Agent Authority Levels:**
| Level | Success Rate | Execution | Growth/Learning | Actions |
|-------|---|---|---|---|
| AUTONOMOUS | 90%+ | Full autonomy | Demonstrates learning | Execute immediately |
| SUPERVISED | 75-89% | Execute + report | Good execution, needs growth | Execute with async reporting |
| MONITORED | 70-79% | Execute + approval gate | Needs coaching | Escalate to director before execution |
| TRAINING | <70% | Human-led + feedback loop | Intensive feedback needed | Director handles; agent shadows |

**Data Flows:**
- Reads from Layer 3 (Knowledge Graph) for venture context, task definitions
- Reads from Layer 5 (Skills Registry) for available actions
- Writes to Layer 6 (Decision Engine) for decisions and audit trail
- Calls Layer 4 (Infrastructure) for compute, storage, external integrations

---

## Layer 3: Knowledge Graph OS

**Purpose:** Unified graph schema for entities, relationships, and context across 712 ventures and 6 OPCOs.

**Components:**
- **Neo4j Graph Database** — Entity types, relationships, constraints
- **PostgreSQL (Supabase)** — Transactional data, venture state, tasks
- **Qdrant Vector DB** — Embeddings for semantic search, notes RAG, capabilities
- **Entity Types** — Venture, OPCO, Founder, Agent, Skill, Tool, Decision, Task (see ONTOLOGY.md)
- **Key Relationships** — ORCHESTRATES, BELONGS_TO, LEADS, EXECUTES, etc.

**Tech Stack:**
- Graph: Neo4j 5.x with Cypher
- RDBMS: PostgreSQL 16, Supabase
- Vector DB: Qdrant 1.x
- Query Layer: GraphQL, REST APIs
- Caching: Redis

**Canonical Repo:** `worldwidebro-os-knowledge-graph`

**Key Files:**
- `neo4j-schema.cypher` — Graph constraints, indexes, uniqueness rules
- `supabase-schema.sql` — PostgreSQL tables: ventures, tasks, decisions, founders
- `ONTOLOGY.md` — Entity definitions, attributes, relationships
- `storage-map.md` — Which data lives where

**Schema Highlights:**

```cypher
// Key node types
CREATE CONSTRAINT venture_id_unique FOR (v:Venture) REQUIRE v.id IS UNIQUE;
CREATE CONSTRAINT opco_id_unique FOR (o:OPCO) REQUIRE o.id IS UNIQUE;
CREATE CONSTRAINT agent_id_unique FOR (a:Agent) REQUIRE a.id IS UNIQUE;

// Key relationships
(:OPCO)-[:ORCHESTRATES]->(v:Venture)
(:Venture)-[:LED_BY]->(f:Founder)
(:Agent)-[:BELONGS_TO]->(o:OPCO)
(:Agent)-[:EXECUTES_TASKS]->(t:Task)
(:Task)-[:EXECUTED_BY]->(d:Decision)
```

**Data Flows:**
- Receives entity mutations from Layer 2 (Agents)
- Provides context to Layer 2 agents via queries
- Syncs with Layer 4 infrastructure (Redis cache invalidation)
- Audits all mutations through Layer 6 (Decision Engine)

---

## Layer 4: AI Infrastructure

**Purpose:** Operational services supporting agents, knowledge graph, and execution.

**Components:**
- **Neo4j** (port 7687) — Graph database + browser UI (7474)
- **PostgreSQL** (port 5432) — Supabase-hosted or local
- **Redis** (port 6379) — Cache, sessions, rate limiting
- **Qdrant** (port 6333) — Vector database for embeddings
- **LiteLLM** (port 4000) — LLM proxy, cost tracking, load balancing
- **Langfuse** (port 3003) — LLM observability, prompt versioning
- **Prometheus** (port 9090) — Metrics collection
- **OTel Collector** — Distributed tracing
- **n8n** (port 5678, optional) — Workflow automation for non-agent tasks

**Tech Stack:**
- Containerization: Docker, Docker Compose
- Orchestration: Local docker-compose (dev), Kubernetes (prod)
- IaC: Terraform, CloudFormation
- Monitoring: Prometheus + Grafana, ELK Stack

**Canonical Repo:** `worldwidebro-os-infrastructure`

**Key Files:**
- `docker-compose.yml` — 9 services configuration
- `Makefile` — 20+ operational commands (bootstrap, health, seed, logs, etc.)
- `scripts/bootstrap.sh` — 9-phase setup automation
- `scripts/health-check.sh` — Service validation
- `.env.example` — Configuration template

**Bootstrap Process (3-5 minutes):**
```bash
make bootstrap      # Start all 9 services
make health         # Verify all services running
make seed           # Populate initial data
```

**Verification:**
```bash
# Neo4j
curl http://localhost:7474

# Qdrant
curl http://localhost:6333/health

# PostgreSQL
psql -h localhost -U postgres -d ventures -c "SELECT COUNT(*) FROM ventures;"

# Redis
redis-cli PING

# LiteLLM
curl http://localhost:4000/health
```

**Data Flows:**
- Receives compute requests from Layer 2 (Agents)
- Provides storage, caching, and observability to all layers
- Syncs with external services (Stripe, Slack, HubSpot via MCPs in Layer 5)

---

## Layer 5: Skill + Tools Registry

**Purpose:** Indexed workflows (skills) and operational capabilities (tools) available to agents and humans.

**Components:**
- **296+ Skills** — Named workflows indexed by phase (14 phases) and sector
  - `/gsd-plan-phase`, `/code-review`, `/deploy-and-link-venture`, etc.
  - Each skill is a composable CLI command or orchestration flow
- **40+ Tools** — Operational capabilities (CLI, API, webhook)
  - `bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`, `WebFetch`, `Bash`, etc.
  - Each tool is either a language primitive or MCP integration
- **18 MCPs** — Model Context Protocol integrations
  - GitHub, Slack, Zapier, HubSpot, Notion, Gmail, Google Calendar, etc.
  - Each MCP provides 5-20+ tools for external system integration

**Tech Stack:**
- Skill Definition: YAML + markdown documentation
- Tool Registry: JSON schema, OpenAPI 3.1
- MCP Framework: Claude MCP SDK
- Versioning: Semantic versioning (skills + tools update independently)

**Canonical Repo:** `worldwidebro-os-business-engine`

**Key Files:**
- `agent_tools_registry.yaml` — All 40+ tools mapped to agents and permissions
- `MCP_REGISTRY.json` — 18 MCPs, versions, authentication methods
- `SKILL-INDEX.md` — All 296+ skills indexed by phase + sector
- `.claude/SKILL-INDEX.md` — User-facing skill documentation

**Skill Phases (14 total):**
1. New (idea stage)
2. Plan (roadmap/spec)
3. Design (architecture/UI)
4. Implement (coding)
5. Test (QA/E2E)
6. Secure (security audit)
7. Deploy (CI/CD)
8. Monitor (observability)
9. Optimize (performance)
10. Refactor (cleanup)
11. Document (guides/API docs)
12. Launch (go-to-market)
13. Operate (ongoing support)
14. Sunset (archival)

**Tool Permission Model:**
- Each tool requires 0+ permissions (e.g., `bash` requires `shell:execute`)
- Each agent has a permission whitelist
- Director approvals required for HIGH-risk actions

**Data Flows:**
- Agents discover available skills via registry lookups (Layer 4: Redis cache)
- Agents invoke tools, which may call MCPs (Layer 2 → Layer 5 → external systems)
- Execution results are logged to Layer 6 (audit trail)

---

## Layer 6: Decision Engine + Governance

**Purpose:** 8-layer audit trace for every agent decision, with permission system and escalation.

**Components:**
- **Decision Audit Trace** — 8-layer capture of every decision
- **Permission System** — Per-agent, per-tool restrictions
- **Escalation Logic** — Route HIGH-risk decisions to human director
- **Audit Trail DB** — Immutable log of all decisions and their outcomes

**Tech Stack:**
- Decision Engine: Python + async event bus
- Policy as Code: Cedar (AWS)
- Audit Storage: PostgreSQL (Supabase) + Langfuse
- Alerting: Slack webhooks

**Canonical Repo:** `worldwidebro-os-business-engine`

**Key Files:**
- `decision_audit_trace.py` — 8-layer trace implementation
- `permissions.json` — Per-agent permission sets
- `governance_engine.py` — Escalation and approval logic
- `.planning/GOVERNANCE.md` — Decision authority policy

**8-Layer Decision Trace:**

```
Layer 1: Registry
  ↓ Agent looks up available skills/tools
Layer 2: Agent Factory
  ↓ Skill loads agent configuration, permissions
Layer 3: Task Executor
  ↓ Agent prepares task inputs, validation
Layer 4: Directive Enforcer
  ↓ Check agent authority level (AUTONOMOUS/MONITORED/TRAINING)
Layer 5: MCP Slack
  ↓ Check MCP tool permissions, rate limits, costs
Layer 6: Director
  ↓ HIGH-risk actions escalated to human approval
Layer 7: Execution
  ↓ Task executes if all gates pass
Layer 8: Audit Trail
  ↓ Immutable record: inputs, outputs, timing, success/failure
```

**Risk Assessment Matrix:**

| Authority Level | Execution | Growth/Learning | Auto-Approve? | Escalation |
|---|---|---|---|---|
| AUTONOMOUS (90%+) | Full autonomy | Demonstrates learning | ✅ Auto | Async report only |
| MONITORED (70-79%) | Execute + report | Needs coaching | ❌ Director | Director approval gate |
| TRAINING (<70%) | Human-led | Intensive feedback | ❌ Director | Director executes; agent shadows |

**Data Flows:**
- Receives decisions from Layer 2 (Agents)
- Writes audit trail to Layer 3 (PostgreSQL) and Layer 4 (Langfuse)
- Escalates HIGH-risk decisions via Slack webhooks
- Provides feedback to Layer 7 (Human OS development)

---

## Layer 7: Trust + Governance (Dual-Outcome)

**Purpose:** Evaluate agent and founder performance, assign authority levels, and track human OS development.

**Components:**
- **Success Rate** — % of tasks completed correctly (execution)
- **Learning Velocity** — Growth rate across Human OS layers (development)
- **Authority Assignment** — AUTONOMOUS / MONITORED / TRAINING based on dual-outcome evaluation
- **Audit Logging** — Comprehensive trail for regulatory compliance
- **Security Monitoring** — MCP Slack alerts, anomaly detection
- **Human OS Development** — 10-layer founder growth tracking

**Tech Stack:**
- Metrics DB: Prometheus + Grafana
- Audit Logging: Supabase (PostgreSQL) + Langfuse
- Alerting: Slack, PagerDuty
- Monitoring: CloudWatch, Datadog (prod)

**Canonical Repo:** `worldwidebro-os-business-engine` + sector-specific repos

**Key Files:**
- `.planning/GOVERNANCE-HUMAN-LAYER.md` — Human OS framework
- `HUMAN-OS-FRAMEWORK.md` — 10-layer development model
- `GOVERNANCE-METRICS.md` — KPIs for authority assessment
- Grafana dashboards: agent success rates, founder learning velocity

**Dual-Outcome Evaluation Model:**

| Agent/Founder | Success Rate (Execution) | Learning Velocity (Growth) | Authority Level | Action |
|---|---|---|---|---|
| High | High | AUTONOMOUS | Full autonomy |
| High | Low | MONITORED | Execute well, but coach on growth |
| Low | High | TRAINING | Poor execution, intensive feedback |
| Low | Low | TRAINING | Both execution + growth support needed |

**10 Human OS Layers (Founder Development):**

1. **Foundational Execution** — Task completion, reliability, follow-through
2. **Judgment & Discernment** — Good decision-making, risk assessment
3. **Emotional Resilience** — Stress management, bounce-back from failure
4. **Strategic Thinking** — Long-term vision, pattern recognition
5. **Complexity Navigation** — Systems thinking, multi-causality analysis
6. **Leadership Presence** — Influence, communication, vision casting
7. **Systems Architecture** — Designing for scale, organizational design
8. **Institutional Building** — Culture, governance, team hiring
9. **Capital Stewardship** — Finance, M&A, cap table, exit readiness
10. **Civilization Building** — Legacy, systemic impact, ecosystem design

**Data Flows:**
- Receives audit trail from Layer 6 (Decision Engine)
- Reads agent metrics from Layer 4 (Prometheus)
- Writes authority assignments back to Layer 2 (Agent Operating System)
- Writes founder development metrics to Layer 3 (Knowledge Graph) and Layer 4 (Grafana)
- Alerts via Slack for anomalies or policy violations

---

## Cross-Layer Data Flows

```
User Request (Layer 1)
  ↓
  Portal sends task to Agent (Layer 2)
  ↓
  Agent queries Knowledge Graph (Layer 3)
  ↓
  Uses Infrastructure services (Layer 4): Redis cache, LiteLLM, Qdrant
  ↓
  Looks up available Skills & Tools (Layer 5)
  ↓
  Decision Engine validates permissions (Layer 6)
  ↓
  Task executes, audit trail written (Layer 6 + Layer 4)
  ↓
  Results bubble up to Governance (Layer 7)
  ↓
  Authority level adjusted if needed
  ↓
  Dashboard updated in Portal (Layer 1)
```

---

See also:
- **ONTOLOGY.md** — Entity definitions
- **GOVERNANCE.md** — Decision authority, escalation, audit
- **INTEGRATION.md** — How Tier 1-3 repos fit together
