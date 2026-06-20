# OPTION B: MASTER EXECUTION CHECKLIST
## Complete Infrastructure Build (Supabase → Slack → ClickUp → HubSpot)

**Status:** 🟢 READY TO EXECUTE  
**Date:** 2026-06-10  
**Timeline:** 3 hours total  
**Owner:** You

---

## WHAT YOU'RE BUILDING

Complete infrastructure foundation for OPS-001, CON-001, RE-001 to run 9 operational loops.

```
Supabase  → Database (19 tables)
Slack     → Communication (3 channels + webhooks)
ClickUp   → Task Management (3 workspaces, 12 lists)
HubSpot   → CRM/Pipeline (3 objects, 3 pipelines)
```

---

## FILES YOU NEED

| File | Purpose | Status |
|------|---------|--------|
| SUPABASE-SCHEMA-LOOPS.sql | SQL schema (19 tables) | ✅ Ready |
| OPTION-B2-B4-INFRASTRUCTURE-SETUP.md | Setup guide (Slack/ClickUp/HubSpot) | ✅ Ready |
| This checklist | Execution tracking | ✅ Ready |

---

## PHASE 1: SUPABASE (10 minutes)

**Step 1.1: Open Supabase**
```
1. Go to https://supabase.com
2. Log in to CivilizationOS project
3. Click "SQL Editor"
4. Create new query
```

**Step 1.2: Execute SQL**
```
1. Open: SUPABASE-SCHEMA-LOOPS.sql
2. Copy entire SQL
3. Paste into Supabase
4. Click RUN
5. Wait for completion

SQL executed: ☐
```

**Step 1.3: Verify Tables**
```
Check these exist:

OPS-001:
  ☐ staffing_contractors
  ☐ staffing_assignments
  ☐ staffing_time_logs
  ☐ staffing_payroll
  ☐ staffing_feedback

CON-001:
  ☐ construction_projects
  ☐ construction_daily_logs
  ☐ construction_subcontractors
  ☐ construction_subcontractor_assignments
  ☐ construction_invoices
  ☐ construction_opportunities

RE-001:
  ☐ real_estate_properties
  ☐ real_estate_tenants
  ☐ real_estate_rent_payments
  ☐ real_estate_maintenance_requests
  ☐ real_estate_monthly_expenses
  ☐ real_estate_valuations

Tracking:
  ☐ venture_health_scores
  ☐ loop_execution_logs

B.1 COMPLETE: ☐
```

---

## PHASE 2: SLACK (30 minutes)

**Step 2.1: Create Channels**
```
Create 3 channels:
  ☐ ops-001-staffing
  ☐ con-001-construction
  ☐ re-001-property

(See OPTION-B2-B4-INFRASTRUCTURE-SETUP.md for details)
```

**Step 2.2: Create Webhooks**
```
Reference guide: OPTION-B2-B4-INFRASTRUCTURE-SETUP.md → B.2 → Step 2

For each channel:
  1. Go to https://api.slack.com/apps
  2. Create New App → "From scratch"
  3. Name: "Loop Automation - [Venture Name]"
  4. Select workspace
  5. Incoming Webhooks → Activate
  6. Add New Webhook to Workspace
  7. Select matching channel
  8. Copy URL, save in password manager

Webhooks created:
  ☐ Staffing
  ☐ Construction
  ☐ Property
```

**Step 2.3: Configure Channels**
```
For each channel:
  ☐ Add topic
  ☐ Add description
  ☐ Add emoji to name
  ☐ Set notifications

Channels configured: ☐
```

**Step 2.4: Test Webhooks**
```
For each webhook:
  curl -X POST -H 'Content-type: application/json' \
    --data '{"text":"Test from Loop"}' \
    [YOUR-WEBHOOK-URL]

Expected: Message appears in channel

Webhooks tested:
  ☐ Staffing
  ☐ Construction
  ☐ Property

B.2 COMPLETE: ☐
```

---

## PHASE 3: CLICKUP (60 minutes)

**Step 3.1: Create Workspaces & Lists**
```
Reference: OPTION-B2-B4-INFRASTRUCTURE-SETUP.md → B.3

OPS-001 (4 lists):
  ☐ Active Assignments
  ☐ Pending Matches
  ☐ Contractor Pipeline
  ☐ Payroll Queue

CON-001 (4 lists):
  ☐ Active Projects
  ☐ Opportunities/Bids
  ☐ Subcontractor Schedule
  ☐ Quality Issues

RE-001 (4 lists):
  ☐ Properties
  ☐ Tenant Management
  ☐ Maintenance Requests
  ☐ Capital Planning

All lists created: ☐
```

**Step 3.2: Add Custom Fields**
```
Add custom fields to each list (see setup guide):
  ☐ Text fields
  ☐ Number fields
  ☐ Date fields
  ☐ Select/dropdown fields
  ☐ Currency fields

All custom fields added: ☐
```

**Step 3.3: Set Up Automations**
```
OPS-001 (4 automations):
  ☐ Match created → Create task in Pending Matches
  ☐ Task approved → Move to Active Assignments
  ☐ Every Friday → Remind to review payroll
  ☐ Assignment ends → Archive

CON-001 (4 automations):
  ☐ Opportunity qualified → Create bid task
  ☐ 3 days before deadline → Send reminder
  ☐ Project 80% done → Flag closeout
  ☐ Daily → Check timelines

RE-001 (4 automations):
  ☐ Monthly (1st) → Create "Collect Rent" task
  ☐ Monthly (15th) → Create "Pay Expenses" task
  ☐ 60 days before lease end → Create renewal task
  ☐ Maintenance in-progress → Notify manager

All automations created: ☐
```

**Step 3.4: Test**
```
For each workspace:
  ☐ Create sample task
  ☐ Fill in custom fields
  ☐ Test automation trigger
  ☐ Delete sample when done

ClickUp tested: ☐
B.3 COMPLETE: ☐
```

---

## PHASE 4: HUBSPOT (60 minutes)

**Step 4.1: Create Custom Objects**
```
Reference: OPTION-B2-B4-INFRASTRUCTURE-SETUP.md → B.4

  ☐ Placement (OPS-001)
  ☐ Bid (CON-001)
  ☐ Property (RE-001)

All objects created: ☐
```

**Step 4.2: Create Pipelines**
```
  ☐ Placement Pipeline (OPS-001)
     Stages: In Conversation → Negotiating → Placed → Completed
  
  ☐ Bid Pipeline (CON-001)
     Stages: Opportunity → Bid Prepared → Bid Submitted → Won → Lost → No-Bid
  
  ☐ Lease Pipeline (RE-001)
     Stages: Tenant Search → Application Pending → Approved → Leasing → Notice Given → Vacant

All pipelines created: ☐
```

**Step 4.3: Create Workflows**
```
  ☐ Placement → Feedback (trigger: moved to Completed)
  ☐ Bid → Project (trigger: moved to Won)
  ☐ Lease → Reminders (trigger: monthly)
  ☐ Property Valuation (trigger: manual)

All workflows created: ☐
```

**Step 4.4: Create Dashboards**
```
  ☐ OPS-001 Staffing Overview
  ☐ CON-001 Bid Pipeline
  ☐ RE-001 Properties

All dashboards created: ☐
```

**Step 4.5: Test**
```
  ☐ Create sample record in each object
  ☐ Move through pipeline
  ☐ Verify workflows trigger
  ☐ Check dashboards show data
  ☐ Delete samples when done

HubSpot tested: ☐
B.4 COMPLETE: ☐
```

---

## FINAL VERIFICATION

All infrastructure working?

```
SUPABASE:
  ☐ 19 tables exist
  ☐ Indexes created
  ☐ Realtime enabled

SLACK:
  ☐ 3 channels exist
  ☐ 3 webhooks working
  ☐ Test messages posted

CLICKUP:
  ☐ 3 workspaces exist
  ☐ 12 lists created
  ☐ Custom fields working
  ☐ Automations active

HUBSPOT:
  ☐ 3 objects created
  ☐ 3 pipelines created
  ☐ 4 workflows created
  ☐ 3 dashboards created
```

---

## TIME LOG

| Phase | Estimated | Actual |
|-------|-----------|--------|
| Supabase | 10 min | ___ |
| Slack | 30 min | ___ |
| ClickUp | 60 min | ___ |
| HubSpot | 60 min | ___ |
| Testing | 20 min | ___ |
| **TOTAL** | **3 hours** | **___** |

---

## NEXT: OPTION A

Once this is complete:

```
✅ OPTION B DONE (infrastructure built)
→ OPTION A: Write loop scripts (Claude writes these)
→ OPTION C: Test OPS-001 loops
→ OPTION D: Deploy all 9 loops
```

---

## STATUS: READY

All infrastructure files created. All setup guides written.

**You have everything needed to build Option B.**

Start with Phase 1 (Supabase) and work through all 4 phases.

**Expected completion:** 3 hours  
**Difficulty:** Low  
**Risk:** Very low (reversible)

**Ready to begin?**
