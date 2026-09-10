# LT-005: WEEK 1 EXECUTION PLAN (Sep 10-15, 2026)
**Status:** 🚀 READY TO EXECUTE  
**Authority:** CP-021 (Revenue), Revenue Division  
**Revenue Target:** $1,700-$7,500 (conservative: $2-3K, upside: $5-7.5K)

---

## THREE HIGHEST-LEVERAGE ACTIONS

### 🎯 ACTION #1: DRIVER RECRUITMENT (TODAY - Sep 10)
**Timeline:** 2-3 hours  
**Owner:** Revenue operations lead or ops coordinator  
**Blocker Status:** CRITICAL PATH (no drivers = no deliveries)  

#### What to Do:
```
Contact: OPS-STAFF-001 recruiting system
Request: 3 drivers needed by Sep 12 (Thu morning)
Requirements:
  - Valid driver's license (verified)
  - Vehicle preferred (own car or company vehicle)
  - Clean driving record
  - Flexible availability (part-time OK)
  - HIPAA training willing (2 hours)

Recruitment Flow:
1. Send request to OPS-STAFF-001 ops contact
2. They post opportunity to their network
3. Candidates apply within 24 hours
4. Screen candidates (phone call, 15 min each)
5. Offer positions to top 3
6. Schedule onboarding for Sep 12 (morning)

Talking Points for OPS-STAFF-001:
"We're launching medical courier service. Need 3 flexible drivers
for same-day medical specimen delivery (short routes, higher pay).
If they do well, can scale to full-time. Can you help us recruit?"
```

#### Success Criteria:
- [ ] 3 drivers recruited by Sep 12, 8 AM
- [ ] All have valid licenses + clean records
- [ ] All available for Sep 12-15 (trial period)
- [ ] Compliance onboarding scheduled (2 hours)

**If OPS-STAFF-001 can't deliver by Sep 12:** Plan B is manual recruitment (Facebook groups, Craigslist, LinkedIn, referrals) — takes 1-2 days.

---

### 🎯 ACTION #2: TOP 10 PROSPECT PRIORITIZATION (TODAY - Sep 10)
**Timeline:** 30 minutes  
**Owner:** Sales lead (you)  
**Status:** Ready to go

#### Tier-0 Targets (Call First):

| Rank | Facility | Contact | Phone | Volume | Confidence |
|------|----------|---------|-------|--------|------------|
| 1 | WakeMed, Raleigh | Lab Director | [SEE CSV] | 500+ specimens/day | 85% |
| 2 | Atrium Health, Charlotte | Lab Operations | [SEE CSV] | 500+ | 85% |
| 3 | Novant Health, Charlotte | Lab Operations | [SEE CSV] | 400+ | 84% |
| 4 | Duke Health, Durham | Lab Director | [SEE CSV] | 400+ | 85% |
| 5 | UNC Health, Chapel Hill | Lab Operations | [SEE CSV] | 300+ | 84% |
| 6 | Cone Health, Greensboro | Lab Operations | [SEE CSV] | 200-300 | 83% |
| 7 | Vidant Health, Eastern NC | Lab Operations | [SEE CSV] | 200-300 | 82% |
| 8 | Iredell Health System, Statesville | Lab Director | [SEE CSV] | 100-150 | 82% |
| 9 | Cape Fear Valley, Fayetteville | Lab Director | [SEE CSV] | 100-150 | 81% |
| 10 | Pitt County Memorial, Greenville | Lab Operations | [SEE CSV] | 100-150 | 81% |

**Why These 10:**
- All have 100+ specimens/day (makes economics work)
- Lab directors/operations managers (decision makers)
- HIPAA-aware institutions (compliance pain is relevant)
- Geographically concentrated (NC focus, reachable routes)
- High confidence scores (85%+ for top 5)

#### Call List Preparation:
```bash
# Extract phone numbers from CSV
cat calls/LT-005-FINAL-CALL-LIST.csv | head -11 | tail -10 | \
  awk -F',' '{print $2 " — " $1 " (" $6 ")"}'
```

**Write down on paper or phone:**
- [ ] All 10 names written down
- [ ] Phone numbers + contact titles
- [ ] Specimen volumes noted (for discovery questions)
- [ ] Pain signals highlighted (delays, compliance, costs)

---

### 🎯 ACTION #3: COLD CALL SCRIPT + TALKING POINTS (TODAY - Sep 10)
**Timeline:** 30 minutes (reading/preparation)  
**Owner:** You (sales lead)  
**Status:** Script ready in `scripts/LT-005-SALES-COACH.md`

#### Quick Reference Script:

**OPENER (15 seconds):**
```
"Hi [Name], this is [You] with HealthRoute Medical Courier. 
I'm calling because we help medical labs move specimens fast and safely—
HIPAA-compliant, real-time tracking, and temperature-controlled transport.
Do you have 2 minutes?"
```

**DISCOVERY QUESTIONS (if they say yes):**
1. "How many specimens do you process daily?" → *Determines service level*
2. "What's your geographic service area?" → *Route complexity*
3. "Who do you currently use for courier services?" → *Current solution*
4. "How often do you experience delays?" → *Quantifies pain*
5. "Have you had any HIPAA compliance audits?" → *Triggers compliance pain*

**VALUE PROP (if they show interest):**
```
"Most labs use generic couriers that don't understand specimen handling.
They delay, don't maintain temp control, can't prioritize STAT orders.
We specialize in medical specimens: HIPAA-certified, real-time tracking,
climate-controlled vehicles, full liability insurance. Results: zero compliance gaps
+ faster turnaround + happier doctors."
```

**TRIAL OFFER (if they're interested):**
```
"Let me make this easy: 5 free trial deliveries. You absorb $0 risk.
We'll do 5 pickups + deliveries this week, prove the quality, then you decide.
If you like it, we can set up recurring service ($1K-5K/month depending on volume).
Can we do the trial starting Thursday?"
```

**OBJECTION: "We use UPS / generic courier"**
```
Response: "Many labs do. The issue: generic couriers don't understand specimen
handling. They delay, they don't maintain temp control, can't prioritize STAT orders.
How often do you have delayed results with your current courier?"
```

**OBJECTION: "Cost is a concern"**
```
Response: "I get it. But one lost patient due to delayed results costs you $5K
in referral value. One HIPAA violation can cost $100K+. Our service is insurance
against that. Plus, do the math: if we reduce your delays by 50%, how much would
that be worth in patient satisfaction + referrals?"
```

**CLOSE:**
```
"Great. I'm going to send you a one-page overview of what we offer, plus
pricing based on your volume. Can I get your email? [Get email]
I'll also call back Tuesday to see if you have questions. Does that work?"
```

#### Preparation Checklist:
- [ ] Read entire script (10 min)
- [ ] Practice opener (2 min, out loud)
- [ ] Highlight your 3 key pain signals (compliance, speed, quality)
- [ ] Write down 3 responses to "cost is a concern"
- [ ] Have first 10 prospects written down + phone numbers ready
- [ ] Have notepad for notes during calls

---

## TIMELINE: SEP 10-15

### TODAY (Sep 10)
- [ ] **Morning:** Contact OPS-STAFF-001, start driver recruitment
- [ ] **Afternoon:** Prepare prospect list (top 10), write down phone numbers
- [ ] **Evening:** Read full script + practice opener
- [ ] **By EOD:** 3 drivers recruited (target), cold call script memorized

**Success Metric:** Drivers confirmed by EOD, script ready

---

### TOMORROW (Sep 11) — DAY 1: COLD CALLS
- [ ] **8:00 AM:** Make first 10 calls to Tier-0 prospects
- [ ] **Target:** Get 1-2 "yes" for trial
- [ ] **Outcome Log:** For each call, note:
  - Prospect name + response (interested / objection / voicemail / declined)
  - Volume confirmed (or estimated)
  - Next step (send quote / follow up / add to "later" list)
- [ ] **EOD:** Review call results, identify which prospect is most likely for trial

**Success Metric:** 8+ calls connected, 1-2 prospects interested in trial

---

### SEP 12 (Thu) — DAY 2: DRIVER ONBOARDING + FOLLOW-UP CALLS
- [ ] **Morning:** Driver onboarding (compliance training, vehicle check, route familiarization)
- [ ] **Afternoon:** Follow up with "interested" prospects from Sep 11
- [ ] **Action:** Send customized quote to interested prospects
- [ ] **Calls:** 10+ more calls to remaining prospects on list

**Success Metric:** Drivers ready for deliveries, 3-5 prospects with quotes sent

---

### SEP 13 (Fri) — DAY 3: TRIAL SETUP + PITCH
- [ ] **Morning:** Call top "interested" prospect, pitch trial
- [ ] **Offer:** "Free 5 deliveries this weekend/early next week to prove quality"
- [ ] **Action:** If yes: Get facility contact info (pickup/dropoff addresses, hours)
- [ ] **Afternoon:** Continue calling remaining prospects (10+ calls)

**Success Metric:** 1 trial agreement (target), 5+ proposals sent

---

### SEP 14 (Sat/Sun) — DAY 4: TRIAL EXECUTION (if applicable)
- [ ] **If trial prospect said yes:**
  - Driver makes 5 trial deliveries
  - Proof of delivery collected (photos, signatures)
  - Temperature logs documented
  - Customer satisfaction check (phone call)
- [ ] **If no trial yet:**
  - Continue calling remaining prospects (finish list)
  - Follow up on proposals sent (5+ follow-up calls)

**Success Metric:** First 5 trial deliveries completed, customer satisfied (4.5+/5)

---

### SEP 15 (Sun/Mon) — DAY 5: CONVERSION
- [ ] **Action:** Call trial customer, pitch weekly contract
- [ ] **Offer:** "How many deliveries/week? Let's set up recurring service"
- [ ] **Target:** Secure $1,100/week contract (10 deliveries @ $110)
- [ ] **Backup:** If trial not done yet, continue cold calling (10+ new calls)

**Success Metric:** First recurring customer (trial converted), $1,100/week MRR confirmed

---

## WEEK 1 REVENUE FORECAST

```
Sep 11-12: Prospecting ($0 revenue, 1-2 interested)
Sep 13-14: Trial Deliveries ($550, 5 × $110)
Sep 15+: First Recurring Contract ($1,100/week)

Week 1 Total: $1,650-$2,200 (conservative)
Upside (3-4 customers): $5,000-$7,500
```

---

## BLOCKING ISSUES & MITIGATION

| Blocker | Impact | Mitigation |
|---------|--------|-----------|
| **Drivers not recruited by Sep 12** | Can't execute deliveries | Manual recruitment via FB/LinkedIn/referrals (adds 1-2 days) |
| **0 prospects say "yes"** | No trial to execute | Pivot to email outreach + longer sales cycle (Oct revenue instead) |
| **Prospect needs 2-4 weeks to decide** | Slow sales cycle | Offer trial to de-risk decision ("just 1 week, free") |
| **Stripe checkout fails** | Can't collect money | Manual payment (ACH transfer) or invoice + payment terms |
| **LT-011 dispatch API is down** | Can't optimize routes | Manual routing (spreadsheet) until API restored |

---

## NEXT STEPS (Action Items for TODAY)

### By 5 PM Sep 10:
1. ✅ **Driver Recruitment:** Contact OPS-STAFF-001, send request
2. ✅ **Prospect List:** Write down top 10 + phone numbers
3. ✅ **Script Preparation:** Read + practice LT-005 script
4. ✅ **Stripe Verification:** Log in to Stripe, confirm payment methods active
5. ✅ **Supabase Check:** Confirm `lt_005_customers` table is ready for data entry

### By 8 AM Sep 11:
1. ✅ **Call Readiness:** Phone charged, notepad ready, first 10 prospects written down
2. ✅ **Script Fresh:** Re-read opener, have it word-for-word ready
3. ✅ **Mindset:** This is a trial → if first 5 calls don't connect, call 5 more

---

## SUCCESS CHECKPOINTS

| Checkpoint | Date | Target | Evidence |
|----------|------|--------|----------|
| **Driver Recruitment** | Sep 10 EOD | 3 drivers confirmed | Text confirmation from OPS-STAFF-001 |
| **First Call Batch** | Sep 11 EOD | 10+ calls, 1-2 interested | Handwritten notes + count |
| **Trial Agreement** | Sep 12-13 | 1 prospect says "yes" | Prospect name + trial start date confirmed |
| **Trial Execution** | Sep 13-14 | 5 deliveries completed | Driver notes + photos |
| **Trial Conversion** | Sep 15 | Convert to $1,100/week contract | Stripe charge successful |
| **Week 1 Revenue** | Sep 15 EOD | $1,650+ | Stripe dashboard shows payments |

---

## CRITICAL SUCCESS FACTOR

**Discipline.** Make 10+ calls per day Sep 11-14. Most will be "no" or voicemail. That's normal (80% conversion rate is no from voice, yes from persistence). Expect:
- 10 calls/day
- 8 connect (80% reach rate)
- 1-2 interested (20% conversion)
- 0-1 trial agreement (50% of interested)

If first day yields 0 interested: DON'T PIVOT. Call 5 more. It's a numbers game.

---

**Confidence Level:** 80% ($2-5K revenue Week 1)  
**Go-Live:** Sep 11, 8:00 AM 🚀  
**Report Back:** Sep 15, 5 PM (revenue update)

