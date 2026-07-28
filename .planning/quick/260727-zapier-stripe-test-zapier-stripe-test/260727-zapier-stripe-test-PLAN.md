---
date: 2026-07-27
time: 20:15 EDT
objective: Wire Zapier + Stripe webhook + end-to-end test for Ace Construction Monday launch
scope: 3 tasks, ~25 minutes total
target: Ready by Monday 8:30am ET
---

# Quick Execution Plan — Zapier + Stripe Wiring

**Status:** 🟢 All systems live, 3 connections need wiring  
**Launch:** Monday 7/28, 9:00am ET  
**Current readiness:** 95%

---

## What's Already Live

| Component | Status | Reference |
|-----------|--------|-----------|
| Jotform | ✅ Live | Form ID: 262034682245051 |
| Zapier MCP | ✅ Authenticated | Ready to create zaps |
| Gmail MCP | ✅ Authenticated | Ready to send emails |
| Stripe Price + Link | ✅ Live | price_1TwkzkGogataxROkO2aFKziN ($97/mo) |
| Supabase Tables | ✅ Live | assessments, ace_customers, deal_payments, venture_leads |
| Vercel Deployment | ✅ Live | Next.js app auto-deploys on git push |

---

## Task 1: Create Jotform → Gmail Zapier Zap (5 min)

**What:** Automate form submission → Email 1 send  
**Impact:** Leads get response email immediately after filling form

### Steps

1. **Open Zapier Dashboard**
   - https://zapier.com/app/dashboard

2. **Create New Zap**
   - Trigger: **Jotform** → "New Submission"
   - Select form ID: `262034682245051`
   - Test trigger (submit dummy form)

3. **Add Action: Gmail**
   - Action: **Gmail** → "Send Email"
   - From: `winnerscirclewcllc@gmail.com`
   - To: `{{submitter_email}}`
   - Subject: `Your Ace Construction Assessment is Ready`
   - Body: Use template from `ACE-CONSTRUCTION-EMAIL-SEQUENCE.md` (Email 1)
   - Include Stripe link: `https://buy.stripe.com/3cI5kD86Q94f85I1yZ8g000`

4. **Test & Publish**
   - Test with dummy submission
   - Confirm email arrives
   - Publish zap

### Verify

```bash
# After publishing, submit test form
# Check Gmail inbox for arrival within 30 sec
```

**Success:** Email 1 arrives within 30 seconds of form submission

---

## Task 2: Activate Stripe Webhook Endpoint (10 min)

**What:** Register webhook listener, add signing secret to Vercel  
**Impact:** Stripe sends payment events → Supabase records

### Steps

1. **Get Webhook Endpoint URL**
   ```bash
   # URL is already in codebase at:
   # /Users/acebless/Documents/con-001-ace-construction/app/api/webhooks/stripe/route.ts
   
   # Public URL (Vercel):
   # https://con-001-ace-construction.vercel.app/api/webhooks/stripe
   ```

2. **Register Webhook in Stripe Dashboard**
   - Go: https://dashboard.stripe.com/webhooks
   - Click "Add endpoint"
   - Endpoint URL: `https://con-001-ace-construction.vercel.app/api/webhooks/stripe`
   - Events to send:
     - `payment_intent.succeeded`
     - `charge.completed`
   - Copy signing secret (starts with `whsec_`)

3. **Add Secret to Vercel Environment**
   ```bash
   # Option A: Via Vercel Dashboard
   # Project: con-001-ace-construction
   # Settings → Environment Variables
   # Add: STRIPE_WEBHOOK_SECRET = [copied value]
   
   # Option B: Via CLI
   vercel env add STRIPE_WEBHOOK_SECRET
   # Paste secret when prompted
   vercel redeploy
   ```

4. **Verify Webhook**
   - Stripe dashboard shows endpoint as "active"
   - No red warning flags

### Test Event

```bash
# Send test event from Stripe dashboard
# Webhook details → "Send test webhook"
# Select payment_intent.succeeded

# Verify in Supabase:
psql -h localhost -U postgres -d ventures \
  -c "SELECT * FROM deal_payments ORDER BY created_at DESC LIMIT 1;"
```

**Success:** Test webhook event recorded in Supabase deal_payments table

---

## Task 3: End-to-End Test (10 min)

**What:** Complete flow: Form → Email → Payment → Dashboard  
**Impact:** Validates all pieces connected before Monday launch

### Test Sequence

#### Step 1: Submit Form (1 min)

```bash
# Visit form
curl -s "https://form.jotform.com/262034682245051" | head -c 100

# Or manually:
# https://form.jotform.com/262034682245051
# Fill with test data:
# Name: Test User
# Email: your-test-email@gmail.com
# Industry: Construction
# Hours: 35
```

#### Step 2: Verify Email Arrival (2 min)

```bash
# Check inbox for:
# - Subject: "Your Ace Construction Assessment is Ready"
# - From: winnerscirclewcllc@gmail.com
# - Contains Stripe link
# - Arrives within 30 seconds of form submission
```

#### Step 3: Process Payment (3 min)

```bash
# Use Stripe test card:
# https://buy.stripe.com/3cI5kD86Q94f85I1yZ8g000

# Fill with:
# Email: your-test-email@gmail.com
# Card: 4242 4242 4242 4242 (test card)
# Expiry: 12/25
# CVC: 123

# Complete payment
```

#### Step 4: Verify Supabase Records (2 min)

```bash
# Check assessments table (form submission)
psql -h localhost -U postgres -d ventures \
  -c "SELECT name, email, readiness_pct FROM assessments WHERE email='your-test-email@gmail.com' ORDER BY created_at DESC LIMIT 1;"

# Check deal_payments table (payment recorded)
psql -h localhost -U postgres -d ventures \
  -c "SELECT venture_id, amount, paid_at FROM deal_payments WHERE created_at > NOW() - '10 minutes'::interval;"

# Check venture_leads table (pipeline visibility)
psql -h localhost -U postgres -d ventures \
  -c "SELECT venture_id, email, created_at FROM venture_leads WHERE email='your-test-email@gmail.com';"
```

#### Step 5: Verify Dashboard Display (2 min)

```bash
# Visit Hermes dashboard:
# https://con-001-ace-construction.vercel.app/dashboard

# Verify cards show:
# - Lead Count: 1+ (from venture_leads)
# - MRR This Month: $97+ (from deal_payments)
# - Recent submissions visible
```

### Success Checklist

- [ ] Form submission recorded in assessments table
- [ ] Email 1 arrived within 30 seconds
- [ ] Payment processed (Stripe shows $97 charge)
- [ ] deal_payments table has new record
- [ ] Dashboard shows updated lead count + MRR
- [ ] No webhook errors in Stripe logs

---

## Rollback Plan (If Any Failure)

| Failure | Fix | Time |
|---------|-----|------|
| Email doesn't arrive | Restart Zapier zap, test trigger again | 2 min |
| Webhook fails | Check Vercel env vars set correctly, redeploy | 3 min |
| Dashboard doesn't update | Verify Supabase queries in code, check RLS policies | 5 min |

---

## Timeline

| Time | Task | Owner |
|------|------|-------|
| **Tonight (7/27, 8:15–8:45pm ET)** | Create Zapier zap + activate webhook | Claude |
| **Tonight (8:45–8:55pm ET)** | End-to-end test | Claude + User verification |
| **Monday 8:00am ET** | Final pre-flight checks (system health) | Claude |
| **Monday 9:00am ET** | **LAUNCH** — Post TikTok #1, monitor conversions | User |

---

## Success Metrics (First 24 Hours)

| Metric | Target | How to Verify |
|--------|--------|---|
| Form submissions | 10+ | `SELECT COUNT(*) FROM assessments WHERE created_at > NOW() - '24 hours'::interval;` |
| Email deliveries | 100% | Check Gmail folder, no bounces |
| Payment conversions | 1–2 | `SELECT COUNT(*) FROM deal_payments WHERE created_at > NOW() - '24 hours'::interval;` |
| Dashboard live | All cards visible | Visual check of Vercel deployment |
| Webhook success rate | 100% | Stripe dashboard shows 0 failures |

---

## Resources

- **Zapier MCP:** Authenticated, ready to execute
- **Gmail MCP:** Authenticated, ready to send
- **Stripe Dashboard:** https://dashboard.stripe.com
- **Vercel Project:** con-001-ace-construction
- **Supabase:** CivilizationOS (rhlkjelglvurowdalrgh)
- **Email Template:** `/Users/acebless/Documents/ACE-CONSTRUCTION-EMAIL-SEQUENCE.md`

---

**Status:** 🟢 Ready to execute  
**Confidence:** 95% (all systems tested separately, this wires them together)  
**Next:** Execute tasks, then launch Monday 9am
