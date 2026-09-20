# ACE Construction & Contracting OS (CON-001)
## Commercial GC & Developer Outbound Prospecting Engine
**Target Audience:** VPs of Preconstruction, Chief Estimators, Senior Project Managers at Top NC Commercial General Contractors  
**Core Offer:** Rapid Turnkey Commercial Subcontracting & 48-Hour CSI MasterFormat Takeoff Feasibility  
**Distance-to-Cash Strategy:** $299 Pre-Con Scope Audit & Intake (100% credited toward construction contract)

---

## 1. Phone Prospecting (Cold Calling Playbook)

### Opening & Hook (First 15 Seconds)
> **Rep:** "Hi `{{contact_name}}`, this is `{{rep_name}}` with ACE Construction & Contracting here in North Carolina. I know you're likely in plan reviews, so I'll keep this under 45 seconds. We provide commercial trade contracting and automated 48-hour CSI Division 09 framing, drywall, and interior tenant improvement scoping. The reason for my call is to ask: are you currently looking for responsive, pre-vetted trade coverage on any upcoming commercial or medical TI bids in `{{hq_city}}`?"

### Value Proposition (If Prospect Shows Interest / "What do you do?")
> **Rep:** "We know estimating bandwidth is the biggest bottleneck in Q4. For active projects, we review your architectural plan set and turn around a complete CSI MasterFormat takeoff with verified unit pricing, OSHA 1926 safety plans, and 100% verified COI insurance inside of 48 hours. We also have active crews ready to mobilize across Charlotte and Raleigh."

### The $299 Low-Friction Offer (Intake Consultation)
> **Rep:** "Rather than trading cold emails, we offer commercial GCs a **$299 Pre-Construction Scope & Feasibility Audit**. We review your drawings, identify scope gaps or code anomalies, and deliver a detailed P10/P50/P90 cost and schedule model. If you award us the subcontract or project package, that $299 is credited 100% right back to you on mobilization."

### Handling Objections

#### Objection 1: "We already have our own subcontractors / stable trade partners."
> **Response:** "Understood—we don't ask you to replace your primary subs. But almost every GC we speak with in `{{hq_city}}` has had at least one drywall or framing sub drop out or bid 30% over budget on a tight deadline. Would it hurt to keep us on your secondary bid list as a verified backup so you have competitive coverage on your next RFP?"

#### Objection 2: "Just send me an email with your info."
> **Response:** "Happy to do that, `{{contact_name}}`. What's the best email for you? Also, so I don't send generic marketing fluff: are you mostly bidding medical office TI, retail, or industrial warehouse right now?" *(Logs trade preferences, sends Touch 1 immediately)*.

#### Objection 3: "We're not bidding anything right now."
> **Response:** "Got it. When is your next cycle of project releases expected? We can sync back up 2 weeks prior so your estimating team has our pre-qualification package and COI on file."

---

## 2. 3-Touch Email Campaign

### Touch 1: Day 1 — The Capability & Capacity Intro
**Subject:** Subcontractor trade coverage & capacity for `{{company_name}}`  
**To:** `{{email}}`  

Hi `{{contact_name}}`,

Hope your project sites across `{{hq_city}}` are moving along smoothly.

I noticed `{{company_name}}`'s active pipeline in `{{primary_sector}}`. As commercial deadlines tighten into Q4, several preconstruction teams have asked us for reliable trade coverage in:
- **CSI Division 09:** Light-gauge metal stud framing, drywall, Level 5 finishing, acoustical ceilings.
- **Commercial Tenant Improvements:** Medical clinics, corporate office buildouts, and retail refits.
- **Turnkey Speed:** 48-hour takeoff turnarounds with full MasterFormat unit-cost leveling.

All ACE crews carry active $1M/$2M General Liability, full Workers' Comp, and strict OSHA 1926 compliance.

Do you have any open bid packages or RFPs this month where an extra competitive number would help `{{company_name}}`?

Best regards,

**ACE Construction & Contracting Operations**  
Charlotte & Raleigh, NC  
Direct: (704) 555-0199 | Bids: estimating@aceconstruction.com  
Portal: https://con-001-ace-construction.vercel.app/services  

---

### Touch 2: Day 4 — The 48-Hour Plan Takeoff & Scope Audit ($299 Offer)
**Subject:** 48-hour plan takeoff for your upcoming `{{hq_city}}` bids  
**To:** `{{email}}`  

Hi `{{contact_name}}`,

Quick follow-up to my note earlier this week.

If your estimating team is buried in plan sets, we offer a streamlined **Pre-Construction Scope & Feasibility Audit**:
1. You share your digital plan set or conceptual sketches.
2. Inside **48 hours**, our estimating team returns an itemized CSI takeoff with material/labor breakouts and P10/P50/P90 cost risk modeling.
3. If `{{company_name}}` contracts with us for the scope, our $299 intake fee is credited 100% back on your first draw.

You can upload drawings directly or schedule a 15-minute scope review here:  
👉 **[Schedule Pre-Con Scope Review](https://con-001-ace-construction.vercel.app/booking/consultation)**

Would Thursday or Friday afternoon work for a quick 5-minute introductory call?

Best,

**ACE Commercial Estimating Team**  

---

### Touch 3: Day 9 — The Breakup / Quick Trade Question
**Subject:** Permission to close your file for Q4?  
**To:** `{{email}}`  

Hi `{{contact_name}}`,

I haven't heard back, so I assume you have full subcontractor coverage lined up for `{{company_name}}`'s current pipeline.

I'll take you off our follow-up list for now. If you ever run into a sub default, schedule crunch, or need a fast, bonded backup bid on commercial framing, drywall, or interior fit-outs anywhere in North Carolina, feel free to submit the RFP to `estimating@aceconstruction.com`.

Wishing you and your project superintendents a safe, profitable quarter.

Best regards,

**Commercial Preconstruction Director**  
ACE Construction & Contracting LLC  

---

## 3. LinkedIn InMail / Message Sequences

### InMail to VP of Preconstruction / Chief Estimator
**Subject:** Trade capacity in `{{hq_city}}` for `{{company_name}}`  
> Hi `{{contact_name}}`, saw `{{company_name}}`'s impressive work across `{{primary_sector}}` in the Carolinas. We operate ACE Construction & Contracting OS—delivering 48-hour turnarounds on commercial CSI Division 09 framing/drywall takeoffs and turnkey interior buildouts with verified COIs. Are you accepting trade pre-qualification packages for your upcoming bid list? Let's connect.

---

## 4. Operational Tracking & CRM Protocol

1. **Daily Cadence:** 25 cold calls / 50 emails sent daily from `DATA/prospects/nc_commercial_gcs.csv`.
2. **Response SLAs:** Any incoming reply or drawing submission must receive a response within **15 minutes**.
3. **Escalation Trigger:** If a GC requests a bid, immediately trigger `src/app/api/ai/estimate/route.ts` to generate preliminary takeoff bounds.
4. **Deposit Collection:** Direct all early-stage clients to `/booking/consultation` for upfront $299 capture via Stripe.
