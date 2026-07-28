---
name: operating-model
description: How Worldwidebro Holdings runs—work flow, approval chains, margin capture, delegation mechanics
status: ACTIVE
version: 1.0
created: 2026-07-25
updated: 2026-07-25
---

# OPERATING MODEL

How Worldwidebro Holdings actually operates—the mechanics of turning 712 ventures into an efficient, automated system.

## Core Operating Principle

**One venture's output = Another venture's input.**

Work flows through the delegation network continuously. Margins are captured at every handoff.

---

## The Work Flow (4-Step Cycle)

### 1. Work Generation (Source OPCO)
A venture creates work or identifies an opportunity:

```
STA-001 (Staffing) says:
  "I have 5 electrical contractors ready"
  
Opportunity created:
  ├─ Contractor profiles (names, rates, reviews)
  ├─ Available dates
  ├─ Skill match scoring
  └─ Posted to delegation queue

System logs:
  ├─ Work created: STA-001
  ├─ Timestamp: 2026-07-25T09:15:00Z
  ├─ Work type: CONTRACTOR_PLACEMENT
  └─ Value: $5K potential revenue
```

---

### 2. Work Discovery (Receiving OPCO)
Another venture finds the work via the delegation network:

```
CON-001 (Construction) watches delegation queue:
  "CON-001 needs 5 electricians for Project Alpha"
  
Match found:
  ├─ STA-001's contractors meet requirements
  ├─ Match score: 92%
  ├─ Cost: $3K (contractor labor)
  ├─ CON-001 margin: $2K (if billed at $5K)
  └─ STA-001 margin: $0 (already paid by CON)
```

---

### 3. Work Execution (Both OPCOs)
Contractors are placed, work happens:

```
STA-001 executes:
  ├─ Sends contractor to CON-001 site
  ├─ Logs hours daily
  ├─ Tracks performance
  └─ Records completion

CON-001 executes:
  ├─ Supervises on-site work
  ├─ Validates quality
  ├─ Captures billable hours
  └─ Pays STA-001 per contractor-hour

Metrics tracked:
  ├─ STA: Placement success % (did contractor show up?)
  ├─ CON: Project completion % (was work done well?)
  ├─ Both: Revenue, cost, margin
  └─ System: Delegation velocity (work/week)
```

---

### 4. Margin Capture & Reinvestment (Finance OPCO)
Revenue flows through FIN, margins are reinvested:

```
Money flow:
  Customer pays CON-001 → $5K
    ↓
  CON-001 pays STA-001 → $3K
    ↓
  CON-001 gross profit → $2K
    ↓
  CON-001 operating costs → $0.8K (40%)
    ↓
  CON-001 net profit → $1.2K (60%)
    ↓
  Reinvestment:
    ├─ 20% ($240) → Grow CON-001
    ├─ 20% ($240) → Fund new Layer 1 ventures
    ├─ 10% ($120) → Acquisition fund
    ├─ 5% ($60) → Investment capital
    └─ 5% ($60) → Founder / contingency

FIN-001 handles:
  ├─ Receives cash from all OPCOs
  ├─ Allocates to reinvestment buckets
  ├─ Tracks capital deployment
  ├─ Reports cash position
  └─ Triggers new venture launches
```

---

## Approval Chains

**Not every decision needs human approval.** Only exceptions:

### Automatic (No Approval Needed)
- Work <$1K → Instant delegation
- Contractor placement (if score >85%) → Execute immediately
- Venture routine operations (Layer 1) → Agent-driven
- Marketing spend <$500 → Approved by COO-Agent

### Manager Approval (1-2 hours)
- Work $1K-$5K → COO-Agent or OPCO lead approves
- New contractor onboarding → STA-001 lead approves
- Venture staffing changes → OPCO lead approves

### Founder Approval (24 hours)
- New venture launch (>$5K capital) → Antwuan approves
- Acquisition (>$100K) → Antwuan approves
- Capital reallocation (>$50K) → Antwuan approves
- Debt >$10K → Antwuan approves (rare)

### Board/Legal Review (1 week)
- M&A >$500K → Board review
- New legal entity creation → Legal reviews
- Compliance issues → Legal + Founder

---

## Margin Capture Rules

Margins are captured at **every handoff** between OPCOs:

### STA → CON (Contractor Placement)
```
Contractor's true cost to STA: $30/hour
STA sells to CON at: $40/hour
STA margin: $10/hour = 25%
CON bills client at: $60/hour
CON margin: $20/hour = 33%
End client pays: $60/hour
```

### CON → RE (Project to Property Management)
```
CON completes construction project: $100K revenue
RE takes on property management: $2K/month
RE sells PM at market rate: $3K/month
RE margin: $1K/month = 33%
```

### RE → FIN (Property to Capital)
```
RE owns property, wants to refinance
FIN arranges loan: $500K principal
FIN borrowing cost: 8% = $40K/year
FIN offers RE: 10% = $50K/year
FIN margin: 2% = $10K/year
```

### FIN → TECH (Capital to Optimization)
```
FIN has $500K to deploy
TECH builds investment platform
TECH charges 0.5% fee = $2.5K/year
TECH saves FIN 2% in slippage = $10K/year
TECH total margin: $12.5K/year
```

---

## Financial Approvals & Capital Operations

See **[FINANCIAL-OPERATIONS.md](FINANCIAL-OPERATIONS.md)** for complete details. Quick reference below:

### Capital Request Approvals

**Automatic (<$1K) — No approval needed:**
- Bootstrap capital for new ventures
- Contractor onboarding (STA-001)
- Marketing spend (under $500)
- Inventory purchases (under $1K)
- Operational expenses (under $1K)

**Manager Approval ($1K-$5K) — 1-2 hours:**
- New venture launch capital
- OPCO equipment purchases
- Trade credit expansion
- Credit card requests
- Hiring bonuses

**Founder Approval ($5K+) — 24 hours:**
- Venture acquisition ($5K-$500K)
- Large capex (vehicles, real estate)
- Debt approval (>$10K borrowed)
- Capital reallocation (>$50K moved between OPCOs)
- Investor outreach / fundraising

**Board Review (>$500K):**
- M&A transactions
- Major recapitalization
- Equity rounds
- Strategic partnerships

### Payment Policies

| Transaction Type | Timeline | Owner |
|------------------|----------|-------|
| Payroll | Weekly (FIN-034 + STA-001) | STA-001 |
| Contractor invoices | Net 30 (STA → CON) | CON-001 |
| Vendor payments | Net 30-60 (FIN-011) | FIN-001 |
| Customer billing | Net 30-45 (varies) | Each venture |
| Tax payments | Quarterly (FIN-006) | OPS-001 |
| Dividend distribution | Quarterly (if profitable) | CFO-Agent |

### Daily Finance Operations

**Daily:**
- Time tracking & hour logging (STA-001)
- Expense receipts processed (n8n)
- Sales tax collected (automated, COMMERCE/RETAIL ventures)
- Cash position monitored (FIN-001 dashboard)

**Weekly:**
- Payroll calculated & deposited (FIN-034)
- Accounts payable review (FIN-011)
- Accounts receivable aging (FIN-012)
- Delegation margins captured (Neo4j logs)

**Monthly:**
- P&L prepared (3-statement close: P&L, Balance Sheet, Cash Flow)
- Variance analysis (budgeted vs actual)
- Venture KPIs reviewed
- Capital reallocation decisions
- Reinvestment pool updated

**Quarterly:**
- Tax planning & estimated payments (FIN-006)
- Credit score review & optimization (FIN-007)
- Business credit expansion (trade lines, cards)
- Insurance review & claims filing
- Risk assessment (by sector & OPCO)

**Annually:**
- Year-end close & financial audit (FIN-011)
- Tax filing (FIN-006 + FIN-033 + FIN-034)
- Entity structure review (C-Corp, S-Corp, LLC optimization)
- Venture performance ranking
- Acquisition targets identified
- Investment allocation decided

### Reinvestment Rules

From gross profit, **split capital as:**
```
60% of revenue → Profit (after opex)
├─ 20% → Grow existing venture (CON-001 grows CON)
├─ 20% → Fund new ventures (Layer 1-2 launches)
├─ 10% → Acquisition fund (buy distressed businesses)
├─ 5% → Investment capital (stocks, bonds, alternatives)
└─ 5% → Founder / contingency
```

**Example: CON-001 does $20K revenue**
```
Revenue:           $20,000
Opex (40%):        $8,000
Gross profit:      $12,000

Reinvestment:
  Grow CON:        $2,400 (new equipment, subcontractors)
  New ventures:    $2,400 (bootstrap STA/RE ventures)
  Acquisitions:    $1,200 (save toward $50K+)
  Investments:     $600 (deploy to diversified portfolio)
  Founder:         $600 (discretionary)
  ───────────
  Total reinvested: $7,200 (60% of profit)
```

**Capital deployment velocity:**
- Month 1-3: Bootstrap ventures only ($1K-$5K)
- Month 4-6: Add trade credit + RBF ($50K-$200K)
- Month 7-9: Add venture debt + grants ($500K+)
- Month 10-12: Add equity raises + acquisitions ($1M+)

### Financial Risk Thresholds

**Auto-alerts trigger for:**
- Venture cash runway < 30 days → Founder notified
- Unpaid invoices > 60 days → Collections escalated
- Debt service ratio > 50% of revenue → Refinance recommended
- Credit score drop > 50 points → Credit review
- Missed tax deadlines → Compliance alert

---

## Handoff Protocols

When work moves from one OPCO to another:

### Handoff Checklist
```
Before handoff:
  ├─ Quality check (is work acceptable?)
  ├─ Documentation complete (files, data, metadata)
  ├─ Financial terms agreed (pricing, timeline, payment)
  ├─ Ownership clear (who owns the relationship?)
  └─ Escalation path defined (who handles issues?)

At handoff:
  ├─ Timestamp logged (when did transfer occur?)
  ├─ Parties recorded (who is sending? who is receiving?)
  ├─ Margin recorded (what's the value split?)
  ├─ Status updated in Neo4j
  └─ Metrics tracked (success rate, cycle time, quality)

After handoff:
  ├─ OPCO 1: Follow-up on quality (is receiver happy?)
  ├─ OPCO 2: Track progress (is work moving forward?)
  ├─ Finance: Record transaction (margin to reinvest pool)
  └─ System: Update KPIs (velocity, success rate)
```

---

## Delegation Velocity (Key Metric)

**Delegation Velocity** = Work units moved between OPCOs per week

### Why This Matters
- Higher velocity = More revenue
- More revenue = More capital to reinvest
- More capital = Faster scaling to 100+ ventures

### Measuring Velocity
```
Week 1 metrics:
  ├─ STA → CON: 10 placements
  ├─ CON → RE: 2 projects
  ├─ RE → FIN: 1 refinance
  ├─ FIN → TECH: $100K deployed
  └─ Velocity score: 13 work units/week

Week 2 goal: 16 work units/week (+23%)
Month 2 goal: 25 work units/week
Month 6 goal: 100+ work units/week
```

---

## Bottleneck Identification & Resolution

The system automatically identifies slowdowns:

### Common Bottlenecks
| Bottleneck | Cause | Resolution |
|-----------|-------|-----------|
| STA can't find contractors | Low applicant flow | Scale recruiting, raise pay |
| CON can't sell projects | Poor sales pipeline | More marketing, presales training |
| RE can't close deals | Market conditions | Broaden geography, adjust pricing |
| FIN can't deploy capital | Analysis paralysis | Speed up underwriting, auto-approve <$50K |
| TECH can't keep up | Infrastructure limits | Scale servers, hire engineers |

### Resolution Process
```
Bottleneck detected (automated):
  ├─ System identifies: STA has 0 placements in queue
  ├─ Root cause analysis: No new contractors onboarded
  ├─ Recommendation: Scale recruiting spend +$1K/week
  └─ Alert sent to COO-Agent + Founder

Within 24 hours:
  ├─ Decision made (approve or override)
  ├─ If approved: $1K recruitment spend authorized
  ├─ Team mobilized: More job postings, referral bonuses
  └─ New metrics tracked: Daily contractor applications

By day 7:
  ├─ Bottleneck resolved
  ├─ Velocity increases
  ├─ ROI on $1K spend calculated
  └─ Decision recorded for future reference
```

---

## Related Documents

- [[BUSINESS]] — What we're building & why
- [[DELEGATION-NETWORK]] — Visual map of sector interconnections
- [[FUNDING-SOURCES]] — How capital flows

---

**Last Updated:** July 25, 2026  
**Owner:** Antwuan Johns
