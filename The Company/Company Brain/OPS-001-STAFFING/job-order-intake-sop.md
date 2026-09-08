# Job Order Intake SOP — OPS-001 Staffing

**Purpose:** Document a new job opening and trigger the matching algorithm  
**Owner:** OPS-001 Staffing Manager  
**Success:** Every job order received → matching results sent to employer within 24 hours  
**Form:** Zapier form or voice intake (transcribed to form fields)

---

## INTAKE CHECKLIST — CAPTURE ALL FIELDS

**When you receive a job order (from cold call, email, or inbound form), create a new record with:**

### REQUIRED FIELDS (Deal-breakers if missing)

| Field | Format | Rules | Examples |
|-------|--------|-------|----------|
| **Job Title** | Text | Actual role name, not generic "worker" | "Journeyman Electrician", "HVAC Technician", "Licensed Plumber" |
| **Company Name** | Text | Legal name + DBA if applicable | "ABC HVAC Contractors", "Smith Electrical Services" |
| **Pay Range** | Number range | Hourly ($) or annual salary ($) | "$28–$35/hr" or "$60K–$70K/yr" |
| **Work Type** | Dropdown | W2 (employee) / 1099 (contractor) / Contract | W2, 1099, or Contract |
| **Must-Haves** | Text (comma-separated list) | Licenses, certifications, experience, equipment requirements | "NC license, 5+ yrs exp, own tools, valid DL" |
| **Start Date** | Date | ASAP or specific date | "Sept 15", "ASAP (within 2 weeks)", "Oct 1" |
| **Hiring Manager Name** | Text | First & last name | "John Smith" |
| **Hiring Manager Phone** | Phone | Direct phone (not receptionist) | "+1-828-555-1234" |
| **Hiring Manager Email** | Email | Direct email | "john@abchvac.com" |

### RECOMMENDED FIELDS (Improve matching)

| Field | Format | Notes |
|-------|--------|-------|
| **Job Description** | Text | Role duties, day-to-day tasks (helps sales follow-up) |
| **Interview Process** | Text | What steps? In-person, phone screen, skills test? How long? | "1 phone screen, 1 in-person, tool allowance test" |
| **Equipment Provided** | Text | Does company provide tools or must candidate have own? | "Provide all hand tools, candidate brings DL only" |
| **Travel Required** | Yes/No | Does role require travel? | "Yes, 10% local, 5% regional" |
| **Shift/Hours** | Text | 9-5, on-call, rotating, nights? | "7am–5pm M–F, on-call weekends" |
| **Typical Candidate Age** | Text | Optional; for context only (never discriminate) | "Experienced (10+ yrs)" |
| **Bonus Qualifications** | Text | Nice-to-haves, not deal-breakers | "Experience with smart thermostats", "Bilingual Spanish" |

---

## FORM SUBMISSION PROCESS

### Via Zapier Form: "OPS-001 Job Order Intake"

**Step 1: Open Zapier Form**  
URL: [Insert Zapier form link here or create shortlink]

**Step 2: Fill Required Fields**  
- Do NOT submit incomplete job orders (required fields = deal-breakers)
- If hiring manager won't give phone/email, call back tomorrow (escalate as "[Company] - No Direct Contact")

**Step 3: Submit Form**  
- Zapier auto-creates record in Supabase `venture_leads` table
- Triggers MCP microservice `run_matching_algorithm()` (see [After Intake](#after-intake) below)

### Via Voice Intake (e.g., phone call mid-conversation)

**If you capture job order details verbally:**
1. Jot down all required fields in meeting notes
2. Transcribe to Zapier form within 1 hour (while fresh)
3. Submit same as above

---

## FIELD VALIDATION RULES

**BEFORE submitting:**

| Field | Validation | If Invalid | Action |
|-------|-----------|-----------|--------|
| **Job Title** | Not null, not generic ("worker", "staff") | User sees error; cannot submit | Re-prompt: "What's the exact job title?" |
| **Pay Range** | Numeric, min < max, both > $0 | User sees error; cannot submit | Re-prompt: "Is that $28–$35/hr or $65K–$75K/year?" |
| **Work Type** | One of: W2, 1099, Contract | User sees error; cannot submit | Re-prompt with dropdown |
| **Must-Haves** | At least 1 item (comma-separated or bullet) | User sees warning; can submit with acknowledgment | Prompt: "Are there really no deal-breakers?" |
| **Start Date** | Valid date (YYYY-MM-DD) or "ASAP" | User sees error; cannot submit | Re-prompt: "Sept 15 or ASAP?" |
| **Hiring Manager Phone** | Valid format: +1-(XXX)-XXX-XXXX | User sees warning; can submit | Prompt: "Please double-check this number" |
| **Hiring Manager Email** | Valid email format | User sees warning; can submit | Prompt: "Please double-check this email" |

**Validation Logic (in Zapier form settings):**
- Mark fields REQUIRED (with red asterisk): Job Title, Company, Pay Range, Work Type, Must-Haves, Start Date, Hiring Manager (Name + Phone + Email)
- Format: Phone field = [Phone] type (auto-formats), Email field = [Email] type (auto-validates)
- Conditional: If Work Type = "1099", show "Note: No benefits, candidate is independent contractor"

---

## AFTER INTAKE — NEXT ACTIONS (AUTOMATIC + MANUAL)

### AUTOMATIC: Zapier Workflow Triggers

**Immediately after form submission:**

**Action 1: Trigger MCP Microservice**
```
Zapier Trigger: Form Submission
├─ Call: OmniRoute /api/matching_algorithm
├─ Payload: [Job Title, Must-Haves, Pay Range, Start Date, Company]
└─ Timeout: 30 sec (if longer, queue async job)
```

**Action 2: Slack Notification to ops-001 channel**
```
Message:
"🎯 NEW JOB ORDER
Company: [Company Name]
Role: [Job Title]
Pay: [Pay Range]
Start: [Start Date]
Matching algorithm running... check Zapier dashboard for results in ~15 min"
```

**Action 3: Add to ClickUp (OPS-001 → "Job Orders" folder)**
```
Task Name: "[Company] — [Job Title] [$Pay]"
Assigned to: Matching Algorithm Agent
Status: "Matching In Progress"
Due: [Tomorrow, 2pm] (24-hour SLA for sending candidates)
Priority: High if Start Date = ASAP; Medium if 2+ weeks out
```

### MANUAL: You Send Template Email (Next Day, 2pm)

**If matching found 3+ qualified candidates:**

Subject: `[Company] — Qualified Candidates for [Job Title] Ready to Interview`

```
Hi [Hiring Manager Name],

We received your job order for [Job Title] yesterday. Great news—we found 3 qualified candidates 
who match your must-haves:

[CANDIDATE 1]
  • [Years] years exp in [trade]
  • [Key cert/skill]
  • Available: [Start date or ASAP]

[CANDIDATE 2]
  • [Years] years exp
  • [Key cert/skill]
  • Available: [Start date or ASAP]

[CANDIDATE 3]
  • [Years] years exp
  • [Key cert/skill]
  • Available: [Start date or ASAP]

Next step: You pick which candidate(s) to interview. We'll send you their full resume 
and contact info once you confirm interest.

Ready to move forward? Reply to this email or call me at [Your Phone].

— [Your Name]  
Worldwidebro Staffing  
[Your Phone]
```

---

## ESCALATION RULES — If Matching Fails

### Scenario 1: Zero Matching Candidates Found (0/50+ candidate pool)

**Action (SAME DAY, within 2 hours):**
1. **Call hiring manager back** (don't email—this is an emergency)
   > "Hi [name], we ran our matching algorithm and hit a gap. Help me refine: 
   > [Must-Have 1] is mandatory, right? What if we relaxed that to [alternative]?"

2. **Offer alternatives:**
   - Reduce years-of-experience requirement by 2–3 years (pair with senior candidate for first week)
   - Relax certification requirement if candidate has equivalent experience
   - Widen start date window ("This week" → "Within 2 weeks")
   - Expand geographic radius (local → regional)

3. **If still zero after refinement:**
   - Mark as "Candidate Gap — Future Sourcing" in ClickUp
   - Add to OPS-001 outbound call list (passive sourcing for future match)
   - Email hiring manager: "We'll keep sourcing. Expected availability: [2 weeks / 1 month]"

### Scenario 2: Only 1–2 Candidates (Below Target of 3+)

**Action (SAME DAY):**
1. Send what you have with note:
   > "[Candidate 1] is a strong match. We're sourcing 2–3 more to give you options. 
   > Expect full list by [tomorrow, 5pm]."

2. Fast-track additional sourcing:
   - Post to OPS-001 internal candidate pool
   - Reach out to passive candidates from previous roles (message: "Hey, similar role just opened...")
   - Contact trade school alumni networks, union training centers

---

## SUCCESS CRITERIA (JOB ORDER INTAKE PHASE)

| Metric | Target | Notes |
|--------|--------|-------|
| **Form Completion Time** | 2–3 min | Includes all required fields, no incomplete submissions |
| **24-Hour Turnaround** | 100% of orders | Matching results emailed within 24h of order |
| **Candidate Match Rate** | 3–5 per order | Average number of qualified candidates per job |
| **Employer Response Rate** | 30–40% | % of employers who reply to candidate email within 48h |
| **Interview Scheduling** | 60–70% of replies | % of positive responses that convert to scheduled interview |
| **Escalation Clearance** | <2 hours | Time to resolve "zero matches" via refinement call |

---

## TEMPLATES & LINKS

**Zapier Form Link (OPS-001 Job Order Intake):**  
[Copy this link: https://zapier.com/...] ← Replace with actual form URL

**Slack Channel:**  
#ops-001-staffing

**ClickUp Folder:**  
OPS-001 → Job Orders

**Supabase Table:**  
`venture_leads` (records created automatically)

**MCP Microservice Endpoint:**  
`OmniRoute /api/matching_algorithm` (auto-called on form submit)

