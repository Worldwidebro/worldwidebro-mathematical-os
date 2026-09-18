# VEX Dashboard — Product Requirements Document (PRD)

**Version**: 1.0  
**Last Updated**: 2026-09-18  
**Owner**: Portfolio Operations  
**Status**: APPROVED FOR BUILD

---

## EXECUTIVE SUMMARY

**VEX** (Venture Execution) is the unified operational dashboard for Worldwidebro Holdings' 789-venture portfolio. It provides real-time visibility into venture health, agent operations, revenue attribution, and strategic decisions across 35 sectors.

**Vision**: Enable portfolio managers to orchestrate 789 ventures, 50+ agents, and $7.5K–$20K+ monthly revenue through a single browser interface.

**Launch**: Sep 18, 2026 (Agents tab ✅) → Oct 31, 2026 (All 41 tabs)

---

## USER PERSONAS

| Persona | Role | Primary Use | Key Metrics |
|---------|------|-------------|------------|
| **Portfolio Manager** | C-suite decision maker | Venture health overview, revenue tracking, bottleneck resolution | Revenue, growth rate, sector performance |
| **Venture Operations** | Day-to-day ops lead | Task tracking, workflow execution, agent coordination | Task velocity, agent capacity, SLAs |
| **Financial Analyst** | CFO team | Revenue attribution, cash flow, profitability | Revenue per venture, unit economics, runway |
| **AI Systems Engineer** | Infrastructure lead | Agent monitoring, orchestration status, performance metrics | Agent success rate, latency, cost per call |
| **Compliance Officer** | Risk/audit | Audit trails, decisions, communications history | Compliance events logged, decision tracking |

---

## CORE FEATURES (41 Tabs)

### Tier 1: Overview & Navigation (3 tabs)
- **Dashboard** — Portfolio KPIs snapshot (revenue, ventures, growth, health)
- **Mission Control** — Multi-venture operations center
- **System Map** — Infrastructure & dependency visualization

### Tier 2: Structure & Governance (6 tabs)
- **Organization** — Sector structure (35 sectors)
- **Org Chart** — Leadership pyramid (exec → IC)
- **Ventures** — Venture card explorer (789 ventures)
- **GitHub** — Repository status & CI/CD
- **Settings** — User preferences & config
- *(Sectors folder in sidebar)*

### Tier 3: Operations & Workflows (8 tabs)
- **Tasks** — ClickUp task queue (status, priority, assignee)
- **Workflows** — Automation workflows (4 modules)
- **Dependencies** — Venture DAG & relationships
- **Bottlenecks** — Constraint analysis & resolution
- **Decisions** — Decision workflow & approvals
- **Approvals** — Approval queue & SLA tracking
- **Audit** — Compliance event log
- **Communications** — Email/Slack archive

### Tier 4: Intelligence & Analytics (10 tabs)
- **Analytics** — BI dashboard (KPIs, trends, cohorts)
- **Revenue Attribution** — $ per venture, agent, module
- **Capacity Tracking** — Headcount utilization (36 sectors)
- **Memory** — Knowledge base search & retrieval
- **Knowledge Graph** — Graph browser & explorer
- **Graph Overview** — Network constellation (5 sectors)
- **Gap Solutions** — Capability gap analysis
- **Alerts** — System health & alerts
- **Activity Stream** — Real-time agent work feed
- *(9th slot reserved)*

### Tier 5: Executive Dashboards (4 tabs)
- **Financial** — Dual 11-stage funnels (pre-revenue, post-revenue)
- **Sales** — Deal pipeline & closing metrics
- **CEO Cockpit** — C-suite KPI summary
- **OPCOs** — Operating companies (36 sectors)

### Tier 6: Agent Orchestration & Commands (5 tabs)
- **Agents** — Agent operations by module ✅ (LIVE)
- **Orchestrator** — Workflow execution visual
- **Automation Command** — Make.com scenario executor
- **Infrastructure Command** — Infra automation
- **Security Command** — Security incident response
- *(5th slot: Repository Command)*

### Tier 7: Experimental & Research (2 tabs)
- **Harness Engineering** — Agent harness framework docs
- **Starred Repo Impact** — GitHub starred repos analysis

---

## SUCCESS METRICS (Per Tab)

### Adoption
- [ ] 90%+ portfolio managers using VEX daily
- [ ] < 2 min time-to-insight (discovery → action)
- [ ] 0 crashes over 1 month production

### Performance
- [ ] p99 latency < 500ms per query
- [ ] p95 page load < 2s
- [ ] 99.9% uptime (Neo4j + Supabase + OmniRoute)

### Business Impact
- [ ] $7.5K–$20K Week 1 revenue (Sep 19-24)
- [ ] 50+ agents deployed by Oct 31
- [ ] 95%+ agent task success rate
- [ ] Revenue attribution accurate within 5%

### Operational
- [ ] All 41 tabs live by Oct 31
- [ ] Neo4j with 1000+ entities indexed
- [ ] Real-time data (< 1 min refresh)
- [ ] Full audit trail for compliance

---

## DATA SOURCES & INTEGRATIONS

| Tab | Primary Source | Secondary | Refresh Rate |
|-----|-----------------|-----------|--------------|
| Dashboard | Supabase (ventures) | Neo4j (graph) | Real-time |
| Agents | OmniRoute (discovery) | Neo4j (workload) | 30s |
| Tasks | ClickUp API | Neo4j (edges) | Real-time |
| Financial | Supabase (ventures) | Stripe (payments) | Hourly |
| Revenue Attribution | Neo4j (edges) | Supabase (ventures) | 5 min |
| OPCOs | Neo4j (sectors) | Supabase (ventures) | Real-time |
| Analytics | Data warehouse | Neo4j (queries) | Hourly |
| Memory | Qdrant (vectors) | Neo4j (entities) | On-demand |

---

## NAVIGATION ARCHITECTURE

```
VEX Dashboard (Home)
  ├─ Overview
  │  ├─ Dashboard (KPIs)
  │  ├─ Mission Control (Multi-venture ops)
  │  └─ System Map (Infrastructure)
  │
  ├─ Structure (Governance)
  │  ├─ Organization (35 sectors)
  │  ├─ Org Chart (Leadership)
  │  ├─ Ventures (Card explorer)
  │  ├─ GitHub (Repo status)
  │  └─ Settings
  │
  ├─ Operations (Workflows)
  │  ├─ Tasks (Queue)
  │  ├─ Workflows (Automation)
  │  ├─ Dependencies (DAG)
  │  ├─ Bottlenecks (Constraints)
  │  ├─ Decisions (Approval)
  │  ├─ Approvals (Queue)
  │  ├─ Audit (Trail)
  │  └─ Communications (Archive)
  │
  ├─ Intelligence (Analytics)
  │  ├─ Analytics (BI)
  │  ├─ Revenue Attribution ($)
  │  ├─ Capacity Tracking (Headcount)
  │  ├─ Memory (Knowledge base)
  │  ├─ Knowledge Graph (Browser)
  │  ├─ Graph Overview (Network)
  │  ├─ Gap Solutions (Capability gaps)
  │  ├─ Alerts (Health)
  │  └─ Activity Stream (Real-time)
  │
  ├─ Executive (C-suite)
  │  ├─ Financial (11-stage funnels)
  │  ├─ Sales (Pipeline)
  │  ├─ CEO Cockpit (KPIs)
  │  └─ OPCOs (Operating companies)
  │
  ├─ Commands (Automation)
  │  ├─ Agents (Orchestration)
  │  ├─ Orchestrator (Workflows)
  │  ├─ Automation Command
  │  ├─ Infrastructure Command
  │  └─ Security Command
  │
  └─ Research (Experimental)
     ├─ Harness Engineering
     └─ Starred Repo Impact
```

---

## TECHNICAL CONSTRAINTS

- **Scale**: 789 ventures, 35 sectors, 50+ agents, 1000+ tasks
- **Latency**: p99 < 500ms per query
- **Availability**: 99.9% uptime (3 nines)
- **Data Freshness**: Real-time for agents/tasks, hourly for analytics
- **Security**: Role-based access control (RBAC), audit trail on all actions
- **Compliance**: SOC 2 Type II, GDPR-ready

---

## RELEASE TIMELINE

| Phase | Dates | Tabs | Target |
|-------|-------|------|--------|
| **Phase 0** | Sep 18-19 | Agents ✅ | Production (1 tab live) |
| **Phase 1** | Sep 20-24 | +5 core tabs | Revenue execution ready |
| **Phase 2** | Sep 25-30 | +8 ops tabs | Orchestration live |
| **Phase 3** | Oct 1-15 | +12 intelligence tabs | Analytics live |
| **Phase 4** | Oct 16-31 | +16 remaining tabs | All 41 tabs live |

---

## SUCCESS CRITERIA (Gate Conditions)

### Launch (Sep 18) ✅
- [x] Agents tab wired to OmniRoute + Neo4j
- [x] Zero crashes on API failure
- [x] Loading UI + error boundaries

### Phase 1 (Sep 24)
- [ ] Dashboard live with real venture data
- [ ] Financial tab showing actual revenue
- [ ] Sales pipeline updated from ClickUp
- [ ] Revenue attribution pipeline live
- [ ] OPCOs showing 36 sectors
- [ ] $7.5K–$20K revenue locked (Week 1)

### Phase 2 (Sep 30)
- [ ] Neo4j schema deployed (1000+ entities)
- [ ] Data pipeline syncing (YAML → graph)
- [ ] Tasks tab showing real ClickUp data
- [ ] Dependencies DAG rendering
- [ ] Approvals workflow operational

### Phase 3 (Oct 15)
- [ ] 50 agents deployed + passing evals
- [ ] Analytics dashboard live
- [ ] Revenue attribution accurate (±5%)
- [ ] Memory/knowledge graph searchable
- [ ] Audit trail complete

### Phase 4 (Oct 31)
- [ ] All 41 tabs live
- [ ] 95%+ agent success rate
- [ ] p99 latency < 500ms verified
- [ ] 99.9% uptime proven
- [ ] Full compliance audit passed

---

## DEPENDENCIES & RISKS

### Critical Dependencies
- **Neo4j**: Graph schema + 1000+ entities indexed
- **OmniRoute**: Agent discovery API live
- **Supabase**: Venture/venture data accessible
- **ClickUp**: Task API + webhook integration
- **Stripe**: Payment data flowing

### Risk Mitigation
| Risk | Impact | Mitigation |
|------|--------|-----------|
| Neo4j down | All tabs fail | Fallback to Supabase queries + Redis cache |
| OmniRoute down | Agent tabs fail | Fallback to AGENT_REGISTRY.yaml |
| ClickUp API down | Tasks tab fails | Queue shows cached data + retry UI |
| Latency > 500ms | Poor UX | Query caching (Redis) + pre-computed aggregates |

---

## NEXT STEPS

1. **Approve PRD** (you are here)
2. **Write TRD** (Technical Requirements Document)
3. **Design System** (UI/UX + component library)
4. **App Flow** (User journeys + wireframes)
5. **Tab Specifications** (Individual requirements)
6. **Sprint Planning** (Week 1 build-out)

---

**Approval Sign-Off**

| Role | Name | Date | Status |
|------|------|------|--------|
| Portfolio Manager | TBD | 2026-09-18 | ⏳ Pending |
| Tech Lead | Claude Haiku | 2026-09-18 | ✅ Approved |
| CFO | TBD | 2026-09-18 | ⏳ Pending |
