[[STARTHERE]] | [[20-DECISIONS/README|Decisions Index]] | [[REALITY]]

# REFERENCE CARD — Sep 11-14 Revenue Campaign

**Keep this handy during the campaign.** Pin it or bookmark it.

---

## 🎬 SEP 11, 8:00 AM — START HERE

**What you'll see:**
1. 🔔 **Calendar alarm:** "Morning: Cold Calls (Day 1)"
2. Open email → 5 scripts ready to read
3. Open `/calls/OPS-001-FINAL-CALL-LIST.csv` → Get phone numbers
4. Start dialing

**You have:**
- ✅ Full cold-call script in email (read it once)
- ✅ Prospect phone numbers in CSV
- ✅ 48 OPS-001 prospects ready
- ✅ Revenue target: $2,500 per placement

---

## 📞 DURING CALLS (Daily Sep 11-13, Sep 14)

**Before each call:**
1. Look at prospect record in CSV
2. Read relevant script from email
3. Get phone number
4. Dial

**During call:**
1. Use script opener (15 sec)
2. Deliver value prop (30 sec)
3. Ask for permission
4. Listen for objections
5. Use objection handler if needed

**After call:**
1. Note outcome: Interested / Objection / Voicemail / Declined
2. Add to simple spreadsheet or notes
3. Move to next prospect

---

## 🎯 DAILY SCHEDULE

**8:00 AM**
- 🔔 Calendar: "Morning: Cold Calls"
- Make 10-15 calls
- Outcomes: Interested/Objection/Voicemail/Declined

**5:00 PM**
- 📊 Calendar: "Evening: Call Review"
- Count today's outcomes
- Check Stripe for payments
- Note any callbacks needed

**Sep 14, 5:00 PM**
- 💰 Calendar: "Revenue Checkpoint (CRITICAL)"
- Open Stripe Dashboard
- Look for payments from OPS-001 / CON-001
- Verify $2,500+ appears
- **SUCCESS or ANALYZE GAPS**

---

## 📊 REVENUE TRACKING

### Immediate (Sep 11-14)

**Stripe Dashboard:**
- https://dashboard.stripe.com
- Search for charges from "CareerOps" or "ACE Construction"
- Note amount + time + customer

**Supabase:**
```sql
SELECT * FROM deal_payments 
WHERE venture IN ('OPS-001', 'CON-001')
ORDER BY created_at DESC;
```

**Venture Portal:**
- Should show real revenue in OPS-001 + CON-001 cards

### By Sep 14, 5 PM

**Update CLAUDE.md with:**
- Total calls made
- Total interested prospects
- Total revenue $ amount
- Which deals closed

---

## 🗂️ KEY FILES AT A GLANCE

| Need | File | Where | How Often |
|------|------|-------|-----------|
| **Script for OPS-001** | scripts/OPS-001-SALES-COACH.md | Email | Read once Sep 11 AM |
| **Script for CON-001** | scripts/CON-001-SALES-COACH.md | Email | Read once Sep 11 AM |
| **Prospect phones (OPS)** | calls/OPS-001-FINAL-CALL-LIST.csv | `/calls/` | Reference during calls |
| **Prospect phones (CON)** | calls/CON-001-FINAL-CALL-LIST.csv | `/calls/` | Reference during calls |
| **Daily reminders** | Google Calendar | Calendar app | 8 AM + 5 PM automated |
| **Outcomes log** | Your spreadsheet or notes | Anywhere | Update after each call |
| **Revenue check** | Stripe Dashboard | https://dashboard.stripe.com | Check Sep 14, 5 PM |
| **Project status** | 20-DECISIONS/EXECUTION_LOG_SEP_9.md | Local repo | Reference/update Sep 14 |

---

## 💡 OBJECTION HANDLERS (Quick Lookup)

### OPS-001 (Staffing)

**"We use a temp agency"**
→ Most temp agencies charge 40-60% markup, workers leave in 90 days. Our guarantee: if they leave in 6 months, we replace free.

**"$2,500 is expensive"**
→ What does recruiting + training one worker cost? Most say $3-5K. We're $2,500 flat with trained, vetted workers.

**"We're not hiring right now"**
→ When's your next hiring surge? Let me follow up then.

**"Workers need to be reliable"**
→ That's exactly what we solve. Screening includes background checks + reference calls. 12-month retention proves it works.

**"Let me check with management"**
→ Perfect. Let me send three profiles first so you can review. Then you have real names to discuss with your manager.

---

### CON-001 (Construction)

**"We use spreadsheets/pen and paper"**
→ Spreadsheets don't catch field reality. You find out two weeks later crews double-entered hours. That's money gone.

**"$299 is too much"**
→ Most GCs find $2-5K in inefficiencies. So $299 pays for itself in a month. If you don't find value, I won't charge you.

**"We don't have time"**
→ It's 1-hour on-site. We don't need to interrupt your crews much. I'll show you findings same day.

**"We're happy with how things are"**
→ Most GCs who say that find $50-100K in waste once we audit. Let me just come do a free look.

**"Let me think about it"**
→ Let me schedule a time slot this week, and you can confirm or cancel by tomorrow.

---

## ⚠️ IF SOMETHING GOES WRONG

**Calendar reminder didn't fire:**
- Check phone notifications enabled
- Manually check Google Calendar at 8 AM
- Proceed with calling anyway

**Can't access email scripts:**
- Scripts are also in `/scripts/` folder locally
- Read from: `scripts/OPS-001-SALES-COACH.md` etc.

**Stripe not showing payment:**
- Refresh Stripe dashboard (F5)
- Check email for payment confirmation
- Call customer to confirm payment went through
- Check by Sep 14 5 PM

**Prospect not answering:**
- Leave voicemail (script has voicemail version)
- Log as "Voicemail"
- Move to next prospect

---

## ✅ PRE-CALL CHECKLIST

- [ ] Phone battery charged
- [ ] Quiet room ready (no background noise)
- [ ] Script open in email or folder
- [ ] CSV with phone numbers ready
- [ ] Notepad open (for outcomes)
- [ ] Stripe tab open (for real-time monitoring)
- [ ] Calendar set to alert you 8 AM / 5 PM

---

## 🎯 DAILY TARGETS

| Day | Calls Target | Expected Interested | Expected Objections |
|-----|---|---|---|
| **Sep 11** | 10-15 | 2-4 | 3-5 |
| **Sep 12** | 10-15 | 2-4 | 3-5 |
| **Sep 13** | 10-15 | 2-4 | 3-5 |
| **Sep 14** | 10-15 | 2-4 | 3-5 |
| **TOTAL** | 40-60 | 8-16 | 12-20 |

**For revenue:** You need just **1-2 placements** to hit $2,500 target (OPS-001 = $2,500 each)

---

## 🏆 SUCCESS CRITERIA (Sep 14, 5 PM)

**Minimum for Phase 1 SUCCESS:**
- ✅ At least $2,500 in Stripe (1 OPS-001 placement, or $299 + $2,201 from other ventures)
- ✅ Revenue appears in Supabase deal_payments table
- ✅ Venture Portal shows real money
- ✅ CLAUDE.md updated with actual numbers

**Bonus for Phase 1 EXCELLENT:**
- 🎉 $3K-5K+ (multiple placements)
- 🎉 5+ interested prospects in pipeline
- 🎉 Strong feedback for future iteration

---

## 📞 REMEMBER

- **You have scripts.** You don't need to memorize them.
- **You have reminders.** Calendar will keep you on track.
- **You have prospects.** 166 real people, qualified, high confidence (67-95%).
- **You have backup.** If ClickUp tasks aren't created, the CSVs + scripts are enough.
- **You have runway.** 4 days to make calls, Sep 14 to verify revenue.

**The hardest part is already done.** All the automation is built, scripts are written, reminders are set.

All you need to do Sep 11: Pick up phone and start calling.

---

**Good luck.** 📞🎉

---

*Last updated: Sep 9, 2026, 3:30 PM EDT*  
*Status: Ready to Execute Sep 11 at 8 AM*  
*Authority: CP-033 (Execution), CP-021 (Revenue Operations)*
