# Venture Operations System: ClickUp + Notion Structure

**Status**: Ready to set up  
**Date**: 2026-07-31  
**Tools**: ClickUp (tasks/execution) + Notion (docs/knowledge)

---

## 📊 OVERALL STRUCTURE

```
Worldwidebro Holdings (Master Workspace)
│
├── ClickUp Workspace (Execution Hub)
│   ├── LT-005 (Medical Courier)
│   │   ├── 🎯 Revenue Targets
│   │   ├── 📞 Call Tracking (with scripts)
│   │   ├── 💰 Funding & Budget
│   │   ├── 👥 Team & Payroll
│   │   └── 📈 Weekly Progress
│   │
│   ├── OPS-001 (Staffing)
│   │   ├── 🎯 Revenue Targets
│   │   ├── 📞 Call Tracking (74 prospects)
│   │   ├── 💰 Funding & Budget
│   │   ├── 👥 Team & Payroll
│   │   └── 📈 Weekly Progress
│   │
│   ├── CON-001, EC-112, RE-001 (same structure)
│   │
│   └── 🏢 Corporate (Cross-venture)
│       ├── Funding Pipeline
│       ├── Licensing Deals
│       ├── Employee Roster
│       └── Weekly Revenue Dashboard
│
└── Notion Workspace (Knowledge Hub)
    ├── 🏢 Ventures Database (Master)
    │   └── Each venture has: Profile, Prospects, Scripts, Docs
    │
    ├── 📞 Prospect Database (Linked to ClickUp)
    │   └── LT-005: 4 hospital prospects
    │   └── OPS-001: 74 contractor prospects
    │   └── CON-001: 98 federal projects
    │   └── EC-112: 1000+ Etsy sellers
    │   └── RE-001: 500+ agents
    │
    ├── 📚 Knowledge Base
    │   ├── Call Scripts (per venture)
    │   ├── Funding Strategies
    │   ├── Revenue Models
    │   └── Operational Playbooks
    │
    └── 📈 Analytics Dashboard
        ├── Revenue Tracker
        ├── Funding Status
        └── Team Progress
```

---

## 🎯 CLICKUP STRUCTURE (EXECUTION HUB)

### Workspace: Worldwidebro Holdings

**Spaces (Per Venture):**

```
Space: LT-005 (Medical Courier)
├── Folder: Revenue & Targets
│   ├── List: Revenue Goals ($2K-3K first customer)
│   ├── List: Funding Checklist ($10K-15K needed)
│   └── List: Break-even Analysis
│
├── Folder: Customer Acquisition
│   ├── List: Prospect Calls
│   │   ├── Task: Call Duke Health (919) 684-8111
│   │   │   ├── Description: [CALL SCRIPT HERE]
│   │   │   ├── Due: Today
│   │   │   ├── Priority: Urgent
│   │   │   ├── Assignee: [Your name]
│   │   │   ├── Status: Not Started / In Progress / Done
│   │   │   └── Custom Fields:
│   │   │       - Contact Name: [name]
│   │   │       - Outcome: [Spoke to / Voicemail / Demo booked]
│   │   │       - Next Step: [Follow-up date]
│   │   │       - Revenue Potential: $2K-3K/month
│   │   │
│   │   ├── Task: Call UNC Health (919) 966-4131
│   │   ├── Task: Call Atrium Health (704) 355-1000
│   │   └── Task: Call Wake Forest (336) 716-2011
│   │
│   └── List: Demo Pipeline
│       └── Task: Schedule demo with [company]
│
├── Folder: Operations
│   ├── List: Funding
│   │   ├── Task: Reserve $5K for vehicle deposit
│   │   ├── Task: Apply for HIPAA certification ($500-1K)
│   │   └── Task: Get insurance quote ($1K-2K/month)
│   │
│   ├── List: Hiring
│   │   ├── Task: Vet first driver/contractor
│   │   ├── Task: Set up payroll processing
│   │   └── Task: Draft contractor agreement
│   │
│   └── List: First Customer Execution
│       ├── Task: Book first pickup (Fri of Week 1)
│       ├── Task: Execute first delivery
│       ├── Task: Get paid by hospital
│       └── Task: Pay driver ($200-300)
│
└── Folder: Weekly Progress
    ├── List: Week 1 (This week)
    ├── List: Week 2
    └── List: Week 3+

Space: OPS-001 (Staffing)
├── Folder: Revenue & Targets
│   ├── List: Revenue Goals ($3K-7K first customer)
│   ├── List: Placement Targets (5-10/month)
│   └── List: Commission Structure
│
├── Folder: Customer Acquisition
│   ├── List: Priority Calls (12 companies)
│   │   ├── Task: Call SYNCON (704) 555-0101
│   │   │   ├── Description: [CALL SCRIPT HERE]
│   │   │   ├── Pain Point: Crew shortages
│   │   │   ├── Value Prop: Pre-vetted crew dispatch
│   │   │   ├── Due: [Day]
│   │   │   └── Revenue Potential: $3K-7K/month
│   │   │
│   │   ├── Task: Call Riley & Associates (704) 555-0102
│   │   ├── Task: Call HICAPS Inc. (704) 555-0103
│   │   └── [9 more HIGH priority calls]
│   │
│   └── List: Medium Priority (Next 24 prospects)
│
├── Folder: Operations
│   ├── List: Contractor Network
│   │   └── Task: Vet electricians/HVAC techs
│   │
│   ├── List: First Placement
│   │   ├── Task: Match 3 electricians to SYNCON job
│   │   ├── Task: Electricians complete work
│   │   ├── Task: Invoice contractor ($1K)
│   │   └── Task: Pay electricians ($500-700 each)
│   │
│   └── List: Scaling
│       ├── Task: Build team management system
│       └── Task: Set up payment processing
│
└── Folder: Weekly Progress
    ├── List: Week 1
    └── List: Week 2+

Space: CON-001, EC-112, RE-001 (Same structure as above)
```

### Custom Fields (All Ventures)

Add to every task:
- **Contact**: Name, Phone, Email
- **Outcome**: Spoke to / Voicemail / Demo booked / Not interested
- **Revenue Potential**: $ amount
- **Next Step**: Follow-up date/action
- **Status**: Not Started / In Progress / Done / Closed Won

---

## 📚 NOTION STRUCTURE (KNOWLEDGE HUB)

### Master Database: Ventures

**Properties:**
- Name (LT-005, OPS-001, etc.)
- Sector (Logistics, Staffing, Construction, etc.)
- Status (Planning, Active, Live)
- Revenue Target (first month)
- Funding Needed
- Call Script
- Prospect List
- Operational Playbook

**Example Row - LT-005:**
```
Name: LT-005
Sector: Logistics - Medical Courier
Status: Active
Revenue Target: $2K-3K/month (first customer)
Funding Needed: $10K-15K (vehicle, cert, ops)
Call Script: [Link to script page]
Prospect List: [Link to prospect database]
Operational Playbook: [Link to operations doc]
Team Members: [Link to team roster]
Weekly Progress: [Link to weekly updates]
```

### Prospect Database (Linked to Ventures)

**Properties:**
- Company Name
- Contact Name
- Contact Role
- Phone
- Email
- Venture (LT-005, OPS-001, etc.)
- Priority (HIGH, MEDIUM, LOW)
- Pain Point
- Value Prop
- Call Script
- Status (Not contacted, Called, Demo booked, Customer)
- Revenue Potential
- Notes

**Example - LT-005 Prospects:**
```
| Company | Contact | Phone | Venture | Priority | Status | Revenue |
|---------|---------|-------|---------|----------|--------|---------|
| Duke Health | Lab Director | (919) 684-8111 | LT-005 | HIGH | Not contacted | $2K-3K/mo |
| UNC Health | Operations | (919) 966-4131 | LT-005 | HIGH | Not contacted | $2K-3K/mo |
| Atrium Health | Logistics Mgr | (704) 355-1000 | LT-005 | HIGH | Not contacted | $2K-3K/mo |
| Wake Forest | Lab Manager | (336) 716-2011 | LT-005 | HIGH | Not contacted | $1K-2K/mo |
```

### Call Script Pages (Template)

**Page: LT-005 Call Script**

```
Venture: LT-005 (Medical Courier)
Target: Hospital/Lab Directors

## Opening (30 sec)
"Hi [Name], this is [Your Name] with Worldwidebro Courier. 
We help [Hospital] eliminate cold-chain headaches with 
same-day, HIPAA-compliant specimen transport. Do you handle 
specimen logistics?"

## Value Prop (60 sec)
"We guarantee:
- Real-time tracking (Google Maps integration)
- HIPAA & SOC2 certified
- 1-hour STAT pickups
- Temperature-controlled vehicles
- Full insurance coverage

Typical customers save 2-3 hours/day on logistics coordination."

## Close (30 sec)
"I can get you set up with 3 free trial runs this week 
to see if it works for you. Does Tuesday at 2 PM work 
for a quick walkthrough?"

## Tracking
- Called: [Date]
- Outcome: [Spoke to / Voicemail / Demo booked]
- Next Step: [Follow-up date]
- Notes: [Any objections or interest signals]
```

### Operations Playbook Pages

**Page: LT-005 Operations Playbook**

```
## Phase 1: Funding & Setup (Week 1)
- Reserve $5K for vehicle
- Apply for HIPAA cert ($500-1K)
- Get insurance quote ($1K-2K/month)
- Set up payroll processing

## Phase 2: First Customer (Week 1-2)
- Call 3 hospitals (Duke, UNC, Atrium)
- Book first pickup (Friday Week 1)
- Execute delivery with contractor driver
- Invoice customer ($75 standard pickup)

## Phase 3: Revenue & Scaling (Week 2-3)
- Get paid by hospital ($75)
- Pay driver 50% ($37.50)
- Book next 5-10 pickups
- Generate $300-500/week revenue
- Hire first full-time driver ($500-700/week)

## Phase 4: Licensing (Week 3+)
- Document white-label platform
- Pitch to regional operators (TN, VA)
- Close first licensing deal ($1K/month + 10% rev share)
```

### Analytics Dashboard

**Page: Weekly Revenue Tracker**

```
## Revenue This Week
- LT-005: $0 → [updates as orders come in]
- OPS-001: $0 → [updates as placements happen]
- CON-001: $0
- EC-112: $0
- RE-001: $0

## Targets vs. Actual
- Week 1 Target: $5.1K-6.8K (operations)
- Week 1 Actual: $[amount]
- Variance: $[+/-]

## Funding Status
- LT-005: $10K needed, $[X] committed
- OPS-001: $2K needed, $[X] committed
- Total: $18K needed, $[X] committed

## Team Status
- LT-005 Driver: [Name], Status: [Not hired / Onboarding / Active]
- OPS-001 Contractors: [X] vetted, [X] placed
- Team Payroll This Week: $[amount]
```

---

## 🔗 LINKING CLICKUP & NOTION

### How They Work Together:

**ClickUp = Execution** (Day-to-day operations)
- Individual tasks (calls, deliveries, placements)
- Progress tracking (status updates, outcomes)
- Team assignments (who's doing what)
- Weekly dashboards (revenue, progress)

**Notion = Knowledge** (Reference & strategy)
- Prospect database (searchable by venture/status)
- Call scripts (copy-paste ready)
- Revenue models (reference)
- Playbooks (step-by-step guides)

**Linking:**
- ClickUp tasks link to Notion prospect records
- ClickUp descriptions embed Notion scripts
- Weekly ClickUp summaries feed into Notion analytics
- Revenue tracked in both (ClickUp for real-time, Notion for analysis)

---

## 🚀 SETUP THIS WEEK

### ClickUp Setup (30 min)

1. **Create Workspace**: "Worldwidebro Holdings"
2. **Create 5 Spaces**: One per venture (LT-005, OPS-001, etc.)
3. **Create Folders** (per space):
   - Revenue & Targets
   - Customer Acquisition
   - Operations
   - Weekly Progress
4. **Create Lists** (per folder): See structure above
5. **Add Tasks**: All 8 HIGH-priority calls + operational tasks
6. **Set Custom Fields**: Contact, Outcome, Revenue Potential, Next Step, Status
7. **Add Team Members**: You + any employees/contractors

### Notion Setup (30 min)

1. **Create Workspace**: "Worldwidebro Holdings"
2. **Create Ventures Database**: Master database with all ventures
3. **Create Prospect Database**: All 750+ prospects (linked to ventures)
4. **Create Call Scripts Pages**: One per venture
5. **Create Playbooks Pages**: Operations for each venture
6. **Create Analytics Page**: Weekly revenue tracker
7. **Link to ClickUp**: Add ClickUp task URLs in prospect records

### Templates (Copy & Paste Ready)

**ClickUp Task Template:**
```
Title: Call [Company] - [Venture]
Description: [Call Script from Notion]
Due: [Date]
Priority: Urgent
Assignee: [Name]
Custom Fields:
  Contact Name: [Name]
  Contact Phone: [Phone]
  Contact Email: [Email]
  Revenue Potential: $[Amount]/month
  Status: Not Started
  Next Step: [Follow-up if no answer]
```

**Notion Prospect Template:**
```
Company Name: [Name]
Contact Name: [Title]
Contact Phone: [Phone]
Contact Email: [Email]
Venture: [LT-005 / OPS-001 / etc.]
Priority: [HIGH / MEDIUM / LOW]
Pain Point: [From research]
Value Prop: [From script]
Call Script: [Link to script page]
Status: Not contacted
Revenue Potential: $[Amount]
ClickUp Link: [Link to task]
Notes: [Initial research]
```

---

## 📋 YOUR ACTION CHECKLIST THIS WEEK

- [ ] Create ClickUp workspace
- [ ] Create 5 venture spaces
- [ ] Add 8 HIGH-priority calls as tasks
- [ ] Create Notion workspace
- [ ] Add ventures database
- [ ] Add 750 prospects database
- [ ] Add call scripts (per venture)
- [ ] Add operations playbooks
- [ ] Link ClickUp & Notion
- [ ] Invite team members
- [ ] Start making calls (Task 1: Duke Health)

---

## 💰 TRACKING REVENUE IN BOTH SYSTEMS

### ClickUp Task (Real-time execution):
```
Title: First LT-005 Pickup - Duke Health
Status: In Progress
Due: Friday
Assignee: [Driver]
Outcome: Pickup completed, $75 earned
Payment Status: Invoice sent, awaiting payment
Notes: Temperature maintained throughout, customer satisfied
```

### Notion Analytics (End-of-week summary):
```
Week 1 Revenue
- LT-005: 1 pickup completed = $75
- OPS-001: [Pending first placement]
- Total Revenue: $75
- Total Payroll: $37.50 (driver)
- Profit: $37.50
- Status: ON TRACK (Week 1 target: $5K-6K by end of week)
```

---

**Status**: Ready to set up. Start with ClickUp for execution, then Notion for knowledge base.

