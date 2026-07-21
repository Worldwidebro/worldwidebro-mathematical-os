---
title: Complete Funnel Strategies (Investor + Customer + Founder) + Monorepo Architecture
date: 2026-07-20
status: Implementation Blueprint
---

# PART 1: INVESTOR FUNNEL STRATEGY

## Three Investor Personas & Funnels

**Persona A: Angel/Micro-VC ($10K-$500K)**
- Entry: LinkedIn ad → `/investors` landing
- CTA: "Schedule 15-min Intro"
- Conversion: Founder call → Term sheet (14-30 days)

**Persona B: Institutional LP ($1M-$10M)**
- Entry: Warm intro → `/institutional` landing  
- CTA: "Request LP Call"
- Conversion: Due diligence → Closing (30-90 days)
- Post-close: Access `/lp-portal` (real-time dashboards)

**Persona C: Sovereign/Strategic ($10M+)**
- Entry: Government relations → `/strategic` landing
- CTA: "Strategic Meeting Request"
- Conversion: Economic impact modeling → Partnership (60-180 days)

**Investor Pages Needed:**
- `/investors` — Quick pitch, 2-min video, CTA
- `/institutional` — Fund structure, historical returns, fee model
- `/strategic` — Jobs created, tax revenue impact, regional stories
- `/lp-portal` — Private dashboard (portfolio, reports, docs)

---

# PART 2: CUSTOMER FUNNEL STRATEGY

## Three Customer Personas & Journeys

**Persona A: End Users (SaaS/Service customers)**
- Discovery → Free trial → Onboarding → Upgrade → Renewal
- Example: Using CON venture estimating software
- Pages: `/` (hero), `/pricing` (tiers), `/case-studies`, `/dashboard` (portal)

**Persona B: Buyers (Evaluating solutions)**
- Problem search → Demo request → Sales call → Proposal → Contract
- Example: Construction company evaluating vendors
- Pages: `/solutions` (how we solve), `/comparison`, `/resources`, `/contact`

**Persona C: Enterprise Procurement**
- Compliance check → RFQ → Legal review → Signature
- Pages: `/security` (SOC 2, GDPR), `/compliance` (HIPAA/PCI), `/sla`, `/procurement`

**Customer Portal (all ventures):**
- Account status + billing
- Usage metrics
- Invoice history
- Team + access control
- API keys + webhooks
- Support tickets
- Knowledge base

---

# PART 3: FOUNDER RESOURCES STRATEGY

## Founder Hub Sections

**Discovery Phase:**
- `/founders` — Application criteria, timeline, success stories
- `/join` — Application form + acceptance process

**Building Phase:**
- `/playbooks` — SaaS, Services, Physical playbooks
- `/operating-system` — IZA OS shared infrastructure
- `/templates` — Business plans, pitch decks, financial models
- `/tools` — Supabase setup, n8n workflows, Stripe guides

**Growth Phase:**
- `/funding` — How to raise from the fund
- `/dashboard` — Real-time venture KPIs (revenue, runway)
- `/support` — 1:1 advisors + cohort peers
- `/community` — Founder groups, monthly calls, peer learning

---

# PART 4: MONOREPO ARCHITECTURE

## Target Repository Structure

```
worldwidebro-holdings/  (monorepo)
│
├── apps/
│   ├── vex-hero-site/           (Holdings brand + portfolio)
│   ├── investor-portal/         (LP dashboard)
│   ├── founder-hub/             (Resources + playbooks)
│   └── venture-template/        (Template + CLI generator)
│
├── packages/
│   ├── shared-components/       (SectorHero, VentureCard, Dashboard)
│   ├── design-tokens/           (Tailwind config, colors, typography)
│   ├── content/                 (Playbooks, case studies, FAQs)
│   └── api-client/              (Supabase, n8n, Stripe clients)
│
├── services/
│   ├── api/                     (REST API)
│   ├── webhooks/                (n8n handlers)
│   ├── agents/                  (CrewAI orchestration)
│   └── migrations/              (Supabase schema)
│
├── tools/
│   ├── venture-factory/         (create_venture.py CLI)
│   ├── sector-generator/        (generate sector hubs)
│   └── analytics-pipeline/      (automated reporting)
│
└── docs/
    ├── ARCHITECTURE.md
    ├── DEPLOYMENT.md
    ├── INVESTOR-FUNNEL.md
    ├── CUSTOMER-FUNNEL.md
    ├── FOUNDER-RESOURCES.md
    └── OPERATIONS.md
```

## Current vs Target

| Component | Current | Target | Status |
|-----------|---------|--------|--------|
| Holdings brand | vex-hero-site | Part of monorepo | ✅ Exists |
| Sector hubs | Manual (6 planned) | 14 templated pages | ❌ Week 1 |
| Investor portal | None | `/lp-portal` with dashboards | ❌ Week 2 |
| Founder hub | Scattered docs | Unified `/founders` | ❌ Week 2 |
| Venture sites | 50 individual repos | 1 template + CLI | ❌ Week 3-4 |
| Shared components | Only in vex | `packages/shared-components` | ❌ Week 1 |
| Backend API | None | REST API service | ❌ Week 2 |
| Webhook handlers | Ad-hoc | `services/webhooks` | ❌ Week 2 |
| Agent orchestration | ✅ Built | Move to `services/agents` | 🟡 Move |
| Database schema | Supabase UI | Version control | ❌ Week 1 |

## Monorepo Benefits

✅ Single source of truth for components/branding
✅ Deploy all sectors in parallel (Vercel)
✅ Shared code across all apps via `packages/`
✅ PNPM workspaces for isolated dependency management
✅ Atomic commits for related changes across apps

---

# SUCCESS CHECKLIST

✅ Documentation complete (this file + 3 funnel docs)
✅ Pages inventory (SECTOR-PAGES-COMPLETION-STATUS.md)
✅ Agent & execution roadmap (PAGES-AND-AGENTS-ROADMAP.md)
✅ Local infrastructure running (Docker containers up)

❌ Sector hero pages deployed (6 live, ready Week 1)
❌ Investor funnel wired (forms → Supabase, dashboard live)
❌ Customer funnels optimized (pricing, trial, renewal automation)
❌ Founder hub built (playbooks + tools accessible)
❌ Monorepo structure live (vex-hero-site consolidated, apps/ created)

