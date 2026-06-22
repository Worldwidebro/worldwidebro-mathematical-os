# CON OS — 5 Zapier Zaps Deployment Guide
**Status:** Ready to Deploy | **Timeline:** Jun 19-20, 2026  
**Reference:** `con-os-functions.py` + `CON-OS-ZAPIER-MAPPING.md`

---

## QUICK REFERENCE: 5 ZAPS AT A GLANCE

| # | Zap Name | Trigger | Actions | Time | Status |
|---|----------|---------|---------|------|--------|
| 1 | Daily Construction Briefing | Schedule (8 AM daily) | ClickUp → Slack | 30 min | ⏳ Build |
| 2 | Work Logging to Notion | ClickUp task status change | Clockify → Notion → Slack | 20 min | ⏳ Build |
| 3 | Send Invoice | Invoice created (Python webhook) | Gmail → Notion → Slack → ClickUp | 40 min | ⏳ Build |
| 4 | Process Payment | Stripe charge.succeeded webhook | Update invoice → Notion → ClickUp → Slack | 35 min | ⏳ Build |
| 5 | Weekly Revenue Report | Schedule (Friday 5 PM) | ClickUp → N8N (DuckDB) → Email → Notion | 50 min | ⏳ Build |

**Total Setup Time:** 2.5 hours (one-time)  
**Per-Venture Deployment:** 30 minutes (template reuse)

---

## ZAP #1: DAILY CONSTRUCTION BRIEFING

**Purpose:** Send team daily work assignment at 8 AM every morning

**Trigger:** Schedule → Every Day at 8:00 AM

**Actions:**
1. ClickUp: Find Tasks (List ID, Status: Not Started/In Progress, Due Date: Today)
2. Zapier Formatter: Format message with task names, assignments, hours
3. Slack: Send to #construction-{{VentureID}} with @mentions

**Setup Time:** 30 minutes

---

## ZAP #2: WORK LOGGING TO NOTION

**Purpose:** Auto-log daily work when task status changes

**Trigger:** ClickUp → Task Status Changed to "In Progress"

**Actions:**
1. Clockify: Start Timer
2. Notion: Create Work Log entry (Date, Project, Task, Hours, Status, Location, Weather)
3. Slack: Notify #proj-{{VentureID}}-work-log

**Setup Time:** 20 minutes

---

## ZAP #3: SEND INVOICE

**Purpose:** Auto-email invoice to client when created

**Trigger:** Webhook (from con-os-functions.py) → Invoice created

**Actions:**
1. Notion: Create Invoice record (ID, Client, Amount, Status)
2. Gmail: Send email with invoice breakdown and payment link
3. ClickUp: Create follow-up task
4. Slack: Notify #revenue channel

**Setup Time:** 40 minutes

---

## ZAP #4: PROCESS PAYMENT

**Purpose:** Auto-update when payment received via Stripe

**Trigger:** Stripe → Successful charge webhook

**Actions:**
1. Notion: Update Invoice Status to PAID
2. ClickUp: Create "Send thank you email" task
3. Google Calendar: Schedule follow-up call (Project closeout)
4. Slack: Notify #revenue with payment confirmation

**Setup Time:** 35 minutes

---

## ZAP #5: WEEKLY REVENUE REPORT

**Purpose:** Send weekly metrics every Friday at 5 PM

**Trigger:** Schedule → Every Friday at 5:00 PM

**Actions:**
1. ClickUp: Query projects completed this week
2. Stripe: Query successful charges this week
3. Webhook to N8N: Send data for DuckDB analysis
4. Notion: Create weekly summary entry
5. Gmail: Send detailed report with KPIs

**Setup Time:** 50 minutes

---

## DEPLOYMENT SEQUENCE

### Phase 1: Configuration (55 minutes)
- Email domain setup: 15 mins
- Stripe webhook setup: 30 mins
- Slack workspace setup: 10 mins

### Phase 2: Build Zaps (2.5 hours)
- Zap #1: 30 mins
- Zap #2: 20 mins
- Zap #3: 40 mins
- Zap #4: 35 mins
- Zap #5: 50 mins

### Phase 3: Testing (1 hour)
- End-to-end test all workflows
- Verify notifications
- Check data flow

### Phase 4: Go-Live (30 mins)
- Enable all zaps
- Activate schedules
- Monitor first 24 hours

---

## VALIDATION CHECKLIST

✓ Email delivery working  
✓ ClickUp sync active  
✓ Notion database entries created  
✓ Slack messages formatting correctly  
✓ Stripe webhook firing  
✓ Revenue calculations accurate  
✓ No duplicate notifications  
✓ Edge cases handled  

---

**Status: READY FOR IMMEDIATE DEPLOYMENT**

Next Step: Execute Phase 1 configuration, then build zaps sequentially
