---
name: OPERATIONAL-ARCHITECTURE
title: 'OPERATIONAL ARCHITECTURE: Worldwidebro Holdings Orchestration System'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# OPERATIONAL ARCHITECTURE: Worldwidebro Holdings Orchestration System

**Purpose:** Define the complete database schema, positions, contract types, task structures, and relationship maps to turn 687 ventures into a controlled execution network.

**Status:** Blueprint (2026-05-08)

---

# TIER 1: CORE DATABASE TABLES (Supabase)

These are the source-of-truth tables for the entire system.

## 1. VENTURES (Product Definition)

```sql
ventures (
  id UUID PRIMARY KEY,
  sector VARCHAR,
  venture_code VARCHAR UNIQUE,
  name VARCHAR,
  product_description TEXT,
  service_type VARCHAR,
  target_market TEXT,
  price_point DECIMAL,
  revenue_potential VARCHAR (low/medium/high),
  stage VARCHAR (pre-launch/mvp/scaling/mature),
  lead_source VARCHAR (network/social/referral),
  priority_tier INTEGER (1-5, where 1 = urgent),
  affiliate_network BOOLEAN,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)

Example:
- CON-001: Foundation Repair Service
- BW-087: Beauty Subscription Box
- TECH-042: SaaS HR Platform
```

---

## 2. CLIENTS (Demand Side)

```sql
clients (
  id UUID PRIMARY KEY,
  name VARCHAR,
  email VARCHAR,
  phone VARCHAR,
  industry VARCHAR,
  company_size VARCHAR,
  location VARCHAR,
  pain_point TEXT,
  budget_range VARCHAR,
  decision_maker BOOLEAN,
  lead_source VARCHAR (network/social/cold),
  lead_quality VARCHAR (hot/warm/cold),
  contacted_date DATE,
  last_contact_date DATE,
  status VARCHAR (prospect/qualified/negotiating/closed/lost),
  created_at TIMESTAMP,
  contact_owner_id UUID REFERENCES positions
)

Example:
- John Smith, CEO Construction Firm, pain: crew scheduling
- Sarah Chen, CMO Tech, pain: marketing automation
```

---

## 3. VENDORS / AFFILIATES (Supply Side)

```sql
vendors (
  id UUID PRIMARY KEY,
  vendor_name VARCHAR,
  vendor_type VARCHAR (contractor/agency/freelancer/staffing),
  specialization VARCHAR,
  location VARCHAR,
  contact_name VARCHAR,
  email VARCHAR,
  phone VARCHAR,
  rate_card JSONB,
  capacity_available BOOLEAN,
  capacity_units INTEGER (how many concurrent projects),
  reliability_score DECIMAL (0-100),
  insurance_status VARCHAR (active/expired/none),
  past_performance_rating DECIMAL (0-5),
  affiliation_agreement BOOLEAN,
  msa_signed_date DATE,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)

Example:
- Elite Electric (contractor, electricians, reliability: 94)
- Phoenix PM Group (agency, project managers, capacity: 5 projects)
```

---

## 4. CONTRACTS (Relationship Enforcement)

```sql
contracts (
  id UUID PRIMARY KEY,
  contract_type VARCHAR (msa/work_order/vendor_agreement/subcontractor/sla),
  venture_id UUID REFERENCES ventures,
  client_id UUID REFERENCES clients (for client contracts),
  vendor_id UUID REFERENCES vendors (for vendor contracts),
  contract_code VARCHAR,
  status VARCHAR (draft/signed/active/completed/terminated),
  contract_document_url TEXT,
  start_date DATE,
  end_date DATE,
  value DECIMAL,
  payment_terms VARCHAR (upfront/milestone/net-30),
  scope_of_work TEXT,
  deliverables JSONB,
  sla_metrics JSONB,
  penalty_terms TEXT,
  insurance_requirements TEXT,
  signed_date DATE,
  signed_by_id UUID REFERENCES positions,
  created_at TIMESTAMP
)

Example:
- MSA-ELITE-ELEC-001: Master Service Agreement with electrician
- WO-CON-001-2026-Q2: Work Order for CON-001, Q2 2026
```

---

## 5. WORK ORDERS (Per-Project Execution)

```sql
work_orders (
  id UUID PRIMARY KEY,
  wo_number VARCHAR UNIQUE,
  contract_id UUID REFERENCES contracts,
  venture_id UUID REFERENCES ventures,
  client_id UUID REFERENCES clients,
  vendor_id UUID REFERENCES vendors,
  project_name VARCHAR,
  scope_of_work TEXT,
  deliverables JSONB,
  start_date DATE,
  end_date DATE,
  price DECIMAL,
  cost DECIMAL,
  margin DECIMAL,
  status VARCHAR (assigned/in_progress/delayed/completed/paid),
  assigned_to_id UUID REFERENCES positions,
  approved_by_id UUID REFERENCES positions,
  created_at TIMESTAMP,
  completion_date DATE,
  payment_received_date DATE
)

Example:
- WO-2026-0001: Electrician scope for Foundation Repair Project
- WO-2026-0042: PM services for SaaS launch
```

---

## 6. PROJECTS (Multi-Vendor Execution)

```sql
projects (
  id UUID PRIMARY KEY,
  project_code VARCHAR,
  venture_id UUID REFERENCES ventures,
  client_id UUID REFERENCES clients,
  name VARCHAR,
  scope TEXT,
  start_date DATE,
  end_date DATE,
  status VARCHAR (planning/active/delayed/completed/closed),
  budget DECIMAL,
  spent DECIMAL,
  margin DECIMAL,
  primary_pm_id UUID REFERENCES positions,
  stage VARCHAR (bidding/procurement/execution/closeout),
  vendors_assigned JSONB (array of vendor_ids),
  created_at TIMESTAMP,
  completed_at DATE
)

Example:
- PRJ-2026-CON-001: Foundation Repair for Smith Construction
  Vendors: Elite Electric (WO-0001), Plumb Pro (WO-0002), HVAC Solutions (WO-0003)
```

---

## 7. POSITIONS / ROLES (Human & Agent Structure)

```sql
positions (
  id UUID PRIMARY KEY,
  position_code VARCHAR,
  position_name VARCHAR,
  position_type VARCHAR (human/agent/hybrid),
  department VARCHAR,
  reports_to_id UUID REFERENCES positions,
  authority_level INTEGER (1-10, where 10 = CEO),
  approval_threshold DECIMAL (max authority to approve),
  responsibilities JSONB,
  vendor_coverage JSONB (which vendors report to this person),
  client_coverage JSONB (which clients are this person's relationships),
  active BOOLEAN,
  created_at TIMESTAMP
)

Example Positions:
- POS-CEO-001: CEO / Founder (human, authority: 10)
- POS-SALES-001: Head of Sales (human, authority: 7, approval_threshold: $50K)
- POS-AGENT-QWN-BEAUTY: qwen-beauty-wellness agent (agent, authority: 6)
- POS-PM-CONSTRUCTION: Construction PM (human, authority: 5)
```

---

## 8. RELATIONSHIPS (Contact Maps)

```sql
relationships (
  id UUID PRIMARY KEY,
  source_type VARCHAR (client/vendor/position),
  source_id UUID,
  target_type VARCHAR (venture/position/vendor/client),
  target_id UUID,
  relationship_type VARCHAR (owns/manages/contacts/reports_to/assigned_to/leads),
  active BOOLEAN,
  created_at TIMESTAMP
)

Example:
- John Smith (client) → CON-001 (venture) [interested in]
- qwen-beauty-wellness (agent) → BW-087 (venture) [manages]
- Elite Electric (vendor) → Foundation Repair Project [assigned to]
```

---

## 9. LEADS (Deal Pipeline Bridge)

```sql
leads (
  id UUID PRIMARY KEY,
  lead_code VARCHAR,
  client_id UUID REFERENCES clients,
  venture_id UUID REFERENCES ventures,
  lead_status VARCHAR (new/contacted/interested/qualified/negotiating/closed/lost),
  lead_quality VARCHAR (hot/warm/cold),
  discovery_call_date DATE,
  proposal_sent_date DATE,
  negotiation_start_date DATE,
  close_date DATE,
  deal_value DECIMAL,
  contact_owner_id UUID REFERENCES positions,
  notes TEXT,
  created_at TIMESTAMP
)

Example:
- LEAD-2026-0001: John Smith → CON-001, deal_value: $150K
```

---

## 10. REVENUE TRACKING (Finance)

```sql
revenue_transactions (
  id UUID PRIMARY KEY,
  work_order_id UUID REFERENCES work_orders,
  venture_id UUID REFERENCES ventures,
  client_id UUID REFERENCES clients,
  transaction_type VARCHAR (invoice/payment/deposit),
  amount DECIMAL,
  status VARCHAR (pending/paid/overdue),
  invoice_date DATE,
  due_date DATE,
  paid_date DATE,
  payment_method VARCHAR,
  created_at TIMESTAMP
)
```

---

# TIER 2: CLICKUP TASK STRUCTURE

ClickUp is your **accountability + execution layer**. Maps to the database.

## List Structure

### 1. COMPANY OPERATIONS (Org Management)
Lists under this folder:
- **Positions & Authority** — Define each role, approval authority, coverage
- **Vendors / Affiliates** — Onboard, score, contract management
- **Clients / Accounts** — Relationship management, history, renewal
- **Contracts** — MSAs, work orders, SLAs (status tracking)

### 2. SALES & NEGOTIATION
- **Leads** — New prospects (from network, social, referral)
- **Discoveries** — Scheduled calls, qualification scores
- **Negotiations** — Active deals, objection handling, close tracking
- **Closed Deals** — Won revenue, post-close follow-up, upsells

### 3. EXECUTION BY SECTOR
*For each of 16 sectors:*
- **[Sector] Operations** — Ventures in this sector, active projects
- **[Sector] Vendors** — Assigned subcontractors, performance tracking
- **[Sector] Revenue** — MRR target, Stripe product IDs, revenue tracking

### 4. PROJECT MANAGEMENT
- **Active Projects** — All in-flight work (venue, status, % complete)
- **Work Orders** — Granular unit of work (vendor assigned, deadline, margin)
- **Procurement** — Vendor selection, RFQs, purchase orders
- **Quality & Compliance** — Inspections, safety, permits

### 5. FINANCIAL
- **Invoicing** — Work orders → invoices, payment tracking
- **Vendor Payables** — What we owe contractors (milestone-based)
- **Cash Flow** — Projected revenue vs. actual, payables schedule
- **Monthly Close** — Revenue per venture, margin by sector

---

# TIER 3: POSITIONS & AUTHORITY STRUCTURE

## Core Positions

### LEADERSHIP
| Position | Authority | Responsibilities | Reports To |
|----------|-----------|------------------|-----------|
| **CEO / Founder** | 10 | Strategic direction, all approvals | Board |
| **COO / Operations** | 9 | Vendor mgmt, project coordination, QA | CEO |
| **CFO / Finance** | 9 | Revenue tracking, cash flow, payables | CEO |
| **Head of Sales** | 8 | Lead generation, client relationships, close | CEO |

### SECTOR MANAGERS (Human)
| Position | Authority | Coverage | Reports To |
|----------|-----------|----------|-----------|
| **Construction PM** | 6 | CON-001 through CON-087 | COO |
| **Tech Sales Lead** | 7 | TECH-001 through TECH-120 | Head of Sales |
| **Beauty & Wellness Manager** | 6 | BW-001 through BW-087 | COO |

### AGENTS (AI / Autonomous)
| Agent | Authority | Coverage | Supervisors |
|-------|-----------|----------|-------------|
| **qwen-beauty-wellness** | 5 | Beauty ventures, lead routing | Beauty & Wellness Manager |
| **qwen-construction** | 5 | Construction ventures, vendor coordination | Construction PM |
| **qwen-technology** | 5 | Tech ventures, project tracking | Tech Sales Lead |

### VENDOR COORDINATION
| Position | Authority | Role |
|----------|-----------|------|
| **Vendor Manager** | 5 | Onboard affiliates, manage MSAs, track performance |
| **Subcontractor Liaison** | 4 | Field coordination, quality checks, payment processing |

---

# TIER 4: TASK CATEGORIES & WORKFLOWS

## TASK TYPE 1: CLIENT ACQUISITION

**Owner:** Head of Sales + Sector Agents

**Workflow:**
```
New Lead (Client Contact Found)
    ↓
[Task 1] Warm Intro / Cold Outreach (email/call)
    ↓
[Task 2] Discovery Call Scheduled
    ↓
[Task 3] Needs Assessment (document pain point)
    ↓
[Task 4] Proposal Generated (venture product + pricing)
    ↓
[Task 5] Present & Handle Objections
    ↓
[Task 6] Contract Negotiation (terms, timeline, payment)
    ↓
[Task 7] Close & Sign
    ↓
[Task 8] Handoff to Execution
```

**ClickUp Tracking:**
- Task due date = call date
- Assigned to = sector agent or sales person
- Custom field: Deal Value
- Custom field: Close Probability

---

## TASK TYPE 2: VENDOR ACTIVATION

**Owner:** Vendor Manager + COO

**Workflow:**
```
Vendor Identified (potential subcontractor)
    ↓
[Task 1] Initial Outreach & Qualification
    ↓
[Task 2] Rate Card Negotiation
    ↓
[Task 3] MSA (Master Service Agreement) Created & Signed
    ↓
[Task 4] Insurance Verification
    ↓
[Task 5] Performance Baseline Established
    ↓
[Task 6] Added to Affiliate Network
```

**ClickUp Tracking:**
- Task due date = contract sign date
- Assigned to = Vendor Manager
- Custom field: Reliability Score
- Custom field: Capacity (units)

---

## TASK TYPE 3: PROJECT EXECUTION

**Owner:** Project PM + Vendors

**Workflow:**
```
Work Order Created (from client project)
    ↓
[Task 1] Select & Assign Vendor
    ↓
[Task 2] Scope & Deliverables Finalized
    ↓
[Task 3] Work Order Issued & Signed
    ↓
[Task 4] Vendor Begins Execution
    ↓
[Task 5] Progress Monitoring (daily/weekly check-ins)
    ↓
[Task 6] Quality Inspection
    ↓
[Task 7] Completion & Payment
    ↓
[Task 8] Post-Project Review
```

**ClickUp Tracking:**
- Task due date = milestone date
- Assigned to = vendor (externally tracked)
- Custom field: Work Order Value
- Custom field: Budget vs. Actual

---

## TASK TYPE 4: FINANCIAL CLOSE

**Owner:** CFO + Accountant

**Workflow:**
```
Month End Approaching
    ↓
[Task 1] All Invoices Issued
    ↓
[Task 2] All Payments Received (or aged AR tracked)
    ↓
[Task 3] Vendor Payables Processed
    ↓
[Task 4] Revenue Recognized by Sector
    ↓
[Task 5] Margin Calculated
    ↓
[Task 6] Cash Flow Projection Updated
```

**ClickUp Tracking:**
- Task due date = 5th of following month
- Assigned to = CFO
- Custom field: Total Revenue
- Custom field: Margin %

---

# TIER 5: CONTACT & RELATIONSHIP MAPS

## CLIENT → VENTURE MATCHING

```
Client Profile:
  Name: John Smith
  Industry: Construction
  Pain: Crew scheduling, invoicing, permits
  Budget: $100K+ / year
  Location: Texas

Match to Ventures:
  ✅ CON-001: Foundation Repair (can sell inspection services)
  ✅ CON-042: Project Management SaaS (solve his scheduling pain)
  ✅ TECH-055: Invoicing Platform (accounting pain)

Lead Routing:
  → qwen-construction agent (initial outreach)
  → Construction PM (relationship management)
  → Head of Sales (negotiation/close)

Expected Deal Value: $150K in Year 1
```

---

## VENDOR → VENTURE ASSIGNMENT

```
Vendor Profile:
  Name: Elite Electric
  Type: Contractor (electricians)
  Capacity: 3 concurrent projects
  Reliability: 94/100
  Rate: $85/hour

Assignment to Ventures:
  → CON-001: Foundation Repair (electrical work)
  → CON-042: Renovation Project (wiring)
  → CON-055: Commercial Build (electrical systems)

Monitoring:
  → Weekly status updates (ClickUp)
  → Quality inspections every 2 weeks
  → Payment: Milestone-based (every $25K completed)
  → Performance score: Track reliability, quality, timeliness
```

---

## POSITION → COVERAGE MAP

```
Position: Head of Sales
Reports To: CEO
Authority Level: 8
Approval Threshold: $50K

Coverage:
  - Clients: Sarah Chen (CMO), Mike Johnson (CFO), Linda Garcia (COO)
  - Ventures: TECH-001, TECH-042, TECH-087
  - Daily Tasks:
    • 5 outreach calls / day
    • 2 discovery calls / day
    • Weekly pipeline review
    • Monthly revenue forecast

KPIs:
  - Leads generated / month
  - Conversion rate (leads → deals)
  - Average deal size
  - Sales cycle time
```

---

# TIER 6: AGENT RESPONSIBILITIES

### qwen-beauty-wellness Agent

```
Autonomous Authority: 5/10 (escalates above $25K to human)
Coverage: All beauty & wellness ventures (BW-001 through BW-087)

Daily Tasks:
  1. Check ClickUp for new leads assigned to beauty sector
  2. Route leads to Beauty & Wellness Manager for warm intro
  3. Monitor active negotiations (remind on follow-up dates)
  4. Track vendor performance (salon partners, cosmetic suppliers)
  5. Generate weekly sector report (leads, closures, revenue)

Examples:
  - New lead: "Jane's Salon, needs booking system"
    → Agent flags to Beauty Manager
    → Agent suggests: BW-042 (Salon Booking Software)
    → Agent tracks if contacted in next 24 hours

  - Vendor issue: "Supplier delayed makeup shipment"
    → Agent alerts Vendor Manager
    → Agent tracks resolution

  - Deal closed: "$50K contract with 10 salons"
    → Agent updates revenue tracker
    → Agent schedules implementation kickoff
```

---

# TIER 7: DATA FLOWS

## Lead → Revenue Flow

```
1. NEW LEAD (ClickUp)
   Client found (network, social, referral)
   ↓
2. LEAD QUALIFICATION (Supabase: leads table)
   Is there a venture match?
   ↓
3. OUTREACH (ClickUp: Leads list)
   Email, call, warm intro
   ↓
4. DISCOVERY (ClickUp: Discoveries list)
   Document pain, budget, timeline
   ↓
5. PROPOSAL (Supabase: contracts table draft)
   Price, scope, timeline
   ↓
6. NEGOTIATION (ClickUp: Negotiations list)
   Terms, risk, payment structure
   ↓
7. CLOSE (Supabase: contracts table signed)
   Contract executed
   ↓
8. EXECUTION (Supabase: work_orders, projects)
   Vendor assigned, work begins
   ↓
9. REVENUE (Supabase: revenue_transactions)
   Invoice issued, payment received
```

---

## Vendor Assignment Flow

```
1. VENDOR IDENTIFIED (network, referral, cold outreach)
   ↓
2. QUALIFICATION (verify: insurance, performance, capacity)
   ↓
3. RATE NEGOTIATION (unit pricing, terms)
   ↓
4. MSA SIGNED (master agreement executed)
   ↓
5. WORK ASSIGNMENT (new project needs this vendor type)
   ↓
6. WORK ORDER ISSUED (scope, price, timeline, deliverables)
   ↓
7. EXECUTION (vendor performs work)
   ↓
8. INSPECTION (QA, completeness check)
   ↓
9. PAYMENT (based on milestone completion)
   ↓
10. PERFORMANCE REVIEW (update reliability score, capacity)
```

---

# TIER 8: TOOLS REQUIRED

## Supabase (Source of Truth)
- Ventures, Clients, Vendors, Contracts, Work Orders, Projects, Positions
- Revenue tracking
- Real-time queries via API

## ClickUp (Execution + Accountability)
- All task management
- Custom fields (deal value, vendor capacity, margin, etc.)
- Automation: lead created → assigned to agent
- Monthly reporting views

## n8n (Workflow Automation)
- ClickUp new lead → assign to agent
- Contract signed → create work order
- Invoice issued → payment tracking
- Vendor performance → update score

## Stripe (Payment Processing)
- Invoice payment tracking
- Subscription billing (if recurring ventures)
- Payables to vendors

## Claude + Local Agents (AI)
- Lead qualification
- Proposal generation
- Vendor selection
- Performance analysis
- Reporting

## Mac Studio + Tailscale (Infrastructure)
- Local execution
- Agent coordination
- Data sync with cloud

---

# NEXT: Implementation Priority

1. **Week 1:** Build Supabase tables (ventures, clients, vendors, positions)
2. **Week 2:** Configure ClickUp lists + custom fields
3. **Week 3:** Map existing contacts to database
4. **Week 4:** Set up first 3 sector agents
5. **Week 5:** First client acquisition cycle (end-to-end)
6. **Week 6:** Revenue tracking + monthly close process

---

**Status:** Blueprint ready. Waiting on user confirmation to build.
