---
id: DOCS-ARCH-001
title: "Company Brain Master System Architecture"
aliases: ["_DOCS/architecture", "Master Architecture Specification"]
tags: [architecture, system-design, control-planes, pipelines, layers]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[ARCHITECTURE|ARCHITECTURE.md]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]] | [[56-ENGINEERING/README|56-ENGINEERING]]

# Company Brain Master System Architecture

> **Authority:** System Architecture & Infrastructure Control Plane ([[CP-027]])  
> **Master Operating Contract:** [[ANTIGRAVITY.md]]  
> **Live Runtime State:** [[CLAUDE.md]]  
> **Location:** `_DOCS/architecture.md`  
> **Status:** 🟢 ACTIVE — Canonical Reference (2026-09-06)

---

## 1. Architectural Foundations
Company Brain is an enterprise-scale distributed cognitive operating system coordinating 700+ ventures, 893 owned repositories, 903 starred capabilities, and local-first AI inference across Apple Silicon hardware.

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                       00-CONSTITUTION & RESPECT                         │
│           Ethical Boundaries • Agency • Governance Constraints          │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    SEVEN OPERATIONAL PLANES (CP-001 to CP-035)           │
│   Governance • Data • Cognition • Execution • Observation • Evolution   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│               TEN-STAGE COGNITIVE PIPELINE (_PIPELINES/)                │
│ Ingestion → Processing → Transformation → Indexing → Retrieval →        │
│ Reasoning → Code Intel → Execution → Learning → Observability           │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                 50 NUMBERED OPERATING DOMAINS (00 to 50)                │
│ 00-CONSTITUTION ... 14-CAPABILITIES ... 23-VENTURES ... 50-MASTER-CTRL  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Architectural References
- **Master Contract:** [[ANTIGRAVITY.md]] (45 mandatory engineering & agent rules).
- **Executive Orientation:** [[STARTHERE.md]] & [[INDEX.md]].
- **Runtime Infrastructure:** [[CLAUDE.md]] (Mac Studio `100.87.214.70`, Tailscale mesh, OmniRoute `:20128`, Neo4j `:7687`, Qdrant `:6333`).
- **Master Control Hub:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] & [[50-MASTER-CONTROL/SEVEN_PLANES|SEVEN_PLANES.md]].
- **Engineering Domain:** [[56-ENGINEERING/README|56-ENGINEERING Hub]] & [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING Gateway]].
- **Evaluation & Benchmarking:** [[42-EVALUATION/README|42-EVALUATION Hub]].
- **Blueprints & Templates:** [[_TEMPLATES/README|Templates Gallery]].
- **Canonical Registries:** [[_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml]] & [[_REGISTRIES/VENTURE_REGISTRY.yaml]].

---

## 3. VENTURE REVENUE ARCHITECTURE: How 789 Ventures Make Money Independently

**Critical Distinction:** VEX is the **relationship intelligence layer**. Ventures generate revenue through **their own independent business models**, not through VEX.

```text
HOLDING COMPANY (Worldwidebro Holdings)
│
├─ Capital Allocation (VEX → Neo4j → Capital OS)
│  └─ Decides which ventures to fund, scale, or shut down
│
├─ VENTURE-001 (CareerOps Staffing / OPS-001)
│  ├─ Product: $2,500 placement fees + $1K/mo recurring
│  ├─ Revenue Source: Employer → Payment → Stripe → PostgreSQL
│  ├─ VEX Role: Track investor cap allocation, forecast ROI
│  └─ Independence: Fully autonomous (web app, form, payment)
│
├─ VENTURE-002 (ACE Construction / CON-001)
│  ├─ Product: $299 consultation + $5K-50K project fees
│  ├─ Revenue Source: GC → Consultation → Proposal → Contract → Payment
│  ├─ VEX Role: Show which advisors help close construction deals
│  └─ Independence: Fully autonomous (site, form, Stripe)
│
├─ VENTURE-003 ... VENTURE-789
│  └─ Each has unique revenue model, product, and payment flow
│
└─ Company Brain Role: Orchestrate capital, intelligence, and execution
   but DO NOT directly generate venture revenue
```

### 3.1 The Four Revenue Layers (Capital Playbook)

**Layer 1: Labor Income (20–30 ventures)**
```
Revenue Model: Service delivery + staffing + placement fees
Examples: OPS-001 (staffing), CON-001 (construction), LT-005 (courier)
Per-Venture: $0–50K/mo revenue (independent of VEX)
Margin Target: 40–53%
VEX Role: Track which people/investors back these, forecast cash flow
```

**Layer 2: Skill Monetization (50–100 ventures)**
```
Revenue Model: Digital products, APIs, templates, SaaS subscriptions
Examples: Growth OS, ClickUp automations, coding templates
Per-Venture: $0–10K/mo revenue (subscription + licensing)
Margin Target: 80–95%
VEX Role: Map which partners distribute these, track adoption
```

**Layer 3: Asset Acquisition (10–20 ventures)**
```
Revenue Model: SMB acquisition, real estate, equipment leasing
Examples: RE-001 (real estate), FIN-037 (trading), property portfolios
Per-Venture: $5K–200K/mo revenue (management fees + profit share)
Margin Target: 20–35%
VEX Role: Track investor commitments, property valuations, debt service
```

**Layer 4: Capital Compounding (Dynamic)**
```
Revenue Model: Treasury allocation, LP distributions, dividend payouts
Examples: Holding company reinvests venture profits
Per-Venture: Passthrough (venture profit → holding reserves)
Margin Target: Portfolio-wide equity compounding
VEX Role: Optimize capital allocation across all 789 ventures
```

### 3.2 Venture Revenue Independence Map

Each venture operates as a **self-contained economic unit**:

```
VENTURE OPS-001 (CareerOps Staffing)
│
├─ Website: ops-staff-001-staffing.vercel.app (Vercel deployment)
│  └─ Autonomous from VEX (independent React app)
│
├─ Product/Service: Staffing placement + matching
│  └─ Independent business logic (no VEX dependency)
│
├─ Payment Gateway: Stripe (standalone account)
│  └─ Webhook → Supabase (venture_payments table)
│  └─ Triggers: Growth OS notification, ClickUp task, Neo4j update
│
├─ Customer Acquisition: Cold calls, referrals, Growth OS campaigns
│  └─ Independent sales (Growth OS is coordination, not revenue)
│
├─ Revenue Recognition: $2,500 per placement + $1K/mo recurring
│  └─ Recorded in Supabase, reported to holding company
│
└─ VEX Connection: Neo4j tracks investor cap, people involved, ROI
   but does NOT execute the staffing transaction
```

### 3.3 The Three Revenue Flows

**Flow 1: Venture → Customer Payment (Direct Revenue)**
```
Customer fills OPS-001 form
  ↓
Stripe captures $2,500
  ↓
Supabase records payment (venture_payments table)
  ↓
PostgreSQL syncs to holding company accounting
  ↓
VENTURE REVENUE RECOGNIZED: $2,500
  ↓
VEX/Neo4j updates: Venture metrics, investor ROI
```

**Flow 2: Venture → Holding Company (Capital Return)**
```
Venture generates $10K/mo profit
  ↓
Holding company takes management fee (20%)
  ↓
Investor gets distribution (80% to LPs)
  ↓
HOLDING COMPANY REVENUE: $2K/mo
  ↓
Capital OS reinvests $5K into next venture, reserves $5K
```

**Flow 3: VEX → Decision Intelligence (No Direct Revenue)**
```
VEX shows: "Investor X knows founder Y who can help Venture Z"
  ↓
Relationship connection made
  ↓
Venture Z closes deal worth $50K
  ↓
VEX gets CREDIT but not PAYMENT
  ↓
VEX Role: Increase decision quality, reduce friction
  ↓
Holding company benefits via better venture outcomes
```

### 3.4 Venture Independence vs Company Brain Coordination

| Aspect | Venture Autonomous | Company Brain Role | VEX Role |
|--------|------|---|---|
| **Product Design** | ✅ Venture-specific | ❌ Not involved | Reference industry patterns |
| **Payment Processing** | ✅ Stripe/payment gateway | ❌ Not involved | Track payment timing |
| **Customer Acquisition** | ✅ Sales team + marketing | Coordinate via Growth OS | Show warm intros to prospects |
| **Service Delivery** | ✅ Venture operations | Help with ClickUp scheduling | Link relevant advisors |
| **Revenue Recognition** | ✅ Venture CFO | Sync to holding company books | Track investor cap returns |
| **Unit Economics** | ✅ Venture analytics | Monitor for portfolio health | Forecast venture ROI |
| **Scaling Decision** | ✅ Venture team | Approve capital allocation | Show which people/partners help |

### 3.5 The Critical Boundary: What VEX Does NOT Do

```
❌ VEX does NOT generate venture revenue
❌ VEX does NOT process payments (Stripe does)
❌ VEX does NOT execute service delivery (venture team does)
❌ VEX does NOT hire employees (venture team does)
❌ VEX does NOT contact customers (Growth OS campaigns do)
❌ VEX does NOT close deals (sales team does)

✅ VEX DOES provide relationship context for better decisions
✅ VEX DOES track investor cap allocation and returns
✅ VEX DOES connect warm introductions (people → people → venture)
✅ VEX DOES forecast portfolio ROI and capital efficiency
✅ VEX DOES identify gaps (venture needs advisor, investor, partner)
```

### 3.6 Money Flow Example: OPS-001 Placing a Candidate

```
TIMELINE: Candidate placed in 7 days

Day 1:
  Growth OS: Show staffing campaign to 100 prospects
    ↓
Day 2–3:
  VEX: Show "Employer A knows someone who knows hiring manager at Venture X"
    ↓
Day 4:
  Candidate fills OPS-001 form via Vercel site
    ↓
Day 5:
  Sales call (human, script in ClickUp)
    ↓
Day 6:
  Employer agrees to hire → Stripe processes $2,500
    ↓
Day 7:
  Supabase records payment
  Neo4j updates: OPS-001 +$2,500 revenue, investor equity appreciates
  Growth OS dashboard shows: "1 placement closed, $2,500 ARR"
  
REVENUE: OPS-001 earned $2,500 INDEPENDENTLY (venture product worked)
INTELLIGENCE: VEX showed the warm path (relationship worked)
COMPANY BENEFIT: Holding company now has $2,500 to reinvest or return to LP
```

### 3.7 The Holding Company Flywheel

```
789 Ventures Generate Revenue Independently
  ↓
Holding Company Captures Performance Data (Neo4j + Supabase)
  ↓
VEX Analyzes: Which ventures outperform, which need help
  ↓
Capital OS Reallocates: Fund winners, fix underperformers, shut zombies
  ↓
Company Brain Executes: Moves advisors, introduces partners, approves hires
  ↓
Loop: Better capital allocation → better venture outcomes → higher portfolio return
```

---
