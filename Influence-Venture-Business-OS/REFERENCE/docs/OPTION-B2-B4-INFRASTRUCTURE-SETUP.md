# OPTION B.2 → B.4: COMPLETE INFRASTRUCTURE SETUP
## Slack + ClickUp + HubSpot Configuration Guide
**Status:** Ready to Execute  
**Date:** 2026-06-10

---

## OPTION B.2: SLACK CHANNELS SETUP

### Overview
Create 3 Slack channels (one per venture) with webhooks for automation outputs

### Step 1: Create Slack Channels

**Channel 1: #ops-001-staffing**
```
Name: ops-001-staffing
Description: OPS-001 Venture Staffing—Daily matching, payroll, utilization
Visibility: Private
Members: You, ops manager, accountant

Posts (automated):
  - Daily 9 AM: Contractor-venture matches (5-10 new)
  - Daily 10 AM: Utilization dashboard
  - Friday 5 PM: Bi-weekly payroll summary
```

**Channel 2: #con-001-construction**
```
Name: con-001-construction
Description: CON-001 Ace Construction—Projects, bids, billing
Visibility: Private
Members: You, project manager, accountant

Posts (automated):
  - Daily 8 AM: New bid opportunities
  - Daily 4 PM: Project status updates
  - Friday 5 PM: Invoice & billing summary
```

**Channel 3: #re-001-property**
```
Name: re-001-property
Description: RE-001 Property Holdings—Rent, maintenance, expenses
Visibility: Private
Members: You, property manager, accountant

Posts (automated):
  - Monthly (1st): Rent collection status
  - Monthly (15th): Expense summary
  - As needed: Maintenance notifications
```

### Step 2: Create Slack Webhooks (for Loop Automation)

**Create Webhook for #ops-001-staffing:**

```
1. Go to https://api.slack.com/apps
2. Click "Create New App" → "From scratch"
3. App Name: "Loop Automation - Staffing"
4. Select your workspace
5. Go to "Incoming Webhooks" → Toggle "Activate"
6. Click "Add New Webhook to Workspace"
7. Select channel: #ops-001-staffing
8. Copy Webhook URL (looks like: https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXX)
9. Save in secure location (password manager)
```

**Repeat for #con-001-construction and #re-001-property**

### Step 3: Configure Channel Settings

For each channel:
```
1. Click channel name → Settings
2. Add topic: "[Venture Name] Operations"
3. Add description (copy from above)
4. Set notification policy: "@everyone" can post
5. Pin messages: Loop schedule, contact info, escalation process
6. Add emoji to channel name:
   - #ops-001-staffing → 👥
   - #con-001-construction → 🏗️
   - #re-001-property → 🏠
```

---

## OPTION B.3: CLICKUP WORKSPACE SETUP

### Overview
Create 3 workspaces with lists and custom fields for task management

### Workspace 1: OPS-001 Staffing Operations

**Create 4 Lists:**

```
List 1: Active Assignments
  Fields:
    - Contractor Name (text)
    - Venture (text)
    - Start Date (date)
    - End Date (date)
    - Expected Hours (number)
    - Hours Logged (number)
    - Status (select: active/completed/paused/cancelled)
    - Quality Score (0-100)

List 2: Pending Matches
  Fields:
    - Contractor Name (text)
    - Skills (text)
    - Venture Need (text)
    - Match Score (0-100)
    - Action (select: approve/reject/discuss)

List 3: Contractor Pipeline
  Fields:
    - Contractor Name (text)
    - Skills (text)
    - Status (select: prospect/screening/offer/onboarded)
    - Start Date (date)

List 4: Payroll Queue
  Fields:
    - Contractor Name (text)
    - Period (text: "Jun 1-14")
    - Hours (number)
    - Rate (currency)
    - Amount (currency)
    - Status (select: pending/approved/paid)
```

### Workspace 2: CON-001 Construction Operations

**Create 4 Lists:**

```
List 1: Active Projects
  Fields:
    - Project Name (text)
    - Client (text)
    - Budget (currency)
    - Spent (currency)
    - % Complete (0-100)
    - Timeline Start (date)
    - Timeline End (date)
    - Status (select: planning/in-progress/completed)

List 2: Opportunities/Bids
  Fields:
    - Project Name (text)
    - Source (select: SAM.gov/NCDOT/HomeAdvisor/Angi/Direct)
    - Estimated Budget (currency)
    - Match Score (0-100)
    - Deadline to Bid (date)
    - Status (select: new/bid-prepared/submitted/won/lost)

List 3: Subcontractor Schedule
  Fields:
    - Project (text)
    - Trade (select: roofing/electrical/plumbing/hvac/general)
    - Subcontractor (text)
    - Start Date (date)
    - End Date (date)
    - Status (select: scheduled/in-progress/completed)

List 4: Quality Issues
  Fields:
    - Project (text)
    - Issue (text)
    - Category (select: safety/budget/schedule/quality)
    - Priority (select: critical/high/medium/low)
    - Status (select: open/in-progress/resolved)
```

### Workspace 3: RE-001 Real Estate Operations

**Create 4 Lists:**

```
List 1: Properties
  Fields:
    - Address (text)
    - City (text)
    - Property Type (select: single-family/duplex/triplex)
    - Bedrooms (number)
    - Purchase Price (currency)
    - Current Value (currency)
    - Monthly Rent (currency)
    - Status (select: occupied/vacant/maintenance)

List 2: Tenant Management
  Fields:
    - Property (text)
    - Tenant Name (text)
    - Lease Start (date)
    - Lease End (date)
    - Monthly Rent (currency)
    - Status (select: active/notice-given/moving-out)

List 3: Maintenance Requests
  Fields:
    - Property (text)
    - Description (text)
    - Category (select: emergency/urgent/routine)
    - Estimated Cost (currency)
    - Actual Cost (currency)
    - Vendor (text)
    - Status (select: open/scheduled/in-progress/completed)

List 4: Capital Planning
  Fields:
    - Property (text)
    - Expense Type (select: roof/HVAC/plumbing/exterior)
    - Expected Cost (currency)
    - Planned Year (number)
    - Status (select: planning/budgeted/in-progress)
```

### Automations in ClickUp

**For OPS-001:**
```
- When match created → Automatically create task in "Pending Matches"
- When task moved to "Approved" → Move to "Active Assignments"
- Every Friday → Remind to review payroll queue
```

**For CON-001:**
```
- When opportunity marked "qualified" → Create bid preparation task
- 3 days before deadline → Send reminder
- When project 80% complete → Flag for closeout
```

**For RE-001:**
```
- Monthly (1st) → Create task "Collect Rent"
- Monthly (15th) → Create task "Pay Expenses"
- 60 days before lease end → Create renewal task
```

---

## OPTION B.4: HUBSPOT CONFIGURATION

### Overview
Set up HubSpot for deal/opportunity tracking

### Step 1: Create Custom Objects

**Custom Object: Placement (OPS-001)**

```
Name: Placement
Properties:
  - Contractor Name
  - Venture ID
  - Start Date
  - End Date
  - Expected Hours
  - Actual Hours
  - Quality Score
  - Status
  - Notes

Associations: Link to Contacts (contractors) and Companies (ventures)
```

**Custom Object: Bid (CON-001)**

```
Name: Bid
Properties:
  - Project Name
  - Client Name
  - Estimated Budget
  - Location
  - Source (SAM.gov, NCDOT, etc.)
  - Deadline
  - Match Score
  - Pipeline Stage
  - Notes

Associations: Link to Contacts (clients) and Companies
```

**Custom Object: Property (RE-001)**

```
Name: Property
Properties:
  - Address
  - City, State, Zip
  - Property Type
  - Bedrooms, Bathrooms
  - Purchase Price
  - Current Value
  - Monthly Income
  - Status
  - Notes

Associations: Link to Contacts (tenants)
```

### Step 2: Create Pipelines

**Pipeline: Placement (OPS-001)**
```
Stages:
  1. In Conversation
  2. Negotiating
  3. Placed
  4. Completed

Expected: Convert 60%+, timeline <30 days
```

**Pipeline: Bid (CON-001)**
```
Stages:
  1. Opportunity
  2. Bid Prepared
  3. Bid Submitted
  4. Won
  5. Lost
  6. No-Bid

Expected: Win 50%+, pipeline value $180K-$300K
```

**Pipeline: Lease (RE-001)**
```
Stages:
  1. Tenant Search
  2. Application Pending
  3. Approved
  4. Leasing
  5. Notice Given
  6. Vacant

Expected: Occupancy 95%+, time to fill <14 days
```

### Step 3: Set Up Workflows

**Workflow: Placement → Feedback**
```
Trigger: Placement moved to "Completed"
Actions:
  - Send feedback survey to contractor
  - Send feedback survey to venture
  - Log scores in Supabase
```

**Workflow: Bid → Project Creation**
```
Trigger: Bid moved to "Won"
Actions:
  - Create project task in ClickUp
  - Schedule kickoff meeting
  - Notify team in Slack
```

**Workflow: Lease → Rent Reminders**
```
Trigger: Lease in "Leasing" (monthly)
Actions:
  - 5 days before due: Send rent reminder
  - 15 days overdue: Create legal task
```

### Step 4: Create Dashboards

**Dashboard 1: OPS-001 Staffing**
```
Cards:
  - Pipeline breakdown (by stage)
  - Conversion rate
  - Active placements
  - Average duration
  - NPS trends
```

**Dashboard 2: CON-001 Bids**
```
Cards:
  - Opportunities in pipeline
  - Win rate
  - Pipeline value ($)
  - Time to bid (days)
  - Source breakdown
```

**Dashboard 3: RE-001 Properties**
```
Cards:
  - Portfolio value ($)
  - Occupancy %
  - Time to fill vacancy
  - Monthly income ($)
  - Upcoming lease renewals
```

---

## COMPLETION CHECKLIST

### B.1: Supabase SQL ✅
```
☐ Execute SQL file in Supabase
☐ Verify 19 tables created
☐ Verify indexes created
☐ Enable realtime publications
```

### B.2: Slack Channels ✅
```
☐ Create 3 channels
☐ Create 3 webhooks (save URLs)
☐ Configure channel settings
☐ Test webhooks with sample message
```

### B.3: ClickUp Workspaces ✅
```
☐ Create 3 workspaces
☐ Create 12 lists (4 per workspace)
☐ Add custom fields to each list
☐ Set up automations (12 total)
☐ Test with sample tasks
```

### B.4: HubSpot Configuration ✅
```
☐ Create 3 custom objects
☐ Create 3 pipelines
☐ Set up 4 workflows
☐ Create 3 dashboards
☐ Verify data flows correctly
```

---

## TIME ESTIMATE

| Task | Time |
|------|------|
| B.1 Supabase | 10 min |
| B.2 Slack | 30 min |
| B.3 ClickUp | 60 min |
| B.4 HubSpot | 60 min |
| Testing | 20 min |
| **TOTAL** | **3 hours** |

---

## YOU NOW HAVE

✅ **B.1:** Supabase SQL file (ready to execute)  
✅ **B.2:** Slack setup guide (3 channels + webhooks)  
✅ **B.3:** ClickUp setup guide (3 workspaces + 12 lists)  
✅ **B.4:** HubSpot setup guide (3 objects + 3 pipelines)  

**Next:** Execute these 4 steps, check off the checklist, then we proceed to **OPTION A** (write loop scripts).

Ready to build infrastructure?
