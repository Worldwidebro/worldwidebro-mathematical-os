# ConstructionOS Frontend MVP

## Problem Statement

Construction contractors (electricians, plumbers, HVAC specialists) receive 10-20 leads per week but can only respond to 5-8 because estimates take 2-3 days to prepare manually. By the time an estimate is sent, leads go cold and convert at 40% instead of the achievable 70%. This delays revenue and wastes lead acquisition spend.

## Evidence

- **ACE Construction**: 15+ leads/week, can only handle 5-8 → $30-50K/month in lost revenue
- **Industry standard**: Estimates take 2-3 days (email chains, phone calls, spreadsheets)
- **Competitor approach**: Procore, BuilderTrend solve this for large GCs but start at $500+/month and are too complex for 3-5 person crews
- **Market gap**: No solution for small electrical/plumbing contractors (long tail of construction)

## Proposed Solution

Build a web app that captures leads via form, instantly drafts AI-powered estimates (30 seconds), and converts approved estimates into projects with automatic crew assignment and invoicing. Single integrated system replaces lead capture (Google Form) + estimation (email) + scheduling (text/calls) + invoicing (manual).

## Key Hypothesis

We believe **AI-drafted estimates delivered same-day** will **increase lead conversion from 40% to 70%** for **small construction crews (3-10 people)**.
We'll know we're right when **ACE Construction captures $500/month revenue and crew adoption reaches 5+ daily active users**.

## What We're NOT Building

- **Procore integration** (Phase 2+) - complex, deferred
- **Mobile app** (Phase 2+) - web-responsive MVP sufficient
- **Multi-trade marketplace** (Phase 3+) - single company MVP
- **Advanced forecasting/BI** (Phase 2+) - basic dashboards only
- **Customer portal** (Phase 2+) - email estimates MVP, portal Phase 2

## Success Metrics

| Metric | Target | How Measured |
|--------|--------|--------------|
| Lead-to-estimate time | 30 seconds | Timestamp in database |
| Lead conversion rate | 70% (from 40%) | Approved estimates / total leads |
| Monthly recurring revenue | $500 | Stripe invoices |
| Crew daily active users | 5+ | Login events |
| AI estimate accuracy | Within 10% of manual | Audit of first 20 estimates |
| Production uptime | 99% | Sentry + monitoring |

## Open Questions

- [ ] AI auto-approve <$2K estimates, or always human review?
- [ ] SMS/push notifications, or email only?
- [ ] GPS tracking for crews, or scheduling dashboard sufficient?
- [ ] Resend or SendGrid for email reliability?
- [ ] Labor breakdown in estimate, or total cost only?

---

## Users & Context

**Primary User**
- **Who**: Construction crew manager (ACE: owner/lead electrician), 35-55, tech-comfortable
- **Current behavior**: Receive lead → call customer → spend 2-3 hours in spreadsheet → email estimate → follow up by phone/text
- **Trigger**: New lead arrives → manager needs to respond <24h or lead goes cold
- **Success state**: Receive lead → click "Create Estimate" → AI drafts (30s) → review → email sent → move to next lead

**Job to Be Done**
When a new lead arrives, I want to draft a professional estimate in 30 seconds, so I can respond same-day and increase win rate (40% → 70%).

**Non-Users**
- **Large GCs** (100+ crew) → Procore/Autodesk (budget, complexity tolerance)
- **Solo contractors** (1 person) → don't need crew scheduling
- **Estimator freelancers** → different workflow (competitive bidding)

---

## Solution Detail

### Core Capabilities (MoSCoW)

| Priority | Capability | Rationale |
|----------|------------|-----------|
| Must | Lead capture (web form) | Foundation - no leads, no revenue |
| Must | AI estimate drafting | Core differentiator - speed |
| Must | Estimate approval workflow | Human review required (binding decisions) |
| Must | Project creation from estimate | Convert estimate → work |
| Must | Crew assignment | Dispatch to available crew |
| Must | Invoice generation | Collect payment |
| Must | Stripe payment processing | Accept online payment |
| Should | Dashboard (lead status, pipeline) | Visibility but not revenue-blocking |
| Should | Time entry logging | Required for invoice accuracy |
| Could | SMS/push notifications | Nice to have, email sufficient |
| Won't | Mobile native app | Web-responsive MVP enough |
| Won't | Procore integration | Phase 2 |
| Won't | Safety/compliance module | Phase 2 |
| Won't | Equipment/inventory tracking | Phase 2 |

### MVP Scope

**Week 1-2:** PRD, architecture, team, GitHub setup  
**Week 3-4:** Next.js app + auth + 4 pages + lead form  
**Week 5-8:** NestJS API (12 endpoints) + Supabase schema + Stripe webhooks + email  
**Week 9-10:** AI agents (estimate drafter + task delegator) + evaluation  
**Week 11-12:** Testing (unit, integration, E2E, security)  
**Week 13:** Deploy to production, ACE live beta, support  

### User Flow (Critical Path)

```
Lead arrives (web form)
  → Manager sees new lead in dashboard
  → Clicks "Create Estimate"
  → AI drafts estimate (30s)
  → Manager reviews & approves
  → Email sent to customer
  → Customer approves → Stripe payment link
  → Customer pays → Project created
  → Manager assigns crew
  → Crew logs time daily
  → Invoice auto-generated
  → Sent to customer, payment tracked
```

---

## Technical Approach

**Feasibility**: HIGH

**Existing Assets**
- Supabase project live (`rhlkjelglvurowdalrgh`)
- Backend skeleton (`con-os-functions.py`)
- Stripe account configured
- Zapier automation ready
- vex-hero-site (Next.js reference)

**Architecture Notes**
- Monolithic NestJS backend (easier iteration, single deploy)
- RLS policies for multi-tenant isolation (prepare for Phase 2)
- Schema pre-planned (50 tables MVP → 120+ Phase 2)
- Prompts in database (enable AI evolution)
- Events published to Kafka (async Phase 2 ready)

**Technical Risks**

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| AI estimates hallucinate | High | Guardrails (min $500, max 3x market), human approval always, evaluation tests |
| Crew won't adopt | Medium | Free trial, demo ROI, weekly check-ins |
| Supabase schema gaps | Low | Reviewed thoroughly, migrations versioned |
| Stripe webhook failures | Low | Retry logic, Sentry monitoring |
| Email reliability | Low | Fallback plan (SendGrid if needed) |

---

## Implementation Phases

| # | Phase | Description | Status | Can Parallel | Depends |
|---|-------|-------------|--------|--------------|---------|
| 1 | Spec & Planning | PRD, architecture, team, GitHub | pending | - | - |
| 2 | Frontend Setup | Next.js, auth, 4 pages, lead form | pending | - | 1 |
| 3 | Backend API | NestJS, 12 endpoints, Supabase | pending | with 4 | 1 |
| 4 | Database Schema | Expand Supabase, RLS, migrations | pending | with 3 | 1 |
| 5 | Core Workflows | Lead → Estimate → Project → Invoice | pending | - | 3,4 |
| 6 | AI Agents | Estimate drafter, task delegator, eval | pending | - | 5 |
| 7 | Testing & QA | Unit, integration, E2E, security | pending | - | 6 |
| 8 | Launch & Beta | Deploy, ACE live, support | pending | - | 7 |

### Phase Details

**Phase 1: Spec & Planning**
- Goal: Alignment on what/who/how to measure
- Scope: PRD approved, architecture approved, team assigned, GitHub repos created
- Success: Team ready to start Week 3

**Phase 2: Frontend Setup**
- Goal: Core UI ready, auth working, lead form functional (no backend yet)
- Scope: Next.js 14, Supabase auth, 4 pages, dummy data
- Success: Can log in, submit lead form (saves to DB)

**Phase 3 & 4: Backend + Database (Parallel)**
- Goal: APIs live, database complete, data flows end-to-end
- Scope: NestJS with 12 endpoints, Supabase schema expanded, RLS policies
- Success: curl tests pass, Swagger docs generated, queries <500ms

**Phase 5: Core Workflows**
- Goal: Lead-to-invoice flow works (human estimates, no AI yet)
- Scope: Lead form → API → Email → Approval → Project → Crew → Time → Invoice → Stripe
- Success: Create lead, receive estimate email, customer pays (test), invoice in dashboard

**Phase 6: AI Agents**
- Goal: Estimates drafted by AI, crew assigned by AI (both human-approved)
- Scope: Estimate drafter agent, task delegator, evaluation metrics, cost tracking
- Success: AI drafts 20+ realistic estimates, accuracy audit passes

**Phase 7: Testing & QA**
- Goal: Production-ready, 0 critical bugs, monitoring live
- Scope: Unit tests (80%+ coverage), integration, E2E, security, performance
- Success: All tests pass, security clear, production ready

**Phase 8: Launch & Beta**
- Goal: ACE live, revenue generated, support in place
- Scope: Vercel + Railway deploy, ACE crew 1-week parallel, monitoring, support playbook
- Success: 5+ crew active daily, $500+ revenue, 0 errors for 48h

---

## Decisions Log

| Decision | Choice | Alternatives | Rationale |
|----------|--------|--------------|-----------|
| Backend | NestJS | FastAPI, Express | Type safety + fast + DI modularity |
| Frontend | Next.js 14 | React SPA, Remix | SSR, Vercel deploy, App Router modern |
| Database | Supabase | Firebase, PlanetScale | Already live, RLS ready, vector support later |
| AI | LangChain | Vercel AI SDK, manual | Multi-agent orchestration |
| Deploy | Vercel + Railway | AWS ECS, Heroku | Fast, cheap, GitHub integration |
| Estimates | AI + human approval | AI only, manual only | High-stakes decisions need human review |
| Multi-tenant | RLS on org_id | Separate DBs | Simpler, scales to 100+ customers |

---

## Research Summary

**Market Context**
- Procore, Buildertrend, Jobber are market leaders but $500+/month, too complex for small crews
- Small crews (3-10 people) have no budget/complexity tolerance for enterprise platforms
- No specialized product for electricians/plumbers <$100K/year revenue
- AI-powered estimating nascent in construction; no incumbent yet
- Lead conversion: 40% manual, 65-75% achievable with speed

**Technical Context**
- Supabase fully operational (auth + DB + RLS)
- NestJS + Next.js 14 standard for construction apps (vex-hero-site pattern)
- Claude API proven for construction (estimating, compliance, safety)
- Stripe webhooks reliable for residential/commercial
- Vercel + Railway scale to millions; costs <$100/month at MVP volume

---

## Related Repositories

**Platform Architecture:**
- `iza-os-construction-core` — Shared ConstructionOS backend, UI, database, AI agents
- Serves as infrastructure for all CON-* ventures

**Tenant Repositories:**
- `con-001-ace-construction` — Pilot customer (ACE electrical)
- `con-002-plumbing-co` — Phase 2 customer (plumbing)
- `con-003-hvac-specialist` — Phase 2 customer (HVAC)
- ... (CON-004 through CON-030 as ventures launch)

**Relationship:** All CON-* ventures run on iza-os-construction-core backend, isolated by `organization_id` in RLS policies.

---

## Implementation Readiness

**Go/No-Go Checklist**
- [ ] Team assigned (PM, 2 FE, 2 BE, 1 AI, 1 DevOps)
- [ ] GitHub repos created + CI/CD skeleton
- [ ] Supabase project confirmed active
- [ ] Stripe account confirmed live
- [ ] Claude API access confirmed
- [ ] ACE Construction stakeholder kickoff scheduled

---

*Generated: 2026-07-24*
*Status: DRAFT - ready for team review*
*Next: Team assignment → Phase 1 kickoff → use `/prp-plan` to generate implementation breakdown*
