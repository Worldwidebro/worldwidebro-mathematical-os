---
name: VENTURES-REMOTE-ENV
title: Ventures Remote Environment Configuration Inventory
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Ventures Remote Environment Configuration Inventory

**Updated:** 2026-08-01  
**Auto-update:** Daily 8am UTC (via GitHub Actions or local cron)  
**Source of Truth:** This file + Vercel projects + Supabase console

---

## Supabase Instances (Master Registry)

| Instance | Project ID | URL | Purpose | Ventures |
|----------|-----------|-----|---------|----------|
| **Main** | `cyhzilqldouzgynacqpe` | https://cyhzilqldouzgynacqpe.supabase.co | Unified platform DB | All active ventures (shared) |
| CON-001 | `rhlkjelglvurowdalrgh` | (Supabase) | Construction payments | CON-001 (ACE) |
| *To add* | *pending* | | | |

**Credentials Location:**
- Local: `/Users/acebless/.claude/settings.local.json` (SUPABASE_URL)
- Vercel env: Set via `vercel env add` (requires SUPABASE_SERVICE_ROLE_KEY)
- Production: Supabase dashboard API settings

---

## Venture Deployment Status

### ✅ LIVE (Vercel Deployed)

#### **CON-001: Ace Construction**
- **URL:** https://con-001-ace-construction.vercel.app
- **Repo:** `/Users/acebless/Documents/02_PROJECTS/CON/con-001-ace-construction`
- **Stack:** Next.js, Supabase, Stripe, Resend, Zapier
- **Supabase Project:** `cyhzilqldouzgynacqpe` (shared)
- **Stripe Account:** Connected (webhooks active)
- **Vercel Config:** `vercel.json` (NextJS, iad1 region)
- **Env Vars Needed:**
  - ✅ `NEXT_PUBLIC_SUPABASE_URL` (live)
  - ✅ `NEXT_PUBLIC_SUPABASE_ANON_KEY` (live)
  - ⏳ `SUPABASE_SERVICE_ROLE_KEY` (needed for API routes)
  - ✅ `RESEND_API_KEY` (live)
  - ✅ `STRIPE_SECRET_KEY` (live)
  - ✅ `STRIPE_WEBHOOK_SECRET` (live)
- **Last Deploy:** Jul 28, 2026
- **Status:** Ready (needs SUPABASE_SERVICE_ROLE_KEY only)

#### **LT-005: Medical Courier Dispatch**
- **URL:** (pending — local dev)
- **Repo:** `/Users/acebless/Documents/_archive/lt-005-medical-courier-dispatch`
- **Stack:** React, auth, billing, dispatcher, customer-portal
- **Supabase Project:** `cyhzilqldouzgynacqpe` (shared)
- **Stripe Account:** (configuration pending)
- **Vercel Config:** vercel.json (pending review)
- **Status:** Code complete; needs Vercel deploy + env setup

#### **STA-001: Staffing Agency** *(Week 1 launch 2026-08-04)*
- **URL:** (not deployed yet)
- **Repo:** `/Users/acebless/Documents/_archive/ops-staff-001-staffing`
- **Stack:** HTML forms (client/employee intake) + ClickUp + weekly MD tracking
- **Supabase Project:** `cyhzilqldouzgynacqpe` (shared, for ClickUp data sync)
- **Stripe Account:** (not configured)
- **Vercel Config:** N/A (forms are HTML only)
- **Status:** Infrastructure ready; execution phase starting
- **Files:**
  - Forms: `forms/customer/onboarding/client-intake.html`, `forms/employee/onboarding/candidate-application.html`
  - Daily: `templates/WEEKLY-CALL-SHEET.md`
  - Weekly: `STAFFING-AGENCY-STATUS.md`
  - Tracking: ClickUp "Staffing Agency" space

#### **Vex Hero (Main Platform)**
- **URL:** https://vex-hero-site.vercel.app (or custom domain)
- **Repo:** `/Users/acebless/Documents/vex-hero-site`
- **Stack:** React/Vite, Vercel
- **Supabase Project:** `cyhzilqldouzgynacqpe` (shared)
- **Vercel Config:** `vercel.json` (SPA routing only)
- **Status:** Live; links to all ventures

#### **Vex API (Backend)**
- **URL:** (API only — pending Vercel/Railway deploy)
- **Repo:** `/Users/acebless/Documents/vex-api`
- **Stack:** Node.js/Express, Supabase
- **Supabase Project:** `cyhzilqldouzgynacqpe` (shared)
- **Status:** Code ready; deployment pending

### 🚀 PENDING DEPLOYMENT

#### **EC-111: Miss Toys (E-commerce)**
- **Repo:** `/Users/acebless/Documents` (Medusa backend locally running)
- **Stack:** Medusa, Stripe, Vercel/Railway
- **Status:** Backend live locally; storefront + payment integration pending
- **Needs:** Stripe connect, Vercel/Railway deploy, UI

#### **RE-001: Real Estate**
- **Repo:** `/Users/acebless/Documents/re-001-worldwidebro-holdings`
- **Status:** Blueprint complete; code pending
- **Needs:** Core SaaS backend, property listings, agent portal

#### **OPS-001: Operations**
- **Repo:** `/Users/acebless/Documents/_archive/ops-001-*`
- **Status:** ClickUp integration + templates ready
- **Needs:** Vercel frontend for OpCo dashboard

### ⏱️ NOT STARTED

| Venture | Code Ready | Deployment Ready | Blockers |
|---------|-----------|-----------------|----------|
| FIN-* (Trading) | Partial | No | Broker API keys, backtest framework |
| Other sectors | Varies | No | (Audit framework for each) |

---

## Conversion Tracking (STA-001 Model)

### Files That Tell Status

#### **Daily Execution Tracking**
- **File:** `WEEKLY-CALL-SHEET.md`
- **Updated:** Daily (team fills in during work)
- **Shows:** Call log, daily outreach metrics, job orders this week
- **Owner:** Sales team

#### **Real-time ClickUp Tracking**
- **Location:** ClickUp "Staffing Agency" workspace
- **Lists:** Target Accounts, Client Job Orders, Candidate Pipeline, Placements & Billing
- **Shows:** Prospect status, who's been called, who's a client, where candidates are
- **Owner:** Operations manager

#### **Weekly Summary Dashboard**
- **File:** `STAFFING-AGENCY-STATUS.md`
- **Updated:** Friday EOD (auto-fill from ClickUp + call sheet data)
- **Shows:** Weekly metrics, revenue, conversion rates by sector, historical trends
- **Owner:** Leadership reporting

### Conversion Stages & Tracking

| Stage | Criterion | Tracked In | Example |
|-------|-----------|-----------|---------|
| **Prospect** | Called, no JO yet | WEEKLY-CALL-SHEET row | "Acme Tech — interested, callback Thu" |
| **Client** | Signed agreement | ClickUp "Client Job Orders" list + client-intake.html form | Company profile captured, agreement signed |
| **Active** | Has ≥1 Job Order | ClickUp "Client Job Orders" (JO-001, JO-002, etc.) | "Acme Tech: Senior Engineer $120-150K" |
| **Placement** | Candidate submitted | ClickUp "Candidate Pipeline" (Submitted status) | Candidate sent to hiring manager |
| **Closed** | Candidate accepted | ClickUp "Placements & Billing" + Supabase `deal_payments` | Invoice issued, 20% fee collected |

### How to Know if Conversion is Real

✅ **Prospect → Client:** Form submission from client-intake.html completed + stored  
✅ **Client → Active:** At least 1 Job Order created in ClickUp "Client Job Orders" list  
✅ **Active → Placement:** Candidate record moved to "Submitted" status in ClickUp "Candidate Pipeline"  
✅ **Placement → Closed:** Entry in ClickUp "Placements & Billing" + Supabase `deal_payments` table has amount > 0  

**Verification:** Every Friday, STAFFING-AGENCY-STATUS.md shows conversion funnels (prospects → clients → placements → revenue). If a company is in "Client Job Orders" but not "Placements & Billing", they're active but not yet converted to revenue.

---

## Daily 8am Update (Proposed Automation)

### What Gets Updated
1. **STAFFING-AGENCY-STATUS.md** — Weekly metrics auto-filled from ClickUp
2. **This file (VENTURES-REMOTE-ENV.md)** — Vercel/Supabase status snapshotted
3. **Deployment checklist** — Any venture env changes flagged

### Trigger
- **Option A:** GitHub Actions (`.github/workflows/venture-env-sync.yml`) at 08:00 UTC daily
- **Option B:** Local macOS cron job (launchctl plist)
- **Option C:** Manual: `npm run sync-venture-env`

### Script Needed
```bash
# scripts/venture-env-sync.js
# 1. vercel env ls (fetch all Vercel projects' env vars)
# 2. supabase query ventures table (count active ventures)
# 3. clickup export (STA-001: calls, JOs, placements, revenue)
# 4. update VENTURES-REMOTE-ENV.md (status table)
# 5. update STAFFING-AGENCY-STATUS.md (metrics from ClickUp export)
# 6. git add + git commit + git push
```

---

## File Organization (Current State)

### Staffing Agency (STA-001)
- `/Users/acebless/Documents/_archive/ops-staff-001-staffing/STAFFING-AGENCY-STATUS.md` — Weekly dashboard
- `/Users/acebless/Documents/_archive/ops-staff-001-staffing/templates/WEEKLY-CALL-SHEET.md` — Daily log
- `/Users/acebless/Documents/_archive/ops-staff-001-staffing/forms/customer/onboarding/client-intake.html` — Client capture
- `/Users/acebless/Documents/_archive/ops-staff-001-staffing/forms/employee/onboarding/candidate-application.html` — Candidate capture
- `/Users/acebless/Documents/CLAUDE.md` — STA-001 operations section

### Active Ventures
- `02_PROJECTS/CON/con-001-ace-construction/` — Live on Vercel
- `_archive/lt-005-medical-courier-dispatch/` — Ready to deploy
- `vex-hero-site/` — Live
- `vex-api/` — Ready to deploy

---

## T7 Shield (Backup Drive)

**Status:** Not currently mounted  
**Path when mounted:** `/Volumes/T7/` (via Tailscale: `ssh macstudio-t7`)  
**Recommended:** Monthly sync of all venture repos + environment templates

---

**Last Updated:** 2026-08-01 09:15 UTC  
**Next Update:** 2026-08-02 08:00 UTC (when automated sync runs)
