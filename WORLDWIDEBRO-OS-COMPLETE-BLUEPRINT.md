---
title: Worldwidebro OS — Complete System Blueprint
date: 2026-07-27
version: 1.0
status: PHASE 3 COMPLETE
---

# Worldwidebro OS — Complete System Blueprint

**Mission:** Build a $100M holding company by orchestrating 712 ventures across 38 sectors using unified AI operating system.

**Legal Entity:** WinnerCircle WC LLC  
**Operating Name:** Worldwidebro Holdings  
**GitHub Org:** @Worldwidebro  
**Email:** winnerscirclewcllc@gmail.com

---

## System Layers (7-Layer Stack)

```
┌────────────────────────────────────────────────────────────────────┐
│ LAYER 1: EXPERIENCE                                                │
│ Apps, Dashboards, Mobile, Web, Voice                              │
│ (Worldwidebro Venture Portal + Agent Command Center)              │
└────────┬─────────────────────────────────────────────────────────┘
         │
┌────────▼─────────────────────────────────────────────────────────┐
│ LAYER 2: AGENT OPERATING SYSTEM                                  │
│ Fractal Orchestration + CrewAI Pipelines + Agent Roster           │
│                                                                    │
│ Canonical Repo: worldwidebro-os-business-engine                  │
│ 22 Agents × 6 OPCOs (CON, STA, RE, EDU, FIN, LOG)                │
│ Decision Authority: 90%+ AUTONOMOUS, 70-79% MONITORED, <70% TRAINING
│                                                                    │
│ Files:                                                             │
│ ├─ .fractal_agent_spawn.py (spawn nodes, 6 parallel children)   │
│ ├─ crewai-agent-orchestrator.py (4-agent CON pipeline)          │
│ ├─ .planning/AGENTS.md (22 agents, decision authority)           │
│ └─ AGENT-OPERATING-SYSTEM.md (standards, KPIs)                   │
└────────┬─────────────────────────────────────────────────────────┘
         │
┌────────▼─────────────────────────────────────────────────────────┐
│ LAYER 3: KNOWLEDGE GRAPH OS                                      │
│ Neo4j + PostgreSQL + Qdrant                                       │
│                                                                    │
│ Canonical Repo: worldwidebro-os-knowledge-graph                  │
│ 10 Entity Types, Key Relationships, Storage Map                   │
│                                                                    │
│ Files:                                                             │
│ ├─ ONTOLOGY.md (entity definitions + relationships)               │
│ ├─ neo4j-schema.cypher (graph constraints)                        │
│ └─ supabase-schema.sql (transactional schema)                     │
└────────┬─────────────────────────────────────────────────────────┘
         │
┌────────▼─────────────────────────────────────────────────────────┐
│ LAYER 4: AI INFRASTRUCTURE                                        │
│ 9 Services: Neo4j, PostgreSQL, Redis, Qdrant, LiteLLM,           │
│ Langfuse, Prometheus, OTel, n8n                                   │
│                                                                    │
│ Canonical Repo: worldwidebro-os-infrastructure                   │
│                                                                    │
│ Files:                                                             │
│ ├─ docker-compose.yml (9 services)                                │
│ ├─ Makefile (20+ commands)                                        │
│ ├─ scripts/bootstrap.sh (9-phase setup)                           │
│ └─ scripts/health-check.sh (service validation)                   │
│                                                                    │
│ Entry Point: make bootstrap (3-5 min)                             │
└────────┬─────────────────────────────────────────────────────────┘
         │
┌────────▼─────────────────────────────────────────────────────────┐
│ LAYER 5: SKILL + TOOLS REGISTRY                                  │
│ 296+ Skills × 14 Phases + 40+ Tools + 18 MCPs                    │
│                                                                    │
│ Canonical Repo: worldwidebro-os-business-engine                  │
│                                                                    │
│ Files:                                                             │
│ ├─ agent_tools_registry.yaml (40+ tools → agents)                │
│ ├─ MCP_REGISTRY.json (18 MCPs)                                   │
│ └─ SKILL-INDEX.md (296+ skills indexed)                          │
└────────┬─────────────────────────────────────────────────────────┘
         │
┌────────▼─────────────────────────────────────────────────────────┐
│ LAYER 6: DECISION ENGINE + GOVERNANCE                            │
│ 8-Layer Trace, Permission System, Audit Trail                    │
│                                                                    │
│ 8 Layers: Registry → Agent Factory → Task Executor → Directive    │
│ Enforcer → MCP Slack → Director → Execution → Audit Trail        │
│                                                                    │
│ Files:                                                             │
│ ├─ decision_audit_trace.py (8-layer engine)                      │
│ ├─ permissions.json (per-agent limits)                           │
│ └─ governance_engine.py (escalation logic)                       │
└────────┬─────────────────────────────────────────────────────────┘
         │
┌────────▼─────────────────────────────────────────────────────────┐
│ LAYER 7: TRUST + GOVERNANCE                                      │
│ Success Rate → Authority, Audit Logs, Security, Monitoring       │
│                                                                    │
│ Evaluation: 90%+ AUTONOMOUS, 80-89% SUPERVISED,                  │
│ 70-79% MONITORED, <70% TRAINING                                  │
│                                                                    │
│ Auditing: Supabase + Neo4j + Grafana + Slack                     │
│ Security: MCP Slack alerts, director approvals                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## Repository Authority Tiers

### Tier 1 (Canonical — Never Fork)
- **worldwidebro-os-knowledge-graph** — Graph schema, entities, relationships
- **worldwidebro-os-business-engine** — Agents, skills, tools, decision logic
- **worldwidebro-os-infrastructure** — Docker, bootstrap, health checks

→ All other repos reference, never duplicate

### Tier 2 (Sector Extensions — Extend, Don't Override)
- **worldwidebro-construction-os** — CON-specific
- **worldwidebro-finance-os** — FIN-specific
- **worldwidebro-staffing-os** — STA-specific
- **worldwidebro-education-os** — EDU-specific
- **worldwidebro-marketing-os** — MKTG-specific

→ Extend base schemas, reference Tier 1

### Tier 3 (Consumption — Read-Only)
- **worldwidebro-ventures** — 712 ventures
- **worldwidebro-venture-portal** — Sector discovery
- **worldwidebro-agent-command-center** — Operations

→ Read from Tier 1 + Tier 2

---

## Agent Roster

| Sector | Agent | Role | Success Rate | Authority |
|--------|-------|------|---|---|
| **CON** | venture_classifier | Classify leads | 94% | AUTONOMOUS |
| | estimator_gen1 | Estimate costs | 88% | SUPERVISED |
| | risk_assessor | Risk ID | 91% | AUTONOMOUS |
| | project_scheduler | Schedule | 75% | MONITORED |
| **STA** | candidate_matcher | Match skills | TBD | TRAINING |
| | availability_tracker | Schedule shifts | TBD | TRAINING |
| | rate_optimizer | Dynamic pay | TBD | TRAINING |
| **RE** | property_valuer | Valuate | TBD | TRAINING |
| | listing_categorizer | Tag | TBD | TRAINING |
| | lead_qualifier | Score | TBD | TRAINING |
| **EDU** | student_tracker | Monitor | TBD | TRAINING |
| | content_atomizer | Generate | TBD | TRAINING |
| | enrollment_optimizer | Recommend | TBD | TRAINING |
| **FIN** | transaction_processor | GL categorize | TBD | TRAINING |
| | risk_calculator | Portfolio risk | TBD | TRAINING |
| | compliance_checker | Monitor | TBD | TRAINING |
| **LOG** | route_optimizer | Optimize | TBD | TRAINING |
| | shipment_tracker | Track | TBD | TRAINING |
| | cost_calculator | Estimate | TBD | TRAINING |

---

## Quick Start

**Bootstrap (3-5 minutes):**
```bash
cd /tmp/civ-infra-work
make bootstrap
make health
make seed
```

**Services:**
- Grafana: http://localhost:3001
- Neo4j: http://localhost:7474
- Qdrant: http://localhost:6333
- LiteLLM: http://localhost:4000
- Langfuse: http://localhost:3003

---

## Success Metrics

- Agent success rates: CON agents 75-94% ✓
- System uptime: >99.5%
- Decision latency: <30s lead → estimate
- Venture coverage: 4 → 50+ by Q4

---

**Status:** ✅ PHASE 1 (Brand Consolidation) + PHASE 2 (Authority Matrix) + PHASE 3 (Master Blueprint) COMPLETE
