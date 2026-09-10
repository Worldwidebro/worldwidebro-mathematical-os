# LT-005: TODAY CHECKLIST (Sep 10, 2026)
**What You Need to Do RIGHT NOW to Execute Tomorrow**

---

## ⏰ TIMELINE: 3-4 hours of work
- **Now - 12 PM:** Recruit drivers (direct recruitment)
- **12 PM - 1 PM:** Prepare prospect list + phone numbers
- **1 PM - 2 PM:** Read + practice script
- **2 PM - 4 PM:** Verify Stripe + Supabase setup
- **EOD:** Everything ready for 8 AM call start tomorrow

---

## 🚨 HIGHEST PRIORITY: RECRUIT DRIVERS (INDEPENDENT)

**TASK:** Post driver recruitment job + start recruiting directly

**Direct Recruitment Channels (Choose 2-3):**

### Option A: Facebook Groups + Local Community
```
Post to:
- NC Local Job Groups (Search "North Carolina jobs" on Facebook)
- Raleigh/Charlotte/Durham community groups
- Gig work groups

Message:
"🚗 Medical Courier Drivers Needed — Flexible Hours

We're launching a medical courier service and need 3 drivers ASAP.

What you'll do:
- Same-day medical specimen delivery (short routes, high pay)
- Temperature-controlled transport
- Proof of delivery documentation
- Work flexible hours (part-time OK)

Requirements:
✅ Valid driver's license
✅ Clean driving record  
✅ Vehicle preferred (or willing to use company vehicle)
✅ Available starting Sep 12
✅ Willing to do 2-hour HIPAA training

Compensation: $25-30 per delivery
Opportunity: If trial succeeds, scales to full-time

Interested? Reply with your phone number.
Contact: [YOUR PHONE] or [YOUR EMAIL]"
```

### Option B: Craigslist Gigs
```
Go to: craigslist.org → Raleigh/Charlotte/Durham → Gigs
Post identical message above
```

### Option C: LinkedIn Outreach
```
Search: "Delivery drivers" OR "Courier drivers" in NC
Send: Personalized message with job offer
Message: "Hi [Name], we're hiring medical courier drivers starting Sep 12.
Flexible hours, $25-30/delivery. Interested?"
```

### Option D: Word of Mouth (Fastest)
```
Text/call everyone you know:
- "Know any reliable drivers? We're hiring medical couriers for Sep 12.
  $25-30/delivery, flexible. Can you recommend someone?"
  
Ask them to share with their network.
```

**Target:** Get applications by 2 PM today, interview by 3-4 PM, confirm 3 drivers by EOD

**Success Criteria:**
- [ ] Posts made to 2-3 channels (Facebook, Craigslist, LinkedIn)
- [ ] 5+ applications received by 2 PM
- [ ] Phone interviews completed (15 min each)
- [ ] 3+ drivers confirmed + phone numbers collected
- [ ] All have valid licenses (ask them to confirm)
- [ ] All available Sep 12 morning (confirm in writing)

**Vetting Questions (During Phone Interview):**
1. "How long have you been driving?" → (At least 5 years clean record)
2. "Do you have a reliable vehicle?" → (Yes = good, "can use one" = OK)
3. "Any traffic violations in last 2 years?" → (Should be NO)
4. "Can you start Thursday morning?" → (Must be YES)
5. "Are you comfortable with HIPAA training?" → (Should be YES/willing)

---

## 📋 TASK 2: PREPARE PROSPECT LIST + PHONE NUMBERS

**TASK:** Write down top 10 prospects + their phone numbers + specimen volumes

**Do this now:**
1. Open: `calls/LT-005-FINAL-CALL-LIST.csv`
2. Print first 10 rows (WakeMed through Pitt County Memorial)
3. Write phone numbers on paper or in phone's notes app
4. Write specimen volumes next to each name
5. Highlight their "pain signal" column (what problem they have)

**Prospect List (COPY THIS):**

```
1. WAKEOMED, Raleigh — [PHONE: get from CSV] — 500+ specimens/day
   → Pain: Major system, compliance audits
   
2. ATRIUM HEALTH, Charlotte — [PHONE] — 500+ specimens/day
   → Pain: Multiple hospitals, vendor consolidation
   
3. NOVANT HEALTH, Charlotte — [PHONE] — 400+ specimens/day
   → Pain: Temperature control, specimen rejections
   
4. DUKE HEALTH, Durham — [PHONE] — 400+ specimens/day
   → Pain: Research labs, complex compliance
   
5. UNC HEALTH, Chapel Hill — [PHONE] — 300+ specimens/day
   → Pain: Multiple departments, inconsistency
   
6. CONE HEALTH, Greensboro — [PHONE] — 200-300 specimens/day
   → Pain: Multiple campuses, courier coordination
   
7. VIDANT HEALTH, Eastern NC — [PHONE] — 200-300 specimens/day
   → Pain: Regional solution, not national carrier
   
8. IREDELL HEALTH, Statesville — [PHONE] — 100-150 specimens/day
   → Pain: Small system, overpaying
   
9. CAPE FEAR VALLEY, Fayetteville — [PHONE] — 100-150 specimens/day
   → Pain: Growth phase, scaling logistics
   
10. PITT COUNTY MEMORIAL, Greenville — [PHONE] — 100-150 specimens/day
    → Pain: New director, implement best practices
```

**Success Criteria:**
- [ ] All 10 names written down (paper or phone)
- [ ] All phone numbers recorded
- [ ] Specimen volumes noted (for discovery)
- [ ] Pain signals highlighted

---

## 🗣️ TASK 3: READ + PRACTICE COLD CALL SCRIPT

**TASK:** Learn the cold call opener so you can say it naturally tomorrow

**What to do:**
1. Read entire `scripts/LT-005-SALES-COACH.md` (20 minutes)
2. Read the COLD CALL CARD above (10 minutes)
3. Practice the opener OUT LOUD 5 times:

```
"Hi [Name], this is [You] with HealthRoute Medical Courier. 
I'm calling because we help medical labs move specimens fast and safely—
HIPAA-compliant, real-time tracking, temperature-controlled transport.
Do you have 2 minutes?"
```

4. Practice responding to these 3 objections OUT LOUD:
   - "We use UPS"
   - "Cost is a concern"
   - "Let me check with the lab director"

**Success Criteria:**
- [ ] Opener memorized (can say naturally, not robotic)
- [ ] Discovery questions written down (for reference during calls)
- [ ] 3 key objection responses memorized
- [ ] Script feels comfortable (not overly polished, authentic)

**Tip:** Confidence comes from repetition. Practice the opener while:
- Driving
- Showering
- Walking
- Waiting for coffee
- Throughout the day

By tomorrow 8 AM, you should be able to say it without thinking.

---

## ✅ TASK 4: VERIFY STRIPE + SUPABASE ARE READY

**TASK:** Confirm payment system works + database is prepared

**Stripe Check:**
1. Log in to: https://dashboard.stripe.com
2. Verify:
   - [ ] You're logged in as the correct account
   - [ ] You see "HealthRoute" or similar account
   - [ ] Payment methods are active (credit card processing on)
   - [ ] Webhook for order notifications is set up
3. Take screenshot of dashboard (proof)

**Supabase Check:**
1. Log in to: https://app.supabase.com
2. Navigate to: `lt_005_customers` table
3. Verify:
   - [ ] Table exists and is accessible
   - [ ] Columns present: `id`, `name`, `phone`, `email`, `address`, `specimen_volume`
   - [ ] Table is empty (ready for new records)
4. Repeat for: `lt_005_orders` and `lt_005_revenue_log` tables

**LT-011 Dispatch Integration:**
1. Verify endpoint: `https://lt-011-dispatch-software.vercel.app/api/routes/optimize`
2. Expected: Returns route optimization data
3. If you get 404 or error: Note it (can use manual routing as backup)

**Success Criteria:**
- [ ] Stripe account active + payment methods on
- [ ] Supabase tables accessible + ready
- [ ] LT-011 API endpoint working (or noted as backup plan)

---

## 📞 TASK 5: PHONE + ENVIRONMENT PREP

**TASK:** Physical setup for calls tomorrow morning

**Phone Prep:**
- [ ] Charge phone overnight (full battery by 8 AM)
- [ ] Disable notifications during calls (silent mode)
- [ ] Test speaker phone (volume OK?)
- [ ] Install or open: Notes app (for call tracking)
- [ ] Save all 10 prospect phone numbers in contacts

**Environment Prep:**
- [ ] Find quiet room for calls (no background noise)
- [ ] Have notepad + pen next to phone
- [ ] Have 2-3 bottles of water ready (hydration = better calls)
- [ ] Have script + objection handlers printed out (as backup)

**Mindset Prep:**
- [ ] Read "YOUR MANTRA" below 3 times
- [ ] Get 8 hours sleep tonight
- [ ] No alcohol tonight (clear head tomorrow)
- [ ] Light breakfast tomorrow (8 AM start needs fuel)

**Success Criteria:**
- [ ] Phone 100% charged by 8 AM
- [ ] Quiet space identified for calls
- [ ] All 10 prospects saved to phone contacts
- [ ] Notepad + pen ready on desk

---

## YOUR MANTRA (Read This 3 Times)

```
I'm not selling a courier service.

I'm solving their compliance risk + helping them serve patients faster.

Most labs have had at least one HIPAA scare.

I'm the solution to that scare.

Lead with that.

The rest flows.
```

---

## BACKUP PLANS (If Something Goes Wrong Today)

**If drivers can't be recruited by 2 PM:**
- Continue recruiting through evening (expand to more Facebook groups, Craigslist, LinkedIn)
- Call local temp agencies (day labor firms often have drivers)
- Do manual deliveries yourself if needed (can start with 2 drivers instead of 3)
- Worst case: Start delivery operations on Sep 12-13 (staggered timeline)

**If you can't reach prospects tomorrow:**
- Leave voicemail: "Hi [Name], this is [You] from HealthRoute. I'll call back tomorrow at [TIME]. If you want to reach me: [YOUR PHONE]"
- Call again Thursday + Friday
- Send email with one-pager as backup

**If Stripe doesn't work:**
- Use manual payment (ACH transfer or check)
- Trial customers don't need payment day 1 anyway
- Fix Stripe by Day 2

**If you freeze up on first call:**
- That's normal. Make the call anyway.
- After first call, you'll feel way more confident
- Second call will be easier
- By call 5, you'll be in a groove

---

## FINAL CHECKLIST (By 5 PM Today)

- [ ] Driver recruitment posts made (2-3 channels)
- [ ] 3+ drivers recruited + confirmed available
- [ ] Top 10 prospects written down + phone numbers recorded
- [ ] Cold call script read + opener practiced 5 times
- [ ] Stripe + Supabase verified working
- [ ] Phone charged + contacts saved
- [ ] Quiet space identified for tomorrow
- [ ] Got 8 hours sleep planned for tonight
- [ ] Read the MANTRA above 3 times
- [ ] Confidence level: 8/10+ (should feel ready, not nervous)

---

## TOMORROW MORNING (Sep 11, 7:55 AM)

**5 Minutes Before First Call:**
1. Open notepad on phone
2. Pull up first prospect (WakeMed)
3. Read opener one more time (out loud)
4. Take 3 deep breaths
5. Dial

**During Each Call:**
1. Write down: Name + Title + Volume + Response (interested/objection/voicemail/declined)
2. If interested: Get email + best time to call back
3. If objection: Get enough info to send follow-up
4. If voicemail: Leave message + move to next prospect

**After Each Call:**
1. Mark outcome in notes
2. Move to next prospect
3. Repeat 10-15 times

**By 12 PM:**
- 10+ calls made
- Results documented
- At least 1-2 prospects interested (target)

---

**Go time: Sep 11, 8:00 AM 🚀**

You've got this. Recruit drivers independently. Make the calls. Report back Friday with revenue.

