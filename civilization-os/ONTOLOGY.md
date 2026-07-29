# Civilization OS — Entity Ontology

## Core Entities

### Venture
**Definition:** Autonomous business unit operating within a sector, with its own product, revenue model, and P&L.

**Attributes:**
- `id`: VEN-{SECTOR}-{NUMBER} (e.g., CON-001, FIN-042)
- `name`: Human-readable venture name
- `sector`: LT, FIN, CON, RE, EDU, STA, MKTG, TECH, etc. (38 total)
- `stage`: IDEA, MVP, GROWTH, SCALE, EXIT
- `revenue_model`: subscription, marketplace, services, product, hybrid
- `status`: planned, active, paused, archived
- `founder_id`: FK to Founder
- `opco_id`: FK to OPCO
- `created_at`, `updated_at`: Timestamps

**Relationships:**
- `HAS_PRODUCTS` → Product
- `HAS_LEAD_CAPTURES` → Lead
- `HAS_DEALS` → Deal
- `BELONGS_TO` → OPCO
- `LED_BY` → Founder

---

### OPCO (Operating Company)
**Definition:** Sector-level holding company orchestrating 40-150 ventures with shared infrastructure, agents, and compliance.

**Attributes:**
- `id`: {SECTOR}-OS (e.g., CON-OS, FIN-OS)
- `name`: Sector operating company name
- `sector`: LT, FIN, CON, RE, EDU, STA, MKTG, TECH
- `mission`: Strategic mission for the sector
- `parent_company_id`: FK to Parent (Worldwidebro Holdings)
- `status`: active, archived
- `created_at`: Timestamp

**Known OPCOs (6 primary):**
- **CON-OS** (Construction) — worldwidebro-construction-os
- **STA-OS** (Staffing) — worldwidebro-staffing-os
- **RE-OS** (Real Estate) — worldwidebro-real-estate-os
- **EDU-OS** (Education) — worldwidebro-education-os
- **FIN-OS** (Finance) — worldwidebro-finance-os
- **LOG-OS** (Logistics) — worldwidebro-logistics-os

**Relationships:**
- `ORCHESTRATES` → Venture (40-150 per OPCO)
- `OWNS_AGENTS` → Agent (3-4 per OPCO)
- `ENFORCES_GOVERNANCE` → GovernancePolicy
- `OWNS_INFRASTRUCTURE` → InfrastructureComponent

---

### Founder
**Definition:** Human operator responsible for venture growth, Human OS development, and strategic decisions.

**Attributes:**
- `id`: FOU-{NUMBER}
- `name`: Founder name
- `email`: Email address
- `venture_ids`: [FK to Venture, ...]
- `success_rate`: % of executed tasks with positive outcomes
- `learning_velocity`: Growth rate across Human OS layers
- `authority_level`: AUTONOMOUS (90%+), MONITORED (70-79%), TRAINING (<70%)
- `created_at`, `updated_at`: Timestamps

**Relationships:**
- `LEADS` → Venture
- `DEVELOPS_SKILLS_IN` → HumanOSLayer (10 layers total)
- `RECEIVES_COACHING_FROM` → Coach
- `HAS_AUTHORITY_LEVEL` → GovernanceLevel

---

### Investor
**Definition:** Capital partner providing funding, oversight, and strategic guidance across the portfolio.

**Attributes:**
- `id`: INV-{NUMBER}
- `name`: Investor name or firm
- `type`: individual, fund, strategic_partner
- `capital_committed`: USD amount
- `capital_deployed`: USD amount
- `status`: active, exited
- `created_at`: Timestamp

**Relationships:**
- `FUNDS` → OPCO
- `PROVIDES_OVERSIGHT_TO` → Venture
- `HAS_EXIT_TERMS` → Deal

---

### Agent
**Definition:** AI agent orchestrating decision-making, task execution, and reporting for a specific domain within an OPCO.

**Attributes:**
- `id`: AGT-{SECTOR}-{NUMBER}
- `name`: Agent name (e.g., venture_classifier, estimator_gen1)
- `role`: Classification, estimation, risk assessment, scheduling, optimization, etc.
- `sector`: Which OPCO owns this agent
- `success_rate`: % of tasks completed correctly
- `decision_authority`: AUTONOMOUS, SUPERVISED, MONITORED, TRAINING
- `tools`: [array of tool IDs]
- `mcp_integrations`: [array of MCP IDs]
- `created_at`, `updated_at`: Timestamps

**Relationships:**
- `BELONGS_TO` → OPCO
- `EXECUTES_TASKS` → Task
- `USES_TOOLS` → Tool
- `INTEGRATES_WITH` → MCP
- `ESCALATES_TO` → Director (human approval)

---

### Skill
**Definition:** Named workflow or capability indexed by phase and sector, executed by agents or humans.

**Attributes:**
- `id`: SKL-{NUMBER}
- `name`: Skill name (e.g., /gsd-plan-phase, /code-review)
- `phase`: One of 14 execution phases
- `sector`: Which sectors use this skill
- `execution_time`: Typical time to execute
- `success_rate`: Historical success %
- `requires_human_input`: boolean
- `created_at`: Timestamp

**Relationships:**
- `INDEXED_BY` → Phase
- `AVAILABLE_IN` → Sector
- `INVOKED_BY` → Agent
- `REQUIRED_FOR` → ExecutionFlow

---

### Tool
**Definition:** Operational capability (CLI command, API endpoint, integration) available to agents.

**Attributes:**
- `id`: TL-{NUMBER}
- `name`: Tool name (e.g., bash, Write, Bash, Read)
- `type`: bash, read, write, api_call, webhook, etc.
- `permissions_required`: [array of permission strings]
- `rate_limit`: Calls per minute (if applicable)
- `cost_per_call`: USD (for API tools)
- `created_at`: Timestamp

**Relationships:**
- `AVAILABLE_TO` → Agent
- `GUARDED_BY` → Permission
- `INTEGRATED_BY` → MCP

---

### MCP (Model Context Protocol)
**Definition:** Integration layer connecting Claude to external systems (GitHub, Slack, Zapier, HubSpot, etc.).

**Attributes:**
- `id`: MCP-{NUMBER}
- `name`: MCP name (e.g., github, slack, zapier)
- `version`: Semantic version
- `status`: active, deprecated
- `tools_provided`: Number of tools exposed
- `integrations`: [array of system names]
- `authentication`: oauth2, api_key, custom
- `created_at`, `updated_at`: Timestamps

**Relationships:**
- `EXPOSES` → Tool
- `INTEGRATES_WITH` → ExternalSystem
- `GOVERNED_BY` → Permission

---

### Decision
**Definition:** Discrete execution choice, tracked through 8-layer governance trace for audit and learning.

**Attributes:**
- `id`: DEC-{TIMESTAMP}-{RANDOM}
- `agent_id`: FK to Agent
- `task_id`: FK to Task
- `decision_type`: approve, execute, escalate, reject, learn
- `input_state`: JSON snapshot of decision inputs
- `output_state`: JSON snapshot of decision outcome
- `confidence`: 0.0-1.0 confidence score
- `trace_layers`: [8-layer audit trail, see GOVERNANCE.md]
- `created_at`, `updated_at`: Timestamps

**Relationships:**
- `MADE_BY` → Agent
- `EXECUTES` → Task
- `AUDITED_BY` → AuditTrail
- `ESCALATED_TO` → Director

---

### Task
**Definition:** Discrete work unit with clear start, end, success criteria, and tracking.

**Attributes:**
- `id`: TAS-{TIMESTAMP}-{RANDOM}
- `venture_id`: FK to Venture
- `agent_id`: FK to Agent (if agent-assigned)
- `title`: Task name
- `description`: Full task description
- `status`: planned, in_progress, blocked, completed, failed
- `priority`: 1-5 (1=highest)
- `estimated_hours`: Effort estimate
- `actual_hours`: Time spent
- `assigned_to`: FK to Founder or Agent
- `due_date`: Deadline
- `created_at`, `updated_at`: Timestamps

**Relationships:**
- `BELONGS_TO` → Venture
- `ASSIGNED_TO` → Agent or Founder
- `BLOCKED_BY` → Task (dependency)
- `EXECUTED_BY` → Decision

---

### HumanOSLayer
**Definition:** One of 10 human development layers tracked for founder growth and authority escalation.

**Attributes:**
- `id`: HOL-{1..10}
- `name`: Layer name (e.g., Decision-Making, Emotional Intelligence)
- `order`: 1-10 (bottom-to-top development order)
- `description`: What proficiency looks like at each level
- `metrics`: [array of KPI names to track]

**Known Layers:**
1. Foundational Execution (task completion, reliability)
2. Judgment & Discernment (good decisions, risk assessment)
3. Emotional Resilience (stress management, bounce-back)
4. Strategic Thinking (long-term vision, pattern recognition)
5. Complexity Navigation (systems thinking, multi-causality)
6. Leadership Presence (influence, communication, vision casting)
7. Systems Architecture (designing for scale, scalability)
8. Institutional Building (culture, governance, org design)
9. Capital Stewardship (finance, M&A, exit readiness)
10. Civilization Building (legacy, systemic impact, ecosystem design)

**Relationships:**
- `DEVELOPED_BY` → Founder
- `MEASURED_BY` → Metric

---

## Relationship Summary

```
Worldwidebro Holdings (root)
├── OPCO (6 sectors: CON, STA, RE, EDU, FIN, LOG)
│   ├── ORCHESTRATES → Venture (712 total, 40-150 per OPCO)
│   │   ├── LED_BY → Founder
│   │   ├── HAS_PRODUCTS → Product
│   │   ├── HAS_LEAD_CAPTURES → Lead
│   │   └── HAS_DEALS → Deal
│   │
│   ├── OWNS_AGENTS → Agent (22 total, 3-4 per OPCO)
│   │   ├── USES_TOOLS → Tool (40+ total)
│   │   ├── INTEGRATES_WITH → MCP (18 total)
│   │   ├── EXECUTES_TASKS → Task
│   │   └── ESCALATES_TO → Director
│   │
│   └── ENFORCES_GOVERNANCE → GovernancePolicy
│       ├── USES_SKILLS → Skill (296+ total, 14 phases)
│       └── AUDITS_DECISIONS → Decision (8-layer trace)
│
└── Founder (portfolio of ventures)
    ├── LEADS → Venture
    ├── DEVELOPS_SKILLS_IN → HumanOSLayer (10 layers)
    └── RECEIVES_COACHING_FROM → Coach

Investor (cross-holding)
├── FUNDS → OPCO
├── PROVIDES_OVERSIGHT_TO → Venture
└── HAS_EXIT_TERMS → Deal
```

---

## Storage Map

| Entity | Primary Store | Secondary Store | Indexed By |
|--------|---------------|-----------------|-----------|
| Venture | PostgreSQL (Supabase) | Neo4j (graph) | venture_id, sector, stage |
| OPCO | PostgreSQL (Supabase) | Neo4j (graph) | opco_id, sector |
| Founder | PostgreSQL (Supabase) | Neo4j (graph) | founder_id, authority_level |
| Agent | PostgreSQL (Supabase) | Neo4j (graph) | agent_id, sector, success_rate |
| Task | PostgreSQL (Supabase) | Neo4j (graph) | task_id, status, venture_id |
| Decision | PostgreSQL (Supabase) + Langfuse (audit) | Neo4j (graph) | decision_id, agent_id, timestamp |
| Skill | PostgreSQL (Supabase) | Neo4j (graph) | skill_id, phase, sector |
| Tool | PostgreSQL (Supabase) | Neo4j (graph) | tool_id, type |
| MCP | PostgreSQL (Supabase) | Neo4j (graph) | mcp_id, status |

---

See also:
- **TOPOLOGY.md** — System layers and infrastructure
- **GOVERNANCE.md** — Decision authority, escalation, audit
- **INTEGRATION.md** — Tier 1-3 repo relationships
