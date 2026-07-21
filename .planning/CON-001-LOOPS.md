# CON-001 Loop Engineering — 5 Core Loops

## Loop 1: Lead Intake (L1 — automated + report)

**Trigger:** Gmail webhook (new inquiry)  
**State:** `STATE.md` (track lead count, classification distribution)  
**Action:** 
1. Extract email (name, project, budget, timeline)
2. Classify with AI (complexity: low/mid/high)
3. Create record in Supabase `venture_leads`
4. Notify Slack `#new-leads`

**Cadence:** Real-time (webhook)  
**Verifier:** Lead appears in Supabase within 1 minute  
**Budget:** ~0.05 tokens per email (AI classification)

---

## Loop 2: Proposal Generation (L1 — automated delivery)

**Trigger:** Manual approval in admin portal OR auto-trigger 2h after lead created  
**State:** `STATE.md` (proposals generated, sent, viewed)  
**Action:**
1. Query lead details from Supabase
2. Generate scope + pricing with OpenAI
3. Render PDF (template)
4. Email to customer + Slack notification

**Cadence:** Real-time or scheduled  
**Verifier:** PDF received by customer, tracked via link click  
**Budget:** ~2-3 tokens per proposal (OpenAI generation)

---

## Loop 3: Payment Processing (L2 — webhook listener)

**Trigger:** Stripe payment webhook (payment_intent.succeeded)  
**State:** `STATE.md` (revenue YTD, payment success rate)  
**Action:**
1. Receive Stripe event
2. Match to Supabase invoice_id
3. Update `venture_projects.status` → "paid"
4. Send confirmation email + Slack alert

**Cadence:** Real-time (webhook)  
**Verifier:** Status updated in Supabase within 10 seconds  
**Budget:** Negligible (no AI)

---

## Loop 4: Daily Briefing (L1 — scheduled report)

**Trigger:** Daily 8am EST  
**State:** `STATE.md` (daily_briefings_sent, avg_response_time)  
**Action:**
1. Query: new leads (24h), proposals sent, payments received, overdue projects
2. Format summary (markdown)
3. Post to Slack `#briefing`
4. Update STATE.md with metrics

**Cadence:** Daily weekdays (0 8 * * 1-5)  
**Verifier:** Slack message posted, STATE.md updated  
**Budget:** ~0.1 tokens per briefing (formatting)

---

## Loop 5: Exception Monitoring (L2 — anomaly detection)

**Trigger:** Every 6 hours  
**State:** `STATE.md` (anomalies_detected, avg_resolution_time)  
**Action:**
1. Query: overdue projects (>30 days), unpaid invoices (>7 days), payment failures (last 6h)
2. Score severity (critical/warning/info)
3. Post to Slack `#alerts` only if critical/warning
4. Track in STATE.md

**Cadence:** 0 */6 * * * (every 6 hours)  
**Verifier:** Alerts arrive <5 min of condition trigger  
**Budget:** ~0.2 tokens per check (anomaly scoring)

---

## STATE.md Template

```
# CON-001 Loop State

## Metrics (updated daily by daily-briefing loop)
- Total leads (24h): 0
- Proposals sent (24h): 0
- Revenue YTD: $0
- Active projects: 0
- Overdue projects: 0

## Loop Status
| Loop | Last Run | Status | Next Run |
|------|----------|--------|----------|
| Lead Intake | — | 🟢 Ready | Real-time |
| Proposal Gen | — | 🟡 Pending config | On demand |
| Payment Processing | — | 🟢 Ready | Real-time |
| Daily Briefing | — | 🟢 Ready | 2026-07-17 08:00 |
| Exception Monitor | — | 🟡 Pending testing | 2026-07-17 06:00 |

## Run Log
| Date | Loop | Trigger | Status | Notes |
|------|------|---------|--------|-------|
| — | — | — | — | — |
```

---

## Loop Budget

| Loop | Cadence | Tokens/Run | Runs/Month | Total Tokens |
|------|---------|-----------|-----------|--------------|
| Lead Intake | Per email (~10/day) | 0.05 | 300 | 15 |
| Proposal Gen | Per approval (~5/day) | 2-3 | 150 | 375 |
| Payment Processing | Per payment (~5/day) | 0 | 150 | 0 |
| Daily Briefing | 1/day | 0.1 | 20 | 2 |
| Exception Monitor | Every 6h | 0.2 | 120 | 24 |
| **TOTAL** | — | — | — | **~416 tokens/month** |

---

## Next Steps

1. ✅ Define loops (this file)
2. → Create STATE.md + budget tracking
3. → Wire Zapier/n8n per loop
4. → Deploy + test each loop
5. → Measure (loop-ready score)
6. → Document in loop-engineering registry
7. → Scale to next 10 ventures
