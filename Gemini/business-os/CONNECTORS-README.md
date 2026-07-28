# Hermes Payment & Automation Connectors

Complete guide for 4 production integrations: Stripe payments, email delivery, Zapier automation, monitoring.

**Status:** Ready for Monday 7/28 launch (CON-001 Ace Construction)

---

## 1. Stripe Webhook Handler

**File:** `stripe_webhook_handler.py`  
**Purpose:** Receive Stripe payment events → publish to event bus → trigger Hermes agent

### Events Handled
- `invoice.payment_succeeded` — Payment confirmed, update MRR
- `customer.subscription.created` — New customer, send welcome email
- `charge.refunded` — Refund issued, send notice

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   ```bash
   export STRIPE_WEBHOOK_SECRET=whsec_xxx  # Get from Stripe dashboard
   export STRIPE_SECRET_KEY=sk_live_xxx
   export SUPABASE_KEY=your_supabase_key
   ```

3. **Create FastAPI route:**
   ```python
   from fastapi import Request
   from stripe_webhook_handler import webhook_endpoint

   @app.post("/webhooks/stripe")
   async def stripe_webhook(request: Request):
       body = await request.body()
       signature = request.headers.get("stripe-signature")
       return await webhook_endpoint(body.decode(), signature)
   ```

4. **Test locally:**
   ```bash
   python stripe_webhook_handler.py
   ```

### Monitoring
- Check `audit_logs` table for every webhook
- View traces in Langfuse dashboard
- Monitor error rate in Prometheus/Grafana

---

## 2. Email Service (Resend)

**File:** `email_service.py`  
**Purpose:** Send transactional emails for customer lifecycle

### Email Sequences
- **Day 0:** Welcome email (on signup)
- **Day 2:** Onboarding check-in (via Zapier)
- **Day 5:** Upsell follow-up (via Zapier)
- **Payment:** Receipt email (after successful charge)
- **Refund:** Refund notice (on charge reversal)

### Setup

1. **Create Resend account:** https://resend.com
2. **Get API key** from dashboard
3. **Set environment variable:**
   ```bash
   export RESEND_API_KEY=re_xxx
   export FROM_EMAIL=noreply@aceconstruction.com
   ```

4. **Test:**
   ```bash
   python -c "
   import asyncio
   from email_service import send_welcome_email
   asyncio.run(send_welcome_email('test@example.com', 'CON-001'))
   "
   ```

### Integration Points
- `stripe_webhook_handler.py` calls `send_payment_receipt()` and `send_welcome_email()`
- Zapier zaps call email service via event_bus or webhook
- All emails logged in Resend dashboard

---

## 3. Zapier Automation (3 Zaps)

**File:** `ZAPIER-SETUP-GUIDE.md`  
**Purpose:** Connect Jotform → Supabase → Email automation

### The 3 Zaps

| Zap | Trigger | Action | When |
|-----|---------|--------|------|
| **Zap 1** | Jotform form submitted | Insert row in Supabase | Immediate |
| **Zap 2** | New row in Supabase | Send welcome email | Day 0 |
| **Zap 3** | Scheduled (every 2 days) | Send follow-ups | Day 2 & 5 |

**Setup:** See `ZAPIER-SETUP-GUIDE.md` for detailed UI steps

---

## 4. Monitoring & Observability

**File:** `MONITORING-SETUP-GUIDE.md`  
**Purpose:** Track costs, latency, errors, revenue

### Services

| Service | URL | Purpose |
|---------|-----|---------|
| Langfuse | http://localhost:3003 | LLM traces (Hermes costs/latency) |
| Prometheus | http://localhost:9090 | System metrics (payment count, errors) |
| Grafana | http://localhost:3001 | Dashboards & alerts |

**Setup:** See `MONITORING-SETUP-GUIDE.md` for detailed configuration

---

## Environment Variables

```bash
# Stripe
STRIPE_WEBHOOK_SECRET=whsec_xxx
STRIPE_SECRET_KEY=sk_live_xxx

# Email
RESEND_API_KEY=re_xxx
FROM_EMAIL=noreply@aceconstruction.com

# Monitoring
LANGFUSE_PUBLIC_KEY=pk_xxx
LANGFUSE_SECRET_KEY=sk_xxx
LANGFUSE_HOST=http://localhost:3003

# Infrastructure
SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
SUPABASE_KEY=eyJhbGc...
REDIS_URL=redis://localhost:6379
```

---

## Pre-Launch Checklist

- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Stripe webhook secret in `.env`
- [ ] Resend API key in `.env`
- [ ] Zapier: All 3 zaps published (toggled ON)
- [ ] Monitoring: Langfuse + Prometheus running
- [ ] FastAPI route `/webhooks/stripe` created
- [ ] Tests pass: `python test_connectors.py`

---

## Files

```
stripe_webhook_handler.py      # Stripe → Event Bus
email_service.py               # Resend email wrapper
test_connectors.py             # Integration tests
requirements.txt               # Dependencies
CONNECTORS-README.md           # This file
ZAPIER-SETUP-GUIDE.md          # Zapier UI setup
MONITORING-SETUP-GUIDE.md      # Monitoring guide
```
