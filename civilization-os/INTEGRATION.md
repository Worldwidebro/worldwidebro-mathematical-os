---
name: civilization-os/INTEGRATION
title: Civilization OS — Repository Integration Map
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Civilization OS — Repository Integration Map

## Repository Tiers

The Worldwidebro ecosystem is organized into 3 tiers: **Canonical** (never fork), **Sector Extensions** (extend, don't override), and **Consumption** (read-only).

---

## Tier 1: Canonical Repositories (Authority of Truth)

These repos define the OS and are referenced by all others. Never fork or duplicate code from these.

### worldwidebro-os-knowledge-graph
**Purpose:** Unified entity schema, relationships, and storage map for entire system.

**Owner:** Founder + data architect  
**Tech Stack:** Neo4j 5.x + Cypher, PostgreSQL 16, Qdrant 1.x, Supabase

**Key Files:**
- `ONTOLOGY.md` — Entity definitions, 10 entity types, key relationships
- `neo4j-schema.cypher` — Graph constraints, indexes, uniqueness rules
- `supabase-schema.sql` — PostgreSQL tables: ventures, tasks, decisions, founders
- `storage-map.md` — Which data lives where (PostgreSQL vs. Neo4j vs. Qdrant)
- `neo4j-seed.cypher` — Initial graph data (OPCOs, sample ventures)
- `migrations/` — Schema evolution (new entity types, relationships)

**Consumed By:**
- All 6 Sector OPCOs (Tier 2)
- Portal + Agent Command Center (Tier 3)
- Business engine (Tier 1)

**How to Update:**
1. Changes to entity types → Update `ONTOLOGY.md`
2. Schema changes → Create migration in `migrations/`
3. New relationships → Update `neo4j-schema.cypher`
4. Notify all Tier 2 + Tier 3 repos of breaking changes

---

### worldwidebro-os-business-engine
**Purpose:** Agent orchestration, skill registry, tools, decision engine, governance logic.

**Owner:** Founder + AI engineer  
**Tech Stack:** Python 3.12+, CrewAI, LangChain, Langfuse, Prometheus

**Key Files:**
- `.fractal_agent_spawn.py` — Spawn 6 OPCO agent trees (parallel execution)
- `crewai-agent-orchestrator.py` — 4-agent pipeline for CON (example implementation)
- `.planning/AGENTS.md` — All 22 agents: name, role, success rate, authority level
- `agent_tools_registry.yaml` — 40+ tools mapped to agents + permissions
- `MCP_REGISTRY.json` — 18 MCPs: name, version, auth method, tools provided
- `SKILL-INDEX.md` — 296+ skills indexed by 14 phases + sector
- `decision_audit_trace.py` — 8-layer decision trace implementation
- `permissions.json` — Per-agent permission whitelists
- `governance_engine.py` — Escalation logic, authority assignment

**Consumed By:**
- All 6 Sector OPCOs (Tier 2) — inherit agent orchestration pattern
- Portal + Command Center (Tier 3) — trigger agent tasks

**How to Update:**
1. New agent → Add to `AGENTS.md`, create agent Python class
2. New skill → Add to `SKILL-INDEX.md`, register with skill loader
3. New tool → Add to `agent_tools_registry.yaml`, implement tool
4. New MCP → Add to `MCP_REGISTRY.json`, test integrations
5. Permission change → Update `permissions.json`, notify affected agents

---

### worldwidebro-os-infrastructure
**Purpose:** Operational services, bootstrap, health checks, observability.

**Owner:** Founder + DevOps engineer  
**Tech Stack:** Docker, Kubernetes, Terraform, Prometheus, Grafana

**Key Files:**
- `docker-compose.yml` — 9 services: Neo4j, PostgreSQL, Redis, Qdrant, LiteLLM, Langfuse, Prometheus, OTel, n8n
- `Makefile` — 20+ commands: bootstrap, health, seed, logs, restart, etc.
- `scripts/bootstrap.sh` — 9-phase setup (2-5 min)
- `scripts/health-check.sh` — Validate all services running
- `.env.example` — Config template (ports, credentials, limits)
- `terraform/` — IaC for production deployment (AWS/GCP)

**Consumed By:**
- All 6 Sector OPCOs (Tier 2) — reference for deployment
- Portal + Command Center (Tier 3) — depend on running services

**How to Update:**
1. Add service → Update `docker-compose.yml`, add health check
2. New Makefile command → Add to `Makefile` with documentation
3. Deployment config → Update `terraform/` + `.env.example`
4. Test everything locally first: `make bootstrap && make health`

---

## Tier 2: Sector Extensions (OPCO-Specific)

These repos extend Tier 1 schemas and implement sector-specific logic. Never fork from Tier 1; always reference.

### worldwidebro-construction-os
**Purpose:** CON-sector operating company for 100+ construction ventures.

**Inherits From:** Tier 1 (knowledge-graph, business-engine, infrastructure)

**Owns:**
- **4-Agent CON Pipeline:**
  - `venture_classifier` — Lead classification (construction opportunity type)
  - `estimator_gen1` — Cost estimation (labor, materials, timeline)
  - `risk_assessor` — Risk identification (safety, regulations, market)
  - `project_scheduler` — Project scheduling (timeline, milestones)
  
- **CON-Specific Entities:** (extends ONTOLOGY)
  - Property, ConstructionProject, Estimate, SafetyReport, Permit
  
- **CON-Specific Skills:** (extends SKILL-INDEX)
  - `/con-estimate-generator`, `/con-risk-audit`, `/con-project-create`
  
- **CON Domain Logic:**
  - Estimate calculation rules (material costs, labor rates)
  - Risk scoring model (safety regulations, market volatility)
  - Milestone dependencies (construction phases)

**Key Files:**
- `agents/` — 4 CON agents (venture_classifier, estimator_gen1, risk_assessor, project_scheduler)
- `schemas/con-entities.sql` — CON-specific tables (projects, estimates, permits)
- `agents/estimator-rules.yaml` — Cost estimation configuration
- `agents/risk-scoring-model.py` — Risk calculation logic
- `.planning/AGENTS.md` — CON agent roster + success rates

**References to Tier 1:**
```python
# In agents/estimator_gen1.py
from worldwidebro_os_business_engine import CrewAIOrchestrator, Tool
from worldwidebro_os_knowledge_graph import VentureEntity, TaskEntity

# Fetch venture from knowledge graph
venture = knowledge_graph.query("MATCH (v:Venture {id: $id}) RETURN v", id=venture_id)

# Log decision through governance engine
governance_engine.log_decision(agent_id="AGT-CON-001", decision=estimation_result)
```

**How to Extend:**
1. Add CON-specific entity type → Update `schemas/con-entities.sql`
2. Add CON skill → Add to skill loader in business-engine
3. Modify estimation rules → Update `estimator-rules.yaml`
4. Test in isolation: `cd worldwidebro-construction-os && make test`
5. Deploy to CON infrastructure: `make deploy-con`

---

### worldwidebro-staffing-os, worldwidebro-real-estate-os, etc.
**Pattern:** Same as CON-OS

**Each OPCO has:**
- 3-4 agents (domain-specific)
- Domain-specific entities (extends ONTOLOGY)
- Domain-specific skills (extends SKILL-INDEX)
- Domain logic (calculations, rules, workflows)
- Local Makefile for isolated testing + deployment

---

## Tier 3: Consumption Repositories (Read-Only)

These repos read from Tier 1 + Tier 2 but never modify. No code duplication.

### worldwidebro-venture-portal
**Purpose:** User-facing portal for venture discovery, dashboard, lead capture.

**Tech Stack:** Next.js 15, React 19, TypeScript, Vercel

**Reads From:**
- Layer 3 (Knowledge Graph) — Venture metadata, sectors, stages
- Layer 4 (Redis) — Cached agent performance metrics
- Layer 5 (Skills Registry) — Available skills to offer users
- All Tier 2 OPCOs — Sector-specific data

**Writes To:**
- Layer 4 (Redis) — User activity logs (analytics)
- Layer 2 (Business Engine) — Task creation (via API)

**Key Files:**
- `src/pages/sectors/[sector].tsx` — Sector hero pages (CON, STA, RE, EDU, FIN, LOG)
- `src/components/venture-grid.tsx` — Venture discovery and filtering
- `src/api/ventures/[id].ts` — Venture details + related deals
- `src/api/tasks/create.ts` — Create task via business engine
- `src/dashboard/agent-performance.tsx` — Real-time agent success rates (from Prometheus)

**How to Consume:**
```typescript
// Fetch ventures from knowledge graph
const ventures = await supabase
  .from('ventures')
  .select('*')
  .eq('sector', 'CON')
  .eq('status', 'active');

// Create task via business engine API
const response = await fetch('/api/tasks/create', {
  method: 'POST',
  body: JSON.stringify({
    venture_id: 'CON-001',
    skill: '/gsd-plan-phase',
    inputs: { ... }
  })
});
```

**Never Do:**
- Don't duplicate agent logic
- Don't query Neo4j directly (always go through API)
- Don't modify knowledge graph
- Don't copy skills from business-engine

---

### worldwidebro-agent-command-center
**Purpose:** Operations dashboard for founders, directors, admins.

**Tech Stack:** Next.js 15, Grafana dashboards, TypeScript

**Reads From:**
- All Tier 1 + Tier 2 (read-only)
- Prometheus metrics (agent success rates, latency)
- Langfuse (decision audit trail)
- Supabase (venture state, task progress)

**Key Files:**
- `src/dashboards/agent-performance.tsx` — Agent success rates, authority levels
- `src/dashboards/decision-audit.tsx` — Recent decisions, escalations
- `src/dashboards/founder-human-os.tsx` — Human OS layer progression
- `src/dashboards/opco-overview.tsx` — OPCO metrics by sector
- `src/grafana/dashboards/` — Pre-built Grafana dashboards

**How to Integrate:**
```typescript
// Read agent success rate from Prometheus
const metrics = await prometheus.query('agent_success_rate{sector="CON"}');

// Read recent decisions from Langfuse
const decisions = await langfuse.getTraces({ agent_id: 'AGT-CON-001', limit: 50 });

// Read founder Human OS metrics from Supabase
const founder = await supabase
  .from('founders')
  .select('*,human_os_layers(*)')
  .eq('id', 'FOU-001');
```

---

### worldwidebro-ventures
**Purpose:** 712 venture repositories and deployment targets.

**Structure:**
```
worldwidebro-ventures/
├── ventures/
│   ├── CON-001-ace-construction/
│   │   ├── venture.json (metadata)
│   │   ├── README.md (venture description)
│   │   └── src/ (venture-specific code)
│   ├── CON-002-*/
│   └── ...
├── ecosystem/ (shared utilities)
│   ├── venture-loader.ts (load venture from manifest)
│   ├── skill-invoker.ts (call skills for ventures)
│   └── defaults/ (venture template)
└── VENTURES-REGISTRY.csv (canonical venture list)
```

**Reads From:**
- Tier 1 (business-engine) — Available skills
- Tier 2 OPCOs — OPCO-specific knowledge
- Tier 3 (Portal) — Public venture data

**Key Integrations:**
- `venture.json` — Venture metadata (reads from knowledge graph)
- `skill-invoker.ts` — Invokes skills from business-engine
- `VENTURES-REGISTRY.csv` — Canonical list synced with Supabase

**Never Do:**
- Don't implement agent logic (reference business-engine)
- Don't duplicate entity schemas (reference knowledge-graph)
- Don't run docker-compose (reference infrastructure)

---

## Data Flow Example: Creating a Construction Lead

**Request Flow (Layer 1 → Layer 2 → Layers 3-6 → Feedback Loop):**

```
1. User submits lead on Portal (Tier 3)
   ↓ worldwidebro-venture-portal/src/api/leads/create.ts
   
2. Portal calls business-engine task API (Tier 1)
   ↓ POST /api/tasks { skill: '/gsd-triage-lead', inputs: {...} }
   
3. Business engine routes to CON agent (Tier 2)
   ↓ worldwidebro-construction-os/agents/venture_classifier.py
   
4. Agent queries knowledge graph (Tier 1)
   ↓ Fetch venture context, segment rules
   
5. Agent classifies lead through 8-layer trace (Tier 1)
   ↓ Layer 1: Registry → Layer 8: Audit Trail
   
6. Decision logged to PostgreSQL + Langfuse (Tier 1 Infrastructure)
   ↓ Immutable record with success/failure metrics
   
7. Portal dashboard refreshed (Tier 3)
   ↓ Command center shows new lead, agent classification, next task
   
8. Feedback loop (Tier 1)
   ↓ Success rate updated, authority level adjusted if needed
```

---

## Dependency Graph

```
┌─────────────────────────────────────────────────────────┐
│ Tier 3: Consumption (Read-Only)                         │
│                                                          │
│  Portal ─────┐                                          │
│              ├──→ Command Center                        │
│              └──→ Ventures Repo                         │
└─────────────────────────────────────────────────────────┘
       ↓ (reads from)
┌─────────────────────────────────────────────────────────┐
│ Tier 2: Sector Extensions (Extend, Don't Duplicate)     │
│                                                          │
│  CON-OS ────┬─→ STA-OS                                  │
│             ├─→ RE-OS                                   │
│             ├─→ EDU-OS                                  │
│             ├─→ FIN-OS                                  │
│             └─→ LOG-OS                                  │
└─────────────────────────────────────────────────────────┘
       ↓ (inherits from, references)
┌─────────────────────────────────────────────────────────┐
│ Tier 1: Canonical (Never Fork)                          │
│                                                          │
│  OS-KG ──┬──→ OS-Business-Engine ──→ OS-Infrastructure  │
│          └──→ (shared by all OPCOs)                     │
└─────────────────────────────────────────────────────────┘
```

---

## Integration Checklist

When adding a new venture, OPCO, or feature:

**Before Starting:**
- [ ] Understand which tier(s) will be affected
- [ ] Check Tier 1 ONTOLOGY for entity types you need
- [ ] Check Tier 1 business-engine for available skills

**During Implementation:**
- [ ] Reference Tier 1, don't duplicate
- [ ] If new entity type needed, update Tier 1 ONTOLOGY + schema
- [ ] If new skill needed, add to Tier 1 SKILL-INDEX
- [ ] If new OPCO-specific logic, create Tier 2 extension
- [ ] Test in isolation before integration

**Before Deployment:**
- [ ] Verify all Tier 1 references still resolve
- [ ] Run integration tests: `make integration-test`
- [ ] Update VENTURES-REGISTRY.csv if new ventures added
- [ ] Notify impacted OPCOs of any Tier 1 changes

---

See also:
- **README.md** — System overview and quick start
- **TOPOLOGY.md** — 7-layer architecture (which repos live where)
- **ONTOLOGY.md** — Entity definitions used across repos
- **GOVERNANCE.md** — Decision authority enforced across repos
