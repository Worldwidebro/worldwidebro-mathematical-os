[[STARTHERE]] | [[38-OPPORTUNITIES/CAPITAL_STACK/README|Capital Stack Index]] | [[CAPITAL-READINESS-ENGINE]] | [[23-VENTURES/RE-001|RE-001 Spec]] | [[BUSINESS-CAPITAL-DATA-ROOM/RE-001/COMPILED-MASTER-PROSPECTUS|Data Room Prospectus]]

# 💼 Capital Readiness Dossier: RE-001 — WorldwideBro Holdings / Real Estate Deal Engine

```yaml
facility_id: "CAP-RE-001-DSCR-01"
venture_id: "RE-001"
brand_name: "WorldwideBro Holdings / Deal Engine"
legal_entity: "WorldwideBro Holdings LLC"
jurisdiction: "North Carolina / Delaware"
naics_code: "531110 (Lessors of Residential Buildings) / 531311 (Residential Property Managers)"
commercial_status: "INCOME_READY (Stripe Active: $250 Express Underwriting / $499/mo Deal Room)"
primary_credit_request: "$750,000 CDFI Affordable Housing Acquisition Bridge Line"
secondary_credit_request: "$1,500,000 Commercial 30-Year DSCR Rental Portfolio Facility"
tertiary_credit_request: "$500,000 Fix-and-Flip / Bridge-to-Perm Revolver"
cdfi_lenders: "Enterprise Community Loan Fund / LISC Housing Fund / Self-Help Ventures Fund"
dscr_lenders: "Kiavi / Visio Lending / Lima One Capital"
target_close_date: "Q1 2027"
underwriting_dscr_target: "1.35x"
readiness_state: "UNDERWRITING_READY"
```

---

## 1. Executive Credit Memorandum & Real Estate Strategy

### Business Description
WorldwideBro Holdings LLC operates an automated **Real Estate Deal Engine and Portfolio Management Platform** (`https://re-001-worldwidebro-holdings.vercel.app`). The venture synthesizes municipal tax records, code violation registries, probate filings, and property appraisal data to identify off-market, distressed single-family and small multifamily residential properties. By coupling proprietary data extraction with in-house trade contracting (`CON-001`), WorldwideBro Holdings acquires, rehabilitates, and operates residential properties at a 25%–35% discount to fair market value, prioritizing workforce affordable housing.

### Credit Facilities Overview

#### 1. CDFI Affordable Housing Acquisition Bridge Line (\$750,000)
* **Purpose:** Provides immediate, patient acquisition capital to purchase distressed or tax-delinquent single-family homes before they are acquired by speculative institutional equity firms.
* **Terms:** 24-Month revolving line, 4.0% interest-only, advancing **up to 85% of Purchase Price + 100% of verified renovation budget**.
* **Impact Covenant:** At least 60% of acquired units must be restricted to tenants earning ≤80% of Area Median Income (AMI) or enrolled in Section 8 housing choice voucher programs.

#### 2. Commercial 30-Year DSCR Portfolio Takeout Facility (\$1,500,000)
* **Underwriting Mechanism:** DSCR loans qualify **based solely on property rental cash flow**, not personal W-2 income or personal tax returns:
  $$\text{DSCR} = \frac{\text{Gross Monthly Rental Income}}{\text{Principal} + \text{Interest} + \text{Taxes} + \text{Insurance} + \text{HOA (PITIA)}} \ge 1.25\times$$
* **Terms:** 30-Year fixed amortizing, 6.75%–7.25%, non-recourse with standard carve-outs.

---

## 2. Acquisition & Renovation Model: 5-Property Seed Portfolio

| Property Type | Acquisition Cost | Renovation Budget (CON-001) | Total Cost Basis | Post-Rehab Appraised Value (ARV) | Projected Monthly Rent | Monthly PITIA Debt Service | Individual Property DSCR |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Single Family (3/2) #1 | \$110,000 | \$35,000 | \$145,000 | \$215,000 | \$1,750 | \$1,180 | **1.48x** |
| Single Family (3/1) #2 | \$95,000 | \$40,000 | \$135,000 | \$195,000 | \$1,600 | \$1,090 | **1.47x** |
| Single Family (4/2) #3 | \$130,000 | \$45,000 | \$175,000 | \$260,000 | \$2,100 | \$1,420 | **1.48x** |
| Duplex (2/1 + 2/1) #4 | \$160,000 | \$50,000 | \$210,000 | \$310,000 | \$2,600 | \$1,710 | **1.52x** |
| Single Family (3/2) #5 | \$105,000 | \$30,000 | \$135,000 | \$200,000 | \$1,650 | \$1,100 | **1.50x** |
| **PORTFOLIO TOTALS** | **\$600,000** | **\$200,000** | **\$800,000** | **\$1,180,000** | **\$9,700/mo** | **\$6,500/mo** | **1.49x Aggregate** |

---

## 3. Three-Year Pro Forma Financial Projection (Rental Cash Flow + SaaS Deal Room)

```text
CONSOLIDATED INCOME STATEMENT & PORTFOLIO VALUATION (USD)
───────────────────────────────────────────────────────────────────────────────
METRIC                              YEAR 1 (2027)   YEAR 2 (2028)   YEAR 3 (2029)
───────────────────────────────────────────────────────────────────────────────
Residential Rental Units Under Mgmt            10              32              75
Gross Annual Rental Income               $194,000        $640,000      $1,560,000
Deal Room SaaS Subscriptions ($499/mo)    $59,880        $179,640        $359,280
Underwriting Fee Revenue ($250/eval)      $25,000         $60,000        $125,000
TOTAL GROSS REVENUE                      $278,880        $879,640      $2,044,280

Property Taxes, Insurance & Maintenance   ($58,200)      ($185,000)      ($445,000)
Operating SG&A & Tech Infrastructure      ($65,000)      ($145,000)      ($285,000)
NET OPERATING INCOME (NOI)               $155,680        $549,640      $1,314,280

Annual Long-Term DSCR Debt Service       ($78,000)       ($257,000)      ($620,000)
NET CASH FLOW AFTER DEBT SERVICE          $77,680        $292,640        $694,280
PORTFOLIO DEBT SERVICE COVERAGE (DSCR)      1.99x           2.13x           2.12x
(Lender Minimum Target: 1.25x — Fully Surpassed)

TOTAL REAL ESTATE PORTFOLIO VALUE      $2,100,000      $6,800,000     $16,500,000
PORTFOLIO NET EQUITY (Assets - Debt)     $950,000      $3,100,000      $7,800,000
───────────────────────────────────────────────────────────────────────────────
```

---

## 4. Underwriting Checklist & Regulatory Documentation

- [x] **Verified Code Base:** Production commit `a761e80` in `Worldwidebro/re-001-worldwidebro-holdings`.
- [x] **Live Surface & Commercial Pricing:** Verified live at `https://re-001-worldwidebro-holdings.vercel.app` ($250 Underwriting / $499/mo Deal Room).
- [x] **Database & Schema Architecture:** Complete 40-table PostgreSQL schema in `DATABASE_SCHEMA.sql` tracking properties, leases, debt schedules, and maintenance.
- [x] **CDFI Affordability Compliance Plan:** 60% workforce AMI tenant rent cap covenants drafted.
- [x] **Contractor Synergy Verification:** Construction and rehabilitation scopes executed directly by `CON-001` (ACE Construction & Contracting LLC).

---

## 5. Connected Systems & Wiki Links

- **Capital Stack Master Index:** [[38-OPPORTUNITIES/CAPITAL_STACK/README|38-OPPORTUNITIES/CAPITAL_STACK/README.md]]
- **Venture Specification:** [[23-VENTURES/RE-001|RE-001 Venture Spec]]
- **Data Room Master Prospectus:** [[BUSINESS-CAPITAL-DATA-ROOM/RE-001/COMPILED-MASTER-PROSPECTUS|RE-001 Master Prospectus]]
- **Commercial Sales Pipeline:** [[20-DECISIONS/RE-001-SALES-PIPELINE|RE-001 Sales Pipeline]]
- **Capital Readiness Engine:** [[CAPITAL-READINESS-ENGINE|CAPITAL-READINESS-ENGINE.md]]
- **Multi-Venture Summary:** [[BUSINESS-CAPITAL-DATA-ROOM/5-VENTURE-INTEGRATED-SUMMARY|5-Venture Integrated Summary]]
- **Canonical Facilities Registry:** [[_REGISTRIES/CANONICAL/CAPITAL_FACILITIES_REGISTRY.yaml]]
