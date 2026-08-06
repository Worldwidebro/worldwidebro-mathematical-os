# Agentic Email Revenue Loop — 712 Venture End-to-End

**Status:** Framework v1 (ready to test on CON-001, OPS-001, TECH-038)  
**Goal:** Every venture generates MRR via automated agent-driven email sequences + clickable CTAs routing back to landing pages.

---

## Core Loop (Repeatable Per Venture)

```
Lead captures email on landing page
    ↓ (Webhook fires)
Trigger.dev routes to Hermes Agent
    ↓ (Agent reads venture config from Supabase)
Agent loads email sequence (Resend template)
    ↓ (Hermes fetches from ventures.email_sequences[stage])
Day 0: Welcome email + CTA (clickable link → /venture/id/stage-1)
Day 1: Value email + CTA
Day 3: Social proof email + CTA
Day 7: Limited-time offer + CTA
    ↓ (User clicks CTA, lands on page with pre-filled booking/checkout)
Agent records interaction in Supabase (deal_interactions table)
    ↓ (If user books/buys, Stripe webhook fires)
Agent triggered for upsell sequence or celebration email
    ↓
MRR updated in ventures.monthly_revenue
```

---

## Schema (Supabase Tables — Already Exist)

### ventures.email_sequences
```
venture_id | stage | template_name | subject | body_html | cta_text | cta_url | delay_hours | enabled
CON-001    | welcome | con-001-welcome | "Ready to build?" | <html>...</html> | "See plans" | /ventures/con-001/plans | 0 | true
CON-001    | day-1   | con-001-value   | "Here's how..." | <html>...</html> | "Book demo" | /ventures/con-001/demo | 24 | true
```

### deal_interactions
```
deal_id | venture_id | email_sent_at | email_opened_at | cta_clicked_at | stage
DEAL-001 | CON-001 | 2026-08-05T10:00:00Z | 2026-08-05T14:30:00Z | 2026-08-05T14:35:00Z | welcome
```

---

## Per-Sector Implementations

### CONSTRUCTION (CON-001: Ace Construction)
**Funnel:** Lead inquiry → Consultation booking → Quote → Payment

**Email Sequence:**
| Stage | Delay | Subject | CTA | CTA URL |
|-------|-------|---------|-----|---------|
| welcome | 0h | "Your free construction assessment is ready" | "Book 30-min consultation" | /con-001/book-consultation |
| day-1 | 24h | "3 things you should know before hiring contractors" | "See our checklist" | /con-001/checklist |
| day-3 | 72h | "Here's what other clients paid (spoiler: you might save more)" | "Get your quote" | /con-001/quote-request |
| day-7 | 168h | "Ready to start? Let's lock in your project" | "Schedule start date" | /con-001/checkout |

**Agent role:** Respond to booking questions, suggest add-on services (electrical upgrade, design work), track consultation → quote → payment.

---

### LOGISTICS (LT-005: Medical Courier)
**Funnel:** Emergency delivery inquiry → Rate quote → Account setup → First shipment

**Email Sequence:**
| Stage | Delay | Subject | CTA | CTA URL |
|-------|-------|---------|-----|---------|
| welcome | 0h | "Your urgent delivery estimate (ready in 5 min)" | "Get rate quote" | /lt-005/rate-quote |
| day-1 | 24h | "How our 24/7 network saved $3K for hospital partners" | "View service map" | /lt-005/coverage |
| day-3 | 72h | "Set up recurring pickups and save 20%" | "Create account" | /lt-005/signup |
| day-7 | 168h | "Your first pickup is 15 minutes away" | "Track shipment" | /lt-005/track |

**Agent role:** Answer service area questions, handle hazmat inquiries, schedule pickups, upsell account features.

---

### FINANCE (FIN-037: Automated Trading System)
**Funnel:** Market data request → Demo access → Account funding → Live trading

**Email Sequence:**
| Stage | Delay | Subject | CTA | CTA URL |
|-------|-------|---------|-----|---------|
| welcome | 0h | "Your personalized portfolio analysis (AI-powered)" | "View analysis" | /fin-037/portfolio-analysis |
| day-1 | 24h | "Why our traders are up 14% YTD (while market is flat)" | "Start demo trading" | /fin-037/demo-account |
| day-5 | 120h | "Ready to go live? Here's what you need" | "Fund your account" | /fin-037/funding-setup |
| day-14 | 336h | "Your demo expires soon — go live today" | "Activate trading" | /fin-037/activate |

**Agent role:** Answer risk questions, explain strategy, suggest account tier, handle objections.

---

### REAL ESTATE (RE-001: Property Management OS)
**Funnel:** Property listing → Owner inquiry → Property assessment → Management contract

**Email Sequence:**
| Stage | Delay | Subject | CTA | CTA URL |
|-------|-------|---------|-----|---------|
| welcome | 0h | "Your property is worth: $XXX (verified estimate)" | "See valuation" | /re-001/valuation |
| day-2 | 48h | "We manage 2,340 properties in your area (earn $XXX/mo)" | "Schedule property tour" | /re-001/book-tour |
| day-7 | 168h | "Last chance: lock in management contract before rates increase" | "Sign contract" | /re-001/sign |

**Agent role:** Answer tenant questions, provide comps, process property docs, upsell maintenance packages.

---

## Implementation Path (This Week)

### Step 1: Load email sequences (1 hr)
```bash
# For each venture, seed email_sequences table
psql -h localhost -U postgres -d ventures << 'EOF'
INSERT INTO email_sequences (venture_id, stage, template_name, subject, body_html, cta_text, cta_url, delay_hours, enabled)
VALUES 
  ('CON-001', 'welcome', 'con-001-welcome', 'Your free construction assessment is ready', '<html>Welcome to Ace Construction...</html>', 'Book 30-min consultation', '/con-001/book-consultation', 0, true),
  ('CON-001', 'day-1', 'con-001-value', '3 things you should know', '<html>Before hiring any contractor...</html>', 'See our checklist', '/con-001/checklist', 24, true),
  ('CON-001', 'day-3', 'con-001-quote', 'What other clients paid', '<html>Transparent pricing...</html>', 'Get your quote', '/con-001/quote-request', 72, true),
  ('CON-001', 'day-7', 'con-001-close', 'Ready to start?', '<html>Lock in your project date...</html>', 'Schedule start date', '/con-001/checkout', 168, true);
EOF
```

### Step 2: Wire Hermes + trigger.dev (2 hrs)
Create workflow in trigger.dev:

```yaml
# trigger.dev: lead-to-email-sequence
name: venture-email-automation

trigger:
  - stripe.customer.created
  - form.submitted

actions:
  1. lookup_venture:
     source: Supabase ventures table
     query: "venture_id from deal.venture_id"
  
  2. call_hermes_agent:
     url: http://localhost:3000/hermes/gateway
     payload:
       venture_id: ${venture_id}
       lead_email: ${customer.email}
       stage: welcome
     response: agent_id
  
  3. send_email:
     service: Resend
     template: ${ventures.email_sequences.body_html}
     to: ${customer.email}
     subject: ${ventures.email_sequences.subject}
  
  4. log_interaction:
     table: deal_interactions
     record:
       deal_id: ${deal.id}
       venture_id: ${venture_id}
       email_sent_at: now()
       stage: welcome
  
  5. schedule_next_email:
     trigger.dev cron:
       delay: ${ventures.email_sequences[day-1].delay_hours}
       action: call_hermes_agent with stage=day-1
```

### Step 3: Make landing page CTAs clickable (30 min per venture)
```html
<!-- /con-001/plans page -->
<a href="/con-001/checkout?from=email-day-3&utm_campaign=day-3-quote">
  Book your consultation
</a>

<!-- On click, track in deal_interactions -->
<script>
  document.querySelectorAll('a[data-cta]').forEach(link => {
    link.addEventListener('click', () => {
      fetch('/api/deals/interactions', {
        method: 'POST',
        body: JSON.stringify({
          deal_id: '${deal_id}',
          venture_id: '${venture_id}',
          cta_clicked_at: new Date().toISOString(),
          stage: '${stage}',
          cta_url: link.href
        })
      });
    });
  });
</script>
```

### Step 4: Test loop (1 hr)
1. Submit test form → Stripe customer created
2. Hermes agent triggers (check `hermes_cli.main` logs)
3. Email received in inbox
4. Click CTA link
5. Verify deal_interactions logged in Supabase
6. Check scheduled email sent 24h later

---

## Success Metrics (Per Venture, Per Week)

| Metric | CON-001 | LT-005 | FIN-037 |
|--------|---------|--------|---------|
| Leads entering sequence | 50 | 30 | 20 |
| Email open rate | 25% | 20% | 35% |
| CTA click rate | 15% | 12% | 20% |
| Conversion to booking/signup | 5% | 8% | 12% |
| MRR delta | +$2K | +$1.5K | +$3K |

---

## What Exists Today (Don't Build)
- ✅ Hermes Agent (running, gateway mode)
- ✅ trigger.dev (serverless workflows)
- ✅ Supabase (ventures, deals, email_sequences tables ready)
- ✅ Resend (email service, auth configured)
- ✅ Landing pages (Vercel deployed, routes exist)
- ✅ Stripe (webhooks live)

## What Needs Building (This Week)
- ⏳ Seed email_sequences table per venture (SQL insert, 1 hr)
- ⏳ Build trigger.dev workflow (2 hrs)
- ⏳ Add CTA click tracking to landing pages (30 min each)
- ⏳ Test loop end-to-end (1 hr)

**Total time to live:** ~5 hours per venture (4-6 ventures per week possible)

---

## Agent Upsell Logic (Week 2+)

Once email sequences are live, agents can trigger upsells:

```
if close_probability > 70%:
  trigger upsell_sequence (premium features, add-ons)
  
if email_opened_rate < 15%:
  trigger re_engagement_sequence (discount offer)
  
if cta_click_rate > 50% but no_conversion:
  agent sends live chat message (objection handling)
```

---

## Open Questions (Clarify Before Building)

1. **CON-001:** Does booking CTA go to Calendly or internal scheduler?
2. **LT-005:** Can agent auto-generate rate quotes, or manual review required?
3. **FIN-037:** Does agent explain trading strategy, or route to live chat with trader?
4. **RE-001:** Can agent auto-process property docs, or manual verification needed?

---

**Next: Pick ONE venture (recommend CON-001), run Steps 1-4 this week, measure MRR impact.**
