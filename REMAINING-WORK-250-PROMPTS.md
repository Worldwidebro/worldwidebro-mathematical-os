---
title: Remaining Work — 250-Prompt Operational Manual Framework
subtitle: What We Have vs. What's Missing (Agent-Ready Deep Work)
date: 2026-07-20
status: Active Inventory
---

# WHAT WE ALREADY HAVE ✅

## Level 0: Infrastructure (COMPLETE)

| Component | File | Status | Live |
|-----------|------|--------|------|
| **Docker Compose** | docker-compose.yml | ✅ Complete | Neo4j, Redis, PostgreSQL, Qdrant, Grafana, Langfuse, Prometheus, n8n |
| **MCP Registry** | MCP_REGISTRY.json | ✅ Complete | 30+ MCPs mapped |
| **Tool Capability Map** | TOOL_CAPABILITY_MAP.md | ✅ Complete | Goals → MCPs binding |
| **System Constitution** | WORLDWIDEBRO-OS/WHOAMI.md | ✅ Complete | IZA OS + 6 OPCOs + 712 ventures |
| **OPCO Architecture** | OPCO-DEPENDENCY-ARCHITECTURE.md | ✅ Complete | Dependency flows |
| **Dependency Map** | DEPENDENCY-MAP.json | ✅ Complete | All MCPs + tools + services |

## Level 1: Agent Organization (COMPLETE)

| Component | File | Status | Live |
|-----------|------|--------|------|
| **AGENTS.md** | AGENTS.md | ✅ Complete | 4 CON agents + authority levels |
| **TEAMS.md** | TEAMS.md | ✅ Complete | 7 OPCO teams + escalation |
| **DEPARTMENTS.md** | DEPARTMENTS.md | ✅ Complete | Economic models + principles |
| **Tech Stack** | TECH-STACK-ARCHITECTURE.md | ✅ Complete | Tool audit + gaps |

## Level 2: Automation & Routing (EXISTS, NOT WIRED)

| Component | Status | Note |
|-----------|--------|------|
| Multi-Model Router | ✅ Built | Routes to qwen2.5 or Claude |
| CrewAI Orchestrator | ✅ Built | 4 CON agents sequenced (07/20) |
| LiteLLM Config | ✅ Built | Model routing + fallback |
| OTel Collector Config | ✅ Built | Telemetry pipeline |

## Level 3: Repositories & Knowledge (EXISTS, NOT INDEXED)

| Component | Count | Status | Note |
|-----------|-------|--------|------|
| Repo Registry | 1,639 repos | ⏳ Partial | Inventoried; not fully in Neo4j |
| Venture Registry | 712 ventures | ✅ Supabase | Not all Neo4j nodes |
| Repo-Venture Map | CSV | ⏳ Partial | Built but not wired to agents |
| Capability Catalog | JSON | ⏳ Partial | 70% of repos have metadata |

---

# WHAT'S MISSING (250-PROMPT ROADMAP)

## Prompts 1–25: INFRASTRUCTURE INTELLIGENCE (50% DONE)

**Status:** docker-compose built; unified operational view missing.

**Missing:**
- Enumerate all running services + SPOF analysis (JSON + Mermaid DAG)
- Service inventory with ownership + persistence strategy (CSV)
- Filesystem analysis (hot/warm/cold tiers) + storage migration
- Network topology reverse-engineer (ingress/egress/TLS/Kubernetes)
- Implicit dependency discovery (env vars, bind mounts, hardcoded paths)

**Artifact:** Operational dashboard showing system health, dependencies, and failure scenarios.

---

## Prompts 26–50: REPOSITORY INTELLIGENCE (20% DONE)

**Status:** 1,639 repos inventoried; not semantically indexed.

**Missing:**
- Parse every repo into org KG (product boundaries, domains, techs, APIs)
- Semantic similarity across all repos (consolidation opportunities)
- Capability matrix (repos → business capabilities → revenue)
- Architectural debt scoring (maintainability, testing, deployment)
- Repo execution graph (prerequisites for each 712 ventures)

**Artifact:** Neo4j ingestion scripts + capability relationship edges.

---

## Prompts 51–75: DATA ENGINEERING (40% DONE)

**Status:** Multiple data sources exist; no unified pipeline.

**Missing:**
- Enumerate every data source (Supabase, Neo4j, Qdrant, PostgreSQL, GitHub)
- Canonical enterprise ontology (ventures, people, assets, customers)
- ELT pipeline with validation checkpoints
- Data lifecycle policy (retention, latency, reproducibility)

**Artifact:** n8n workflows + SQL migrations + lineage tracking.

---

## Prompts 76–100: OMNIROUTER INTELLIGENCE (0% DONE)

**Status:** OmniRouter is GitHub project; not integrated.

**Missing:**
- Evaluate diegosouzapw/OmniRoute for our routing needs
- Design router for task complexity + confidence-based model selection
- Cost-aware routing (local vs. cloud, token budgeting)
- Formalize planner–executor–critic contracts

**Artifact:** Router configuration + integration into CrewAI orchestrator.

---

## Prompts 101–125: MCP ECOSYSTEM (80% DONE)

**Status:** MCPs discovered + mapped; not all wired to agents.

**Missing:**
- Wire MCPs into agent decision paths (when does each agent use which MCP?)
- Event-driven MCP orchestration (retries, queues, idempotency)
- Detect missing MCPs (finance audit trails, legal contracts)

**Artifact:** n8n workflows + MCP capability → agent mapping.

---

## Prompts 126–150: MULTI-AGENT OPERATING SYSTEM (60% DONE)

**Status:** AGENTS.md + TEAMS.md exist; execution wiring incomplete.

**Missing:**
- Wire agents to OPCO operations (agents don't execute locally on departments yet)
- Delegation graph (which tasks never need approval; confidence thresholds)
- Agent contracts (typed I/O, SLAs, rollback procedures)

**Artifact:** Agent-to-OPCO assignment + execution triggers.

---

## Prompts 151–175: 712 VENTURE STUDIO (10% DONE)

**Status:** Ventures exist in Supabase; not instantiable as modules.

**Missing:**
- Venture as autonomous business OS module (CRM, sales, finance, ops, AI agents)
- Dependency-aware launch plans (effort, revenue, leverage, time-to-cash)
- Venture instantiation template (<30 min from template → live)

**Artifact:** Automation script + infrastructure-as-code.

---

## Prompts 176–200: REVENUE AUTOMATION (15% DONE)

**Status:** Individual pieces exist; not connected end-to-end.

**Missing:**
- Lead capture form → CRM → agent workflows → documents → invoicing
- Closed-loop marketing intelligence (SEO + social + paid + CRM + LTV)
- Revenue attribution graph (customer interaction → campaign → agent → repo)

**Artifact:** End-to-end n8n workflows + attribution Neo4j edges.

---

## Prompts 201–250: CIVILIZATION SCALE (0% DONE)

**Status:** Framework defined (WHOAMI.md, 100+ principles); not implemented.

**Missing:** Knowledge ontology → educational products → ventures + macroeconomic simulation + adaptive learning engine (future work)

---

# AGENTS' CURRENT READINESS

## What Agents CAN Do ✅

- Classify leads (venture_classifier: 94%)
- Generate estimates (estimator_gen1: 88%)
- Assess risk (risk_assessor: 91%)
- Schedule projects (project_scheduler: 75%)
- Route models (multi_model_router.py)
- Execute n8n workflows
- Query Neo4j
- Search Qdrant

## What Agents CANNOT Do ❌

- **Execute locally on OPCO departments** — Assigned to isolation, not operations
- **Capture leads from landing pages** — Form → Supabase → agent trigger wiring missing
- **Auto-generate + send proposals** — Estimator output not connected to document pipeline
- **Schedule in customer calendars** — Project_scheduler output not connected to calendar APIs
- **Invoice automatically** — Completion signal not triggering invoice workflow
- **Report results back** — No feedback loop to marketing teams

**Root cause:** Agents orchestrated in isolation. Missing:
1. Event triggers (lead arrives → wake agent)
2. Output pipelines (agent decision → action in external systems)
3. Feedback loops (agent learns from outcomes)
4. OPCO assignments (agent identity in department)

---

# ACTUAL REMAINING WORK (Priority Order)

## Week 1: Wire Agents to OPCOs (CRITICAL)

```
Landing Page Form Submit
        ↓
Supabase: venture_leads
        ↓
n8n Webhook Trigger
        ↓
CON crew execution
        ↓
Output Actions:
  • Update CRM
  • Create calendar event
  • Draft proposal
  • Queue invoice
```

**Time:** 8-10 hours  
**Result:** One lead → flows through all agents → outputs in all systems

---

## Week 2: Unified Operational View

Create Grafana dashboard showing:
- All services health (docker ps)
- All agents + success rates
- All ventures + pipeline
- All MCPs available + used

**Time:** 6-8 hours

---

## Week 3: Venture Instantiation

One command launches venture (<30 min):
- Folder structure
- Landing page (Vercel)
- Supabase tables
- Neo4j node + relationships
- Agent assignment
- Slack channel
- Airtable row

**Time:** 12-16 hours

---

# SUMMARY

| Domain | Prompts | Complete | Missing | Action |
|--------|---------|----------|---------|--------|
| Infrastructure | 1–25 | 50% | 12–13 | Wire dashboard |
| Repositories | 26–50 | 20% | 20 | Index repos in Neo4j |
| Data Engineering | 51–75 | 40% | 15 | Build ELT pipeline |
| OmniRouter | 76–100 | 0% | 25 | Evaluate + integrate |
| MCP Ecosystem | 101–125 | 80% | 5 | Wire to agents |
| Multi-Agent OS | 126–150 | 60% | 10 | **Execute locally on OPCOs** |
| Venture Studio | 151–175 | 10% | 22 | Automate instantiation |
| Revenue Engines | 176–200 | 15% | 21 | Connect end-to-end |
| Civilization | 201–250 | 0% | 50 | Future |
| **TOTAL** | **250** | **32%** | **~160** | **Wire, don't rebuild** |

**Reality:** Don't write 160 new prompts. WIRE the 80 already done. The glue is missing, not the pieces.
