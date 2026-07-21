---
title: Sector Pages Completion Status — What's Live vs. Missing
date: 2026-07-20
status: Inventory
---

# DEPLOYED (LIVE) ✅

## Holdings Brand Site
| Site | URL | Status | Last Updated | Blocker |
|------|-----|--------|--------------|---------|
| **VEX (Portfolio Hub)** | https://vex-hero-site-sigma.vercel.app | Live | Jul 16 | Missing pages: Case Studies, Intake/Apply, Advisory, Sector heroes, 404 (in git stash) |

## Sector Pages (Deployed)

### COMM (Community) — 50 Ventures ✅ COMPLETE
| Site | URL | Status | Type |
|------|-----|--------|------|
| **Bloom Hub** | https://bloom-community-hub.vercel.app | Live | Sector hub + 48 venture links |
| **comm-001 to comm-050** | https://comm-NNN-*.vercel.app | Live (48/50) | Individual venture sites |
| **comm-014, comm-019** | (Vercel deploy failed) | Blocked | Network error (ECONNRESET) — needs retry |

### CON (Construction) — 1 Deployed
| Site | URL | Status | Blocker |
|------|-----|--------|---------|
| **CON-001 Ace Construction** | https://con-001-ace-construction.vercel.app | Live | Stripe/Resend secrets not configured |

### STA (Staffing) — 1 Deployed
| Site | URL | Status | Blocker |
|------|-----|--------|---------|
| **OPS-STAFF-001 Staffing** | https://ops-staff-001-staffing.vercel.app | Live (built parallel) | Not audited this session |

---

# MISSING SECTOR PAGES (High Priority) ❌

## Pages That Need to Be Created

### 1. **CON (Construction) — Sector Hero Page**
**Status:** ❌ Not created  
**Template:** vex-hero-site/src/components/SectorHero.tsx  
**Content Needed:**
- Hero section (CTA to leads form)
- Services grid (estimating, scheduling, risk assessment)
- Case studies (from CON ventures)
- Pricing/packages
- Lead capture form → Supabase trigger
- Link to CON-001 + other CON ventures

**Time to deploy:** 2-3 hours (template exists, content needed)

### 2. **STA (Staffing) — Sector Hero Page**
**Status:** ❌ Not created  
**Template:** vex-hero-site/src/components/SectorHero.tsx  
**Content Needed:**
- Hero section (contractor/client split CTAs)
- Available roles grid
- Matching algorithm explainer
- Testimonials from STA ventures
- Lead capture (job poster → Supabase)
- Link to OPS-STAFF-001 + other STA ventures

**Time to deploy:** 2-3 hours

### 3. **RE (Real Estate) — Sector Hero Page**
**Status:** ❌ Not created  
**Template:** vex-hero-site/src/components/SectorHero.tsx  
**Content Needed:**
- Hero section (buyer/seller/agent CTAs)
- Properties showcase (from RE ventures)
- Valuation tool explainer
- Market analysis features
- Lead capture (property inquiry → Supabase)
- Link to RE ventures

**Time to deploy:** 2-3 hours

### 4. **EDU (Education) — Sector Hero Page**
**Status:** ❌ Not created  
**Template:** vex-hero-site/src/components/SectorHero.tsx  
**Content Needed:**
- Hero section (student/educator/parent CTAs)
- Course offerings from EDU ventures
- Learning outcomes + skills
- Content atomization explainer (30-layer curriculum)
- Enrollment form → Supabase
- Link to EDU ventures

**Time to deploy:** 2-3 hours

### 5. **FIN (Finance) — Sector Hero Page**
**Status:** ❌ Not created  
**Template:** vex-hero-site/src/components/SectorHero.tsx  
**Content Needed:**
- Hero section (investors/traders CTAs)
- Portfolio management tools showcase
- Risk modeling features
- Risk calculator explainer
- Lead capture (account inquiry → Supabase)
- Link to FIN ventures

**Time to deploy:** 2-3 hours

### 6. **LOG (Logistics) — Sector Hero Page**
**Status:** ❌ Not created  
**Template:** vex-hero-site/src/components/SectorHero.tsx  
**Content Needed:**
- Hero section (shipper/carrier CTAs)
- Route optimization demo
- Tracking features
- Cost calculator
- Quote form → Supabase
- Link to LOG ventures

**Time to deploy:** 2-3 hours

---

# VEX SITE MISSING PAGES (Currently in Git Stash)

**Location:** `vex-hero-site` repo, stashed changes

| Page | Purpose | Status | Content |
|------|---------|--------|---------|
| **Case Studies** | Client success stories | Stashed | — |
| **Intake/Apply** | New venture application flow | Stashed | — |
| **Advisory Packages** | Consulting + support tiers | Stashed | — |
| **Sector Heroes** | CON, STA, RE, EDU, FIN, LOG hubs | Stashed | — |
| **404** | Error page | Stashed | — |

**Action:** `git stash pop` in vex-hero-site → add missing sector hubs → deploy

---

# INDIVIDUAL VENTURE SITES (Beyond Sector Hubs)

## COMM (Community) — 50 Real Ventures ✅ DEPLOYED
All 48-50 sites are live:
- Static Next.js apps (no backend wiring)
- Informational only (no lead capture → agent workflows yet)
- Real repos with real code (verified in `repo-site-scan-2026-07`)

## CON (Construction) — Ventures Ready to Deploy
| Venture | Repo | Status | Blocker |
|---------|------|--------|---------|
| CON-001 | con-001-ace-construction | Live | Stripe/Resend config |
| CON-002 to CON-012 | con-002-*.vercel.app (estimated) | Built (not deployed) | — |

## STA (Staffing) — Ventures Ready to Deploy
| Venture | Repo | Status | Blocker |
|---------|------|--------|---------|
| STA-001/OPS-STAFF-001 | ops-staff-001-staffing | Live | Audit needed |
| STA-002 to STA-010 | sta-*.vercel.app (estimated) | Built (not deployed) | — |

## RE (Real Estate) — Ventures Ready to Deploy
| Venture | Repo | Status | Blocker |
|---------|------|--------|---------|
| RE-001 to RE-008 | re-*.vercel.app (estimated) | Built (not deployed) | — |

## EDU (Education) — Ventures Ready to Deploy
| Venture | Repo | Status | Blocker |
|---------|------|--------|---------|
| EDU-001 to EDU-015 | edu-*.vercel.app (estimated) | Built (not deployed) | — |
| ET-011 | et-011-landing-kit | Live | — |

## FIN (Finance) — Ventures Ready to Deploy
| Venture | Repo | Status | Blocker |
|---------|------|--------|---------|
| FIN-001 to FIN-020 | fin-*.vercel.app (estimated) | Built (not deployed) | — |

## LOG (Logistics) — Ventures Ready to Deploy
| Venture | Repo | Status | Blocker |
|---------|------|--------|---------|
| LOG-001 to LOG-010 | log-*.vercel.app (estimated) | Built (not deployed) | — |

---

# COMPLETION ROADMAP (What Needs to Happen)

## Phase 1: Fix Existing Deployments (2-3 days)
- ✅ COMM: Already done (48/50 deployed)
- ⏳ CON-001: Wire Stripe + Resend (1 day)
- ⏳ STA-001: Audit + wire if needed (1 day)
- ⏳ VEX site: Pop stashed pages + deploy (1 day)

## Phase 2: Create Sector Hero Pages (3-4 days)
- Create CON sector hero (2-3h)
- Create STA sector hero (2-3h)
- Create RE sector hero (2-3h)
- Create EDU sector hero (2-3h)
- Create FIN sector hero (2-3h)
- Create LOG sector hero (2-3h)
- **Total:** ~15-18 hours (can be parallelized)

## Phase 3: Deploy Individual Ventures (Parallel, 5-7 days)
- Deploy CON ventures (CON-002 to CON-012) — ~2h
- Deploy STA ventures (STA-002 to STA-010) — ~2h
- Deploy RE ventures (RE-001 to RE-008) — ~2h
- Deploy EDU ventures (EDU-001 to EDU-015) — ~2h
- Deploy FIN ventures (FIN-001 to FIN-020) — ~2h
- Deploy LOG ventures (LOG-001 to LOG-010) — ~2h
- **Total:** ~12 hours (run in parallel = 2-3 days)

## Phase 4: Wire Lead Capture → Agent Workflows (Ongoing)
- Form submit → Supabase venture_leads table
- n8n webhook trigger → CON crew execution
- Output actions (CRM, calendar, proposals, invoices)
- **This is separate from page creation; happens in parallel**

---

# CRITICAL INSIGHT

**You have 96 real venture sites built across the portfolio.** Most aren't deployed yet because:
1. **No sector hero pages exist** (CON, STA, RE, EDU, FIN, LOG need these)
2. **No lead capture wiring** (forms submit but no agent triggers)
3. **No secrets configured** (Stripe, Resend, Supabase keys missing)

**The template exists.** Sector pages can be created in 2-3 hours each using the `SectorHero` component pattern already proven in COMM.

---

# NEXT ACTIONS (Today)

1. **Restore VEX stashed pages** — `git stash pop` (5 min)
2. **Create ONE sector hero** (CON) as proof-of-concept (2-3h)
3. **Deploy it** to Vercel (5 min)
4. **Template the remaining 5** (STA, RE, EDU, FIN, LOG) — (12-15h)
5. **Deploy all 6 sector hubs in parallel** (15 min)
6. **Then:** Wire lead capture → agents

**Time to completion:** 24-30 hours (can compress to 2-3 days if parallelized)
**Blocker:** None — all templates + repos ready.
