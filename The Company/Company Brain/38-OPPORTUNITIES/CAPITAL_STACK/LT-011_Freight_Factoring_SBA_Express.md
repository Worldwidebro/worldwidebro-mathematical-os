[[STARTHERE]] | [[38-OPPORTUNITIES/CAPITAL_STACK/README|Capital Stack Index]] | [[CAPITAL-READINESS-ENGINE]] | [[23-VENTURES/LT-011|LT-011 Venture Spec]] | [[_REGISTRIES/CANONICAL/DISPATCH_OS_CANONICAL_CONTRACT|DispatchOS Contract]]

# 💼 Capital Readiness Dossier: LT-011 — CarrierDispatch / DispatchOS Core

```yaml
facility_id: "CAP-LT-011-FAC-01"
venture_id: "LT-011"
brand_name: "CarrierDispatch / DispatchOS"
legal_entity: "WorldwideBro Fleet OS LLC"
jurisdiction: "North Carolina / Delaware"
naics_code: "541511 (Custom Computer Programming) / 488510 (Freight Transportation Arrangement)"
commercial_status: "INCOME_READY (Stripe Active: $49/mo Starter, $149/mo Pro, $250 Escrow)"
primary_credit_request: "$500,000 SBA Express Working Capital Loan"
secondary_credit_request: "$250,000 - $1,000,000 Embedded Freight Invoice Factoring Facility"
tertiary_credit_request: "$250,000 Fleet Equipment Lease Line"
factoring_partners: "Apex Capital Corp / Triumph Financial (TriumphPay) / RTS Financial"
banking_partner: "Huntington National Bank / Live Oak Bank (SBA PLP Lenders)"
target_close_date: "Q1 2027"
underwriting_dscr_target: "1.55x"
readiness_state: "UNDERWRITING_READY"
```

---

## 1. Executive Credit Memorandum & Facility Purpose

### Business Description
WorldwideBro Fleet OS LLC operates **CarrierDispatch / DispatchOS** (`https://lt-011-dispatch-software.vercel.app`), a sovereign cloud-native transportation management system (TMS) and fleet dispatch operating system. Built on a verified 12-engine domain architecture (`services/api/src/domain/`) with an immutable 13-stage lifecycle state machine, CarrierDispatch equips 1-to-25 truck motor carrier fleets and independent owner-operators with enterprise-grade load booking, VRP route optimization, electronic Proof of Delivery (PoD), and automated invoicing.

### Capital Strategy & Credit Facilities

#### 1. Embedded Freight Invoice Factoring Facility (\$250,000 – \$1,000,000 Revolving Volume)
* **The Industry Bottleneck:** Motor carriers pay fuel, driver payroll, and insurance weekly, but commercial shippers and freight brokers pay on Net-30 to Net-60 day terms.
* **The Solution:** Rather than forcing carriers to seek separate high-cost factoring brokers, CarrierDispatch integrates an **embedded non-recourse factoring facility** directly into its `ENG-BILLING` engine. When a driver uploads a digital PoD and signed BOL at stage `Verified`:
  1. The API automatically verifies geofence timestamps and signature hash;
  2. The carrier can click **"Instant Payout (96%)"**;
  3. The factoring partner advances **96% of the load value within 24 hours**;
  4. The factoring partner retains a 2.5%–3.5% fee, with CarrierDispatch earning an embedded **0.50%–0.75% SaaS interchange referral commission** on every funded load.

#### 2. SBA Express Loan (\$500,000)
* **Term:** 10-Year term loan, Prime + 3.0%, 36-hour SBA turnaround.
* **Use of Proceeds:** Software marketing to independent carrier associations (OOIDA), expanding EDI/API integrations with major load boards (DAT, Truckstop.com), and financing customer success teams.

---

## 2. Factoring Provider Term Sheet Comparison

| Term / Feature | Apex Capital Corp | Triumph Financial (TriumphPay) | RTS Financial | Selected Baseline Target |
| :--- | :--- | :--- | :--- | :--- |
| **Advance Rate** | 95% – 97% | 94% – 96% | 95% | **96.0%** |
| **Factoring Fee (Tiered)** | 2.50% – 3.25% | 2.25% – 3.00% | 2.75% – 3.50% | **2.50% Net (Non-Recourse)** |
| **Recourse vs. Non-Recourse** | Non-Recourse | Non-Recourse | Hybrid | **Non-Recourse (Credit Protected)** |
| **Funding Velocity** | Same-Day ACH / Fuel Card | Sub-2-Hour Direct Deposit | Same-Day Wire | **Same-Day ACH / Instant Card** |
| **API Integration Capability** | REST Webhook Available | Full Enterprise API / Webhooks | Custom SFTP | **Full REST Webhook (`POST /api/billing/`)** |
| **CarrierDispatch Revenue Share** | 0.50% of funded gross volume | 0.65% of funded gross volume | 0.40% of funded gross volume | **0.60% Gross Margin Share** |

---

## 3. Three-Year Pro Forma Financial Projection (TMS SaaS + Embedded Factoring)

```text
CONSOLIDATED REVENUE & EBITDA PROJECTIONS (USD)
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

## 4. Underwriting Checklist & Integration Protocol

- [x] **Verified Code Reality:** Production codebase at `Worldwidebro/lt-011-dispatch-software` ([Commit `d2523fd`](https://github.com/Worldwidebro/lt-011-dispatch-software/commit/d2523fd)).
- [x] **Live Billing Endpoints:** Tested `/api/billing/checkout` and `/api/billing/verify-session`.
- [x] **Commercial Tier Verification:** $49/mo Starter, $149/mo Pro, $250 Shipper Escrow deposit verified live at `https://lt-011-dispatch-software.vercel.app`.
- [x] **SBA Form 1919 & 413:** Documented for WorldwideBro Fleet OS LLC entity.
- [x] **Factoring Partner Master Services Agreement (MSA):** Ready for electronic API handshake with TriumphPay / Apex Capital.

---

## 5. Connected Systems & Wiki Links

- **Canonical Operating Contract:** [[_REGISTRIES/CANONICAL/DISPATCH_OS_CANONICAL_CONTRACT|DISPATCH_OS_CANONICAL_CONTRACT.md]]
- **Master Domain Gateway:** [[58-LOGISTICS/58-LOGISTICS|58-LOGISTICS Master Domain Gateway]]
- **Venture Specification:** [[23-VENTURES/LT-011|LT-011 CarrierDispatch TMS]]
- **Data Room Master Prospectus:** [[BUSINESS-CAPITAL-DATA-ROOM/LT-011/COMPILED-MASTER-PROSPECTUS|LT-011 Master Prospectus]]
- **Data Room Operational Reality:** [[BUSINESS-CAPITAL-DATA-ROOM/LT-011/OPERATIONAL-REALITY|LT-011 Operational Reality]]
- **Commercial Sales Pipeline:** [[20-DECISIONS/LT-011-SALES-PIPELINE|LT-011 Sales Pipeline]]
- **Sales Coach & Script:** [[scripts/LT-011-SALES-COACH|LT-011 Sales Coach]]
- **Social Media & Outreach:** [[VENTURE-SOCIAL-EXECUTION-LT-011|LT-011 Social Media Execution]]
- **Grant Action Pack:** [[38-OPPORTUNITIES/GRANTS/LT-011_DOT_EPA_CarrierDispatch|USDOT / EPA SBIR Phase I Action Pack ($175K)]]
- **Capital Readiness Engine:** [[CAPITAL-READINESS-ENGINE|CAPITAL-READINESS-ENGINE.md]]
- **Integrated Legal + Financial Summary:** [[BUSINESS-CAPITAL-DATA-ROOM/5-VENTURE-INTEGRATED-SUMMARY|5-Venture Integrated Legal + Financial Summary]]
- **Sovereign Capital Stack Index:** [[38-OPPORTUNITIES/CAPITAL_STACK/README|38-OPPORTUNITIES/CAPITAL_STACK/README.md]]
- **Canonical Facilities Registry:** [[_REGISTRIES/CANONICAL/CAPITAL_FACILITIES_REGISTRY.yaml]]
