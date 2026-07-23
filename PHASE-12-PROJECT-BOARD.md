---
title: Phase 12 — IZA OS Cores + vex Integration + Monetization + Playbooks
date: 2026-07-23
status: In Progress
effort_hours: 240-320
---

# Phase 12 Project Board

**Goal:** All 7 OS cores deployed, vex routing live, monetization tracking active, 90-day playbooks drafted & scheduled.

**Status:** 5% (stubs created, code verification in progress)

---

## Work Breakdown by Stream

### Stream 1: CODE INVENTORY & CORE DEPLOYMENT (Blocker)
**Owner:** Backend Architect + DevOps Engineer  
**Duration:** 40-60 hours  
**Dependency:** None (blocks all others)

| Task | Assignee | Effort | Status | Notes |
|------|----------|--------|--------|-------|
| **T12.1a** Verify iza-os-construction-core has app code | Backend Architect | 4h | ⏳ Ready | Check GitHub, examine Vercel deploy history |
| **T12.1b** Verify logistics/realestate cores exist on GitHub | Backend Architect | 2h | ⏳ Ready | Search Worldwidebro org, check deployment history |
| **T12.1c** Extract Next.js template from iza-os-marketing-core | Backend Architect | 8h | ⏳ Blocked on 12.1a/b | Clone, document auth/data flow, create starter scaffold |
| **T12.1d** Stub 3 cores with minimal Next.js + README | Backend Architect | 6h | ✅ DONE | Created staffing/education/finance repos, pushed stubs |
| **T12.2a** Deploy cores to Vercel (4+ cores) | DevOps Engineer | 12h | ⏳ Blocked on 12.1c | Each core: new Vercel project, env vars, custom domain |
| **T12.2b** Wire auth middleware: opco_role → venture filter | Backend Architect | 12h | ⏳ Blocked on 12.1c | Supabase session, middleware.ts, RLS policies |
| **T12.2c** Test e2e: dashboard loads + filters by OPCO | QA/Test Automator | 6h | ⏳ Blocked on 12.2a | Playwright: login → venture query → UI render |

**Acceptance:** All 7 cores live on Vercel, auth working, data flowing. `[T12.1/T12.2 GREEN]`

---

### Stream 2: VEX ROUTING & INTEGRATION (Depends on Stream 1)
**Owner:** Frontend Developer + Full-Stack Architect  
**Duration:** 30-40 hours  
**Dependency:** Stream 1 (cores deployed)

| Task | Assignee | Effort | Status | Notes |
|------|----------|--------|--------|-------|
| **T12.3a** Update vex sectors.ts: add core_subdomain + dashboard_link | Frontend Developer | 4h | ⏳ Blocked on S1 | Map all 7 sectors → core subdomains |
| **T12.3b** Add "View Dashboard" CTA on sector heroes | Frontend Developer | 6h | ⏳ Blocked on S1 | Button/link on each sector page, styling |
| **T12.3c** Test e2e: vex click → core dashboard loads | QA/Test Automator | 6h | ⏳ Blocked on S1 | Playwright: click hero → navigate → auth → dashboard |
| **T12.3d** Verify routing across all 7 sectors | Full-Stack Architect | 4h | ⏳ Blocked on S1 | Smoke test each sector link, latency check |
| **T12.3e** Deploy vex to Vercel (if not live) | DevOps Engineer | 4h | ⏳ Pending | Confirm/re-deploy vex-hero-site |

**Acceptance:** Click any sector on vex → routed to core dashboard → auth succeeds → ventures filtered by OPCO. `[T12.3 GREEN]`

---

### Stream 3: MONETIZATION FRAMEWORK (Parallel to Stream 1/2)
**Owner:** Financial Analyst + Backend Architect  
**Duration:** 50-70 hours  
**Dependency:** None (can start immediately)

| Task | Assignee | Effort | Status | Notes |
|------|----------|--------|--------|-------|
| **T12.4a** Define revenue model per sector (7 models) | Financial Analyst | 12h | ⏳ Ready | Use con-001, miss-toys, hermes as comps; document pricing logic |
| **T12.4b** Calculate unit economics (CAC, LTV, payback) | Financial Analyst | 16h | ⏳ Ready | Spreadsheet per sector, sensitivity analysis, break-even |
| **T12.4c** Design KPI schema (Supabase tables + aggregates) | Backend Architect | 12h | ⏳ Ready | ventures_revenue, sector_metrics, kpi_snapshots, edge functions |
| **T12.4d** Create Supabase tables + RLS policies | Backend Architect | 8h | ⏳ Blocked on 12.4c | Schema, migrations, indexes, policies |
| **T12.4e** Build Grafana dashboards per sector | DevOps/Observability Engineer | 12h | ⏳ Blocked on 12.4d | MRR chart, churn gauge, runway forecast, alerts |
| **T12.4f** Wire Langfuse → Grafana for LLM cost tracking | Observability Engineer | 10h | ⏳ Blocked on 12.4e | Trace ingestion, cost attribution per venture |

**Acceptance:** Grafana shows live MRR/churn/runway for each sector. Manual entry for first 30 days (before automation). `[T12.4 GREEN]`

---

### Stream 4: EXECUTION PLAYBOOKS (Parallel, depends on Stream 3)
**Owner:** Product Manager + Sales/GTM Specialist  
**Duration:** 80-100 hours  
**Dependency:** Stream 3 (KPI framework defined)

| Task | Assignee | Effort | Status | Notes |
|------|----------|--------|--------|-------|
| **T12.5a** CON (Construction) 90-day playbook | Sales/GTM Specialist | 12h | ⏳ Ready | GC outreach script, pricing model, crew hiring, 30d revenue target |
| **T12.5b** STA (Staffing) 90-day playbook | Sales/GTM Specialist | 12h | ⏳ Ready | Contractor pipeline (LinkedIn/Indeed), matching logic, payroll, 10-placement target |
| **T12.5c** RE (Real Estate) 90-day playbook | Sales/GTM Specialist | 12h | ⏳ Ready | MLS integration, cold-call script, deal pricing, 5-deal target |
| **T12.5d** EDU (Education) 90-day playbook | Product Manager | 12h | ⏳ Ready | Curriculum launch (Azriel testbed?), cohort size, pricing, growth loop |
| **T12.5e** FIN (Finance) 90-day playbook | Sales/GTM Specialist | 12h | ⏳ Ready | Ledger schema, risk modeling, advisor onboarding, AUM target |
| **T12.5f** LOG (Logistics) 90-day playbook | Sales/GTM Specialist | 12h | ⏳ Ready | Carrier relationships, route optimization, shipment pricing, volume target |
| **T12.5g** MKT (Marketing) 90-day playbook | Product Manager | 14h | ⏳ Ready | Campaign template, multi-venture orchestration, budget, ROAS target |

**Acceptance:** 7 playbooks drafted, user-approved, handed off to sector teams for execution. `[T12.5 GREEN]`

---

### Stream 5: AUTOMATION & MONITORING (Depends on Streams 1-4)
**Owner:** DevOps/Observability Engineer + Backend Architect  
**Duration:** 30-40 hours  
**Dependency:** Streams 1-4 (all systems live)

| Task | Assignee | Effort | Status | Notes |
|------|----------|--------|--------|-------|
| **T12.6a** Create `/loop` job for nightly KPI collection | Backend Architect | 8h | ⏳ Blocked on S4 | Script: fetch ventures → calculate MRR/churn/runway → snapshot to Supabase |
| **T12.6b** Set alert thresholds (MRR decline, churn, runway) | Observability Engineer | 6h | ⏳ Blocked on S4 | Grafana alert rules, Slack/email notifications |
| **T12.6c** Deploy `/loop` + test for 3+ days | DevOps Engineer | 8h | ⏳ Blocked on 12.6a | Verify nightly runs, log inspection, fix any data gaps |
| **T12.6d** Document runbook: sector KPI interpretation | Product Manager | 6h | ⏳ Blocked on S4 | Guide: "When MRR drops 20%, do this…" |
| **T12.6e** Onboard sector teams to dashboards & playbooks | Product Manager | 6h | ⏳ Blocked on S5 | Training, access, usage metrics |

**Acceptance:** `/loop` running 3+ days without error. Grafana dashboards live. Sector teams can read + act on KPIs. `[T12.6 GREEN]`

---

## Dependency Graph

```
[Stream 1: Code & Deployment]
  ↓
  ├─→ [Stream 2: vex Routing] (requires deployed cores)
  │     ↓
  │     └─→ [Demo: vex → core dashboard] ✓ [GATE]
  │
  ├─→ [Stream 3: Monetization] (parallel, independent)
  │     ↓
  │     └─→ [Stream 4: Playbooks] (requires KPI schema)
  │           ↓
  │           └─→ [Stream 5: Automation] (requires live playbooks)
  │                 ↓
  │                 └─→ [Sector team handoff] ✓ [FINAL GATE]
```

---

## Effort Estimate by Role

| Role | Hours | Days | FTE* |
|------|-------|------|------|
| Backend Architect | 80 | 10 | 1.25 |
| Frontend Developer | 10 | 1.5 | 0.2 |
| DevOps/Observability Engineer | 40 | 5 | 0.625 |
| QA/Test Automator | 12 | 1.5 | 0.2 |
| Financial Analyst | 28 | 3.5 | 0.4 |
| Product Manager | 44 | 5.5 | 0.7 |
| Sales/GTM Specialist | 72 | 9 | 1.125 |
| Full-Stack Architect (review/integration) | 8 | 1 | 0.125 |
| **TOTAL** | **294** | **37** | **4.625** |

*FTE = Full-Time Equivalent (assumes 8-hour days)

---

## Team Composition (Recommended)

### Core Implementation Team (Weeks 1-2)
- 1x Backend Architect (Stream 1, 2b, 4c)
- 1x DevOps Engineer (Stream 1, 2a, 5c)
- 1x Frontend Developer (Stream 2, vex routing)
- 1x QA/Test Automator (Stream 2c, 3, end-to-end verification)

**Daily standup**: 15min, 10am (9am PT / 12pm ET)

### Monetization & Strategy Team (Weeks 1-3, parallel)
- 1x Financial Analyst (Stream 3a/b, 4)
- 1x Product Manager (Stream 4, playbook consolidation, 5d)
- 1x Sales/GTM Specialist (Stream 4, all 7 playbooks)

**Weekly sync**: Thursday 2pm, strategic review + playbook drafts

### Observability & Handoff Team (Weeks 2-4)
- 1x Observability Engineer (Stream 3e/f, 5b)
- 1x Backend Architect (Stream 5a)
- 1x Product Manager (Stream 5d/e, sector onboarding)

---

## Decision Gates (Blocking Next Work)

| Gate | Required By | Owner | Decision |
|------|------------|-------|----------|
| **12.1a/b** Do logistics/realestate cores have code? | Today | User | Yes → proceed | No → stub both |
| **12.4b** Unit economics data source | Before T12.4 start | Financial Analyst + User | Real comps (con-001, miss-toys) OR forecast |
| **12.5** Launch sequence | Before T12.5 start | Product Manager + User | Sequential per sector (30d apart) OR parallel all 7 |

---

## Milestones & Timeline

| Milestone | Target Date | Owner | Criteria |
|-----------|------------|-------|----------|
| **M1: Cores live** | 2026-07-28 (5d) | Backend Arch + DevOps | All 7 cores deployed to Vercel, auth working |
| **M2: vex routed** | 2026-07-31 (8d) | Frontend + QA | Click any sector → core dashboard loads |
| **M3: KPIs live** | 2026-08-04 (12d) | Financial Analyst + Obs Eng | Grafana dashboards show real data per sector |
| **M4: Playbooks drafted** | 2026-08-11 (19d) | GTM Specialist + PM | 7 playbooks approved, ready to execute |
| **M5: Automation live** | 2026-08-15 (23d) | Backend Arch + DevOps | `/loop` running 3+ days, sector teams trained |
| **GATE: Ship Phase 12** | 2026-08-18 (26d) | Product Manager | All streams GREEN, teams ready to execute |

---

## Risk Register

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|-----------|
| Cores have no deployable code (except marketing) | **CRITICAL** | Medium | Gate T12.1a/b immediately. Already stubbed 3 cores. |
| Supabase RLS too restrictive for filtering | High | Low | Test auth middleware early (Week 1). Have Neo4j fallback. |
| Sector teams refuse playbooks (prefer autonomy) | High | Medium | Involve GTM specialist in co-creation. User buy-in required. |
| Grafana dashboards slow with 700+ ventures | Medium | Low | Aggregate to sector/OPCO level, not venture detail. Optimize Week 2. |
| `/loop` job breaks mid-month | Medium | Medium | Run 3-day test first. Alert on failure. Manual fallback ready. |

---

## Success Criteria (Phase Complete)

- [ ] All 7 cores deployed to Vercel with live URLs
- [ ] vex routing wired: sector click → core dashboard (verified end-to-end)
- [ ] Monetization KPIs live in Grafana (MRR, churn, runway, LTV per sector)
- [ ] 90-day playbooks drafted + user-approved (7 total)
- [ ] `/loop` running nightly for 3+ days without error
- [ ] Sector teams trained + dashboards accessible
- [ ] **Timeline: Complete by 2026-08-18**

---

## Handoff to Execution Phase

Once Phase 12 gates PASS, each sector team receives:
1. Deployed OS core dashboard (their sector only, filtered by opco_role)
2. Approved 90-day playbook (with KPI targets)
3. Live Grafana dashboard (MRR, churn, runway tracking)
4. Nightly KPI snapshots (automated via `/loop`)

Sector teams then own execution: lead gen, onboarding, revenue tracking.
