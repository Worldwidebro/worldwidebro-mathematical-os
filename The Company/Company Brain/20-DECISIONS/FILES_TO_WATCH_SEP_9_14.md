# FILES TO WATCH & UPDATE — Sep 9-14 Revenue Campaign

**Purpose:** Track which files to monitor and update as the revenue campaign progresses Sep 11-14

---

## 📋 FILES ACTIVE DURING CAMPAIGN

### Critical Files (Check Daily Sep 11-14)

| File | Purpose | When to Check | Who Updates | Update Frequency |
|------|---------|---|---|---|
| **Google Calendar** | Daily reminders | 8 AM + 5 PM | System (automated) | Every morning/evening |
| **Gmail Inbox** | Sales scripts | Sep 11, 8 AM | System (already sent Sep 9) | Once (read once) |
| **calls/OPS-001-FINAL-CALL-LIST.csv** | Prospect phone list | During calls | User (log outcomes) | After each call |
| **calls/CON-001-FINAL-CALL-LIST.csv** | Prospect phone list | During calls | User (log outcomes) | After each call |
| **calls/LT-005-FINAL-CALL-LIST.csv** | Prospect phone list | During calls | User (log outcomes) | After each call |
| **calls/LT-011-FINAL-CALL-LIST.csv** | Prospect phone list | During calls | User (log outcomes) | After each call |
| **calls/RE-001-FINAL-CALL-LIST.csv** | Prospect phone list | During calls | User (log outcomes) | After each call |
| **Stripe Dashboard** | Revenue tracking | Sep 14, 5 PM | Stripe (real-time) | Daily check |
| **Supabase (deal_payments)** | Revenue persistence | Sep 14, 5 PM | Automated webhook | Real-time |
| **Venture Portal** | Revenue display | Sep 14, 5 PM | Automated sync | Real-time |

### Reference Files (Read Once Before Sep 11)

| File | Purpose | Read By | Deadline |
|------|---------|---|---|
| **scripts/OPS-001-SALES-COACH.md** | Cold call script | User | Before Sep 11, 8 AM |
| **scripts/CON-001-SALES-COACH.md** | Cold call script | User | Before Sep 11, 8 AM |
| **scripts/LT-005-SALES-COACH.md** | Cold call script | User | Before Sep 11, 8 AM |
| **scripts/LT-011-SALES-COACH.md** | Cold call script | User | Before Sep 11, 8 AM |
| **scripts/RE-001-SALES-COACH.md** | Cold call script | User | Before Sep 11, 8 AM |
| **20-DECISIONS/PATH_1_QUICK_START.md** | Quick reference | User | Sep 11 morning |
| **20-DECISIONS/EXECUTION_GUIDE_SEP_10.md** | Detailed checklist | User | If issues arise |

### Status Files (Updated Sep 9, Track Changes)

| File | Purpose | Last Updated | Next Update |
|------|---------|---|---|
| **CLAUDE.md** | Project status | Sep 9 (execution section added) | Sep 14 (revenue checkpoint) |
| **20-DECISIONS/EXECUTION_LOG_SEP_9.md** | Execution log | Sep 9 | Sep 14 (final revenue numbers) |
| **20-DECISIONS/OPTION-C-ORCHESTRATOR-IMPLEMENTATION.md** | Architecture | Sep 9 | After Sep 14 (lessons learned) |

---

## 📊 FILES TO UPDATE BASED ON OUTCOMES

### If Revenue Target Achieved ($2,500+)

**Update these files Sep 14 evening:**
1. `CLAUDE.md` → Add "Phase 1 SUCCESS ✅" section
2. `REALITY.md` → Document actual revenue number
3. `20-DECISIONS/EXECUTION_LOG_SEP_9.md` → Add final results
4. `20-DECISIONS/OPTION-C-ORCHESTRATOR-IMPLEMENTATION.md` → Mark complete

### If Revenue Target NOT Met

**Update these files Sep 14 evening:**
1. `20-DECISIONS/EXECUTION_LOG_SEP_9.md` → Document gap analysis
2. `20-DECISIONS/PHASE-2-ANALYSIS.md` (create new) → What to fix
3. `CLAUDE.md` → Note partial success + gaps

---

## 🔄 WORKFLOW FOR UPDATING FILES DURING CAMPAIGN

### Daily (Sep 11-14)

**Morning (When alarm fires 8 AM):**
```
✅ Open calendar reminder
✅ Read script from email
✅ Open CSVs to get phone numbers
→ Start calling (5-10 min per call)
→ Log outcomes somewhere (spreadsheet or notes)
```

**Evening (When alarm fires 5 PM):**
```
✅ Open calendar reminder
✅ Count today's outcomes
✅ Update CSVs with outcomes (optional but recommended)
✅ Check Stripe for any new payments
→ Log in simple spreadsheet or text file
```

### Sep 14, 5 PM (Revenue Checkpoint)

**Critical:**
1. Open Stripe Dashboard
2. Search for charges from OPS-001 and CON-001
3. Note exact amount + time
4. Verify in Supabase: `SELECT SUM(amount_usd) FROM deal_payments WHERE venture IN ('OPS-001', 'CON-001');`
5. Check Venture Portal for real-time display
6. **Update CLAUDE.md with actual numbers**

---

## 💾 FILES THAT AUTO-UPDATE (No Manual Action Needed)

| System | File | Updates | Frequency |
|--------|------|---------|-----------|
| **Stripe** | (Dashboard) | Payment transactions | Real-time |
| **Supabase** | `deal_payments` table | Via webhook from Stripe | Real-time |
| **Google Calendar** | (Calendar app) | Reminders firing | Exact times |
| **Gmail** | (Email inbox) | Scripts (already there) | One-time Sep 9 |
| **Google Drive** | (Auto-sync) | Any scripts shared | Real-time |

---

## 📁 ClickUp WORKAROUND (If User Wants Tasks)

**Since Stage 1 (ClickUp creation) is blocked:**

**Option A: Manual Creation (Recommended)**
1. Go to https://app.clickup.com
2. Create ONE list: "Cold Calls Sep 11-14"
3. Create 166 tasks manually (takes ~2 hours)
   - Or create 5 subtasks for each venture
   - Or just reference CSV files during calls

**Option B: Skip ClickUp (Minimum)**
1. Just use CSV files + email scripts
2. Log outcomes in spreadsheet or text file
3. Check Stripe at end of day

**Update CLAUDE.md if you manually create ClickUp tasks** → Add note: "Stage 1 recovery completed manually by user Sep [date]"

---

## 📞 CALL TRACKING TEMPLATE (Optional)

If you want to track calls in a spreadsheet:

```
Date | Venture | Company | Contact | Phone | Script Used | Outcome | Notes | Follow-Up
2026-09-11 | OPS-001 | [Name] | [Person] | 555-1234 | OPS-001-v1 | Interested | Wants warehouse workers | Send profiles
```

---

## 🎯 SUCCESS METRICS TO TRACK

| Metric | Target | Deadline | Where to Check |
|--------|--------|----------|---|
| **Total Calls Made** | 40-60 calls | Sep 14 EOD | Your call log |
| **Interested Prospects** | 5-10 | Sep 14 EOD | Your call log |
| **Revenue Generated** | $2,500+ | Sep 14, 5 PM | Stripe Dashboard |
| **Deals Closed** | 1-2 | Sep 14 EOD | Stripe + Supabase |
| **Scripts Delivered** | 5/5 ✅ | Sep 11 | Gmail inbox |
| **Reminders Firing** | 8/8 ✅ | Sep 11-14 | Google Calendar |

---

## FILES TO PRESERVE (DO NOT DELETE)

- All CSV files in `/calls/` (backup copy of prospects)
- All scripts in `/scripts/*-SALES-COACH.md` (gold standard scripts)
- `20-DECISIONS/` folder (execution documentation)
- `CLAUDE.md` and `REALITY.md` (master references)

---

## FILES THAT CAN BE ARCHIVED AFTER SEP 14

- Individual call logs (after data is entered into CRM)
- Temporary outcome spreadsheets (after results consolidated)
- Execution logs (keep for 30 days, then archive to `/20-DECISIONS/ARCHIVED/`)

---

## CHECKLIST: Before Sep 11, 8 AM

- [ ] Read all 5 scripts from email
- [ ] Check Google Calendar → 8 reminders visible
- [ ] Download/open `/calls/*FINAL-CALL-LIST.csv` → Get first 10 phone numbers
- [ ] Test phone dialer works
- [ ] Have Stripe dashboard open in browser tab
- [ ] Have Supabase console open in another tab
- [ ] Set phone notification volume to high
- [ ] Have calendar notification enabled

---

**If any file needs emergency update during Sep 11-14:**
- Email or Slack the update to your own notes
- Consolidate all changes into CLAUDE.md on Sep 14 evening
- Commit to Git with message: "Update: Sep 14 revenue campaign results"

---

**Remember:** The scripts and reminders are already live. All you need to do Sep 11 is pick up the phone and start calling. Everything else is automated. 🚀
