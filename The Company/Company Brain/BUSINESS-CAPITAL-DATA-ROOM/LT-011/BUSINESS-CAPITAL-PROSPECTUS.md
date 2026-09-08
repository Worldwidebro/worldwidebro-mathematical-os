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

---

## 7. Future State: Where We're Going (Year 1–5 Strategic Vision)

### 7.1 Vision & Strategic Mission

**CarrierDispatch's Five-Year Strategic Arc:**

Year 1 (2027): Establish SaaS product-market fit with $365K revenue ($185K SaaS + $135K factoring fees + $45K escrow), deploy 450 power units on platform, prove 88.5% gross margins. Target: 150 active carrier fleets, <24 hour payout proving model works.

Year 3 (2029): $5.3M revenue ($2.15M SaaS + $2.6M factoring + $540K escrow), 7,200+ trucks on platform, 88.5% gross margins maintained. Become the operating system for independent trucking industry. Target: 1,800 carrier fleets, national presence in all major freight lanes.

Year 5 (2032): $14M+ revenue, 3,500+ trucks, mission to become logistics OS (like McKesson for supply chain). Strategic acquisition target for trucking giants (J.B. Hunt, Schneider, Swift) or PE consolidation ($150–400M valuation).

**Long-term Moat:** Permanent advantage through (1) embedded factoring—instant payout creates switching costs via embedded financial services; (2) fleet data—5+ years of GPS + load data enables better routing than generic maps; (3) network effects—more trucks = better load matching = faster payouts = more trucks.

### 7.2 Future Customer Segments & LTV Evolution

**Year 1–5 Primary Target:** Independent motor carriers (1–50 trucks), owner-operators, regional freight brokers, specialty haulers.

**Tier 1** (5–50 truck fleets): Regional carriers with stable lanes, willing to invest in tech
**Tier 2** (1–5 independent trucks): Owner-operators, high volume seeking better loads
**Tier 3** (Brokers/3PLs): Freight intermediaries using platform to dispatch to carrier network

**Customer LTV Projection:**
- Year 1: $4K–$8K per fleet (annual SaaS + factoring revenue)
- Year 3: $12K–$25K per fleet (SaaS + factoring + marketplace commissions)
- Year 5: $40K–$100K+ per fleet (full stack: SaaS + fintech + load matching + maintenance ecosystem)

**CAC Payback:** 2–3 months (fast because factoring ROI justifies cost). CAC $400–$800, ARPU $1,000–$2,000/month per fleet.

### 7.3 Future Products & Service Expansion

**Phase 1 (Q1–Q2 Year 1):** Core TMS, embedded factoring (0.60%), PoD verification. Revenue: $365K.

**Phase 2 (Q3 Year 1–Q2 Year 2):**
- **Load Matching Engine:** AI-driven load board integration (DAT, Truckstop, Uber Freight), skip broker fees entirely. Revenue: $30–$100/load commission = $500K–$1M/year.
- **Fuel Card Partnerships:** Negotiate $0.03–$0.05/gallon discounts through volume aggregation. Revenue: $50K–$200K/year in rebates.

**Phase 3 (Q3 Year 2–Q2 Year 3):**
- **Insurance Marketplace:** Commercial general liability, workers' comp, physical damage. Commission: 5–10% = $200K–$600K/year.
- **Predictive Maintenance:** IoT sensors on trucks, predictive alerts before breakdowns. Revenue: $50–150/month per truck = $300K–$1M/year.
- **Financial Services:** Micro-loans for drivers, asset financing for truck purchases. Revenue: $200K–$800K/year.

**Phase 4 (Year 3+):** Adjacent logistics—construction equipment transport, temp labor logistics, specialized hazmat, refrigerated goods.

### 7.4 Revenue & Economics Evolution

**Year 1 → Year 5 Revenue Trajectory:**
- Year 1: **$365K** ($185K SaaS + $135K factoring + $45K escrow)
- Year 3: **$5.3M** ($2.15M SaaS + $2.6M factoring + $540K escrow)
- Year 5: **$14M+** ($3.5M SaaS + $7M factoring + $1.5M load matching + $1.5M fintech/insurance + $0.5M other)

**Unit Economics:**
- CAC: $400–$800 (partner-driven, low paid acquisition)
- ARPU: $1,000–$2,000/month per fleet
- Gross LTV: $60K–$200K (5–10 year cohort, 100x LTV/CAC ratio)
- Gross Margin: 88.5%+ (SaaS model scales without incremental delivery costs)
- Profitability Path: Break-even Month 4–5 (high-margin embedded fintech model)

**Pricing Evolution:**
- Year 1: $49–$149/month SaaS + 0.60% factoring fee
- Year 3: $150–$350/month SaaS + 0.50% factoring + load commissions
- Year 5: Premium tiers ($500–$1,500/month), white-label (OEMs, load boards), enterprise pricing

### 7.5 Geographic & Vertical Expansion Strategy

**Geographic Rollout:**
- Year 1: Southeast US (high truck density, low tech adoption), target major freight corridors (Charlotte, Atlanta)
- Year 2: Midwest + Southwest (replicate playbook, expand freight lane coverage)
- Year 3: National presence (all major trucking corridors, coast-to-coast)
- Year 4–5: Canada (NAFTA integration, shared carrier networks)

**Vertical Expansion (Specialty Hauling):**
- Hazmat (3–5% of fleet, highest regulatory barrier + highest pay)
- Temp-controlled (pharmaceutical cold-chain, food distribution)
- Drayage (rail/port operations, highest margins)
- Construction equipment transport (specialization from CON-001 integration)

**TAM:** $50B+ SaaS + fintech opportunity (US trucking industry $900B+, SaaS penetration <2%).

### 7.6 Capital Strategy & Funding Roadmap

**Year 1 Capital Requirement:** $1.9M (SBA Express $500K + Equity $750K + Factoring Revolver $500K + SBIR $175K)

- SBA Express: $500K (sales, integrations, support team)
- Seed Equity: $750K (product development, geographic expansion)
- Embedded Factoring Revolver: $500K (fund carrier payouts, self-liquidating via load fees)
- USDOT SBIR Grant: $175K (safety technology, compliance)

**Funding Sources:**
- SBA Express: $500K (current)
- Seed Equity: $750K (current)
- Series A (Year 2): $3–5M (geographic expansion, team 15→35, fintech platform)
- Series B (Year 3): $15–20M (national scale, load marketplace, insurance integration)

**Capital Allocation:**
- Sales/Carrier Acquisition: 35%
- Product/Tech: 30% (route optimization, telematics, integrations)
- Operations/Support: 20%
- Contingency: 15%

**Valuation Trajectory:**
- Seed: $3–4M post-money (current)
- Series A: $15–20M (Year 2, $600K SaaS ARR)
- Series B: $60–80M (Year 3, $2M+ ARR)
- Exit: $150–400M (10–30x revenue multiple for SaaS + fintech combo)

### 7.7 Series A & Acquisition Readiness Criteria

**Series A Proof Points (Year 2):**
- $600K SaaS ARR (proven recurring model)
- 450+ active trucks (scale proof)
- $200K+ monthly factoring volume (fintech traction)
- 20%+ month-over-month growth (hypergrowth phase)
- 6+ states operational (geographic repeatability)

**Strategic Acquisition Readiness (Year 3–4):**
- $2M+ ARR ($1.2M+ SaaS recurring)
- 2,500+ trucks on platform (network density)
- 88.5%+ gross margins maintained (profitability proof)
- Embedded in 3+ ancillary services (load matching, insurance, maintenance)

**Likely Acquirers:** J.B. Hunt, Schneider Electric, Swift Transportation (trucking giants seeking SaaS/fintech layer); Caterpillar, Komatsu (equipment OEMs seeking logistics intelligence); Trimble, Samsara (fleet management platforms seeking TMS integration); PE roll-ups (trucking consolidation plays).

### 7.8 Team & Organizational Evolution

**Year 1 Team (15 people):**
- CEO, VP Sales, VP Product, VP Operations, CTO, 2 Integration Engineers, 2 Dispatch Support, 2 Data Analysts, CFO, 1 Sales Rep

**Year 3 Team (35 people):**
- Expanded sales team: 8–10 regional carrier acquisition managers
- Operations: 4–5 (24/7 dispatch center, QA, compliance)
- Product: 5–6 engineers (TMS, telematics, marketplace, AI)
- Finance/Admin: 2–3 (controller, accountant, HR)
- Data/Analytics: 2–3 (load optimization, predictive modeling)

**Culture:** Data-driven, carrier-first mentality (understand trucking deeply), fast-moving (weekly feature releases). Remote-first with regional dispatch hubs.

### 7.9 Technology & AI/ML Roadmap

**Year 1–3 Automation Priorities:**
1. **ML Route Optimization:** Vehicle Routing Problem (VRP) solver reduces deadhead by 15–20% (Year 1, already in progress)
2. **Predictive Dispatch:** AI suggests best loads for each truck based on history (Year 1–2)
3. **Real-Time Telematics:** GPS breadcrumbs → predictive ETA, fuel consumption forecasting (Year 1)
4. **Anomaly Detection:** Detect unusual driving patterns, unsafe behavior (Year 2)
5. **Surge Pricing:** Dynamic load pricing based on demand + supply (Year 3)

**Tech Stack:**
- Frontend: React, React Native (carrier mobile app, broker dashboard)
- Backend: Node.js/Express or Python/Django
- Data: PostgreSQL (transactional), BigQuery (analytics), Redis (real-time dispatch)
- AI/ML: OR-Tools for route optimization, TensorFlow for demand forecasting
- Infrastructure: AWS multi-region, Kubernetes, spatial APIs (MapBox, Google Maps)

**Security & Compliance:**
- TLS 1.3, AES-256 at rest
- USDOT compliance (ELDs, safety regs)
- Carrier data privacy (DOT regulations)
- SOC 2 Type II (Year 1–2)

**Data Moat:** 5+ years of GPS breadcrumbs + load history = unique understanding of trucking network efficiency; enabling better routing, pricing, and predictive maintenance than any competitor can match.

### 7.10 Long-Term Strategy & Exit Path

**Primary Exit Path (Preferred):** Acquisition by trucking giant (J.B. Hunt, Schneider, Swift) or PE-backed consolidation play (Year 5–7, $150–400M valuation).

**Competitive Threats & Defenses:**
- Samsara entering TMS space → Our advantage: dedicated carrier focus (not just fleet tracking), embedded fintech (they don't have it), 12-engine architecture (more robust than generic TMS)
- Load boards (DAT, Uber Freight) adding TMS → We don't compete on loads, we integrate with them; our moat is fintech + optimization, not load supply
- OEMs (Volvo, Daimler) integrating TMS into vehicles → They focus on hardware; we focus on software + network effects

**Moat Layers (in order of strength):**
1. **Embedded Factoring** (Tier 1): Instant payout creates financial switching cost; competitors can't replicate without fintech partnerships (6–12 month replication)
2. **Fleet Data** (Tier 1): 5+ years of GPS + load data = better routing than maps (18+ month replication time)
3. **Network Effects** (Tier 2): More carriers → better load matching → faster payouts → more carriers (virtuous cycle, 2–3 year cycle)
4. **Carrier Density** (Tier 2): 2,500+ trucks creates network liquidity competitors can't replicate (2+ year cycle)

**Standalone Path (Low Probability):** Build to $50–100M revenue, consider strategic hold for dividend income if not acquired (SaaS+fintech is inherently profitable once scaled).

**International Expansion (Year 4–5):** Canada (NAFTA integration, shared carrier networks), Mexico (emerging trucking market). Requires regulatory compliance (DOT-equivalent, peso clearing).

**Strategic Partnerships:** White-label integration with load boards (DAT, Truckstop, Uber Freight, Amazon Relay), OEM partnerships (Volvo, Daimler, Freightliner for in-cab integration), fintech partners (Stripe, Cross River Bank for lending).

**Founder's Legacy:** Build operating system for independent trucking (currently fragmented, underserved by enterprise TMS). Enable smaller carriers to compete with megacarriers through technology. Reduce $12B/year wasted on empty deadhead through better routing.

---

## 8. Exit Strategy & Investor Returns

**Debt Repayment:** SBA Express loan ($500K) is repaid via cash flow with 1.98x DSCR in Year 1, improving to 45.09x by Year 3. Embedded factoring revolver is self-liquidating.

**Investor Return:** For seed equity investors ($750K at $3–4M post-money), CarrierDispatch targets **5x–8x MOIC** via acquisition by trucking conglomerate or PE roll-up (Year 5–7, $150–400M) leveraging the recurring SaaS + embedded fintech model.

---

## 99. Knowledge Graph & Wiki Links
- **Enterprise Blueprint:** [[../../../.gemini/antigravity/brain/967faccb-83a2-4a79-bb59-5a54ffb7969e/family_enterprise_blueprint.md|Family Enterprise Architecture Blueprint]]
- **Taxonomy Group:** [[Sector Taxonomy]]
- **Primary Domains:**
  - [[01_IDENTITY/COMPANY-PROFILE.md|Corporate Identity]]
  - [[05_FINANCIAL/3-YEAR-PRO-FORMA.md|Financial Pro Forma]]
  - [[14_LOANS/LOAN-PACKAGE.md|Commercial Loan Underwriting]]
  - [[99_INDEX/CAPITAL-READINESS-SCORECARD.md|Capital Readiness Scorecard]]
