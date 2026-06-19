# System Architecture: Plane as Company Brain

**Status**: Phase 0 Foundation

**Created**: 2026-06-04

---

## The Problem → Solution

### TODAY (Chaos)
712 ventures scattered across 5 systems with no single source of truth.

**Result**: Operators, founders, investors each use different systems

**Outcome**: No unified view of venture health, dependencies, priorities

### AFTER PLANE (Organization)
PLANE = Central Hub with real-time sync to all other systems.

**Result**: Everyone uses ONE system with synchronized data everywhere

**Outcome**: Real-time visibility, automated updates, agent autonomy

---

## How Items 1-4 Align with Plane

### 1. PHASES (Creation Path)

**Phase 0: Foundation**
- Understand Plane architecture
- Inventory 712 ventures (current state)
- Map existing system dependencies
- Design venture → Plane data model
- Output: Data model diagram + API requirements

**Phase 1: Integration Layer**
- Build Supabase → Plane sync (ventures as projects)
- Build Plane → Supabase reverse sync
- Build Knowledge Graph → Plane labels
- Build webhook handlers
- Output: Sync scripts + tested with 50-venture pilot

**Phase 2: Activation**
- Bulk-create all 712 venture projects in Plane
- Populate custom fields (metrics, contacts, repos)
- Create standard cycles (weekly, monthly, quarterly)
- Create standard views (status, risk, runway, sector)
- Output: All 712 ventures live in Plane

**Phase 3: Autonomy**
- Build Slack integration (status → notifications)
- Build GitHub integration (repos ↔ Plane issues)
- Build Obsidian export (Plane → live dashboard)
- Build agent interface (agents read/write Plane)
- Output: All systems synchronized, agents autonomous

---

### 2. FOLDER STRUCTURE (Supporting Phases)

```
/PLANE/
├─ 00_FOUNDATION/         Phase 0 Outputs (Analysis & Design)
├─ 01_SCHEMAS/            Phase 1 Designs (Data Models)
├─ 02_INTEGRATION/        Phase 1 Scripts (Sync Infrastructure)
├─ 03_TEMPLATES/          Phase 2 Templates (Venture Structure)
├─ 04_AUTOMATION/         Phase 3 Workflows (External Wiring)
├─ 05_SCRIPTS/            Phase 2-3 Operations (Bulk Import)
├─ 06_DOCS/               All Phases (Reference)
└─ 07_DASHBOARDS/         Phase 3 Views (Live Dashboards)
```

Flow: Phase 0 → 00_FOUNDATION, Phase 1 → 01_SCHEMAS + 02_INTEGRATION, Phase 2 → 03_TEMPLATES, Phase 3 → 04_AUTOMATION + 07_DASHBOARDS

---

### 3. SYSTEM CONNECTIONS (How Plane Connects Everything)

```
                      PLANE (Central Hub)
                    [712 Projects + Metrics]
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
        SUPABASE      KNOWLEDGE GRAPH         GITHUB
        (Ventures)      (Relationships)       (Repos)
         ↔ Bi-dir    →    Mapping   ←       ↔ Links
            │                 │                 │
            └─────────────────┼─────────────────┘
                              │
                ┌─────────────┴──────────────┐
                │                            │
              SLACK                      OBSIDIAN
            (Notifications)            (Dashboard)
                │                            │
                └─────────────┬──────────────┘
                              │
                        AGENTS (Claude)
                    [Autonomous Management]
```

| System | Sync | Frequency |
|--------|------|-----------|
| Supabase | Bi-directional | Real-time webhooks |
| Knowledge Graph | Map to labels | Daily sync |
| GitHub | Link repos | Webhook |
| Slack | Push notifications | Webhook |
| Obsidian | Export data | Hourly sync |

---

### 4. DATA MODEL (Reducing Confusion)

```
ONE WORKSPACE: All 712 Ventures
│
├─ PROJECT: Venture A
│  ├─ Custom Fields: Sector, Stage, MRR, Runway, Contact, Repo, Risk Level
│  ├─ Module: Product Dev (issues with tasks)
│  ├─ Module: Go-to-Market (issues with tasks)
│  ├─ Cycles: Weekly, Monthly, Quarterly (OKR tracking)
│  └─ Views: Health Dashboard, Roadmap, Risk Register, Metrics Tracker
│
├─ PROJECT: Venture B
│  └─ (Same structure)
│
└─ SHARED VIEWS (Visible to All):
   ├─ Portfolio Dashboard (Total MRR, Runway, Risk Count)
   ├─ Risk Heatmap (High/Medium/Low by runway vs burn rate)
   ├─ Dependency Graph (What blocks what)
   └─ Sector Summary (Metrics by sector)
```

**Key Design**:
1. Venture = Plane PROJECT (not issue)
2. Work = ISSUES (individual tasks)
3. Cycles = Planning Horizons (weekly/monthly/quarterly)
4. Custom Fields = Metadata (searchable, filterable)
5. Labels = Knowledge Graph Tags (relationships)
6. Views = Role-Based Dashboards (founder/investor/operator)

---

## How Confusion → Organization

| Question | Today | With Plane |
|----------|-------|-----------|
| Status of venture X? | Check Supabase → GitHub → Slack | Open Plane project |
| Is venture Y at risk? | Manual runway check | Plane auto-flags + Slack alert |
| Which ventures block Z? | Query knowledge graph | Plane dependency view |
| Total MRR? | SQL query | Plane portfolio dashboard |
| Who's working on what? | Check GitHub + Slack | Plane issues show assignments |
| Quarterly goals? | Static documents | Plane cycles with OKR tracking |
| Can agents run autonomously? | Must query multiple systems | Agents read/write Plane API |

---

## Integration Architecture

**Sync Flow**:
1. **Supabase → Plane**: Ventures created in Supabase auto-create Plane projects
2. **Plane → Supabase**: Status updates in Plane cascade back to Supabase
3. **Supabase → Obsidian**: Knowledge graph syncs to Obsidian dashboard daily
4. **Plane → Slack**: Metrics changes trigger Slack notifications (webhooks)
5. **GitHub ↔ Plane**: Venture repos link to Plane projects (issues ↔ PRs)
6. **Plane → Agents**: Claude agents read Plane API to understand venture state
7. **Agents → Plane**: Claude agents write task updates, create issues, manage status

---

## Success Definition

**Plane is the Company Brain when**:
- ✅ Single source of truth (no more checking multiple systems)
- ✅ Real-time sync (update once, cascade everywhere)
- ✅ Role-based views (founder/investor/operator each see what matters)
- ✅ Agent autonomy (agents manage ventures without human intervention)
- ✅ New venture <5 min (from creation to live operational status)
- ✅ All 712 ventures visible in one dashboard
- ✅ Risk detection automated (no manual runway checks)
- ✅ Dependencies tracked (no surprise blockers)

---

## Next: Phase 0 Execution

**What we'll do**:
1. Audit Plane codebase (architecture, API)
2. Inventory 712 ventures (gaps, metrics, contacts)
3. Design data model (teams vs flat)
4. Create integration requirements

**User input needed before Phase 1**:
1. Plane deployment: Self-hosted or cloud?
2. Venture hierarchy: Teams or flat?
3. Critical use cases: Which 3-5 first?

**Timeline**: 3-4 days
