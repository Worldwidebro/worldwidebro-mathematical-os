---
name: family-office-os/OPCO-STRUCTURE
title: OPCO Structure & Governance
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# OPCO Structure & Governance

**Scope:** 38 OPCOs, economic layers, folder templates, governance models  
**Status:** Complete taxonomy with implementation templates  
**Generated:** 2026-07-28  
**Source:** `/Documents/OPCO_SECTORS_38.md`

---

## OPCO Overview

An **Operational Company (OPCO)** is an economic unit that:
- Represents one or more related business sectors
- Manages capital allocation to 15–100+ ventures
- Reports ROI, deployment velocity, and compliance metrics
- Operates autonomously within governance guardrails

**38 Total OPCOs across 7 Economic Layers:**

---

## Economic Layers & OPCO Grouping

### Layer 1: Infrastructure (5 OPCOs, 112 ventures)
Physical and connectivity backbone

| OPCO | Ventures | Capital Tier | Typical Investment |
|------|----------|--------------|-------------------|
| OPCO-Construction | 20 | T1/T2 | $100K–$2M (project financing) |
| OPCO-Transportation | 30 | T2 | $50K–$500K (fleet, routing) |
| OPCO-RealEstate | 35 | T1 | $500K–$5M (land, development) |
| OPCO-Energy | 15 | T2 | $250K–$1M (renewable, utility) |
| OPCO-Telecom | 12 | T2 | $100K–$1M (fiber, spectrum) |

**Governance:** Infrastructure lead (VP) + monthly capital committee

---

### Layer 2: Labor & Services (7 OPCOs, 281 ventures)
People, skills, and service delivery

| OPCO | Ventures | Capital Tier | Typical Investment |
|------|----------|--------------|-------------------|
| OPCO-Staffing | 25 | T2 | $50K–$250K (recruiting, training) |
| OPCO-Healthcare | 25 | T2 | $100K–$1M (clinics, wellness) |
| OPCO-Operations | 121 | T3 | $10K–$100K (ops, admin) |
| OPCO-Beauty | 40 | T2 | $25K–$250K (salons, spas) |
| OPCO-Hospitality | 35 | T2 | $50K–$500K (hotels, F&B) |
| OPCO-Legal | 18 | T2 | $25K–$250K (practices, services) |
| OPCO-Accounting | 22 | T2 | $50K–$250K (firms, services) |

**Governance:** Labor Operations lead (SVP) + bi-weekly sync

---

### Layer 3: Commerce (5 OPCOs, 170 ventures)
Buying, selling, and transaction services

| OPCO | Ventures | Capital Tier | Typical Investment |
|------|----------|--------------|-------------------|
| OPCO-Marketplace | 112 | T1 | $50K–$1M (platform, growth) |
| OPCO-Retail | 45 | T2 | $50K–$500K (storefronts, inventory) |
| OPCO-Automotive | 28 | T2 | $100K–$1M (dealers, services) |
| OPCO-Agriculture | 32 | T2 | $50K–$500K (farms, logistics) |
| OPCO-Manufacturing | 25 | T2 | $250K–$2M (plants, equipment) |

**Governance:** Commerce lead (VP) + weekly deployment review

---

### Layer 4: Capital & Finance (5 OPCOs, 221 ventures)
Money management and investment

| OPCO | Ventures | Capital Tier | Typical Investment |
|------|----------|--------------|-------------------|
| OPCO-Financial | 41 | T1 | $100K–$2M (fintech, banking) |
| OPCO-Insurance | 30 | T1 | $100K–$1M (underwriting, claims) |
| OPCO-Investment | 100 | T1 | $500K–$5M (funds, secondaries) |
| OPCO-VentureCap | 28 | T1 | $250K–$2M (accelerators, syndication) |
| OPCO-Trading | 22 | T1 | $100K–$1M (algorithms, prop trading) |

**Governance:** Finance lead (CFO) + real-time approval authority

---

### Layer 5: Content & Culture (5 OPCOs, 152 ventures)
Media, entertainment, and human expression

| OPCO | Ventures | Capital Tier | Typical Investment |
|------|----------|--------------|-------------------|
| OPCO-Media | 21 | T2 | $50K–$500K (publishing, broadcast) |
| OPCO-Publishing | 35 | T2 | $25K–$250K (books, magazines) |
| OPCO-Gaming | 40 | T2 | $100K–$1M (games, esports) |
| OPCO-Sports | 38 | T2 | $50K–$500K (teams, facilities) |
| OPCO-Music | 18 | T2 | $25K–$250K (labels, artists) |

**Governance:** Content lead (CMO) + monthly strategy review

---

### Layer 6: Knowledge & Development (4 OPCOs, 152 ventures)
Learning, training, and human capital

| OPCO | Ventures | Capital Tier | Typical Investment |
|------|----------|--------------|-------------------|
| OPCO-Education | 57 | T1/T2 | $50K–$500K (schools, platforms) |
| OPCO-ELearning | 32 | T2 | $25K–$250K (courses, content) |
| OPCO-Training | 28 | T2 | $50K–$500K (programs, certifications) |
| OPCO-Recruiting | 35 | T2 | $25K–$250K (talent matching, placement) |

**Governance:** Education lead (Chief Learning Officer) + monthly review

---

### Layer 7: Systems & Innovation (7 OPCOs, 359 ventures)
Technology, data, and continuous improvement

| OPCO | Ventures | Capital Tier | Typical Investment |
|------|----------|--------------|-------------------|
| OPCO-Technology | 50 | T1 | $100K–$1M (hardware, infrastructure) |
| OPCO-SaaS | 85 | T1 | $50K–$1M (software, platforms) |
| OPCO-Data | 42 | T1 | $100K–$1M (analytics, insights) |
| OPCO-Security | 30 | T1 | $50K–$500K (cybersecurity, compliance) |
| OPCO-Environment | 18 | T3 | $50K–$500K (sustainability, green) |
| OPCO-Consulting | 40 | T2 | $50K–$250K (advisory, implementation) |
| OPCO-Government | 24 | T3 | $50K–$250K (public sector, civic tech) |

**Governance:** CTO/Innovation lead (CTO) + weekly sync, monthly review

---

## Folder Structure Template

**Each OPCO has a standardized folder structure:**

```
family-office-os/opcos/
└── OPCO-{Name}/
    ├── README.md                          # OPCO charter, team, goals
    ├── CAPITAL-ALLOCATION-{OPCO}.md       # This OPCO's tier, formula, thresholds
    ├── ventures/
    │   ├── {SECTOR}-{NUMBER}/             # One venture per folder
    │   │   ├── venture.json               # Venture metadata
    │   │   ├── status.md                  # Current funding, deployment status
    │   │   ├── financials/
    │   │   │   ├── deployments.csv        # Capital deployed (date, amount, status)
    │   │   │   ├── revenue.csv            # Revenue by month
    │   │   │   └── roi-tracking.json      # Predicted vs actual ROI
    │   │   └── docs/
    │   │       ├── pitch.md               # Venture pitch
    │   │       ├── market.md              # Market analysis
    │   │       └── team.md                # Founder/team info
    │   └── [repeat for all ventures]
    ├── governance/
    │   ├── OPCO-LEAD.md                   # OPCO lead (name, contact, authority)
    │   ├── approval-matrix.json           # Who approves what amount
    │   ├── monthly-review-checklist.md    # Monthly review protocol
    │   └── escalation-paths.md            # Who to contact for issues
    ├── metrics/
    │   ├── current-allocation.json        # Current capital allocation
    │   ├── roi-tracking.csv               # 12mo rolling ROI average
    │   ├── deployment-velocity.csv        # Deployments per week/month
    │   └── approved-vendors.json          # Approved payment/deployment platforms
    └── archives/
        ├── exited-ventures/               # Ventures that exited (success/failure)
        ├── archived-deployments/          # Old deployment records
        └── historical-roi/                # Historical ROI data
```

---

## OPCO Governance Model

### Decision Authority Matrix

| Decision Type | < $50K | $50K–$100K | $100K–$500K | $500K–$1M | $1M+ |
|---------------|--------|-----------|-----------|----------|------|
| **Deployment** | OPCO Agent | OPCO Agent (if conf > 70%) | OPCO Lead | OPCO Lead + CFO | Board |
| **Rebalance** | Auto-logged | Weekly review | OPCO Lead | CFO | Board |
| **Emergency** | OPCO Lead | OPCO Lead | CFO | Board | Board |
| **New Venture** | OPCO Lead | OPCO Lead | CFO + Board | Board | Board |
| **Pivot/Exit** | OPCO Lead | OPCO Lead | CFO + Board | Board | Board |

### OPCO Lead Role

**Title:** OPCO Lead (VP or SVP depending on OPCO size)

**Responsibilities:**
- Oversee 15–100+ ventures within OPCO
- Approve deployments up to $500K (within allocation)
- Attend monthly capital committee meetings
- Ensure ventures stay aligned with OPCO mission
- Track ROI vs forecast and report monthly
- Manage OPCO team (small ops team, 2–4 people)

**Authority:**
- Approve ventures under $500K
- Request emergency reserve draws
- Recommend tier reclassification
- Hire/fire venture leads within OPCO

**Reporting:**
- Monthly: ROI report, deployment velocity, tier status
- Quarterly: Strategic review, 3-month forecast
- Ad-hoc: Escalations, emergency requests

---

## Monthly Review Protocol

**Every 1st of month, 12am UTC, each OPCO lead:**

1. **Review last month's deployments**
   - How many ventures deployed capital?
   - Total deployed amount vs allocation
   - Deployment success rate (% confirmed by Stripe)

2. **Calculate and report 12-month rolling ROI**
   - Average ROI across all ventures
   - Compare to tier benchmark (T1: 15%, T2: 10%, T3: 8%)
   - Identify underperformers (ROI < 50% of benchmark)

3. **Assess deployment velocity**
   - Deployment rate this month vs target
   - Velocity factor for next month's rebalance
   - Flag if > 70% drawdown (fast burn rate)

4. **Recommend tier adjustment (if applicable)**
   - Is OPCO ready for tier upgrade/downgrade?
   - Evidence: ROI trend, velocity consistency, deployment quality

5. **Submit to capital committee**
   - CSV: last month's deployments, ROI data, velocity
   - Narrative: 1-page summary of status and requests
   - Attachments: Any venture updates or escalations

---

## Integration with Capital Allocation System

**Weekly Rebalance (Mondays 6am UTC):**

```
For each OPCO:
  1. Query capital_deployment_log: how much deployed this week?
  2. Query capital_allocations: what's remaining?
  3. Apply allocation formula (Tier 1/2/3)
  4. If new allocation > 5% different from current → update
  5. Log decision in capital_decisions table
  6. Notify OPCO lead via Slack
```

**Monthly Tier Review (1st of month, 12am UTC):**

```
For each OPCO:
  1. Query capital_deployment_log: calculate 12mo avg ROI
  2. Compare to tier benchmark (T1: 15%, T2: 10%, T3: 8%)
  3. Calculate growth rate (this month's ROI - 6mo ago ROI) / 6mo ago ROI
  4. If reclassification criteria met → flag for CFO review
  5. If reclassified → update OPCO tier in Neo4j
  6. Notify OPCO lead + board secretary
```

---

## OPCO Launch Checklist

**When creating a new OPCO:**

1. **Define scope**
   - Which sectors/ventures does this OPCO manage?
   - Initial venture count and capital needs
   - Name, code (e.g., OPCO-SaaS)

2. **Assign OPCO lead**
   - VP or SVP-level executive
   - Background in sector
   - Authority to approve up to $500K

3. **Set initial allocation**
   - Assign tier (T1/T2/T3/Reserve/Strategic)
   - Calculate base allocation % using formula
   - Set venture deployment targets

4. **Create OPCO folder structure**
   - Run: `mkdir -p family-office-os/opcos/OPCO-{Name}/(ventures/governance/metrics/archives)`
   - Copy template files
   - Create README.md with charter and team

5. **Register in Neo4j**
   - Create node: `(o:OPCO {name: 'OPCO-X', tier: 'T1', lead: 'Name', capital: $X})`
   - Create relationships to ventures: `(o)-[:MANAGES]->(v:Venture)`
   - Create relationships to lead: `(o)-[:LED_BY]->(p:Person)`

6. **Supabase setup**
   - Create entries in opco_capital_allocations table
   - Set initial capital_decisions records (bootstrap)
   - Enable real-time subscriptions for dashboard

7. **Configure agents**
   - Register OPCO agent with Langfuse
   - Set approval thresholds ($50K, $100K, $500K, etc.)
   - Configure decision-making parameters

---

## OPCO Example: OPCO-SaaS (T1, Mature)

**Charter:**
- Manage 85 SaaS ventures (subscription software, platforms)
- Deploy $148M capital (actual, varies by formula)
- Target 18%+ ROI
- Deploy to 50+ ventures per quarter

**Team:**
- OPCO Lead: John Doe (VP Engineering/Product)
- Ops Manager: Jane Smith
- Finance Analyst: Bob Johnson

**Monthly Targets:**
- Deployments: 12–15 ventures
- Capital deployed: $10M–$15M
- Approval rate: 90%+ of submitted ventures
- ROI tracking: 15–20% average

**Governance:**
- Weekly: Slack sync with team + finance
- Monthly: Full review + board reporting
- Quarterly: Strategic planning + tier assessment

**Current Status (example):**
- 12mo avg ROI: 18.2% (exceeds 15% T1 benchmark)
- Velocity factor: 0.92 (deployed 92% of target)
- Current allocation: $148.46M (formula-based)
- Reserve available: $15M (emergency buffer)

---

## Cross-OPCO Coordination

**Scenarios requiring cross-OPCO collaboration:**

### Scenario 1: Marketplace-Infrastructure Venture
**Case:** E-commerce platform needs both marketplace infrastructure AND logistics support

**Resolution:**
- OPCO-Marketplace leads (owns venture relationship)
- OPCO-Transportation co-invests (capital + expertise)
- Strategic pool pays integration costs ($500K cross-OPCO deployment)
- Board approves, both OPCOs credit deployment

### Scenario 2: SaaS-for-Construction
**Case:** Software platform specifically for construction industry

**Resolution:**
- OPCO-SaaS leads (tech platform, product)
- OPCO-Construction co-invests (domain expertise, customer acquisition)
- Both OPCOs share ROI percentage (split based on investment ratio)
- Financial records: both OPCOs log capital_deployment records (partial amounts)

### Scenario 3: Emergency Pivot
**Case:** Manufacturing venture needs to shift to supply-chain tech

**Resolution:**
- Current OPCO-Manufacturing releases venture to OPCO-SaaS
- Reserve pool covers transition costs ($250K)
- Board approves OPCO transfer
- capital_decisions logs reclassification
- Both OPCOs update venture.json metadata

---

## Tier Reclassification Rules

### Promotion from T3 to T2
**Criteria:**
- 12mo ROI > 10%
- Deployment velocity > 70%
- Confidence in growth trajectory (no negative sentiment)

**Process:**
- OPCO lead recommends (monthly review)
- CFO approves (1-week review window)
- Board notification
- New allocation formula applies immediately

### Promotion from T2 to T1
**Criteria:**
- 12mo ROI > 15%
- Deployment velocity > 85%
- 3+ months sustained performance at T2 level

**Process:**
- OPCO lead recommends (monthly review)
- CFO + Board approval (requires board vote)
- Effective next quarter
- New allocation formula applies (27% pool share)

### Demotion from T1 to T2
**Criteria:**
- 12mo ROI < 12%
- Deployment velocity < 70%
- 2 consecutive months below threshold

**Process:**
- CFO initiates review (automatic)
- OPCO lead presents remediation plan (1-week)
- Board votes (if ROI < 10%, automatic demotion)
- New allocation formula applies immediately
- OPCO lead performance improvement plan (60-day)

### Demotion from T2 to T3
**Criteria:**
- 12mo ROI < 5%
- Deployment velocity < 50%
- 1 month at threshold triggers review

**Process:**
- CFO initiates review (immediate)
- OPCO lead presents emergency recovery plan (48h)
- Board decides (likely demotion + leadership change)
- New allocation formula applies immediately

---

## Success Metrics by Tier

### Tier 1 (Mature)
| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| 12mo ROI | 18%+ | < 12% |
| Deployment velocity | 90%+ | < 70% |
| Deployment success | 95%+ | < 90% |
| Avg deal size | $100K–$500K | > $1M (concentration) |
| New ventures/quarter | 10+ | < 5 |

### Tier 2 (Growth)
| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| 12mo ROI | 10%+ | < 5% |
| Deployment velocity | 80%+ | < 60% |
| Deployment success | 90%+ | < 80% |
| Avg deal size | $50K–$250K | > $500K (concentration) |
| New ventures/quarter | 5–10 | < 3 |

### Tier 3 (Early)
| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Growth trajectory | +50% YoY | negative (decline) |
| Deployment velocity | 60%+ | < 40% |
| Deployment success | 80%+ | < 70% |
| Avg deal size | $25K–$100K | > $250K (concentration) |
| New ventures/quarter | 3–5 | < 2 |

---

## Version History

| Date | Version | Change |
|------|---------|--------|
| 2026-07-28 | 1.0 | Complete 38 OPCO taxonomy + folder templates |

---

**Generated:** 2026-07-28  
**Status:** Ready for deployment and OPCO team onboarding
