# OPTION C: Full MCP Orchestrator — Implementation (Sep 10)

**Status:** Ready to execute Sep 10 morning (50 min setup + 5 min execution)  
**Authority:** CP-033 (Execution), CP-021 (Revenue)  
**Objective:** Automate 166 tasks → 5 scripts → 8 calendar reminders in 5 minutes

---

## ORCHESTRATOR ARCHITECTURE

```
Entry Point: /2026-09-10-mcp-orchestrator.sh
    ↓
Parse CSVs (5 ventures, 166 prospects)
    ↓
Stage 1: CREATE CLICKUP TASKS
    ├─ Load: calls/OPS-001-FINAL-CALL-LIST.csv (48 rows)
    ├─ Load: calls/CON-001-FINAL-CALL-LIST.csv (48 rows)
    ├─ Load: calls/LT-005-FINAL-CALL-LIST.csv (30 rows)
    ├─ Load: calls/LT-011-FINAL-CALL-LIST.csv (25 rows)
    ├─ Load: calls/RE-001-FINAL-CALL-LIST.csv (15 rows)
    ├─ MCP: mcp__claude_ai_ClickUp__clickup_create_task × 166
    ├─ Loop: Create task in venture-specific folder + list
    ├─ Set: Custom fields (Pipeline Stage, Deal Value, Pain Signal, Call Outcome, Call Date)
    ├─ Assign: To [founder] (self)
    └─ Collect: Task IDs + links → tasks_created.json
    ↓
Stage 2: SEND SALES SCRIPTS VIA GMAIL
    ├─ Load: scripts/OPS-001-SALES-COACH.md
    ├─ Load: scripts/CON-001-SALES-COACH.md
    ├─ Load: scripts/LT-005-SALES-COACH.md
    ├─ Load: scripts/LT-011-SALES-COACH.md
    ├─ Load: scripts/RE-001-SALES-COACH.md
    ├─ MCP: mcp__claude_ai_Gmail__send_message × 5
    ├─ To: winnerscirclewcllc@gmail.com (your email)
    ├─ Subject: "[VENTURE] Sales Script Ready"
    ├─ Body: Script text + ClickUp task link + revenue potential
    └─ Collect: Send confirmations → scripts_sent.json
    ↓
Stage 3: CREATE CALENDAR REMINDERS
    ├─ MCP: mcp__claude_ai_Google_Calendar__create_event × 8
    ├─ Sep 11 8 AM: "🔔 Morning: Cold Calls (Day 1)"
    ├─ Sep 11 5 PM: "📊 Evening: Call Review (Day 1)"
    ├─ Sep 12 8 AM: "🔔 Morning: Cold Calls (Day 2)"
    ├─ Sep 12 5 PM: "📊 Evening: Call Review (Day 2)"
    ├─ Sep 13 8 AM: "🔔 Morning: Cold Calls (Day 3)"
    ├─ Sep 13 5 PM: "📊 Evening: Call Review (Day 3)"
    ├─ Sep 14 8 AM: "🔔 Morning: Cold Calls (Day 4)"
    ├─ Sep 14 5 PM: "📊 Evening: Call Review + Revenue Checkpoint (Day 4)"
    └─ Collect: Event IDs → reminders_created.json
    ↓
COMPLETION REPORT
├─ ✅ 166 tasks created (4 hours of cold-call work)
├─ ✅ 5 scripts distributed (ready to read)
├─ ✅ 8 reminders set (triggers your workflow)
└─ 💰 Revenue path unblocked (all automation in place, just make calls)
```

---

## PRE-EXECUTION CHECKLIST (Sep 10, 7 AM)

- [ ] CSV files verified (calls/ folder, 166 rows total)
- [ ] Sales scripts verified (scripts/ folder, 5 files)
- [ ] ClickUp workspace accessed + folders/lists verified
- [ ] Gmail connected + can send email
- [ ] Google Calendar connected + can create events
- [ ] OmniRoute running (omniroute_status() passes)
- [ ] Neo4j running (neo4j_status() passes)

---

## EXECUTION SEQUENCE

### Step 1: Load CSVs + Verify (5 min)
```bash
# Check CSV structure
head -5 calls/OPS-001-FINAL-CALL-LIST.csv
head -5 calls/CON-001-FINAL-CALL-LIST.csv
head -5 calls/LT-005-FINAL-CALL-LIST.csv
head -5 calls/LT-011-FINAL-CALL-LIST.csv
head -5 calls/RE-001-FINAL-CALL-LIST.csv

# Count rows (should be 166 total)
wc -l calls/*FINAL-CALL-LIST.csv
```

### Step 2: Stage 1 — ClickUp Task Creation (15 min)

**For each CSV:**
1. Read prospect row (company_name, phone, contact_name, title, pain_signal)
2. Call: `mcp__claude_ai_ClickUp__clickup_create_task`
3. Parameters:
   ```json
   {
     "list_id": "{venture_folder_list_id}",
     "title": "{contact_name} @ {company_name}",
     "description": "Phone: {phone}\nTitle: {title}\nPain Signal: {pain_signal}",
     "priority": "high",
     "custom_fields": {
       "Pipeline Stage": "Contacted",
       "Deal Value": "{revenue_potential}",
       "Pain Signal": "{pain_signal}",
       "Call Outcome": "Not yet called",
       "Call Date": "Sep 11-14"
     },
     "assignees": ["{founder_clickup_id}"]
   }
   ```

**Result:** 166 tasks in ClickUp, one per prospect, linked to correct venture folder

### Step 3: Stage 2 — Gmail Script Distribution (10 min)

**For each script:**
1. Read file (scripts/OPS-001-SALES-COACH.md, etc.)
2. Call: `mcp__claude_ai_Gmail__send_message`
3. Parameters:
   ```json
   {
     "to": "winnerscirclewcllc@gmail.com",
     "subject": "[OPS-001] Sales Script Ready for Cold Calls",
     "body": "Cold Call Script for CareerOps Staffing\n\n{script_text}\n\n---\n\nAll 48 prospects for OPS-001 are now in ClickUp.\nReview task details before each call.\nRevenue potential: $2,500 per placement.\n\nStart: Sep 11, 8 AM (see calendar reminders)"
   }
   ```

**Result:** 5 emails in your inbox, one per venture, with script ready to read

### Step 4: Stage 3 — Calendar Reminders (10 min)

**Create 8 recurring reminders:**
```json
Morning Reminders (8 AM, Sep 11-14):
{
  "summary": "🔔 Morning: Cold Calls (Day 1)",
  "description": "Make 10-15 calls today. Script in email. ClickUp tasks ready.",
  "start": "2026-09-11T08:00:00",
  "end": "2026-09-11T09:00:00",
  "reminders": [{"method": "notification", "minutes": 15}]
}

Evening Reminders (5 PM, Sep 11-13, 14):
{
  "summary": "📊 Evening: Call Review (Day 4 = Revenue Checkpoint)",
  "description": "Review today's calls. Update ClickUp task outcomes. Check Stripe for payments.",
  "start": "2026-09-14T17:00:00",
  "end": "2026-09-14T18:00:00",
  "reminders": [{"method": "notification", "minutes": 5}]
}
```

**Result:** 8 calendar events set, triggers your daily workflow

---

## EXPECTED OUTCOMES (Sep 10 by 11 AM)

| Component | Metric | Target | Status |
|-----------|--------|--------|--------|
| **ClickUp Tasks** | Tasks created | 166 | ✅ Ready to create |
| | Ventures represented | 5 | ✅ Ready |
| | Custom fields filled | 100% | ✅ Ready |
| | Assignment | All to founder | ✅ Ready |
| **Gmail Scripts** | Emails sent | 5 | ✅ Ready to send |
| | Content | Full script + links | ✅ Ready |
| **Calendar** | Reminders set | 8 | ✅ Ready to create |
| | Coverage | Sep 11-14 daily | ✅ Ready |

---

## EXECUTION COMMAND (Sep 10, 9 AM)

```bash
# Stage 1: Create all ClickUp tasks
python3 scripts/csv_to_clickup_converter.py --create

# Stage 2: Send all scripts to email
python3 scripts/send_sales_scripts.py --all

# Stage 3: Set all calendar reminders
python3 scripts/create_calendar_reminders.py --week

# Final: Print completion report
python3 scripts/orchestrator_summary.py
```

---

## WHAT HAPPENS NEXT (Sep 11-14)

**Each Morning (8 AM):**
- Calendar reminder fires: "🔔 Morning: Cold Calls"
- You open ClickUp → Today's 10-15 task list
- You open email → Read script (sent Sep 10)
- You start calling (numbers in ClickUp task details)

**During Calls:**
- ClickUp task open in second window
- Update "Call Outcome" field as you call
- Log call duration, objections handled

**Each Evening (5 PM):**
- Calendar reminder fires: "📊 Evening: Call Review"
- Review today's ClickUp task updates
- Check Stripe dashboard for payment confirmations
- Update "Pipeline Stage" based on call outcomes

**Sep 14 (Revenue Checkpoint):**
- Evening reminder: "📊 Evening: Call Review + Revenue Checkpoint"
- Target: $2,500 (OPS-001) + $299 (CON-001) minimum
- Verify in Stripe, Supabase, and Venture Portal

---

## MCP TOOLS WIRED

**ClickUp (166 calls):**
- `mcp__claude_ai_ClickUp__clickup_create_task`
- `mcp__claude_ai_ClickUp__clickup_update_task` (during calls)
- `mcp__claude_ai_ClickUp__clickup_get_custom_fields`

**Gmail (5 calls):**
- `mcp__claude_ai_Gmail__send_message`

**Google Calendar (8 calls):**
- `mcp__claude_ai_Google_Calendar__create_event`

**Supporting (Monitoring):**
- `company-brain:neo4j_status()`
- `company-brain:infrastructure_status()`
- `omniroute:list_models()` (for later agent routing)

---

## DURATION

- **Setup (Sep 10, 7-9 AM):** Verify checklist (2 hours, manual)
- **Execution (Sep 10, 9-11 AM):** Run 3 scripts (50 minutes automated)
- **Result:** All 166 tasks ready Sep 10 at 11 AM
- **Revenue window:** Sep 11-14 (4 days of calls)
- **Checkpoint:** Sep 14, 5 PM (revenue confirmed)

---

## ROLLBACK PLAN (If Something Breaks)

**If ClickUp fails:**
- CSV still exists (calls/*)
- Manually create tasks in ClickUp (5 min per venture)
- Or retry: `python3 scripts/csv_to_clickup_converter.py --create --retry`

**If Gmail fails:**
- Scripts still in scripts/ folder
- Manually forward scripts to your email (2 min)

**If Calendar fails:**
- Manually add 8 reminders to Google Calendar (5 min)

**Bottom line:** Worst case, 15 min of manual work still gets you to Day 1 ready

---

## AUTHORITY & APPROVALS

- **CP-033 (Execution):** This orchestrator is an execution workflow (Stage 1 of revenue automation)
- **CP-021 (Revenue):** This triggers revenue recognition in Stripe/Supabase/Venture Portal
- **Approval Gate:** Revenue checkpoint Sep 14 (founder confirms $2.5K+ in systems)

---

**Status:** ✅ Architecture Complete | ⏳ Execution Scheduled Sep 10, 9 AM

**Next:** Sep 10, 7 AM → Run pre-execution checklist
