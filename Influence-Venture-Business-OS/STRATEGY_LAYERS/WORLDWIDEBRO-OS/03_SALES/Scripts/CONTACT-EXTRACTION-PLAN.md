# Contact Extraction & Lead Mapping System

**Status:** Ready for immediate execution (Path A)  
**Objective:** Extract existing contacts → map to ventures → generate first 50 leads → execute outreach → close deals by 2026-05-23

---

## PHASE 1: CONTACT EXTRACTION (Today - 2026-05-10)

### Contact Sources & Extraction Templates

#### Source 1: LinkedIn (Highest Quality)
**Where to find:** LinkedIn contacts, saved profiles, 2nd degree connections

**Extraction Method:**
1. Go to linkedin.com/mynetwork/invite-friends
2. Download "Manage your connections" → Export CSV
3. Extract key data: First Name, Last Name, Title, Company, Email (if visible)

**Template:**
```
LinkedIn_Contacts.csv
first_name, last_name, headline (title), company, location, url, warmth_score
```

**Quality Indicators:**
- ✅ Headline shows decision-maker title (CEO, Founder, Director, Manager)
- ✅ Company is operating business (not corporate job)
- ✅ Recent activity/mutual connections = warmer lead

---

#### Source 2: Gmail Contacts (Volume)
**Where to find:** google.com/contacts or Gmail sidebar

**Extraction Method:**
1. Go to contacts.google.com
2. Select "More" → "Export"
3. Choose "Google CSV" format
4. Download

**Template:**
```
Gmail_Contacts.csv
name, email, phone, company (from signature parsing), notes (from past emails)
```

**Quality Indicators:**
- ✅ Multiple email threads = higher engagement
- ✅ Company signature in past emails
- ✅ Business email domain (not @gmail.com)

---

#### Source 3: Phone Contacts (Direct)
**Where to find:** iPhone/Mac Contacts app or Android Contacts

**Extraction Method:**
1. Open Contacts app
2. Select all contacts with "groups" or labels
3. Export to CSV or manually note top 20-30 people you'd call

**Template:**
```
Phone_Contacts.csv
full_name, phone, company (if known), warmth_score (1-10 how likely to take call)
```

**Quality Indicators:**
- ✅ You have their personal phone number = warm relationship
- ✅ You've called them in past 6 months
- ✅ They've responded positively before

---

#### Source 4: Past Email Threads & CRM (Context)
**Where to find:** Gmail archive, past deals, client emails

**Extraction Method:**
1. Search Gmail for: "from: [your domain]" + common keywords (proposal, invoice, meeting, etc.)
2. Note: email addresses, company names, project context
3. Identify people you've already worked with or proposed to

**Template:**
```
Email_Archive.csv
contact_name, email, company, project_context, last_interaction_date, deal_stage
```

**Quality Indicators:**
- ✅ Person already said "yes" to conversation with you
- ✅ Existing business relationship = easiest close
- ✅ Recent interaction = freshest relationship

---

#### Source 5: Slack/Discord Communities (Network Edges)
**Where to find:** Industry Slack groups, Discord communities you're part of

**Extraction Method:**
1. Search your communities for people in target sectors
2. Identify: names, roles, company, DM history
3. Note engagement level

**Template:**
```
Community_Contacts.csv
username, real_name (if known), stated_company, industry, community_source
```

**Quality Indicators:**
- ✅ Active in industry-specific channels
- ✅ You've had past conversations
- ✅ Company size/stage matches venture fit

---

## PHASE 2: CONTACT QUALITY SCORING

### Warmth Score (1-10 Scale)

```
SCORE 9-10: IMMEDIATE OUTREACH (Call within 24 hours)
- Existing client or past customer
- Recent positive interaction (within 30 days)
- Explicit interest in your products
- Personal relationship / friend-of-friend with intro

SCORE 7-8: HIGH PRIORITY (Call within 1 week)
- Know them personally or via warm intro
- They're in your target industry/role
- Email/phone contact established before
- Responded positively to past outreach

SCORE 5-6: MEDIUM PRIORITY (Call within 2 weeks)
- Found via LinkedIn/community
- Have their email/phone but no past contact
- They're decision-maker but cold contact
- Industry fit is strong

SCORE 3-4: LOW PRIORITY (Batch outreach)
- Cold contact via email list
- Weak industry fit
- No clear pain point match
- Large company with generic contact

SCORE 1-2: SKIP (Not right fit)
- Wrong industry/role
- No decision-making authority
- Company size not a fit
- Unverified contact
```

---

## PHASE 3: VENTURE-TO-CONTACT MATCHING

### Matching Framework

For each contact, identify 3-5 ventures they should hear about:

```
Contact: John Smith
Title: CEO, Construction Firm
Company: Elite Builders (50 people)
Pain Points: Crew scheduling, invoicing, compliance
Sector Match: CONSTRUCTION
Ventures to Pitch:
  - CON-001: Crew scheduling app (solves pain #1)
  - CON-015: Invoicing automation (solves pain #2)  
  - CON-042: Compliance tracker (solves pain #3)
Warmth: 8
Call Type: "Do you still struggle with..."
```

### Matching Rules

**Rule 1: Job Title → Sector**
- CEO/Founder → All sectors (broad pitch)
- Finance/CFO → Financial services, invoicing ventures
- COO/Operations → All operations ventures
- Sales/Marketing → E-commerce, marketing tech
- Tech/Engineering → Software, tech sector
- HR/People → Staffing, education, training

**Rule 2: Company Size → Venture Stage**
- 1-10 people → Pre-launch, MVP ventures (low-cost, simple)
- 11-50 people → Scaling ventures (moderate complexity)
- 51-200 people → Enterprise ventures (full-featured)
- 200+ people → Mature platform ventures (integration-heavy)

**Rule 3: Industry → Sector Match**
- Construction → Construction sector ventures
- Beauty/salon → Beauty & wellness
- Food/restaurant → Food & hospitality
- Tech startup → Tech & software
- E-commerce shop → E-commerce ventures
- Financial services → Financial sector
- Education → Education ventures

---

## PHASE 4: OUTREACH MESSAGE TEMPLATES

### Template 1: Cold Email (LinkedIn Message)

```
Subject: [Company name] + [Venture] question

Hi [Name],

I noticed you're [running/leading] [company] in [industry].

A lot of [similar role/company size] are struggling with [pain point]. 
We built [venture name] specifically to solve that.

Quick question: Are you currently [experiencing pain point]? 
And who on your team handles [domain]?

I'll send over a short demo video if it's relevant.

[Your name]
```

### Template 2: Warm Email (Referred)

```
Subject: [Referrer name] suggested I reach out

Hi [Name],

[Referrer name] thought you'd be interested in [Venture] because you're working on [project/goal].

I've helped [similar] teams with [specific result]. 
Wondering if a quick call (15 min) would be useful?

Availability: [2-3 specific times]

[Your name]
```

### Template 3: Phone Script (Cold Call)

```
Hi [Name], this is [Your name] with Worldwidebro Holdings. 
I know you're busy—do you have 30 seconds?

I'm calling because you're in [industry], and a lot of [similar roles] 
are dealing with [pain point right now]. 

We built [venture] specifically to fix that. 
Would it make sense to hop on a quick demo call?

[Listen for yes/no]
- YES: "Great! How's Tuesday or Wednesday?" (book 30-min call)
- NO: "Fair enough. Mind if I send you a one-pager anyway?" (email + nurture)
```

### Template 4: ClickUp Founder Intro (WarmIntro)

```
Hi [Contact A] + [Contact B],

[Contact A], you mentioned [business need].
[Contact B], you're running [venture that solves that].

You two should talk. [Contact B] can probably help you with [specific problem].

[Your name]
```

---

## PHASE 5: FIRST 50 LEADS GENERATION

### Target Distribution (By Warmth)
- 10 leads (Score 9-10): Personal network, existing relationships
- 15 leads (Score 7-8): Warm introductions, LinkedIn 2nd degree
- 15 leads (Score 5-6): LinkedIn/community, strong fit
- 10 leads (Score 3-4): Email list, reasonable fit

### Execution Timeline
- **Day 1 (2026-05-09):** Extract all contacts from sources above
- **Day 2 (2026-05-10):** Score contacts + match to ventures
- **Day 3-4 (2026-05-11/12):** Build first 50 leads list + assign outreach type
- **Day 5+ (2026-05-13+):** Begin outreach (5-10 calls/day minimum)

### Success Criteria
- All contacts with Warmth ≥7 reached within 48 hours
- First meeting booked by 2026-05-14
- First proposal sent by 2026-05-17
- First deal closed by 2026-05-23

---

## Next Step: Extract Contacts

Ready to populate these templates with actual contact data from:
1. LinkedIn export (top 50 connections)
2. Gmail contacts export (key relationships)
3. Phone contacts (call-list)
4. Past email archive (existing relationships)
5. Community member list (warm network)

**Action:** Export contacts from each source and fill in the Contact Extraction template below.
