# DOCUMENT-REQUIREMENT-ENGINE.md

**Purpose:** Automated logic engine that generates required document sets based on venture context (type, sector, deal, stage, jurisdiction).

**Audience:** Business operators, venture managers, legal, compliance teams  
**Integration Point:** `MASTER-DOCUMENT-ONTOLOGY-REGISTRY.yaml` (source of all 206 document definitions)  
**Status:** Production-ready logic specification (pseudocode + rules, not implementation code)  
**Version:** 1.0 (2026-09-06)  
**Authority:** Venture Operations Control Plane (CP-033) + Legal Governance (RESPECT #5)

---

## EXECUTIVE SUMMARY

The Document Requirement Engine answers: **"What documents do we need to execute this venture?"**

**Input:** Venture metadata (5-7 fields)  
**Process:** Route through layered IF/THEN decision trees (400+ rules)  
**Output:** Ordered list of required documents with:
- Dependencies (Document A must exist before B can be signed)
- Timelines (when each doc is due)
- Approval chain (who signs, in what order)
- Validation gates (what makes it complete)

**Example:**
```
VENTURE: CON-001 (Construction Acquisition)
  Type: Construction
  Sector: Real Estate (Commercial)
  Deal: $8.5M acquisition of existing office building
  Stage: Due diligence (Day 3 of 45)
  Jurisdiction: North Carolina + federal

REQUIRED DOCUMENTS (generated):
  1. Purchase Agreement (Day 0 - Executed) ✅
  2. Title Insurance Commitment (Day 7) → Enables: Phase 2 docs
  3. Phase II Environmental Assessment (Day 14) → Enables: Financing docs
  4. Lender Requirements (Day 10) → Blocks: Phase 3 until received
  5-15. [10 more docs in dependency order]
```

---

## SECTION 1: INPUT SCHEMA

### Core Metadata Fields (Always Required)

```
VENTURE CONTEXT:
├── venture_id: String (e.g., "CON-001", "LT-005")
├── venture_name: String
├── venture_type: Enum [Construction, Staffing, Logistics, Real Estate, Technology, Healthcare, Finance, Transportation]
├── primary_sector: Enum [SEC-001 to SEC-035] (see SECTOR-TAXONOMY-MASTER)
├── stage: Enum [Ideation, Validation, MVP, Growth, Scale, Exit]
├── jurisdiction: List<String> (e.g., ["North Carolina", "Federal - OSHA", "Federal - FDA"])
└── maturity: Enum [Brand New, Existing, Acquisition, Merger, Joint Venture]

DEAL CONTEXT (if applicable):
├── deal_type: Enum [Organic Founding, Acquisition, Merger, Licensing, Partnership, Lease, Loan, Investment]
├── deal_size_usd: Integer (e.g., 8500000)
├── deal_structure: Enum [Asset Sale, Stock Sale, Merger, Partnership, Lease, License]
└── counterparty_type: Enum [Individual, Private Company, Public Company, Government, Non-profit, Foreign Entity]

COMPLIANCE CONTEXT:
├── regulated_industry: Boolean (is venture in regulated industry? healthcare, finance, transportation, construction, etc.)
├── employee_count_est: Integer (affects HR/labor docs)
├── data_sensitivity: Enum [None, PII, PHI, PCI, IP, Confidential, Combination]
└── export_control: Boolean (selling internationally?)
```

### Derivable Fields (Auto-Calculated)

```
ENGINE CALCULATES:
├── is_acquisition: Boolean = (deal_type IN [Acquisition, Merger])
├── requires_diligence: Boolean = (deal_size_usd >= 500000 OR regulated_industry = true)
├── requires_financing: Boolean = (deal_size_usd > 1000000 AND venture_type != Technology)
├── is_multi_jurisdictional: Boolean = (COUNT(jurisdiction) > 1)
├── required_approvals: List<String> = [Board, Regulatory, Lender, Insurance, etc.]
└── has_environmental_risk: Boolean = (venture_type IN [Construction, Real Estate, Transportation, Logistics])
```

---

## SECTION 2: CORE ROUTING LOGIC

### Master Decision Tree

All document requirements flow through this hierarchical logic:

```
START: Venture Metadata
  │
  ├─→ GATE 1: Operational Documents (Always Required)
  │     └─→ [ Certificates, Bylaws, Operating Agreements, Policies ]
  │
  ├─→ GATE 2: Deal Documents (IF deal_type != Organic Founding)
  │     └─→ ROUTE by deal_type → [Acquisition Docs, Partnership Docs, Lease Docs, etc.]
  │
  ├─→ GATE 3: Financing Documents (IF requires_financing = true)
  │     └─→ ROUTE by lender_type → [Bank SBA Loan, Equipment Finance, Venture, Private Equity, etc.]
  │
  ├─→ GATE 4: Regulatory & Compliance (IF regulated_industry = true)
  │     └─→ ROUTE by industry → [Healthcare Docs, Finance Docs, Construction Docs, etc.]
  │
  ├─→ GATE 5: Employment Documents (IF employee_count_est > 0)
  │     └─→ ROUTE by employee_count → [Handbook, Policies, Agreements, etc.]
  │
  ├─→ GATE 6: Intellectual Property (IF data_sensitivity IN [IP, Confidential])
  │     └─→ [ NDAs, IP Assignments, Patent, Trademarks, etc. ]
  │
  └─→ GATE 7: Environmental & Risk (IF has_environmental_risk = true)
        └─→ [ Environmental Assessments, Insurance, Compliance Certs, etc. ]

OUTPUT: Complete Document Set (ordered by dependencies + timeline)
```

### Logic Language Conventions

```
IF <condition>:
  THEN <action> [required documents | routing decision | dependent gate]
  ELSE_IF <alternative_condition>:
    THEN <alternative_action>
  ELSE:
    [default or skip this gate]

EXAMPLES:
  IF venture_type = "Construction" AND deal_type = "Acquisition" AND deal_size_usd >= 5000000:
    THEN require: [Purchase Agreement, Phase II Environmental Assessment, Lien Waivers, Bonds, etc.]
         AND open: GATE 3 (Financing) + GATE 4 (Regulatory)
    
  IF venture_type = "Healthcare" AND regulated_industry = true:
    THEN require: [HIPAA Business Associate Agreement, Compliance Attestation, Privacy Policy, etc.]
         AND set timeline: MUST_COMPLETE before any patient data access
    
  IF deal_type = "Acquisition" AND counterparty_type IN [Foreign Entity, Public Company]:
    THEN require: [CFIUS Analysis, Foreign Investment Review, etc.]
         AND escalate: requires director/board approval
```

---

## SECTION 3: GATE-BY-GATE RULES

### GATE 1: Operational Documents (100% Probability)

**Condition:** Always execute for all ventures  
**Purpose:** Establish legal entity, governance, operational baseline

```
STANDARD DOCS (all ventures):
  ├── Certificate of Formation / Incorporation
  ├── Bylaws OR Operating Agreement (depending on entity type)
  ├── IRS Form SS-4 (EIN Assignment)
  ├── Board Minutes (if corporation) OR Member Consent (if LLC)
  └── Secretary/Custodian Resolutions

BASELINE POLICIES (all ventures):
  ├── Confidentiality & NDA Master
  ├── IT & Data Security Policy
  ├── Conflicts of Interest Policy
  ├── Anti-Corruption & FCPA Policy (if international)
  └── Document Retention & Archival Policy
```

**Timeline:**  
- Certificate of Formation: **Day 1** (required before anything else)
- Operating Agreement: **Day 3**
- IRS Form SS-4: **Day 2** (expedite if financing needed)
- Policies: **Day 5**

**Dependencies:** None (these are prerequisites)  
**Approval Chain:** Founder → (if multi-founder: all founders) → Secretary/Corporate Officer

**Validation:** All GATE 1 docs signed and archived in secure vault

---

### GATE 2: Deal Documents

**Condition:** IF `deal_type != Organic Founding`

#### RULE 2A: ACQUISITION DOCUMENTS

```
IF venture_type IN [Construction, Real Estate, Technology] 
   AND deal_type IN [Acquisition, Merger]
   AND deal_size_usd >= 500000:
  
  THEN require in order:
    Phase 1: Preliminary (Pre-Signing)
      1. Confidentiality Agreement (NDA)
         Timeline: Day 1 (before any information flow)
         Approval: Seller + Buyer lead negotiator
      
      2. Letter of Intent (LOI) / Term Sheet
         Timeline: Day 3-5 (before diligence)
         Approval: Seller principals + Buyer principals
         Dependencies: None, can run in parallel with Phase 1
    
    Phase 2: Due Diligence (Pre-Signing, Running in Parallel)
      3. Purchase Agreement (Master document - 80-120 pages typical)
         Timeline: Day 15-20 (negotiated over 2 weeks)
         Approval: Buyer attorney + Seller attorney → Buyer principals + Seller principals
         Dependencies: LOI already signed
      
      4. Disclosure Schedules (Exhibits to Purchase Agreement)
         Timeline: Day 20-25 (completed as part of Purchase Agreement negotiation)
         Approval: Same as Purchase Agreement
         Includes: Customer list, vendor agreements, litigation, environmental, IP, employees, financials
      
      5. Environmental Site Assessment (Phase I, mandatory if property-involved)
         Timeline: Day 10 (order early, runs 7-10 days)
         Approval: Buyer + Buyer's lender (if applicable)
         Dependencies: Can start day 1 of LOI
      
      6. Financial Due Diligence Package (P&L, Balance Sheet, Tax Returns, 3 years)
         Timeline: Day 5 (requested in LOI, collected over 10 days)
         Approval: Seller CFO/accountant provides
         Dependencies: NDA already signed before receiving
      
      7. Legal Due Diligence (Contracts, Litigation, IP, Regulatory)
         Timeline: Day 5-20 (running parallel to financial)
         Approval: Seller's legal team compiles, Buyer's attorney reviews
         Dependencies: NDA signed before disclosure
    
    Phase 3: Closing (Post-Signing, Pre-Closing)
      8. Representations & Warranties Insurance (if deal > $2M)
         Timeline: Day 30 (ordered after Purchase Agreement signed)
         Approval: Buyer insurance broker + lender + Seller (may contribute premium)
         Dependencies: Purchase Agreement finalized
      
      9. Updated Phase II Environmental (if Phase I flagged issues)
         Timeline: Day 25 (conditional on Phase I findings)
         Approval: Buyer + Environmental consultant
         Dependencies: Phase I complete
      
      10. Stockholder Consent / Board Resolutions (both buyer + seller)
          Timeline: Day 25-28 (before closing)
          Approval: Board of directors + shareholders
          Dependencies: Purchase Agreement finalized
      
      11. Third-Party Consents (Landlord, Key Vendors, IP Licensor, etc.)
          Timeline: Day 10-30 (varies; some consents take 2-3 weeks)
          Approval: Third parties (landlord, vendor, licensor)
          Dependencies: Can request immediately after LOI or Purchase Agreement
      
      12. Officer Certificates (Rep & Warranty Certificates at Closing)
          Timeline: Day 35 (one day before or at closing)
          Approval: CEO/CFO of both entities
          Dependencies: Purchase Agreement + all diligence complete
      
      13. Closing Statements (Proration, Expense Allocation, Wire Instructions)
          Timeline: Day 33 (3 days before closing)
          Approval: Seller CFO + Buyer CFO + Escrow agent
          Dependencies: Purchase Agreement + financial details finalized
      
      14. Deed of Assignment (if asset sale - transfers property)
          Timeline: Day 34-35 (prepared 1-2 days before closing)
          Approval: Seller legal counsel + Buyer legal counsel
          Dependencies: None (prepared in parallel)
      
      15. Closing Checklist & Conditions Waiver
          Timeline: Day 34 (day before closing)
          Approval: Both counsel + lender (if applicable)
          Dependencies: All conditions verified

TOTAL ACQUISITION FLOW: 35-45 days for $5M+ deal
```

#### RULE 2B: PARTNERSHIP / JOINT VENTURE DOCUMENTS

```
IF deal_type IN [Partnership, Joint Venture]:
  
  THEN require:
    1. Partnership Agreement (or JV Agreement)
       Timeline: Day 10
       Approval: All partners sign
       Includes: Capital contributions, profit sharing, governance, exit clauses
    
    2. Capitalization Schedule
       Timeline: Day 8 (before agreement signing)
       Approval: CFO/accountant
    
    3. Operating Procedures / Rules of Conduct
       Timeline: Day 15
       Approval: Partners
    
    4. Non-Compete Agreements (if applicable)
       Timeline: Day 10
       Approval: All partners
    
    5. Dispute Resolution / Arbitration Clause
       Timeline: Day 10 (part of Partnership Agreement)
       Approval: All partners + legal counsel
```

#### RULE 2C: LEASE DOCUMENTS

```
IF deal_type = "Lease":
  
  THEN require:
    1. Commercial Lease (master document)
       Timeline: Day 5-10
       Approval: Landlord + Tenant + Landlord's attorney + Tenant's attorney
    
    2. Tenant Improvement Agreement (if build-out required)
       Timeline: Day 15
       Approval: Landlord + Tenant
    
    3. Personal Guaranty (if landlord requires)
       Timeline: Day 10
       Approval: Business owner + Landlord
    
    4. Estoppel Certificate (confirms lease terms)
       Timeline: Day 7
       Approval: Landlord
```

#### RULE 2D: LICENSE / DISTRIBUTION DOCUMENTS

```
IF deal_type IN [Licensing, Distribution]:
  
  THEN require:
    1. License / Distribution Agreement
       Timeline: Day 15-20
       Approval: Licensor + Licensee + IP counsel
    
    2. Schedule of Licensed IP (patents, trademarks, copyrights)
       Timeline: Day 10
       Approval: Licensor IP team
    
    3. IP Indemnification Provisions
       Timeline: Day 15 (part of agreement)
       Approval: Licensor counsel
    
    4. Royalty Audit Rights
       Timeline: Day 15 (part of agreement)
       Approval: Licensor
```

---

### GATE 3: FINANCING DOCUMENTS

**Condition:** IF `requires_financing = true` (typically: deal_size_usd >= $1M OR venture_type IN [Construction, Real Estate])

#### RULE 3A: TRADITIONAL BANK FINANCING (SBA Loan, Commercial Loan)

```
IF lender_type = "Bank" AND loan_size < $5M:
  
  THEN require in order:
    Phase 1: Application & Underwriting (Weeks 1-4)
      1. Loan Application Form (SBA Form 1919 for SBA loans)
         Timeline: Day 1
         Approval: Lender loan officer
      
      2. Personal Financial Statement (PFS)
         Timeline: Day 1
         Approval: Applicant completes, lender verifies
      
      3. Business Financial Statements (3 years P&L, Balance Sheet, Tax Returns)
         Timeline: Day 3
         Approval: CPA / accountant prepares
      
      4. Business Plan & Executive Summary
         Timeline: Day 5
         Approval: Owner / consultant prepares
      
      5. Projected Cash Flow Statement (24-36 months)
         Timeline: Day 5
         Approval: CFO / accountant prepares
      
      6. Personal & Business Credit Reports
         Timeline: Day 2
         Approval: Lender orders, applicant consents
      
      7. Management Resume(s) (for key principals)
         Timeline: Day 3
         Approval: Applicants
    
    Phase 2: Approval & Documentation (Weeks 4-6)
      8. Loan Commitment Letter
         Timeline: Day 25
         Approval: Lender loan committee
         Dependencies: Complete underwriting + credit approval
      
      9. Use of Proceeds Certification (how loan money will be spent)
         Timeline: Day 27
         Approval: Borrower certifies
      
      10. Personal Guaranty (if required by lender, typically yes)
          Timeline: Day 28
          Approval: Personal guarantor + lender
      
      11. Promissory Note (the actual loan document)
          Timeline: Day 30 (final version)
          Approval: Both borrower + lender counsel
      
      12. Security Agreement (what collateral secures the loan)
          Timeline: Day 30
          Approval: Both counsel
          Includes: UCC-1 filings, collateral description
      
      13. Uniform Commercial Code (UCC) Financing Statement
          Timeline: Day 32 (prepared, filed at closing)
          Approval: Lender's counsel
      
      14. Certificate of Insurance (proof of hazard/liability insurance)
          Timeline: Day 28
          Approval: Borrower's insurance broker + lender
      
      15. Disbursement Instructions / Loan Agreement
          Timeline: Day 33
          Approval: Borrower + lender
      
      16. Compliance Certificate (EEO, OSHA, environmental for regulated ventures)
          Timeline: Day 30 (if applicable)
          Approval: Borrower certifies compliance

TOTAL SBA/BANK FINANCING FLOW: 30-45 days
```

#### RULE 3B: EQUIPMENT FINANCE (Loans, Leases)

```
IF venture_type IN [Construction, Logistics, Transportation, Manufacturing]
   AND equipment_cost >= $100000:
  
  THEN require:
    1. Equipment List & Specifications
       Timeline: Day 1
       Approval: Borrower provides
    
    2. Equipment Finance Agreement (or Master Lease)
       Timeline: Day 10
       Approval: Lessor/Lender + Lessee/Borrower
    
    3. UCC-1 Financing Statement (for equipment)
       Timeline: Day 12
       Approval: Lender's counsel
    
    4. Insurance Requirement Certificate
       Timeline: Day 10
       Approval: Borrower's insurance broker
```

#### RULE 3C: REAL ESTATE CONSTRUCTION FINANCING (Construction Loan)

```
IF venture_type = "Construction" AND deal_size_usd >= $2M:
  
  THEN require in order:
    1. Loan Application (Construction-specific form)
       Timeline: Day 1
    
    2. Detailed Construction Budget (line-item cost breakdown)
       Timeline: Day 5
       Approval: General Contractor + Lender
       Dependencies: None
    
    3. Construction Timeline / Schedule
       Timeline: Day 5
       Approval: General Contractor
    
    4. Architect's or Engineer's Plans (for permanent financing)
       Timeline: Day 10 (should already exist)
       Approval: Lender reviews
    
    5. Title Policy Commitment (required for lender)
       Timeline: Day 10 (order early)
       Approval: Title company
    
    6. Phase I Environmental Assessment
       Timeline: Day 10
       Approval: Lender + Borrower
    
    7. Appraisal (of finished project or existing property)
       Timeline: Day 15
       Approval: Lender's appraiser
    
    8. Lender's Loan Conditions Letter
       Timeline: Day 20
       Approval: Lender's underwriting
    
    9. Construction Loan Agreement (interest-only, draws as work progresses)
       Timeline: Day 28
       Approval: Lender + Borrower counsel
    
    10. General Contractor Agreement (with lender protections)
        Timeline: Day 25
        Approval: Developer + GC + Lender
        Includes: Payment schedule tied to % completion
    
    11. Subordination Agreements (if equity investor involved)
        Timeline: Day 25
        Approval: Equity investor + Lender
    
    12. Mechanic's Lien Waivers (from GC + major subs, periodic)
        Timeline: Day 35+ (monthly, each draw period)
        Approval: GC + Subcontractors
        Triggers: Required before each draw request

TOTAL CONSTRUCTION FINANCING: 35-60 days (draws continue during construction)
```

#### RULE 3D: VENTURE CAPITAL / PRIVATE EQUITY

```
IF lender_type IN [Venture Capital, Private Equity] OR funding_type = "Series Funding":
  
  THEN require:
    1. Term Sheet (10-15 pages)
       Timeline: Day 5-10
       Approval: VC/PE firm + Founders
    
    2. Capitalization Table (pre- and post-investment)
       Timeline: Day 10
       Approval: Existing shareholders + New investor
    
    3. Investor Rights Agreements
       Timeline: Day 20
       Approval: Investor counsel + Company counsel
    
    4. Voting Agreements (if investor getting board seat)
       Timeline: Day 20
       Approval: All shareholders
    
    5. Anti-Dilution Provisions
       Timeline: Day 20 (part of rights agreement)
    
    6. Drag-Along / Tag-Along Rights
       Timeline: Day 20 (part of rights agreement)
    
    7. Preferred Stock Certificate of Designation
       Timeline: Day 18
       Approval: Board + Shareholders
    
    8. Stock Purchase Agreement
       Timeline: Day 25
       Approval: Investor counsel + Company counsel
    
    9. Shareholders' Agreement (if multiple investors)
       Timeline: Day 22
       Approval: All shareholders
    
    10. Board Resolutions (authorizing stock issuance)
        Timeline: Day 25
        Approval: Board of directors

TOTAL VC/PE FINANCING: 25-35 days
```

---

### GATE 4: REGULATORY & COMPLIANCE DOCUMENTS

**Condition:** IF `regulated_industry = true`

#### RULE 4A: HEALTHCARE VENTURES

```
IF venture_type IN [Healthcare, Telemedicine, Medical Device, Pharmaceuticals]:
  
  THEN require:
    FEDERAL REQUIREMENTS:
      1. HIPAA Business Associate Agreement (BAA)
         Timeline: Day 10 (before any patient data access)
         Approval: All partners handling PHI + compliance officer
      
      2. Privacy Policy (HIPAA-compliant)
         Timeline: Day 15
         Approval: Privacy officer + Legal
      
      3. Security Risk Assessment
         Timeline: Day 20 (ongoing, annual)
         Approval: HIPAA security officer
      
      4. Breach Notification Plan
         Timeline: Day 15
         Approval: Compliance officer
      
      5. FDA Compliance Attestation (if medical device/drug)
         Timeline: Day 30+ (often requires consulting firm)
         Approval: Regulatory affairs + FDA
      
      6. DEA Registration (if dispensing controlled substances)
         Timeline: Day 45 (federal process, 4-6 weeks)
         Approval: DEA
      
      7. State Medical License (if applicable)
         Timeline: 30-90 days (state-dependent, must register physicians)
         Approval: State licensing board
      
      8. Credentialing & Privileging Documentation (for hospital networks)
         Timeline: Day 45 (ongoing, 4-6 weeks)
         Approval: Credentialing committee
    
    STATE-SPECIFIC:
      9. State Health Department Registration/License
         Timeline: Day 20-30 (varies by state)
         Approval: State authority
      
      10. Workers' Compensation Insurance Certificate
          Timeline: Day 15
          Approval: Insurance carrier
      
      11. Professional Liability Insurance
          Timeline: Day 15
          Approval: Insurance broker + carrier
```

#### RULE 4B: FINANCIAL SERVICES VENTURES

```
IF venture_type IN [Banking, Insurance, Investment, Lending, Fintech]:
  
  THEN require:
    FEDERAL REQUIREMENTS:
      1. Banking License Application (if taking deposits)
         Timeline: 6-12 months (regulatory process)
         Approval: Federal Reserve + OCC
      
      2. AML/KYC Compliance Program (Anti-Money Laundering / Know Your Customer)
         Timeline: Day 30 (before operations)
         Approval: Chief Compliance Officer + Board
      
      3. OFAC Compliance Certification (Office of Foreign Assets Control)
         Timeline: Day 15
         Approval: Compliance officer
      
      4. Sarbanes-Oxley (SOX) Compliance (if public)
         Timeline: Ongoing
      
      5. SEC Registration (if securities trading)
         Timeline: 60+ days
         Approval: SEC + legal counsel
      
      6. Privacy Policy & Data Security Plan (GLBA-compliant if Gramm-Leach-Bliley)
         Timeline: Day 20
         Approval: Privacy officer
      
      7. Cybersecurity Incident Response Plan
         Timeline: Day 30
         Approval: CISO + Board
    
    STATE-SPECIFIC:
      8. Money Transmitter License (varies by state)
         Timeline: 30-90 days per state
         Approval: State regulatory body
      
      9. Insurance License (if insurance product)
         Timeline: 60-120 days
         Approval: State insurance commissioner
```

#### RULE 4C: CONSTRUCTION VENTURES

```
IF venture_type = "Construction":
  
  THEN require:
    LICENSING & PERMITS:
      1. General Contractor License (if required by state)
         Timeline: Before day 1 of work
         Approval: State licensing board
      
      2. Building Permits (per project)
         Timeline: Before construction starts
         Approval: Local building department
      
      3. Electrical, Plumbing, HVAC Permits (if applicable)
         Timeline: Before respective trades begin
         Approval: Local authorities
    
    INSURANCE & BONDING:
      4. General Liability Insurance Certificate
         Timeline: Day 10 (before bidding)
         Approval: Insurance broker
      
      5. Workers' Compensation Insurance
         Timeline: Day 10 (mandatory if any employees)
         Approval: Insurance carrier + state
      
      6. Surety Bonds (Bid Bond, Performance Bond, Payment Bond)
         Timeline: Day 5-10 (for public/large projects)
         Approval: Surety company
      
      7. Builder's Risk / Inland Marine Insurance
         Timeline: Day 5 (if contracting work)
         Approval: Insurance broker
    
    COMPLIANCE:
      8. OSHA Safety Plan & Certifications
         Timeline: Day 1 (for projects with 10+ workers)
         Approval: Safety director + OSHA
      
      9. Environmental Compliance (stormwater, hazmat, etc.)
         Timeline: Day 5 (before ground disturbance)
         Approval: Local environmental agency
      
      10. Lien Waiver Agreements (from subs & suppliers, ongoing)
          Timeline: Before each payment
          Approval: GC + Subcontractors
```

#### RULE 4D: TRANSPORTATION / LOGISTICS VENTURES

```
IF venture_type IN [Logistics, Transportation, Ride-Share, Delivery]:
  
  THEN require:
    FEDERAL:
      1. DOT Authority Certificate (if interstate commerce)
         Timeline: Day 15-30
         Approval: FMCSA (Federal Motor Carrier Safety Admin)
      
      2. FMCSA Compliance Safety Attestation
         Timeline: Day 20
         Approval: Safety director
      
      3. Drug & Alcohol Testing Program (if commercial drivers)
         Timeline: Day 15 (must be in place before hiring)
         Approval: Third-party testing administrator
      
      4. Hours of Service (HOS) Logging Compliance
         Timeline: Day 15 (electronic logging device or paper)
         Approval: Driver training + compliance officer
    
    STATE:
      5. Commercial Driver License (CDL) for drivers
         Timeline: Per driver (varies by state)
         Approval: State DMV
      
      6. Vehicle Registration & Commercial Plates
         Timeline: Day 7
         Approval: State DMV
    
    INSURANCE:
      7. Commercial Auto Insurance
         Timeline: Day 10 (required before operations)
         Approval: Insurance broker + carrier
      
      8. Cargo Liability Insurance (if transporting goods)
         Timeline: Day 10
         Approval: Insurance broker
```

---

### GATE 5: EMPLOYMENT & HR DOCUMENTS

**Condition:** IF `employee_count_est > 0`

```
BASELINE (1+ employees):
  1. Employee Handbook / Operations Manual
     Timeline: Day 15 (before first hire)
     Includes: At-will employment, confidentiality, conduct, benefits, PTO, remote work, dress code
  
  2. At-Will Employment Agreements (one per employee)
     Timeline: Day 1 (sign on day 1)
     Approval: Employee + HR
  
  3. Confidentiality & NDA (Employee version)
     Timeline: Day 1
     Approval: Employee + HR
  
  4. IP Assignment Agreement (critical for tech/design ventures)
     Timeline: Day 1
     Approval: Employee + HR + Legal
  
  5. Non-Compete / Non-Solicitation (state-dependent, check enforceability)
     Timeline: Day 1 (or before employment if sensitive role)
     Approval: Employee + HR + Legal
  
  6. Form I-9 (Immigration & Employment Authorization)
     Timeline: Day 1 (federal requirement)
     Approval: HR + employee provides documents
  
  7. W-4 Form (Federal Tax Withholding)
     Timeline: Day 1
     Approval: Employee completes
  
  8. State Tax Form (varies by state)
     Timeline: Day 1
     Approval: Employee completes

BASELINE POLICIES (1+ employees):
  9. Payroll & Compensation Policy
     Timeline: Day 15 (before first payroll)
  
  10. Anti-Harassment & Equal Opportunity Policy (Title VII, ADA, ADEA)
      Timeline: Day 15 (federal requirement)
  
  11. Americans with Disabilities Act (ADA) Compliance Notice
      Timeline: Day 10
  
  12. Wage & Hour Policy (breaks, overtime, minimum wage compliance)
      Timeline: Day 15
  
  13. Attendance & Punctuality Policy
      Timeline: Day 15
  
  14. Remote Work / Telecommuting Policy (if applicable)
      Timeline: Day 10
  
  15. Data Security & Password Policy
      Timeline: Day 15
  
  16. Social Media & Communications Policy
      Timeline: Day 15

IF employee_count_est >= 50:
  ADDITIONAL (50+ employees triggers EEOC reporting + enhanced compliance):
  
  17. EEOC Affirmative Action Plan
      Timeline: Day 30 (ongoing, annual update)
  
  18. Diversity & Inclusion Policy
      Timeline: Day 30
  
  19. Workers' Compensation Notice (posted, required)
      Timeline: Day 5
  
  20. OSHA Poster (required posting for 1+ employees, construction/hazmat)
      Timeline: Day 5
  
  21. Family & Medical Leave Act (FMLA) Policy (if 50+ employees)
      Timeline: Day 30

IF venture_type IN [Healthcare, Finance, Government Contracting]:
  ADDITIONAL (sensitive industries):
  
  22. Background Check Authorization & Policy
      Timeline: Before hiring
  
  23. Drug Testing Policy (if applicable)
      Timeline: Before hiring
  
  24. Clearance/Certification Requirements Documentation
      Timeline: Before hiring
```

---

### GATE 6: INTELLECTUAL PROPERTY DOCUMENTS

**Condition:** IF `data_sensitivity IN [IP, Confidential] OR venture_type = "Technology"`

```
PATENTS (IF venture has innovative technology):
  1. Provisional Patent Application (filing placeholder, 1-year window)
     Timeline: Before public disclosure (Day 1)
     Approval: Inventor + IP counsel + startup founder
     Cost: ~$1,500 (provisional, minimal)
  
  2. Utility Patent Application (full patent, 18-month publication timeline)
     Timeline: Day 30-60 (coordinate with provisional or standalone)
     Approval: Patent attorney + inventor
     Cost: ~$8,000-15,000 + ongoing USPTO fees
  
  3. Patent Assignment Agreement (if employee invented)
     Timeline: Day 1 (along with employment agreement)
     Approval: Employee + Employer
  
  4. Freedom to Operate (FTO) Opinion (optional but advised for VC-backed)
     Timeline: Day 45 (cost ~$3K-5K)
     Approval: Patent counsel

TRADEMARKS (IF brand matters):
  5. Trademark Availability Search
     Timeline: Day 1 (before brand launch)
     Approval: IP counsel
  
  6. Trademark Registration Application (USPTO or WIPO if international)
     Timeline: Day 15-30 (filing)
     Approval: IP counsel
     Timeline to registration: 6-12 months

COPYRIGHTS:
  7. Copyright Registration (for software, content, designs)
     Timeline: Day 30 (optional but recommended for litigation)
     Approval: Author/company
  
  8. License Grants (Creative Commons or proprietary)
     Timeline: Day 15 (if offering work under license)
     Approval: IP counsel

SOFTWARE & CODE:
  9. Open Source Compliance Audit (if using open-source libraries)
     Timeline: Day 30 (critical for VC fundraising)
     Approval: CTO + IP counsel
  
  10. GPL / MIT / Apache License Compliance Documentation
      Timeline: Day 30 (if shipping with open-source)
      Approval: Software lead
  
  11. Third-Party Software License Review (SaaS tools, libraries, frameworks)
      Timeline: Day 20
      Approval: CTO

CONFIDENTIALITY:
  12. Mutual Non-Disclosure Agreements (NDA) for partners/vendors/investors
      Timeline: Day 10 (ongoing, as needed)
      Approval: Counsel on both sides
  
  13. Employee NDAs (see GATE 5)
      Timeline: Day 1 (with employment)

DATA & PRIVACY:
  14. Privacy Policy (for data collection, GDPR/CCPA compliant)
      Timeline: Day 20 (before beta launch)
      Approval: Privacy counsel + founder
  
  15. Terms of Service (legal terms for SaaS/app users)
      Timeline: Day 25 (before public launch)
      Approval: Counsel
  
  16. Data Processing Agreement (if handling EU resident data - GDPR)
      Timeline: Day 30 (if internationalized)
      Approval: Privacy counsel
```

---

### GATE 7: ENVIRONMENTAL, RISK & INSURANCE

**Condition:** IF `has_environmental_risk = true` OR venture involves property/hazmat/manufacturing

```
ENVIRONMENTAL ASSESSMENTS:
  1. Phase I Environmental Site Assessment (ESA)
     Timeline: Day 10 (standard for any real property acquisition)
     Approval: Environmental consultant + Lender (if financing)
     Cost: $2K-5K
  
  2. Phase II ESA (if Phase I flags contaminants)
     Timeline: Day 15-20 (conditional)
     Approval: Lender + Environmental consultant
     Cost: $5K-25K depending on extent
  
  3. Asbestos & Lead Paint Inspection (if pre-1980s building)
     Timeline: Day 10
     Approval: Property owner + potential buyers
     Cost: $500-2K
  
  4. Mold & Indoor Air Quality Assessment (if water damage history)
     Timeline: Day 10-15 (conditional)
     Approval: Environmental consultant
  
  5. Wetlands & Wildlife Habitat Survey (if project affects land)
     Timeline: Day 15-30 (complex, may need federal permits)
     Approval: Army Corps of Engineers + Environmental consultant
  
  6. Hazardous Materials Audit (if manufacturing/chemical facility)
     Timeline: Day 20
     Approval: Environmental compliance officer + EPA

ENVIRONMENTAL COMPLIANCE:
  7. Stormwater Management Plan (for construction projects)
     Timeline: Day 15 (before ground disturbance)
     Approval: Environmental engineer + Local authority
  
  8. Spill Prevention Control & Countermeasures (SPCC) Plan (if storing hazmat)
     Timeline: Day 20 (federal requirement if >1,320 gallons on-site)
     Approval: Environmental coordinator + EPA
  
  9. Air Emissions Permit (if manufacturing/food processing/dry cleaning)
     Timeline: Day 30-60 (varies by state)
     Approval: State air quality board
  
  10. Water Discharge Permit (if discharging to waterways)
      Timeline: Day 30-60 (NPDES permits)
      Approval: EPA or state environmental agency

INSURANCE:
  11. General Liability Insurance
      Timeline: Day 10 (before operations)
      Approval: Insurance broker + carrier
  
  12. Property Insurance (if owning/leasing real estate)
      Timeline: Day 10 (lender-required)
      Approval: Insurance broker
  
  13. Environmental Liability Insurance
      Timeline: Day 15 (for manufacturing/hazmat ventures)
      Approval: Insurance broker
  
  14. Pollution Liability Insurance (for environmental risk)
      Timeline: Day 15 (if handling hazmat)
      Approval: Insurance broker
  
  15. Directors & Officers (D&O) Insurance (if VC-backed)
      Timeline: Day 45
      Approval: Board + Insurance broker
  
  16. Cyber Liability & Data Breach Insurance
      Timeline: Day 20
      Approval: CISO + Insurance broker
```

---

## SECTION 4: VENTURE TYPE MATRICES

Specific requirements by the 5 primary venture types.

### CONSTRUCTION (CON-001, CON-002, etc.)

```
GATE 1: Operational ✅ (all ventures)
GATE 2: Deal Docs ✅ (almost always: acquisition or new project)
  - Required: Purchase Agreement, Environmental Assessments, Lien Waivers, Bonds
GATE 3: Financing ✅ (typically $2M+ projects = Construction Loan)
  - Required: Construction Loan Agreement, GC Agreement, Disbursement schedule, Draw requests
GATE 4: Regulatory ✅ (highly regulated)
  - Required: Contractor license, Building permits, OSHA, Environmental permits
GATE 5: Employment ✅ (employees + subs)
  - Required: Employee handbook, I-9, Subcontractor agreements (not employees but critical)
GATE 6: IP ❌ (low priority unless proprietary method)
GATE 7: Environmental ✅ (highest priority)
  - Required: Phase I/II ESA, SPCC if hazmat, Stormwater management

PRIORITY TIMELINE:
  Day 1-5: GATE 1 (Entity formation), GATE 2 (Purchase docs), Begin GATE 7 (Phase I ESA)
  Day 5-15: GATE 3 (Financing application), GATE 4 (Permits, licensing)
  Day 15-30: GATE 2 (Acquisitions close), GATE 3 (Financing underwriting)
  Day 30+: GATE 5 (Hire subs/crews), Ongoing GATE 4 (Draw requests with lien waivers)
```

### STAFFING / HR TECH (OPS-001, STA-001, etc.)

```
GATE 1: Operational ✅ (all ventures)
GATE 2: Deal Docs ✅ (if acquiring another staffing company, YES; otherwise no)
GATE 3: Financing ✅ (if $1M+ or VC-backed, YES; bootstrap, maybe not)
  - If financed: SBA loan, equipment finance (tech stack), or equity
GATE 4: Regulatory ✅ (highly regulated - employment law + background checks)
  - Required: PEO partnership agreement, Background check policy, I-9 procedures, EEO compliance
GATE 5: Employment ✅ (critical - you ARE an employment company)
  - Required: Employee handbook, Contractor agreements, Payroll setup, Workers' comp
GATE 6: IP ⚠️ (medium - if proprietary matching algorithm)
  - Optional: IP assignment, Algorithm documentation, Software license grants
GATE 7: Environmental ❌ (not applicable)

PRIORITY TIMELINE:
  Day 1-10: GATE 1 (Entity), GATE 5 (Handbook, I-9, W-4 setup), GATE 4 (PEO/EOR contract)
  Day 10-20: GATE 3 (Financing if needed), Set up insurance (GL, Workers comp)
  Day 20+: GATE 6 (If tech-enabled: IP assignments for matching algorithm)
```

### LOGISTICS / 3PL (LOG-001, LOG-005, etc.)

```
GATE 1: Operational ✅ (all ventures)
GATE 2: Deal Docs ✅ (often: acquire existing 3PL, warehouses, fleet)
GATE 3: Financing ✅ (warehouse + fleet = major capex, almost always financed)
  - Required: Equipment finance (vehicles), Real estate financing (if buying warehouse)
GATE 4: Regulatory ✅ (highly regulated - DOT, FMCSA, hazmat)
  - Required: DOT authority, CDL certifications, FMCSA compliance, Hazmat training if applicable
GATE 5: Employment ✅ (drivers + warehouse staff)
  - Required: Employee handbook, Drug testing policy, HOS logging setup, I-9s
GATE 6: IP ⚠️ (medium if proprietary routing software)
  - Optional: Software IP, Algorithms, Technology licensing
GATE 7: Environmental ✅ (vehicles = emissions, hazmat handling possible)
  - Required: Vehicle registration, Emissions compliance, Hazmat storage if applicable

PRIORITY TIMELINE:
  Day 1-10: GATE 1 (Entity), GATE 4 (DOT authority, CDL compliance), GATE 5 (Insurance)
  Day 10-20: GATE 3 (Equipment finance), Begin GATE 2 (if acquisition)
  Day 20+: GATE 4 (ongoing: driver certifications), GATE 5 (hire crew)
```

### REAL ESTATE (RE-001, RE-005, etc.)

```
GATE 1: Operational ✅ (all ventures)
GATE 2: Deal Docs ✅ (almost always: acquisition or partnership)
  - Required: Purchase agreement, Lease agreements, Title insurance, 1031 exchange docs (if applicable)
GATE 3: Financing ✅ (virtually always: real property mortgages)
  - Required: Real estate financing, Appraisal, Title commitment, Subordination agreements
GATE 4: Regulatory ✅ (zoning, environmental, HOA)
  - Required: Zoning verification, HOA CC&Rs if applicable, Regulatory compliance per use
GATE 5: Employment ⚠️ (medium - property managers, leasing agents)
GATE 6: IP ❌ (not applicable unless unique building design)
GATE 7: Environmental ✅ (highest priority - Phase I/II, ground contamination)
  - Required: Phase I/II ESA, Appraisal, Survey

PRIORITY TIMELINE:
  Day 1-5: GATE 1 (Entity), GATE 7 (Phase I ESA), GATE 4 (Zoning verification)
  Day 5-15: GATE 2 (Purchase agreement), GATE 3 (Financing application, appraisal)
  Day 15-30: GATE 7 (Phase II if needed), Title insurance commitment
  Day 30-45: Close (GATE 2/3)
```

### TECHNOLOGY / SAAS (TECH-001, TECH-040, etc.)

```
GATE 1: Operational ✅ (all ventures)
GATE 2: Deal Docs ✅ (if acquiring competitor or partnership, YES; greenfield, sometimes)
GATE 3: Financing ⚠️ (high if seeking VC; low if bootstrapped)
  - If VC: Full VC docs (GATE 3D)
  - If SBA: SBA loan OK too
  - If bootstrap: maybe just operating capital, less docs
GATE 4: Regulatory ⚠️ (medium to high if handling personal data / healthcare / finance)
  - If B2B SaaS only: minimal regulatory
  - If handling PII: Privacy policy, GDPR/CCPA compliance
  - If healthcare: HIPAA BAA required
  - If fintech: AML/KYC, OFAC, potentially SEC registration
GATE 5: Employment ✅ (engineers, product, support)
  - Required: Employee handbook, IP assignment (critical!), NDA, Non-compete
GATE 6: IP ✅ (critical - this is the company's moat)
  - Required: Provisional/utility patents, Trademark, Open-source compliance audit, Software licensing
GATE 7: Environmental ❌ (not applicable)

PRIORITY TIMELINE:
  Day 1-5: GATE 1 (Entity), GATE 6 (Provisional patent if novel, NDA/Confidentiality)
  Day 5-15: GATE 5 (Employee handbook, IP assignments for hires), GATE 4 (Privacy policy if data-heavy)
  Day 15-30: GATE 3 (If seeking funding: VC docs; if SBA: SBA loan)
  Day 20+: GATE 6 (Trademark application, open-source audit)
```

---

## SECTION 5: DEPENDENCY GRAPH

Which documents must exist before others can be signed/effective.

### Universal Prerequisites (All Gates)

```
BLOCKING DOCUMENTS (must exist first):
  A. Certificate of Formation (GATE 1)
     └─ Blocks: Everything (no legal entity, no deal possible)
  
  B. Operating Agreement / Bylaws (GATE 1)
     └─ Blocks: Board resolutions, employment agreements, financing docs
  
  C. EIN Assignment (GATE 1)
     └─ Blocks: Tax documents, payroll, financing applications
```

### Deal-Specific Dependencies (GATE 2)

```
ACQUISITION FLOW:
  1. NDA
     └─ Enables: LOI (can't exchange info without confidentiality)
  
  2. LOI / Term Sheet
     └─ Enables: Purchase Agreement negotiation, Environmental assessments, Financial diligence
  
  3. Purchase Agreement (draft/negotiated)
     └─ Enables: Officer certificates, Closing documents, Board resolutions for approval
  
  4. Environmental Phase I
     └─ Enables: Phase II (if findings), Lender underwriting decision
  
  5. Financial Due Diligence Package
     └─ Enables: Lender underwriting, Purchase agreement pricing negotiation
  
  6. Lender's Loan Conditions Letter
     └─ Enables: Financing documents, Closing date certainty
```

### Financing Dependencies (GATE 3)

```
SBA LOAN FLOW:
  1. Business Plan / Executive Summary
     └─ Enables: Loan application review
  
  2. Loan Commitment Letter (approval)
     └─ Enables: Promissory Note finalization, UCC filing, Closing
  
  3. Security Agreement (what collateral secures loan)
     └─ Enables: UCC-1 filing, lender perfected interest
  
  4. UCC-1 Financing Statement
     └─ Enables: Lender's interest is now recorded, protects lender
  
  CONSTRUCTION LOAN FLOW:
  1. Construction Budget & Timeline
     └─ Enables: Lender appraisal decision, loan sizing
  
  2. GC Agreement (signed contract)
     └─ Enables: Lender construction disbursement mechanism, draw schedule
  
  3. Lender Loan Conditions Letter
     └─ Enables: Construction loan agreement signing
  
  4. Mechanic's Lien Waivers (from subs)
     └─ Enables: Next draw release (ongoing, each phase)
```

### Regulatory Dependencies (GATE 4)

```
HEALTHCARE:
  1. HIPAA Privacy Policy
     └─ Enables: HIPAA BAA (can't have BAA without policy)
  
  2. Business Associate Agreement
     └─ Enables: Handling patient data legally
  
  3. Breach Notification Plan
     └─ Enables: Response procedures if data incident

CONSTRUCTION:
  1. General Contractor License
     └─ Enables: Bidding on projects legally
  
  2. Building Permits (applied for)
     └─ Enables: Starting construction (approval required)

FINANCE:
  1. AML/KYC Compliance Program
     └─ Enables: Account opening, transaction processing
  
  2. OFAC Compliance Certification
     └─ Enables: Customer due diligence, sanctions screening
```

### Employment Dependencies (GATE 5)

```
  1. Employee Handbook
     └─ Enables: At-will employment agreements, policy compliance
  
  2. At-Will Employment Agreement
     └─ Enables: Day 1 employment, payroll processing
  
  3. Form I-9 (identity verification)
     └─ Enables: Legal work authorization, payroll
  
  4. Confidentiality & IP Assignment
     └─ Enables: Employee access to trade secrets, code ownership
  
  5. Payroll Setup (W-4, state forms)
     └─ Enables: First paycheck
```

### IP Dependencies (GATE 6)

```
  1. Provisional Patent Application
     └─ Enables: 1-year clock starts, can claim "patent pending"
  
  2. IP Assignment (if employee-invented)
     └─ Enables: Company ownership of invention, Utility patent filing with correct ownership
  
  3. Open-Source Compliance Audit
     └─ Enables: Shipping product legally, avoiding GPL liability
```

---

## SECTION 6: TIMELINE RULES

### Phased Timeline Model

All venture documents follow a 45-90 day sequence:

```
PHASE 1: FOUNDATION (Days 1-5)
  └─ Entity formation, core policies, foundational docs
  └─ Output: Legal entity ready to transact
  └─ Blocker: Nothing proceeds without Phase 1 complete

PHASE 2: OPERATIONAL SETUP (Days 5-15)
  └─ Insurance, compliance basics, employment setup
  └─ Output: Ready to hire, operate, conduct business
  └─ Blocker: Can't hire employees without Phase 2

PHASE 3: DEAL SPECIFIC (Days 15-30)
  └─ Deal documents, financing applications, regulatory filings
  └─ Output: Deal in motion, financing underway
  └─ Blocker: Complex deals may delay

PHASE 4: CLOSING PREPARATION (Days 30-45)
  └─ Final due diligence, closing conditions, signatures
  └─ Output: Deal ready to close
  └─ Blocker: Outstanding diligence items

PHASE 5: CLOSING & POST-CLOSE (Days 45+)
  └─ Fund draw, title transfer, operational handoff
  └─ Output: Deal closed, ongoing compliance
  └─ Blocker: Post-closing adjustments
```

### Examples by Venture Type

#### CONSTRUCTION ACQUISITION ($8.5M, 45-day close)

```
Days 1-5 (Phase 1: Foundation)
  ✓ Certificate of Formation
  ✓ Operating Agreement
  ✓ EIN Assignment
  ✓ Board Minutes
  ✓ Confidentiality Policy

Days 5-15 (Phase 2: Setup + Deal Kick-Off)
  ✓ General Liability Insurance
  ✓ Contractor License verification
  ✓ Letter of Intent signed (Day 10)
  ✓ Purchase Agreement draft begins
  ✓ Environmental Phase I ordered (7-10 day turnaround)

Days 15-30 (Phase 3: Deal Execution)
  ✓ Phase I ESA received & reviewed (Day 20)
  ✓ Purchase Agreement finalized & signed (Day 20)
  ✓ Financial diligence complete (Day 20)
  ✓ SBA financing application submitted (Day 15)
  ✓ Lender appraisal ordered (Day 15)
  ✓ Lender due diligence underway
  ✓ Board/shareholder resolutions prepared (Day 25)

Days 30-45 (Phase 4: Closing Prep)
  ✓ Lender Loan Conditions Letter received (Day 35)
  ✓ Phase II ESA complete (if needed, Day 35)
  ✓ Promissory Note finalized (Day 38)
  ✓ Security Agreement signed (Day 38)
  ✓ UCC-1 prepared for filing (Day 40)
  ✓ Board resolutions executed (Day 40)
  ✓ Closing date confirmed (Day 42)

Days 45+ (Phase 5: Closing & Post-Close)
  ✓ Funds wire received (Day 45)
  ✓ Deed of assignment executed (Day 45)
  ✓ UCC-1 filed (Day 45)
  ✓ Insurance updates filed (Day 46)
  ✓ Title transfer recorded (Day 46)
  ✓ Operational handoff begins (Day 46+)
```

#### STAFFING SERVICES ($500K SBA Loan, 30-day to funding)

```
Days 1-5
  ✓ Entity formation
  ✓ Employee handbook drafted
  ✓ Confidentiality policy

Days 5-15
  ✓ PEO agreement signed (Day 8)
  ✓ GL & Workers comp insurance (Day 7)
  ✓ SBA loan application submitted (Day 10)
  ✓ Personal financial statements prepared (Day 3)
  ✓ Business plan finalized (Day 7)

Days 15-30
  ✓ SBA loan underwriting (Days 15-25)
  ✓ Lender conditions letter (Day 20)
  ✓ Payroll setup in PEO system (Day 20)
  ✓ Background check procedures established (Day 15)

Days 30+
  ✓ SBA loan commitment letter (Day 28)
  ✓ Promissory note & security agreement (Day 30)
  ✓ Loan funds wire (Day 32)
  ✓ First staff hire (Day 35)
```

---

## SECTION 7: APPROVAL WORKFLOWS

Who must sign what, in what order.

### Approval Chain Principles

```
RULE: Serial, not parallel
- Document A (signed by party X) → Party Y reviews → Documents B, C, D (signed by Y) → Proceed

RULE: Authority levels
- Founder/Owner can sign operating docs, employment, standard agreements
- Board must approve financing, major contracts, business decisions
- Counsel reviews/approves legal documents
- Lender approves financing docs
- Regulatory body approves regulatory/compliance docs
```

### Example Approval Chains

#### Purchase Agreement (Multi-Party Deal)

```
Chain: Seller Legal → Buyer Legal → Seller Principals → Buyer Principals → Both Board resolutions

Day 1-5:  Buyer's counsel drafts (reviews business requirements from buyer principals)
Day 8:    Seller's counsel reviews + proposes edits (red-lines)
Day 12:   Buyer's counsel responds to red-lines, parties negotiate on phone
Day 15:   Both counsels agree on final language
Day 18:   Buyer principals review (board meeting if corporation)
Day 18:   Seller principals review (board meeting if corporation)
Day 20:   Both parties execute (wet signatures or digital signature)
Day 21:   Copies to all stakeholders (lender, insurance, etc.)
```

#### Construction Loan (Lender-Driven)

```
Chain: Borrower → Lender Loan Officer → Lender Underwriting → Lender Counsel → Lender Approval Committee → Borrower Counsel → Final signature

Day 1:    Borrower submits application
Day 5:    Loan officer reviews, requests additional docs
Day 10:   Underwriting committee reviews (internal)
Day 12:   Lender counsel drafts loan agreement (promissory note, security agreement)
Day 15:   Underwriting committee approves in principle (conditional on conditions)
Day 18:   Lender counsel finalizes loan documents
Day 25:   Borrower's counsel reviews (may suggest edits)
Day 28:   Borrower principals sign (may require board approval)
Day 30:   Lender loan committee gives final approval
Day 32:   Documents executed (both sides)
Day 35:   Funds wire
```

---

## SECTION 8: VALIDATION RULES

What makes a document set "complete" for each gate/phase?

### Validation Checklist Framework

```
GATE 1 VALIDATION (Operational):
  ✓ Certificate of Formation on file with Secretary of State
  ✓ Operating Agreement signed by all members/owners
  ✓ EIN assigned (IRS confirmation)
  ✓ Board minutes or written consent of members on file
  ✓ All core policies drafted and approved by counsel

GATE 2 VALIDATION (Deal):
  ✓ Purchase Agreement fully executed (both signatures)
  ✓ All required schedules completed and attached
  ✓ Third-party consents received (landlord, vendor, IP licensor)
  ✓ Board resolutions or shareholder approval on file
  ✓ Environmental assessments received and reviewed
  ✓ No outstanding conditions blocking closing

GATE 3 VALIDATION (Financing):
  IF Bank Loan:
    ✓ Loan commitment letter signed
    ✓ Promissory note drafted and reviewed by borrower's counsel
    ✓ Security agreement executed
    ✓ UCC-1 prepared with correct legal name and address
    ✓ Insurance certificates provided to lender
    ✓ Underwriting conditions satisfied
  
  IF VC Financing:
    ✓ Term sheet signed
    ✓ Stock purchase agreement finalized
    ✓ Cap table updated (pre/post investment)
    ✓ Board seat (if required) filled
    ✓ Shareholder agreements executed (all parties)
    ✓ Certificates of designation filed

GATE 4 VALIDATION (Regulatory):
  ✓ All required licenses obtained and current
  ✓ All required permits filed/approved
  ✓ Compliance certifications on file
  ✓ Insurance policies active and proof provided
  ✓ No outstanding regulatory violations

GATE 5 VALIDATION (Employment):
  ✓ Employee handbook reviewed and approved
  ✓ First employee I-9 on file (employment verified)
  ✓ Payroll system active (W-4, tax withholding set up)
  ✓ Confidentiality/NDA signed by all employees
  ✓ IP assignments on file for all employees (tech ventures)
  ✓ Workers' comp policy active

GATE 6 VALIDATION (IP):
  ✓ Patent application filed (provisional or full utility)
  ✓ Trademark application filed or registered
  ✓ Open-source audit completed (if shipping OSS)
  ✓ IP assignments in place for all employee creators
  ✓ License grants documented (Creative Commons, proprietary, etc.)

GATE 7 VALIDATION (Environmental):
  ✓ Phase I ESA received and reviewed
  ✓ Phase II ESA complete (if Phase I flagged issues)
  ✓ Environmental compliance certs on file (emissions, water, hazmat)
  ✓ Insurance policies active (environmental liability, pollution)
  ✓ Regulatory agencies confirm compliance status
```

### Document Readiness Metrics

```
DOCUMENT COMPLETION STATUS:
  DRAFT     = Legal review only (counsel reviewed, not yet signed)
  FINAL     = Ready to sign (all redlines resolved, both parties agree)
  EXECUTED  = Signed by required parties (wet signature or e-signature)
  FILED     = Submitted to government/regulatory body (if applicable)
  RECORDED  = Officially on file with government (deeds, UCC-1, etc.)
  ENFORCED  = Actively in use (insurance policies active, contracts binding)

GATE COMPLETION = All documents within gate have reached minimum status:
  Operational gate: All docs EXECUTED
  Deal gate: Master doc EXECUTED, schedules FINAL, third-party consents RECEIVED
  Financing gate: Commitment RECEIVED, loan docs EXECUTED, UCC FILED
  Regulatory gate: Licenses/permits FILED or RECORDED, compliance CERTIFIED
  Employment gate: Handbook approved, I-9 EXECUTED, payroll ACTIVE
  IP gate: Applications FILED or RECORDED, assignments EXECUTED
  Environmental gate: Assessments RECEIVED, compliance CERTIFIED
```

---

## SECTION 9: INTEGRATION POINTS

How the Document Requirement Engine connects to other systems.

### Input Sources

```
DATA SOURCE 1: VENTURE REGISTRY
  └─ Reads: venture_id, venture_type, sector, stage, maturity
  └─ Location: `_REGISTRIES/CANONICAL/ventures-by-sector.yaml`
  └─ Frequency: Real-time (pulled at document generation time)

DATA SOURCE 2: DEAL TRACKER
  └─ Reads: deal_type, deal_size_usd, counterparty_type, deal_structure
  └─ Location: ClickUp (CP-033 execution tracking)
  └─ Frequency: Real-time (whenever deal created/updated)

DATA SOURCE 3: MASTER-DOCUMENT-ONTOLOGY-REGISTRY
  └─ Reads: Full document definitions (purpose, fields, approval chain, template)
  └─ Location: `_ONTOLOGY/MASTER-DOCUMENT-ONTOLOGY-REGISTRY.yaml`
  └─ Frequency: Loaded at startup (cached)

DATA SOURCE 4: JURISDICTION MAPPER
  └─ Reads: Jurisdiction-specific regulatory requirements
  └─ Location: `_REGISTRIES/CANONICAL/JURISDICTION-REQUIREMENTS.yaml` (new registry needed)
  └─ Frequency: On-demand when jurisdiction provided

DATA SOURCE 5: CONTROL-PLANES-BY-SECTOR
  └─ Reads: Required approvers by sector (CP-033 ops, CP-034 engineering, etc.)
  └─ Location: `_REGISTRIES/CANONICAL/control-planes-by-sector.yaml`
  └─ Frequency: On-demand
```

### Output Destinations

```
DESTINATION 1: ClickUp Project Template
  └─ Action: Auto-create ClickUp project with tasks for each required document
  └─ Tasks: Doc name, due date, approval chain, template link
  └─ Trigger: Document set generated
  └─ Location: CP-033 (Execution control plane)
  
  Example ClickUp project structure:
  ├─ Foundation Docs (GATE 1)
  │  ├─ Task: Create Certificate of Formation (due Day 1)
  │  ├─ Task: Draft Operating Agreement (due Day 3)
  │  └─ [etc.]
  ├─ Deal Docs (GATE 2)
  │  ├─ Task: NDA signed (due Day 1)
  │  ├─ Task: LOI negotiated (due Day 5)
  │  └─ [etc.]
  └─ [Other gates...]

DESTINATION 2: Document Template Generator
  └─ Action: Populate templates from `_TEMPLATES/` with venture-specific data
  └─ Examples:
    - Operating Agreement → Inserts venture name, member names, ownership %
    - Promissory Note → Inserts loan amount, rate, term, collateral
    - Employment Agreement → Inserts company name, position, salary, NDA terms
  └─ Output: Markdown + DOCX (ready for attorney review)

DESTINATION 3: Approval Workflow Engine
  └─ Action: Create approval chain in document management system
  └─ Trigger: Document status changes
  └─ Example: When "Purchase Agreement" → Final, auto-send to all parties for signature

DESTINATION 4: Neo4j Knowledge Graph
  └─ Action: Record document requirements as relationships
  └─ Nodes: Venture → Document Requirement (e.g., CON-001 --requires--> PurchaseAgreement)
  └─ Edges: Dependencies (PurchaseAgreement --blocks--> PromissoryNote)
  └─ Queries: "What docs does CON-001 need?" OR "Which docs must be signed before ClosingStatement?"

DESTINATION 5: Qdrant Vector Index
  └─ Action: Embed document requirements for semantic search
  └─ Query examples:
    - "Find all documents required for $5M construction acquisition in NC"
    - "What environmental docs do logistics ventures need?"
    - "Which documents require board approval?"
  └─ Enables: Natural language queries by users
```

### Workflow Integration (MCP)

```
MCP TOOL 1: document_requirements_engine
  └─ Input: venture_id, deal_context (optional)
  └─ Output: Ordered list of required documents with timelines + approval chains
  └─ Example call:
    ```
    document_requirements_engine(
      venture_id="CON-001",
      deal_type="Acquisition",
      deal_size_usd=8500000,
      jurisdiction=["North Carolina", "Federal-OSHA"]
    )
    ```
  └─ Returns:
    ```
    {
      "venture": "CON-001",
      "gates_required": [1, 2, 3, 4, 5, 7],
      "total_documents": 48,
      "critical_path_days": 45,
      "documents": [
        {
          "doc_id": "DOC-001",
          "name": "Certificate of Formation",
          "gate": 1,
          "due_day": 1,
          "approval_chain": ["founder"],
          "dependencies": [],
          "status": "draft"
        },
        {...}
      ]
    }
    ```

MCP TOOL 2: create_document_project
  └─ Input: venture_id, requirements_output (from tool 1)
  └─ Action: Create ClickUp project with tasks, due dates, template links
  └─ Output: ClickUp project URL

MCP TOOL 3: populate_document_template
  └─ Input: template_id, venture_context
  └─ Action: Fill template with venture-specific data
  └─ Output: Markdown + DOCX

MCP TOOL 4: track_document_status
  └─ Input: venture_id
  └─ Output: Real-time document status across all gates
  └─ Example: "3 of 48 docs executed, 12 in draft, 33 pending"
```

---

## SECTION 10: PSEUDOCODE ALGORITHM

High-level pseudocode for engine implementation (not actual code).

```python
# DOCUMENT REQUIREMENT ENGINE - PSEUDOCODE

FUNCTION generate_document_requirements(venture_context):
  
  # Step 1: Load venture metadata
  venture = FETCH venture_context.venture_id FROM ventures-by-sector.yaml
  deal = FETCH deal_context FROM ClickUp IF deal_type != "Organic Founding"
  compliance = FETCH jurisdiction compliance reqs FROM jurisdiction-requirements.yaml
  
  # Step 2: Determine which gates to open
  required_gates = []
  
  GATE_1_ALWAYS = TRUE  # Operational always required
  required_gates.APPEND(1)
  
  IF deal.deal_type != "Organic Founding":
    required_gates.APPEND(2)  # Deal documents
  
  IF deal.deal_size_usd >= 1000000 OR venture.regulated_industry == TRUE:
    required_gates.APPEND(3)  # Financing documents
  
  IF venture.regulated_industry == TRUE:
    required_gates.APPEND(4)  # Regulatory documents
  
  IF venture.employee_count_est >= 1:
    required_gates.APPEND(5)  # Employment documents
  
  IF venture.data_sensitivity IN ["IP", "Confidential"] OR venture.venture_type == "Technology":
    required_gates.APPEND(6)  # IP documents
  
  IF venture.venture_type IN ["Construction", "Real Estate", "Logistics", "Transportation"] 
     OR venture.has_environmental_risk == TRUE:
    required_gates.APPEND(7)  # Environmental documents
  
  # Step 3: Route through each gate logic
  document_set = []
  
  FOR EACH gate IN required_gates:
    SWITCH gate:
      CASE 1:
        document_set.APPEND(GATE_1_OPERATIONAL_LOGIC())
      CASE 2:
        document_set.APPEND(GATE_2_DEAL_LOGIC(deal.deal_type, deal.deal_size))
      CASE 3:
        document_set.APPEND(GATE_3_FINANCING_LOGIC(lender_type, loan_size))
      CASE 4:
        document_set.APPEND(GATE_4_REGULATORY_LOGIC(venture.venture_type, jurisdiction))
      CASE 5:
        document_set.APPEND(GATE_5_EMPLOYMENT_LOGIC(venture.employee_count_est))
      CASE 6:
        document_set.APPEND(GATE_6_IP_LOGIC(venture.venture_type))
      CASE 7:
        document_set.APPEND(GATE_7_ENVIRONMENTAL_LOGIC(venture.venture_type))
  
  # Step 4: Apply dependencies (order documents)
  document_set = SORT_BY_DEPENDENCIES(document_set)
  
  # Step 5: Apply timelines
  FOR EACH document IN document_set:
    document.due_day = CALCULATE_TIMELINE(document.gate, document.dependencies)
    document.phase = DETERMINE_PHASE(document.due_day)
  
  # Step 6: Assign approval chains
  FOR EACH document IN document_set:
    document.approval_chain = FETCH approval_chain FROM MASTER_DOCUMENT_ONTOLOGY_REGISTRY
    document.approvers = RESOLVE_APPROVERS(approval_chain, venture.control_planes)
  
  # Step 7: Validate completeness
  validation_result = VALIDATE_DOCUMENT_SET(document_set)
  
  IF validation_result.status == "INCOMPLETE":
    LOG warning: validation_result.missing_documents
  
  # Step 8: Return formatted output
  RETURN {
    venture_id: venture.venture_id,
    gates_required: required_gates,
    total_documents: COUNT(document_set),
    critical_path_days: MAX(document.due_day FOR EACH document IN document_set),
    documents: document_set,
    validation_status: validation_result
  }

END FUNCTION


FUNCTION GATE_2_DEAL_LOGIC(deal_type, deal_size):
  
  documents = []
  
  IF deal_type == "Acquisition":
    documents.APPEND(NDA)
    documents.APPEND(LOI)
    documents.APPEND(PurchaseAgreement)
    documents.APPEND(DisclosureSchedules)
    documents.APPEND(EnvironmentalSiteAssessment_Phase1)
    
    IF deal_size >= 5000000:
      documents.APPEND(EnvironmentalSiteAssessment_Phase2)
      documents.APPEND(RepresentationsAndWarrantiesInsurance)
    
    documents.APPEND(StockholderConsent)
    documents.APPEND(ThirdPartyConsents)
    documents.APPEND(OfficerCertificates)
    documents.APPEND(ClosingStatement)
    documents.APPEND(DeedOfAssignment)
  
  ELSE IF deal_type == "Partnership":
    documents.APPEND(PartnershipAgreement)
    documents.APPEND(CapitalizationSchedule)
    documents.APPEND(OperatingProcedures)
    documents.APPEND(NonCompeteAgreement)
  
  ELSE IF deal_type == "Lease":
    documents.APPEND(CommercialLease)
    documents.APPEND(TenantImprovementAgreement)
    documents.APPEND(PersonalGuaranty)
    documents.APPEND(EstoppelCertificate)
  
  RETURN documents

END FUNCTION


FUNCTION SORT_BY_DEPENDENCIES(documents):
  
  ordered = []
  processed = []
  remaining = COPY(documents)
  
  WHILE COUNT(remaining) > 0:
    FOR EACH doc IN remaining:
      IF ALL(doc.dependencies) ARE IN processed:
        ordered.APPEND(doc)
        processed.APPEND(doc)
        remaining.REMOVE(doc)
  
  RETURN ordered

END FUNCTION


FUNCTION CALCULATE_TIMELINE(gate, dependencies):
  
  # Assign day based on gate + dependencies
  base_day_by_gate = {1: 1, 2: 5, 3: 10, 4: 10, 5: 10, 6: 20, 7: 10}
  
  base_day = base_day_by_gate[gate]
  
  IF dependencies.EXISTS:
    # Document can't be due before dependencies complete
    latest_dependency_day = MAX(dep.due_day FOR EACH dep IN dependencies)
    base_day = MAX(base_day, latest_dependency_day + 3)  # +3 days buffer
  
  RETURN base_day

END FUNCTION


FUNCTION VALIDATE_DOCUMENT_SET(documents):
  
  missing = []
  
  FOR EACH gate IN [1, 2, 3, 4, 5, 6, 7]:
    gate_docs = FILTER documents WHERE gate == gate
    
    IF gate.is_required AND COUNT(gate_docs) == 0:
      missing.APPEND("Gate " + gate + " has no documents")
  
  FOR EACH doc IN documents:
    IF doc.approval_chain.COUNT == 0:
      missing.APPEND(doc.name + " has no approval chain")
  
  IF missing.COUNT > 0:
    RETURN {status: "INCOMPLETE", errors: missing}
  ELSE:
    RETURN {status: "COMPLETE"}

END FUNCTION
```

---

## SUMMARY

**The Document Requirement Engine is a decision tree that answers: "What documents does this venture need to succeed?"**

**Key Principles:**
1. **Input-driven**: Venture type, deal type, jurisdiction → generate requirements
2. **Gate-based**: 7 gates (Operational, Deal, Financing, Regulatory, Employment, IP, Environmental)
3. **Dependency-aware**: Documents ordered by what must come first
4. **Timeline-enforced**: Each document has a due date tied to closing/operational deadlines
5. **Approval-complete**: Every document has an approval chain defined
6. **Validation-focused**: Completion checklist proves readiness

**Outputs:**
- Ordered list of 40-80 documents per venture (depending on complexity)
- ClickUp project template (auto-create tasks)
- Document templates (auto-populate with venture data)
- Approval workflows (route to signers)
- Dependency graph (visual: what blocks what)
- Neo4j relationships (queryable: "What docs does CON-001 need?")

**Next Step:** Implement engine using this specification + MCP tools to expose to agents.

---

**Document Status:** Ready for implementation  
**Maintained by:** Venture Operations (CP-033)  
**Last Updated:** 2026-09-06
