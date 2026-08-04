# Venture Readiness Checklist

**Purpose:** Form for humans (call center, ops, finance, engineering) showing exactly what to complete  
**Update Frequency:** Daily (auto-synced from ClickUp)  
**Visibility:** Phone + Desktop  
**Principle:** Humans make calls & decisions. AI does everything else.

---

## STA-001: Staffing Agency (Week 1 EXECUTING — Aug 4 Launch)

### Call Center (Daily, Mon-Fri)
**Role:** Call Center Employee  
**Daily Target:** 50 calls/day  
**Tool:** Phone + ClickUp + HTML forms

**Workflow (don't think, just do):**
```
1. Open ClickUp → "Target Accounts" list
2. Call company (9am-5pm)
3. Log outcome in ClickUp:
   - Interested → Fill client-intake.html form (takes 2 min)
   - Not interested → Mark "not interested"
   - Callback → Schedule follow-up
4. Done ✓
```

**Don't worry about:**
- ❌ Data entry beyond form
- ❌ CRM syncing (automatic)
- ❌ Reports (automatic)
- ❌ Metrics (automatic)

**Check weekly:** Are your calls in ClickUp? If yes, you're done.

### Operations (Weekly, Friday 4-6pm)
**Role:** Operations Manager  
**Tool:** ClickUp + 1 markdown file

**Workflow:**
```
1. Open ClickUp "Staffing Agency" workspace
2. Copy these 4 numbers:
   - Calls this week (from "Target Accounts" history)
   - Job orders (from "Client Job Orders" count)
   - Candidates submitted (from "Candidate Pipeline" → Submitted)
   - Placements closed (from "Placements & Billing" count)
3. Paste into STAFFING-AGENCY-STATUS.md
4. Done ✓
```

**Checklist:**
- [ ] Get calls count from ClickUp
- [ ] Get jobs count from ClickUp
- [ ] Get candidates count from ClickUp
- [ ] Get placements count from ClickUp
- [ ] Paste into STAFFING-AGENCY-STATUS.md "Weekly Metrics" table
- [ ] Add week to "Historical" table
- [ ] Identify 1-2 blockers (what's slowing us down?)
- [ ] Note top-performing sector

**Time:** 30 minutes  
**Blocker:** If you can't find numbers in ClickUp, ping DevOps

### Finance (Weekly, Friday)
**Role:** Finance / Billing  
**Tool:** Stripe dashboard + Supabase

**Workflow:**
```
1. Check Stripe → Payouts (how much came in this week?)
2. If new money: Copy amount to STAFFING-AGENCY-STATUS.md "Weekly Revenue"
3. Done ✓
```

**Checklist:**
- [ ] Check Stripe dashboard for new payments
- [ ] Update STAFFING-AGENCY-STATUS.md revenue line
- [ ] (That's it — Stripe talks to Supabase automatically)

---

## CON-001: Ace Construction (LIVE on Vercel)

### Deployment (TODAY — 5 min)
**Role:** DevOps / Senior Engineer  
**Tool:** Terminal + Vercel CLI

**Blocker:** Missing 1 environment variable on Vercel

**Workflow:**
```
1. Get key: https://app.supabase.com/project/cyhzilqldouzgynacqpe/settings/api
   → Copy "Service Role Key" (long string starting with eyJ...)
2. Terminal: vercel env add SUPABASE_SERVICE_ROLE_KEY
   → Paste key when prompted
3. Terminal: vercel deploy --prod
4. Test: curl -X POST https://con-001-ace-construction.vercel.app/api/contact \
     -H "Content-Type: application/json" \
     -d '{"name":"Test","email":"test@test.com"}'
5. Check Supabase: ventures → venture_leads table should have test record
6. Done ✓
```

**Checklist:**
- [ ] Get SUPABASE_SERVICE_ROLE_KEY from Supabase console
- [ ] Run vercel env add
- [ ] Run vercel deploy --prod
- [ ] Curl test endpoint
- [ ] Verify test record in Supabase
- [ ] Update VENTURES-REMOTE-ENV.md (change ⏳ to ✅)

**Time:** 5 minutes

### Sales (Ongoing)
**Role:** Sales / Marketing  
**Tool:** Phone + Form submissions

**Workflow:**
```
1. Monitor form submissions on https://con-001-ace-construction.vercel.app
2. When someone submits → Record in Supabase automatically (you don't do anything)
3. Follow up within 24 hours
4. Done ✓
```

**Checklist:**
- [ ] Check Supabase `venture_leads` table daily
- [ ] Call prospects within 24 hours
- [ ] Log outcomes in ClickUp "Leads" list

---

## LT-005: Medical Courier Dispatch (Ready to Deploy)

### Deployment (By Aug 5 — 2-3 hours)
**Role:** DevOps / Senior Engineer  
**Tool:** Vercel + GitHub

**Workflow:**
```
1. Create Vercel project: vercel link
2. Add env vars (see .env.example):
   - vercel env add NEXT_PUBLIC_SUPABASE_URL (value: https://cyhzilqldouzgynacqpe.supabase.co)
   - vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY (ask DevOps)
   - vercel env add SUPABASE_SERVICE_ROLE_KEY (get from Supabase)
   - vercel env add STRIPE_SECRET_KEY (needs Stripe account setup first — see below)
3. vercel deploy --prod
4. Test login (can you create account + log in?)
5. Done ✓
```

**Blockers:**
- [ ] Stripe Connect account not set up (need: Secret Key + Webhook Secret)
- [ ] Supabase tables may not exist (ask DevOps to verify schema)

**Checklist:**
- [ ] Create Vercel project
- [ ] Add all env vars from .env.example
- [ ] Deploy to Vercel
- [ ] Test login flow
- [ ] Test basic dispatch request
- [ ] Update VENTURES-REMOTE-ENV.md

**Time:** 2-3 hours

### Stripe Setup (Required for LT-005)
**Role:** Finance / Engineering  
**Tool:** Stripe dashboard

**Workflow:**
```
1. Go to https://stripe.com/connect (create or use existing account)
2. Create API keys (Restricted Recommended):
   - Publishable key (pk_live_...)
   - Secret key (sk_live_...)
   - Restricted key (rk_live_...)
3. Get Webhook secret (Webhooks → Add endpoint → get signing secret)
4. Share keys with engineering (they add to Vercel)
5. Done ✓
```

**Checklist:**
- [ ] Stripe Connect account created/verified
- [ ] API keys generated (pk_ + sk_ + rk_)
- [ ] Webhook configured
- [ ] Keys shared with engineering
- [ ] Update VENTURES-REMOTE-ENV.md

---

## EC-111: Miss Toys (E-commerce — In Development)

### Storefront Build (By Aug 10 — 4 hours)
**Role:** Frontend Engineer  
**Tool:** Vercel + React + Medusa API

**Workflow:**
```
1. Build product listing page (React component)
2. Build product detail page
3. Build shopping cart
4. Build checkout page
5. Connect to Medusa API (http://localhost:9000/store)
6. Deploy to Vercel
7. Done ✓
```

**Checklist:**
- [ ] Product listing page built
- [ ] Product detail page built
- [ ] Cart built
- [ ] Checkout page built
- [ ] API connected (products loading from Medusa)
- [ ] Deployed to Vercel
- [ ] Test buy a product (get to payment screen)

**Time:** 4-6 hours

### Stripe + Payment (By Aug 10 — 2 hours)
**Role:** Finance + Engineering  
**Tool:** Stripe + Medusa + Vercel

**Workflow:**
```
1. Finance: Create Stripe Connect (see LT-005 checklist above)
2. Engineering: Add Stripe keys to Vercel
3. Engineering: Test payment flow (buy product → get to Stripe payment screen)
4. Finance: Verify Stripe shows successful payment
5. Done ✓
```

**Checklist:**
- [ ] Stripe Connect account created
- [ ] API keys in Vercel env
- [ ] Payment screen appears in checkout
- [ ] Test purchase completes
- [ ] Stripe dashboard shows payment received
- [ ] Payout schedule configured

---

## RE-001: Real Estate (Planning — MVP Week 2)

### Product Definition (By Aug 8 — 1 hour)
**Role:** Product Manager  
**Tool:** Notion + GitHub Issues

**Workflow:**
```
1. Define MVP: What's the simplest version that sells?
2. Write user stories in GitHub Issues:
   - "As an agent, I can search properties"
   - "As a buyer, I can contact an agent"
   - "As an admin, I can add properties"
3. Prioritize (what builds first?)
4. Assign to engineering
5. Done ✓
```

**Checklist:**
- [ ] MVP features defined (search, detail, contact, admin upload)
- [ ] GitHub Issues created (1 per feature)
- [ ] Assigned to engineers
- [ ] Sprint planned (Week 2: Aug 12-16)
- [ ] Blocked by what? (data source? agent onboarding?)

**Blockers to solve:**
- [ ] Where do properties come from? (MLS integration? user uploads? seed data?)
- [ ] How do agents sign up? (separate onboarding flow?)
- [ ] CRM link (where do leads go?)

---

## OPS-001: Operations (Planning)

### ClickUp Setup (By Aug 8 — 1 hour)
**Role:** Operations Manager  
**Tool:** ClickUp

**Workflow:**
```
1. Create "Operations" workspace in ClickUp
2. Create lists: Daily Tasks, Weekly Metrics, Blockers, Roadmap
3. Add recurring tasks (daily standup, weekly review)
4. Invite team members
5. Done ✓
```

**Checklist:**
- [ ] Workspace created
- [ ] Lists created (Daily, Weekly, Blockers, Roadmap)
- [ ] Recurring tasks set up
- [ ] Team invited

---

## What NOT to Do (Save Time)

**Don't:**
- ❌ Copy data from ClickUp to spreadsheets (it's already there)
- ❌ Send weekly status emails (dashboard does it)
- ❌ Update CRM manually (forms auto-sync)
- ❌ Create reports (GitHub Actions does it)
- ❌ Schedule follow-ups manually (AI does it)
- ❌ Organize by-sector metrics (dashboard shows it)
- ❌ Repeat data entry (forms do it once)

**Do:**
- ✅ Make calls
- ✅ Fill out forms when prospect says YES
- ✅ Set appointments
- ✅ Make decisions (blockers, priorities)
- ✅ Review metrics weekly
- ✅ Escalate problems

---

## Status Legend

| Status | Meaning | Action |
|--------|---------|--------|
| 🟢 EXECUTING | In progress, on track | Keep executing |
| 🟡 READY | Code done, needs deploy | Deploy this week |
| 🟠 PLANNING | Defining, not building yet | Finalize plan, assign |
| 🔴 BLOCKED | Waiting on external thing | Unblock (in "Blockers" row) |
| ⚫ NOT STARTED | No progress | Don't start yet |

---

## Weekly Rhythm (Who Does What)

**Monday 9am:**
- Call center: Start Week 1 calls (or continue)
- Ops: Brief team on priorities

**Daily (Mon-Fri):**
- Call center: Make 50 calls, fill forms if YES
- DevOps: Monitor deployments (if any)

**Friday 4pm:**
- Ops: Export ClickUp → fill checklist
- Finance: Check Stripe → update revenue
- Leads shared with leadership

**Sunday night:**
- AI sync runs (dashboard updates for Monday)

---

**Last Updated:** 2026-08-01 09:15 UTC  
**How to Use:** Print this → give to each team member → they only do their section  
**Update:** Weekly (add new ventures as they launch)  
**Visible On:** Phone (dashboard coming) + This file
