# LOOPS IMPLEMENTATION ROADMAP
## Complete Execution Plan: Options A, B, C, D (2026-06-10 → 2026-06-28)

**Scope:** OPS-001, CON-001, RE-001 (3 ventures, 9 core loops, 2 weeks)  
**Execution Model:** Parallel infrastructure + sequential validation  
**Success Criteria:** All 9 loops running + validated by 2026-06-28

---

## PHASE 0: DEPENDENCY MAP

```
OPTION B (Infrastructure) ←─ prerequisite for ─→ OPTION A (Scripts)
                                                       ↓
OPTION A (Scripts) ←──── prerequisite for ───→ OPTION C (Test OPS-001)
                                                       ↓
OPTION C (Test) ←────── prerequisite for ─────→ OPTION D (All 3 ventures)
```

**Key insight:** B and A can start in parallel if we define schemas first.

---

## EXECUTION PLAN

### **WEEK 1: Infrastructure (B) + Scripts (A) in Parallel**

#### **OPTION B: INFRASTRUCTURE**

**Goal:** Create Supabase tables, Slack channels, ClickUp workspaces for all 3 ventures

**B.1 Supabase Tables (Day 1-2)**

```sql
OPS-001 (Staffing):
  CREATE TABLE staffing_contractors (
    id UUID PRIMARY KEY,
    name TEXT,
    skills TEXT[], -- ["Python", "React", "Project Management"]
    hourly_rate INT, -- 60-150
    availability INT, -- hours/week available
    status TEXT, -- 'available', 'assigned', 'unavailable'
    nps_score INT -- 0-100
  );

  CREATE TABLE staffing_assignments (
    id UUID PRIMARY KEY,
    contractor_id UUID,
    venture_id TEXT, -- "BW-001", "FIN-036", etc.
    start_date DATE,
    end_date DATE,
    hours_logged INT,
    status TEXT -- 'active', 'completed', 'paused'
  );

  CREATE TABLE staffing_payroll (
    id UUID PRIMARY KEY,
    contractor_id UUID,
    period DATE, -- "2026-06-15" (bi-weekly)
    hours INT,
    rate INT,
    amount INT, -- hours * rate
    payment_date DATE,
    status TEXT -- 'pending', 'paid', 'disputed'
  );

CON-001 (Construction):
  CREATE TABLE construction_projects (
    id UUID PRIMARY KEY,
    venture_id TEXT, -- "CON-001"
    name TEXT,
    budget INT,
    spent INT,
    timeline_start DATE,
    timeline_end DATE,
    progress_pct INT, -- 0-100
    status TEXT -- 'planning', 'in-progress', 'completed'
  );

  CREATE TABLE construction_daily_logs (
    id UUID PRIMARY KEY,
    project_id UUID,
    date DATE,
    hours INT,
    tasks TEXT,
    issues TEXT,
    photo_url TEXT,
    safety_incidents INT
  );

  CREATE TABLE construction_invoices (
    id UUID PRIMARY KEY,
    project_id UUID,
    amount INT,
    invoice_date DATE,
    due_date DATE,
    paid_date DATE,
    status TEXT -- 'sent', 'overdue', 'paid'
  );

RE-001 (Real Estate):
  CREATE TABLE real_estate_properties (
    id UUID PRIMARY KEY,
    venture_id TEXT, -- "RE-001"
    address TEXT,
    purchase_price INT,
    current_value INT,
    monthly_rent INT,
    status TEXT -- 'occupied', 'vacant', 'maintenance'
  );

  CREATE TABLE real_estate_tenants (
    id UUID PRIMARY KEY,
    property_id UUID,
    name TEXT,
    lease_start DATE,
    lease_end DATE,
    rent_amount INT,
    status TEXT -- 'active', 'moving-out', 'evicted'
  );

  CREATE TABLE real_estate_maintenance (
    id UUID PRIMARY KEY,
    property_id UUID,
    date DATE,
    category TEXT, -- 'emergency', 'urgent', 'routine'
    cost INT,
    status TEXT -- 'open', 'in-progress', 'completed'
  );

  CREATE TABLE real_estate_expenses (
    id UUID PRIMARY KEY,
    property_id UUID,
    month DATE,
    mortgage INT,
    property_tax INT,
    insurance INT,
    utilities INT,
    maintenance INT
  );
```

**B.2 Slack Channels (Day 2)**

```
Create channels:
  #ops-001-staffing
    - Webhook: Matching alerts, payroll confirmations, utilization summary
    - Daily post: 9 AM matching report, 4 PM standup
    - Weekly post: Friday payroll summary
  
  #con-001-construction
    - Webhook: Opportunity alerts, project updates, budget alerts
    - Daily post: 4 PM project status
    - Weekly post: Friday invoice summary
  
  #re-001-property
    - Webhook: Rent collection, maintenance, expense updates
    - Monthly post: 1st—rent collection status
    - Monthly post: 15th—expense summary
```

**B.3 ClickUp Workspaces (Day 2-3)**

```
OPS-001 Staffing:
  ├── Active Assignments (tracking placements)
  ├── Pending Matches (contractor suggestions)
  ├── Contractor Pipeline (recruitment)
  └── Payroll Queue (ready to pay)

CON-001 Construction:
  ├── Active Projects (tracking progress)
  ├── Opportunities/Bids (sales pipeline)
  ├── Subcontractor Schedule (scheduling)
  └── Quality Issues (blockers)

RE-001 Property:
  ├── Properties (portfolio management)
  ├── Tenant Management (leases, payments)
  ├── Maintenance Requests (work orders)
  └── Capital Planning (major expenses)
```

**B.4 HubSpot Setup (Day 3)**

```
OPS-001:
  - Custom object: "Placement" (contractor + venture match)
  - Pipeline stages: In Conversation → Negotiating → Placed

CON-001:
  - Custom object: "Bid" (opportunity tracking)
  - Pipeline stages: Opportunity → Bid Submitted → Won → In Progress → Complete

RE-001:
  - Deal tracking for property acquisitions (if needed)
```

**Deliverable:** Infrastructure ready (Supabase, Slack, ClickUp, HubSpot)  
**Effort:** 2-3 hours  
**Owner:** Claude (me)

---

#### **OPTION A: LOOP SCRIPTS (Parallel Track)**

**Goal:** Write the actual loop automation code

**A.1 OPS-001 Loop Scripts (Day 1-3)**

Three loop scripts:

```
LOOP 1: /staffing-matching-engine
  Runs: Daily at 9 AM
  
  Steps:
    1. Get available contractors (status = 'available')
    2. Get open venture positions
    3. Score matches: skills match, rate fit, availability
    4. Filter: score > 60
    5. Top 5 matches → Create ClickUp tasks
    6. Post to Slack: "5 new matches found"
  
  Output:
    - ClickUp: 5 tasks assigned to ops manager
    - Slack: Daily match summary
    - Supabase: Log match attempts

LOOP 2: /contractor-payroll
  Runs: Every 2 weeks (Friday 5 PM)
  
  Steps:
    1. Get time logs for period
    2. For each contractor: hours × rate = amount
    3. Create Stripe transfer
    4. Record in Supabase payroll table
    5. Email confirmation to contractor
    6. Post to Slack: "12 contractors, $47,250 paid"
  
  Output:
    - Stripe: ACH transfers initiated
    - Supabase: Payroll ledger updated
    - Email: Payment confirmations sent
    - Slack: Payroll summary

LOOP 3: /utilization-analytics
  Runs: Daily at 10 AM
  
  Steps:
    1. Get last 7 days of time logs per contractor
    2. Calculate: billable hours / available hours = utilization %
    3. Segment: overutilized (>90%), optimal (75-90%), underutilized (<75%)
    4. For underutilized: create ClickUp "Find placement" task
    5. For overutilized: create alert
    6. Post to Slack: "8 optimal, 2 under, 1 over"
  
  Output:
    - ClickUp: Tasks for contractors needing placement
    - Slack: Daily utilization dashboard
    - Supabase: Utilization metrics logged
```

**A.2 CON-001 Loop Scripts (Day 3-5)**

Three loop scripts:

```
LOOP 1: /construction-opportunities
  Runs: Daily at 8 AM
  
  Steps:
    1. Query SAM.gov: NC contracts > $50K
    2. Query NCDOT: Bid opportunities
    3. Query Charlotte CIP: City projects
    4. Query HomeAdvisor: Quote requests
    5. For each opportunity: Match to our capability
    6. Create HubSpot deal
    7. Create ClickUp bid task (due in 3 days)
    8. Post to Slack: "5 new opportunities"
  
  Output:
    - HubSpot: Deal created for each opportunity
    - ClickUp: Bid preparation task
    - Slack: Daily opportunity summary

LOOP 2: /construction-daily-standup
  Runs: Daily at 4 PM
  
  Steps:
    1. For each active project:
       - Get progress: % complete
       - Get budget: spent vs budget
       - Get timeline: days behind/ahead
    2. Collect: hours logged, tasks, issues, photos
    3. Check alerts:
       - Behind >3 days? Create escalation task
       - Over budget >10%? Create escalation task
       - Safety incident? Immediate alert
    4. Update Supabase project record
    5. Post to Slack: "5 projects: 3 on-track, 1 behind, 1 weather"
  
  Output:
    - Supabase: Project status updated
    - ClickUp: Alerts created for issues
    - Slack: Daily project dashboard

LOOP 3: /construction-billing
  Runs: Weekly (Friday 5 PM)
  
  Steps:
    1. Get completed project milestones
    2. Generate invoice: labor + materials + margin
    3. Send via Stripe/email
    4. Track payment status (record when paid)
    5. If overdue >30 days: reminder task
    6. Pay subcontractors within 7 days of collection
    7. Post to Slack: "Invoiced: $145K, Received: $98K"
  
  Output:
    - Invoices: Sent to customers
    - Supabase: Payment ledger
    - Slack: Weekly billing summary
```

**A.3 RE-001 Loop Scripts (Day 3-5)**

Three loop scripts:

```
LOOP 1: /tenant-rent-collection
  Runs: Monthly (day 1)
  
  Steps:
    1. Get all active tenants
    2. Charge rent via Stripe
    3. If failed: send payment reminder
    4. If 5+ days late: send SMS reminder
    5. If 15+ days late: escalate to legal
    6. Record payments in Supabase
    7. Post to Slack: "Collected: $6,000/6,000 (100%)"
  
  Output:
    - Stripe: Charge customers
    - Email/SMS: Reminders if late
    - Supabase: Payment ledger
    - Slack: Collection status

LOOP 2: /property-maintenance
  Runs: Daily (as requests come in)
  
  Steps:
    1. Get open maintenance requests
    2. Prioritize: emergency (24h), urgent (5d), routine (30d)
    3. Get vendor quotes
    4. If <$500: approve auto
    5. If >$500: escalate for approval
    6. Schedule vendor, verify completion
    7. Record: cost, category, completion date
    8. Post to Slack updates as completed
  
  Output:
    - Vendor coordination: Quotes, POs, scheduling
    - Supabase: Maintenance log
    - Slack: Maintenance updates

LOOP 3: /property-expenses
  Runs: Monthly (day 15)
  
  Steps:
    1. Collect monthly expenses: mortgage, tax, insurance, utilities, maintenance
    2. Process payments (ACH, checks)
    3. Calculate OCR: expenses / rent
    4. Update P&L
    5. Post to Slack: "Rent: $6K, Expenses: $4.8K, Net: $1.2K, OCR: 81%"
  
  Output:
    - Payments: Processed to vendors
    - Supabase: Monthly P&L
    - Slack: Financial summary
```

**Deliverable:** All 9 loop scripts written + documented  
**Effort:** 2-3 hours  
**Owner:** Claude (me)

---

### **WEEK 2: Testing (C) + Deployment (D)**

#### **OPTION C: TEST OPS-001 LOOPS**

**Goal:** Validate all 3 OPS-001 loops work before scaling to others

**C.1 Manual Test Runs (Day 6-7)**

```
TEST LOOP 1: /staffing-matching-engine
  Setup:
    - Create 5 test contractors in Supabase (different skills, rates)
    - Create 3 test venture openings
    - Set contractor status = 'available'
  
  Execute:
    - Run: /loop 1d /staffing-matching-engine
    - Check: ClickUp has 3-5 new tasks
    - Check: Slack message posted with matches
    - Verify: Tasks have contractor name, skills, rate
  
  Pass/Fail: ___

TEST LOOP 2: /contractor-payroll (simulate 2 weeks)
  Setup:
    - Create time logs for 3 contractors (100 hours each @ $100/hr)
    - Expected payroll: $30,000 total
  
  Execute:
    - Run: /loop 2w /contractor-payroll
    - Check: Stripe transfers initiated for $30K
    - Check: Supabase payroll table has 3 entries
    - Check: Slack message shows "$30,000 paid"
    - Verify: Email confirmations sent to contractors
  
  Pass/Fail: ___

TEST LOOP 3: /utilization-analytics (simulate 7 days data)
  Setup:
    - Create time logs: Contractor A (70h), B (90h), C (40h)
    - Contractor capacity: 100h/week each
    - Utilization: A=70%, B=90%, C=40%
  
  Execute:
    - Run: /loop 1d /utilization-analytics
    - Check: Slack shows "1 optimal (90%), 1 underutilized (70%), 1 critical (40%)"
    - Check: ClickUp task created for contractor C "Find placement"
    - Check: Alert for contractor B if overutilized
  
  Pass/Fail: ___
```

**C.2 Validation Checklist (Day 7)**

```
OPS-001 Loops Status:
  ☑ Matching loop finds qualified contractors: __YES__ / NO
  ☑ Payroll loop calculates correctly: __YES__ / NO
  ☑ Utilization loop flags under/over: __YES__ / NO
  ☑ All Slack posts are readable: __YES__ / NO
  ☑ All ClickUp tasks are actionable: __YES__ / NO
  ☑ All Supabase inserts are correct: __YES__ / NO

Issues found & fixed:
  - Issue 1: _______________
  - Issue 2: _______________

Ready for deployment? __YES__ / NO → If NO, debug & retest
```

**Deliverable:** OPS-001 validated + test report  
**Effort:** 3-4 hours  
**Owner:** Claude (me) executes, you review

---

#### **OPTION D: FULL DEPLOYMENT**

**Goal:** Enable all 9 loops and create dashboards

**D.1 Enable OPS-001 Loops (Day 8)**

```
Activate:
  ✓ /loop 1d /staffing-matching-engine (9 AM daily)
  ✓ /loop 2w /contractor-payroll (Fridays 5 PM, bi-weekly)
  ✓ /loop 1d /utilization-analytics (10 AM daily)
  ✓ /loop 1w /quality-feedback-loop (Friday 3 PM)
  ✓ /loop 1d /staffing-pipeline (4 PM daily)
  ✓ /loop 1w /venture-staffing-needs (Monday 9 AM)

Status: OPS-001 LIVE ✅
Monitor: Slack #ops-001-staffing (daily)
Owner: You (review Slack daily, respond to escalations)
```

**D.2 Enable CON-001 Loops (Day 8-9)**

```
Activate (after test validation):
  ✓ /loop 1d /construction-opportunities (8 AM daily)
  ✓ /loop 1d /construction-daily-standup (4 PM daily)
  ✓ /loop 1w /construction-billing (Friday 5 PM)
  ✓ /loop 2w /subcontractor-scheduling (bi-weekly)
  ✓ /loop 1m /equipment-utilization (1st of month)
  ✓ /loop 3m /safety-compliance (quarterly)

Status: CON-001 LIVE ✅
Monitor: Slack #con-001-construction (daily)
Owner: You (review Slack daily, manage bid decisions)
```

**D.3 Enable RE-001 Loops (Day 9-10)**

```
Activate (after test validation):
  ✓ /loop 1m /tenant-rent-collection (1st of month)
  ✓ /loop 1d /property-maintenance (daily as needed)
  ✓ /loop 1m /property-expenses (15th of month)
  ✓ /loop 3m /property-valuation (quarterly)
  ✓ /loop 1y /lease-renewal (60 days before expiry)
  ✓ /loop 1y /capital-planning (January 1st)

Status: RE-001 LIVE ✅
Monitor: Slack #re-001-property (as needed)
Owner: You (monthly expense review, decision on capital)
```

**D.4 Grafana Dashboards (Day 10-11)**

```
Dashboard 1: OPS-001 Staffing
  - Utilization %: Bar chart (daily, 7-day avg, 30-day avg)
  - Placement success rate: % that last >30 days
  - Payroll status: Last payment amount, next due date
  - Pipeline value: $ of open opportunities

Dashboard 2: CON-001 Construction
  - Active projects: Count, % on-time, % on-budget
  - Pipeline opportunities: Count, $ value
  - Bid success rate: % of bids won
  - Project margins: Average % margin

Dashboard 3: RE-001 Property
  - Occupancy %: Units occupied / total units
  - Rent collection status: Collected, late, disputed
  - OCR (operating cost ratio): Expenses / Revenue %
  - Portfolio appreciation: YoY % increase
```

**Deliverable:** All 9 loops running + 3 live dashboards  
**Effort:** 2-3 hours  
**Owner:** Claude (me) deploys + creates dashboards

---

## TIMELINE AT A GLANCE

| Phase | Dates | Activity | Owner | Deliverable |
|-------|-------|----------|-------|-------------|
| **B** | Jun 10-12 | Infrastructure (Supabase, Slack, ClickUp, HubSpot) | Claude | All systems ready |
| **A** | Jun 10-14 | Write 9 loop scripts (OPS-001, CON-001, RE-001) | Claude | 9 scripts + docs |
| **C** | Jun 15-16 | Test OPS-001 loops manually | Claude + You | OPS-001 validated |
| **D** | Jun 17-21 | Deploy all 9 loops + dashboards | Claude | All loops LIVE + monitored |
| **Live** | Jun 22-28 | Monitor + tweak loops based on real data | You + Claude | Fully operational |

**Total effort:** ~20-25 hours over 2 weeks  
**Go-live:** June 24, 2026  
**Fully stable:** June 28, 2026

---

## SUCCESS METRICS

### OPS-001 (Staffing) Success
- ✅ 5-10 contractor-venture matches found daily
- ✅ 100% on-time payroll (bi-weekly, <3 day processing)
- ✅ Average contractor utilization > 75%
- ✅ Contractor NPS > 60
- ✅ 0 missed payment deadlines

### CON-001 (Construction) Success
- ✅ 15-25 opportunities captured per week
- ✅ 10+ active projects tracked daily
- ✅ 80%+ projects deliver on-time
- ✅ 80%+ projects deliver on-budget
- ✅ Invoice accuracy > 99%

### RE-001 (Property) Success
- ✅ 100% rent collected by day 10 of month
- ✅ Maintenance requests resolved within SLA
- ✅ Monthly P&L updated automatically (by day 20)
- ✅ Operating Cost Ratio < 65% (improved from 81%)

---

## NEXT IMMEDIATE STEPS

**Today (June 10):**
1. ✅ You approve this roadmap
2. ➡️ I start OPTION B (infrastructure build) — 2-3 hours
3. ➡️ I start OPTION A (loop scripts) — 2-3 hours

**Tomorrow (June 11):**
4. ➡️ I finish all scripts
5. ➡️ You review + approve
6. ➡️ I begin OPTION C (testing)

**By June 16:**
7. ➡️ OPS-001 loops validated
8. ➡️ Ready to deploy

**By June 24:**
9. ➡️ All 9 loops LIVE
10. ➡️ You monitoring dashboards

---

**Approval:** Ready to proceed with A+B+C+D? ☑️ YES / ☐ NO

If YES → I begin infrastructure + scripts immediately.
