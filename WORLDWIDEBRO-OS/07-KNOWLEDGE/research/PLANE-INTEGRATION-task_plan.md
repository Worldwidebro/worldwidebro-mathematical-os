# Task Plan: Plane as 712-Venture Company Brain

**Goal**: Transform Plane into the centralized organizational system that unifies 712 ventures, connects all external systems, and reduces operational confusion through structured workflows, templates, and real-time synchronization.

**Status**: INITIATING 2026-06-04

**Owner**: Worldwidebro (Chief Orchestrator)

---

## Executive Summary

**Current Problem**: 712 ventures scattered across multiple systems (Supabase, GitHub, Obsidian, Slack, knowledge graph, manual tracking). No single source of truth for venture status, dependencies, priorities, or execution paths.

**Target State**: 
- Plane as the operational center (workspace per venture or team-based organization)
- Real-time sync with Supabase (entities ↔ Plane tasks/projects)
- Knowledge graph integration (relationships visible in Plane)
- Slack automation (status updates, blockers, metrics)
- Obsidian dashboard connected to live Plane data
- Agent autonomy (Claude agents manage ventures, update Plane)

**Completion Target**: 30 days (Phase 0-3)

---

## Phases Overview

| Phase | Duration | Objective | Status |
|-------|----------|-----------|--------|
| **0: Foundation & Analysis** | 3-4 days | Understand Plane architecture, map existing system state, design integration points | `queued` |
| **1: Data Model & Integration Layer** | 5-7 days | Design venture data model, build Supabase ↔ Plane sync, create template structure | `queued` |
| **2: Venture Workspace Setup** | 7-10 days | Create venture templates, populate initial ventures, build automation hooks | `queued` |
| **3: Activation & Automation** | 7-10 days | Wire Slack/GitHub/Obsidian, enable agent management, test end-to-end flows | `queued` |
| **TOTAL** | **~30 days** | **Plane operational as company brain** | — |

---

## Phase 0: Foundation & Analysis

**Objective**: Understand Plane's architecture, inventory existing systems, design integration strategy

**Status**: `queued`

**Subtasks**:
- [ ] Clone/fork Plane repository, audit codebase architecture
- [ ] Document Plane's data model (projects, workspaces, issues, modules, cycles, views)
- [ ] Inventory current 712-venture state (Supabase entities, GitHub repos, contact count)
- [ ] Map existing system dependencies (knowledge graph → Obsidian → Slack → agents)
- [ ] Design venture data model for Plane (how do ventures map to Plane entities?)
- [ ] Identify 3-5 critical use cases (what MUST work first?)
- [ ] Create integration architecture diagram (Plane ↔ Supabase ↔ Knowledge Graph ↔ Slack)
- [ ] List all APIs/webhooks needed (Plane API, Supabase webhooks, GitHub webhooks, Slack)
- [ ] Create Phase 0 findings document

**Completion Target**: 3-4 days

**Deliverables**:
- `PLANE-INTEGRATION-findings.md` (system analysis, data model design, use cases)
- `PLANE-ARCHITECTURE-DIAGRAM.md` (visual integration flow)
- `PLANE-API-REQUIREMENTS.md` (what Plane APIs/webhooks needed)
- `PLANE-VENTURE-DATA-MODEL.md` (how ventures map to Plane)

**Critical Questions**:
- [ ] Plane deployment: self-hosted vs cloud?
- [ ] Workspace structure: 1 workspace with 712 projects, or team-based hierarchy?
- [ ] Does Plane API support bulk operations at 712-venture scale?
- [ ] What's the venture hierarchy (sector → venture → product → task)?

---

## Phase 1: Data Model & Integration Layer

**Objective**: Design venture taxonomy, build sync infrastructure, create reusable templates

**Status**: `queued`

**Subtasks**:
- [ ] Finalize venture data model (decisions on Plane project structure)
- [ ] Design Supabase → Plane sync schema (which entities, which fields)
- [ ] Create Plane venture template (project structure, custom fields, cycles, views)
- [ ] Build sync script: Supabase ventures → Plane projects
- [ ] Build sync script: Supabase metrics/risks → Plane custom fields
- [ ] Build sync script: Plane task status → Supabase (reverse sync)
- [ ] Design knowledge graph sync (graph entities → Plane labels/tags)
- [ ] Create venture workspace hierarchy (teams, projects, issues)
- [ ] Test sync with 50-venture pilot
- [ ] Document sync automation triggers

**Completion Target**: 5-7 days

**Deliverables**:
- `/PLANE/INTEGRATION/sync-supabase-ventures.py`
- `/PLANE/INTEGRATION/sync-plane-status.py`
- `/PLANE/INTEGRATION/knowledge-graph-tagger.py`
- `/PLANE/TEMPLATES/venture-project-template.md`
- `/PLANE/SCHEMA/venture-custom-fields.json`

---

## Phase 2: Venture Workspace Setup

**Objective**: Populate ventures into Plane, create standardized templates, establish baseline automation

**Status**: `queued`

**Subtasks**:
- [ ] Create Plane workspaces structure
- [ ] Bulk-create venture projects (initial batch of 50-100 ventures)
- [ ] Populate custom fields (MRR, runway, sector, contact, repo links)
- [ ] Create standard cycles (weekly → monthly → quarterly)
- [ ] Create standard views (by status, by sector, by risk level, by runway)
- [ ] Build venture onboarding template
- [ ] Create venture archive/pause workflows
- [ ] Design milestone templates (idea → validation → MVP → growth → exit)
- [ ] Test bulk operations (add 712 ventures in batches)

**Completion Target**: 7-10 days

**Deliverables**:
- `/PLANE/TEMPLATES/venture-workspace-structure.md`
- `/PLANE/TEMPLATES/venture-onboarding-checklist.md`
- `/PLANE/SCRIPTS/bulk-create-ventures.py`
- `/PLANE/DOCS/VENTURE-LIFECYCLE.md`

---

## Phase 3: Activation & Automation

**Objective**: Wire all external systems, enable agent autonomy, achieve real-time operational visibility

**Status**: `queued`

**Subtasks**:
- [ ] Build Slack integration: venture status updates → Slack channels
- [ ] Build GitHub integration: venture repos → Plane issues/PRs
- [ ] Build Obsidian sync: Plane projects → Obsidian dataview dashboard
- [ ] Build agent hooks: Claude agents can read/write Plane tasks
- [ ] Create Slack slash commands (/venture-status, /add-blocker, /update-metric)
- [ ] Wire n8n/Make for workflow automation
- [ ] Build metrics automation (MRR, runway, risk → Plane → Slack)
- [ ] Create venture health dashboard
- [ ] Set up automated alerts
- [ ] Test end-to-end flow: new venture → Supabase → Plane → Slack → Obsidian

**Completion Target**: 7-10 days

**Deliverables**:
- `/PLANE/INTEGRATIONS/slack-webhook-handler.py`
- `/PLANE/INTEGRATIONS/github-sync.py`
- `/PLANE/INTEGRATIONS/obsidian-export.py`
- `/PLANE/AGENTS/venture-agent.md`
- `/PLANE/DOCS/AUTOMATION-FLOWS.md`

---

## Target Folder Structure

```
/Users/acebless/Documents/PLANE/
├── 00_FOUNDATION/
│   ├── PLANE-ARCHITECTURE.md
│   ├── PLANE-API-SPEC.md
│   ├── VENTURE-DATA-MODEL.md
│   └── INTEGRATION-DIAGRAM.md
├── 01_SCHEMAS/
│   ├── venture-workspace-structure.json
│   ├── venture-custom-fields.json
│   └── venture-lifecycle-stages.json
├── 02_TEMPLATES/
│   ├── venture-project-template.md
│   ├── venture-onboarding-checklist.md
│   └── milestone-roadmap-template.md
├── 03_INTEGRATION/
│   ├── sync-supabase-ventures.py
│   ├── sync-plane-status.py
│   └── knowledge-graph-tagger.py
├── 04_AUTOMATION/
│   ├── slack-webhook-handler.py
│   ├── github-sync.py
│   └── venture-agent.md
├── 05_DOCS/
│   ├── VENTURE-LIFECYCLE.md
│   ├── AUTOMATION-FLOWS.md
│   └── SETUP-CHECKLIST.md
└── 06_DASHBOARDS/
    └── venture-health-dashboard.md
```

---

## Parallel Execution (Days 8+)

- **Thread A**: Bulk venture creation (Phase 2)
- **Thread B**: Automation wiring (Phase 3)
- **Thread C**: Documentation & testing

---

## Success Criteria

- [ ] Plane deployed and accessible
- [ ] All 712 ventures syncable to Plane projects
- [ ] Supabase ↔ Plane bi-directional sync working
- [ ] Knowledge graph visible in Plane (tags/relationships)
- [ ] Slack receives real-time updates
- [ ] Obsidian shows live Plane data
- [ ] Agents can read/write Plane tasks
- [ ] 0 manual venture updates (all automated)
- [ ] New venture creation <5 minutes end-to-end

---

## Errors Encountered

| Error | Attempt | Resolution |
|-------|---------|------------|
| (none yet) | — | — |

---

## Next Immediate Action

**Start Phase 0**: Audit Plane codebase, document API, inventory 712-venture state, create findings.md with data model recommendations
