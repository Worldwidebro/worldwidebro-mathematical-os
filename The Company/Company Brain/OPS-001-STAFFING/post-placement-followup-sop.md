# Post-Placement Follow-Up SOP — OPS-001 Staffing

**Purpose:** Ensure placements succeed + measure satisfaction + identify upsell opportunities  
**Owner:** OPS-001 Staffing Manager  
**Timeline:** Day 1 → Week 1 → Week 4 → Month 1 (ongoing)  
**Success Metric:** 80%+ employer satisfaction, 30%+ repeat placement rate

---

## TIMELINE & TEMPLATES

### DAY 1 (Candidate's First Day) — Congratulations Email

**Send to:** Hiring Manager email (from cold call job order)  
**Timing:** End of business Day 1 (5–6pm)  
**Subject:** `[Candidate Name] started today — How's it going?`

```
Hi [Hiring Manager Name],

Great to hear [Candidate Name] started this morning! 

Quick question: how's the first day going? One simple 5-star rating helps us know 
if we nailed the match:

👉 RATE THIS PLACEMENT (click one):
  ⭐⭐⭐⭐⭐ Perfect match — everything we hoped
  ⭐⭐⭐⭐ Good fit — minor adjustments needed
  ⭐⭐⭐ It's working out
  ⭐⭐ Concerns starting to surface
  ⭐ Major issues — we need to talk

If you rated 3 or below, reply to this email or call me immediately: [Your Phone]

Either way, I'll check back in one week. Looking forward to a great placement!

— [Your Name]  
Worldwidebro Staffing  
[Your Phone]
```

**Track:** Log Day 1 rating in Supabase `placement_ratings` table (auto-log via Zapier email integration)

---

### WEEK 1 (5 business days after start) — Check-In Call

**Scenario A: 5-star or 4-star rating**
```
Call timing: Tuesday or Wednesday (1 week in, after first Monday crunch)
Call length: 5 min (keep it light—they're busy)
Opening:
  "Hi [name], it's [your name] from Worldwidebro. Just wanted to check in — 
   how's [candidate] settling in?"

Listen for:
  ✓ "Great, no issues" → Thank them, move to Week 4 follow-up
  ✓ "Good overall, but X is different than expected" → Problem-solve verbally 
    (e.g., training, onboarding, tool access)
  ✓ "It's okay" → Dig deeper: "What would make it great?" 
    (signals dissatisfaction; probe for fixes)

Closing:
  "I'll check back in 3 weeks to see how things are going. If anything changes, 
   you know where to find me."
```

**Scenario B: 3-star or lower rating**
```
Call timing: SAME DAY or next morning (urgent)
Call length: 10–15 min (this is a save attempt)
Opening:
  "Hi [name], I saw the rating and wanted to make sure we address this right away. 
   What's going on?"

Listen & Diagnose:
  ❌ Candidate is unreliable → "Is [he/she] showing up on time?"
  ❌ Skills mismatch → "Does [he/she] understand the work, or do they need retraining?"
  ❌ Attitude/fit → "Is it a personality thing or capability?"
  ❌ Tools/equipment issue → "Do they have what they need?"
  ❌ Pay/terms → "Did we get the pay right? Clarify expectations?"

Fix or Replace:
  ✓ Minor issue (needs training, equipment):
    → Offer same-day or next-day fix (e.g., "I'll come by with [tool]")
  ✓ Attitude/fit fixable:
    → Offer 48-hour probation with specific behavioral expectations (e.g., "No phone during work")
  ✓ Skills gap real:
    → Offer replacement: "I'll send two alternatives by tomorrow. You pick."
  ✓ Not fixable:
    → Full replacement candidate (no charge for first 48h trial swap)

Escalate if:
  → Employer wants full refund (rare; commit to replacement candidate within 24h)
  → Candidate is in violation of law (safety, discrimination) → Document & terminate immediately

Closing:
  "I'll check back tomorrow to see if [fix] is working. We're committed to getting this right."
```

**Track:** Update Supabase `placement_status` (Active / At Risk / Issue Resolved / Replaced) + notes

---

### WEEK 4 (3.5 weeks after start) — Feedback Summary Email

**Send to:** Hiring Manager  
**Timing:** 4 weeks after start date (same day of week as placement)  
**Subject:** `[Candidate Name] 4-Week Check-In — Performance Summary`

```
Hi [Hiring Manager Name],

It's been 4 weeks since [Candidate Name] joined your team. Great work getting them 
ramped up! Quick summary email:

✅ PERFORMANCE RATING
  Rating: [5-star / 4-star / etc., based on Week 1 call]
  Comments: [1–2 sentence summary of any issues addressed and status]

📊 MONTH 1 WINS
  ✓ Onboarded and productive
  ✓ [Specific accomplishment if you know it, e.g., "completed 12 service calls"]
  ✓ [Another win or "building relationships with team"]

🎯 NEXT STEPS
  → [Candidate] continues in role
  → We'll stay in touch for the next placement

💡 REFERRAL OPPORTUNITY
  Do you know other companies hiring [similar role]? We can also place 
  [Candidate Name]'s former colleagues. Reply with any leads.

---

LET'S TALK NEXT PLACEMENT

Since this placement worked out, let's discuss:
  1. Are you hiring for another [trade/role] in the next month?
  2. Would you like us to staff an entire team? (We can do bulk placements)
  3. Are you open to temp-to-perm for flexibility?

I'll call next week to explore. In the meantime, if you need anything, call me.

— [Your Name]  
Worldwidebro Staffing  
[Your Phone]
```

**Track:** Log in ClickUp as "Placement Satisfied" task; move to "Month 1 Nurture" folder

---

### MONTH 1 (30 days after start) — Upsell Outreach

**Send to:** Hiring Manager  
**Method:** Phone call (preferred) or email (fallback)  
**Timing:** End of Month 1 (30–35 days after start)  
**Duration:** 5–10 min call

**Call Script:**

```
Opening:
  "Hi [name], it's [your name] from Worldwidebro. I wanted to touch base 
   since [Candidate Name] is now a full month in. How's it going?"

Listen to their response (3–5 sec silence—let them talk).

If positive:
  "Awesome! Before we wrap, I wanted to float three things we can help with:

  1️⃣ NEXT HIRE
     Are you looking to hire another [role] in the next 4–6 weeks? We can have 
     candidates ready to start within 48 hours.

  2️⃣ TEMP STAFFING (Seasonal or Project-Based)
     Do you have seasonal peaks (summer, winter) or big projects where you need 
     extra hands? We can staff teams of 3–5 for 2–4 week pushes.

  3️⃣ REFERRAL BONUS
     Know another [trade] shop hiring? Send us a referral and we'll give you 
     $500 credit toward your next placement (if they hire).

Which of these makes sense for you right now?"

If they show interest:
  → [Take order for next hire]
  → [Explain temp staffing model: weekly rates, no long-term commitment]
  → [Get referral names/contact info, follow up with permission]

Closing:
  "Great. I'll follow up [tomorrow/next week] with details. 
   Thanks for the shot at [Candidate Name]—really happy it's working out."
```

**Track:** Log outcomes in ClickUp (`Next Hire Ordered`, `Temp Staffing Inquiry`, `Referral Received`)

---

## TRACKING & MEASUREMENT

### Supabase Tables Used

**`placement_ratings`**
| Column | Type | Notes |
|--------|------|-------|
| placement_id | UUID | Links to original job_order |
| employer_id | UUID | Hiring manager company |
| day_1_rating | INT (1–5) | Day 1 email response |
| week_1_notes | TEXT | Call notes from Week 1 |
| week_4_status | TEXT | "Active", "Issue", "Replaced", "Satisfied" |
| month_1_upsell | TEXT | "Next Hire", "Temp Staffing", "Referral", "None" |
| created_at | TIMESTAMP | Auto |

**`placements`**
| Column | Type | Notes |
|--------|------|-------|
| id | UUID | Primary key |
| candidate_id | UUID | Links to candidate profile |
| employer_id | UUID | Links to company |
| job_order_id | UUID | Links to original order |
| start_date | DATE | First day of work |
| status | TEXT | "Active", "Ended", "Replaced" |
| end_date | DATE | If ended/replaced |

### ClickUp Task Structure

**Task per placement:**
```
Task Name: "[Company] — [Candidate Name] — [Role]"
  • Status: "Day 1 Sent" → "Week 1 Called" → "Week 4 Summary" → "Month 1 Upsell" → "Closed Won"
  • Assignee: You
  • Due Dates:
    - Day 1 Email: [Start Date]
    - Week 1 Call: [Start Date + 5 business days]
    - Week 4 Email: [Start Date + 28 days]
    - Month 1 Call: [Start Date + 30 days]
  • Custom Field: Employer Satisfaction (1–5 rating)
  • Custom Field: Upsell Type (if any)
  • Subtasks:
    ☐ Day 1 email sent
    ☐ Week 1 call completed (notes: [issue status])
    ☐ Week 4 summary sent
    ☐ Month 1 upsell call completed
```

---

## SUCCESS METRICS & TARGETS

| Metric | Target | How to Measure | Action If Below |
|--------|--------|----------------|----|
| **Day 1 Response Rate** | 60%+ | % of employers who reply to Day 1 email | Add phone call follow-up to Day 1 |
| **Week 1 Satisfaction** | 80%+ rated 4–5 stars | Week 1 call feedback | Crisis escalation (see Scenario B above) |
| **Issue Resolution** | 95% | % of Week 1 issues resolved by Week 4 | Fast-track replacement |
| **Repeat Employer Rate** | 30%+ | % who hire again within 3 months | Increase upsell intensity (call earlier, offer temp staffing) |
| **Referral Conversion** | 20%+ | % of referrals that become actual hires | Incentivize referrals ($500 credit model) |
| **Placement Duration** | 60+ days avg | Days before employee quits/is fired | Improve Week 1 issue handling |

---

## QUICK REFERENCE: WHO TO CALL

**Day 1 Issue (candidate didn't show up, major fit problem):**
→ Call hiring manager immediately (don't wait for Week 1)
→ Offer replacement within 24 hours

**Week 1 Issue (3-star or lower):**
→ Call SAME DAY (within 2 hours of receiving rating)
→ Diagnose & offer fix or replacement

**Month 1 Upsell (all looking good):**
→ Call around Week 5 to pitch next hire / temp staffing / referral bonus
→ Timing: Before they forget you exist + while placement is proving value

---

## TEMPLATES AT A GLANCE

| Time | Method | Subject | Key Message |
|------|--------|---------|---|
| **Day 1 (EOD)** | Email | "How's it going?" | 5-star rating link, emergency call line |
| **Week 1** | Phone | N/A (voice) | Listen & troubleshoot OR thank them |
| **Week 4** | Email | "4-Week Check-In" | Performance summary + referral + next hire pitch |
| **Month 1** | Phone | N/A (voice) | Three upsell options (next hire, temp, referral) |

---

## CONTINUOUS RETENTION

**Monthly Employer Newsletter (Optional but Recommended):**
- Send 1x/month to all employers with active placements
- Include: case studies of long-term placements, new services (temp staffing, training), industry news
- Goal: Stay top-of-mind for next hire

**Annual Review (Year 1+):**
- Call employers who placed candidates 12+ months ago
- Ask: "Still happy with [Candidate]? When do you hire again?"
- Pitch: retainer model or volume discount for 5+ placements/year

