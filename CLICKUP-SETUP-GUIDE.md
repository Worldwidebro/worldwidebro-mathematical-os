# ClickUp Structure Setup Guide
**Date:** 2026-05-09  
**Status:** Ready for manual implementation in ClickUp UI

---

## Overview
This guide provides the complete list structure, custom fields, and task templates needed to set up ClickUp as the execution layer for your orchestration system. All structures are designed to sync with Supabase positions, contracts, and revenue tracking.

---

## PART 1: WORKSPACE & FOLDER STRUCTURE

### Create This Hierarchy in ClickUp:

```
Worldwidebro Holdings (Workspace)
├── Company Operations (Folder)
├── Sales & Negotiation (Folder)
├── Execution by Sector (Folder with 16 sub-folders)
├── Project Management (Folder)
└── Financial (Folder)
```

---

## PART 2: FOLDER 1 — COMPANY OPERATIONS

**Lists to Create:**

### 1.1 Positions & Authority
**Purpose:** Track all 29 positions, reporting structure, authority levels, approval thresholds

**Status Fields:** Active, Inactive, Vacant

**Custom Fields:**
- Position Code (text)
- Position Type (dropdown: Human, Agent, Hybrid)
- Department (dropdown: Executive, Operations, Sales, Finance)
- Authority Level (number: 1-10)
- Approval Threshold ($) (currency)
- Reports To (link to Position)
- Sector Coverage (text, comma-separated)

**Key Tasks:**
- [ ] CEO / Founder (POS-CEO-001)
- [ ] COO / Operations (POS-COO-001)
- [ ] CFO / Finance (POS-CFO-001)
- [ ] Head of Sales (POS-SALES-HEAD-001)
- [ ] Beauty & Wellness Manager (POS-BEAUTY-MANAGER)
- [ ] Tech & Software Manager (POS-TECH-MANAGER)
- [ ] Construction PM (POS-CONSTRUCTION-PM)
- [ ] Finance Manager (POS-FINANCE-MANAGER)
- [ ] Vendor Manager (POS-VENDOR-MANAGER)
- [ ] Senior Sales Rep (POS-SALES-REP-SENIOR)
- [ ] Sales Rep (POS-SALES-REP-002)
- [ ] Subcontractor Liaison (POS-SUBCONTRACTOR-LIAISON)
- [ ] Accountant (POS-ACCOUNTANT)
- [ ] 16 AI Agents (qwen-beauty, qwen-tech, qwen-construction, etc.)

---

### 1.2 Vendors / Affiliates
**Purpose:** Manage affiliate network (contractors, agencies, freelancers, staffing partners)

**Status Fields:** Prospect, Qualified, Active, On Hold, Terminated

**Custom Fields:**
- Vendor Code (text)
- Vendor Type (dropdown: Contractor, Agency, Freelancer, Staffing)
- Specialization (text)
- Location (text)
- Contact Name (text)
- Email (email)
- Phone (phone)
- Capacity (number: units available)
- Reliability Score (rating: 0-5)
- Insurance Status (dropdown: Active, Expired, None)
- Affiliation Agreement (checkbox)
- MSA Signed Date (date)

**Key Tasks (Examples):**
- [ ] Elite Electric (electricians, reliability: 94/100, capacity: 3)
- [ ] Phoenix PM Group (project management, capacity: 5)
- [ ] Premium Staffing (temporary workforce)

---

### 1.3 Clients / Accounts
**Purpose:** Track all client relationships, decision makers, pain points, budget

**Status Fields:** Prospect, Qualified, Active, Inactive, Lost

**Custom Fields:**
- Client Code (text)
- Industry (text)
- Company Size (dropdown: Solo, 2-10, 11-50, 51-200, 200+)
- Location (text)
- Primary Contact (text)
- Email (email)
- Phone (phone)
- Pain Point (text)
- Budget Range (text: e.g., "$50K-100K/year")
- Lead Source (dropdown: Network, Social, Cold, Referral)
- Lead Quality (dropdown: Hot, Warm, Cold)
- Last Contact Date (date)

---

### 1.4 Contracts
**Purpose:** Track all MSAs, work orders, vendor agreements, SLAs

**Status Fields:** Draft, Negotiating, Signed, Active, Completed, Terminated

**Custom Fields:**
- Contract Code (text)
- Contract Type (dropdown: MSA, Work Order, Vendor Agreement, Subcontractor, SLA)
- Related Venture (link)
- Related Client (link)
- Related Vendor (link)
- Start Date (date)
- End Date (date)
- Value ($) (currency)
- Payment Terms (dropdown: Upfront, Milestone, Net-30, Net-60)
- Document URL (URL field)
- Signed By (link to Position)

---

## PART 3: FOLDER 2 — SALES & NEGOTIATION

### 2.1 Leads
**Purpose:** Track all new prospects from network, social, referral

**Status Fields:**
- New Lead (default start)
- Contacted
- Interested
- Qualified
- Negotiating
- Closed
- Lost

**Custom Fields:**
- Lead Code (text: LEAD-2026-0001)
- Client Name (text)
- Contact Email (email)
- Contact Phone (phone)
- Industry (text)
- Venture Match (link to venture)
- Pain Point (text)
- Budget Range (text)
- Lead Quality (dropdown: Hot, Warm, Cold)
- Source (dropdown: Network, Social, Referral, Cold)
- Assigned To (link to Position)

**Workflow:**
1. Create task when new lead found
2. Move to "Contacted" after first outreach
3. Move to "Interested" when they respond positively
4. Move to "Qualified" after initial call confirms fit
5. Transition to Negotiations list when discovery shows real interest

---

### 2.2 Discoveries
**Purpose:** Track scheduled calls, needs assessment, qualification depth

**Status Fields:**
- Scheduled
- Completed
- Follow-up Needed
- Qualified
- Not Qualified

**Custom Fields:**
- Lead Code (link to Leads)
- Call Date (date)
- Call Time (time)
- Contact Name (text)
- Phone (phone)
- Time Zone (text)
- Pain Points Documented (text)
- Budget Confirmed (currency)
- Timeline (text: e.g., "3-month implementation")
- Next Action (text)
- Notes (text area)

---

### 2.3 Negotiations
**Purpose:** Track active deals, pricing discussions, contract negotiation

**Status Fields:**
- Proposal Sent
- Awaiting Feedback
- Negotiating Terms
- Ready to Close
- Closed (moved to Closed Deals)

**Custom Fields:**
- Deal Code (text: DEAL-2026-0001)
- Lead Code (link)
- Client Name (text)
- Venture (link)
- Proposed Value ($) (currency)
- Proposed Timeline (text)
- Key Terms (text area)
- Objections (text area)
- Proposed Solution (text area)
- Close Probability (%) (number)
- Expected Close Date (date)
- Owner (link to Position)

---

### 2.4 Closed Deals
**Purpose:** Track completed sales, revenue recognition, post-close follow-up

**Status Fields:**
- Contract Signed
- Awaiting First Payment
- Revenue Recognized
- Active Relationship
- Upsell Opportunity

**Custom Fields:**
- Deal Code (text)
- Client Name (text)
- Venture (link)
- Final Value ($) (currency)
- Close Date (date)
- First Revenue Date (date)
- Contract URL (URL)
- Implementation Start (date)
- Monthly Recurring Revenue (currency, if applicable)
- Payment Terms (text)
- Account Manager (link to Position)
- Upsell Opportunities (text area)

---

## PART 4: FOLDER 3 — EXECUTION BY SECTOR

**Create 16 sub-folders, one per sector:**
1. Beauty & Wellness Sector
2. Technology Sector
3. Construction Sector
4. E-Commerce Sector
5. Financial Services Sector
6. Food & Hospitality Sector
7. Education Sector
8. Media & Content Sector
9. Fitness & Sports Sector
10. Logistics & Transport Sector
11. Professional Services Sector
12. Software & Tech Sector
13. Specialized Services Sector
14. Emerging Ventures Sector
15. Community Sector
16. Operations Sector

**In EACH sector folder, create these 3 lists:**

### [Sector] Operations
**Purpose:** Track ventures in this sector, active projects, health status

**Status Fields:** Planning, Active, Delayed, Completed, On Hold

**Custom Fields:**
- Venture Code (text: BW-001, TECH-042, etc.)
- Product Name (text)
- Stage (dropdown: Pre-launch, MVP, Scaling, Mature)
- Sector Manager (link to Position)
- Active Projects (number)
- Last Update (date)
- Current Focus (text)

---

### [Sector] Vendors
**Purpose:** Track which vendors/contractors are assigned to this sector

**Status Fields:** Prospect, Qualified, Active, On Hold, Terminated

**Custom Fields:**
- Vendor Name (text)
- Vendor Type (dropdown: Contractor, Agency, Freelancer, Staffing)
- Specialization (text)
- Assigned To Ventures (text)
- Capacity Available (number)
- Reliability Score (rating 0-5)
- Last Project (text)
- Next Available (date)

---

### [Sector] Revenue
**Purpose:** Track MRR, revenue targets, stripe product IDs, monthly revenue

**Status Fields:** Active, Planning, Paused, Archived

**Custom Fields:**
- Month (text: e.g., "May 2026")
- MRR Target ($) (currency)
- MRR Actual ($) (currency)
- % of Target (%) (number)
- Ventures Generating Revenue (number)
- Stripe Product IDs (text)
- Payment Methods (text)
- Outstanding Invoices ($) (currency)
- Notes (text area)

---

## PART 5: FOLDER 4 — PROJECT MANAGEMENT

### 4.1 Active Projects
**Purpose:** Track all in-flight client projects (multi-vendor, multi-phase)

**Status Fields:** Planning, Procuring, In Progress, Delayed, Completed, Closed

**Custom Fields:**
- Project Code (text: PRJ-2026-0001)
- Client Name (text)
- Venture (link)
- Project Name (text)
- Scope (text area)
- Start Date (date)
- Target End Date (date)
- Budget ($) (currency)
- Spent to Date ($) (currency)
- % Complete (number)
- Primary PM (link to Position)
- Vendors Assigned (text: comma-separated)
- Risk Level (dropdown: Low, Medium, High)

---

### 4.2 Work Orders
**Purpose:** Track individual vendor work units (granular execution units)

**Status Fields:** Assigned, In Progress, Delayed, Completed, Paid, Disputed

**Custom Fields:**
- Work Order #  (text: WO-2026-0001)
- Project (link to Active Projects)
- Client (link to Client)
- Vendor Assigned (link to Vendor)
- Scope (text area)
- Deliverables (text area)
- Start Date (date)
- End Date (date)
- Price ($) (currency)
- Cost ($) (currency)
- Margin ($) (currency = Price - Cost)
- % Complete (number)
- Quality Approval (dropdown: Not Started, In Review, Approved, Issues)
- Payment Status (dropdown: Not Started, Sent, Received, Disputed)

---

### 4.3 Procurement
**Purpose:** Track vendor selection, RFQs, purchase orders for specific projects

**Status Fields:** RFQ Sent, Quotes Received, Negotiating, PO Issued, Completed

**Custom Fields:**
- Procurement Code (text)
- Project (link)
- Services/Goods Needed (text)
- Estimated Budget ($) (currency)
- Vendors Contacted (number)
- Quotes Received (number)
- Lowest Quote ($) (currency)
- Selected Vendor (link to Vendor)
- PO Date (date)
- Expected Delivery (date)
- Notes (text area)

---

### 4.4 Quality & Compliance
**Purpose:** Track inspections, safety checks, permit status, compliance requirements

**Status Fields:** Pending, In Progress, Approved, Issues Found, Resolved, Archived

**Custom Fields:**
- Inspection Type (dropdown: Quality, Safety, Permit, Compliance, Insurance)
- Related Project (link)
- Related Vendor (link)
- Inspector Name (text)
- Inspection Date (date)
- Findings (text area)
- Issues Found (number)
- Resolution Required (text area)
- Resolution Date (date)
- Sign-Off By (link to Position)

---

## PART 6: FOLDER 5 — FINANCIAL

### 5.1 Invoicing
**Purpose:** Track all invoices issued to clients from work orders

**Status Fields:** Draft, Sent, Viewed, Partially Paid, Paid, Overdue, Disputed

**Custom Fields:**
- Invoice # (text: INV-2026-0001)
- Client (link to Client)
- Related Work Order (link)
- Invoice Date (date)
- Due Date (date)
- Amount ($) (currency)
- Description (text area)
- Payment Method (dropdown: Bank Transfer, Card, Check, ACH)
- Payment Received Date (date)
- Days Overdue (number, auto-calculated if overdue)

---

### 5.2 Vendor Payables
**Purpose:** Track what you owe vendors based on work completed

**Status Fields:** Not Started, Submitted, Approved, Processing, Paid, Disputed

**Custom Fields:**
- Payable Code (text)
- Vendor (link)
- Related Work Order (link)
- Invoice from Vendor (text)
- Amount Owed ($) (currency)
- Milestone (if milestone-based)
- % Complete (number)
- Approved For Payment (checkbox)
- Payment Date (date)
- Payment Method (dropdown)
- Notes (text area)

---

### 5.3 Cash Flow
**Purpose:** Weekly/monthly cash position projection and actual tracking

**Status Fields:** Projected, Actual, Variance Analysis

**Custom Fields:**
- Period (text: e.g., "Week of May 9")
- Projected Revenue In ($) (currency)
- Actual Revenue In ($) (currency)
- Projected Vendor Payables Out ($) (currency)
- Actual Vendor Payables Out ($) (currency)
- Net Cash Position ($) (currency)
- Outstanding Invoices ($) (currency)
- Outstanding Payables ($) (currency)
- Forecast for Next 30 Days ($) (currency)
- Notes (text area)

---

### 5.4 Monthly Close
**Purpose:** End-of-month financial summary by sector and venture

**Status Fields:** In Progress, Ready for Review, Reviewed, Closed, Archived

**Custom Fields:**
- Month (text: e.g., "May 2026")
- Sector (link to sector)
- Total Revenue ($) (currency)
- Total Cost of Goods/Services ($) (currency)
- Gross Margin ($) (currency)
- Margin % (%)
- Number of Active Ventures (number)
- Number of Closed Deals (number)
- Total Client Invoices (#) (number)
- Total Paid Invoices (#) (number)
- Outstanding AR ($) (currency)
- CFO Sign-Off (date)
- Notes (text area)

---

## PART 7: AUTOMATION & WORKFLOW SETUP

### Recommended Automations (Set in ClickUp UI):

1. **New Lead → Auto-assign to Sector Manager**
   - Trigger: Task created in "Leads" list
   - Action: Assign to sector-specific manager based on industry tag

2. **Discovery Call → Auto-create Negotiation Task**
   - Trigger: Task status = "Completed" in Discoveries
   - Condition: Lead Quality = "Qualified"
   - Action: Create task in Negotiations list, link original lead

3. **Work Order Completed → Auto-create Invoice**
   - Trigger: Work Order status = "Completed"
   - Action: Create task in Invoicing list, pull client + amount from WO

4. **Invoice Paid → Auto-mark Work Order as "Paid"**
   - Trigger: Invoice status = "Paid"
   - Condition: Match invoice to related work order
   - Action: Update work order status to "Paid"

5. **Vendor Payable Due → Auto-remind Finance Manager**
   - Trigger: 3 days before payable due date
   - Action: Reminder notification to Finance Manager

---

## PART 8: CUSTOM FIELD SUMMARY (Copy-Paste Ready)

### Global Custom Fields (Use across multiple lists):
- Position Code (text)
- Position Type (dropdown)
- Department (dropdown)
- Authority Level (number)
- Approval Threshold ($) (currency)
- Contract Code (text)
- Venture (link)
- Client Name (text)
- Contact Email (email)
- Contact Phone (phone)
- Vendor Name (text)
- Lead Code (text)
- Deal Code (text)
- Project Code (text)
- Work Order # (text)
- Invoice # (text)
- Amount ($) (currency)
- Status Tracker (dropdown)
- Assigned To (link to Position)
- Date Fields (start, end, due, completion, sign-off)

---

## PART 9: QUICK START CHECKLIST

- [ ] Create "Company Operations" folder with 4 lists
- [ ] Create "Sales & Negotiation" folder with 4 lists
- [ ] Create "Execution by Sector" folder with 16 sub-folders
- [ ] Create "Project Management" folder with 4 lists
- [ ] Create "Financial" folder with 4 lists
- [ ] Add all custom fields to relevant lists
- [ ] Create sample tasks in each list (3-5 examples)
- [ ] Set up 5 recommended automations
- [ ] Test workflow: New Lead → Discovery → Negotiation → Closed Deal
- [ ] Configure permissions by position level

---

## Status
**To Implement:** Create all folders, lists, custom fields, and automations in ClickUp UI.  
**Expected Time:** 2-3 hours to set up completely.  
**Next Step:** Once ClickUp is live, begin mapping existing contacts into Leads list and matching to ventures.

