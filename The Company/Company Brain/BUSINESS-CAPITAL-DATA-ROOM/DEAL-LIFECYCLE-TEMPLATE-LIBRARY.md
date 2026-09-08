# Deal Lifecycle Template Library

**Purpose:** Canonical document sequences for three deal types. Use as reference for your venture's specific transaction.  
**Updated:** 2026-09-08 | **Authority:** CP-032 (Business Operations Control Plane)  
**Related:** [[VENTURE-OS-INSTITUTIONAL-ARCHITECTURE]], [[TERM-SHEET-MASTER]]

---

## Overview: Deal Lifecycle Patterns

Three universal patterns govern most venture deals:

1. **Acquisition Lifecycle** — Buy/sell of operating company or asset block
2. **Financing Round Lifecycle** — Equity investment, SAFE, or debt raise
3. **Real Estate Lifecycle** — Property purchase, financing, recording

Each has distinct document sequences, approval gates, and contingency structures. **Key insight:** Some documents are simultaneous (parallel work); others strictly sequential (one waits for prior).

---

## ACQUISITION DEAL LIFECYCLE

**Typical Duration:** 16-18 weeks (4-6 months) | **Simultaneous Workstreams:** Yes (2-3 parallel)

### Stage 1: Discovery (Week 0-2)

**Goal:** Buyer identifies target, seller confirms interest.

**Documents:**
- **NDA (Mutual)** — 2 pages
  - Prepared by: Seller's counsel or template
  - Signed by: Both parties (executive + authorized counsel)
  - Purpose: Protect sensitive discussions
  - Timing: Before any substantive conversation
  - Gate: NDA back before teaser shared

- **Teaser** — 2-3 pages
  - Prepared by: Seller's M&A advisor or CFO
  - Format: One-page executive summary + financials summary
  - Includes: Industry, size, EBITDA, growth rate, NO company name (blind initially)
  - Timing: Within 2-3 days of NDA
  - Gate: Buyer confirms interest to proceed

**Timeline:** Day 1 (NDA) → Day 3-4 (Teaser) → Day 7 (Buyer requests materials)

**Simultaneous:** Legal team drafts CIM while deal team pitches teaser to other potential buyers.

---

### Stage 2: Qualification (Week 2-4)

**Goal:** Buyer evaluates strategic fit; seller confirms buyer's financial capacity.

**Documents:**
- **Confidential Information Memorandum (CIM)** — 40-60 pages
  - Prepared by: Seller's investment banker or M&A advisor
  - Sections: Executive summary, company history, market position, financials (3-5 years audited + LTM), customer concentration, contracts, team, risks
  - Distribution: Only to qualified buyers under NDA
  - Timing: Week 2-3
  - Gate: Buyer confirms interest to submit LOI

- **Management Presentation** — 1 hour (slides + Q&A)
  - Prepared by: CEO + CFO
  - Format: Live or video; 30 slides covering business model, markets, financials, growth plan
  - Attendees: Buyer's board + lead investor
  - Timing: Week 3, after CIM review
  - Gate: Buyer decision to submit LOI or walk

- **Banker's Estimate of Value** — 2-3 pages (internal use)
  - Prepared by: Seller's investment banker
  - Method: Comparable companies, precedent transactions, DCF
  - Range: Typically 5-7x EBITDA for SaaS, 3-4x for services
  - Use: Seller sets LOI price expectations
  - Timing: Week 1 (before teaser), updated Week 3 (after buyer feedback)

**Timeline:** 
- Week 2: CIM distributed to shortlist (5-8 buyers)
- Week 3: Management presentations to top 2-3 buyers
- Week 4: LOI deadline (often Thursday, "sporting chance" for all buyers)

**Simultaneous:** 
- Financial due diligence team starts testing numbers (Phase 1)
- Legal team prepares data room structure
- Operations prepares customer/contract lists

---

### Stage 3: Term Sheet / Letter of Intent (Week 4-8)

**Goal:** Non-binding agreement on price, structure, and conditions.

**Documents:**
- **Letter of Intent (LOI)** — 4-6 pages
  - Prepared by: Buyer's counsel (standard language)
  - Key Terms: Purchase price, deal structure (cash/stock/earnout split), closing conditions, exclusivity period (30-60 days), termination rights
  - Price Format: One of:
    - Fixed: "$X million for 100% equity"
    - Range: "$X-Y million (valuation step-up for revenue growth)"
    - Earn-out: "$X base + $Y if EBITDA > target over 24 months"
  - Reps & Warranties: High-level only (full detail in SPA)
  - Gate: Signed by both CEO + board chair
  - Timing: Week 4 (buyer's offer) → Week 5 (seller counter) → Week 6 (signed)

- **Exclusivity Agreement** (often embedded in LOI)
  - Duration: 30-60 days (typical: 45 days)
  - Scope: Seller agrees not to shop deal to other buyers during exclusivity
  - Exceptions: Board-shop outs (board can brief other buyers if they walk)
  - Timing: Signed with LOI

- **Management Reps Letter** — 2-3 pages
  - Prepared by: CEO + CFO
  - Purpose: Seller's officers certify certain facts (financial accuracy, no undisclosed liabilities, no litigation)
  - Use: Buyer's due diligence comfort; basis for indemnification post-close
  - Timing: Week 6 (with LOI, sometimes Week 8 before SPA)

**Timeline:**
- Week 4 (Wed): Buyer submits LOI
- Week 4 (Thu-Fri): Seller review, board discussion
- Week 5 (Mon-Tue): Seller counter; buyer rebuttal
- Week 5 (Wed-Thu): Negotiation on price/earnout/carve-outs
- Week 6 (Mon): LOI signed
- Week 6-8: Exclusivity period begins; due diligence commences

**Contingencies:**
- Financing contingency: Buyer must secure debt by Week 10 (if leveraged deal)
- Customer concentration: If one customer = 30%+ revenue, buyer may demand revenue retention/guarantees
- Key person risk: CEO must stay 12-24 months (golden handcuffs)

---

### Stage 4: Due Diligence (Week 8-14)

**Goal:** Buyer validates all material facts; seller prepares closing.

**Documents:**
- **Data Room** — Virtual repository (Box/Intralinks)
  - Prepared by: Seller's legal team + CFO
  - Contents:
    - **Financial:** 3-5 years P&L, balance sheet, cash flow; tax returns; audit reports; revenue recognition policies
    - **Legal:** Corporate docs (cert of incorporation, bylaws), board minutes (2 years), stock ledger, cap table
    - **Contracts:** All customer contracts (>$50K annual), vendor agreements, employment agreements, IP licenses
    - **Compliance:** Insurance policies, tax audits, regulatory filings, health & safety records
    - **IP:** Patent registrations, trademark registrations, copyright registration, IP assignment docs
    - **HR:** Organization chart, offer letters (redacted), equity grants, severance agreements, benefits plans
    - **Litigation:** All active litigation, settlement agreements, insurance claims history
  - Access: Buyer's team + their advisors (legal, accounting, tax)
  - Timing: Open Week 8; additions/corrections through Week 13
  - Gate: All material questions answered before SPA signing

- **Financial Due Diligence (Phase 2)** — Seller's team provides
  - EBITDA reconciliation: Show how audited financials → claimed "normalized" EBITDA
  - Add-backs: Justify one-time costs, owner benefits, adjustments
  - Working capital study: Verify inventory, receivables, payables (timing-sensitive)
  - CapEx forecast: Seller certifies maintenance CapEx vs growth CapEx
  - Timeline: Week 8-12

- **Legal Due Diligence Report** — 30-50 pages (buyer's counsel)
  - Prepared by: Buyer's legal team (review data room)
  - Sections: Corporate status, capitalization, material contracts, litigation, IP, compliance, employment
  - Issues Identified: Lists every gap, risk, or potential breach
  - Timing: Week 12 (draft) → Week 13 (finalized)

- **Tax Due Diligence** — 10-15 pages (buyer's accountant)
  - Review: Tax returns, tax positions, carryforward losses (NOLs), depreciation schedules
  - COGS & deductions: Verify tax treatment is conservative
  - Timing: Week 10-12

**Parallel Workstream: Buyer Secures Financing**
- Week 8: Buyer submits loan application + seller financials to lender
- Week 10: Lender issues commitment letter (or decline)
- Week 12: Lender performs underwriting (review data room items)
- Gate: Financing must be committed before SPA signing (Week 14)

**Timeline:**
- Week 8: Data room opens; buyer team mobilizes (3-5 people)
- Week 9-10: First-round questions (50-100 items)
- Week 11: Second-round clarifications; deal team resolves
- Week 12: Legal/tax due diligence reports completed; issues list reviewed
- Week 13: Final questions; seller's counsel and buyer's counsel conference calls to resolve
- Week 14: All items resolved; parties ready for SPA

**Contingencies:**
- Revenue validation: Buyer independently verifies top 5 customer revenues
- Customer concentration: Buyer may negotiate customer guarantees if >25% revenue
- Warranty insurance: If any gaps found, buyer may require reps & warranties insurance

---

### Stage 5: Definitive Docs & SPA Negotiation (Week 14-16)

**Goal:** Finalize legal terms; prepare for closing.

**Documents:**
- **Stock Purchase Agreement (SPA)** — 50-80 pages
  - Prepared by: Buyer's counsel (draft) → Seller's counsel (comments) → Negotiations
  - Sections:
    - **Recitals:** Parties, representations of facts, intent
    - **Price & Closing:** Total consideration, payment method (wire/escrow), closing date (target: Week 16-17)
    - **Reps & Warranties:** Seller certifies company facts (financials accurate, no liabilities, IP owned, no litigation, etc.)
      - Survival period: Typically 18 months for general reps; 3-6 years for tax & environmental
    - **Conditions:** What must happen before close (financing, third-party consents, no material adverse change)
    - **Covenants:** Seller & buyer obligations pre-close (maintain business, no new debt, etc.)
    - **Indemnification:** Post-closing remedy if reps are breached
      - Indemnity basket: $50K (threshold before indemnification kicks in)
      - Indemnity cap: Often 10-15% of purchase price (e.g., if $10M deal, cap is $1-1.5M)
      - Indemnity period: 18-24 months post-close (exceptions for tax/employment = 3-6 years)
    - **Escrow:** Portion of purchase price (5-10%) held back 18-24 months to cover potential indemnity claims
  - Negotiation points:
    - Reps survival (seller wants shorter; buyer wants longer)
    - Basket & cap (seller wants high; buyer wants low)
    - Earnout mechanics (if applicable)
  - Timing: Week 14 (buyer draft) → Week 15 (seller comments & negotiation) → Week 16 (signed)

- **Schedules & Exhibits** (Part of SPA, 20-40 pages)
  - Cap Table (current equity ownership)
  - Material Contracts (list of all deals >$50K)
  - Litigation/Liabilities (all known issues)
  - Compliance Exceptions (any regulatory violations)
  - Employee/Benefits (headcount, benefit obligations)
  - Environmental/Real Estate (for ops with physical sites)

- **Closing Conditions** — Separate memo (2-3 pages, internal)
  - Prepared by: Deal counsel for both parties
  - Lists: All items that must be satisfied before wire (financials final check, board resolutions, third-party consents, lender sign-off, insurance, etc.)
  - Purpose: No surprises on closing day
  - Timing: Week 15

- **Officer's Certificate** — 2-3 pages (signed at closing)
  - Prepared by: Seller's CEO + CFO
  - Certifies: All closing conditions met, reps accurate as of closing
  - Signed: 24 hours before or at closing (Week 17-18)

- **Board Resolutions** — 3-5 pages (both parties)
  - Seller's board: Authorizes sale, approves SPA, approves earnout mechanics
  - Buyer's board: Authorizes purchase, financing terms, integration plan
  - Signed: Week 15 (before SPA signature for formality)

**Timeline:**
- Week 14 (Mon): Buyer issues SPA draft (50 pages)
- Week 14-15: Seller's counsel reviews, marks up (red-line)
- Week 15 (Wed-Thu): Negotiation calls (often 2-3 calls)
- Week 15 (Fri): Parties agree on final terms
- Week 16 (Mon): SPA signed by all parties + board resolutions
- Week 16-17: Final closing conditions checklist executed

**Contingencies:**
- Financing: Lender must issue final approval + commitment letter (no conditions that weren't in Week 8 commitment)
- Regulatory: Any antitrust review or industry license transfer required
- Third-party consents: Major customers, landlord, lenders must consent to change of control

---

### Stage 6: Closing (Week 16-18)

**Goal:** Execute final documents; transfer ownership.

**Documents:**
- **Wire Instructions** — 1 page (certified, signed)
  - Prepared by: Buyer's counsel or finance team
  - Contains: Bank name, routing, account # for wire of purchase price
  - Security: Seller's counsel independently verifies with bank (never trust email)
  - Timing: Day before closing

- **Closing Statement** — 2-3 pages
  - Prepared by: Deal counsel
  - Shows: Gross purchase price, less escrow, plus/minus working capital adjustments, net amount wired
  - Example:
    ```
    Gross Purchase Price:           $10,000,000
    Less: Escrow (10%):             ($1,000,000)
    Less: Seller debt payoff:         ($500,000)
    Plus: Assumed liabilities:        ($200,000)
    Working capital adjustment:     ($50,000)
    ────────────────────────────────
    Net wire to seller:             $8,250,000
    ```
  - Timing: Day of closing (final reconciliation)

- **Certificate of Good Standing** — 1 page (from Secretary of State)
  - Prepared by: Seller's corporate counsel
  - Shows: Company is validly incorporated, no default on filings
  - Requested: Week 17, obtained within 24-48 hours
  - Timing: Delivered at closing

- **Articles of Incorporation / Bylaws** — Certified copies
  - Prepared by: Secretary of State + company
  - Timing: Delivered at closing (as evidence of corporate authority)

- **Board Resolutions** (second signature) — Signed at closing
  - Both parties' boards re-sign confirming closing conditions met
  - Timing: Within 1 hour of wire (to create legal record)

- **Stock Certificates** — Physically signed
  - Prepared by: Seller's transfer agent or company secretary
  - Shows: Stock canceled on seller side; issued on buyer side
  - Timing: Delivered same day or next business day

- **Assumed Liability Schedules** — If buyer assumes debt/liabilities
  - Prepared by: Deal counsel
  - Lists: Which liabilities buyer is assuming vs. seller paying off at closing
  - Signed: Day of closing

- **Escrow Agreement** — If any cash held back
  - Prepared by: Escrow agent (bank or law firm)
  - Defines: Conditions for release, holdback amount, treatment of interest, dispute resolution
  - Parties: Buyer, seller, escrow agent
  - Timing: Signed at closing

**Closing Checklist:**
- [ ] All closing conditions satisfied (financing, consents, representations)
- [ ] SPA + schedules fully executed by all parties
- [ ] Officer's certificate signed by seller's officers
- [ ] Wire instructions confirmed (callback verification)
- [ ] Escrow agreement signed (if applicable)
- [ ] Board resolutions signed
- [ ] Stock certificate transferred (or notation made if electronic)
- [ ] Assumed liabilities acknowledged by buyer
- [ ] Purchase price wired to seller's account
- [ ] Proof of wire receipt obtained
- [ ] Closing statement executed

**Timeline:**
- Week 17 (Mon): Final closing checklist verified
- Week 17 (Tue-Wed): All documents executed and initialed
- Week 17 (Thu 2pm): Wire sent by buyer to seller
- Week 17 (Thu 3pm): Seller's counsel confirms receipt
- Week 17 (Fri): All final docs exchanged and recorded

---

### Stage 7: Post-Closing (Week 18+)

**Goal:** Transition operations; resolve any lingering issues.

**Documents:**
- **Closing Certificate (Final)** — 1 page
  - Confirms: All closing conditions satisfied, deal closed as of [date & time]
  - Signed: Deal counsel (evidence for future disputes)
  - Timing: Day after closing

- **Transition Services Agreement (if applicable)** — 10-20 pages
  - Prepared by: Seller's counsel
  - Scope: Seller provides limited services post-close (e.g., accounting support, customer introductions, systems transition) for 30-90 days
  - Cost: Seller compensated for time + costs
  - Termination: Buyer can terminate early; seller must wind down
  - Timing: Executed at closing if needed; typically 30-90 days

- **Indemnity Escrow Release Schedule** — Ongoing
  - Prepared by: Escrow agent + deal counsel
  - Milestones: 
    - 50% release at 12 months post-close (if no material claims)
    - 50% release at 18-24 months post-close (after indemnity period expires)
  - Claims: Buyer can make claims against escrow anytime during holdback period
  - Timing: Release checks issued 30-45 days after milestone dates

- **Integration Plan Execution** — Internal document
  - Prepared by: Buyer's operations team
  - Focuses: System consolidation, staff transitions, customer communication, financial consolidation
  - Timing: Ongoing through Month 6 post-close

- **Customer Retention Metrics** — Ongoing
  - Tracks: Customer churn, contract renewals, upsell opportunities
  - Purpose: If earnout exists, validates earnout calculations
  - Timing: Monthly reporting if earnout in place

**Timeline:**
- Week 18: Transition services begin (if needed)
- Month 1-3: Integration execution; system consolidation
- Month 6: Earnout measurement period (if applicable); first integration milestone
- Month 12: 50% escrow release (if no claims); earnout paid (if earned)
- Month 24: Final escrow release; indemnity period expires

---

## FINANCING ROUND LIFECYCLE

**Typical Duration:** 8-12 weeks (2-3 months) | **Structure:** Pre-money valuation + investment terms

### Stage 1: Discovery (Week 0-1)

**Goal:** Founder pitches investors; investors express interest.

**Documents:**
- **Pitch Deck** — 15-20 slides
  - Sections: Problem, solution, market size, traction, team, financials (3-year projection), funding ask, use of funds
  - Format: PDF or Google Slides (shareable)
  - Timing: First meeting or pre-meeting
  - Gate: Investor agrees to intro call

- **Term Sheet Expectations** — Internal memo (founder notes)
  - Prepared by: Founder + advisor
  - Records: Valuation expectations, dilution comfort, investor profile, timeline
  - Use: Founders align on acceptable terms before first investor meeting
  - Timing: Week 0 (before first pitch)

**Timeline:** Week 0-1

---

### Stage 2: Investor Engagement & Qualification (Week 1-3)

**Goal:** Founder pitches multiple investors; investors evaluate fit.

**Documents:**
- **Investment Memo** (Founder-prepared) — 8-10 pages
  - Sections: Executive summary, problem/solution, market opportunity, traction/metrics, team, financial projections (3-year, monthly burn rate), capital structure (cap table), funding ask + use of funds
  - Use: Investors evaluate company before meeting
  - Timing: Sent to interested investors Week 1-2

- **Cap Table** — 1-2 pages (spreadsheet)
  - Shows: Current share ownership, fully diluted shares (including option pool), founder vesting schedules
  - Format: CSV or Google Sheets
  - Purpose: Investor understands their dilution post-investment
  - Timing: Shared Week 2-3

- **Financial Model** — 3-5 page spreadsheet (separate file)
  - Sections: Monthly cash flow (24 months), P&L projections (3 years), unit economics, key metrics (CAC, LTV, churn)
  - Shared: With cap table
  - Timing: Week 2

- **Reference Calls** — Unwritten (3-5 calls)
  - Format: Investor calls founder's customers, advisors, past investors
  - Duration: 15-30 min calls
  - Purpose: Verify traction, team quality, product-market fit claims
  - Timing: Week 2-3 (in parallel with evaluation)

**Timeline:** 
- Week 1: Pitch decks + investment memos to 5-8 investors
- Week 2: First investor meetings (1-2 hours)
- Week 2-3: Reference calls conducted
- Week 3: Top 1-2 investors signal willingness to lead

**Gate:** Investor commits to "mark" (intent to invest) before moving to term sheet.

---

### Stage 3: Term Sheet / Investment Terms (Week 3-5)

**Goal:** Founder and lead investor agree on valuation, terms, governance.

**Documents:**
- **Term Sheet (TS)** — 4-6 pages (NON-BINDING, except confidentiality & exclusivity clauses)
  - Prepared by: Lead investor's counsel
  - Key Terms:
    - **Amount:** $X million investment
    - **Pre-money valuation:** Company worth $Y before investment (determines investor ownership %)
    - **Post-money valuation:** $Y + $X
    - **Investor ownership:** $X divided by post-money = ownership %
    - **Security:** Typically Series A Preferred Stock (not common stock)
    - **Board Seats:** Investor gets 1 board seat (founder keeps 1-2)
    - **Anti-dilution:** Protection if next round is lower valuation (weighted average or full ratchet)
    - **Liquidation Preference:** If company fails, investor gets paid first (typically 1x non-participating)
    - **Voting Rights:** Investor has veto on certain actions (new debt, equity issuance, M&A)
  - Exclusivity: 30-45 days (founder can't shop to other investors during this period)
  - Non-binding: Term sheet is indicative; only definitive docs are binding
  - Timing: Week 3 (investor draft) → Week 4 (founder review + negotiation) → Week 5 (signed)

- **SAFE** (Simple Agreements for Future Equity) — Alternative to TS + Series Docs
  - Prepared by: Y Combinator template (industry standard) or founder's counsel
  - Structure: Loan-like instrument; converts to preferred stock on future priced round or liquidity event
  - Advantage: Faster than full Series A docs (1 page agreement)
  - When used: Pre-Series A (seed rounds), founder wants to move fast
  - Timing: If using SAFE, can close in Week 3-4 (no full Series A negotiation needed)
  - Terms: Investment amount, valuation cap (max valuation for conversion), discount rate (typically 20-30% discount on next round valuation)

**Timeline (Full Term Sheet):**
- Week 3 (Mon): Investor issues TS
- Week 3-4: Founder review + advisor input; board meeting to approve
- Week 4 (Thu): Founder counter on valuation/board seats/anti-dilution
- Week 5 (Mon): Final negotiation call; TS signed
- Week 5-7: Exclusivity period (other investors cannot be approached)

**Timeline (SAFE):**
- Week 3 (Mon): Investor provides SAFE template
- Week 3 (Wed): Founder + counsel review; minimal negotiation (SAFE is standard)
- Week 3 (Fri): SAFE signed + wire received

**Contingencies:**
- Valuation: Founder may push for higher valuation; investor may demand lower (typically 20-30% negotiation range)
- Board seats: Investor wants veto on budget/hiring; founder wants autonomy (compromise: observer seat, then board seat at Series B)
- Liquidation preference: Investor wants participating preferred (1x + upside); founder wants non-participating (1x only) to preserve upside

---

### Stage 4: Due Diligence & Legal Docs (Week 5-8)

**Goal:** Investor validates team, product, financials; counsel drafts definitive docs.

**Documents:**
- **Due Diligence Questionnaire** — 10-20 pages (investor's legal team)
  - Covers: Company formation, IP ownership, employee agreements, customer contracts, financial accuracy, regulatory compliance
  - Prepared by: Founder's counsel (answers all questions)
  - Timing: Week 5-6

- **Amended & Restated Certificate of Incorporation (A&R Cert)** — 5-8 pages
  - Prepared by: Founder's counsel
  - Changes from current cert: 
    - Establishes Series A Preferred Stock class
    - Sets voting rights, conversion terms, liquidation preferences
    - Often increases authorized shares (to accommodate option pool)
  - Approved by: Board + shareholder vote
  - Timing: Week 6 (prepared) → Week 8 (signed at closing)

- **Series A Preferred Stock Purchase Agreement** — 30-50 pages
  - Prepared by: Investor's counsel (founder's counsel comments)
  - Sections:
    - Terms: Amount, price per share, investor & founder reps
    - Conditions: What must close (proper capitalization, IP owned, no litigation)
    - Governance: Board observer rights, information rights (quarterly financials/updates)
    - Anti-dilution: Protection formula if future rounds are lower
    - Drag-along/Tag-along: Investor can force sale (drag) or follow seller (tag)
  - Negotiation points: Anti-dilution scope, board voting, information rights frequency
  - Timing: Week 6 (draft) → Week 7 (negotiation) → Week 8 (signed)

- **Investor Rights Agreement** — 5-10 pages
  - Covers: Information rights (quarterly updates), board observer status, participation rights (right to invest in future rounds)
  - Preparation: Investor's counsel (standard)
  - Timing: Week 7

- **Co-Sale & Drag-Along Agreement** — 3-5 pages
  - Co-sale (tag-along): If founder sells shares, investor can sell pro-rata portion
  - Drag-along: If investor + founder agree to sell company, minority shareholders must sell too
  - Purpose: Prevents founder from cashing out while investor stays in dying company
  - Timing: Week 7

- **Option Pool Documentation** — If increasing option pool
  - 2008 Equity Incentive Plan (or equivalent): 10-15 pages
  - Outlines: Option pool size, vesting schedules (typically 4-year vesting, 1-year cliff), exercise price
  - Board approval: Week 6-7
  - Timing: Executed Week 8 (before or at closing)

- **Cap Table Update** — 1 page (revised)
  - Updated to reflect: New Series A shares, adjusted option pool, fully diluted share count
  - Signed: By founder + investor (proof of share count agreement)
  - Timing: Week 8

**Timeline:**
- Week 5: Investor issues due diligence questionnaire
- Week 5-6: Founder's counsel answers all questions; provides docs (IP assignments, employment agreements, customer contracts)
- Week 6: Investor's counsel drafts A&R Cert + Series A Purchase Agreement
- Week 6-7: Founder's counsel reviews + red-lines (typically 1-2 calls to resolve)
- Week 7: Board meeting to approve Series A + A&R Cert
- Week 8 (Mon-Tue): Final documents reviewed; closing conditions checklist

**Contingencies:**
- IP ownership: All founder side projects must be assigned to company (not personal projects)
- Employee vesting: Any founders on accelerated vesting due to funding (must revert to standard 4-year/1-year cliff)
- Affiliate transactions: Investor may require founder to disclose/terminate any related-party deals

---

### Stage 5: Closing (Week 8-9)

**Goal:** Execute docs; transfer funds; create company records.

**Documents:**
- **Closing Conditions Checklist** — 2-3 pages
  - Prepared by: Lead investor's counsel
  - Lists: All reps & warranties satisfied, docs executed, no material adverse changes, IP assigned, board approval obtained
  - Gate: Both parties sign off before wire
  - Timing: Day before or day of closing

- **Investor Signature Package** — Bundled documents
  - Contents: Series A Purchase Agreement, A&R Cert, Investor Rights Agreement, co-sale/drag-along, cap table
  - Format: Docusign or wet signatures (less common for startups)
  - Timing: Day of closing

- **Wire Instructions** — Certified by investor's bank
  - Amount: $X million investment
  - Destination: Company's bank account
  - Verification: Founder's counsel confirms instructions independently (never trust email)
  - Timing: 1-2 business days before closing

- **Board Resolutions** (Founder's board + investor board member)
  - Resolutions:
    1. Approve Series A investment + A&R Cert
    2. Approve option pool increase (if applicable)
    3. Elect investor's board designee
  - Signed: Week 8 (before or day of closing)

- **Capitalization Table (Final)** — Updated with Series A shares
  - Shows: Founder shares, employee option pool, Series A investor shares, fully diluted
  - Signed: By founder + lead investor (agreement on final ownership)
  - Timing: Closing day

- **Stock Certificates** — Issued for Series A shares
  - Format: Physical or electronic (most startups use electronic ledger now)
  - Signed: Company secretary + investor (proof of share ownership)
  - Timing: Same day or next business day post-closing

- **Certificate of Good Standing** — From Secretary of State
  - Confirms: Company is validly incorporated, no filings in default
  - Requested: Week 8
  - Timing: Delivered at closing

**Closing Checklist:**
- [ ] All closing conditions satisfied (IP, no litigation, board approval)
- [ ] Series A Purchase Agreement signed by investor + founder
- [ ] A&R Cert signed by founder + board + investor (some investors also sign)
- [ ] Investor Rights Agreement signed
- [ ] Co-sale/Drag-along signed
- [ ] Board resolutions signed by all directors (founder + investor designee + any other directors)
- [ ] Option pool approved (if increased)
- [ ] Wire received by company bank (proof of wire in account)
- [ ] Series A stock certificates issued (or ledger updated)
- [ ] Capitalization table finalized & signed by all parties

**Timeline:**
- Week 8 (Mon): Final documents executed
- Week 8 (Tue): Wire sent by investor
- Week 8 (Wed): Wire received by company; board resolutions signed
- Week 8 (Thu): Stock certificates issued; company announces Series A

---

### Stage 6: Post-Closing (Week 9+)

**Goal:** Company operates with new capital; investor governance begins.

**Documents:**
- **Series A Funding Announcement** — Blog post or press release (1-2 pages)
  - Prepared by: Founder + investor
  - Includes: Funding amount, use of funds, customer quotes, investor quote
  - Timing: Week 9 (1-2 weeks post-closing)

- **Investor Update #1** — Due 30 days post-closing
  - Prepared by: Founder + CFO
  - Contents: Month 1 metrics (users, revenue, burn rate), team updates, product roadmap, any material risks
  - Distribution: Investor + board members
  - Frequency: Monthly thereafter

- **12-Month Financial Projections (Updated)** — If investor didn't have detailed ones
  - Prepared by: Founder + CFO
  - Shows: Monthly revenue/burn, paths to profitability or next funding round
  - Timing: After Series A (refined based on investor feedback)

- **Board Meeting Schedule** — Recurring meetings
  - Frequency: Monthly during early stage; quarterly after profitability/Series B
  - Attendees: Founder CEO + investor board designee + any other board members/observers
  - Agenda: Company metrics, product roadmap, hiring, fundraising (if applicable)
  - Timing: Ongoing

**Timeline:**
- Week 9-10: Announcement; first investor communications
- Week 10+: Monthly board updates + investor updates begin
- Month 3: First formal board meeting (if not done at closing)
- Month 6-12: Series A investor engagement (quarterly board meetings, periodic calls)

---

## REAL ESTATE DEAL LIFECYCLE

**Typical Duration:** 8-12 weeks (2-3 months) | **Key:** Contingency period is critical

### Stage 1: Discovery & Offer (Week 0-1)

**Goal:** Buyer finds property; submits offer.

**Documents:**
- **Property Information Sheet** — 2-3 pages
  - Prepared by: Seller's agent or broker
  - Contents: Address, square footage, lot size, year built, zoning, recent renovations, property taxes, utilities, HOA fees (if applicable)
  - Use: Buyer evaluates property before viewing
  - Timing: Before property tour

- **Comparable Market Analysis (CMA)** — 3-5 pages
  - Prepared by: Buyer's agent or appraiser
  - Shows: Similar properties sold nearby (past 6-12 months), their sale prices, price per square foot
  - Purpose: Justify offer price; lender uses for appraisal
  - Timing: Week 0 (before offer submitted)

- **Purchase & Sale Agreement (Offer)** — 2-4 pages (template-based)
  - Prepared by: Buyer's agent (state-standard form)
  - Key Terms:
    - **Property:** Legal description (from deed)
    - **Purchase price:** $X (total offer)
    - **Earnest money:** 1-3% of purchase price (good faith deposit)
    - **Contingencies:** 
      - Financing contingency (30-45 days; buyer must obtain mortgage approval or can back out)
      - Inspection contingency (10-15 days; buyer can inspect property, request repairs, or walk away)
      - Appraisal contingency (lender's appraisal must support price or buyer can walk)
      - Title contingency (seller must provide clear title)
    - **Closing date:** Typically 30-45 days from acceptance
    - **Seller concessions:** Seller may pay buyer's closing costs (2-3% of purchase price)
  - Timeline: Week 0-1 (offer submitted by buyer; seller has 24-48 hours to respond)

- **Inspection Contingency Period** — Starting Week 2
  - Buyer's inspector visits property (home inspection, pest inspection, radon if applicable)
  - Buyer has 10-14 days to identify issues + request repairs or credit
  - Seller has 5 days to respond with repair offer or credit

**Timeline:**
- Week 0 (Fri): Buyer submits offer
- Week 0 (Fri-Sat): Seller reviews; counters or accepts
- Week 1 (Mon): Offer accepted; earnest money wired to escrow (1-2 business days)
- Week 2 (Mon): Inspection contingency begins (10-14 days)

---

### Stage 2: Earnest Money & Inspection (Week 1-3)

**Goal:** Buyer validates property condition; earnest money held in escrow.

**Documents:**
- **Earnest Money Deposit Receipt** — 1 page
  - Prepared by: Escrow agent
  - Shows: Amount, property, parties, escrow agent contact info
  - Timeline: Issued 24-48 hours after offer acceptance
  - Use: Proof earnest money received (held in trust)

- **Home Inspection Report** — 20-40 pages
  - Prepared by: Licensed home inspector
  - Covers: Foundation, roof, HVAC, plumbing, electrical, appliances, pest damage, mold, lead paint (if pre-1978)
  - Findings: Categorized as major repairs (roof/foundation), minor (cosmetic), or informational
  - Cost: Typically $400-800 (paid by buyer)
  - Timeline: Week 2-3 (2-3 days after inspection appointment)

- **Pest / Termite Inspection** — 2-3 pages (if required by lender)
  - Prepared by: Licensed pest control inspector
  - Covers: Termites, carpenter ants, wood rot, previous pest treatments
  - Cost: $100-200 (typically paid by seller or buyer per state law)
  - Timeline: Often same week as home inspection

- **Radon Test** — 1-2 pages (if buyer requests)
  - Prepared by: Radon testing company
  - Shows: Radon levels (safe if <2 pCi/L; requires mitigation if higher)
  - Cost: $150-300
  - Timeline: Week 2-3

- **Title Search / Preliminary Title Report** — 5-10 pages
  - Prepared by: Title company
  - Shows: Ownership history, liens, easements, covenants on the property
  - Timing: Ordered Week 1 (after offer accepted); completed Week 2-3
  - Gate: Title must be "clear" (no liens except mortgage lender's)
  - Use: Basis for title insurance quote

- **Repair Request / Negotiation** — 1-2 pages
  - Prepared by: Buyer (based on inspection findings)
  - Format: List of repairs + $ credits requested from seller
  - Example:
    ```
    1. Roof repair ($2,500) → Request $2,500 credit
    2. HVAC cleaning ($500) → Request $500 credit
    Total requested credit: $3,000
    ```
  - Timeline: Week 3 (after inspection; buyer has 5-10 days to submit)
  - Gate: Seller counters within 3-5 days

**Timeline:**
- Week 1: Earnest money deposited
- Week 2: Home inspection + pest inspection performed
- Week 2-3: Inspection reports received
- Week 3 (Mon-Tue): Buyer reviews reports; submits repair request
- Week 3 (Tue-Wed): Seller reviews; counters with repair offer or credit
- Week 3 (Thu): Parties agree on repairs/credits or buyer can walk away

---

### Stage 3: Financing & Appraisal (Week 2-5)

**Goal:** Lender approves loan; property appraisal validates price.

**Documents (Prepared in parallel with inspection contingency):**
- **Loan Application** — 5-10 pages
  - Prepared by: Buyer (borrower)
  - Contents: Income documentation, employment history, assets, liabilities, credit authorization
  - Submitted to: Lender (bank, mortgage company, or broker)
  - Timeline: Week 1-2 (same week offer accepted)

- **Pre-Qualification / Pre-Approval Letter** — 1-2 pages
  - Prepared by: Lender
  - States: Buyer is approved for $X loan at Y% interest rate (subject to appraisal & property approval)
  - Use: Proof to seller that buyer is serious + financially capable
  - Timeline: Week 1-2 (if buyer didn't have pre-approval before offer)

- **Appraisal Order** — Internal lender document
  - Prepared by: Lender (orders from appraisal company)
  - Purpose: Third-party valuation to ensure property supports loan amount
  - Cost: $400-600 (paid by buyer via appraisal fee in loan application)
  - Timeline: Ordered Week 2-3

- **Appraisal Report** — 15-25 pages
  - Prepared by: Licensed appraiser
  - Method: Comparable market analysis (recent sales of similar properties nearby)
  - Conclusion: "The value of this property is $X"
  - If appraisal < purchase price: Buyer can renegotiate price, pay difference in cash, or walk away (appraisal contingency)
  - Timeline: Week 4-5 (7-10 days after appraisal ordered)

- **Underwriting Questionnaire** — 5-10 pages
  - Prepared by: Lender (underwriter)
  - Asks: Follow-up questions on borrower's finances, any credit issues, employment changes
  - Response: Buyer provides additional docs (tax returns, bank statements, letters of explanation)
  - Timeline: Week 3-4

- **Clear to Close Letter** — 1 page
  - Prepared by: Lender
  - States: "All underwriting conditions satisfied; loan approved; ready for closing"
  - Timing: Week 5 (3-5 days before closing)
  - Gate: This is final lender approval

**Timeline:**
- Week 1-2: Loan application submitted
- Week 2-3: Appraisal ordered
- Week 3-4: Underwriting questions submitted
- Week 4-5: Appraisal returned
- Week 5 (Mon): Final underwriting review
- Week 5 (Wed): Clear to close issued

---

### Stage 4: Title & Insurance (Week 3-6)

**Goal:** Secure title insurance; verify property is free of liens.

**Documents:**
- **Title Search** — Already ordered in Stage 2
  - Completed: Week 2-3
  - Shows: Any liens, judgments, easements, homeowners association

- **Title Insurance Commitment** — 5-10 pages
  - Prepared by: Title company
  - Shows: What title insurance will cover (standard exclusions: zoning, utilities, etc.)
  - Cost: 0.5-1% of purchase price (varies by state; often split between buyer & seller)
  - Timeline: Week 3-4

- **Title Insurance Policy (Final)** — Issued at closing
  - Prepared by: Title company (after closing)
  - Covers: Buyer + lender for loss due to title defects
  - Cost: Paid at closing (included in closing costs)
  - Timeline: Issued Week 6 (at or after closing)

- **Homeowners Insurance Policy** — Prepared by: Insurance agent
  - Required by: Lender (before closing)
  - Coverage: Property damage, liability, medical payment
  - Cost: Varies by property ($800-2,000/year for modest home)
  - Binder: Issued Week 4-5 (confirms coverage starting at closing)
  - Full policy: Issued after closing
  - Timeline: Binder required by lender before "clear to close"

- **HOA Documents** (if applicable) — 5-15 pages
  - Prepared by: HOA (homeowners association)
  - Contents: HOA bylaws, meeting minutes, financial statements, reserve study, list of current assessments
  - Requested by: Buyer's attorney or title company (Week 2-3)
  - Cost: Typically $200-500 (paid by buyer)
  - Timeline: Received Week 3-4

- **Property Survey** (if ordered) — 1-2 pages (map format)
  - Prepared by: Licensed surveyor
  - Shows: Property boundary lines, existing structures, easements
  - Cost: $300-600
  - Required if: Lender requires it (older properties or if boundaries unclear)
  - Timeline: Week 2-4 (if ordered early)

**Timeline:**
- Week 2-3: Title search completed
- Week 3-4: Title commitment + insurance quote received
- Week 4-5: HOA docs reviewed; homeowners insurance binder obtained
- Week 5-6: Final title policy ready for closing

---

### Stage 5: Closing Preparation (Week 5-6)

**Goal:** Finalize loan terms; prepare closing documents.

**Documents:**
- **Closing Disclosure** — 3-4 pages (TRID form, federal requirement)
  - Prepared by: Lender
  - Shows: Final loan amount, interest rate, monthly payment, all closing costs (title insurance, appraisal, lender fees, taxes, insurance, etc.)
  - Buyer must receive: 3 business days before closing
  - Important: Compare to initial Loan Estimate (should be similar; flag major differences)
  - Timing: Week 5 (issued 3 business days before closing)

- **Promissory Note** — 2-3 pages
  - Prepared by: Lender (standard form)
  - Terms: Loan amount, interest rate, repayment schedule, prepayment terms, default consequences
  - Signed by: Borrower(s) at closing
  - Timeline: Week 6 (at closing)

- **Deed of Trust / Mortgage** — 5-10 pages
  - Prepared by: Lender or title company
  - Secures: Lender's right to foreclose if borrower defaults
  - Signed by: Borrower(s) at closing
  - Timeline: Week 6 (at closing)
  - Recorded: After closing (lender records with county recorder's office)

- **1003 Loan Application** (Final reconciliation) — Buyer verifies final loan terms match application
  - Timing: Week 5 (before Closing Disclosure issued)

- **Closing Agenda / Checklist** — Prepared by: Closing agent (attorney or title company)
  - Lists: All documents to be signed, who signs what, funds to be wired
  - Timeline: Sent to buyer + seller Week 5-6

- **Walk-Through** — Not a document (physical inspection)
  - Timing: Day before or day of closing
  - Purpose: Buyer confirms no damage; all agreed repairs completed; seller's personal items removed
  - Decision point: Buyer can still back out at this stage if major issues discovered

**Timeline:**
- Week 5 (Mon): Closing Disclosure issued; buyer has 3 business days to review
- Week 5 (Fri): Buyer review deadline
- Week 6 (Mon): Walk-through inspection
- Week 6 (Tue): Parties confirm readiness for closing

---

### Stage 6: Closing (Week 6)

**Goal:** Sign all documents; transfer title; record deed.

**Documents:**
- **Title Commitment (Final)** — Confirms title is clear as of closing date
  - Timing: Day before closing

- **Closing Statement / HUD-1** — 2-3 pages (showing all financial transactions)
  - Prepared by: Closing agent (title company or attorney)
  - Shows: 
    - Purchase price
    - Less: Earnest money already paid (credited to buyer)
    - Less: Buyer closing costs (title, appraisal, lender fees, etc.)
    - Less: Seller concessions (if any)
    - Wire amount due from buyer (to closing agent)
    - Wire amount due to seller (minus seller costs & loan payoff)
  - Timeline: Provided to parties 24 hours before closing (for final review)

- **Deed** — 1-2 pages (legal form)
  - Prepared by: Seller's attorney or title company
  - Type: Warranty deed (guarantees clear title) or quitclaim deed (no guarantee; used in family transfers)
  - Signed by: Seller (grantor) at closing
  - Transferred to: Buyer (grantee)
  - Recorded: By closing agent with county recorder (within 24-48 hours after closing)
  - Timeline: Signed at closing

- **Bill of Sale** (if personal property included) — 1 page
  - Includes: Appliances, fixtures, furniture buyer is purchasing (outside of real estate)
  - Signed: Seller + buyer
  - Timing: Signed at closing (optional, only if personal property involved)

- **Affidavit of Non-Foreign Investment in Real Property** — 1 page
  - Seller certifies: Seller is not a foreign investor (federal requirement; allows buyer to avoid withholding taxes)
  - Signed: Seller
  - Timing: Signed at closing

- **Closing Documents Package** — Bundle signed at closing
  - Contents:
    - Promissory note (signed by buyer)
    - Deed of trust / mortgage (signed by buyer)
    - Deed (signed by seller)
    - Closing statement (signed by both parties)
    - Title insurance policy commitment (copy provided)
    - Homeowners insurance policy binder (proof provided)
    - Closing disclosure (already signed by buyer 3 days prior)
    - Any HOA documents (if applicable)
  - Format: Original wet signatures (some states allow DocuSign, but traditional closings use in-person signatures for security)

- **Fund Wires** — Two wire transfers
  - Wire #1: Buyer's lender sends loan proceeds to closing agent
  - Wire #2: Buyer sends remaining funds to closing agent (down payment + closing costs not covered by lender)
  - Verification: Closing agent confirms receipt of both wires before releasing funds

**Closing Day Checklist:**
- [ ] All parties present (buyer, seller, closing agent/attorney, lender rep if in-person)
- [ ] Buyer brings: ID, proof of funds (for down payment), homeowners insurance policy binder
- [ ] Seller brings: ID, any keys/access devices, proof of payoff for existing mortgage
- [ ] Closing agent has: All signed closing documents, proof of wire receipts
- [ ] Buyer reviews & signs: Note, deed of trust, closing disclosure (re-signs if HUD-1 changed), deed
- [ ] Seller reviews & signs: Deed, closing statement, any addendums
- [ ] Wires verified: Lender wire received, buyer wire received
- [ ] Funds released: Closing agent pays seller (after lender's loan payoff), pays title company, keeps fees
- [ ] Deed delivery: Deed given to closing agent for recording

**Timeline:**
- Week 6 (Mon 2pm): Closing meeting (typically 1-2 hours)
- Week 6 (Mon 3pm): All documents signed
- Week 6 (Mon 4pm): Wires confirmed received
- Week 6 (Tue): Closing agent records deed with county recorder

---

### Stage 7: Post-Closing (Week 6+)

**Goal:** Record deed; finalize insurance; transfer utilities.

**Documents:**
- **Recorded Deed** — Photocopy (1-2 pages, recorded by county)
  - Prepared by: County recorder's office
  - Shows: Recording date + book/page number (official record of ownership)
  - Mailed to: Buyer's attorney or title company (typically within 2-4 weeks)
  - Purpose: Proof of ownership; needed for future refinancing/sale
  - Timeline: Recorded within 24-48 hours after closing; received by buyer in 2-4 weeks

- **Title Insurance Policy (Final)** — Issued by title company
  - Covers: Buyer + lender
  - Timeline: Mailed within 30-60 days of closing (follows recorded deed)

- **Homeowners Insurance Policy (Final)** — Issued by insurance agent
  - Replaces binder; actual ongoing policy
  - Timing: Effective at closing; full policy arrives within 2 weeks

- **Mortgage Statement (First)** — From lender
  - Shows: Loan amount, first payment due date, escrow account (taxes + insurance held by lender)
  - Timing: Arrives within 30 days of closing

- **Utility Transfer Confirmations** — From utility companies
  - Buyer transfers: Water, electric, gas, internet from seller's name to buyer's
  - Timeline: Arrange 1-2 weeks before closing; confirmations received after closing
  - Format: Email or letters from each utility provider

**Post-Closing Checklist:**
- [ ] Deed recorded with county (confirm recording number + date)
- [ ] Title insurance policy received + reviewed
- [ ] Homeowners insurance active + policy received
- [ ] Utilities transferred to buyer's name
- [ ] First mortgage payment scheduled
- [ ] Update property address with: Tax assessor, insurance company, utility companies, employer, IRS

**Timeline:**
- Week 6 (Tue-Wed): Deed recorded
- Week 6-8: Utilities transferred
- Week 6-10: Title insurance policy received
- Week 6-12: Mortgage statements + insurance finalized
- Ongoing: Monthly mortgage payments begin

---

## APPENDIX: CONTINGENCY MASTERLIST

### Acquisition Deal Contingencies
| Contingency | Trigger | Remedy | Timeline |
|---|---|---|---|
| **Financing** | Buyer can't secure debt | Deal voids; earnest money returned | Must clear by Week 10 |
| **Customer concentration** | One customer = >25% revenue | Buyer can renegotiate price or request customer guarantees | Flagged in due diligence (Week 10-12) |
| **Material adverse change** | Major customer loss, regulatory action, key person departure | Buyer can terminate or renegotiate | Monitored through closing (Week 16-18) |
| **Third-party consents** | Major customer/landlord refuses change of control | Buyer can terminate or negotiate new terms | Identified in data room (Week 8) |
| **Reps & warranties** | Seller's representations found false | Indemnification post-close; escrow funds available | 18-24 months post-close |

### Financing Round Contingencies
| Contingency | Trigger | Remedy | Timeline |
|---|---|---|---|
| **Due diligence findings** | Investor discovers material issue (IP not owned, litigation hidden) | Investor may reduce price or terminate | Week 5-7 |
| **Valuation adjustment** | Company metrics don't meet expectations (revenue lower than projected) | Lower valuation or investor walks | Week 4-5 |
| **Regulatory** | SEC review, antitrust concern (if strategic investor) | Delay closing 30-60 days or terminate | Identified Week 5-6 |
| **Board approval** | Shareholder/board vote required (for authorization) | Vote held; if fails, deal fails | Week 7-8 |

### Real Estate Contingencies
| Contingency | Trigger | Remedy | Timeline |
|---|---|---|---|
| **Appraisal** | Appraisal < purchase price | Buyer can renegotiate price down, pay difference, or walk | Week 4-5 |
| **Inspection** | Inspection reveals major defects (foundation, roof, termites) | Buyer can request repairs, credits, or terminate | Week 2-3 |
| **Title** | Title search finds lien or encumbrance | Seller must clear title or buyer can terminate | Week 2-4 |
| **Financing** | Lender denies loan | Buyer can terminate (within financing contingency period) | Week 5 (before clear to close) |
| **HOA** | HOA documents show special assessment coming | Buyer can renegotiate price or terminate | Week 3-4 |

---

**Next Steps:**
1. Identify your deal type (Acquisition, Financing, or Real Estate)
2. Reference the appropriate Stage sections above
3. Adapt templates to your specific situation (lawyer/accountant reviews)
4. Track timeline milestones in ClickUp (auto-reminders for contingency deadlines)
5. Update this file with your deal-specific documents as you progress

**Authority:** CP-032 (Business Operations Control Plane) + Venture Finance Domain (Domain 20)
