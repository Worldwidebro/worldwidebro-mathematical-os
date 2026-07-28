# Sector Interoperability Map — How All 38 Sectors Flow Into Each Other

**Created:** 2026-07-25 | **Status:** Tier 2 Complete

**Purpose:** Map which repos connect each sector so work can flow seamlessly with unified APIs.

---

## Hub Architecture

All 38 sectors connect through **5 core hubs**:

1. **iza-os-financial-core** — Capital, payments, ledger (FIN layer)
2. **vex-core** — Work orchestration (TECH layer)
3. **sta-001-staffing-core** — Labor allocation (HR layer)
4. **iza-os-platform-core** — APIs, infrastructure (TECH layer)
5. **documenso** — Contracts, agreements (LEGAL layer)

**Principle:** Every sector API routes through these hubs.

---

## Layer-by-Layer Data Flow

### LAYER 8: CAPITAL ← → LAYER 7: ENABLE ← → LAYER 6: LABOR

```
FIN-001 (iza-os-financial-core)
├─ /api/capital-request → deploys to all 38 sectors
├─ /api/ledger → records all transactions
├─ /api/credit-score → GenixBank credit decisions
└─ /api/payment-gateway → Stripe, ACH, wire

VEX-CORE (vex-core)
├─ /vex/opportunities → "I need 10 workers"
├─ /vex/delegations → "Accepted, executing now"
├─ /vex/margins → "Captured $5K at this handoff"
└─ /vex/health → Real-time network status

STA-001 (sta-001-staffing-core)
├─ /staffing/available-workers → Filter by skill
├─ /staffing/placement → Assign worker to venture
├─ /payroll/hours → Report hours worked
└─ /staffing/performance → Track quality
```

---

### LAYER 5: PRODUCTION → LAYER 4: DISTRIBUTION

```
CON-001 (con-001-ace-construction-core)
├─ /production/order → "Need 20 electricians + materials"
├─ /production/labor → Calls STA-001 /staffing/placement
├─ /production/materials → Calls MFG-* for supplies
└─ /production/delivery → Calls TRANS-001 for shipping

MFG-* (mfg-*-production-core)
├─ /production/capacity → "Can make 1000 units/mo"
├─ /production/quote → Material cost for CON-001
├─ /production/supply → Calls AGRI-*, MIN-* for inputs
└─ /production/ship → Calls TRANS-001

TRANS-001 (trans-001-logistics-core)
├─ /transportation/quote → Shipping cost
├─ /transportation/track → Real-time GPS tracking
├─ /transportation/deliver → Proof of delivery
└─ /transportation/invoice → FIN-001 /api/charge
```

---

### LAYER 3: SALES → LAYER 2: OPTIMIZATION

```
COMMERCE-* (commerce-*-platform)
├─ /commerce/catalog → Import from MFG-*
├─ /commerce/checkout → FIN-001 /api/charge
├─ /commerce/fulfillment → TRANS-001 /transportation/order
└─ /commerce/analytics → DATA-* /data/analytics

RET-* (retail-*-operations)
├─ /retail/inventory → Source from MFG-* or COMMERCE-*
├─ /retail/pos → FIN-001 payment processing
├─ /retail/staff → STA-001 hiring
└─ /retail/marketing → MEDIA-* /media/content

HOS-* (hospitality-*-booking)
├─ /hospitality/properties → RE-001 /properties/list
├─ /hospitality/booking → Calendar + payment
├─ /hospitality/staff → STA-001 hiring
└─ /hospitality/food → AGR-* /agriculture/supply

MEDIA-* (media-*-content)
├─ /media/generate → Create marketing for any sector
├─ /media/distribute → Post to all channels
├─ /media/analytics → Track engagement
└─ /media/recommend → Suggest next content

DATA-* (data-*-analytics)
├─ /data/dashboard/{sector} → Real-time KPIs
├─ /data/forecast → Predict demand
├─ /data/optimize → Pricing recommendations
└─ /data/report → Monthly intelligence
```

---

### LAYER 1: OPERATIONS & REAL ESTATE

```
RE-001 (re-001-property-management)
├─ /properties/register → Add property from CON-001
├─ /properties/rent → HOS-* booking
├─ /properties/refinance → FIN-001 capital unlock
└─ /properties/insurance → INS-* policy management

OPS-001 (ops-001-central-operations)
├─ /operations/ledger-sync → FIN-001 reconciliation
├─ /operations/payroll → STA-001 sync
├─ /operations/sector-health → KPI dashboard
└─ /operations/compliance → Legal + tax tracking
```

---

## Complete API Gateway

**Base:** `api.worldwidebro.com`

```
/auth/*                    → NextAuth (all sectors)
/billing/*                 → FIN-001 subscriptions
/vex/*                     → Orchestration
  ├─ /vex/opportunities    → Discover work
  ├─ /vex/delegations      → Accept/complete work
  ├─ /vex/margins          → Track value capture
  └─ /vex/health           → Network status
  
/sector/{id}/*             → 38 sector APIs
  ├─ /staffing/workers
  ├─ /staffing/placement
  ├─ /construction/projects
  ├─ /manufacturing/quote
  ├─ /transportation/track
  ├─ /hospitality/booking
  ├─ /commerce/checkout
  └─ [33 more sectors...]
  
/data/*                    → Analytics
/media/*                   → Content
/ops/*                     → Operations
/finance/*                 → FIN-001 APIs
  ├─ /finance/capital
  ├─ /finance/credit
  ├─ /finance/payment
  └─ /finance/ledger
```

---

## Central Hub Repos

| Repo | Function | Used By | API Endpoints |
|------|----------|---------|---|
| `iza-os-financial-core` | Capital, payments, ledger | All 38 sectors | /api/capital, /api/charge, /api/ledger, /api/credit |
| `vex-core` | Work orchestration | All 38 sectors | /vex/opportunities, /vex/delegations, /vex/margins |
| `sta-001-staffing-core` | Labor allocation | 15+ service sectors | /staffing/workers, /staffing/placement, /payroll |
| `iza-os-platform-core` | Infrastructure | All 38 sectors | /auth, /api/gateway, /infrastructure |
| `documenso` | Contracts | LEGAL + all sectors | /contracts/generate, /contracts/sign, /contracts/store |

---

## Example: Construction Project End-to-End Flow

```
1. FINANCIAL (FIN-001)
   POST /api/capital {amount: 500000, venture: "CON-001"}
   ← Returns capital allocation ID

2. CONSTRUCTION (CON-001)
   POST /production/order {capital_id: "...", workers: 20}
   → Calls STA-001 + MFG-* + TRANS-001

3. STAFFING (STA-001)
   GET /staffing/available-workers {skill: "electrician", count: 20}
   ← Returns 20 workers, rates $50/hr
   POST /staffing/placement {workers: [IDs], venture: "CON-001", rate: 50}
   → FIN-001 /api/create-payable {amount: 40000, due: "weekly"}

4. MANUFACTURING (MFG-001)
   POST /production/quote {materials: "electrical panels", qty: 100}
   ← Returns $30K quote
   POST /production/order {quote_id: "...", venture: "CON-001"}
   → FIN-001 /api/create-invoice {amount: 30000, due: "30 days"}

5. TRANSPORTATION (TRANS-001)
   POST /transportation/quote {from: "factory", to: "jobsite", weight: 5000}
   ← Returns $5K quote
   POST /transportation/order {quote_id: "..."}
   → FIN-001 /api/charge {amount: 5000}
   → GPS tracking via /transportation/track

6. CONSTRUCTION (CON-001)
   PUT /production/progress {hours: 160, status: "completed"}
   → STA-001 /payroll/finalize {workers: 20, hours: 160}
   → FIN-001 /api/charge {amount: 40000} (labor)
   → FIN-001 /api/margin-capture {amount: 25000} (project profit)

7. REAL ESTATE (RE-001)
   POST /properties/register {project: "CON-001", value: 600000}
   → FIN-001 /api/refinance {property: "...", amount: 200000}
   ← Returns $200K new capital

8. MARKETPLACE (MARKETPLACE-001)
   POST /marketplace/list {property: "...", type: "residential"}
   → MEDIA-001 /media/generate {content_type: "property_listing"}
   → DATA-001 /data/analytics {property_type: "residential"}

9. OPERATIONS (OPS-001)
   POST /operations/ledger-sync {}
   ← All transactions reconciled in FIN-001
   ← Margins calculated: $25K (CON) + $5K (TRANS) + $10K (MFG) = $40K
   → Reinvestment queue updated
   → Next venture auto-funded
```

---

## Monday Launch Verification

**Critical path (5 sectors connected):**

✅ FIN-001 → /api/capital (deploy $100K)
✅ STA-001 → /staffing/workers (find 10 workers)
✅ CON-001 → /production/order (execute project)
✅ RE-001 → /properties/register (own property)
✅ VEX-CORE → /vex/margins (capture $25K margin)

**Test sequence:**
1. POST /vex/opportunities (5 sectors broadcast work)
2. GET /vex/opportunities (agents query for work)
3. POST /vex/delegations (agents accept)
4. PUT /vex/delegations (agents complete + margin log)
5. GET /vex/health (verify flow, margins, no errors)

**Success = all 5 APIs responding + data consistent across repos**
