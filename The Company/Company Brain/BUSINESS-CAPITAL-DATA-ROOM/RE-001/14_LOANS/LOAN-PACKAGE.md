# 🏦 Commercial Credit & Loan Package: WorldwideBro Holdings LLC

```yaml
document_id: "DOC-RE-002"
borrower_legal_name: "WorldwideBro Holdings LLC"
brand_name: "WorldwideBro Holdings / Real Estate Deal Engine"
jurisdiction_of_organization: "Delaware / North Carolina"
naics_code: "531110 (Lessors of Residential Buildings) / 531311"
primary_credit_request: "$750,000 CDFI Affordable Housing Acquisition Bridge Revolver"
secondary_credit_request: "$1,500,000 Commercial 30-Year DSCR Rental Portfolio Facility"
target_institutions: ["Enterprise Community Loan Fund", "LISC Housing Fund", "Self-Help Credit Union", "Kiavi", "Visio Lending"]
blended_portfolio_dscr: "1.49x (Seed Assets) / 1.99x (Year 1 Aggregate)"
minimum_covenant_dscr: "1.25x"
collateral: "First-Lien Recorded Deed of Trust on Residential Real Estate"
```

---

## 1. Credit Request & Financing Facility Structure

### Facility A: \$750,000 CDFI Affordable Housing Acquisition Bridge Line
* **Purpose:** Immediate acquisition and rehabilitation funding for off-market, distressed single-family homes discovered via the Deal Engine before public foreclosure auctions.
* **Structure:** 24-Month revolving line, interest-only monthly payments at 4.00% fixed interest.
* **Advance Rate:** Up to 85% of Purchase Price + 100% of verified rehabilitation budget (max 75% of After-Repair Value).
* **Impact Restriction:** Minimum 60% of units leased to tenants earning $\le 80\%$ Area Median Income (AMI) or receiving Section 8 vouchers.

### Facility B: \$1,500,000 Commercial 30-Year Fixed DSCR Takeout Facility
* **Purpose:** Long-term permanent mortgage financing refinancing the CDFI bridge line once properties are fully renovated, stabilized, and tenanted.
* **Structure:** 30-Year fully amortizing fixed rate (6.85%), non-recourse with standard bad-boy carveouts.
* **Underwriting Criterion:** Property-level Debt Service Coverage Ratio (DSCR) $\ge 1.25\times$:
  $$\text{DSCR} = \frac{\text{Gross Monthly Rent}}{\text{Principal} + \text{Interest} + \text{Taxes} + \text{Insurance} + \text{Reserves (PITIA)}}$$

---

## 2. Seed Portfolio Underwriting Schedule (5 Immediate Target Properties)

| Property Identifier | Property Type | Acquisition Cost | Rehab Budget (CON-001) | Total Cost Basis | Post-Rehab Value (ARV) | Monthly Rent | Monthly PITIA Debt | Property DSCR |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Parcel A-101** | Single Family (3/2) | \$110,000 | \$35,000 | \$145,000 | \$215,000 | \$1,750 | \$1,180 | **1.48x** |
| **Parcel B-204** | Single Family (3/1) | \$95,000 | \$40,000 | \$135,000 | \$195,000 | \$1,600 | \$1,090 | **1.47x** |
| **Parcel C-308** | Single Family (4/2) | \$130,000 | \$45,000 | \$175,000 | \$260,000 | \$2,100 | \$1,420 | **1.48x** |
| **Parcel D-412** | Duplex (2/1 + 2/1) | \$160,000 | \$50,000 | \$210,000 | \$310,000 | \$2,600 | \$1,710 | **1.52x** |
| **Parcel E-515** | Single Family (3/2) | \$105,000 | \$30,000 | \$135,000 | \$200,000 | \$1,650 | \$1,100 | **1.50x** |
| **TOTALS** | **5 Residential Units** | **\$600,000** | **\$200,000** | **\$800,000** | **\$1,180,000** | **\$9,700/mo** | **\$6,500/mo** | **1.49x Blended** |

---

## 3. Repayment Waterfall & Credit Verification

### Primary Source of Repayment: Stable Rental Cash Flow
* **Direct Voucher Backing:** Contractual Section 8 agreements (`LOI-RE-002` with Regional Housing Authority) provide guaranteed direct ACH rental deposits from HUD, mitigating default risk.
* **Net Operating Income (NOI):** Year 1 stabilized NOI of **\$155,680** supports \$78,000 in annual long-term debt service at an aggregate **1.99x DSCR**.

### Secondary Source of Repayment: Real Estate Equity Cushion
* **Conservative LTV:** Total cost basis (\$800,000) represents only **67.8% of After-Repair Value** (\$1,180,000), providing lenders with an immediate \$380,000 (32.2%) equity safety cushion upon project stabilization.

### Tertiary Source of Repayment: Deal Room SaaS & Underwriting Fees
* Recurring software revenues (\$59,880/yr Deal Room SaaS + \$25,000 underwriting fees) provide operational liquidity completely decoupled from property vacancies.

---

## 4. Lender Due Diligence & Document Verification Checklist
- [x] **Entity Organization:** Certificate of Formation, Operating Agreement, and active EIN.
- [x] **Property Management Architecture:** 40-table relational database schema in `DATABASE_SCHEMA.sql`.
- [x] **Contractor Alignment:** Fixed-price construction master agreement executed with affiliate `CON-001`.
- [x] **Institutional Pipeline:** \$705,000 in signed LOIs (`LOI-RE-001` CLT co-acquisition, `LOI-RE-002` housing authority).
- [x] **Insurance Standards:** Builder's risk during rehabilitation converting to standard DP-3 landlord hazard and \$2,000,000 commercial general liability policy.
