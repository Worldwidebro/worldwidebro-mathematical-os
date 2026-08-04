# Real Estate OS — Phase 1 GTM Playbook
**Status:** Ready for Week 1 execution  
**Owner:** Sales + Founder  
**Success Gate:** 3 beta customers signed by Week 8, $0 MRR, Series Pre-Seed pipeline warm by Q4 2026  

---

## Phase 1 Strategy (8 Weeks)

**Mission:** Acquire 3 property manager beta customers, establish market feedback loop, build Series Pre-Seed credibility.

**Channels:**
1. **Direct Warm Outreach** (primary) → 3 closures from ~10 targeted PMs
2. **Community Events** (secondary) → NCAA/ARPM speaking, lead capture
3. **Content + LinkedIn** (foundation) → Blog, organic pipeline for Phase 2

**Investment:** $30K payroll (CTO $15K, Sales $7K, Marketing $5K, CFO $3K) + $5K marketing spend (events, ads) = **$35K total for 8 weeks**

---

## Week-by-Week Execution Calendar

### **WEEK 1: Foundation** (Founder + CTO)

**Sales:**
- [ ] List 10 warm prospect PMs (referrals, chamber, LinkedIn connections)
- [ ] Draft outreach email (template below)
- [ ] Set up Airtable CRM: columns = [Name, Email, Phone, Properties, Warm/Cold, Stage, Last Contact, Next Step]
- [ ] Create landing page draft (Carrd or one-pager)

**Product:**
- [ ] CTO hired or committed
- [ ] MVP scope locked: property + tenant + rent payment + maintenance request
- [ ] Stripe test keys configured
- [ ] Supabase project spun up (re-os-beta)

**Marketing:**
- [ ] LinkedIn profile updated (founder): add "Building RE-OS" to headline
- [ ] 3 blog post drafts queued (see calendar below)

**Finance:**
- [ ] CFO (contractor) onboarded
- [ ] Financial model built (payroll, burn, runway to Pre-Seed)
- [ ] Stripe + Supabase cost projections

**Metrics Setup:**
- [ ] Create Supabase table: `gtm_leads` (id, name, email, phone, properties, channel, stage, created_at, converted_at)
- [ ] Create `gtm_metrics` (week, outreach_sent, calls_scheduled, demos_completed, beta_signups, revenue, churn)

---

### **WEEK 2: Outreach Launch** (Founder + Sales Hire Starts)

**Sales:**
- [ ] Send 10 outreach emails (warm list from Week 1)
- [ ] Log in Airtable: who replied, who ignored, follow-up date
- [ ] Schedule 5-7 discovery calls for Week 3-4
- [ ] Sales hire starts (Week 2): onboarding, CRM training, call shadowing

**Product:**
- [ ] MVP code started (property CRUD + Stripe link)
- [ ] Test Stripe rent payment flow locally

**Marketing:**
- [ ] Post 1: "Why Property Managers Hate Spreadsheets" (Substack/LinkedIn)
- [ ] LinkedIn: Comment on 10 APM/NCAA posts (engagement signal)
- [ ] Join NCAA + ARPM (check eligibility, membership fee)

**Metrics:**
- [ ] Week 1 outreach: 10 emails, log open rates (UTM tracking on reply)
- [ ] Update Airtable: stage = "Outreach Sent" for all 10

---

### **WEEK 3: Demo + Event Planning** (Founder + Sales)

**Sales:**
- [ ] Conduct 5 discovery calls (30 min each, use script below)
- [ ] Demo live to 2-3 best-fit prospects (MVP or clickable prototype)
- [ ] Close 1-2 for beta signup (goal: first customer by end Week 3)
- [ ] Plan NCAA speaking slot (6-min demo + Q&A)

**Product:**
- [ ] MVP feature-complete (basic): property, tenant, rent payment button, maintenance list
- [ ] Tenant invite email (onboarding sequence)
- [ ] Dashboard skeleton (overview, rent paid %, maintenance tickets)

**Marketing:**
- [ ] Post 2: "Rent Collection: Spreadsheets vs. Automated" (LinkedIn article)
- [ ] Start email sequence (Mailchimp/Substack): welcome → feature preview → case study

**Metrics:**
- [ ] Discovery calls conducted: 5 (log in Airtable: stage = "Demo Scheduled")
- [ ] Demo completion: 3 (log: stage = "Demo Completed")
- [ ] Conversion rate so far: 0/3 (expected, early stage)

---

### **WEEK 4: First Closed Deal + Hiring** (Founder + Sales + CTO)

**Sales:**
- [ ] Close first beta customer (sign LOI, email invite, property setup call)
- [ ] Send 10 more outreach emails (expand list, add referral follow-ups)
- [ ] Schedule 5 more discovery calls for Week 5-6
- [ ] Marketing hire starts (Week 4): content calendar, email, events coordination

**Product:**
- [ ] Deploy MVP to staging (Vercel + Supabase beta project)
- [ ] First customer imports 1 property + adds 2 test tenants
- [ ] Test rent payment (Stripe test mode) with customer

**Marketing:**
- [ ] Marketing hire begins: review blog drafts, refine LinkedIn strategy
- [ ] Post 3: "Maintenance Requests: Stop Playing Phone Tag" (LinkedIn)
- [ ] NCAA speaking slot confirmed (Week 6, 15-min slot)

**Hiring:**
- [ ] CTO: Equity doc signed (3–5%, 4-year vest, 1-year cliff)
- [ ] Sales hire: Offer extended, start date Week 4–5
- [ ] Marketing hire: Job posting live (contract or part-time, Week 4 start)
- [ ] CFO (1099): Bookkeeping process live, financial dashboard in Sheets/Airtable

**Metrics:**
- [ ] Beta customers: 1 (Stage = "Active Beta")
- [ ] Outreach: 20 emails sent cumulative
- [ ] Conversion rate (emails → demo): 25% (5 demos from 20 emails)
- [ ] Conversion rate (demo → signup): 20% (1 signup from 5 demos)

---

### **WEEK 5-6: Momentum + Events** (Full team)

**Sales:**
- [ ] Conduct 5 more discovery calls (target 1-2 closures)
- [ ] First customer feedback call (Week 5): "What's working? What's broken?"
- [ ] Attend NCAA chapter meeting (Week 6, demo + booth presence)
- [ ] Close 2nd beta customer (goal: 2 of 3 secured by end Week 6)

**Product:**
- [ ] First customer rent payment live (real Stripe transaction or test)
- [ ] Maintenance ticket workflow tested with customer feedback
- [ ] Bug fixes based on customer input

**Marketing:**
- [ ] Event booth set up (NCAA meeting): laptop, collateral, email signup sheet
- [ ] LinkedIn: Series of 5 posts about "property mgmt" pain points (1 per day Week 5)
- [ ] Email sequence: Feature release to list ("Rent Payment Reminders Now Live")
- [ ] Content: Post 4–5 queued (webinar invite, case study template)

**Hiring:**
- [ ] All three hires onboarded (CTO, Sales, Marketing)
- [ ] Weekly standup: Founder, CTO, Sales, CFO (30 min, Mon 10am)

**Metrics:**
- [ ] Beta customers: 2 (target: 2 of 3)
- [ ] NCAA event: 30–50 attendees, 15–20 email captures
- [ ] Email list: 40–60 subscribers
- [ ] LinkedIn followers: 100–150
- [ ] Demo conversion: 2 of 5 new calls = 40% (trending up)

---

### **WEEK 7: Closing Sprint** (Full team)

**Sales:**
- [ ] 3rd customer target: focus on 3 most-qualified prospects from Weeks 2-5
- [ ] Final outreach: phone calls (not just email) to close 3rd by end of week
- [ ] Beta LOI template finalized (includes data security, feedback expectations, NDA if needed)
- [ ] Close 3rd beta customer (goal: ALL 3 secured by Week 7, testing Week 8)

**Product:**
- [ ] Full product test with first 2 customers: rent payments, maintenance tickets, reporting
- [ ] Onboarding video (5 min, Loom) deployed to welcome email
- [ ] Dashboard v1 live: rent collected YTD, overdue payments, open maintenance tickets

**Marketing:**
- [ ] 2nd event attended (local ARPM meeting or property manager networking event)
- [ ] Blog: Publish case study #1 (anonymized) = "How [PM Name] Cut Rent Collection Time from 4 Hours to 30 Min"
- [ ] LinkedIn: Announce beta cohort launch (3-post series: why we built, who we're helping, apply here)
- [ ] Email: NPS survey sent to first 2 customers (just feedback, no revenue yet)

**Metrics:**
- [ ] Beta customers: 3 (GOAL ACHIEVED)
- [ ] Cumulative outreach: 30+ emails, 10+ calls
- [ ] Website traffic: 200–300 visits (Google Analytics)
- [ ] Email list: 80–100 subscribers
- [ ] Demo-to-close rate: 3 of 10 demos = 30% (on target)

---

### **WEEK 8: Stabilization + Fundraising Prep** (Full team + Advisors)

**Sales:**
- [ ] All 3 customers fully onboarded: properties imported, tenants invited, first payment attempt
- [ ] Weekly check-in calls scheduled (Weeks 8, 12, 16 for 8-week feedback loop)
- [ ] Warm intros to 5 micro-VC investors + angel PM networks (via advisors)

**Product:**
- [ ] Feature freeze (no new features, bug fixes only)
- [ ] Production Stripe keys live (if any customers paying processing fees or later)
- [ ] Feedback survey live (Google Form or Typeform): 5–7 questions on pain points, features, pricing willingness

**Marketing:**
- [ ] 3 testimonial video requests sent to beta customers (2-min Loom clips)
- [ ] Blog: Publish 2 more posts (educational, ongoing LinkedIn push)
- [ ] Email: Send feature update (based on early feedback) to list

**Fundraising:**
- [ ] Pitch deck drafted (see outline below)
- [ ] Investor list built: 10 targets (3 angels, 3 micro-VCs, 4 APM/industry angels)
- [ ] Warm intro requests sent via advisors
- [ ] First investor call scheduled (Week 9)

**Metrics:**
- [ ] Beta customers: 3 (all active, all onboarded)
- [ ] Feature usage: Track property additions, rent payments, maintenance tickets
- [ ] NPS: Collect from 3 customers (expect 20–50 range, directional only)
- [ ] Churn: 0% (free beta, no revenue risk, but engagement matters)
- [ ] Cost per acquisition: $30K payroll ÷ 3 customers = **$10K CAC** (okay for beta, optimize in Phase 2)
- [ ] Investor pipeline: 5–7 warm intros confirmed for Week 9–10

---

## Sales Playbook

### Outreach Email Template

**Subject Line:** "Free property management tool for [PM Name]" OR "Feedback wanted: 15 min?"

**Body:**
```
Hi [Name],

I know the grind—spreadsheets for rent tracking, tenant calls at 6pm, manual maintenance follow-ups.

We built RE-OS to fix that. Takes 10 minutes to set up a property, zero training needed.

I'm not selling anything (it's free through end of year for beta testers), but I'd love your feedback on the workflow.

Would you be open to a quick 15-min call next week to see if it fits how you work?

[Your Name]
[Phone]
[Link to landing page or calendar]
```

**Cadence:**
- Day 1: Initial email
- Day 3: If no reply, follow-up 1 (same thread)
- Day 7: Follow-up 2 ("Last try")
- Day 14: Archive or add to nurture list

---

### Discovery Call Script (30 min)

**Warm-up (2 min):**
> "Thanks for getting on the call. No hard sell today—just want to understand your workflow and see if RE-OS might help."

**Qualification (8 min):**
1. "How many properties do you manage?"
2. "How many people are on your team?"
3. "Walk me through how you currently collect rent—what tool, what's the process?"
4. "What's your biggest pain point with rent collection or tenant communication?"
5. "Do you track maintenance requests? How?"

**Demo (10 min):**
- Screen share: Live product walk-through (property setup → add tenant → send rent request → maintenance ticket)
- Ask: "Does this look like how you work?"
- Answer 1-2 clarifying questions

**Close (10 min):**
1. "What would make this a no-brainer for you?"
2. Listen for objections (integrations, data security, etc.)
3. If interested: "Can we get you set up as a beta tester? You'd try it free through Q4, give us feedback every 2-3 weeks, and help us build what PMs actually need."
4. If not: "Thanks for the feedback—stay in touch, we'll have pricing updates in Jan."
5. Next step: "I'll send you the setup link, onboarding call is 20 min next Tuesday. Sound good?"

**Note:** Log everything in Airtable immediately after call.

---

### Beta LOI (Letter of Intent)

**Template (1 page):**

```
RE-OS BETA TESTING AGREEMENT

This agreement is between [Customer Name] ("Beta Tester") and [Your Company] ("Company").

1. TERM: August 2026–December 2026 (free access through end of year)

2. OBLIGATIONS:
   - Beta Tester will import at least 1 property, add 1+ tenant, test rent payment workflow
   - Beta Tester will provide feedback via 3 check-in calls (Week 2, Week 4, Week 8)
   - Beta Tester will complete 1 NPS/satisfaction survey

3. COMPANY OBLIGATIONS:
   - Company provides free access to all features (no charge for 8-week beta)
   - Company commits to bug fixes and major feature additions based on feedback
   - Company provides email/phone support (24-hour response time)

4. DATA SECURITY:
   - All data encrypted in transit and at rest
   - No data shared with third parties without consent
   - Data deleted upon request

5. CONFIDENTIALITY:
   - Beta Tester may discuss with peers; Company may use testimonials with permission

6. SIGNATURES:
   Beta Tester: _________________ Date: _______
   Company: ____________________ Date: _______
```

**Delivery:** Email as PDF, request e-signature (DocuSign or simple email reply).

---

## CRM Setup (Airtable + Supabase Sync)

### Airtable Schema

**Table: `gtm_leads`**
| Field | Type | Notes |
|-------|------|-------|
| Name | Text | |
| Email | Email | |
| Phone | Phone | |
| Properties | Number | How many they manage |
| Company | Text | PM firm name |
| Channel | Select | Direct / NCAA / LinkedIn / Referral / Inbound |
| Stage | Select | Prospect / Outreach Sent / Call Scheduled / Demo Completed / Negotiating / Beta Signed / Onboarded / Churned |
| Last Contact | Date | |
| Next Step | Text | e.g., "Send demo link" |
| Notes | Long text | Call notes, objections, etc. |
| Created | Date | Auto-stamp |
| Converted | Checkbox | If they signed LOI |

**Table: `gtm_metrics` (weekly rollup)**
| Field | Type | Notes |
|-------|------|-------|
| Week | Number | 1–8 |
| Outreach Sent | Number | Total emails |
| Calls Scheduled | Number | Discovery calls booked |
| Demos Completed | Number | Actual demo calls |
| Beta Signups | Number | LOI signed |
| Revenue | Currency | $0 for beta (track for Phase 2) |
| Churn | Number | Customers who went inactive |
| Notes | Text | Blockers, wins |

### Supabase Sync (Zapier/Make workflow)

**Trigger:** Airtable row updated → **Action:** Update Supabase `gtm_leads` table

**Why:** Single source of truth; analytics queries can pull from Supabase for dashboards.

---

## Pricing Recommendation

**DECISION: Free Beta (Phase 1) → Usage-Based (Phase 2)**

### Phase 1 (Now–Q4 2026)
- **Free tier:** Unlimited properties, unlimited maintenance requests, rent payment tracking (Stripe processing fees apply: 2.2% + $0.30 per transaction)
- **Commitment messaging:** "Free through December 2026; pricing TBD based on feedback from beta testers"
- **Why:** Adoption > Revenue at this stage; customer feedback loop is the real asset

### Phase 2 (Jan 2027+)
**Pricing Model: Landlord-Centric Usage-Based**

| Tier | Price | Included | Target |
|------|-------|----------|--------|
| **Starter** | $15/mo | Up to 5 properties, rent collection, maintenance, basic reporting | Solo PMs (1–5 units) |
| **Pro** | $29/mo | Unlimited properties, advanced reporting, tenant portal customization, 2 team seats | Growing PMs (6–50 units) |
| **Enterprise** | Custom | White-label, API access, dedicated Slack support, custom integrations | Multi-manager firms (50+ units) |

**Processing Fees:** 2.2% + $0.30 per rent payment transaction (Stripe pass-through; we keep none)

**Math for LTV/CAC:**
- Average PM: 15 properties, $800/mo in rents
- Monthly rent transactions: 15 × $800 = $12,000/mo
- Processing revenue: 2.2% + $0.30 × N = ~$264/mo
- Subscription revenue (Pro tier): $29/mo
- Total MRR per PM: $293/mo
- 12-month LTV: ~$3,500
- CAC (Phase 1): $10K → LTV:CAC = 0.35x (acceptable for venture, will improve in Phase 2)

---

## Hiring Plan + Equity Structure

### CTO / Lead Engineer

**Hire Timeline:** Week 1–2 (immediate, core to MVP delivery)

**Responsibility:**
- MVP architecture (Supabase + Next.js + Stripe)
- 6-week delivery timeline (Weeks 1–6)
- Technical hiring (2nd engineer by Week 8)
- Infrastructure + deployment

**Salary:** $15K (3 months, $180K ARR equivalent)  
**Equity:** 3–5% (4-year vest, 1-year cliff, standard SAFE)  
**Onboarding:** Week 1 (Day 1: repo walkthrough, tech stack, MVP scope)

**Job Description:**
```
Senior Engineer / CTO — RE-OS (Fullstack)
Early-stage SaaS for property managers. Lead technical decisions.
Requirements:
- 5+ yrs fullstack (React, Node, SQL)
- Product-minded (ship features, not just code)
- Stripe + Supabase experience preferred
- Comfortable with autonomous work (solo for first 6 weeks)
Equity: 3–5% · Salary: $15K for first 3 months
```

---

### Sales / CRO

**Hire Timeline:** Week 4–5 (after initial outreach, hire to scale)

**Responsibility:**
- Direct outreach (emails, calls)
- Event coverage (NCAA, ARPM meetings)
- Customer onboarding + relationship management
- CRM management (Airtable)
- Deal closing (LOI, contract)

**Salary:** $7K (3 months, $84K ARR equivalent, commission-eligible Phase 2)  
**Equity:** 1–2% (4-year vest)  
**Onboarding:** Week 4 (shadow founder calls Week 4–5, own calls by Week 6)

**Job Description:**
```
Sales / Customer Success Lead — RE-OS
Acquire first 3 beta customers and nurture them through Q4.
Requirements:
- 2+ yrs SMB/SaaS sales or customer success
- Property management or construction background (preferred, not required)
- Comfortable cold outreach + relationship building
- Event networking skills
Salary: $7K for first 3 months + commission (TBD) · Equity: 1–2%
```

---

### Marketing / Growth

**Hire Timeline:** Week 6–7 (content, events, brand)

**Responsibility:**
- Content creation (blog, LinkedIn, email)
- Event coordination (NCAA speaking, networking)
- Landing page + website updates
- Lead nurture (email sequences)
- Analytics + reporting

**Salary:** $5K (3 months, contract or part-time, $30K ARR equivalent)  
**Equity:** 0.5–1% (4-year vest, if full-time; none if contract)  
**Onboarding:** Week 6 (start content calendar immediately)

**Job Description:**
```
Marketing / Growth Lead — RE-OS
Build brand and content to support beta acquisition and Phase 2 launch.
Requirements:
- 2+ yrs marketing or content creation (SaaS preferred)
- Strong LinkedIn presence or blog portfolio
- Event planning + speaking coordination experience
Salary: $5K for first 3 months (contract/part-time, flexible) · Equity: 0.5–1%
```

---

### CFO / Finance (Contractor)

**Hire Timeline:** Week 1 (immediately, for financial model + fundraising)

**Responsibility:**
- Bookkeeping + P&L
- Financial model (payroll, burn, runway)
- Series Pre-Seed financial package (cap table, projections)
- Fundraising support

**Fee:** $3K (1099, 3 months, or $4K/mo retainer Phase 2)  
**Equity:** None (contractor, but option pool reserved)

---

### Equity Vesting Terms (Standard)

- **Vesting:** 4-year total, 1-year cliff (clawed back if they leave before 1 year)
- **Exercise window:** 10 years after departure
- **Strike price:** $0.01/share (409A valuation TBD, likely $500K–$1M pre-seed valuation)
- **Vesting schedule:** 1/48 per month after cliff

**Example:** CTO with 4% equity
- Month 0–12: Vest 0%, cliffed (if leave at month 11, lose all)
- Month 12: Cliff vests 1% (12 months ÷ 4 years)
- Month 12–48: Vest 1% per month
- Month 48: 100% vested

---

## Marketing Calendar (Week 2–8)

### Blog Post Schedule

| Week | Title | Angle | Length | Channel |
|------|-------|-------|--------|---------|
| 2 | Why Property Managers Hate Spreadsheets | Pain point validation | 800 words | Substack + LinkedIn |
| 3 | Rent Collection: Spreadsheets vs. Automated | Education + comparison | 1000 words | Substack + LinkedIn article |
| 4 | Maintenance Requests: Stop Playing Phone Tag | Pain point (maintenance) | 800 words | Substack + LinkedIn |
| 5 | How to Collect Rent on Time (Every Time) | Actionable | 1000 words | Substack + website blog |
| 6 | Case Study: How [PM Name] Cut Collection Time 75% | Social proof (anonymized) | 1200 words | Substack + LinkedIn article |
| 7 | The Hidden Cost of Spreadsheet Property Mgmt | ROI/financial angle | 900 words | Substack + LinkedIn |
| 8 | What We Learned from 100 Property Managers | Research/credibility | 1000 words | Website blog + LinkedIn |

### LinkedIn Content (2x per week)

**Week 2–3:** Problem validation
- "What's your biggest property management headache?" (poll)
- Repost NCAA/ARPM content (show community involvement)

**Week 4–5:** Education + engagement
- "Rent collection benchmarks: How long does it take you?" (engagement)
- Article: "Why spreadsheets fail property managers"

**Week 6–7:** Social proof + buzz
- "Excited to announce our beta cohort—3 amazing PMs trying RE-OS"
- Testimonial teaser: "Here's what [PM] said about their first week"

**Week 8:** Positioning for Phase 2
- "Announcing our Series Pre-Seed funding push"
- Call to action: "Join 100+ PMs on our waitlist" (set up email signup link)

### Email Sequences (Mailchimp/Substack)

**Sequence 1: New Subscriber Welcome (Trigger: Email signup)**
- Email 1 (Day 0): Welcome + value prop + link to landing page
- Email 2 (Day 3): Blog post #1 + case study
- Email 3 (Day 7): Feature overview (video walkthrough)
- Email 4 (Day 14): Early beta access (if spot available)

**Sequence 2: Cold List Nurture (Separate list, triggered after demo)**
- Email 1: "Enjoyed our call—here's the demo link"
- Email 2 (Day 3): Feature benefit reminder + case study
- Email 3 (Day 7): Customer testimonial (once available)
- Email 4 (Day 14): "Last chance to join beta cohort"

---

## Success Metrics Dashboard (Week 1–8)

### Weekly Reporting (Every Friday)

| Metric | Target W8 | Tracking | Source |
|--------|-----------|----------|--------|
| **Acquisition** | | | |
| Outreach emails sent | 30+ | Airtable (cumulative) | |
| Discovery calls scheduled | 10+ | Airtable (stage: "Call Scheduled") | |
| Demos completed | 10 | Airtable (stage: "Demo Completed") | |
| Beta customers signed | 3 | Airtable (stage: "Beta Signed") | LOI count |
| **Engagement** | | | |
| Email list subscribers | 100+ | Mailchimp open rate tracker | |
| LinkedIn followers | 300+ | LinkedIn analytics | |
| Website visits | 500+ | Google Analytics | |
| Blog posts published | 5–6 | Website + Substack | |
| **Conversion** | | | |
| Email → call rate | 50%+ | (Calls ÷ emails sent) | Airtable |
| Demo → close rate | 30% | (3 closes ÷ 10 demos) | Airtable |
| Time to close | <4 weeks | (LOI date – first contact) | Airtable |
| **Product** | | | |
| Properties onboarded | 5+ | Supabase count | |
| Tenants invited | 15+ | Supabase count | |
| Rent payments tested | 3+ | Stripe test mode + production | |
| **Financial** | | | |
| Payroll spend | $30K | Finance tracker (CFO) | |
| Burn rate | $4–5K/week | $30K ÷ 8 weeks | |
| CAC (cumulative) | $10K/customer | $30K payroll ÷ 3 customers | |
| Revenue | $0 | (Beta = free) | —|

### Dashboard Setup (Supabase + Google Sheets)

**Query 1: Weekly Lead Summary**
```sql
SELECT 
  stage, 
  COUNT(*) as count
FROM gtm_leads
WHERE created_at > NOW() - INTERVAL '1 week'
GROUP BY stage;
```
→ Embed in weekly Slack report

**Query 2: Conversion Funnel**
```sql
SELECT 
  'Prospect' as stage, COUNT(*) as count FROM gtm_leads WHERE stage IN ('Prospect', 'Outreach Sent')
UNION ALL
SELECT 'Call Scheduled', COUNT(*) FROM gtm_leads WHERE stage = 'Call Scheduled'
UNION ALL
SELECT 'Demo Completed', COUNT(*) FROM gtm_leads WHERE stage IN ('Demo Completed', 'Negotiating')
UNION ALL
SELECT 'Beta Signed', COUNT(*) FROM gtm_leads WHERE stage IN ('Beta Signed', 'Onboarded');
```
→ Weekly metric report

**Google Sheets:** Public dashboard pulling Supabase queries + LinkedIn/Google Analytics data for founder visibility.

---

## Series Pre-Seed Fundraising (Weeks 6–12)

### Pitch Narrative (2 min)

> "There are 50,000 independent property managers in the US managing $300B+ in residential real estate. They're stuck on spreadsheets, manual rent chasing, and maintenance chaos. RE-OS automates rent collection, tenant communication, and maintenance tracking—delivering recurring software revenue at $15–30/property/month.
>
> We're closing our first 3 beta customers in Q4 2026 with 40% feature adoption. We're raising $50K pre-seed to scale to 50 customers and $50K MRR by Q2 2027, with a path to $500K MRR nationally."

### Investor Targets (Weeks 8–12)

**Tier 1: Angel Property Managers (3–5 investors)**
- Existing PM customers (convert to angels)
- ROI: 10–20x if product hits (own the product early)
- Check size: $5–25K typical
- Approach: Direct call after Week 6 beta traction

**Tier 2: Micro-VC Funds ($25–100K checks)**
- Lerer Hippeau (NYC, SMB SaaS)
- Greycroft (NYC, SaaS + fintech)
- Plug & Play (Silicon Valley, SaaS accelerator)
- Foundry (Charlotte, regional focus)
- Approach: Warm intro via advisor (Week 8)

**Tier 3: PM Industry Angels (2–4 investors)**
- Retired/semi-retired PMs with exit experience
- NC/SC network via ARPM/NCAA
- Approach: Referral from beta customers (Week 6–7)

### Pitch Deck Outline

**Deck structure (12–15 slides):**

1. **Title slide:** RE-OS | Property Management for the 21st Century
2. **Problem:** 50,000 PMs stuck on spreadsheets, losing revenue
3. **Market size:** TAM $600M (50K PMs × $12K/yr SaaS spend), SAM $50M (Carolinas)
4. **Solution:** 3-minute demo walkthrough (rent collection, maintenance, reporting)
5. **Traction:** 3 beta customers, 40% feature adoption, testimonial quote
6. **Business model:** Usage-based + subscription ($15–30/mo)
7. **Unit economics:** $3,500 LTV, $1K CAC (Phase 2), 42-month payback
8. **Team:** Founder + CTO + Sales lead (photos + brief bios)
9. **Roadmap:** Phase 2 (Jan–Mar 2027): 50 customers, $50K MRR
10. **Financials:** 3-year pro forma (conservative growth)
11. **Ask:** $50K pre-seed for product, sales, marketing (burn: $4K/week)
12. **Use of funds:** Payroll ($30K), marketing ($10K), ops ($10K)
13. **Closing:** "Help us help 10,000 PMs over the next 5 years"

**Deliverables:** Figma deck (30 min to build), PDF export, 2-min video demo

### Warm Intro Request Email (to advisors/angels)

**Template:**
```
Hi [Advisor],

We're raising $50K for RE-OS (property management SaaS) and I'd like a warm intro to [Investor Name] at [Fund].

Quick context:
- Closing 3 beta customers this month (10K PMs addressable market)
- $15–30/property/mo SaaS model
- Raising for product + sales to hit 50 customers by Q2 2027

Would you be comfortable making an intro?

[Your Name]
[Deck attached]
```

---

## Execution Priorities (Week 1 Blockers)

**MUST DO (No excuses):**
1. ✓ Create Airtable CRM (Week 1, 30 min)
2. ✓ Hire CTO (Week 1–2, MVP builds on this)
3. ✓ Send 10 outreach emails (Week 2, Day 1)
4. ✓ Conduct 5 discovery calls (Week 3)
5. ✓ Close 1 beta customer (Week 3–4)
6. ✓ Deploy MVP to staging (Week 4)
7. ✓ Close 3 customers total (Week 7)

**NICE TO HAVE (if time allows):**
- Blog posts (Week 2–3 is early, OK to delay if sales need founder)
- LinkedIn content (secondary to direct outreach)
- Event speaking (good traction play, but sales is primary)

**RED FLAGS (stop if detected):**
- MVP not feature-complete by Week 4 (re-scope, add contractor engineer)
- Zero calls scheduled by Week 3 (revisit outreach list quality, not quantity)
- Conversion rate below 20% by Week 5 (sales playbook needs refinement)

---

## Weekly Standup Template (15 min, Mondays 10am)

**Attendees:** Founder, CTO, Sales, CFO

**Format:**
1. **Wins (2 min):** What shipped? Customer activity?
2. **Blockers (3 min):** Product, hiring, customer roadblocks
3. **This week (5 min):** Weekly goals + DRIs assigned
4. **Metrics (5 min):** Review dashboard (leads, demos, closes)

**Example Week 3 standup:**
```
Wins: Close discovery calls, first demo completed
Blockers: Stripe test keys not working (CTO to debug Day 2)
This week: Conduct 5 demos (Sales), deploy payment flow (CTO), publish blog post (Founder)
Metrics: 10 emails → 5 calls scheduled, 1 demo done, 0 closes yet (on pace for Week 4)
```

---

## Wrap-Up: What Success Looks Like (Week 8)

✅ **Product:**
- MVP deployed, 3 customers onboarded, first rent payment tested
- Dashboard showing: 5 properties, 15 tenants, 3 rent payments tracked
- Bug-free enough for light production use

✅ **Sales:**
- 3 beta customers signed LOI
- 30+ outreach emails, 10 discovery calls, 3 closures = 30% close rate (good for warm leads)
- CRM fully managed in Airtable, no data loss

✅ **Marketing:**
- 100+ email subscribers (Mailchimp/Substack)
- 5–6 blog posts published (ongoing SEO value)
- 300+ LinkedIn followers, 500+ website visits
- 1–2 testimonial videos queued for fundraising

✅ **Team:**
- CTO, Sales, Marketing hired + onboarded
- CFO financial model built, $30K payroll tracked
- Weekly standups running, communication clear

✅ **Fundraising:**
- Pitch deck drafted
- 10 investor targets identified
- Warm intros requested (5–7 pending)
- First investor calls scheduled Week 9–10

**Next Phase (Week 9+):** Investor meetings, Phase 2 scope (paid pricing, 20-customer target, $10K MRR)

---

## Quick Reference: Critical Docs + Folders

| Artifact | Owner | Location | Status |
|----------|-------|----------|--------|
| Airtable CRM | Sales | airtable.com/app/[workspace] | Live Week 1 |
| Supabase DB (re-os-beta) | CTO | supabase.com | Live Week 1 |
| Landing page | Founder | Carrd or custom domain | Live Week 1 |
| Pitch deck | Founder | Figma | Draft Week 6, final Week 8 |
| Financial model | CFO | Google Sheets | Live Week 1 |
| Marketing calendar | Marketing | Notion/Airtable | Live Week 4 |
| GitHub repo (MVP) | CTO | github.com/[org]/re-os | Private, shared with team |

---

**Status:** Ready to execute.  
**Last updated:** Phase 1 kickoff  
**Next review:** Week 4 (halfway checkpoint)
