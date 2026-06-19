# Worldwidebro Holdings: Operating System Roadmap (Revenue-First)

**Date:** 2026-06-17  
**Focus:** Turn structure into revenue  
**Horizon:** 90-day quick wins + 12-month scaling

---

## The Problem We're Solving

**Current state:** 704 ventures in 18 OPCOs with perfect structure but zero operational status.

**Solution:** Build an operating system that:
1. Tracks what's actually happening in each venture
2. Identifies revenue-generating ventures
3. Allocates capital & talent to winners
4. Eliminates zombie ventures
5. Scales what works

---

## Phase 1: Venture Inventory & Operational Status (Week 1)

**Goal:** Know exactly what we own, who owns it, and what it's worth.

### Deliverable: VENTURE_INVENTORY_MASTER.csv

```csv
venture_id,venture_name,opco,owner,status,revenue_ytd,monthly_burn,priority,90day_revenue_potential,notes
CON-001,LocalRoof Co,OPCO-Construction,antwuan-johns,Operating,$45000,$2000,HIGH,$15000,"5 active jobs, monthly contracts"
FIN-001,GenixBank,OPCO-Financial,contractor-1,Research,$0,$5000,MEDIUM,$0,"Product development, not live"
EC-001,E-Commerce Marketplace,OPCO-Marketplace,team-lead,Building,$8000,$10000,HIGH,$50000,"Beta testing with 50 vendors"
ST-001,Temp Agency,OPCO-Staffing,recruiter-lead,Operating,$32000,$1500,HIGH,$20000,"Growing, need more recruiters"
TECH-001,SaaS Platform,OPCO-Technology,dev-lead,Building,$0,$15000,MEDIUM,$5000,"MVP ready for launch"
...
```

### Status Categories
- **Idea** — Concept only, no work started
- **Research** — Market validation in progress
- **Building** — Product/service being built
- **Launching** — Ready to go live
- **Operating** — Active, generating revenue
- **Scaling** — Proven model, expanding
- **Acquired** — Acquisition completed
- **Archived** — Shut down or paused

### What This Reveals

Running this analysis on 704 ventures, expect:
- **5-10% Operating** (30-70 ventures generating revenue)
- **10-15% Launching** (70-100 ventures ready to go)
- **20-30% Building** (140-210 ventures in development)
- **40-50% Idea/Research** (280-350 ventures not started)
- **10-15% Archived** (70-100 dead projects)

---

## Phase 2: Command Center Dashboard (Week 2)

**Goal:** One place to see the entire business portfolio.

### Tool Recommendation
- **Airtable** (best for this use case)
  - 704-venture database
  - Multiple views (by OPCO, by status, by revenue)
  - Real-time filtering
  - Automation hooks
  - API for integrations

### Dashboard Views

**1. Executive Dashboard**
```
Portfolio Health
├── Total Ventures: 704
├── Operating: 47 (6.7%)
├── Revenue (YTD): $2.3M
├── Burn Rate: -$180K/month
├── Cash Runway: 8 months
├── Red Flags: 12 ventures
└── Green Lights: 23 ventures
```

**2. OPCO View (One per OPCO)**
```
OPCO-Marketplace (160 ventures)
├── Operating: 12
├── Revenue (YTD): $520K
├── Avg revenue per venture: $43K
├── Ventures to shut down: 5
├── Ventures to scale: 3
└── Next hire: Sales person
```

**3. Status View (Funnel)**
```
Idea       → Research    → Building    → Launching → Operating
280        → 70          → 140         → 100       → 47
ventures   → ventures    → ventures    → ventures  → ventures
-0.8%/mo   → +3%/mo      → -2%/mo      → +15%/mo   → +8%/mo
(attrition)(progress)    (stalling)    (launching) (growing)
```

**4. Revenue View**
```
Rank  Venture        Revenue/mo  Trend    Priority
1     EC-001         $45K        ↑↑       SCALE
2     CON-001        $32K        ↑        SCALE
3     ST-001         $28K        ↑        SCALE
4     OPS-015        $18K        →        MAINTAIN
5     TECH-008       $12K        ↓        FIX OR KILL
...
```

---

## Phase 3: 90-Day Revenue Ventures (Week 3-4)

**Goal:** Identify 3-5 ventures that can generate $500K-$1M in 90 days.

### Quick-Win Candidates

Based on your past work, these are likely:

**1. OPCO-Staffing (Recruiting/Temp)**
- Status: Operating (ST-001 doing $28K/month)
- 90-day potential: $100K/month
- Capital needed: $10K (recruiting tools, ads)
- Team: 1-2 recruiters
- Barrier: Low (repeatable process)

**2. OPCO-Operations (BPO Services)**
- Status: Building (some ventures active)
- 90-day potential: $75K/month
- Capital needed: $15K (training, infrastructure)
- Team: 1 operations lead + 5 contractors
- Barrier: Medium (needs process documentation)

**3. OPCO-Construction (Trade Services)**
- Status: Operating (CON-001 doing $32K/month)
- 90-day potential: $80K/month
- Capital needed: $5K (marketing, tools)
- Team: Existing (expand current jobs)
- Barrier: Low (proven model)

**4. OPCO-Marketplace (Job Board/Service Platform)**
- Status: Building (EC-001 beta)
- 90-day potential: $60K/month
- Capital needed: $25K (platform, marketing)
- Team: 1 PM + 1 growth person
- Barrier: High (network effects needed)

**5. OPCO-Technology (AI Agency/Automation)**
- Status: Building (concepts exist)
- 90-day potential: $50K/month
- Capital needed: $10K (tools, initial client work)
- Team: 2 engineers, 1 sales
- Barrier: Medium (GTM needed)

### 90-Day Revenue Target: $365K/month ($1.1M quarterly)

---

## Phase 4: Horizontal Team Charter (Month 2)

### Finance Horizontal
**Role:** Capital allocation, cash management, financial reporting

**Responsibility:**
- Daily cash position
- Monthly P&Ls per OPCO
- Capital deployment ($100K available)
- Fundraising strategy
- Tax optimization

**Team:** 1 CFO + 1 Controller (hire or contract)

### Sales Horizontal
**Role:** Revenue generation, customer acquisition, partnerships

**Responsibility:**
- Sales pipeline (all OPCOs)
- Customer acquisition cost tracking
- Partnership deals
- Revenue forecasting

**Team:** 1 VP Sales + 2 Account Managers

### Operations Horizontal
**Role:** Process standardization, execution, efficiency

**Responsibility:**
- SOP documentation (all OPCOs)
- Process automation
- Quality control
- Performance metrics

**Team:** 1 VP Ops + 1 Operations Manager

### Technology Horizontal
**Role:** Infrastructure, AI systems, software stack

**Responsibility:**
- CRM system (all OPCOs)
- AI agents
- Automation tools
- Tech stack decisions

**Team:** 1 CTO + 2 Engineers

### Marketing Horizontal
**Role:** Brand, awareness, lead generation

**Responsibility:**
- Brand strategy
- Lead gen campaigns
- Content creation
- Website/SEO

**Team:** 1 CMO + 1 Marketing Manager

### HR Horizontal
**Role:** Recruiting, talent, culture

**Responsibility:**
- Recruiting pipeline
- Contractor management
- Training & development
- Compensation strategy

**Team:** 1 Head of People (part-time initially)

### Legal Horizontal
**Role:** Contracts, compliance, protection

**Responsibility:**
- Operating agreements
- Customer contracts
- Regulatory compliance
- Risk management

**Team:** 1 General Counsel (contract)

### Data & Analytics Horizontal
**Role:** Dashboards, insights, forecasting

**Responsibility:**
- Financial dashboards
- KPI tracking
- Forecasting models
- Business intelligence

**Team:** 1 Data Analyst (part-time)

---

## Phase 5: 18-PDF Template (Month 2)

**Do NOT create 704 PDFs yet.**

Create ONE master template with all 18 documents:

1. Business Profile (name, mission, market)
2. Formation Documents (EIN, state registration)
3. Financial Model (P&L, cash flow, unit economics)
4. Marketing Plan (customer acquisition strategy)
5. Sales Process (pipeline, close rate, ACV)
6. Operations Manual (SOPs, processes)
7. Technology Stack (tools, systems, AI)
8. Team Structure (org chart, roles)
9. Customer Contracts (templates, terms)
10. Supplier Agreements (vendor list, terms)
11. KPI Dashboard (revenue, margin, growth)
12. 90-Day Plan (priorities, milestones)
13. Quarterly Reviews (performance tracking)
14. Risk Assessment (threats, mitigations)
15. Competitive Analysis (market position)
16. Scaling Strategy (how to 10x)
17. Acquisition Plan (if applicable)
18. Annual Review (year summary)

Use as master template for all OPCOs.

---

## Phase 6: Governance Structure (Month 3)

### Board/Advisor Council
- CEO (yourself)
- CFO (Finance Horizontal lead)
- COO (Operations Horizontal lead)
- CTO (Technology Horizontal lead)
- External advisor (business, legal, finance)

**Meetings:** Monthly

**Decisions:**
- Capital allocation >$50K
- New OPCO launches
- Major acquisitions
- Portfolio wind-downs

### OPCO Presidents
Each OPCO gets a president/GM who:
- Owns P&L
- Reports quarterly KPIs
- Manages 3-5 top ventures
- Hires/fires within budget

---

## Phase 7: Real Estate & Investment OPCOs (Month 4+)

### Real Estate OPCO (Currently: 1 venture)

**Build acquisition pipeline:**
1. Month 1-2: Scout 20-50 distressed properties
2. Month 3-4: Acquire 2-3 at discount
3. Month 5+: Renovate + hold or flip

**Capital needed:** $200K (acquisition + renovation)

**Revenue model:**
- Rentals ($3-5K/month per property)
- Flips ($20-50K per deal)
- Management fees ($1-2K/month per property managed)

### Investment OPCO (Currently: 0 ventures)

**Build investment portfolio:**
1. SPVs (Special Purpose Vehicles) for deals
2. Business acquisitions (small companies)
3. Real estate syndications
4. Venture investments

**Capital needed:** $500K initial

**Revenue model:**
- Equity returns
- Management fees
- Dividend income

---

## Phase 8: Quarterly Portfolio Review Process (Ongoing)

Every quarter (90 days):

### Review Every Venture
```
Status?     Keep / Scale / Sell / Merge / Pause / Archive
Revenue?    On track? Off track?
Team?       Right people? Need to hire?
Capital?    More needed? Payback time?
Risk?       Any red flags?
```

### Action Items
- KEEP: Support, don't interfere
- SCALE: Allocate more capital, hire talent
- SELL: Find buyer, transition
- MERGE: Combine with similar venture
- PAUSE: Freeze, revisit later
- ARCHIVE: Shut down, preserve IP

### Example: Q3 Review

```
EC-001 (Marketplace)
├── Status: Operating ✓
├── Revenue: $45K/month (exceeding target)
├── Team: Need 2 more customer service reps
├── Capital: +$50K for marketing
├── Risk: Competitor entering market
└── Decision: SCALE — allocate capital & hire

FIN-002 (Fintech Product)
├── Status: Building
├── Revenue: $0
├── Team: 2 engineers, stalled
├── Capital: Already spent $80K, no product
├── Risk: Team demoralized, wrong market
└── Decision: PAUSE — revisit in Q4

TECH-045 (Random AI Tool)
├── Status: Idea
├── Revenue: $0
├── Team: Nobody assigned
├── Capital: None spent
├── Risk: Dozens like this, not differentiated
└── Decision: ARCHIVE — kill it
```

---

## Priority Execution Order

### Week 1-2: Inventory
- [ ] Create VENTURE_INVENTORY_MASTER.csv with all 704 ventures
- [ ] Categorize status (Idea, Research, Building, Launching, Operating, Scaling, Acquired, Archived)
- [ ] Identify owner per venture
- [ ] List revenue YTD + monthly burn

### Week 3-4: Dashboard
- [ ] Set up Airtable workspace
- [ ] Build 5 views (Executive, OPCO, Status, Revenue, Team)
- [ ] Connect to Supabase (auto-sync)
- [ ] Create Slack alerts for red flags

### Month 2: Quick Wins
- [ ] Pick 3-5 high-potential ventures
- [ ] Allocate capital ($50-100K)
- [ ] Hire 3-5 key people (Sales, Ops, Tech)
- [ ] Target $365K/month revenue in 90 days

### Month 3: Horizontals
- [ ] Finance Horizontal operational
- [ ] Sales Horizontal building pipeline
- [ ] Operations Horizontal documenting SOPs
- [ ] Marketing Horizontal launching campaigns

### Month 4: Governance
- [ ] OPCO presidents assigned
- [ ] Monthly reporting cadence
- [ ] Quarterly reviews scheduled
- [ ] Capital allocation rules set

### Month 5-6: Real Estate
- [ ] Build acquisition pipeline
- [ ] Scout 50+ properties
- [ ] Target 2-3 acquisitions

### Month 7+: Investment
- [ ] Build investment portfolio
- [ ] Close 1-2 deals
- [ ] Target 10%+ annual returns

---

## Success Metrics (90 Days)

✅ Venture inventory complete  
✅ Command center live with real-time data  
✅ 47+ ventures operating (6.7% of portfolio)  
✅ $365K/month revenue (quick wins)  
✅ Horizontal teams hired  
✅ Governance structure active  
✅ Zero zombie ventures (killed or paused)  

---

## Critical Insight

**You don't need to fix all 704 ventures.**

You need to:
1. Know which ones matter (top 5% = $1.5M revenue)
2. Kill the zombies (bottom 30% = waste of time)
3. Scale the winners (middle 65% = can work with support)

The command center let's you do this in 90 days instead of 2 years.

