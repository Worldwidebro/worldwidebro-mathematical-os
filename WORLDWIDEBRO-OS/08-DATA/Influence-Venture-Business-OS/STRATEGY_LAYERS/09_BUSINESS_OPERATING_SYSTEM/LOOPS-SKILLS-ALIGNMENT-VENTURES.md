# LOOPS ↔ SKILLS ALIGNMENT + SECTOR-SPECIFIC OPERATIONS
## How Automation Works Across Ventures, Staffing, Construction & Real Estate

**Date:** 2026-06-10  
**Focus:** Connecting loops (WHEN) + skills (HOW) + ventures (WHAT)

---

## PART 1: LOOPS vs SKILLS — How They Align

### What's the Difference?

| Aspect | Loops | Skills |
|--------|-------|--------|
| **Purpose** | Execute on recurring intervals | Define HOW to execute something |
| **Trigger** | Time-based (daily, hourly, on-demand) | User invokes OR called by loop |
| **Example** | `/loop 1d /venture-health-check` | `/code-review` (reviews code) |
| **Duration** | Continuous (enabled/disabled) | Single execution (completes) |
| **Workflow** | Runs autonomously | Can be manual or automated |

### The Alignment Model

```
SKILL (Process Definition)
  ↓ (invoked by)
LOOP (Time-based Trigger)
  ↓ (executes using)
MCP TOOLS (Supabase, Slack, GitHub, ClickUp, HubSpot, Stripe)
  ↓ (updates)
VENTURE DATA (health score, metrics, tasks)
```

### Real Example: BW-001 Customer Feedback Loop

**Scenario:** BW-001 (Lash Extension Studio) needs daily customer feedback

```
SKILL: /customer-feedback-collection
  Input: venture_id = BW-001
  Process:
    1. Query Supabase for recent customers
    2. Send Google Form link via email
    3. Collect responses
    4. Store in Supabase
    5. Alert if NPS drops below 40
    6. Post summary to Slack #bw-001

LOOP: /loop 1d /customer-feedback-collection
  Runs skill once per day
  Parameters: venture_id=BW-001
  Output: Daily feedback summary in Slack

TOOLS USED:
  - Supabase: Read customer list, store responses
  - Google Forms: Collect feedback
  - Slack: Post summary
  - Email: Send Google Form link
```

### How Skills are Reused

Same skill, many ventures:

| Skill | Ventures Using It |
|-------|-------------------|
| `/subscription-billing` | All SaaS ventures (50+) |
| `/revenue-tracking` | All ventures (170+) |
| `/team-standup` | All ventures with teams (100+) |
| `/payroll-processing` | Service + Staffing ventures (15+) |

---

## PART 2: VENTURE STAFFING (OPS-001)

**OPS-001:** Venture Staffing Operations  
**Business Model:** B2B contractor matching + fulfillment  
**Stage:** MVP (development)  
**Revenue:** Commission + markup on billable hours

---

### OPS-001 Core Purpose

Match contractors to ventures' staffing needs, manage placements, process payroll.

**Key Stakeholders:**
- **Contractors:** Service providers (developers, designers, project managers)
- **Ventures:** Internal ventures + external clients needing staff
- **Revenue:** % of billable hours or fixed retainer per venture

**Key Metrics:**
- Utilization %: % of contractor hours billable (target: 80%)
- Placement success: % lasting 30+ days (target: 85%+)
- Venture satisfaction: NPS of ventures using staffing
- Contractor satisfaction: NPS of contractors

---

### OPS-001 Core Loops (6 essential)

#### 1. DAILY CONTRACTOR-VENTURE MATCHING
```
/loop 1d /staffing-matching-engine venture_id=OPS-001

Finds: Best contractor for each venture need
Inputs: Available contractors + venture openings
Outputs: Match suggestions to ClickUp
KPI: 5-10 matches/day with 50%+ conversion
```

#### 2. BI-WEEKLY PAYROLL PROCESSING
```
/loop 2w /contractor-payroll venture_id=OPS-001

Calculates: Hours × rate for each contractor
Pays: ACH transfers to contractors (within 7 days)
Outputs: Payment confirmations + payroll ledger
KPI: 100% on-time payment, <3 day processing
```

#### 3. DAILY UTILIZATION TRACKING
```
/loop 1d /utilization-analytics venture_id=OPS-001

Measures: % of contractor hours billable
Segments: Optimal (75-90%), Under (need placement), Over (burnout risk)
Outputs: Daily dashboard + Slack alert
KPI: Avg 80% utilization, <2 idle contractors
```

#### 4. WEEKLY QUALITY FEEDBACK
```
/loop 1w /quality-feedback-loop venture_id=OPS-001 day=Friday

Surveys: Venture + contractor on assignment quality
Collects: 1-5 ratings, NPS, issues
Escalates: If either party gives <3
Outputs: Weekly quality score
KPI: Venture NPS > 50, Contractor NPS > 50
```

#### 5. DAILY SALES PIPELINE
```
/loop 1d /staffing-pipeline venture_id=OPS-001

Tracks: Open placements in HubSpot
Stages: In conversation → Negotiating → Closing → Placed
Alerts: If stuck >14 days
Outputs: Pipeline summary to Slack
KPI: 8-12 active deals, 60%+ win rate
```

#### 6. WEEKLY VENTURE STAFFING NEEDS UPDATE
```
/loop 1w /venture-staffing-needs venture_id=OPS-001 day=Monday

Checks: Every venture's staffing status
Asks: Any new openings? Budget? Timeline?
Updates: Supabase with hiring needs
Feeds: Results into daily matching loop
Outputs: Match suggestions based on fresh needs
KPI: 80%+ of ventures have known hiring status
```

---

### OPS-001 Daily Dashboard Metric

```
🎯 STAFFING OPERATIONS — Daily Snapshot

Placements:
  • Active assignments: 12
  • Utilization (avg): 78%
  • Quality score: 4.2/5 stars

Financial:
  • Contractor payroll (this cycle): $47,250
  • Venture revenue (estimated): $56,000
  • Net margin: 16%

Health:
  • Contractor NPS: 62
  • Venture NPS: 58
  • Escalations today: 0
  • Next payroll: 4 days
```

---

## PART 3: CONSTRUCTION SECTOR (CON-001 through CON-020)

**Ventures:** 20 construction companies (general contractors, specialty trades)  
**Business Model:** Project-based service (lump sum or time + materials)  
**Strategy:** Partnership-first (integrate with platforms, government contracts, subcontractor networks)  
**Revenue:** Labor markup (100-150%), material markup (20-30%)

---

### Construction Ecosystem

```
DEMAND (Where work comes from):
  ├── Government contracts (SAM.gov, NCDOT, Charlotte CIP)
  ├── Existing platforms (HomeAdvisor, Angi, Zillow, Nextdoor)
  ├── Direct customers (word-of-mouth, local reputation)
  └── Subcontractor referrals

VALUE CHAIN:
  Bid → Estimate → Schedule → Coordinate → Build → Inspect → Invoice

MONETIZATION:
  Labor (70% of revenue) + Materials (20%) + Equipment (5%) + Contingency (5%)
  Typical margin: 12-18% net profit
```

---

### Construction Core Loops (6 essential)

#### 1. DAILY OPPORTUNITY MONITORING
```
/loop 1d /construction-opportunities

Monitors: SAM.gov, NCDOT, Charlotte CIP, HomeAdvisor, Angi, Zillow
Alerts: If new project matches capability + budget > $50K
Outputs: HubSpot deal creation + ClickUp bid task
KPI: 15-25 opportunities/week, 50%+ qualified
```

#### 2. BI-WEEKLY SUBCONTRACTOR SCHEDULING
```
/loop 2w /subcontractor-scheduling

For each active project: Identify needed trades
Schedule: Roofing, electrical, plumbing, HVAC, etc.
Checks: Availability, rate, insurance, preferred subs
Outputs: PO + schedule to subcontractors
KPI: 85%+ sub utilization, 90%+ schedule adherence
```

#### 3. DAILY PROJECT STATUS UPDATES
```
/loop 1d /construction-daily-standup

Collects: Site photo, hours, tasks, issues, safety
Updates: % complete, budget spent, timeline
Alerts: Behind >3 days, over budget >10%, safety incident
Outputs: ClickUp update + Slack post
KPI: 85%+ on-time, 80%+ on-budget, 0 safety incidents
```

#### 4. WEEKLY INVOICE & PAYMENT
```
/loop 1w /construction-billing day=Friday

Creates: Invoice from time logs + materials
Tracks: Customer payment status (send reminders if overdue)
Pays: Subcontractors within 7 days of customer payment
Outputs: Invoices sent + payments processed
KPI: <45 days sales outstanding, 100% sub payment on-time
```

#### 5. MONTHLY EQUIPMENT MANAGEMENT (if using CON-005)
```
/loop 1m /equipment-utilization day=1

Optimizes: Equipment allocation across projects
Tracks: Rental costs per project
Manages: Return schedule + maintenance
Outputs: Equipment ledger + cost summary
KPI: 90%+ utilization, <5% rental cost
```

#### 6. QUARTERLY COMPLIANCE & SAFETY
```
/loop 3m /safety-compliance day=1

Audits: OSHA compliance, PPE, incident reports, training
Verifies: Worker's comp, general liability, bonding
Checks: Specialty licenses (electrical, plumbing)
Outputs: Compliance audit report
KPI: 100% compliance, 0 OWASP violations, 0 incidents
```

---

### Construction Revenue Example

Typical project: $50,000 renovation

```
REVENUE:
  Labor (3 crew × $60/hr × 300 hrs)           $54,000
  Materials (at markup)                       $18,000
  Subcontractors (at margin)                  $12,000
  Equipment rental                             $3,000
  ──────────────────────────────────────────
  TOTAL REVENUE                               $87,000

COSTS:
  Crew labor                                 ($36,000)
  Subcontractor (cost, no markup)            ($10,000)
  Materials (cost, no markup)                ($12,000)
  Equipment (cost)                            ($3,000)
  Overhead (10%)                              ($8,700)
  ──────────────────────────────────────────
  TOTAL COST                                 ($69,700)

GROSS PROFIT:                                 $17,300
GROSS MARGIN:                                 19.9%
```

---

### Construction Daily Dashboard

```
🏗️ CONSTRUCTION — Daily Snapshot

Projects:
  • Active: 5
  • On-track: 3
  • Behind schedule: 1 (flag for acceleration)
  • Delayed (weather): 1

Financial:
  • Revenue invoiced: $145,000
  • Payments received: $98,000 (67% collected)
  • Subcontractor payables: $64,000
  • Net cash position: Positive $34,000

Safety:
  • Incidents: 0
  • Compliance: 100%
  • PPE checks: Passed

Next 7 days:
  • Roof work: Project A (on schedule)
  • Electrical trade: Project C (needs scheduling)
  • Inspection: Project B (day 5)
```

---

## PART 4: REAL ESTATE SECTOR (RE-001, RE-002, etc.)

**Ventures:** Property holdings (rental income) + flips (appreciation)  
**Business Models:**
1. Rental: Own property → Rent to tenant → Monthly recurring income
2. Flip: Buy low → Renovate → Sell high → Lump sum profit
3. Services: Property management for others

**Key Metrics:**
- Occupancy %: % of units rented (target: 95%+)
- OCR (Operating Cost Ratio): Expenses / Revenue (target: <60%)
- Days to collect rent: (target: <10 days)
- Appreciation: Annual value increase (target: 3-5%)

---

### Real Estate Core Loops (6 essential)

#### 1. MONTHLY RENT COLLECTION & TENANT MANAGEMENT
```
/loop 1m /tenant-rent-collection day=1

Charges: Rent via ACH auto-pay
Follows up: Reminders if overdue (day 5, 10, 15)
Late fees: Apply after 15 days
Refunds: Security deposit minus damages within 30 days
Outputs: Supabase payment ledger + Slack summary
KPI: 98%+ collection rate, <10 days to collect
```

#### 2. MONTHLY EXPENSE TRACKING & MAINTENANCE
```
/loop 1m /property-maintenance day=5

Tracks: Tenant maintenance requests
Prioritizes: Emergency (24h), Urgent (5 days), Routine (30 days)
Vendors: Get quotes, approve <$500, escalate >$500
Outputs: Maintenance log + Slack cost summary
KPI: Maintenance <8% of rent, on-time resolution
```

#### 3. MONTHLY EXPENSE PAYMENTS & LEDGER
```
/loop 1m /property-expenses day=15

Collects: Mortgage, property tax, insurance, utilities, HOA
Processes: Payments to vendors
Updates: Monthly P&L
Outputs: Expense ledger + cash flow dashboard
KPI: Operating expenses <60% of rent, >3 mo cash reserve
```

#### 4. QUARTERLY PROPERTY VALUATION & TAX PLANNING
```
/loop 3m /property-valuation day=1

Updates: Property market value (Zillow, comparables)
Tracks: Appreciation YoY
Calculates: Depreciation for tax deductions
Plans: 1031 exchanges if needed
Outputs: Portfolio valuation report
KPI: 3-5%/year appreciation, optimize tax deductions
```

#### 5. ANNUAL LEASE RENEWAL & RENT ADJUSTMENT
```
/loop 1y /lease-renewal day=60-before-expiry

Sends: Renewal notice 60 days before expiry
Proposes: Market-rate rent
Collects: Tenant response by day 30
If moving out: Begin marketing (Zillow, Facebook, Nextdoor)
Outputs: Updated leases or vacancy marketing
KPI: 80%+ renewal rate, <5% vacancy
```

#### 6. ANNUAL PROPERTY INSPECTION & CAPITAL PLANNING
```
/loop 1y /capital-planning day=1

Inspects: Roof, HVAC, plumbing, appliances, systems
Identifies: Major expenses (next 3-5 years)
Budgets: Roof ($12K in 5 yrs), HVAC ($6K in 3 yrs)
Reserve fund: Build capital reserve ($500/mo)
Outputs: 5-year capital plan
KPI: Reserve fund >$50K, no deferred maintenance
```

---

### Real Estate Revenue Example

3 rental properties:

```
MONTHLY REVENUE:
  Unit 1: $2,000/mo rent
  Unit 2: $2,200/mo rent
  Unit 3: $1,800/mo rent
  ──────────────────────
  TOTAL: $6,000/month ($72,000/year)

MONTHLY EXPENSES:
  Mortgages (3 × $1,200):            ($3,600)
  Property taxes:                      ($400)
  Insurance:                           ($300)
  Maintenance reserve:                 ($400)
  HOA fees:                            ($150)
  ──────────────────────
  TOTAL: ($4,850/month) ($58,200/year)

NET CASH FLOW:                        $1,150/month ($13,800/year)
Operating Cost Ratio (OCR):           81% (too high, target <60%)

PLUS: Depreciation tax deduction
  If financed:depreciation ~$6,000/year (tax shield)
  Real return (with tax benefit): ~$19,800/year
```

---

### Real Estate Daily Dashboard

```
🏠 REAL ESTATE — Daily Snapshot

Properties: 3 units
  • Occupied: 3/3 (100%)
  • Avg tenure: 2.8 years
  • Tenant NPS: 65

Monthly (running):
  • Rent collected: $6,000
  • Expenses: $4,850
  • Net: $1,150
  • OCR: 81% (⚠️ high, target 60%)

Portfolio Health:
  • Total value: $580,000
  • Equity: $180,000 (31%)
  • YoY appreciation: +$24,000 (+4.1%)

Upcoming:
  • Unit 2 lease renewal: July 30 (60 days)
  • Annual inspection: June 30
  • HVAC maintenance: Due Q3
```

---

## SUMMARY: LOOPS BY SECTOR

### OPS-001 (Staffing)
- **6 loops** running daily/bi-weekly
- **Primary focus:** Utilization %, payment on-time, placement success
- **Tools:** Supabase, ClickUp, Stripe, Slack, HubSpot
- **Revenue driver:** Billable hours × markup

### Construction (CON-001 to CON-020)
- **6 loops** running daily/weekly/monthly
- **Primary focus:** Schedule adherence, profit margin, safety
- **Tools:** Supabase, ClickUp, HomeAdvisor/Angi, Slack, HubSpot
- **Revenue driver:** Project scope × margin

### Real Estate (RE-001+)
- **6 loops** running monthly/quarterly/annually
- **Primary focus:** Occupancy %, cash flow, appreciation
- **Tools:** Supabase, Slack, Payment processing, Tax software
- **Revenue driver:** Rent - Expenses = Net cash flow + appreciation

---

## NEXT STEPS TO ACTIVATE

**Week 1: Pick first ventures**
- OPS-001 (1 staffing venture)
- CON-001 (1 construction venture)
- RE-001 (1 real estate venture)

**Week 2-3: Build 3 core loops per venture**
- Daily health check (all)
- Revenue/metric tracking (daily or monthly)
- Team/ops summary (Slack post)

**Week 4: Test loops manually**
- Run `/loop 1d /skill-name` for 7 days
- Verify outputs (Slack posts, ClickUp updates)
- Adjust intervals/parameters

**Week 5+: Automate via schedule**
- Move to `/schedule` skill for recurring runs
- Expand to all ventures in each sector
- Scale loops across 712 ventures

---

**Questions:**
- OPS-001: Start with matching + payroll loops?
- Construction: Start with general contracting (CON-001) or one trade (CON-009 roofing)?
- Real estate: Start with 1 property or portfolio of 3?
