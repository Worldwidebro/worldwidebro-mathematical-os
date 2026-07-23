---
name: AI-BOSS-OS Git & Monorepo Strategy
type: Infrastructure Strategy
last-updated: 2026-07-22
purpose: Maps layer-based branches, venture subrepos, and monorepo structure to existing WORLDWIDEBRO-OS folders and GitHub
---

# AI-BOSS-OS GIT & MONOREPO STRATEGY
**Aligning Layer Architecture with Git Branches, GitHub Repos, and Local Folder Structure**

---

## 🌳 BRANCH ARCHITECTURE (Layer-Based + Venture-Based)

```
main (stable, production infrastructure)
│
├── INFRASTRUCTURE LAYER BRANCHES (released independently)
│   ├── layer/obsidian-vault      ← Knowledge authoring (Obsidian syncs here)
│   ├── layer/neo4j               ← Relationship graph schema + migrations
│   ├── layer/qdrant              ← Embeddings + collections + pipelines
│   ├── layer/postgres            ← Database schema + migrations + audit trails
│   ├── layer/agents              ← Agent definitions, permissions, factory
│   ├── layer/omniroute           ← Model routing config + rules
│   └── layer/observability       ← Langfuse dashboards + tracing rules
│
└── VENTURE BRANCHES (experiment fast, iterate per venture)
    ├── venture/STA-001-staffing  ← Staffing venture (pulls infrastructure/* )
    ├── venture/CON-001-construction
    ├── venture/FIN-001-finance
    └── ...up to 712 ventures (created on-demand)
```

**Release Model:**
- Infrastructure branches merge → main independently (Neo4j schema v2 ships separately from agent v3)
- Venture branches iterate fast locally, pull shared infrastructure updates automatically

---

## 📁 MONOREPO STRUCTURE (Main GitHub Repo)

```
worldwidebro/ (main monorepo)
├── .gitmodules                    ← Git subtree references to 712 venture repos
├── .github/workflows/             ← CI/CD for infrastructure layers
│   ├── neo4j-schema-tests.yml
│   ├── agent-factory-tests.yml
│   └── venture-sync.yml
│
├── infrastructure/                ← Core layers (layer/* branches track these)
│   ├── neo4j/
│   │   ├── schema/
│   │   │   ├── 001-venture-model.cypher
│   │   │   ├── 002-relationships.cypher
│   │   │   └── loader.py
│   │   └── migrations/
│   │
│   ├── qdrant/
│   │   ├── collections/
│   │   │   ├── repositories.json
│   │   │   ├── notes.json
│   │   │   └── embeddings.py
│   │   └── rebuilds/
│   │
│   ├── postgres/
│   │   ├── schema/
│   │   │   ├── 001-ventures.sql
│   │   │   ├── 002-relationships.sql
│   │   │   └── migrations/
│   │   └── supabase-config/
│   │
│   ├── omniroute/
│   │   ├── config/
│   │   │   ├── routing-rules.yaml
│   │   │   ├── model-weights.json
│   │   │   └── token-budget.yaml
│   │   └── integrations/
│   │
│   └── observability/
│       ├── langfuse/
│       │   ├── dashboards.json
│       │   ├── rules.yaml
│       │   └── cost-tracking.yaml
│       └── prometheus/
│
├── knowledge/                     ← Obsidian vault (layer/obsidian-vault)
│   ├── 00-IDENTITY/
│   │   ├── values.md
│   │   ├── goals.md
│   │   └── principles.md
│   ├── 01-VENTURES/
│   │   ├── STA-001/
│   │   │   ├── strategy.md
│   │   │   └── roadmap.md
│   │   └── ...
│   ├── 02-KNOWLEDGE/
│   │   ├── business/
│   │   ├── technology/
│   │   └── science/
│   ├── 03-DECISIONS/
│   │   └── ADR-*.md
│   └── 04-ARCHIVE/
│
├── agents/                        ← Agent definitions (layer/agents)
│   ├── ceo-agent.yaml
│   ├── research-agent.yaml
│   ├── engineering-agent.yaml
│   ├── finance-agent.yaml
│   ├── operations-agent.yaml
│   ├── agent_factory.py
│   ├── permissions.json
│   └── tests/
│
├── shared/                        ← Reusable across all ventures
│   ├── schemas/
│   │   ├── venture-schema.sql
│   │   ├── venture.json-schema
│   │   └── capability-taxonomy.json
│   ├── templates/
│   │   ├── venture-template/
│   │   │   ├── founding-doc.md
│   │   │   └── README.md
│   │   └── agent-template/
│   ├── playbooks/
│   │   ├── 30-day-playbook.md
│   │   ├── integration-playbook.md
│   │   └── venture-completion-checklist.md
│   └── skills/
│       └── 296-skills-reference.md
│
└── ventures/                      ← Git subtree references (712 venture repos)
    ├── STA-001/
    │   ├── (pulls from worldwidebro/STA-001 repo)
    │   ├── README.md
    │   ├── src/
    │   ├── docs/
    │   └── tests/
    ├── CON-001/
    ├── FIN-001/
    └── ...up to 712
```

---

## 🔄 GIT WORKFLOW

**Infrastructure Changes (Layer Branches)**
```
layer/neo4j (update schema)
    ↓
feature/neo4j-agent-edges
    ↓
PR → Code Review → Merge to layer/neo4j → main
    ↓
All venture/* branches auto-sync updated schema
```

**Venture Changes (Venture Branches)**
```
venture/STA-001 (staffing logic)
    ↓
feature/STA-001-matching-v2
    ↓
PR → Code Review → Merge to venture/STA-001 → main
    ↓
Deployed independently, doesn't block other ventures
```

---

## 📂 MAPPING: WORLDWIDEBRO-OS Folder → Git Structure

**TODAY: Disk**
```
~/Documents/WORLDWIDEBRO-OS/
├── 00-DIRECTIVES/             → knowledge/ (layer/obsidian-vault)
├── 04-OPERATIONS/playbooks/   → shared/playbooks/
├── 05-AGENTS/                 → agents/ (layer/agents)
└── REGISTRIES/                → infrastructure/postgres/schema
```

**TOMORROW: Git-Ready**
```
~/worldwidebro/ (monorepo)
├── infrastructure/            (Neo4j, Qdrant, PostgreSQL, OmniRoute, Observability)
├── knowledge/                 (Obsidian vault, synced to Neo4j)
├── agents/                    (Agent definitions, CrewAI)
├── shared/                    (Templates, playbooks, schemas)
└── ventures/                  (712 venture subtrees)
```

---

## 🎯 ALIGNMENT TABLE: Layers ↔ Branches ↔ Repos ↔ Folders

| Layer | Branch | GitHub Repo | Local Folder | Syncs To |
|-------|--------|-------------|--------------|----------|
| **Obsidian** | `layer/obsidian-vault` | `worldwidebro/worldwidebro:knowledge/` | `~/worldwidebro/knowledge/` | Neo4j |
| **Neo4j** | `layer/neo4j` | `worldwidebro/worldwidebro:infrastructure/neo4j/` | `~/worldwidebro/infrastructure/neo4j/` | Postgres |
| **Qdrant** | `layer/qdrant` | `worldwidebro/worldwidebro:infrastructure/qdrant/` | `~/worldwidebro/infrastructure/qdrant/` | Qdrant server |
| **PostgreSQL** | `layer/postgres` | `worldwidebro/worldwidebro:infrastructure/postgres/` | `~/worldwidebro/infrastructure/postgres/` | Supabase |
| **Agents** | `layer/agents` | `worldwidebro/worldwidebro:agents/` | `~/worldwidebro/agents/` | CrewAI |
| **OmniRoute** | `layer/omniroute` | `worldwidebro/OmniRoute` (standalone) | `~/worldwidebro/infrastructure/omniroute/` | Model routing |
| **Langfuse** | `layer/observability` | `worldwidebro/worldwidebro:infrastructure/observability/` | `~/worldwidebro/infrastructure/observability/` | Langfuse |
| **Shared** | `main` | `worldwidebro/worldwidebro:shared/` | `~/worldwidebro/shared/` | All ventures |
| **Ventures** | `venture/X` | `worldwidebro/X` (712 repos) | `~/worldwidebro/ventures/X/` | Independent CI/CD |

---

## 📋 KEY FILES THAT BRIDGE LAYERS

| File | Purpose | Lives In | Git Flow |
|------|---------|----------|----------|
| `venture-schema.sql` | Canonical venture definition | `shared/schemas/` | Git → Supabase migration |
| `30-day-playbook.md` | Execution framework | `shared/playbooks/` | Git → Ventures pull |
| `agent.yaml` | Agent definitions | `agents/` | Git → CrewAI load |
| `capability-taxonomy.json` | Shared capabilities | `shared/schemas/` | Git → Neo4j seed |
| `neo4j-schema.cypher` | Graph structure | `infrastructure/neo4j/` | Git → Neo4j load |
| `routing-rules.yaml` | Model routing config | `infrastructure/omniroute/` | Git → OmniRoute reload |
| `langfuse-dashboards.json` | Observability setup | `infrastructure/observability/` | Git → Langfuse load |

---

## ✅ THIS ALIGNS WITH YOUR AI-BOSS-OS VISION

**You proposed:**

> "OmniRoute is the model-routing nervous system"

**Maps to:** `infrastructure/omniroute/config/` on `layer/omniroute` branch — central routing logic, versioned, deployed independently.

> "Obsidian = human knowledge, Neo4j = machine brain"

**Maps to:** `knowledge/` synced to Neo4j via `layer/obsidian-vault` → Neo4j script. Every decision written in Obsidian becomes a graph node.

> "Qdrant = semantic memory"

**Maps to:** `infrastructure/qdrant/` with rebuild pipelines. Repository vectors (1,648), notes embeddings, all queryable by agents.

> "All 712 ventures spawn from templates"

**Maps to:** `ventures/` with git subtrees + `shared/templates/venture-template/`. Each venture pulls shared schemas, playbooks, and agent definitions.

> "Everything observable via Langfuse"

**Maps to:** `infrastructure/observability/langfuse/` feeds traces, costs, decisions from all layers. Single dashboard shows everything.

---

## 🚀 NEXT STEPS

**Week 1: Initialize Monorepo**
- Create `worldwidebro/worldwidebro` GitHub repo
- Initialize `~/worldwidebro/` locally
- Create layer/* branches
- Move infrastructure files into structure

**Week 2: Add Venture Subtrees**
- Add git subtrees for first 3 ventures (STA, CON, FIN)
- Verify shared/ inheritance
- Test CI/CD per venture

**Week 3-4: Activate Sync Pipelines**
- Obsidian → Neo4j sync
- Layer branches → all ventures auto-pull
- Langfuse instrumentation live

**Result:** A version-controlled, observable, scalable AI-BOSS-OS where all 712 ventures share infrastructure but iterate independently.
