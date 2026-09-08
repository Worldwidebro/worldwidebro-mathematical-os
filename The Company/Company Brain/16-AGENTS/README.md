# 16-AGENTS: Routing & Execution Agents

**Layer:** 16/50  
**Status:** 🟢 ACTIVE  
**Updated:** 2026-09-02

**Owned by:** [[52-PEOPLE]] (managers, approvers, executors)  
**Governed by:** [[27-SECURITY]], [[46-GOVERNANCE]]

---

## Overview

Routing agents are the nerve system of Company Brain. Each agent:
- **Routes** tasks to appropriate execution context (L1/L2/L3)
- **Decides** which control plane to activate based on venture & task type
- **Executes** via Fractal loop orchestration
- **Costs** tracked per-step for autonomy budget gates
- **Approved by** [[52-PEOPLE]] (team leads, sector executives)

**Architecture:**
```
ClickUp Task → Webhook → Fractal Routing Agent → Neo4j → Control Plane
                                ↓
                         [[52-PEOPLE]] approval chain
```

---

## 5 Core Routing Agents

| Agent | Purpose | Fractal | Managed By | Approvers |
|-------|---------|---------|------------|-----------|
| [[AGT-001-venture-pm]] | Project mgmt | venture-pm | TBD | TBD |
| [[AGT-002-financial]] | Revenue | financial | TBD | TBD |
| [[AGT-003-technical]] | Infrastructure | technical | TBD | TBD |
| [[AGT-004-sales]] | Lead qualification | sales | TBD | TBD |
| [[AGT-005-operations]] | Workflow automation | operations | TBD | TBD |

---

## Education & Specialized Routing Fleet

| Agent | Purpose | Routing Key | Domain Link | Primary Execution Loop |
|:---|:---|:---|:---|:---|
| [[16-AGENTS/AGT-006-education-teacher\|AGT-006]] | Curriculum Planning & Presentation Slides | `education-teacher` | [[SECTORS/SEC-037-education\|SEC-037]] | [[node/plans/course-generation-loop\|Course Generation Loop]] |
| [[16-AGENTS/AGT-007-education-peer\|AGT-007]] | Discussion Design & Peer Interaction | `education-peer` | [[SECTORS/SEC-037-education\|SEC-037]] | [[node/plans/course-generation-loop\|Course Generation Loop]] |
| [[16-AGENTS/AGT-008-education-content\|AGT-008]] | Quiz Generation & Interactive Elements | `education-content` | [[SECTORS/SEC-037-education\|SEC-037]] | [[node/plans/course-generation-loop\|Course Generation Loop]] |
| [[16-AGENTS/AGT-009-education-eval\|AGT-009]] | Assessments, Outcomes & Learning Analytics | `education-eval` | [[42-EVALUATION/README\|42-EVALUATION]] | [[node/plans/course-generation-loop\|Course Generation Loop]] |

---

## Integration Points

### Fractal (Loop Orchestration)
- **Location:** `/fractal/fractal/impl/company_brain.py`
- **Status:** ✅ 5 agents implemented

### Company Brain Registry
- **Location:** `/_REGISTRIES/agents/AGT-*.yaml`
- **Status:** ✅ 5 metadata files

### Obsidian Vault
- **Location:** `/16-AGENTS/AGT-*.md`
- **Status:** ✅ 5 agent files with wikilinks

### Neo4j Knowledge Graph
- **Location:** `localhost:7687`
- **Status:** ⏸️ Auth pending
- **Relationships:** Agent → MANAGED_BY → Person, Agent → APPROVES → Person

### People & Teams
- **Location:** `[[52-PEOPLE]]`
- **Status:** 🟡 Pending assignments

---

## Approval Chain (L1 → L2 → L3)

```
L1: Person proposes via agent (reports only)
    ↓ (Person approves)
L2: Agent executes with monitoring (can retry)
    ↓ (After 10+ successes, Manager approves)
L3: Agent runs autonomously (no per-step approval)
```

---

## Related Domains

- [[52-PEOPLE]] ← Agent managers & approvers
- [[08-KNOWLEDGE-GRAPH]] ← Neo4j connections
- [[14-CAPABILITIES]] ← Agent capabilities
- [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER]] ← Sector assignments
- [Control Planes Registry](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES/control-planes-by-sector.yaml) ← Execution routing
- [[27-SECURITY]] ← Agent permissions
- [[46-GOVERNANCE]] ← Approval workflows

---

**Next:** Assign managers & approvers from [[52-PEOPLE]] to each agent

**See also:** [Agents Registry](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES/agents/), [[02-SOURCES]] (data feeds)

---

## Specialized Engineering, Sales & Financial Agents (`.agents/agents/`)

| [[.agents/agents/portfolio-manager|Portfolio Manager]] | Ventures | Master 789-venture portfolio governance, stage progression, monetization velocity | `portfolio-manager.md` |
| [[.agents/agents/product-manager|Product Manager]] | Product | PRDs, user pain points, MVP scoping, product-market fit, outcome metrics | `product-manager.md` |
| [[.agents/agents/senior-project-manager|Senior Project Manager]] | Project Mgmt | Task breakdowns, 30-60m dev task lists, sprint execution without scope creep | `senior-project-manager.md` |
| [[.agents/agents/engineering-database-optimizer|Database Optimizer]] | Engineering | Schema design, indexing strategies, query tuning, and EXPLAIN ANALYZE | `engineering-database-optimizer.md` |
| [[.agents/agents/engineering-payments-billing-engineer|Payments & Billing]] | Engineering | PSP integrations (Stripe, Adyen), idempotent webhooks, SCA/3DS | `engineering-payments-billing-engineer.md` |
| [[.agents/agents/finance-financial-analyst|Financial Analyst]] | Finance | Scenario modeling, unit economics, cash-flow forecasting | `finance-financial-analyst.md` |
| [[.agents/agents/sales-deal-strategist|Deal Strategist]] | Sales | MEDDPICC qualification, enterprise positioning, win planning | `sales-deal-strategist.md` |
| [[.agents/agents/sales-outbound-strategist|Outbound Strategist]] | Sales | Signal-based prospecting sequences, ICP definitions | `sales-outbound-strategist.md` |
| [[.agents/agents/architect|System Architect]] | Architecture | System boundaries, domain modeling, ADRs | `architect.md` |
| [[.agents/agents/devops|DevOps Engineer]] | Operations | CI/CD pipelines, Docker container lifecycles | `devops.md` |
| [[.agents/agents/engineer|Software Engineer]] | Engineering | Full-stack development, polyglot implementations | `engineer.md` |
| [[.agents/agents/qa|QA Engineer]] | Quality | End-to-end testing, test suites, regression prevention | `qa.md` |
| [[.agents/agents/repository-intelligence|Repository Intelligence]] | Knowledge | GitHub inventory audits, code reality verification | `repository-intelligence.md` |
| [[.agents/agents/researcher|Researcher]] | Research | Scholarly literature, competitive analysis | `researcher.md` |
| [[.agents/agents/security|Security Auditor]] | Security | Zero-trust review, AST dependency vulnerability scanning | `security.md` |

---

## Modular Skills & Agency Personas Fleet (`.agents/skills/`)

For on-demand behavioral personas and procedural operational runbooks imported from `msitarzewski/agency-agents`, consult the master catalog:
- 📖 **Full Catalog & Wikilinks (280 Skills):** [[15-SKILLS/README|15-SKILLS Fleet Catalog]]
- **Divisions Covered:** Academic & Research, Business Operations, Engineering, Finance, Game Development, GIS & Spatial, Healthcare, Marketing, Paid Media, Product, Project Management, Sales, Security, Spatial Computing, Testing, and Specialized Cultural Navigation.

