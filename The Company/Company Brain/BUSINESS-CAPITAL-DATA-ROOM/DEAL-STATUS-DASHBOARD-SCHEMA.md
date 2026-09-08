# Deal Status Dashboard Schema

**Scope:** Unified tracking system for venture deal lifecycle, document completion, and capital/partnership milestones across Company Brain operating ventures.

**Authority:** CP-026 (Financial Control Plane) × CP-033 (Execution/ClickUp Orchestration)

**Master Registry Location:** `_REGISTRIES/CANONICAL/DEAL_STATUS_REGISTRY.yaml`

**Last Updated:** 2026-09-08

---

## 1. OVERVIEW & PHILOSOPHY

Deal Status Dashboard provides real-time visibility into five parallel acquisition/financing/partnership deals running across Company Brain's operating ventures.

**Why This Exists:**
- Deals involve 50-200 interdependent documents
- Documents have prerequisites (can't sign Definitive Agreement until term sheet signed)
- Each stage has hard deadlines (miss signature by Friday, entire next stage slips)
- Five deals running in parallel need unified oversight
- Counsel, CFO, investors, and founders each need different views

**What It Tracks:**
- Current stage for each deal
- Document completion % (what's done vs. required for this stage)
- Blocking dependencies (what's preventing next step)
- Key dates and stage transitions
- Responsible parties and their actions
- Status history (when did diligence start? when did legal review finish?)

**Integration Points:**
```
BUSINESS-CAPITAL-DATA-ROOM/     (source of truth for documents)
    ↓
DEAL-STATUS-DASHBOARD-SCHEMA    (this file: data structure + views)
    ↓
ClickUp (CP-033)                 (tasks for each action: "Legal Review NDA")
    ↓
Neo4j Knowledge Graph            (deal → venture → capabilities → outcomes)
    ↓
Dashboards (email/Notion/Hero)   (visibility for leadership)
```

---

## 2. DATA STRUCTURE

### 2.1 Core Deal Entity

```yaml
deal_id: "CON-001-ACQ-2026-09"
deal_type: "Acquisition" | "Growth Capital" | "Financing" | "Partnership"
venture_id: "CON-001"
venture_name: "Ace Construction"
sector: "SEC-009-Construction"

# Timeline
initiated_date: "2026-09-01"
target_close_date: "2026-12-31"
current_stage: "Diligence"
stage_start_date: "2026-09-10"
stage_end_date: "2026-10-15" # estimated

# Parties involved
counterparty_name: "Vertex Capital Partners"
counterparty_type: "Private Equity"
deal_size: "$5.2M"
deal_currency: "USD"
lead_counsel:
  name: "Jane Smith"
  firm: "Acme Legal LLP"
  email: "jsmith@acmeLegal.com"
lead_facilitator:
  name: "Marcus Chen"
  role: "CEO, CON-001"
  email: "marcus@acecon.com"

# Progress & Status
progress_pct: 64  # docs complete / total docs required at this stage
last_update: "2026-09-08T15:30:00Z"
status_direction: "On Track" | "At Risk" | "Blocked" | "Accelerating"

# SLA tracking
days_in_stage: 5
days_until_stage_deadline: 37
```

### 2.2 Document Schema (Array)

Each deal has 50-200 documents tracked in a documents array:

```yaml
documents:
  - doc_id: "CON-001-ACQ-2026-NDA-001"
    doc_type: "NDA"                          # Type (predefined list)
    doc_name: "Mutual Non-Disclosure Agreement"
    
    # Status tracking
    status: "Completed"                      # Status enum (see 2.3 below)
    completion_pct: 100
    
    # Dates
    created_date: "2026-09-01"
    started_date: "2026-09-01"
    in_review_date: "2026-09-03"
    signed_date: "2026-09-08"
    due_date: "2026-09-15"                   # SLA due date
    due_stage: "Discovery"                   # Must complete by this stage
    days_to_due: 7
    
    # Content & ownership
    latest_version: "v2"
    signer_count: 2
    signers_completed: 2
    pending_signers: []
    assigned_to:
      - name: "Jane Smith"
        role: "Counsel"
        email: "jsmith@acmeLegal.com"
    
    # Dependencies
    depends_on:
      - "CON-001-ACQ-2026-NDA-001"           # Prerequisites
    blocks:
      - "CON-001-ACQ-2026-TERM-SHEET-001"    # What this doc unblocks
    is_blocked: false
    blocked_reason: null
    
    # Location & Links
    file_path: "BUSINESS-CAPITAL-DATA-ROOM/CON-001/02_LEGAL/NDA.pdf"
    signature_type: "Digital Signature (DocuSign)" | "Manual" | "Countersignature Required"
    storage_link: "https://drive.google.com/..."
    
    # Metadata
    classification: "Confidential"
    legal_review_required: true
    legal_review_complete: true
    board_approval_required: false
    cfo_approval_required: true
    cfo_approved: true
    investor_review_required: false
    
    # Notes
    notes: "Signed 2026-09-08. Minor redlines on Section 4 accepted by both parties."
```

### 2.3 Status Enum (Canonical)

```yaml
statuses:
  "Not Started":
    icon: "⬜"
    color: "#999999"  # Gray
    meaning: "No work begun yet"
    sla_risk: false
    
  "In Preparation":
    icon: "🟡"
    color: "#FFC107"  # Amber
    meaning: "Being drafted/prepared"
    sla_risk: false
    
  "In Review":
    icon: "🔵"
    color: "#2196F3"  # Blue
    meaning: "Legal/CFO review in progress"
    sla_risk: false
    if_overdue: "needs_escalation"
    
  "Awaiting Signature":
    icon: "⏳"
    color: "#FF9800"  # Orange
    meaning: "Ready to sign, waiting for counterparty"
    sla_risk: true
    if_overdue: "escalate_to_counterparty"
    
  "Completed":
    icon: "✅"
    color: "#4CAF50"  # Green
    meaning: "Signed and filed"
    sla_risk: false
    
  "Blocked":
    icon: "🛑"
    color: "#F44336"  # Red
    meaning: "Cannot proceed without dependency"
    sla_risk: true
    requires_action: "resolve_dependency"
```

### 2.4 Deal Stage Progression

```yaml
stages:
  - stage_id: 1
    stage_name: "Discovery"
    duration_days: 14
    documents_required: 8
    documents: ["NDA", "Confidential Information Form", "Executive Summary"]
    gate_criteria: "Mutual NDA signed + Confidential Info provided"
    next_stage: "Qualification"
    
  - stage_id: 2
    stage_name: "Qualification"
    duration_days: 21
    documents_required: 12
    documents: ["Team Overview", "Financial Summaries (Y-1, Y-2, TTM)", "Cap Table", "Customer List (Redacted)"]
    gate_criteria: "Financial review complete + team assessment done"
    next_stage: "Term Sheet"
    
  - stage_id: 3
    stage_name: "Term Sheet"
    duration_days: 10
    documents_required: 3
    documents: ["Term Sheet Draft", "Board Resolution (Company)", "Term Sheet Final (Signed)"]
    gate_criteria: "Term sheet signed by both parties"
    next_stage: "Diligence"
    
  - stage_id: 4
    stage_name: "Diligence"
    duration_days: 35
    documents_required: 35
    documents:
      - "Corporate Docs (Articles, Bylaws, Board Minutes)"
      - "IP Documentation (Patents, Trademarks, Copyrights)"
      - "Material Contracts (Customer, Vendor, Employment)"
      - "Litigation History & Insurance"
      - "Tax Returns (3 years)"
      - "Financial Audit Report"
      - "Employee List & Equity Schedules"
      - "Real Estate Deeds & Leases"
      - "Regulatory Compliance Certificates"
    gate_criteria: "All diligence items complete + no deal-breakers identified"
    next_stage: "Definitive"
    
  - stage_id: 5
    stage_name: "Definitive"
    duration_days: 21
    documents_required: 8
    documents:
      - "Purchase Agreement (Draft → Final)"
      - "Representations & Warranties Schedules"
      - "Closing Certificate"
      - "Officer Certificates"
      - "Legal Opinion Letter"
    gate_criteria: "Definitive agreement signed + all SLAs met"
    next_stage: "Closing"
    
  - stage_id: 6
    stage_name: "Closing"
    duration_days: 5
    documents_required: 6
    documents:
      - "Closing Statement"
      - "Wire Instructions (Verified)"
      - "Closing Certificates"
      - "Final Legal Opinion"
    gate_criteria: "Funds received + documents recorded"
    next_stage: "Post-Closing"
    
  - stage_id: 7
    stage_name: "Post-Closing"
    duration_days: 90
    documents_required: 5
    documents:
      - "100-Day Transition Plan"
      - "Milestone Check-ins (Monthly)"
      - "Integration Report"
    gate_criteria: "Ongoing performance tracking"
    next_stage: null
```

---

## 3. DEAL ENTITY EXAMPLES (5 Operating Ventures)

### Deal 1: CON-001 (Ace Construction) — Acquisition

```yaml
deal_id: "CON-001-ACQ-2026-09"
venture_id: "CON-001"
venture_name: "Ace Construction"
sector: "SEC-009-Construction"

deal_type: "Acquisition"
counterparty_name: "Vertex Capital Partners"
counterparty_type: "Private Equity"
deal_size: "$5.2M"
deal_currency: "USD"

initiated_date: "2026-09-01"
target_close_date: "2026-12-31"
current_stage: "Diligence"
stage_start_date: "2026-09-10"
stage_end_date: "2026-10-15"

progress_pct: 64
documents_complete: 23
documents_required: 36
status_direction: "On Track"

lead_counsel:
  name: "Jane Smith"
  firm: "Acme Legal LLP"
  email: "jsmith@acmeLegal.com"

lead_facilitator:
  name: "Marcus Chen"
  role: "CEO, CON-001"

key_blockers: []
at_risk_documents:
  - "Material Customer Contracts (Redline in progress)"
days_in_stage: 5
days_until_stage_deadline: 37

document_breakdown:
  Completed: 23
  In Review: 8
  In Preparation: 3
  Awaiting Signature: 2
  Not Started: 0
  Blocked: 0
```

### Deal 2: OPS-001 (Staffing) — Growth Capital

```yaml
deal_id: "OPS-001-GRO-2026-09"
venture_id: "OPS-001"
venture_name: "Operations One Staffing"
sector: "SEC-013-Staffing-and-HR"

deal_type: "Growth Capital"
counterparty_name: "Catalyst Venture Partners"
counterparty_type: "VC Fund (Series A)"
deal_size: "$3.5M"
deal_currency: "USD"

initiated_date: "2026-08-15"
target_close_date: "2026-11-30"
current_stage: "Qualification"
stage_start_date: "2026-09-05"
stage_end_date: "2026-09-26"

progress_pct: 58
documents_complete: 7
documents_required: 12
status_direction: "At Risk"

lead_counsel:
  name: "Robert Kim"
  firm: "Tech Legal Associates"
  email: "rkim@techlegal.com"

lead_facilitator:
  name: "Sarah Johnson"
  role: "Founder & CEO, OPS-001"

key_blockers:
  - "Cap Table: Need updated equity schedule from 2026-Q2 option grants"
  - "Financial Summary: Waiting on June YTD reconciliation from accounting"

at_risk_documents:
  - "Customer References (Only 3 of 5 provided)"
  - "Team Bios (CFO on vacation, can't finalize signature)"

days_in_stage: 4
days_until_stage_deadline: 17

document_breakdown:
  Completed: 7
  In Review: 2
  In Preparation: 2
  Awaiting Signature: 1
  Not Started: 0
  Blocked: 1  # Cap Table (blocked on accounting)
```

### Deal 3: LT-005 (Logistics) — Financing

```yaml
deal_id: "LT-005-FIN-2026-10"
venture_id: "LT-005"
venture_name: "Last-Mile Logistics"
sector: "SEC-011-Logistics-and-Supply-Chain"

deal_type: "Financing"
counterparty_name: "CrossBorder Capital"
counterparty_type: "Debt/Credit Facility"
deal_size: "$8.0M (Credit Facility)"
deal_currency: "USD"

initiated_date: "2026-08-01"
target_close_date: "2026-11-15"
current_stage: "Term Sheet"
stage_start_date: "2026-09-05"
stage_end_date: "2026-09-15"

progress_pct: 100
documents_complete: 3
documents_required: 3
status_direction: "On Track"

lead_counsel:
  name: "Elena Rodriguez"
  firm: "Commercial Finance Legal"
  email: "erodriguez@commfinlaw.com"

lead_facilitator:
  name: "David Wong"
  role: "CFO, LT-005"

key_blockers: []
at_risk_documents: []

days_in_stage: 4
days_until_stage_deadline: 6

document_breakdown:
  Completed: 3
  In Review: 0
  In Preparation: 0
  Awaiting Signature: 0
  Not Started: 0
  Blocked: 0

# Next milestone: Enter Diligence on 2026-09-16
next_milestone: "Begin 30-day financial audit (Diligence stage)"
```

### Deal 4: LT-011 (Logistics) — Strategic Partnership

```yaml
deal_id: "LT-011-PART-2026-09"
venture_id: "LT-011"
venture_name: "Logistics Tech Innovations"
sector: "SEC-011-Logistics-and-Supply-Chain"

deal_type: "Partnership"
counterparty_name: "Global Freight Alliance"
counterparty_type: "Strategic Partner"
deal_size: "Revenue Share (Est. $1.2M Year 1)"
deal_currency: "USD"

initiated_date: "2026-09-02"
target_close_date: "2026-10-31"
current_stage: "Discovery"
stage_start_date: "2026-09-02"
stage_end_date: "2026-09-16"

progress_pct: 37
documents_complete: 3
documents_required: 8
status_direction: "Accelerating"

lead_counsel:
  name: "Thomas Park"
  role: "General Counsel, LT-011"
  email: "tpark@logtech.com"

lead_facilitator:
  name: "Lisa Chen"
  role: "Founder, LT-011"

key_blockers: []
at_risk_documents:
  - "Executive Summary (Draft ready, needs CEO review)"

days_in_stage: 7
days_until_stage_deadline: 9

document_breakdown:
  Completed: 3
  In Review: 2
  In Preparation: 2
  Awaiting Signature: 1
  Not Started: 0
  Blocked: 0

# Fast-tracked due to strategic urgency
expedited_timeline: true
expedited_reason: "Partner has January product launch dependency"
```

### Deal 5: RE-001 (Real Estate) — Development Financing

```yaml
deal_id: "RE-001-DEV-2026-09"
venture_id: "RE-001"
venture_name: "Real Estate Development Corp"
sector: "SEC-035-Real-Estate-Development"

deal_type: "Financing"
counterparty_name: "Apex Real Estate Capital"
counterparty_type: "Commercial Real Estate Lender"
deal_size: "$12.5M"
deal_currency: "USD"

initiated_date: "2026-07-15"
target_close_date: "2026-12-15"
current_stage: "Diligence"
stage_start_date: "2026-09-01"
stage_end_date: "2026-10-05"

progress_pct: 71
documents_complete: 25
documents_required: 35
status_direction: "On Track"

lead_counsel:
  name: "William Martinez"
  firm: "Real Estate & Land Law"
  email: "wmartinez@relaw.com"

lead_facilitator:
  name: "Angela Reeves"
  role: "CEO, RE-001"

key_blockers: []
at_risk_documents:
  - "Environmental Phase I (Pending wetlands assessment — contractor delay)"

days_in_stage: 8
days_until_stage_deadline: 27

document_breakdown:
  Completed: 25
  In Review: 6
  In Preparation: 3
  Awaiting Signature: 1
  Not Started: 0
  Blocked: 0

# Real estate-specific docs
real_estate_specific:
  - "Survey (Current)"
  - "Phase I Environmental Report"
  - "Phase II Environmental Report (in progress)"
  - "Zoning & Land Use Compliance"
  - "Title Insurance Commitment"
  - "Existing Encumbrances Schedule"
```

---

## 4. DASHBOARD VIEWS & QUERIES

### 4.1 Portfolio Overview (Card View)

**Layout:** 5 cards (one per deal), shown at a glance

```
┌─ CON-001: Ace Construction ────────────────────────┐
│ Stage: Diligence (5d in / 37d remaining)            │
│ Progress: ████████░░ 64% (23/36 docs done)         │
│ Status: ✅ On Track                                │
│ Next Gate: "All diligence items complete"           │
│ At Risk: 1 document (Material Customer Contracts)   │
│ Lead Counsel: Jane Smith                            │
└────────────────────────────────────────────────────┘

┌─ OPS-001: Staffing (Series A) ─────────────────────┐
│ Stage: Qualification (4d in / 17d remaining)        │
│ Progress: ██████░░░░ 58% (7/12 docs done)          │
│ Status: ⚠️ AT RISK                                 │
│ Blockers: 1 (Cap Table — accounting delay)          │
│ At Risk: 2 documents (Cap Table, Customer Refs)     │
│ Lead Counsel: Robert Kim                            │
└────────────────────────────────────────────────────┘

┌─ LT-005: Last-Mile Logistics ──────────────────────┐
│ Stage: Term Sheet (4d in / 6d remaining)            │
│ Progress: ██████████ 100% (3/3 docs done)          │
│ Status: ✅ On Track (Ready to advance)              │
│ Next Milestone: Enter Diligence on 2026-09-16       │
│ Lead Counsel: Elena Rodriguez                       │
└────────────────────────────────────────────────────┘

┌─ LT-011: Logistics Tech (Partnership) ─────────────┐
│ Stage: Discovery (7d in / 9d remaining)             │
│ Progress: █████░░░░░ 37% (3/8 docs done)           │
│ Status: 🚀 Accelerating (expedited)                │
│ At Risk: 1 document (Exec Summary — pending CEO)    │
│ Lead Counsel: Thomas Park (internal)                │
└────────────────────────────────────────────────────┘

┌─ RE-001: Real Estate Development Financing ────────┐
│ Stage: Diligence (8d in / 27d remaining)            │
│ Progress: ███████░░░ 71% (25/35 docs done)         │
│ Status: ✅ On Track                                │
│ At Risk: 1 document (Phase I Env — contractor)      │
│ Lead Counsel: William Martinez                      │
└────────────────────────────────────────────────────┘

PORTFOLIO HEALTH: 4/5 On Track, 1/5 At Risk
CRITICAL ACTIONS: 2 items need leadership review
```

### 4.2 Timeline View (Gantt Chart)

```
STAGE TIMELINE (All Deals Overlaid)

Sep   ├─ Discovery         
      │  └─ LT-011 ════════════════ (2w)
      │  └─ CON-001 (behind) ════════════ (Moved from Aug)
      │
      ├─ Qualification
      │  └─ OPS-001 ════════════════ (3w, at risk: -5d)
      │
      ├─ Term Sheet
      │  └─ LT-005 ═════ (1w, ready to advance 09-16)
      │
Oct   ├─ Diligence
      │  └─ CON-001 ════════════════════════════ (5w)
      │  └─ RE-001 ════════════════════════════ (4w)
      │  └─ OPS-001 (queued, starts 09-26) ─→
      │
Nov   ├─ Definitive
      │  └─ CON-001 (queued) ─→
      │  └─ RE-001 (queued) ─→
      │  └─ OPS-001 (queued) ─→
      │
Dec   ├─ Closing
      │  └─ CON-001 (target: 12-31) ─→
      │  └─ OPS-001 (target: 11-30) ─→
      │
      ├─ Post-Closing
      │  └─ LT-005 (target: 11-15) ─→

KEY:
════ On schedule (green)
───  At risk — behind 5+ days (orange)
─→   Queued for future stage (gray)
```

### 4.3 Document Checklist View (by Venture)

**Query: "Show me all documents for CON-001, grouped by status"**

```
CON-001: ACE CONSTRUCTION — ACQUISITION DEAL
Target Close: 2026-12-31 | Deal Size: $5.2M | Lead Counsel: Jane Smith

═══════════════════════════════════════════════════════════════════════════

✅ COMPLETED (23 documents)
├─ 2026-09-01  NDA (Mutual)                     [SIGNED 2026-09-08]
├─ 2026-09-01  Confidential Information Form    [SIGNED 2026-09-05]
├─ 2026-09-03  Executive Summary                [SIGNED 2026-09-06]
├─ 2026-09-05  Financial Summary (2024)         [SIGNED 2026-09-08]
├─ 2026-09-05  Financial Summary (2025)         [SIGNED 2026-09-08]
├─ 2026-09-05  Financial Summary (TTM)          [SIGNED 2026-09-07]
├─ 2026-09-06  Team Overview Document           [SIGNED 2026-09-08]
├─ 2026-09-08  Organizational Structure Chart   [SIGNED 2026-09-08]
├─ 2026-09-08  Cap Table (Current)              [SIGNED 2026-09-08]
├─ 2026-09-05  Insurance Policies (Current)     [SIGNED 2026-09-07]
├─ 2026-09-06  Real Estate Deed                 [SIGNED 2026-09-06]
├─ 2026-09-07  Real Estate Lease (HQ)           [SIGNED 2026-09-07]
├─ 2026-09-08  Equipment Inventory List         [SIGNED 2026-09-08]
├─ 2026-09-05  Tax Return (2024)                [SIGNED 2026-09-05]
├─ 2026-09-05  Tax Return (2023)                [SIGNED 2026-09-05]
├─ 2026-09-05  Financial Audit Report (2024)    [SIGNED 2026-09-05]
├─ 2026-09-07  Employee List                    [SIGNED 2026-09-07]
├─ 2026-09-08  Equity Schedule                  [SIGNED 2026-09-08]
├─ 2026-09-03  Articles of Incorporation        [SIGNED 2026-09-03]
├─ 2026-09-03  Bylaws (Current)                 [SIGNED 2026-09-03]
├─ 2026-09-03  Board Meeting Minutes (YTD)      [SIGNED 2026-09-03]
├─ 2026-09-06  Litigation History Report        [SIGNED 2026-09-06]
└─ 2026-09-08  Certificate of Good Standing    [SIGNED 2026-09-08]

🔵 IN REVIEW (8 documents)
├─ 2026-09-05  Employee Agreements Template     [Counsel review: 3d pending]
├─ 2026-09-06  Customer List (Redacted)         [CFO review: 2d pending]
├─ 2026-09-07  Vendor Contracts (Summary)       [Counsel review: 1d pending]
├─ 2026-09-08  IP Documentation (Patents)       [Counsel review: 1d pending]
├─ 2026-09-08  IP Documentation (Trademarks)    [Counsel review: 1d pending]
├─ 2026-09-06  Material Customer Contracts      [Counsel redline: 5d OVERDUE]
├─ 2026-09-07  Material Vendor Contracts        [Counsel redline: 4d pending]
└─ 2026-09-08  Regulatory Compliance Certs      [Investor review: 1d pending]

🟡 IN PREPARATION (3 documents)
├─ 2026-09-08  Intellectual Property Licenses   [Being drafted: 50% complete]
├─ 2026-09-08  Customer References (Redacted)   [Being collected: 4 of 6 received]
└─ 2026-09-08  Competitive Analysis             [Being prepared: 30% complete]

⏳ AWAITING SIGNATURE (2 documents)
├─ 2026-09-08  Board Resolution (Company)       [Ready; Marcus Chen to sign]
└─ 2026-09-08  Term Sheet (Draft → Final)       [Ready; awaiting investor signature]

═══════════════════════════════════════════════════════════════════════════

BLOCKING DEPENDENCIES:
None currently blocking. One watch: "Material Customer Contracts" is 5 days overdue
in counsel review — if not complete by 2026-09-13, may impact Diligence gate (Sep 15).

UPCOMING MILESTONES:
• 2026-09-15: Diligence stage gate (all required docs must be complete)
• 2026-09-20: Legal review SLA (all counsel reviews must close)
• 2026-10-15: End of Diligence stage

RESPONSIBLE PARTIES:
• Jane Smith (Counsel): Employee Agreements, Contracts, IP, Regulatory review
• Marcus Chen (CEO): Board Resolution, Customer References
• Sarah Reeves (CFO): Financial documents, Customer List
```

### 4.4 At-Risk Dashboard (Executive View)

**Query: "Show me every document across all deals that is blocked or overdue"**

```
⚠️ AT-RISK DOCUMENTS ACROSS ALL DEALS (5 items requiring action)

1. ⏸️ OPS-001 — Cap Table (BLOCKED)
   Stage: Qualification | Due: 2026-09-15 | Overdue: 2 days
   Status: "Not Started" (waiting on predecessor)
   Blocked By: Q2 2026 equity option grant reconciliation from accounting
   Responsible: Sarah Johnson (CEO) → needs to push accounting
   Action: Call CFO to expedite equity schedule from June
   Consequence: Blocks Diligence entry (2026-09-26 now at risk)

2. ⏸️ OPS-001 — Customer References (IN PREPARATION)
   Stage: Qualification | Due: 2026-09-15 | Days Until Due: 7
   Status: 3 of 5 references provided
   Blocked By: (Contact issue) — Can't reach 2 tier-1 customers
   Responsible: Sarah Johnson (Founder)
   Action: Sarah to personally reach out by EOD 2026-09-09
   Risk Level: MEDIUM (can substitute with 2 backup refs if needed)

3. ⏳ CON-001 — Material Customer Contracts (IN REVIEW)
   Stage: Diligence | Due: 2026-09-15 | OVERDUE: 5 days
   Status: Counsel redline in progress
   Responsible: Jane Smith (Counsel) + Marcus Chen (CEO)
   Action: Jane to complete redline by EOD 2026-09-09; Marcus to respond 2026-09-10
   Risk Level: HIGH (controls 2 downstream docs: Definitive clause precedence)

4. ⏳ LT-011 — Executive Summary (IN REVIEW)
   Stage: Discovery | Due: 2026-09-15 | Days Until Due: 7
   Status: Draft ready, pending CEO review
   Responsible: Lisa Chen (Founder)
   Action: CEO review and sign off by 2026-09-10 (expedited deal)
   Risk Level: LOW (backup plan: use prior partner summary)

5. ⏳ RE-001 — Phase I Environmental Report (IN PREPARATION)
   Stage: Diligence | Due: 2026-09-30 | Days Until Due: 22
   Status: Pending wetlands assessment (contractor delay)
   Responsible: William Martinez (Counsel) + Angela Reeves (CEO)
   Action: Follow up with environmental contractor today; escalate if no ETA
   Risk Level: MEDIUM (Phase II depends on this; could delay Definitive by 10d)

═══════════════════════════════════════════════════════════════════════════

IMMEDIATE ACTIONS REQUIRED (This Week):
□ OPS-001: Sarah Johnson to call accounting re: equity schedule (2026-09-09)
□ OPS-001: Sarah Johnson to contact 2 missing customer references (2026-09-09)
□ CON-001: Jane Smith to complete Material Contracts redline (2026-09-09)
□ CON-001: Marcus Chen to respond to redlines (2026-09-10)
□ LT-011: Lisa Chen to review & sign Exec Summary (2026-09-10)
□ RE-001: William Martinez to follow up with environmental contractor (2026-09-08)

ESCALATION THRESHOLD:
If any item remains "In Review" for >7 days or "In Preparation" for >10 days,
escalate to CFO (David Wong) and General Counsel (Elena Rodriguez) for resolution.
```

### 4.5 Stage Readiness Query

**Query: "Which deals are ready to advance to the next stage?"**

```
DEAL STAGE READINESS ANALYSIS (2026-09-08)

✅ READY TO ADVANCE (1 deal)
├─ LT-005 (Last-Mile Logistics)
   Current Stage: Term Sheet | Progress: 100% (3/3 docs complete)
   Gate Criteria: "Term sheet signed by both parties" ✅ MET
   Approved By: Elena Rodriguez (Counsel)
   Ready Date: 2026-09-16
   Recommended Action: ENTER DILIGENCE STAGE
   Diligence Timeline: 35 days (estimated close by 2026-11-15)

🟡 CLOSE TO READY (1 deal — 5-7 days)
├─ CON-001 (Ace Construction)
   Current Stage: Diligence | Progress: 64% (23/36 docs complete)
   Gate Criteria: "All diligence items complete + no deal-breakers"
   Estimated Readiness: 2026-09-13 to 2026-09-15
   Watch Item: Material Customer Contracts (5d overdue in review)
   Recommended Action: MONITOR — Keep Materials Contracts on track

🟠 NOT READY (3 deals — 10+ days)
├─ OPS-001 (Operations One)
   Current Stage: Qualification | Progress: 58% (7/12 docs complete)
   Gate Criteria: "Financial review complete + team assessment done"
   Blocker: Cap Table (accounting delay — 2 days overdue)
   Estimated Readiness: 2026-09-20 to 2026-09-26 (14-21 days)
   Recommended Action: ESCALATE Cap Table blocker to CFO

├─ LT-011 (Logistics Tech)
   Current Stage: Discovery | Progress: 37% (3/8 docs complete)
   Gate Criteria: "Mutual NDA signed + Confidential Info provided"
   Status: Accelerated timeline (expedited for Jan partner deadline)
   Estimated Readiness: 2026-09-16 (8 days — on track)
   Recommended Action: MONITOR (exec summary pending CEO sign)

├─ RE-001 (Real Estate Development)
   Current Stage: Diligence | Progress: 71% (25/35 docs complete)
   Gate Criteria: "All diligence items complete + no deal-breakers"
   Blocker: Phase I Environmental (contractor delay — 22d until due)
   Estimated Readiness: 2026-09-25 to 2026-10-05 (17-27 days)
   Recommended Action: MONITOR (environmental on pace; Phase II pending)
```

---

## 5. INTEGRATION POINTS

### 5.1 ClickUp (CP-033) Integration

Each document status change triggers a ClickUp task:

```yaml
when:
  - Document status changes from "Not Started" → "In Preparation"
    then: Create ClickUp task "Draft [doc_name]"
    assigned_to: document_assigned_to
    due_date: document.due_date
    custom_fields:
      - deal_id: "CON-001-ACQ-2026"
      - doc_type: "NDA"
      - stage: "Discovery"
      - priority: "High" # if overdue or blocking

  - Document status changes to "In Review"
    then: Create/update ClickUp task "Review [doc_name]"
    assigned_to: reviewer (counsel/CFO/investor)
    due_date: document.due_date
    custom_fields:
      - review_type: "Legal" | "Financial" | "Investor"
      - signer_count: document.signer_count
      - pending_signers: document.pending_signers

  - Document status changes to "Awaiting Signature"
    then: Create ClickUp task "Sign [doc_name]"
    assigned_to: signer
    due_date: document.due_date - 2 days (reminder buffer)
    custom_fields:
      - signature_type: "Digital" | "Manual"
      - counterparty: deal.counterparty_name

  - Document status changes to "Completed"
    then: Update ClickUp task to "Completed"
    add_note: "Signed [date] by [signers]. Uploaded to [file_path]."
    trigger_dependent_docs: Check if any documents have this doc as a dependency
      and automatically create follow-up tasks
```

### 5.2 Neo4j Knowledge Graph (CP-013)

Each deal and document are nodes in the knowledge graph:

```yaml
nodes:
  Deal:
    properties: [deal_id, venture_id, counterparty_name, deal_size, stage, progress_pct]
    relationships:
      - OWNS_DOCUMENT → Document
      - INVOLVES_PARTY → Counterparty
      - RELATES_TO_VENTURE → Venture
      - REQUIRES_APPROVAL_FROM → Person

  Document:
    properties: [doc_id, doc_type, status, signed_date, due_date]
    relationships:
      - PART_OF_DEAL → Deal
      - BLOCKS → Document (dependency)
      - REQUIRES_REVIEW_BY → Person (counsel, CFO, investor)
      - SIGNED_BY → Person

  Stage:
    properties: [stage_name, duration_days, documents_required, gate_criteria]
    relationships:
      - CONTAINS_DOCUMENT → Document
      - PRECEDES_STAGE → Stage

queries_supported:
  - "Show me all deals in Diligence stage"
  - "Find all documents blocking CON-001"
  - "List all documents assigned to Jane Smith"
  - "Show me all deals with a CFO_APPROVAL blocker"
  - "Which deals have >20% documents overdue?"
```

### 5.3 Venture OS Document Registry

The dashboard sources from the 22-domain INSTITUTIONAL ARCHITECTURE:

```yaml
document_sources:
  CON-001:
    domain_01_identity: "BUSINESS-CAPITAL-DATA-ROOM/CON-001/01_IDENTITY/"
    domain_02_legal: "BUSINESS-CAPITAL-DATA-ROOM/CON-001/02_LEGAL/"
    domain_03_financial: "BUSINESS-CAPITAL-DATA-ROOM/CON-001/03_FINANCIAL/"
    domain_04_cap_table: "BUSINESS-CAPITAL-DATA-ROOM/CON-001/04_CAP_TABLE/"
    domain_05_intellectual_property: "BUSINESS-CAPITAL-DATA-ROOM/CON-001/05_IP/"
    domain_06_material_contracts: "BUSINESS-CAPITAL-DATA-ROOM/CON-001/06_MATERIAL_CONTRACTS/"
    # ... 22 total domains
    
  # Same structure for OPS-001, LT-005, LT-011, RE-001
```

---

## 6. QUERYABLE VIEWS (Sample Queries)

### Query 1: "What's my highest-risk item right now?"

```
Answer: OPS-001 Cap Table (BLOCKED, 2 days overdue)
Status: Blocked on Q2 equity schedule from accounting
Impact: Blocks Qualification → Diligence transition (scheduled 2026-09-26)
Action: Sarah Johnson to call CFO within 24 hours
```

### Query 2: "Which deals close this quarter?"

```
Q4 2026 Close Targets:
- CON-001: 2026-12-31 (90 days away) — Stage: Diligence (35d) → Definitive (21d) → Closing (5d)
- OPS-001: 2026-11-30 (83 days away) — Stage: Qualification (17d) → Term Sheet (10d) → Diligence (35d) → Definitive (21d)
- LT-005: 2026-11-15 (68 days away) — Stage: Diligence (35d) — READY TO ENTER 2026-09-16
- RE-001: 2026-12-15 (98 days away) — Stage: Diligence (27d) → Definitive (21d) → Closing (5d)
- LT-011: 2026-10-31 (53 days away) — Stage: Term Sheet (10d) → Diligence (35d)
```

### Query 3: "Which documents are Jane Smith responsible for?"

```
Jane Smith (Counsel, Acme Legal LLP) — 18 assigned documents across CON-001:

Completed:
- Articles of Incorporation ✅ (signed 2026-09-03)
- Bylaws ✅ (signed 2026-09-03)
- Board Minutes ✅ (signed 2026-09-03)
- NDA ✅ (signed 2026-09-08)

In Review (Overdue):
- Material Customer Contracts 🔴 (5 days overdue) — ESCALATE

In Review:
- Employee Agreements (3 days)
- Vendor Contracts (1 day)
- IP Documentation (1 day)

In Preparation:
- Intellectual Property Licenses (50% done)

Action: Prioritize Material Contracts redline by EOD 2026-09-09
```

### Query 4: "Show me all documents due in the next 7 days"

```
DOCUMENTS DUE IN NEXT 7 DAYS (2026-09-08 to 2026-09-15)

OVERDUE:
• CON-001 | Material Customer Contracts | Review | 5 days overdue | Jane Smith (Counsel)

DUE TODAY (2026-09-08):
• OPS-001 | Customer References | In Prep | Due today | Sarah Johnson

DUE BY 2026-09-09:
• OPS-001 | Cap Table | Blocked | Due 2026-09-09 | Sarah Johnson (via accounting)

DUE BY 2026-09-10:
• RE-001 | Phase I Environmental | In Prep | Due 2026-09-10 | William Martinez
• LT-011 | Executive Summary | In Review | Due 2026-09-10 | Lisa Chen

DUE BY 2026-09-13:
• CON-001 | Employee Agreements | In Review | Due 2026-09-13 | Jane Smith

DUE BY 2026-09-15:
• (End of current stage gate deadlines for Qualification/Discovery)
  - OPS-001: All Qualification docs must be complete by 2026-09-26
  - LT-011: All Discovery docs must be complete by 2026-09-16

TOTAL DOCUMENTS AT RISK: 5 items (shown in "At-Risk Dashboard" section above)
```

### Query 5: "What's the status of the deals I'm monitoring today?"

```
DAILY STANDUP — 2026-09-08 (Friday EOD)

STARTS TODAY:
• LT-011 enters week 2 of Discovery stage (7/14 days used)

CRITICAL ESCALATIONS NEEDED:
⏸️ OPS-001 Cap Table — 2 days OVERDUE (accounting delay)
🔴 CON-001 Material Contracts — 5 days OVERDUE (counsel review)

ON TRACK:
✅ CON-001 Diligence (23/36 docs done, due Sep 15)
✅ RE-001 Diligence (25/35 docs done, due Oct 5)
✅ LT-005 Term Sheet (3/3 docs done, ready to advance Sep 16)

WATCH ITEMS (Next 7 Days):
⏳ OPS-001 Customer References (3/5 needed by Sep 15)
⏳ LT-011 Exec Summary (needs CEO signature by Sep 10)
⏳ RE-001 Phase I Environmental (awaiting contractor by Sep 10)

DECISIONS NEEDED:
→ Approve LT-005 entry into Diligence stage (recommendation: YES, all gates met)
→ Escalate OPS-001 Cap Table blocker (recommendation: CEO call to accounting CFO)
→ Consider expedited path for LT-011 (Jan product launch deadline)

NEXT REVIEW: Monday 2026-09-11 EOD
```

---

## 7. IMPLEMENTATION NOTES

### 7.1 Data Storage

**Primary Source:** `_REGISTRIES/CANONICAL/DEAL_STATUS_REGISTRY.yaml`
- 5 deal entities (CON-001, OPS-001, LT-005, LT-011, RE-001)
- ~200 document records
- Updated when: Document status changes OR user edits ClickUp task

**Sync Mechanism:** ClickUp ↔ YAML registry
- Trigger: ClickUp API webhook (on task status change)
- Action: Parse ClickUp task → update YAML deal/document record
- Frequency: Real-time (webhook → Lambda → update YAML)
- Fallback: Manual sync via `cb deals sync` CLI command

**Audit Trail:**
- `deal_id`, `updated_date`, `updated_by`, `change_description`
- Full change history stored in Neo4j (linked to Deal node)

### 7.2 Blocking & Dependency Logic

```
When a document status changes:
1. Check if any OTHER documents have this document in their "depends_on" list
2. If this document is now "Completed":
   - Mark all dependent documents as "unblocked"
   - Trigger automatic task creation for downstream docs
3. If this document becomes "Blocked":
   - Mark all dependent documents as "blocked"
   - Notify owners of blocked documents
4. If this document is >N days overdue:
   - Flag as "At Risk"
   - Escalate to counsel/CFO (based on document type)
```

### 7.3 SLA Definitions

```yaml
sla_tiers:
  High:
    - doc_types: [Term Sheet, Definitive Agreement, Closing Certificate]
    - escalation_threshold_days: 3  # Escalate if >3 days overdue
    - escalation_to: [CEO, General Counsel, CFO]
    
  Medium:
    - doc_types: [Material Contracts, Financial Docs, IP Documentation]
    - escalation_threshold_days: 5
    - escalation_to: [Counsel, CFO]
    
  Low:
    - doc_types: [Reference Lists, Team Bios, Market Analysis]
    - escalation_threshold_days: 7
    - escalation_to: [Assigned Owner]
```

### 7.4 Dashboard Refresh Cadence

```
Real-Time:
• Document status changes (ClickUp → YAML)
• Blocking/unblocking of dependent docs

Hourly:
• SLA compliance checks (documents approaching due date)
• At-Risk flagging

Daily (9 AM):
• Executive summary email (portfolio health, blockers)
• Stage readiness analysis

Weekly (Monday 9 AM):
• Full portfolio review
• Deal pacing analysis (are we on track to close date?)
• Forecast next week's critical dates
```

---

## 8. CONTROL PLANES & OWNERS

| Control Plane | Owner | Role | Deal Oversight |
|---|---|---|---|
| **CP-026** (Financial) | David Wong (CFO, LT-005) | Financial review, CFO approvals | All 5 deals |
| **CP-031** (Intelligence/Counsel) | Jane Smith / Elena Rodriguez | Legal review, doc strategy | CON-001, LT-005 leads |
| **CP-033** (Execution/ClickUp) | Sarah Johnson (OPS-001 CEO) | Task orchestration, tracking | All 5 deals |
| **CP-034** (Engineering/Admin) | Marcus Chen (CON-001 CEO) | Document storage, filing | Document repository |

---

**Schema Version:** 1.0  
**Last Revised:** 2026-09-08  
**Next Review:** 2026-09-15 (When first deal advances to next stage)  
**Authority:** CP-026 (Financial) + CP-033 (Execution)
