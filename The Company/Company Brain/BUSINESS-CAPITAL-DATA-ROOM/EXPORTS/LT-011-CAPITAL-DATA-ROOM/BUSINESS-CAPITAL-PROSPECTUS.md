# 🏛️ Master Capital Prospectus: WorldwideBro Fleet OS LLC (CarrierDispatch)

```yaml
document_id: "DOC-LT011-001"
venture_id: "LT-011"
company_name: "WorldwideBro Fleet OS LLC"
brand_name: "CarrierDispatch / DispatchOS"
jurisdiction: "North Carolina / Delaware"
naics_code: "541511 / 488510"
date_of_compilation: "2026-09-07"
confidentiality: "CONFIDENTIAL & PROPRIETARY"
target_facilities: "SBA Express ($500K) + Embedded Freight Factoring ($500K Revolver) + USDOT SBIR ($175K) + Seed Equity ($750K)"
live_surface: "https://lt-011-dispatch-software.vercel.app"
repository: "Worldwidebro/lt-011-dispatch-software (Commit d2523fd)"
```

---

## 1. Executive Summary
WorldwideBro Fleet OS LLC operates **CarrierDispatch / DispatchOS** (`https://lt-011-dispatch-software.vercel.app`), a sovereign transportation management system (TMS) and fleet dispatch platform. Engineered on a verified 12-engine domain architecture with an immutable 13-stage lifecycle state machine, CarrierDispatch equips independent motor carriers (1–25 trucks) and freight brokers with algorithmic route optimization, sub-second GPS breadcrumb telematics, mobile Proof of Delivery (PoD), and embedded invoice factoring.

---

## 2. The Market Problem
* **91% of American motor carriers operate six or fewer trucks.**
* Legacy enterprise TMS platforms (McLeod, TMW) cost \$300–\$800/month/truck with steep learning curves, while consumer dispatch boards lack telematics and automated invoicing.
* Small fleets suffer from a **20.8% empty deadhead rate** (costing \$12,000/truck/yr in wasted fuel) and wait **30 to 60 days to get paid** by freight brokers.

---

## 3. The CarrierDispatch Solution & Moat
1. **Lightweight SaaS Pricing:** Starting at **\$49/mo (Carrier Starter)** and **\$149/mo (Fleet Pro)** with instant self-service onboarding.
2. **12-Engine Architecture (`services/api/src/domain/`):** VRP route optimization solver (`ENG-ROUTE`), live geofencing (`ENG-TRACKING`), and 13-stage deterministic state machine (`ENG-JOB`).
3. **Embedded Non-Recourse Factoring:** Carriers can click *"Instant Payout (96%)"* directly inside the app upon PoD verification, receiving funds in <24 hours while CarrierDispatch earns an embedded **0.60% revenue share** on gross freight volume.

---

## 4. Traction & Revenue Evidence
* **Production Status:** Compiled 100% clean with zero errors, pushed upstream to `main` at commit `d2523fd`.
* **Live Commercial Surfaces:** Deployed at `https://lt-011-dispatch-software.vercel.app` with active Stripe billing (`POST /api/billing/checkout`).
* **Documented Commercial LOI Pipeline:**
  - *Southeast Freight Haulers Association (`LOI-LT011-001`):* \$107,280 LOI (60 power units enrolled in Fleet Pro).
  - *Blue Ridge Logistics Brokerage LLC (`LOI-LT011-002`):* \$600,000 commercial freight tender LOI.
* **Total LOI Face Value:** **\$707,280** (Weighted Probability: **\$475,824**).

---

## 5. Three-Year Pro Forma Financial Summary

```text
CONSOLIDATED REVENUE & CASH FLOW (USD)
───────────────────────────────────────────────────────────────────────────────
METRIC                              YEAR 1 (2027)   YEAR 2 (2028)   YEAR 3 (2029)
───────────────────────────────────────────────────────────────────────────────
Active Carrier Fleets on Platform             150             650           1,800
Active Power Units (Trucks)                   450           2,600           7,200

TMS Software Subscriptions ($49/$149)    $185,000        $745,000      $2,150,000
Embedded Factoring Fee Share (0.60%)     $135,000        $780,000      $2,592,000
Shipper Freight Escrow Fees ($250/dep)    $45,000        $195,000        $540,000
TOTAL GROSS REVENUE                      $365,000      $1,720,000      $5,282,000

Direct Tech Infrastructure & Server Costs ($42,000)      ($115,000)      ($285,000)
GROSS PROFIT                             $323,000      $1,605,000      $4,997,000
Gross Margin                                88.5%           93.3%           94.6%

Operating Expenses (Staff, Sales, Support)($185,000)     ($620,000)    ($1,850,000)
OPERATING INCOME (EBITDA)                $138,000        $985,000      $3,147,000

Annual Debt Service (SBA Express $500K)   ($69,800)       ($69,800)       ($69,800)
NET CASH FLOW AFTER DEBT SERVICE          $68,200        $915,200      $3,077,200
DEBT SERVICE COVERAGE RATIO (DSCR)          1.98x          14.11x          45.09x
───────────────────────────────────────────────────────────────────────────────
```

---

## 6. Sources & Uses of Funds (\$500,000 SBA Express Facility)

| Category | Allocation ($) | Detailed Use of Proceeds |
| :--- | :--- | :--- |
| **Sales & Driver Acquisition** | \$175,000 | Regional trucking association partnerships, digital freight acquisition funnels |
| **Integration Engineering** | \$125,000 | EDI 204/214/210 integrations with major load boards (DAT, Truckstop) |
| **Customer Success & 24/7 Dispatch** | \$110,000 | 2 Dedicated bilingual carrier support dispatchers |
| **Working Capital Reserve** | \$65,000 | 6 Months cloud server and telematics spatial API reserves |
| **Legal & Loan Origination** | \$25,000 | Statutory SBA fees and banking legal documentation |
| **TOTAL USE OF PROCEEDS** | **\$500,000** | **Fully Reconciled with Capital Facilities Registry** |
