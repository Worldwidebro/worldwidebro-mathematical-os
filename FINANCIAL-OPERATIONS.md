# Financial Operations Architecture — Funding, Credit, Insurance, Taxes, Finance

**Created:** 2026-07-25 | **Status:** Tier 1 Complete

**Purpose:** Complete map of how 712 ventures access capital, build credit, insure operations, pay taxes, and manage finances.

---

## Layer 1: FUNDING SOURCES (How Ventures Get Capital)

### 1.1 Bootstrap Capital ($1K-$10K per venture)

**Source:** Worldwidebro Holdings founder reinvestment

**Flow:**
```
Profits from existing ventures
  → FINANCIAL (FIN-001)
  → Re-allocated to new ventures
  → Each new venture gets $1K-$10K
  → 60-day breakeven target
```

**Process:**
- Founder allocates from profit pool
- FINANCIAL approves (< $10K automatic)
- Venture receives capital via `/api/capital-request`
- Tracked in iza-os-financial-core ledger

---

### 1.2 Grant Funding ($5K-$500K per venture)

**Source:** FUND-001 (Grant Scanner)

**How it works:**
```
Venture submits info
  → FUND-001 searches grant database
  → AI matches to 5-10 grants
  → FUND-001 writes grant applications
  → Grants approved, capital deployed
  → Worldwidebro takes 15% success fee
```

**Available grants:**
- Small Business Administration (SBA) grants
- State economic development grants
- Sector-specific grants (construction, education, etc.)
- Non-profit/social impact grants

**Capital amount:** $5K-$500K per grant
**Timeline:** 60-90 days from application to funding
**Cost:** 15% success fee only (pay if grant succeeds)

---

### 1.3 Revenue-Based Financing (RBF) ($50K-$500K per venture)

**Source:** FUND-002 (RBF Platform)

**How it works:**
```
Venture with revenue (proof of traction)
  → Applies to FUND-002
  → AI underwriting via GenixBank
  → RBF offer: 3-10% of monthly revenue
  → Payback when revenue targets met
  → No equity loss, no interest
```

**Example:**
- Venture has $10K/mo revenue
- Applies for $200K RBF
- Repays at 5% of revenue = $500/mo
- 40-month payback (3.3 years)
- No equity dilution

**Capital amount:** $50K-$500K
**Timeline:** 2-4 weeks underwriting
**Repayment:** 3-10% of monthly revenue until goal met

---

### 1.4 Venture Debt ($100K-$1M per venture)

**Source:** FINANCIAL (FIN-001) via GenixBank

**How it works:**
```
Venture with 6+ months of revenue history
  → Applies to GenixBank via FIN-001
  → AI credit scoring
  → Terms: 3-5 year payback, 8-12% APR
  → Secured by assets or revenue streams
```

**Example:**
- Venture has $50K/mo revenue, $200K in assets
- Borrows $300K at 10% APR
- 48-month payback = $6,250/mo
- No equity loss

**Capital amount:** $100K-$1M
**Timeline:** 1-2 weeks underwriting
**Cost:** 8-12% APR (market rates for small business debt)

---

### 1.5 Venture Equity Rounds ($500K-$5M per venture)

**Source:** INVESTMENT (INV-001, INV-002, etc.)

**How it works:**
```
High-potential venture with $100K+ MRR
  → Pitched to INV-001 (Deal Flow Platform)
  → VC screening + diligence
  → Terms: $500K-$5M at 18-24x revenue multiple
  → Worldwidebro retains 20-51% ownership
```

**Example:**
- Venture doing $500K/mo revenue ($6M ARR)
- Raised at 3x revenue = $18M valuation
- $5M equity round at 27.8% dilution
- Worldwidebro's 51% stake now worth $9.2M (pre-round: $9.2M)

**Capital amount:** $500K-$5M
**Timeline:** 4-12 weeks diligence + close
**Dilution:** 20-51% equity per round

---

### 1.6 Government Contracts & SBA Loans ($50K-$5M per venture)

**Source:** GOV-PROCUREMENT (GPC-001-015)

**How it works:**
```
Ventures bid on government contracts
  → GPC coordinates bidding process
  → Wins contract → Advance funding available
  → SBA 7(a) loans against contract
  → $50K-$5M depending on contract size
```

**Capital amount:** $50K-$5M
**Timeline:** 30-90 days SBA processing
**Repayment:** From government contract proceeds (low-risk revenue)

---

## Layer 2: BUSINESS CREDIT (How Ventures Build Creditworthiness)

### 2.1 Business Credit Building (FIN-007)

**Source:** FINANCIAL (FIN-001) via GenixBank

**How it builds:**
```
Step 1: Establish legal entity
  → Federal EIN from IRS
  → Register in state

Step 2: Build credit profile
  → DUNS number (Dun & Bradstreet)
  → Credit report monitoring

Step 3: Get initial trade credit
  → GenixBank issues $5K-$25K credit line
  → Venture buys supplies on net 30
  → Pays on time → score improves

Step 4: Expand credit
  → Credit score 600+ → $50K+ available
  → Credit score 700+ → $500K+ available
  → Credit score 750+ → $2M+ available
```

**Timeline:** 6-12 months to reach 700+ score
**Tools:** Trade credit accounts, business credit cards, supplier financing

---

### 2.2 Trade Credit & Supplier Financing

**How it works:**
```
Venture needs $10K in materials
  → Asks supplier for "net 30" terms
  → Supplier approves (if creditworthy)
  → Venture receives materials, pays in 30 days
  → Payment reported to credit bureaus
  → Improves business credit score
```

**Available for all sectors:**
- MFG suppliers offer net 30-90 terms
- TRANS suppliers offer net 30 terms
- AGRI suppliers offer net 45 terms
- Cumulative available trade credit: $500K+

---

### 2.3 Invoice Factoring (FIN-012)

**How it works:**
```
Venture completes project, invoices customer
  → Customer owes $100K, pays in 60 days
  → Venture needs cash NOW
  → FIN-012 (Invoice Factoring AI) buys invoice at 95%
  → Venture gets $95K immediately
  → FIN-012 collects $100K from customer
  → FIN-012 keeps $5K (5% factoring fee)
```

**Use case:** Bridge cash between invoice and payment
**Cost:** 2-5% factoring fee (depending on venture credit quality)
**Available amount:** Up to 80% of monthly revenue in receivables

---

### 2.4 Business Credit Cards

**Issuers:** GenixBank (via FIN-001), American Express, Chase

**Limits:** $5K-$500K depending on creditworthiness

**Benefits:**
- 30-60 day payment terms
- Bonus points/cash back
- Builds credit history
- Separates personal from business spending

---

## Layer 3: INSURANCE (How Ventures Mitigate Risk)

### 3.1 Liability Insurance (INS-001, INS-002, INS-003)

**Types:**
- General liability (slip & fall, damage to property)
- Professional liability (errors & omissions)
- Product liability (products harm customer)
- Cyber liability (data breach, ransomware)

**Cost:** 0.5%-2% of annual revenue
**Available to:** All 38 sectors

---

### 3.2 Property Insurance

**Types:**
- Building insurance (from RE-001 properties)
- Equipment insurance (manufacturing equipment, vehicles)
- Inventory insurance (goods in warehouse)

**Cost:** 0.5%-1.5% of asset value
**Available to:** CON, MFG, TRANS, RETAIL, WAREHOUSE

---

### 3.3 Workers Compensation Insurance

**Requirement:** Mandatory for all ventures with employees

**Cost:** 1-3% of annual payroll
**Coverage:** Employee injury, disability, medical costs

**Administered by:** STA-001 (Staffing) for workers
**Administered by:** OPS-001 (Operations) for permanent staff

---

### 3.4 Commercial Auto Insurance

**Required for:** TRANS, LOGISTICS, FIELD SERVICE ventures

**Cost:** $800-$2K per vehicle per year
**Coverage:** Liability, collision, comprehensive

---

### 3.5 Surety Bonds

**Required for:** GOV-PROCUREMENT (government contracts), CON (construction permits)

**Cost:** 1-3% of contract value
**Coverage:** Performance guarantees, bid bonds

---

## Layer 4: TAXES (How Ventures Meet Tax Obligations)

### 4.1 Estimated Quarterly Taxes (FIN-006: Tax Prep Filing Services)

**What's owed:**
- Corporate income tax (21% federal, 3-7% state)
- Payroll taxes (15.3% Social Security + Medicare)
- Sales tax (0-8.875% depending on state)
- Excise taxes (certain sectors)

**Payment schedule:**
- Q1: April 15 (Q4 income)
- Q2: June 15 (Q1 income)
- Q3: September 15 (Q2 income)
- Q4: January 15 (Q3 income)

---

### 4.2 Tax Credits & Deductions

**Available credits:**
- R&D tax credit (15-20% of R&D spending)
- Work opportunity tax credit (WOTC) for hiring disadvantaged workers
- ERC (Employee Retention Credit) for payroll taxes

**Available deductions:**
- Business expenses (materials, supplies, travel)
- Home office deduction (if remote)
- Depreciation (equipment, vehicles, buildings)
- Interest deduction (business debt)
- Health insurance (self-employed)

**Utilization:** FIN-021 (Tax Deduction Finder) AI scans spending, identifies $10K-$100K in tax savings per venture per year

---

### 4.3 Sales Tax Management

**Requirements:**
- Collect sales tax from customers (varies by state: 0-8.875%)
- Remit monthly/quarterly to state
- File sales tax return

**Automation:** n8n workflow (via TECH-062) automates sales tax calculation and filing

---

### 4.4 Payroll Tax Management

**Requirements:**
- Federal income tax withholding
- Social Security & Medicare taxes (FICA): 15.3% total
- State income tax withholding
- File monthly/quarterly returns

**Automation:** FIN-034 (Payroll Automation) handles all withholding and filing via STA-001

---

### 4.5 Entity-Level Tax Strategy

**Entity structure impact:**
- C-Corp: Double taxation (entity + shareholder), but liability protection
- S-Corp: Pass-through taxation, must have profit (suitable for $150K+ ventures)
- LLC: Pass-through (default), flexibility
- Solo proprietor: Simple but no liability protection

**Optimization:**
- FIN-008 (Business Formation Services) helps choose optimal structure
- Tax savings: 5-20% of net profit via correct entity choice

---

## Layer 5: FINANCE OPERATIONS (How Ventures Run Daily Finance)

### 5.1 Payroll (FIN-034 + STA-001)

**Monthly process:**
```
STA-001: Track hours worked
  → FIN-034: Calculate gross pay, taxes, deductions
  → FIN-034: File payroll taxes (federal + state)
  → FIN-034: Deposit net pay to employee accounts
  → FIN-034: Generate pay stubs + tax forms
```

**Cost:** $1,000-$5,000/mo (FIN-034 service fee is embedded in FINANCIAL cost)

---

### 5.2 Accounts Payable (FIN-011)

**Process:**
```
Vendor sends invoice
  → FIN-011: Logs invoice (due date, amount)
  → Venture approves payment
  → FIN-011: Schedules payment for due date
  → FIN-011: Tracks cash outflow
```

**Benefit:** Never miss a payment (automatic workflow)

---

### 5.3 Accounts Receivable (FIN-012)

**Process:**
```
Venture completes work, creates invoice
  → FIN-012: Logs invoice (due date, customer, amount)
  → Customer pays by due date OR
  → FIN-012: Offers invoice factoring (95% immediate payout)
  → FIN-012: Tracks cash inflow
```

**Benefit:** Don't wait for payment; access capital via factoring

---

### 5.4 Monthly Accounting (FIN-011)

**Monthly close process:**
```
Day 1-25: Record transactions (invoices, expenses, payroll)
Day 26-27: Reconcile accounts
Day 28: Generate financial statements
  ├─ P&L (profit/loss)
  ├─ Balance sheet (assets/liabilities)
  ├─ Cash flow statement
  └─ Variance analysis (budgeted vs actual)
```

**Automation:** FIN-011 (Automated Bookkeeping) does 80% of work; HUMAN reviews and approves

---

### 5.5 Quarterly Tax Planning (FIN-006)

**Quarterly process:**
```
Weeks 1-2 of month after quarter ends:
  → FIN-006: Calculate estimated quarterly taxes
  → FIN-006: Identify tax-saving opportunities
  → OPS-001: Approves and remits payments
  → FIN-006: Generates quarterly report
```

---

### 5.6 Annual Audit & Tax Filing (FIN-006, FIN-033)

**Annual process:**
```
Dec-Jan: Prepare year-end financials
  → FIN-011: Year-end close
  → Reconcile all accounts
  → Generate annual statements

Jan-Mar: Tax planning & filing
  → FIN-033 (AI Tax Preparation Service): Calculates taxes
  → FIN-006: Files corporate tax return (Form 1120)
  → FIN-034: Files payroll tax forms (Form 941, W-2s)
  → OPS-001: Pays annual tax bill
```

**Cost:** $1K-$10K depending on venture complexity

---

### 5.7 Financial Reporting to Worldwidebro

**Monthly dashboard:**
```
OPS-001 aggregates all 712 ventures:
  ├─ Total revenue: $MMM
  ├─ Total costs: $MMM
  ├─ Total profit: $MMM
  ├─ Total tax liability: $MMM
  ├─ Reinvestment pool: $MMM
  ├─ Capital deployment: $MMM
  └─ Runway by OPCO (months until cash out)
```

**Real-time access:** Dashboard at `ops.worldwidebro.com/financial`

---

## Complete Financial Flow: 90-Day Venture Startup

### Month 1: Launch with Bootstrap Capital

```
Day 1-5:
├─ Worldwidebro allocates $5K bootstrap capital
├─ Venture incorporates (LLC or S-Corp)
├─ Gets EIN from IRS
├─ Opens business bank account

Day 6-15:
├─ Builds DUNS number
├─ Establishes business credit profile
├─ Gets $10K GenixBank credit line
├─ Gets business credit card ($5K limit)

Day 16-30:
├─ Launches MVP
├─ Makes first $2K in revenue
├─ Pays first suppliers (builds trade credit)
├─ Registers for sales tax
└─ Files first payroll (if employees)
```

**Month 1 P&L:**
```
Revenue:        $2,000
Costs:          $1,500
Profit:         $500
Capital burn:   $4,500 (from bootstrap)
Runway:         10 months (if $500/mo profit stays constant)
```

---

### Month 2: Grow Revenue, Access Credit

```
Venture closes first customer at $10K/mo recurring
  → Revenue accelerates $10K/mo
  → Increased capital needs (inventory, team, etc.)
  
Week 1:
├─ Applies for trade credit expansion ($50K)
├─ Applies for invoice factoring credit line ($100K)
├─ GenixBank credit score reaches 650+ (from on-time payments)

Week 2:
├─ Gets $50K trade credit approved
├─ Gets $100K factoring line approved
├─ Can now fund $150K in operating growth

Week 3-4:
├─ Accelerates hiring via STA-001
├─ Increases inventory via MFG-*
├─ Ships first 5 customers at scale
└─ Revenue reaches $30K/mo
```

**Month 2 P&L:**
```
Revenue:        $30,000 (accelerating)
Costs:          $18,000 (higher headcount, inventory)
Profit:         $12,000
Capital burn:   -$7,000 (actually generating capital now!)
Runway:         Indefinite (profitable)
Credit score:   650+ (can access $150K+ credit)
```

---

### Month 3: Unlock Institutional Capital

```
Venture shows $30K+ MRR, is profitable
  → FIN-012 (Invoice Factoring): Can factor $100K/mo
  → GenixBank: Credit score 700+ → offers $500K term loan
  → FUND-001 (Grant Scanner): Identifies $100K in available grants
  → FUND-002 (RBF): Offers $250K RBF on 5% revenue share

Venture chooses capital stack:
├─ $250K RBF (5% of revenue = $1.5K/mo)
├─ $100K term loan from GenixBank (8% APR = $2K/mo)
├─ $100K grant from state (no repayment)
└─ Total capital unlocked: $450K
```

**Month 3 P&L:**
```
Revenue:        $50,000 (with new capital deployed)
Costs:          $28,000 (expanded operations)
Gross profit:   $22,000
Loan payments:  $3,500 (RBF + GenixBank)
Net profit:     $18,500
Runway:         Indefinite
Credit score:   750+ (excellent)
Available capital: $1M+ (can access venture debt/equity)
```

---

## Tax Calendar: Annual Schedule

| Date | Task | Responsibility |
|------|------|---|
| Jan 15 | Q4 estimated tax payment | OPS-001 |
| Jan 31 | Payroll tax forms (Form 941) | FIN-034 |
| Feb 15 | W-2 distribution to employees | STA-001 |
| Mar 15 | Corp income tax return (Form 1120) | FIN-006 |
| Apr 15 | Q1 estimated tax payment | OPS-001 |
| Jun 15 | Q2 estimated tax payment | OPS-001 |
| Sep 15 | Q3 estimated tax payment | OPS-001 |
| Oct 15 | Corp tax return extension (if needed) | FIN-006 |
| **Daily** | Sales tax collection | Each venture |
| **Monthly** | Payroll tax deposits | FIN-034 |
| **Quarterly** | Payroll tax returns (Form 941) | FIN-034 |
| **Quarterly** | Sales tax remittance | n8n (automated) |

---

## Financing Matrix: Capital Sources by Venture Stage

| Stage | Revenue | Available Capital | Source | Terms |
|-------|---------|---|---|---|
| **Pre-Launch** | $0 | $1K-$10K | Bootstrap | No repayment |
| **MVP (1-3 mo)** | $0-$10K | $10K-$25K | Trade credit, GenixBank CC | 30-60 day terms, 18% APR |
| **Traction (3-6 mo)** | $10K-$50K | $50K-$500K | Invoice factoring, RBF, grants | 2-5% fees, 5-10% revenue share |
| **Growth (6-12 mo)** | $50K-$500K | $500K-$2M | Venture debt, equity | 8-12% APR, 20-30% equity |
| **Scale (12+ mo)** | $500K+ | $2M+ | Series A/B, bank financing | Market rates, 15-30% equity |

---

**All 712 ventures use this same financial playbook.**
**Aggregate annual financial capacity: $500M+ in capital access + $200M+ in annual operating capacity.**
