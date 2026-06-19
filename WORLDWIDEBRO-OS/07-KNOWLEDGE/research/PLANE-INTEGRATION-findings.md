---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[PLAN-WORKFLOW]]
  - [[FIN-036-ARBITRAGE-NEXUS]]
---

# Findings: Plane as 712-Venture Company Brain

**Last Updated**: 2026-06-04

**Project**: Unified Venture Operating System (PLANE as central hub)

---

## Current State Analysis

### Existing System Architecture (Today)

**Data Layer**:
- **Supabase** (source of truth): 712 ventures with sectors, contacts, metrics, risks
- **Knowledge Graph**: LightRAG with 17 entity types and 3 relationship types
- **GitHub**: 260+ venture repos

**Organization Layer**:
- **Obsidian**: Dataview dashboard showing entities + relationships
- **Planning files**: task_plan.md, findings.md, progress.md structure
- **Slack**: Real-time notifications + commands

**Agent Layer**:
- **Claude agents**: Autonomous system management
- **Scripts**: populate_venture_knowledge_graph.py, obsidian_graph_sync.py
- **Workflows**: n8n, Make for automation

**Current Pain Points**:
1. No single operational workspace (ventures in 5+ systems)
2. Manual status updates (not synchronized across systems)
3. No clear venture hierarchy (sector → venture → product → task)
4. Slack notifications are batch-based, not real-time
5. No project management structure (milestones, sprints, cycles)
6. GitHub repos disconnected from venture status
7. Agents must query multiple systems to understand venture health

---

## How Plane Solves This (Items 1-4 Alignment)

### Item 1: Phases of Creation/Implementation

**Phase 0: Foundation** → Understand existing 712 ventures + Plane architecture
- Inventory: 712 ventures in Supabase (sectors, metrics, risks, relationships)
- Inventory: Knowledge graph structure (17 entity types, 3 relationship types)
- Inventory: Existing sync scripts and automation
- Design question: How ventures map to Plane (projects? hierarchies?)

**Phase 1: Integration Layer** → Build bi-directional sync
- Supabase ventures → Plane projects (with metrics as custom fields)
- Plane task status → Supabase (closure tracking, milestones)
- Knowledge graph entities → Plane labels/tags
- Result: Plane becomes live mirror of Supabase data

**Phase 2: Activation** → Populate ventures, create templates
- Bulk-create 712 venture projects (with hierarchy)
- Create standard cycles (weekly, monthly, quarterly)
- Create views (by status, runway, risk, sector)
- Result: Plane becomes operational hub

**Phase 3: Autonomy** → Agents manage ventures through Plane
- Agents read Plane to understand venture state
- Agents update Plane tasks/milestones as work completes
- Agents trigger Slack notifications from Plane webhooks
- Result: Plane is the operational interface for autonomous systems

---

### Item 2: Folder Structure Supporting Smooth Phases

**Key Principle**: Each phase builds on previous; folder structure reflects progression

```
/PLANE/
├── 00_FOUNDATION/          ← Phase 0: Research & Design
│   ├── PLANE-ARCHITECTURE.md
│   ├── PLANE-API-SPEC.md
│   ├── VENTURE-DATA-MODEL.md
│   └── INTEGRATION-DIAGRAM.md
│
├── 01_SCHEMAS/             ← Phase 1: Data Model Design
│   ├── venture-workspace-structure.json
│   ├── venture-custom-fields.json
│   ├── venture-lifecycle-stages.json
│   └── knowledge-graph-mapping.json
│
├── 02_INTEGRATION/         ← Phase 1: Sync Scripts
│   ├── sync-supabase-ventures.py
│   ├── sync-plane-status.py
│   ├── knowledge-graph-tagger.py
│   └── webhook-handlers.py
│
├── 03_TEMPLATES/           ← Phase 2: Venture Templates
│   ├── venture-project-template.md
│   ├── venture-onboarding-checklist.md
│   └── milestone-roadmap-template.md
│
├── 04_AUTOMATION/          ← Phase 3: Workflows & Agents
│   ├── slack-webhook-handler.py
│   ├── github-sync.py
│   ├── obsidian-export.py
│   └── venture-agent.md
│
├── 05_SCRIPTS/             ← Phase 2-3: Execution
│   ├── bulk-create-ventures.py
│   ├── backfill-custom-fields.py
│   └── validate-plane-setup.py
│
├── 06_DOCS/                ← All Phases: Documentation
│   ├── VENTURE-LIFECYCLE.md
│   ├── AUTOMATION-FLOWS.md
│   ├── SETUP-CHECKLIST.md
│   └── TROUBLESHOOTING.md
│
└── 07_DASHBOARDS/          ← Phase 3: Live Views
    ├── venture-health-dashboard.md
    ├── sector-summary-dashboard.md
    └── obsidian-export.json
```

**Flow**: Phase 0 outputs → 00_FOUNDATION/, Phase 1 → 01_SCHEMAS/ + 02_INTEGRATION/, Phase 2 → 03_TEMPLATES/, Phase 3 → 04_AUTOMATION/ + 07_DASHBOARDS/

---

### Item 3: How Plane Connects to Existing Systems

```
┌──────────────────────────────────────────┐
│        PLANE (Central Hub)               │
│  Projects, Issues, Cycles, Custom Fields │
└──────────┬───────────────────────────────┘
           │
    ┌──────┴──────────┬──────────────────┐
    │                 │                  │
    ▼                 ▼                  ▼
 SUPABASE      KNOWLEDGE GRAPH       GITHUB
 (Ventures)    (Relationships)       (Repos)
 Bi-directional Sync via Tags        Webhook Links
    │                 │                  │
    └──────────┬──────┴──────────────────┘
               │
    ┌──────────┴──────────┬───────────────┐
    │                     │               │
    ▼                     ▼               ▼
 OBSIDIAN           SLACK          AGENTS
 (Dashboard)   (Notifications)    (Autonomy)
```

| System | Sync | What | Frequency |
|--------|------|------|-----------|
| **Supabase** | Bi-dir | Ventures ↔ Projects | Real-time |
| **Knowledge Graph** | Map | Entities → Labels | Daily |
| **GitHub** | Link | Repos ↔ Issues | Webhook |
| **Obsidian** | Export | Plane → Dataview | Hourly |
| **Slack** | Push | Status → Notifications | Webhook |

---

### Item 4: Data Model & Relationships (Reducing Confusion)

**Problem**: 712 ventures scattered; no unified view

**Solution**: Plane hierarchy with clear relationships

```
WORKSPACE: Worldwidebro Holdings
│
├─ PROJECT: Tesla Battery (venture)
│  ├─ Custom Fields:
│  │  ├─ Sector: Energy
│  │  ├─ Stage: MVP
│  │  ├─ MRR: $15,000
│  │  ├─ Runway: 6 months
│  │  ├─ Contact: john@example.com
│  │  └─ Repo: github.com/worldwidebro/tesla-battery
│  │
│  ├─ MODULE: Product Development
│  │  ├─ ISSUE: Design battery system
│  │  └─ ISSUE: Test charge protocol
│  │
│  ├─ CYCLE: Q2 2026
│  │  ├─ Target MRR: $25K
│  │  └─ Key Results: 3 pilot customers
│  │
│  └─ VIEWS:
│     ├─ Health Dashboard (metrics)
│     ├─ Roadmap (timeline)
│     └─ Risk Register (mitigations)
│
└─ PROJECT: HRMS (venture)
   └─ (Same structure)
```

**Key Decisions**:

1. **Venture as Plane PROJECT** (full project structure)
2. **Work as ISSUES** (individual tasks linked to venture)
3. **Cycles = Planning Horizons** (weekly/monthly/quarterly)
4. **Custom Fields = Metadata** (MRR, runway, stage, sector, contact, repo)
5. **Labels = Knowledge Graph Tags** (relationships visible)
6. **Views = Role-Based Dashboards** (founder, investor, operator perspectives)

---

## Critical Use Cases (Priority Order)

### Must Work First

1. **New Venture Onboarding** (5 min end-to-end)
   - Supabase → Plane project → Slack notification → Obsidian dashboard

2. **Weekly Status Updates** (automated)
   - MRR + runway + blockers updated once → synced everywhere

3. **Risk Detection** (proactive)
   - Runway <3mo or MRR declining → auto-alert team

4. **Dependency Mapping** (cross-venture)
   - Knowledge graph shows what blocks what

5. **Investor Visibility** (metrics at a glance)
   - Dashboard: all 712 ventures, filters by sector/runway/stage

---

## What We Know vs Need to Know

### ✅ What We Know
- 712 ventures in Supabase (sectors, metrics, risks, contacts)
- Knowledge graph live with 17 entity types
- 260+ GitHub repos linkable
- Slack integration ready
- Agents operational
- Obsidian dashboard syncing

### ❓ What We Need (User Input)

1. **Plane Deployment**: Self-hosted or cloud?
2. **Hierarchy**: Teams by sector, or flat 712 projects?
3. **Priority Use Cases**: Which 3-5 MUST work first?
4. **Sync Frequency**: Real-time or acceptable latency?
5. **Metrics Required**: Which are mandatory vs optional?

---

## Implementation Strategy

### Parallel Blockers (Days 8+)

- **Thread A**: Data audit (3-4 days)
- **Thread B**: Plane architecture (3-4 days)
- **Thread C**: Integration scripts (5-7 days)
- **Thread D**: Automation wiring (5-7 days)

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Single source of truth | All 712 ventures in Plane |
| Sync accuracy | 100% field sync |
| Update latency | <5 min Supabase → Plane |
| Operational velocity | New venture <5 min |
| Investor visibility | Dashboard loads <2s |

---

## Errors Encountered

| Error | Attempt | Resolution |
|-------|---------|------------|
| (none yet) | — | — |

---

## Blockers

| Issue | Resolution | Critical? |
|-------|-----------|-----------|
| Plane deployment | Confirm self-hosted vs cloud | YES |
| Venture hierarchy | Confirm teams vs flat | YES |
| Critical use cases | Prioritize 3-5 musts | YES |
| Supabase webhooks | Test reliability | MEDIUM |

---

## Next Actions

1. **User clarifications** (blocking Phase 0):
   - Plane: self-hosted or cloud?
   - Hierarchy: teams or flat?
   - Critical use cases: which 3-5?

2. **Phase 0 execution** (after clarifications):
   - Audit Plane codebase + API
   - Inventory all 712 ventures
   - Create data model diagram
   - List integration points
