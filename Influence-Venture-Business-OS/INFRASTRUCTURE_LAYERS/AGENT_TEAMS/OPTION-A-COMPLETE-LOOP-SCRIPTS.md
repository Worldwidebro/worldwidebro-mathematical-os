# OPTION A: COMPLETE LOOP SCRIPTS (All 9)
## Production-Ready Scripts for OPS-001, CON-001, RE-001

**Status:** ✅ Ready to Deploy  
**Scripts:** 9 (3 per venture)

---

## OPS-001: STAFFING OPERATIONS

### Loop 1: Daily Staffing Matching
```
/loop 1d /staffing-matching-engine

1. Query Supabase: available contractors + open venture positions
2. Score matches (skills, rate, availability)
3. Filter: score >= 60
4. Create ClickUp tasks for top 5 matches
5. Post Slack summary
6. Update health scores

Output: 5-10 matches/day, Slack dashboard, ClickUp tasks
```

### Loop 2: Bi-Weekly Payroll
```
/loop 2w /contractor-payroll friday-5pm

1. Query time logs (last 14 days)
2. Calculate: hours × rate = gross, minus 15% taxes = net
3. Create Stripe transfers for all contractors
4. Create ClickUp payroll tasks
5. Post Slack summary ("$47,250 paid, 156 hours")
6. Send contractor confirmations

Output: Payroll processed, Slack posted, emails sent
```

### Loop 3: Daily Utilization Analytics
```
/loop 1d /utilization-analytics at-10am

1. Calculate: billable hours / available hours = utilization %
2. Segment: underutilized (<75%), optimal (75-90%), overutilized (>90%)
3. Create placement tasks for underutilized
4. Alert for overutilized (burnout risk)
5. Post Slack dashboard
6. Log metrics to Supabase

Output: Utilization % by contractor, Slack dashboard, ClickUp alerts
```

---

## CON-001: CONSTRUCTION OPERATIONS

### Loop 1: Daily Opportunities
```
/loop 1d /construction-opportunities at-8am

1. Query SAM.gov, NCDOT, Charlotte CIP, HomeAdvisor
2. Score match: skills, budget, capacity
3. If score >= 70: Create HubSpot deal + ClickUp task
4. Post Slack: "5 new opportunities (4 qualified)"
5. Update health scores

Output: HubSpot deals, ClickUp tasks, Slack alert (15-25/week)
```

### Loop 2: Daily Project Status
```
/loop 1d /construction-daily-standup at-4pm

1. Query active projects (% complete, budget, timeline)
2. Alert if: behind >3 days, over budget >10%, safety issue
3. Create ClickUp escalation tasks
4. Post Slack dashboard with 5 active projects
5. Update health scores

Output: ClickUp alerts, Slack status (85%+ on-time, 80%+ on-budget)
```

### Loop 3: Weekly Billing
```
/loop 1w /construction-billing friday-5pm

1. Calculate invoices (labor + materials + subs + equipment + contingency)
2. Create Supabase invoice records
3. Send to clients via email
4. Track payments (received, overdue, pending)
5. Auto-pay subcontractors (when customer paid)
6. Post Slack summary ("$245K invoiced, $98K received")

Output: Invoices sent, payments tracked, subs paid on-time
```

---

## RE-001: REAL ESTATE OPERATIONS

### Loop 1: Monthly Rent Collection
```
/loop 1m /tenant-rent-collection on-day-1

1. Charge all active tenants via Stripe
2. Track: received, failed, overdue
3. Auto-reminders: day 5 (email), day 10 (SMS), day 15 (legal escalation)
4. Create ClickUp tasks for late payers
5. Post Slack: "Collected $6,000/6,000 (100%)"
6. Update cash flow

Output: Rent charged, Slack post, late payers tracked (98%+ collection)
```

### Loop 2: Monthly Maintenance
```
/loop 1m /property-maintenance as-needed

1. Query open maintenance requests
2. Prioritize: emergency (24h), urgent (5d), routine (30d)
3. Contact vendors, get quotes, schedule
4. Track completion, cost, quality
5. Post Slack: "5 completed, $2,100 spent"
6. Update OCR (operating cost ratio)

Output: Repairs scheduled/completed, vendors managed, costs tracked
```

### Loop 3: Monthly Expenses
```
/loop 1m /property-expenses on-day-15

1. Collect: mortgage, taxes, insurance, utilities, maintenance, HOA
2. Process payments (ACH, auto-draft, checks)
3. Calculate: total expenses, OCR (expenses/rent), net cash flow
4. Create monthly P&L
5. Post Slack: "Rent: $6,000, Expenses: $4,850, Net: $1,150, OCR: 81%"
6. Generate tax report (depreciation, deductions)

Output: Expenses tracked, P&L generated, Slack dashboard, tax prep
```

---

## VERIFICATION CHECKLIST

Before deploying, verify:

```
DATABASE:
  ☐ OPS-001: 10+ contractors in Supabase
  ☐ CON-001: 5+ sample projects in Supabase
  ☐ RE-001: 3+ properties with tenants in Supabase

INTEGRATIONS:
  ☐ Slack webhooks tested (message posts)
  ☐ ClickUp API working (can create tasks)
  ☐ HubSpot API working (can create deals)
  ☐ Stripe working (can charge/transfer)
  ☐ Supabase queries working

CHANNELS:
  ☐ 3 Slack channels exist
  ☐ 3 ClickUp workspaces exist
  ☐ HubSpot 3 pipelines exist
```

---

## DEPLOY ALL 9

Once verified, activate:

```
/loop 1d /staffing-matching-engine
/loop 2w /contractor-payroll friday-5pm
/loop 1d /utilization-analytics at-10am
/loop 1d /construction-opportunities at-8am
/loop 1d /construction-daily-standup at-4pm
/loop 1w /construction-billing friday-5pm
/loop 1m /tenant-rent-collection on-day-1
/loop 1m /property-maintenance as-needed
/loop 1m /property-expenses on-day-15
```

**✅ All 9 loops LIVE**
