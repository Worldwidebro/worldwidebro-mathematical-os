# Master Folder Map: Repository Structure → WORLDWIDEBRO-OS

**Date:** 2026-07-20  
**Purpose:** Show how 5 separate GitHub repos map into the unified WORLDWIDEBRO-OS structure

---

## The Architecture

```
5 SEPARATE GITHUB REPOS (Source of Truth)
├── worldwidebro-executive
├── worldwidebro-directives
├── vex-hero-site
├── worldwidebro-knowledge-base
└── worldwidebro-infrastructure

                ↓ SYNC/MIRROR ↓

WORLDWIDEBRO-OS (Unified Structure - 712 Ventures Inherit Everything)
```

---

## Repo 1: worldwidebro-executive → EXECUTIVE/

**Purpose:** Strategic oversight, leadership intelligence, portfolio management  
**Frequency:** Weekly updates  

```
worldwidebro-executive/
├── CEO/
│   ├── CEO-MISSION.md
│   ├── CEO-DASHBOARD.md
│   ├── CEO-DECISION-FRAMEWORK.md
│   ├── CEO-AGENDA.md
│   └── CEO-REPORTS.md
├── CFO/
│   ├── FINANCIAL-OVERVIEW.md
│   ├── CAPITAL-ALLOCATION.md
│   ├── CASHFLOW.md
│   └── INVESTMENT-ANALYSIS.md
├── CTO/
├── CMO/
├── COO/
├── PORTFOLIO/
└── REPORTING/

    ↓ SYNCS TO ↓

WORLDWIDEBRO-OS/EXECUTIVE/
```

---

## Repo 2: worldwidebro-directives → DIRECTIVES/

**Purpose:** Operating constitution, decision rules, priorities  
**Frequency:** Monthly (when strategy changes)

```
worldwidebro-directives/
├── NORTH-STAR-DIRECTIVE.md
├── STRATEGIC-DIRECTIVES/
├── OPERATING-DIRECTIVES/
├── VENTURE-DIRECTIVES/
├── AI-DIRECTIVES/
├── PRIORITY/
└── DECISIONS/

    ↓ SYNCS TO ↓

WORLDWIDEBRO-OS/DIRECTIVES/
```

---

## Repo 3: vex-hero-site → GROWTH-OS/ + ANALYTICS/

**Purpose:** CEO dashboard, portfolio UI, public website  
**Frequency:** Daily (data), Weekly (features)

```
vex-hero-site/
├── src/app/dashboard/ → WORLDWIDEBRO-OS/GROWTH-OS/DASHBOARDS/
├── src/app/sectors/[slug]/ → WORLDWIDEBRO-OS/GROWTH-OS/SECTOR-PAGES/
├── data/portfolio.public.json → WORLDWIDEBRO-OS/ANALYTICS/PORTFOLIO-DATA/
└── src/api/ → WORLDWIDEBRO-OS/06-TECHNOLOGY/APIs/
```

---

## Repo 4: worldwidebro-knowledge-base → KNOWLEDGE-OS/

**Purpose:** Neo4j graphs, Qdrant vectors, semantic indexing  
**Frequency:** Real-time (graphs are live)

```
worldwidebro-knowledge-base/
├── graphs/ → WORLDWIDEBRO-OS/KNOWLEDGE-OS/GRAPH-SCHEMAS/
├── vectors/ → WORLDWIDEBRO-OS/KNOWLEDGE-OS/EMBEDDINGS/
├── registries/ → WORLDWIDEBRO-OS/08-DATA/registries/
├── ingestion/ → WORLDWIDEBRO-OS/KNOWLEDGE-OS/INGESTION/
└── queries/ → WORLDWIDEBRO-OS/KNOWLEDGE-OS/QUERIES/
```

---

## Repo 5: worldwidebro-infrastructure → TECHNOLOGY/

**Purpose:** Docker, databases, MCPs, tools, observability  
**Frequency:** Weekly (config), Daily (health)

```
worldwidebro-infrastructure/
├── docker-compose.yml → WORLDWIDEBRO-OS/TECHNOLOGY/infrastructure/
├── services/ → WORLDWIDEBRO-OS/TECHNOLOGY/infrastructure/services/
├── mcps/ → WORLDWIDEBRO-OS/08-DATA/registries/mcp-servers/
├── tools/ → WORLDWIDEBRO-OS/08-DATA/registries/tools-registry.yaml
├── observability/ → WORLDWIDEBRO-OS/TECHNOLOGY/observability/
└── scripts/ → WORLDWIDEBRO-OS/scripts/
```

---

## Complete Structure

```
WORLDWIDEBRO-OS/
├── EXECUTIVE/  ← worldwidebro-executive
├── DIRECTIVES/  ← worldwidebro-directives
├── IDENTITY-OS/
├── KNOWLEDGE-OS/  ← worldwidebro-knowledge-base
├── 05-AGENTS/
├── 06-TECHNOLOGY/  ← worldwidebro-infrastructure
├── AI-PLATFORM/
├── VENTURE-FACTORY/
├── GROWTH-OS/  ← vex-hero-site
├── BUSINESS-OPERATIONS/
├── 03-PORTFOLIO/ (712 ventures)
├── 08-DATA/ (registries, analytics)
└── ANALYTICS/  ← vex-hero-site data/
```

---

## Data Flow

```
EXECUTIVE DECISION
    ↓
DIRECTIVE (rules from decision)
    ↓
TECHNOLOGY (infrastructure wires up)
    ↓
KNOWLEDGE (graph updated)
    ↓
DASHBOARDS (reflect new state)
    ↓
ALL 712 VENTURES INHERIT
```

---

## Navigation

- **Strategy?** → `WORLDWIDEBRO-OS/EXECUTIVE/`
- **Rules?** → `WORLDWIDEBRO-OS/DIRECTIVES/`
- **Portfolio health?** → vex-hero-site dashboard
- **Relationships?** → `WORLDWIDEBRO-OS/KNOWLEDGE-OS/`
- **Infrastructure?** → `WORLDWIDEBRO-OS/06-TECHNOLOGY/`

---

*5 repos. 1 unified OS. 712 ventures inherit everything.*
