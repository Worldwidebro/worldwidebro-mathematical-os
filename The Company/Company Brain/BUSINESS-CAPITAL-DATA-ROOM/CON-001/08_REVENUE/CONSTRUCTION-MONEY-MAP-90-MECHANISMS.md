# CON-001: The Construction Money Map — 90 Monetization Mechanisms Across 8 Economic Layers

**Venture:** `CON-001` (ACE Construction & Contracting LLC)  
**Sector:** `SEC-002: Construction & Infrastructure` | **OpCo:** `OpCo-002`  
**Domain:** `08_REVENUE` | **Authority:** System Architecture & Infrastructure Control Plane (`CP-027`)  
**Implementation Engine:** [`src/lib/finance/payment-engine.ts`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/con-001-ace-construction/src/lib/finance/payment-engine.ts)  
**TypeScript Schemas:** [`src/types/payment-business-logic.ts`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/con-001-ace-construction/src/types/payment-business-logic.ts)  
**Automated Unit Tests:** [`src/__tests__/payment-business-logic.test.ts`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/con-001-ace-construction/src/__tests__/payment-business-logic.test.ts) (36 Passing Tests, 99 Project-Wide)

---

## 1. Executive Architecture: The 8 Economic Layers

Construction is not merely a single project delivery fee. Modern institutional general contracting operates as a multifaceted financial engine combining **advisory services, prime contracts, supply chain capture, recurring maintenance, enterprise SaaS, embedded FinTech, specialized public works, and asset ownership equity**.

```mermaid
flowchart TD
    subgraph CapitalStack [The Construction Money Ecosystem - 8 Economic Layers]
        L1[Layer 1: Professional Services & Advisory]
        L2[Layer 2: Core Construction Projects Delivery]
        L3[Layer 3: Supply Chain, Site Services & Procurement]
        L4[Layer 4: Recurring Facility & Property Services]
        L5[Layer 5: Platform, Marketplace & SaaS]
        L6[Layer 6: Construction Finance, FinTech & Risk]
        L7[Layer 7: Specialized & Public Sector Delivery]
        L8[Layer 8: Asset Ownership & Development Equity]
    end

    L1 -->|Upfront Cash & Trust| L2
    L2 -->|Material Inflows| L3
    L2 -->|Handover MSAs| L4
    L2 & L3 -->|Platform Volume| L5
    L3 & L5 -->|Payment & Lending Float| L6
    L2 -->|Statutory & Prevailing Wage| L7
    L2 & L6 -->|Equity & Capital Compounding| L8
```

---

## 2. The 4-Tier Operational Rollout Strategy

To prevent capital depletion and guarantee immediate solvency, monetization follows a strict **operational sequence based on distance-to-cash**:

```mermaid
flowchart LR
    T1[Tier 1: Cash Engine<br/>Distance-to-Cash <= 48h<br/>No Balance Sheet Risk] --> T2[Tier 2: Core Operations<br/>Active Construction Draw Engine<br/>Net-30 Progressive Cycles]
    T2 --> T3[Tier 3: Platform Scale<br/>Marketplace Spread & FinTech<br/>Software & Financing Volume]
    T3 --> T4[Tier 4: Capital Ownership<br/>Equity, BRRRR & Development<br/>Long-Term Wealth Accumulation]
```

- **Tier 1 (Sell Immediately / Cash Engine <= 48h):** Zero balance sheet risk. Instant cash collection via Stripe checkout for upfront advisory, emergency triage, unit turnovers, and small scopes ($299 audits, $1,500 takeoffs, $2,500 expediting, T&M repairs, white-box prep).
- **Tier 2 (Once Customers Active):** Core general contracting. Mobilization deposits (10–20%), AIA G702/G703 progress draws, milestone certifications, change order capture (21% blended markup), and recurring maintenance MSAs.
- **Tier 3 (Operating Volume / Platform):** FinTech and ecosystem leverage. Prime-sub marketplace spread (15–25%), early-pay factoring (2.5% float yield), equipment rental markups, SaaS subscriptions ($79/seat/mo), and loan origination fees.
- **Tier 4 (Capital-Intensive Ownership):** Long-term asset wealth. Joint-venture sweat-equity deals (20–35% equity carry), Build-to-Rent (BTR), BRRRR commercial repositioning, and fix-and-flip capital recycling.

---

## 3. Canonical Master Registry: 90 Monetization Mechanisms

| # | Mechanism Name | Economic Layer | Rollout Tier | Next.js App Route | Primary Database Tables | Role Required | Target Customer ICP | Payment Trigger / Event |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | **Pre-Con Scope & Feasibility Audit** | L1: Advisory | Tier 1 | `/booking/consultation` | `leads`, `consultations` | `client` | Commercial Tenants, Franchisees | Stripe Checkout Instant |
| **02** | **CSI 50-Division Takeoff & Estimating** | L1: Advisory | Tier 1 | `/booking/takeoff` | `estimates`, `takeoffs` | `client` | Real Estate Investors, Third-Party GCs | Stripe Invoicing Net-Receipt |
| **03** | **Permit Expediting & Entitlements** | L1: Advisory | Tier 1 | `/dashboard/permits` | `permits`, `projects` | `client` | Out-of-State Developers, Architects | Fixed Retainer + City Pass-Through |
| **04** | **Construction Management as Agent (CMa)** | L1: Advisory | Tier 1 | `/dashboard/advisory` | `contracts`, `projects` | `contractor` | Institutional Owners, Non-Profits | Monthly Percentage Draw (4.5%) |
| **05** | **Owner's Representative Retainer** | L1: Advisory | Tier 1 | `/dashboard/advisory` | `contracts`, `milestones` | `contractor` | Busy Commercial Building Owners | Monthly Retainer ($5k–$10k/mo) |
| **06** | **Subcontractor Bid Leveling & Packaging** | L1: Advisory | Tier 1 | `/dashboard/bids` | `bids`, `bid_packages` | `contractor` | Independent Developers | Per Bid Package Fee ($2,500) |
| **07** | **Conceptual Budget Modeling & Feasibility** | L1: Advisory | Tier 1 | `/booking/commercial-intake`| `leads`, `estimates` | `client` | Land Acquirers, Commercial Brokers | Upfront Advisory Invoice |
| **08** | **Constructability & BIM Clash Review** | L1: Advisory | Tier 2 | `/dashboard/drawings` | `drawings`, `reviews` | `contractor` | Architectural Engineering Firms | Milestone Review Sign-off |
| **09** | **Value Engineering (VE) Standalone Audit**| L1: Advisory | Tier 2 | `/dashboard/estimates` | `estimates`, `ve_logs` | `contractor` | Budget-Constrained Developers | Flat Audit Fee or 25% of Savings |
| **10** | **Forensic Inspection & Expert Witness** | L1: Advisory | Tier 2 | `/dashboard/inspections`| `inspections`, `evidence` | `contractor` | Insurance Carriers, Law Firms | Hourly Retainer ($350/hr) |
| **11** | **Site Selection & Zoning Due Diligence** | L1: Advisory | Tier 2 | `/dashboard/sites` | `sites`, `due_diligence`| `contractor` | Retail Chains, Medical Groups | Deliverable Acceptance |
| **12** | **Phase 1 ESA & Geotech Coordination Fee**| L1: Advisory | Tier 3 | `/dashboard/projects` | `projects`, `subcontracts`| `contractor`| Ground-Up Commercial Builders | Management Markup on Third-Party |
| **13** | **Lump Sum / Fixed-Price General Contract**| L2: Projects | Tier 2 | `/dashboard/projects` | `contracts`, `projects` | `contractor` | Commercial Owners, Franchisees | Contract Execution & Progress Draws |
| **14** | **Cost-Plus Fixed Percentage Contract** | L2: Projects | Tier 2 | `/dashboard/projects` | `contracts`, `invoices` | `contractor` | High-End Custom Commercial / Res | Audited Direct Costs + 15% Markup |
| **15** | **Cost-Plus Fixed Fee Contract** | L2: Projects | Tier 2 | `/dashboard/projects` | `contracts`, `invoices` | `contractor` | Public Entities, Transparent Owners | Monthly Pro-Rata Management Fee |
| **16** | **Guaranteed Maximum Price (GMP) Shared Savings**| L2: Projects | Tier 2 | `/dashboard/projects` | `contracts`, `gmp_savings`| `contractor`| Corporate Tenants, Banks | Final Audit (30% Savings to GC) |
| **17** | **Unit Price Trade Contracting** | L2: Projects | Tier 2 | `/dashboard/subcontractor`| `unit_prices`, `draws` | `contractor` | Civil / Highway Developers, Multifamily | Measured Work In-Place (SF / LF) |
| **18** | **Time & Materials (T&M) Emergency Repairs**| L2: Projects | Tier 1 | `/dashboard/contractor` | `daily_logs`, `invoices`| `contractor` | Facility Managers, Landlords | Weekly Timesheet + 15% Materials |
| **19** | **Design-Build Turnkey Delivery** | L2: Projects | Tier 2 | `/dashboard/projects` | `contracts`, `milestones` | `contractor` | Turnkey Commercial Clients | Integrated A/E & Build Draws |
| **20** | **Mobilization Deposit Advance Draw** | L2: Projects | Tier 2 | `/dashboard/projects` | `payments`, `contracts` | `contractor` | All Prime Contract Clients | Contract Signing (10%–20% Bank Wire) |
| **21** | **AIA G702/G703 Certified Progress Draws** | L2: Projects | Tier 2 | `/dashboard/pay-applications`| `pay_applications`, `sov`| `contractor`| Institutional Lenders, GCs, Owners | Monthly 25th Pay App Certification |
| **22** | **Milestone-Based Inspection Draws** | L2: Projects | Tier 2 | `/dashboard/milestones` | `milestones`, `payments` | `contractor` | Residential / Small Commercial Owners | City Inspection Pass (Framing, MEP) |
| **23** | **Stored Materials Off-Site Bonded Draw** | L2: Projects | Tier 2 | `/dashboard/pay-applications`| `stored_materials`, `sov`| `contractor`| Large Commercial Projects | Warehouse Receipt & COI Inspection |
| **24** | **Retainage Step-Down (10% to 5%) & Release**| L2: Projects | Tier 2 | `/dashboard/pay-applications`| `pay_applications`, `liens`| `contractor`| Project Owners, Escrow | 50% Completion & Final Punch Release |
| **25** | **Turnkey Specialty Trade Packages** | L2: Projects | Tier 1 | `/dashboard/contractor` | `subcontracts`, `trade_pkgs`| `contractor`| Regional General Contractors | Lump Sum Bid Package Award |
| **26** | **Supplemental Craft Labor Brokerage** | L2: Projects | Tier 1 | `/dashboard/contractor` | `labor_logs`, `timesheets` | `contractor` | Understaffed Commercial GCs | Weekly Net-7 Invoicing |
| **27** | **Bulk Wholesale Material Procurement Markup**| L3: Supply Chain | Tier 3 | `/dashboard/procurement` | `procurement_orders` | `contractor` | Project Subcontractors, Owners | Material Order FOB Jobsite (15%) |
| **28** | **Heavy Equipment Direct Fleet Rental** | L3: Supply Chain | Tier 2 | `/dashboard/equipment` | `equipment_assets`, `leases`| `contractor`| Trade Subs, Third-Party Builders | Weekly / Monthly Asset Invoicing |
| **29** | **Equipment Brokerage Sub-Rental Commission**| L3: Supply Chain | Tier 3 | `/dashboard/equipment` | `brokerage_deals` | `contractor` | Equipment Rental Houses (CAT, Sunbelt) | Rental Order Confirmation (12–15%) |
| **30** | **Roll-Off Dumpster & Waste Logistics** | L3: Supply Chain | Tier 2 | `/dashboard/site-services` | `waste_tickets`, `invoices`| `contractor`| Demolition & Framing Crews | Per-Pull Hauling Fee + Disposal Fee |
| **31** | **Temporary Sanitation Jobsite Leases** | L3: Supply Chain | Tier 2 | `/dashboard/site-services` | `sanitation_logs` | `contractor` | Active Jobsite Subcontractors | Monthly Service Cycle Billed to Job |
| **32** | **Temporary Jobsite Fencing & Barricades**| L3: Supply Chain | Tier 2 | `/dashboard/site-services` | `site_fencing_orders` | `contractor` | Urban Commercial Renovations | Linear Foot Weekly Lease |
| **33** | **Commercial Final Post-Construction Clean**| L3: Supply Chain | Tier 1 | `/dashboard/site-services` | `work_orders`, `invoices` | `contractor` | Handover GCs, Commercial Landlords | Square Footage Completion Rate ($0.35/SF) |
| **34** | **Jobsite Temporary Power & Climate Control**| L3: Supply Chain | Tier 2 | `/dashboard/site-services` | `utility_logs` | `contractor` | Winter / Summer Commercial Builds | Weekly Generator / Fuel Rebill |
| **35** | **Staged Materials Cross-Docking Storage** | L3: Supply Chain | Tier 3 | `/dashboard/warehousing` | `warehouse_inventory` | `contractor` | National Retail Fixture Vendors | Monthly Pallet / Square Foot Storage |
| **36** | **Surplus Materials & Equipment Auctions** | L3: Supply Chain | Tier 3 | `/dashboard/auctions` | `surplus_assets`, `bids` | `admin` | Local Remodelers, Handymen | Settlement of Closed Bid |
| **37** | **Architectural Salvage & Metal Scrap** | L3: Supply Chain | Tier 1 | `/dashboard/site-services` | `scrap_receipts`, `cash` | `contractor` | Scrap Yards, Historic Restorers | Weight Ticket Cash Disbursement |
| **38** | **Small Tool-Crib Rental to Trade Subs** | L3: Supply Chain | Tier 2 | `/dashboard/equipment` | `tool_tracking`, `fees` | `contractor` | On-Site Subcontractors | Daily Equipment Sign-Out Charge |
| **39** | **Commercial Facility Maintenance — Bronze** | L4: Recurring | Tier 2 | `/dashboard/maintenance` | `maintenance_plans`, `invoices`| `contractor`| Small Retailers, Boutiques | Recurring Stripe Subscription ($750/mo) |
| **40** | **Commercial Facility Maintenance — Silver** | L4: Recurring | Tier 2 | `/dashboard/maintenance` | `maintenance_plans`, `invoices`| `contractor`| Medical Clinics, Restaurants | Recurring Stripe Subscription ($1,500/mo) |
| **41** | **Commercial Facility Maintenance — Gold** | L4: Recurring | Tier 2 | `/dashboard/maintenance` | `maintenance_plans`, `invoices`| `contractor`| Corporate Offices, Strip Centers | Recurring Stripe Subscription ($3,000/mo) |
| **42** | **24/7 Emergency Dispatch & Rapid Triage**| L4: Recurring | Tier 2 | `/dashboard/emergency` | `emergency_tickets` | `contractor` | Property Managers, HOAs, Tenants | $450 Dispatch + 1.5x Premium Labor |
| **43** | **Retail / Office "White-Box" Turnovers** | L4: Recurring | Tier 1 | `/dashboard/turnovers` | `turnover_scopes` | `contractor` | Commercial Real Estate Asset Managers | Milestone Invoicing ($4.50–$9/SF) |
| **44** | **Insurance Property Restoration (Xactimate)**| L4: Recurring | Tier 2 | `/dashboard/restoration` | `insurance_claims` | `contractor` | Insured Property Owners, Adjusters | Two-Party Insurance Settlement Check |
| **45** | **Emergency Storm Mitigation & Board-Up** | L4: Recurring | Tier 1 | `/dashboard/restoration` | `emergency_tickets` | `contractor` | Commercial Landlords post-weather | Direct Credit Card / Insurance Assignment |
| **46** | **Multifamily Unit Fast-Track Turns** | L4: Recurring | Tier 1 | `/dashboard/turnovers` | `turnover_scopes` | `contractor` | Apartment Complexes (50+ Units) | Net-15 Invoicing per Finished Unit |
| **47** | **Quarterly Preventive MEP Inspections** | L4: Recurring | Tier 2 | `/dashboard/maintenance` | `inspections`, `schedules`| `contractor` | Commercial Property Owners | Quarterly Recurring Billing |
| **48** | **Roof Maintenance & Leak Warranty Plans** | L4: Recurring | Tier 2 | `/dashboard/maintenance` | `roofing_plans` | `contractor` | Industrial Warehouses, Big Box Stores | Semi-Annual Inspection Draw |
| **49** | **ADA Commercial Accessibility Upkeep** | L4: Recurring | Tier 2 | `/dashboard/compliance` | `ada_audits`, `remediation`| `contractor`| Hospitality, Public Accommodations | Annual Certification Retainer |
| **50** | **Extended 5-Year Workmanship Warranty** | L4: Recurring | Tier 2 | `/dashboard/warranties` | `warranties`, `payments` | `contractor` | High-End Homeowners, Commercial Owners | Project Closeout Warranty Purchase (2.5%) |
| **51** | **Subcontractor Directory Listing Badge** | L5: Platform | Tier 3 | `/dashboard/subcontractor`| `subcontractor_tiers` | `subcontractor`| Local Trade Subcontractors | Monthly Recurring ($99/mo) |
| **52** | **Subcontractor Pro Network Membership** | L5: Platform | Tier 3 | `/dashboard/subcontractor`| `subcontractor_tiers` | `subcontractor`| Active Commercial Subcontractors | Monthly Recurring ($249/mo) |
| **53** | **Subcontractor Enterprise All-Access** | L5: Platform | Tier 3 | `/dashboard/subcontractor`| `subcontractor_tiers` | `subcontractor`| Multi-Crew Subcontractors | Monthly Recurring ($499/mo) |
| **54** | **Pay-Per-Lead Commercial Bid Opportunities**| L5: Platform | Tier 3 | `/dashboard/leads` | `leads`, `lead_transactions`| `subcontractor`| Subs Seeking Backlog Growth | Stripe Instant Lead Unlock ($125/ea) |
| **55** | **Construction OS Seat Licenses** | L5: Platform | Tier 3 | `/dashboard/settings/team` | `organizations`, `subscriptions`| `admin` | Third-Party GCs, Construction Firms | Monthly Seat Charge ($79/user/mo) |
| **56** | **Active Project Cloud Management Fee** | L5: Platform | Tier 3 | `/dashboard/projects` | `project_saas_fees` | `admin` | External General Contractors | Monthly Project Charge ($150/proj/mo) |
| **57** | **Continuous Compliance-as-a-Service (COI)**| L5: Platform | Tier 3 | `/dashboard/compliance` | `compliance_records` | `subcontractor`| Subcontractor Network Members | Annual Credentialing Fee ($350/yr) |
| **58** | **CSI Estimating API & Pricing Catalog Access**| L5: Platform | Tier 3 | `/api/v1/pricing` | `api_keys`, `usage_metering`| `admin` | Estimating Consultancies, Developers | Monthly API Tier ($199–$999/mo) |
| **59** | **Subcontractor Bonding Readiness Audit**| L5: Platform | Tier 3 | `/dashboard/compliance` | `bonding_audits` | `subcontractor`| Growing Subs Needing $1M+ Bonding | Flat Advisory Review ($1,250) |
| **60** | **Digital Plan Room Hosting & Distribution**| L5: Platform | Tier 3 | `/dashboard/drawings` | `planrooms`, `drawings` | `contractor` | Architects, Project Owners | Per-Project Plan Room Fee ($450) |
| **61** | **Material Vendor Specification Placements**| L5: Platform | Tier 3 | `/dashboard/marketplace` | `vendor_sponsorships` | `admin` | Building Product Manufacturers | Quarterly Sponsorship Retainer |
| **62** | **White-Label Construction Portal Licensing**| L5: Platform | Tier 3 | `/dashboard/admin/whitelabel`| `tenants`, `licenses` | `admin` | Regional Homebuilders, Modular Builders | Annual Software Enterprise License |
| **63** | **Commercial Construction Loan Referral** | L6: FinTech | Tier 3 | `/dashboard/financing` | `loan_referrals` | `contractor` | Commercial Property Developers | Lender Closing (50–100 bps) |
| **64** | **Equipment Lease Origination Commission**| L6: FinTech | Tier 3 | `/dashboard/financing` | `lease_referrals` | `contractor` | Subcontractors Buying Fleet Machinery | Lease Signing (1.5% Origination) |
| **65** | **Merchant Card Processing Interchange Share**| L6: FinTech | Tier 3 | `/api/webhooks/stripe` | `payment_ledgers` | `admin` | All Transacting Clients & Subs | Net Interchange Volume (35 bps) |
| **66** | **Prime-to-Sub Contract Arbitrage Spread**| L6: FinTech | Tier 3 | `/dashboard/contractor/bids`| `prime_sub_spreads` | `contractor` | Commercial Project Owners | Progress Billing Spread (15%–25%) |
| **67** | **Subcontractor Quick-Pay Factoring Fee** | L6: FinTech | Tier 3 | `/dashboard/payments` | `factoring_transactions` | `contractor` | Subcontractors Needing Instant Cash | Sub Invoice Draw (2.5% Discount Fee) |
| **68** | **Builder's Risk Insurance Referral** | L6: FinTech | Tier 3 | `/dashboard/insurance` | `insurance_referrals` | `contractor` | Ground-Up Commercial Owners | Policy Binding Referral (10% Comm) |
| **69** | **Surety Bond Brokerage Referral** | L6: FinTech | Tier 3 | `/dashboard/insurance` | `bond_referrals` | `contractor` | Prime Subs Needing P&P Bonds | Bond Execution Referral (15% Comm) |
| **70** | **Lender Draw Inspection Agency Fee** | L6: FinTech | Tier 3 | `/dashboard/inspections` | `draw_inspections` | `contractor` | Commercial Construction Lenders | Per Inspection Report ($850/visit) |
| **71** | **Owner Financing Staged Second Note** | L6: FinTech | Tier 4 | `/dashboard/financing` | `promissory_notes` | `contractor` | Credit-Worthy Commercial Clients | Monthly Principal + 9.5% Interest |
| **72** | **Mechanics Lien Filing Management Service**| L6: FinTech | Tier 2 | `/dashboard/compliance` | `lien_filings` | `subcontractor`| Subcontractors Facing Non-Payment | Flat Statutory Notice Fee ($350) |
| **73** | **Daily Craft Worker Wage Advance Fee** | L6: FinTech | Tier 3 | `/dashboard/payroll` | `earned_wage_advances` | `contractor` | Trade Laborers & Hourly Workers | Transaction Convenience Fee ($3.99/draw) |
| **74** | **Client Credit Card Processing Surcharge**| L6: FinTech | Tier 2 | `/dashboard/checkout` | `payments`, `surcharges` | `client` | Clients Choosing Card Over ACH/Wire | 3.0% Pass-Through Fee on Card Swipe |
| **75** | **Public Works Prevailing Wage Contracting**| L7: Specialized| Tier 2 | `/dashboard/public-works`| `public_contracts` | `contractor` | NCDOT, School Districts, Municipalities| Certified Payroll Pay Applications |
| **76** | **Davis-Bacon Certified Payroll Admin** | L7: Specialized| Tier 2 | `/dashboard/public-works`| `certified_payrolls` | `contractor` | Lower-Tier Subcontractors | Weekly Processing Fee ($150/sub/wk) |
| **77** | **ADA Commercial Accessibility Retrofits** | L7: Specialized| Tier 1 | `/dashboard/projects` | `ada_scopes` | `contractor` | Retail Stores, Medical Offices | Milestone Invoicing (Ramps, Doors, Stalls)|
| **78** | **LEED & Sustainability Certification Admin**| L7: Specialized| Tier 2 | `/dashboard/compliance` | `leed_logs`, `credits` | `contractor` | ESG Corporate Tenants, Green Funds | Milestone Certification Retainer |
| **79** | **Commercial EV Charging & Solar EPC** | L7: Specialized| Tier 2 | `/dashboard/projects` | `energy_projects` | `contractor` | Corporate Headquarters, Fleet Depots | EPC Turnkey Milestone Draws |
| **80** | **Historic Tax Credit Restoration Contract**| L7: Specialized| Tier 3 | `/dashboard/projects` | `historic_scopes` | `contractor` | Historic Downtown Building Owners | Cost-Plus with Certified Historic Records |
| **81** | **Healthcare Cleanroom & Med-Gas Buildouts**| L7: Specialized| Tier 2 | `/dashboard/projects` | `cleanroom_specs` | `contractor` | Ambulatory Surgery Centers, Labs | Premium Guaranteed Maximum Price |
| **82** | **Job Order Contracting (JOC / IDIQ)** | L7: Specialized| Tier 3 | `/dashboard/public-works`| `joc_orders` | `contractor` | State Universities, Military Bases | Pre-Priced RSMeans Task Orders |
| **83** | **Joint Venture Sweat-Equity Carry (20–35%)**| L8: Ownership | Tier 4 | `/dashboard/equity` | `jv_deals`, `equity_ledgers`| `contractor`| High-Net-Worth Real Estate Syndicates | Project Capital Gain at Disposition |
| **84** | **General Partner (GP) Promote & Waterfall**| L8: Ownership | Tier 4 | `/dashboard/equity` | `gp_waterfalls` | `contractor` | Multi-Investor Commercial Syndications | Tiered Hurdle IRR Distributions (> 15% IRR) |
| **85** | **Build-to-Rent (BTR) Turnkey Construction**| L8: Ownership | Tier 4 | `/dashboard/btr` | `btr_developments`, `units` | `contractor` | Institutional BTR Funds / Own Portfolio | Monthly Net Operating Income (NOI) |
| **86** | **Commercial Flex-Warehouse Build-to-Sell** | L8: Ownership | Tier 4 | `/dashboard/development` | `developments`, `sales` | `contractor` | Commercial Real Estate Buyers | Closing Settlement Net Proceeds |
| **87** | **BRRRR Multi-Family Renovation Refinance** | L8: Ownership | Tier 4 | `/dashboard/equity` | `brrrr_properties` | `contractor` | Proprietary ACE Investment Portfolio | Cash-Out 75% LTV Bank Refinance |
| **88** | **Commercial Fix-and-Flip Capital Recycling**| L8: Ownership | Tier 4 | `/dashboard/equity` | `flip_projects` | `contractor` | ACE Trading Capital Account | Realized Sale Profit Net of Debt |
| **89** | **Land Infill Acquisition & Entitlement** | L8: Ownership | Tier 4 | `/dashboard/land` | `land_parcels`, `entitlements`| `contractor`| Regional Homebuilders, Commercial Users| Shovel-Ready Parcel Resale Margin |
| **90** | **Ground Lease Long-Term Development** | L8: Ownership | Tier 4 | `/dashboard/land` | `ground_leases` | `contractor` | National Triple-Net Tenants (Fast Food) | Unsubordinated 99-Year Ground Rent |

---

## 4. Layer-by-Layer Financial Mechanics & Unit Economics

### Layer 1: Professional Services & Advisory Models
- **Pre-Con Audit (\#01):** \$299 flat fee charged instantly via Stripe. Delivers P10/P50/P90 cost range, local permitting timeline, and risk checklist within 24 hours. Credited 100% back if prime contract executed.
- **CSI Takeoffs (\#02):** \$1,500 flat fee for independent 50-division MasterFormat material and labor quantification. Eliminates estimating overhead for developers.
- **Permit Expediting (\#03):** \$2,500 flat retainer plus municipal pass-through fees. Speeds entitlement by 4–8 weeks using established NC municipal contacts.

### Layer 2: Core Construction Projects Delivery
- **Lump Sum (\#13):** Fixed contract sum with 15%–30% target gross margin. Contractor absorbs cost variances or retains 100% of procurement efficiencies.
- **Cost-Plus % (\#14):** Fully audited direct project expenses + 15.0% general contractor overhead and profit markup.
- **GMP Shared Savings (\#16):** Ceiling cap protects owner; contractor absorbs overruns. When delivered under budget, contractor captures 30% of savings as cash incentive.
- **AIA G702/G703 Billing (\#21):** Monthly progress certification. 10% retainage withheld until 50% project completion, stepping down to 5% thereafter.

### Layer 3: Supply Chain & Site Services
- **Procurement Markup (\#27):** 15% markup applied to direct wholesale lumber, steel, and fixture orders negotiated at distributor tier.
- **Fleet Rentals (\#28 & \#29):** Direct daily/weekly rates on owned mini-excavators and scissor lifts. 12%–15% brokerage commission on third-party sub-rentals.
- **Site Logistics (\#30–\#33):** Bundled dumpster pulls (\$650/haul), temporary sanitation (\$45/wk), fencing (\$1.50/LF), and final post-construction cleaning (\$0.35/SF).

### Layer 4: Recurring Facility & Property Services
- **Commercial MSAs (\#39–\#41):** Tiered monthly retainers (Bronze \$750/mo, Silver \$1,500/mo, Gold \$3,000/mo) providing guaranteed SLA emergency dispatch, scheduled quarterly inspections, and repair discounts.
- **Emergency Dispatch (\#42):** \$450 base mobilization fee + \$185/hr premium labor + 20% material markup for urgent commercial triage.
- **White-Box Turnovers (\#43):** Turnkey \$4.50–\$9.00/SF packages for property managers preparing vacant retail spaces for incoming commercial tenants.

### Layer 5: Platform, Marketplace & SaaS
- **Subcontractor Tiers (\#51–\#53):** SaaS tiers for trades ranging from \$99/mo (Basic listing) to \$499/mo (Enterprise all-access with instant bid invites and priority dispatch).
- **Pay-Per-Lead Opportunities (\#54):** \$125 instant unlock for fully qualified commercial scopes with architectural plans attached.
- **Construction OS Licensing (\#55 & \#56):** \$79/seat/mo + \$150/active project/mo charged to third-party general contractors utilizing the platform for pay applications and EVM tracking.

### Layer 6: Construction Finance, FinTech & Risk
- **Financing Referral Commissions (\#63):** 50 to 100 basis points paid by institutional commercial lenders upon closing renovation and construction debt facilities.
- **Marketplace Spread (\#66):** Retaining the 15%–25% gross spread between owner prime contract value and awarded subcontractor package sums.
- **Early-Pay Factoring (\#67):** 2.5% quick-pay discount for disbursing subcontractor invoices within 24 hours of approval rather than standard Net-60 owner draw cycles.
- **Interchange Rev Share (\#65):** 35 basis points platform revenue share on high-volume card and merchant transactions.

### Layer 7: Specialized & Public Sector Delivery
- **Public Works Certified Payroll (\#75 & \#76):** General contracting for government entities with Davis-Bacon prevailing wage compliance, fringe benefit allocations (28.5%), and statutory payment/performance bonding (1.5%).
- **ADA Accessibility Retrofits (\#77):** Fast-track commercial compliance modifications including concrete ramps, motorized entrances, and ADA restroom conversions.

### Layer 8: Asset Ownership & Development Equity
- **JV Sweat-Equity Deals (\#83 & \#84):** Contributing general contracting services, licensing, and management in exchange for a 20%–35% equity stake and 8% preferred return on commercial real estate syndications.
- **Build-to-Rent (\#85):** Constructing multi-door residential flex communities at cost (\$200k/door) while retaining ownership to capture long-term monthly rental cash flow and terminal valuation cap rate upside.
- **BRRRR Refinance (\#87):** Acquire distressed commercial/multifamily, renovate with captive labor, lease to commercial occupancy, and execute a 75% LTV cash-out refinance to pull 100% of invested capital out tax-free while retaining equity.

---

## 5. Verification & Code Alignment Matrix

All calculation algorithms and mathematical models supporting these 90 mechanisms are verified by automated tests in the production repository:

| Capability Group | Core Functions | Verified Test Cases |
| :--- | :--- | :--- |
| **Contract Delivery Models** | `calculateLumpSum`, `calculateCostPlusPercentage`, `calculateCostPlusFixedFee`, `calculateGMPReconciliation`, `calculateUnitPrice`, `calculateTimeAndMaterials` | 7 Tests (Pass) |
| **Billing & Cash Timing** | `calculateMobilizationDeposit`, `calculateRetainageReduction`, `verifyStoredMaterialsDraw`, `calculateFinalRetainageRelease` | 5 Tests (Pass) |
| **Advisory & Pre-Con** | `calculatePreConFee`, `applyPreConContractCredit` | 2 Tests (Pass) |
| **Margin Expansion** | `calculateChangeOrderPrice`, `calculateValueEngineeringSplit`, `calculateEarlyCompletionBonus` | 4 Tests (Pass) |
| **Recurring Maintenance** | `calculateFacilityMaintenanceRetainer`, `calculateEmergencyDispatchInvoice`, `calculateWhiteBoxTurnover` | 3 Tests (Pass) |
| **Marketplace & Float** | `calculateMarketplacePrimeSubSpread`, `calculateEarlyPayFactoring` | 2 Tests (Pass) |
| **Design-Build Delivery** | `calculateDesignBuildTotal` | 1 Test (Pass) |
| **Supply Chain & Logistics** | `calculateProcurementTotal`, `calculateEquipmentRental`, `calculateSiteServicesTotal` | 3 Tests (Pass) |
| **Specialized & Public** | `calculateDisasterRestorationBilling`, `calculatePublicWorksCertifiedPayroll` | 2 Tests (Pass) |
| **Platform, SaaS & FinTech**| `calculateContractorSaaSBilling`, `calculateFinancingReferralFee`, `calculatePaymentProcessingRevenueShare` | 3 Tests (Pass) |
| **Asset Ownership & Equity** | `calculateJointVentureWaterfall`, `calculateBuildToRentMetrics`, `calculateBRRRRRefinance`, `calculateFixAndFlipMargin` | 4 Tests (Pass) |
| **Total Test Suite** | **12 Functional Domain Calculators** | **36/36 Unit Tests Passing (99/99 Project-Wide)** |
