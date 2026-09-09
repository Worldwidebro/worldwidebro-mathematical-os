# EXECUTION GUIDE — Sep 10 Morning (50 minutes)

**Timeline:** 7:00 AM - 11:00 AM  
**Location:** This folder + terminal + browser tabs  
**Outcome:** 166 tasks in ClickUp + 5 scripts in email + 8 calendar reminders ready to fire  
**Authority:** CP-033 (Execution), CP-021 (Revenue)

---

## 🔐 PRE-CHECK: 7:00 AM (10 minutes)

### Verify Files Exist

```bash
# CSV files (166 prospects total)
ls -lh calls/*FINAL-CALL-LIST.csv
# Expected: 5 files

# Sales scripts (5 ventures)
ls -lh scripts/*-SALES-COACH.md
# Expected: 5 files

# Python scripts (3 stages)
ls -lh scripts/csv_to_clickup_converter.py
ls -lh scripts/send_sales_scripts.py
ls -lh scripts/create_calendar_reminders.py
# Expected: 3 files

# Verify line counts
wc -l calls/OPS-001-FINAL-CALL-LIST.csv  # 48 prospects
wc -l calls/CON-001-FINAL-CALL-LIST.csv  # 48 prospects
wc -l calls/LT-005-FINAL-CALL-LIST.csv   # 30 prospects
wc -l calls/LT-011-FINAL-CALL-LIST.csv   # 25 prospects
wc -l calls/RE-001-FINAL-CALL-LIST.csv   # 15 prospects
# Total should be 166 rows + 5 header lines = 171 total
```

### Verify Services Running

```bash
# ClickUp connectivity (no direct test, but verify in UI)
# Navigate to: https://app.clickup.com
# Log in → Verify workspace + folders exist
# Expected: 5 venture folders (OPS-001, CON-001, LT-005, LT-011, RE-001)

# Gmail connectivity
# Navigate to: https://mail.google.com
# Verify logged in as: winnerscirclewcllc@gmail.com
# Expected: Inbox ready to receive scripts

# Google Calendar connectivity
# Navigate to: https://calendar.google.com
# Verify logged in
# Expected: Calendar ready to receive reminders

# Company Brain infrastructure
cb infrastructure status
# Expected output: All services green ✅
```

### Checklist

- [ ] All 5 CSV files present and readable
- [ ] All 5 sales scripts present
- [ ] All 3 Python execution scripts present
- [ ] ClickUp workspace accessible + folders exist
- [ ] Gmail inbox accessible
- [ ] Google Calendar accessible
- [ ] Company Brain infrastructure healthy

**Status:** ✅ Ready to proceed to Stage 1

---

## 🎯 STAGE 1: CLICKUP TASK CREATION (8:00 AM - 8:15 AM, 15 min)

### Verify Existing Tasks (Safety Check)

```bash
# Optional: Check if tasks already exist
# Navigate to ClickUp, OPS-001 folder → Look at task count
# If tasks exist from a previous run, you may want to delete them first
# (This is a safety check, not required if starting fresh)
```

### Run Stage 1

```bash
cd /Users/acebless/Documents/The\ Company/Company\ Brain

# Preview mode (safe, shows what would be created without creating)
python3 scripts/csv_to_clickup_converter.py --list-only
# Expected: "166 tasks ready" + breakdown by venture

# Actual execution (creates 166 tasks)
python3 scripts/csv_to_clickup_converter.py --create
# Expected: Loop through all 166 rows, create each task
# Duration: ~15 minutes (depends on ClickUp API rate limits)
# Monitor for errors (will print as it goes)
```

### Verify Stage 1 Success

```bash
# Check result file
cat tasks_created.json | jq .
# Expected: tasks_created=166, ventures=5, status=complete

# Visual verification in ClickUp
# Navigate to: https://app.clickup.com
# Folders to check:
# ├─ OPS-001 folder → Should see ~48 tasks
# ├─ CON-001 folder → Should see ~48 tasks
# ├─ LT-005 folder → Should see ~30 tasks
# ├─ LT-011 folder → Should see ~25 tasks
# └─ RE-001 folder → Should see ~15 tasks

# Each task should have:
# ✅ Title: "{Contact Name} @ {Company Name}"
# ✅ Description: Phone, Title, Pain Signal
# ✅ Custom Fields: Pipeline Stage, Deal Value, Pain Signal, Call Outcome, Call Date
# ✅ Assigned to: You (founder)
# ✅ Priority: High
```

**Status:** ✅ 166 tasks created

---

## 📧 STAGE 2: GMAIL SCRIPT DISTRIBUTION (8:20 AM - 8:30 AM, 10 min)

### Run Stage 2

```bash
# Preview mode (safe)
python3 scripts/send_sales_scripts.py
# Expected: Shows 5 emails that would be sent (does not actually send)

# Actual execution (sends 5 emails)
python3 scripts/send_sales_scripts.py --execute
# Expected: Sends email to winnerscirclewcllc@gmail.com
# Duration: ~10 seconds (should be instant)
# Each email contains: Full script + ClickUp links + revenue details
```

### Verify Stage 2 Success

```bash
# Check result file
cat scripts_sent.json | jq .
# Expected: scripts_sent=5, status=complete

# Visual verification in Gmail
# Navigate to: https://mail.google.com
# Inbox should now have 5 new emails:
# ├─ [OPS-001] CareerOps Staffing — Sales Script Ready
# ├─ [CON-001] ACE Construction — Sales Script Ready
# ├─ [LT-005] HealthRoute Medical Courier — Sales Script Ready
# ├─ [LT-011] CarrierDispatch TMS — Sales Script Ready
# └─ [RE-001] WorldwideBro Real Estate — Sales Script Ready

# Each email contains:
# ✅ Full cold-call script
# ✅ Prospect count (48, 48, 30, 25, 15)
# ✅ Revenue per deal
# ✅ ClickUp task links
# ✅ Next steps checklist
```

**Status:** ✅ 5 scripts distributed

---

## 📅 STAGE 3: CALENDAR REMINDERS (8:35 AM - 8:45 AM, 10 min)

### Run Stage 3

```bash
# Preview mode (safe)
python3 scripts/create_calendar_reminders.py
# Expected: Shows 8 events that would be created (does not actually create)

# Actual execution (creates 8 reminders)
python3 scripts/create_calendar_reminders.py --execute
# Expected: Creates 8 events in Google Calendar
# Duration: ~10 seconds (should be instant)
# Events: 8 AM morning kickoff + 5 PM evening review (Sep 11-14)
```

### Verify Stage 3 Success

```bash
# Check result file
cat reminders_created.json | jq .
# Expected: reminders_created=8, status=complete

# Visual verification in Google Calendar
# Navigate to: https://calendar.google.com
# September 11-14 should show:
#
# Sep 11:
#   ├─ 8:00 AM  🔔 Morning: Cold Calls (Day 1)
#   └─ 5:00 PM  📊 Evening: Call Review (Day 1)
#
# Sep 12:
#   ├─ 8:00 AM  🔔 Morning: Cold Calls (Day 2)
#   └─ 5:00 PM  📊 Evening: Call Review (Day 2)
#
# Sep 13:
#   ├─ 8:00 AM  🔔 Morning: Cold Calls (Day 3)
#   └─ 5:00 PM  📊 Evening: Call Review (Day 3)
#
# Sep 14:
#   ├─ 8:00 AM  🔔 Morning: Cold Calls (Day 4)
#   └─ 5:00 PM  📊 Evening: Call Review + Revenue Checkpoint (FINAL)
#
# Each event should:
# ✅ Have description with goals + next steps
# ✅ Have notification 15 minutes before
# ✅ Show in your default calendar
```

**Status:** ✅ 8 calendar reminders created

---

## 🏁 CONSOLIDATION: ORCHESTRATOR SUMMARY (8:50 AM - 9:00 AM, 10 min)

### Generate Summary Report

```bash
# Generate consolidated summary
python3 scripts/orchestrator_summary.py

# Expected output:
# ✅ STAGE 1: CLICKUP TASK CREATION
#    Status: Complete
#    Tasks Created: 166
# 
# ✅ STAGE 2: GMAIL SCRIPT DISTRIBUTION
#    Status: Complete
#    Scripts Sent: 5/5
#
# ✅ STAGE 3: CALENDAR REMINDER CREATION
#    Status: Complete
#    Reminders Created: 8
#
# 🎯 EXECUTION READINESS
#    Status: ✅ All stages complete — ready for revenue campaign
```

### Save Summary

```bash
# Copy summary to today's log
cp orchestrator_summary.json 20-DECISIONS/EXECUTION_SUMMARY_SEP_10.json

# For reference
cat orchestrator_summary.py | tail -20
# Shows: Total prospects (166), revenue targets, next steps
```

---

## ✅ GO-LIVE VERIFICATION (9:00 AM - 11:00 AM)

### Final Checklist

- [ ] **ClickUp:** 166 tasks visible, all custom fields filled, all assigned to you
- [ ] **Gmail:** 5 script emails received and readable
- [ ] **Calendar:** 8 reminders set for Sep 11-14 (4 AM + 4 PM)
- [ ] **Result Files:** tasks_created.json, scripts_sent.json, reminders_created.json all exist
- [ ] **Ready Status:** Orchestrator summary shows "all stages complete"

### Now What? (Sep 11, 8:00 AM)

**Morning Ritual (Daily Sep 11-14):**
1. Wake up
2. Google Calendar alarm fires: "🔔 Morning: Cold Calls"
3. Open ClickUp → OPS-001 list
4. Open Gmail → Today's script
5. Start dialing (phone numbers in ClickUp task descriptions)
6. Update ClickUp task outcomes as you call

**Evening Ritual (Daily Sep 11-13, then Checkpoint Sep 14):**
1. Google Calendar alarm fires: "📊 Evening: Call Review"
2. Review ClickUp task updates for today
3. Update "Pipeline Stage" based on call results
4. Check Stripe dashboard for payment notifications
5. Log outcomes in spreadsheet

**Sep 14 Evening (Revenue Checkpoint):**
1. Calendar alarm: "📊 Evening: Call Review + Revenue Checkpoint (FINAL)"
2. Verify revenue in **all three systems:**
   - Stripe Dashboard: Payments captured?
   - Supabase (deal_payments table): Revenue attributed?
   - Venture Portal: Shows real money?
3. If $2,500+ appears: **PHASE 1 SUCCESS ✅**
4. If target not met: Document gaps + plan Phase 2

---

## 🚨 TROUBLESHOOTING

### Problem: ClickUp tasks not creating

**Cause:** ClickUp API key missing or invalid  
**Fix:**
```bash
# Check ClickUp connection
curl -H "Authorization: Bearer $CLICKUP_TOKEN" https://api.clickup.com/api/v3/team
# Should return: team info + team_id

# If error: Get new token from ClickUp Settings → API
# Update ~/.zshrc or ~/.env with new token
# Re-run: python3 scripts/csv_to_clickup_converter.py --create
```

### Problem: Gmail emails not sending

**Cause:** Gmail not connected or OAuth token expired  
**Fix:**
```bash
# Test Gmail connectivity
# Navigate to: https://mail.google.com
# Verify logged in as: winnerscirclewcllc@gmail.com

# If not logged in: Log in first, then re-run script
# If OAuth error: Re-authorize in MCP settings
```

### Problem: Calendar reminders not appearing

**Cause:** Google Calendar not connected or timezone mismatch  
**Fix:**
```bash
# Navigate to: https://calendar.google.com/calendar/u/0/r
# Verify logged in + calendar visible

# Check timezone: Settings → Timezone should be "America/New_York"
# If wrong: Change to America/New_York + re-run script
```

---

## 📊 SUCCESS METRICS

| Metric | Target | Sep 10 Status |
|--------|--------|---|
| ClickUp tasks | 166 | ✅ Created |
| Ventures represented | 5 | ✅ All represented |
| Gmail scripts | 5 | ✅ Sent |
| Calendar reminders | 8 | ✅ Set |
| Total execution time | 50 min | ✅ On track |

---

## 📝 NOTES FOR SEP 11-14

**Scoring Prospects During Calls:**
- **Interested:** Prospect expressed interest, asked questions
- **Objection:** Prospect had concern (price, timing, need), but didn't hang up
- **Voicemail:** No answer, left message
- **Declined:** Prospect said no, hung up

**After Each Call Update in ClickUp:**
- Change "Call Outcome" field to above
- Add comment: Brief notes on conversation
- Update "Pipeline Stage" if moved

**Revenue Tracking Sep 14:**
- Check Stripe every 2 hours (payments come in throughout day)
- Log any payment in spreadsheet (amount + time + prospect)
- Target: $2,500+ by EOD Sep 14

---

**Status:** ✅ READY TO EXECUTE SEP 10, 8:00 AM

**Next:** See calendar reminder Sep 11, 8:00 AM 🔔
