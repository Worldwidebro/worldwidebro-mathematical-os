# COMPLETE ORG CHART: Worldwidebro Holdings Orchestration System

**Created:** 2026-05-09  
**Status:** LIVE (in Supabase `positions` table)  
**Total Positions:** 20

---

## TIER 1: EXECUTIVE LEADERSHIP (Authority 10-8)

### CEO / Founder
- **Position Code:** POS-CEO-001
- **Type:** Human
- **Authority Level:** 10 (All approvals)
- **Approval Threshold:** $999,999
- **Department:** Executive
- **Reports To:** Board
- **Responsibilities:**
  - Strategic direction & vision
  - All approvals above $500K
  - Board oversight
  - Key partnerships
  - Major vendor relationships

---

### COO / Operations
- **Position Code:** POS-COO-001
- **Type:** Human
- **Authority Level:** 9
- **Approval Threshold:** $500,000
- **Department:** Operations
- **Reports To:** CEO
- **Responsibilities:**
  - Vendor management & onboarding
  - Project coordination across sectors
  - Quality assurance oversight
  - Budget management
  - Daily operations
- **Covers:** All construction, beauty, tech vendors

---

### CFO / Finance
- **Position Code:** POS-CFO-001
- **Type:** Human
- **Authority Level:** 9
- **Approval Threshold:** $500,000
- **Department:** Finance
- **Reports To:** CEO
- **Responsibilities:**
  - Revenue tracking & forecasting
  - Cash flow management
  - Vendor payables
  - Financial close & reporting
  - Compliance & audit

---

### Head of Sales
- **Position Code:** POS-SALES-HEAD-001
- **Type:** Human
- **Authority Level:** 8
- **Approval Threshold:** $200,000
- **Department:** Sales
- **Reports To:** CEO
- **Responsibilities:**
  - Lead generation strategy
  - Client relationship management
  - Deal closing & negotiations
  - Sales KPI tracking
  - Sales team management
- **Covers:** All 16 sectors (direct relationship leads)

---

## TIER 2: SECTOR MANAGERS (Authority 6-5)

### Beauty & Wellness Sector Manager
- **Position Code:** POS-BEAUTY-MANAGER
- **Type:** Human
- **Authority Level:** 6
- **Approval Threshold:** $100,000
- **Covers:** BW-001 through BW-087 ventures
- **Responsibilities:**
  - Beauty/wellness vendor coordination
  - Sub-vendor management
  - Quality assurance for sector
  - Sector reporting & KPIs
  - Client handoff & onboarding

---

### Tech & Software Sector Manager
- **Position Code:** POS-TECH-MANAGER
- **Type:** Human
- **Authority Level:** 6
- **Approval Threshold:** $100,000
- **Covers:** TECH-001 through TECH-120 ventures
- **Responsibilities:**
  - Tech vendor coordination
  - Development partnerships
  - Product launch oversight
  - Sector reporting

---

### Construction Sector PM
- **Position Code:** POS-CONSTRUCTION-PM
- **Type:** Human
- **Authority Level:** 6
- **Approval Threshold:** $100,000
- **Covers:** CON-001 through CON-087 ventures
- **Responsibilities:**
  - Subcontractor management
  - Project delivery oversight
  - Quality & compliance
  - Sector reporting

---

### Finance Manager
- **Position Code:** POS-FINANCE-MANAGER
- **Type:** Human
- **Authority Level:** 5
- **Approval Threshold:** $50,000
- **Reports To:** CFO
- **Responsibilities:**
  - Invoice generation & tracking
  - Vendor payables processing
  - Revenue transaction logging
  - Monthly financial close

---

### Vendor Manager
- **Position Code:** POS-VENDOR-MANAGER
- **Type:** Human
- **Authority Level:** 5
- **Approval Threshold:** $50,000
- **Reports To:** COO
- **Responsibilities:**
  - Vendor onboarding & qualification
  - MSA negotiation & execution
  - Performance scoring system
  - Affiliate network maintenance

---

## TIER 3: AI AGENTS (Authority 5, Escalate Above $50K)

### 16 Sector AI Agents
*(All autonomous, escalate human-level decisions to sector managers)*

| Agent | Position Code | Sector Coverage | Reports To |
|-------|---------------|-----------------|-----------|
| qwen-beauty-wellness | POS-AGENT-QWN-BEAUTY | BW-001:087 | Beauty Manager |
| qwen-technology | POS-AGENT-QWN-TECH | TECH-001:120 | Tech Manager |
| qwen-construction | POS-AGENT-QWN-CONSTRUCTION | CON-001:087 | Construction PM |
| qwen-ecommerce | POS-AGENT-QWN-ECOMMERCE | ECOM-001:150 | Sales Head |
| qwen-financial | POS-AGENT-QWN-FINANCE | FIN-001:050 | Finance Manager |
| qwen-food-hospitality | POS-AGENT-QWN-FOOD | FOOD-001:120 | COO |
| qwen-operations | POS-AGENT-QWN-OPS | OPS Sector | COO |
| qwen-education | POS-AGENT-QWN-EDU | EDU-001:080 | Sales Head |
| qwen-media-content | POS-AGENT-QWN-MEDIA | MEDIA-001:090 | Sales Head |
| qwen-fitness-sports | POS-AGENT-QWN-FITNESS | FIT-001:070 | COO |
| qwen-logistics | POS-AGENT-QWN-LOGISTICS | LOG-001:100 | COO |
| qwen-professional-services | POS-AGENT-QWN-PROF | PROF-001:110 | Sales Head |
| qwen-specialized | POS-AGENT-QWN-SPEC | SPEC-001:050 | COO |
| qwen-emerging | POS-AGENT-QWN-EMERGING | EMRG-001:075 | COO |
| qwen-community | POS-AGENT-QWN-COMM | COMM-001:060 | COO |
| qwen-software-tech | POS-AGENT-QWN-SOFTTECH | SOFTTECH-001:095 | Tech Manager |

**Agent Capabilities:**
- Lead routing by sector
- Vendor performance monitoring
- Deal pipeline tracking
- Performance reporting
- Task assignment & escalation
- Revenue tracking

---

## TIER 4: SUPPORT ROLES (Authority 4-5)

### Senior Sales Representative
- **Position Code:** POS-SALES-REP-001
- **Type:** Human
- **Authority Level:** 4
- **Approval Threshold:** $20,000
- **Reports To:** Head of Sales
- **Responsibilities:**
  - Lead qualification
  - Discovery calls
  - Proposal generation
  - Advanced negotiations
  - High-value client management

---

### Sales Representative
- **Position Code:** POS-SALES-REP-002
- **Type:** Human
- **Authority Level:** 4
- **Approval Threshold:** $20,000
- **Reports To:** Head of Sales
- **Responsibilities:**
  - Cold outreach & prospecting
  - Follow-up calls
  - Lead nurturing
  - Initial qualification

---

### Subcontractor Liaison
- **Position Code:** POS-SUBCONTRACTOR-LIAISON
- **Type:** Human
- **Authority Level:** 4
- **Approval Threshold:** $10,000
- **Reports To:** Vendor Manager
- **Responsibilities:**
  - Field coordination
  - Quality inspections
  - Payment processing
  - Vendor communication

---

### Accountant
- **Position Code:** POS-ACCOUNTANT
- **Type:** Human
- **Authority Level:** 4
- **Approval Threshold:** $10,000
- **Reports To:** CFO
- **Responsibilities:**
  - Invoice generation
  - Expense tracking
  - Financial reporting
  - Tax preparation

---

## DECISION AUTHORITY MATRIX

### Approval Levels by Amount

| Amount | Authority Required | Examples |
|--------|-------------------|----------|
| $0 - $10K | Sector Manager or Specialist | Small work orders, vendor add-ons |
| $10K - $50K | Sector Manager + Finance Manager | Project work orders, vendor contracts |
| $50K - $100K | COO + Finance Manager | Major project launches, vendor MSAs |
| $100K - $500K | COO + CFO | Multi-vendor projects, sector budgets |
| $500K+ | CEO + CFO | Strategic investments, major ventures |

---

## REPORTING STRUCTURE

```
CEO / Founder
│
├─ COO / Operations
│  ├─ Beauty & Wellness Manager
│  │  └─ qwen-beauty-wellness (Agent)
│  ├─ Tech & Software Manager
│  │  └─ qwen-technology (Agent)
│  ├─ Construction PM
│  │  └─ qwen-construction (Agent)
│  ├─ Vendor Manager
│  │  └─ Subcontractor Liaison
│  ├─ Food & Hospitality (Agents)
│  ├─ Fitness & Sports (Agent)
│  ├─ Logistics & Transport (Agent)
│  ├─ Operations (Agents)
│  ├─ Emerging (Agent)
│  └─ Community (Agent)
│
├─ CFO / Finance
│  ├─ Finance Manager
│  │  └─ Accountant
│  └─ qwen-financial (Agent)
│
└─ Head of Sales
   ├─ Senior Sales Rep
   ├─ Sales Rep
   ├─ qwen-ecommerce (Agent)
   ├─ qwen-education (Agent)
   ├─ qwen-media-content (Agent)
   ├─ qwen-professional-services (Agent)
   └─ qwen-software-tech (Agent)
```

---

## POSITION COVERAGE MAP

### Sector Assignments

| Sector | Manager | AI Agent | Venture Count |
|--------|---------|----------|---------------|
| Beauty & Wellness | Beauty Manager | qwen-beauty | 87 |
| Technology | Tech Manager | qwen-tech | 120 |
| Construction | Construction PM | qwen-const | 87 |
| E-Commerce | Sales Head | qwen-ecom | 150 |
| Financial | Finance Manager | qwen-finance | 50 |
| Food & Hospitality | COO | qwen-food | 120 |
| Education | Sales Head | qwen-education | 80 |
| Media & Content | Sales Head | qwen-media | 90 |
| Fitness & Sports | COO | qwen-fitness | 70 |
| Logistics & Transport | COO | qwen-logistics | 100 |
| Professional Services | Sales Head | qwen-prof-services | 110 |
| Software & Tech | Tech Manager | qwen-soft-tech | 95 |
| Specialized Services | COO | qwen-specialized | 50 |
| Emerging | COO | qwen-emerging | 75 |
| Community | COO | qwen-community | 60 |

**Total Ventures Covered:** 708+ (360°coverage)

---

## DAILY EXECUTION ACCOUNTABILITY

### By Position

**CEO / Founder**
- [ ] Review CFO cash flow report
- [ ] Approve deals >$500K
- [ ] 1-2 strategic calls with key clients/vendors
- [ ] Review COO weekly operations summary

**COO / Operations**
- [ ] Approve vendor contracts >$50K
- [ ] Check sector manager reports
- [ ] Resolve escalated project issues
- [ ] Monitor quality metrics

**CFO / Finance**
- [ ] Review daily revenue transactions
- [ ] Approve vendor payables
- [ ] Monitor cash flow against projections
- [ ] Weekly financial review with Finance Manager

**Head of Sales**
- [ ] 5 outreach calls / day
- [ ] 2 discovery calls / day
- [ ] 1 negotiation / day
- [ ] Review ClickUp pipeline status
- [ ] Update deal statuses

**Sector Managers (Beauty, Tech, Construction)**
- [ ] Daily vendor check-in (Slack/ClickUp)
- [ ] Monitor project progress
- [ ] Escalate blockers to COO
- [ ] Quality spot-checks
- [ ] Weekly sector reporting

**AI Agents (16 Total)**
- [ ] Route new leads by sector
- [ ] Monitor vendor performance vs. KPIs
- [ ] Track project progress
- [ ] Generate daily sector reports
- [ ] Escalate human decisions (>$50K, conflicts, issues)

**Finance Manager**
- [ ] Process invoices / send to clients
- [ ] Process vendor payables
- [ ] Update revenue tracking
- [ ] Daily cash position check

**Vendor Manager**
- [ ] Onboard new vendors
- [ ] Negotiate MSAs
- [ ] Update performance scores
- [ ] Resolve vendor issues

**Sales Reps**
- [ ] Make 10 outreach calls / day
- [ ] Qualify leads
- [ ] Prepare discovery call materials
- [ ] Update ClickUp pipeline

---

## ESCALATION PATHS

### When Something Breaks

| Issue | Escalation Path |
|-------|-----------------|
| Project delayed | Sector PM → COO → CEO (if critical) |
| Vendor not performing | Vendor Mgr → COO → CEO (if MSA violation) |
| Deal stuck | Sales Rep → Head of Sales → COO (if contract issue) |
| Payment issue | Finance Mgr → CFO → CEO (if major client) |
| Quality failure | Sector PM → COO → CEO + Legal (if liability) |
| Budget overrun | Sector PM → COO + CFO → CEO |

---

## AGENT AUTONOMY RULES

### What Agents Can Decide Independently (<$50K)
- Assign leads to humans
- Suggest vendor matches
- Generate performance reports
- Track project progress
- Route work orders

### What Requires Human Approval (>$50K)
- New vendor contracts
- Major project changes
- Pricing negotiations
- Scope changes
- Resource allocation disputes

---

**Status:** ✅ READY FOR DEPLOYMENT

All 20 positions defined. Ready to populate positions table and assign humans to roles. AI agents ready to activate by sector.
