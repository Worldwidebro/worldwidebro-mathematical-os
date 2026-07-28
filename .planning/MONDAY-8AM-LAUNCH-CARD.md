---
date: 2026-07-29
time: "8:00 AM ET"
status: Ready to execute
---

# Monday 8:00 AM — ACE Construction Launch Card

## 25 Min Launch Window (8:00–8:30 AM)

### 8:00–8:05: Zapier Setup (5 min)

```
1. zapier.com → Create new Zap
2. Trigger: Jotform (form 262034682245051)
   Event: New Submission
3. Action: Gmail
   To: [your email]
   Subject: {{First Name}}, here's your readiness score
   Body: You scored {{readiness_pct}}% readiness
4. Test → ON
```

**Done when:** Zap shows "Active"

---

### 8:05–8:15: Stripe Webhook (10 min)

**Step A: Stripe Dashboard (2 min)**
```
1. https://dashboard.stripe.com/webhooks
2. "Add an endpoint"
3. URL: https://con-001-ace-construction.vercel.app/api/stripe/webhook
4. Events: payment_intent.succeeded, checkout.session.completed
5. Copy signing secret (whsec_...)
```

**Step B: Vercel (3 min)**
```
1. https://vercel.com → con-001-ace-construction
2. Settings → Environment Variables
3. Add: STRIPE_WEBHOOK_SECRET = [paste from step A]
4. Deploy (auto on env change)
```

**Step C: Verify (5 min)**
```bash
stripe trigger payment_intent.succeeded
# Check Stripe logs for POST to webhook endpoint
```

**Done when:** Vercel shows green deploy + Stripe shows endpoint active

---

### 8:15–8:25: E2E Test (10 min)

**Test 1: Form Submission**
```
1. https://form.jotform.com/262034682245051
2. Fill: Name=Test, Email=[your-email], Industry=Construction, Hours=20
3. Submit
⏱ Wait 2 min for email → Check inbox
✓ Row in Supabase assessments table
```

**Test 2: Payment**
```
1. https://con-001-ace-construction.vercel.app
2. Click "Start Assessment ($97)"
3. Card: 4242 4242 4242 4242, any future date, any CVC
4. Complete checkout
✓ Row in Supabase deal_payments table
✓ Dashboard MRR now shows $97
```

**Done when:** All 3 systems show live data (email + table + dashboard)

---

### 8:25–8:30: Final Check

- [ ] Zapier zap is ON
- [ ] Stripe webhook endpoint is active
- [ ] Vercel has STRIPE_WEBHOOK_SECRET env var
- [ ] Form submission test passed
- [ ] Payment test recorded
- [ ] Dashboard displays live MRR ($97)

---

## 9:00 AM: LAUNCH

**Post TikTok #1** → Funnel begins

---

## Fallback (if any step fails)

| Issue | Fix | Time |
|-------|-----|------|
| Email didn't arrive | Zapier paused → re-enable zap | 2 min |
| Payment didn't record | Stripe webhook not wired → check Vercel env var | 3 min |
| Dashboard still $0 | Vercel build stale → manual redeploy | 2 min |

**Confidence: 95%** ✅  
**Rollback:** None needed (all systems isolated, no data loss)

---

**Use this card Monday morning. Everything else is already done.**
