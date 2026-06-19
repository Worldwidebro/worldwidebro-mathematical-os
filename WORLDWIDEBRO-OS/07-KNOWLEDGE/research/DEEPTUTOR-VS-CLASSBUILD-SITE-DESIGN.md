# DeepTutor vs ClassBuild: Platform Alignment & Site Design

**Question:** Which platform should we use? What does the site look like?  
**Answer:** ClassBuild + Skool (not DeepTutor). Here's why + the actual UI mockups.

---

## 🎯 ALIGNMENT: CAN THEY WORK TOGETHER?

### DeepTutor: What It Is
```
Multi-user AI tutoring platform
├─ Python FastAPI backend
├─ Next.js frontend
├─ Persistent knowledge workspace
├─ Agentic TutorBot with tools/MCP
├─ LlamaIndex RAG
├─ Multi-LLM support
└─ Self-hosted (you run the server)

Best for: Long-term student-tutor relationships, persistent learning environments
```

### ClassBuild: What It Is
```
Course generation + distribution platform
├─ React 19 + Vite frontend (browser-native)
├─ AI-powered course generation (you run locally)
├─ Exports to: PPTX, SCORM, HTML, ZIP
├─ Built-in learning science (5 principles)
├─ No backend needed (client-side)
└─ Integrates with any LMS/Skool
```

---

## 🔄 CAN THEY INTEGRATE?

### Option A: ClassBuild Alone ✅ RECOMMENDED

```
Your Machine (Local)
    ↓
ClassBuild generates course JSON
    ↓
Upload to Skool (manual drag-drop)
    ↓
Students see course on Skool
    ↓
Skool handles: hosting, payments, community
```

**Effort:** Minimal  
**Integration:** Loose (file exports)  
**Recommendation:** YES, do this

---

### Option B: DeepTutor + ClassBuild ⚠️ POSSIBLE BUT COMPLEX

```
ClassBuild generates course JSON
    ↓
Import JSON into DeepTutor database
    ↓
DeepTutor hosts chapters + quizzes
    ↓
DeepTutor student interface shows lessons
    ↓
Students interact with TutorBot + course
```

**What you'd need to build:**
- Stripe payment integration (DeepTutor doesn't have this)
- Multi-course management system (not built in)
- Marketing/landing pages (not built in)
- Email/CRM system (not built in)
- Analytics dashboard (not built in)

**Effort:** 6-8 weeks of engineering  
**Cost:** $20K-30K in dev work  
**Timeline:** Too slow for startup stage  
**Recommendation:** NO, too complex

---

### Option C: DeepTutor Only ❌ WRONG FOR THIS BUSINESS

```
You host DeepTutor on your own server
Students access DeepTutor interface
But: No payment system, no multi-course catalog, no marketing integration
```

**Problems:**
- Designed for tutoring relationships, not course sales
- No payment processing built in
- No customer acquisition tools
- Requires Docker/DevOps knowledge
- Scaling costs money (server + bandwidth)

**Recommendation:** NO, not the right tool

---

## ✅ VERDICT: USE CLASSBUILD + SKOOL

| Dimension | DeepTutor | ClassBuild | Winner |
|-----------|-----------|-----------|--------|
| **Time to Launch** | 8-12 weeks | 2-4 weeks | ClassBuild ✅ |
| **Infrastructure Cost** | $$$ (servers) | $ (Skool 5% cut) | ClassBuild ✅ |
| **Course Generation** | Manual | AI-powered | ClassBuild ✅ |
| **Payment Processing** | ❌ Not built | ✅ Skool handles | ClassBuild ✅ |
| **Community Features** | ✅ Strong | ⚠️ Basic (Skool) | DeepTutor |
| **Customization** | ✅ Highly | ⚠️ Limited | DeepTutor |
| **Multi-course** | ⚠️ Possible | ✅ Built-in | ClassBuild ✅ |
| **Extensibility** | ✅ (MCP, tools) | ⚠️ (prompt libs) | DeepTutor |

**Winner for your business model:** **ClassBuild + Skool** (5 key wins vs 1)

---

## 🎨 WHAT THE SITE LOOKS LIKE: CLASSBUILD + SKOOL

### 1. LANDING PAGE (Before Signup)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                 ┃
┃                    AI BOSS HOLDINGS                            ┃
┃              Learn from Venture Operators                      ┃
┃                                                                 ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                                 ┃
┃  ┌───────────────────────────────────┐                        ┃
┃  │  CLAIM YOUR FREE CHAPTER           │                        ┃
┃  │  "Fundamentals of Contracting"     │                        ┃
┃  │                                    │                        ┃
┃  │  ✓ 8-chapter course               │                        ┃
┃  │  ✓ Real-world scenarios           │                        ┃
┃  │  ✓ Learning science embedded      │                        ┃
┃  │                                    │                        ┃
┃  │      [  GET FREE CHAPTER  ]        │                        ┃
┃  └───────────────────────────────────┘                        ┃
┃                                                                 ┃
┃                          OR                                     ┃
┃                                                                 ┃
┃  ┌──────────────────────────────────────────────────────────┐ ┃
┃  │ Join 50+ Venture Operators                               │ ┃
┃  │                                                          │ ┃
┃  │ Get unlimited access to all courses:                     │ ┃
┃  │ ✓ General Contracting (8 chapters)                       │ ┃
┃  │ ✓ AI Automation Systems (8 chapters)                     │ ┃
┃  │ ✓ Fintech Fundamentals (8 chapters)                      │ ┃
┃  │ ✓ Weekly Q&A calls                                       │ ┃
┃  │ ✓ 500+ templates                                         │ ┃
┃  │ ✓ Community network                                      │ ┃
┃  │                                                          │ ┃
┃  │           $49/month or $490/year                         │ ┃
┃  │                                                          │ ┃
┃  │         [  JOIN FOR $49/MONTH  ]                         │ ┃
┃  │       14-day money-back guarantee                        │ ┃
┃  └──────────────────────────────────────────────────────────┘ ┃
┃                                                                 ┃
┃  ─────────────────────────────────────────────────────────    ┃
┃                                                                 ┃
┃  Why venture operators choose us:                              ┃
┃  • Real examples from actual ventures in your network         ┃
┃  • 5 learning science principles embedded                     ┃
┃  • Peer community (not isolated video)                        ┃
┃  • Templates & resources (not just lectures)                 ┃
┃  • Expert instructors (not just AI)                          ┃
┃                                                                 ┃
┃  "This course saved me $150K in contract disputes"            ┃
┃  — Sarah K, Gen Contracting                                    ┃
┃                                                                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

### 2. AFTER SIGNUP: MEMBER DASHBOARD (Skool)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ AI Boss Holdings  [Profile] [Messages] [Settings] [Log Out]   ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                               ┃
┃ YOUR LEARNING PATH                                           ┃
┃ ════════════════════════════════════════════════════════════ ┃
┃                                                               ┃
┃ General Contracting Progress: 60%                            ┃
┃ ████████░░ Chapter 4: Risk Allocation (IN PROGRESS)          ┃
┃ Estimated time remaining: 3 hours                            ┃
┃ [Resume Learning] [View All Chapters]                        ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ AVAILABLE COURSES                                            ┃
┃                                                               ┃
┃ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        ┃
┃ │ General      │  │ AI Automation│  │  Fintech     │        ┃
┃ │ Contracting  │  │   Systems    │  │ Fundamentals │        ┃
┃ │              │  │              │  │              │        ┃
┃ │ ✅ Active    │  │ ✅ Active    │  │ ✅ Active    │        ┃
┃ │ 8/8 chapters │  │ 8/8 chapters │  │ 8/8 chapters │        ┃
┃ │ Completed    │  │ Not started  │  │ Not started  │        ┃
┃ │              │  │              │  │              │        ┃
┃ │ [Start Over] │  │[Start Course]│  │[Start Course]│        ┃
┃ └──────────────┘  └──────────────┘  └──────────────┘        ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ COMMUNITY & DISCUSSION                                       ┃
┃                                                               ┃
┃ 🔥 Hot Topics (This Week):                                  ┃
┃  [23] Contract disputes: What we got wrong                  ┃
┃  [15] AI automation tools: Best options                     ┃
┃  [8]  Scaling from 5 to 50 people                           ┃
┃                                                               ┃
┃ 👥 Members (51 active):                                      ┃
┃  Sarah K. • Marcus L. • You • 48 others                      ┃
┃  [Browse Full Community]                                     ┃
┃                                                               ┃
┃ 📊 Leaderboard (Course Completion):                          ┃
┃  1. Sarah K. — 100% (GenCon + AI)                            ┃
┃  2. Marcus L. — 87% (GenCon + Fintech)                       ┃
┃  3. You — 60% (GenCon)                                       ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ RESOURCES & TEMPLATES                                        ┃
┃                                                               ┃
┃ • 500+ Templates (download instantly)                        ┃
┃ • Discussion Starters (peer learning)                        ┃
┃ • Weekly Q&A Recordings                                      ┃
┃ • Case Study Library                                         ┃
┃ • Audiobooks (8 chapters of each course)                     ┃
┃                                                               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

### 3. INSIDE A COURSE: CHAPTER VIEW (Skool Classroom)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ AI Boss Holdings > General Contracting > Chapter 3           ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                               ┃
┃ CHAPTER 3: Risk Allocation and Insurance                    ┃
┃ ═══════════════════════════════════════════════════════════ ┃
┃                                                               ┃
┃ Learning Objectives:                                         ┃
┃ ☐ Identify and classify construction risks                  ┃
┃ ☐ Understand contractual risk allocation                    ┃
┃ ☐ Design insurance and bonding strategies                   ┃
┃ ☐ Apply risk analysis to project planning                   ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ OPENING SCENARIO                                             ┃
┃                                                               ┃
┃  🏗️ During excavation, your crew discovers                 ┃
┃     underground utilities the survey missed.                 ┃
┃                                                               ┃
┃  💰 Relocation costs: $150,000                              ┃
┃  📅 Project delay: 2 weeks                                  ┃
┃                                                               ┃
┃  Your contract says: "Contractor responsible for            ┃
┃  discovering existing conditions."                           ┃
┃                                                               ┃
┃  But the survey was inadequate.                             ┃
┃                                                               ┃
┃  Question: Who bears the cost?                              ┃
┃            (Think before reading below)                      ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ CONTENT (Expandable Sections)                               ┃
┃                                                               ┃
┃ ▸ Section 1: Types of Construction Risk                    ┃
┃   Financial • Schedule • Safety • Legal • Quality            ┃
┃                                                               ┃
┃ ▸ Section 2: Risk Identification and Analysis               ┃
┃   Brainstorming • Probability Matrix • Risk Register         ┃
┃                                                               ┃
┃ ▸ Section 3: Contractual Risk Allocation                    ┃
┃   Indemnity • Insurance • Liability Limits                   ┃
┃                                                               ┃
┃ ▸ Section 4: Insurance and Bonding Strategy                 ┃
┃   Builder's Risk • General Liability • Bonds                 ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ THINK ABOUT IT (3 Practice Questions)                        ┃
┃                                                               ┃
┃ Q1: Underground utilities discovered. Your contract           ┃
┃     says contractor assumes site risks. Is this a            ┃
┃     change order or your cost? [Your answer] [Check]        ┃
┃                                                               ┃
┃ Q2: Your electrician gets injured, out 3 months.            ┃
┃     Who bears the project delay impact?                      ┃
┃     [Your answer] [Check]                                    ┃
┃                                                               ┃
┃ Q3: Weather delays the critical path 2 weeks.               ┃
┃     Contract says "contractor assumes X days."               ┃
┃     How many days would you negotiate?                       ┃
┃     [Your answer] [Check]                                    ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ KEY TAKEAWAYS (Collapsible)                                 ┃
┃                                                               ┃
┃ ✓ Construction risk includes 6 categories; each needs       ┃
┃   different mitigation strategies.                           ┃
┃                                                               ┃
┃ ✓ Identify risks early by probability + impact.             ┃
┃   Create a risk register and update monthly.                 ┃
┃                                                               ┃
┃ ✓ Contracts allocate risk through indemnity, insurance,      ┃
┃   liability limits, and responsibility clauses.              ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ RESOURCES FOR THIS CHAPTER                                   ┃
┃                                                               ┃
┃ 📄 Risk Assessment Template (download)                       ┃
┃ 📄 Insurance Checklist (download)                            ┃
┃ 📹 Video Summary (15 min)                                    ┃
┃ 🎙️ Audio Version (podcast format)                            ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ DISCUSSION & QUESTIONS                                       ┃
┃                                                               ┃
┃ [18 replies] Risk allocation in changing conditions          ┃
┃ [5 replies]  Insurance we needed that wasn't covered         ┃
┃ [New Discussion] Share your risk management story            ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ PROGRESS                                                      ┃
┃                                                               ┃
┃ ✅ Chapter 3 Complete!                                       ┃
┃                                                               ┃
┃ [← Previous: Chapter 2]  [Next: Chapter 4 →]                ┃
┃                                                               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

### 4. RESOURCES TAB (Templates, Videos, Audiobooks)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ AI Boss Holdings > Resources                                 ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                               ┃
┃ DOWNLOAD INSTANTLY (500+ Templates)                          ┃
┃                                                               ┃
┃ General Contracting:                                         ┃
┃  📄 AIA Contract Template ......................... 25 DLs   ┃
┃  📄 Generic Contract Template ..................... 18 DLs   ┃
┃  📄 Risk Assessment Form .......................... 42 DLs   ┃
┃  📄 Insurance Checklist ........................... 38 DLs   ┃
┃  📄 Change Order Template ......................... 31 DLs   ┃
┃  📄 Payment Application Form ...................... 22 DLs   ┃
┃                                                               ┃
┃ AI Automation:                                               ┃
┃  📄 Workflow Audit Checklist ...................... 19 DLs   ┃
┃  📄 Tool Stack Comparison ......................... 14 DLs   ┃
┃  📄 ROI Calculator ................................ 27 DLs   ┃
┃  📚 Prompt Library (100+ prompts) ................. 31 DLs   ┃
┃                                                               ┃
┃ Fintech:                                                      ┃
┃  📄 Compliance Checklist .......................... Coming   ┃
┃  📄 Payment Flow Diagram .......................... Coming   ┃
┃  📄 Bank Relationship Template .................... Coming   ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ WATCH VIDEOS (Chapter Summaries)                             ┃
┃                                                               ┃
┃  📹 General Contracting (8 videos, 15 min each)             ┃
┃     Ch 1 Fundamentals [4.2k views] [15:32]                  ┃
┃     Ch 2 Contract Types [1.8k views] [18:45]                ┃
┃     ...more                                                  ┃
┃                                                               ┃
┃  📹 AI Automation (Coming 6/15)                              ┃
┃     Ch 1 Foundations [0 views] [TBD]                        ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ LISTEN TO AUDIOBOOKS (Podcast Format)                        ┃
┃                                                               ┃
┃  🎙️ General Contracting (8 chapters, 8 hours)               ┃
┃     Narrated by [Sarah K, Gen Contracting expert]           ┃
┃     [Listen in Spotify] [Download MP3]                      ┃
┃                                                               ┃
┃  🎙️ AI Automation (Coming 6/15)                              ┃
┃     [Notify me when ready]                                   ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ LIVE Q&A REPLAYS (Weekly Calls)                              ┃
┃                                                               ┃
┃  📺 June 1: "Contract Disputes & Mitigation" [Watch]        ┃
┃  📺 June 8: "Profitability Deep Dive" [Watch]               ┃
┃  📺 June 15: "Scaling Your Team" [Scheduled]                ┃
┃                                                               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

### 5. PREMIUM TIER: COACHING DASHBOARD

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ AI Boss Holdings > Premium Coaching ($299/month)            ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                               ┃
┃ YOU'RE A PREMIUM MEMBER                                      ┃
┃                                                               ┃
┃ Your monthly benefits:                                       ┃
┃ ✅ All courses + resources (same as standard)                ┃
┃ ✅ 1-on-1 monthly coaching (2 hours)                        ┃
┃ ✅ Priority email support (24-hour response)                 ┃
┃ ✅ Peer network calls (2x/month)                             ┃
┃ ✅ Access to founder interviews (private)                    ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ YOUR COACHING SCHEDULE                                       ┃
┃                                                               ┃
┃ 🔴 UPCOMING (This Month)                                     ┃
┃                                                               ┃
┃  📅 June 15 @ 2:00 PM PT                                     ┃
┃  "Contract Disputes & Mitigation"                            ┃
┃  Coach: Sarah K. (General Contracting expert)                ┃
┃  [Join Call] [Reschedule] [Add to Calendar]                 ┃
┃                                                               ┃
┃  📅 June 22 @ 3:00 PM PT                                     ┃
┃  "Profitability Deep Dive"                                   ┃
┃  Coach: Marcus L. (Finance + Operations)                     ┃
┃  [Join Call] [Reschedule] [Add to Calendar]                 ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ 📺 PAST CALLS (Watch Recordings)                            ┃
┃                                                               ┃
┃  June 1: "Scaling from 5 to 20 People" [Watch]             ┃
┃          [Download Transcript] [PDF Notes]                  ┃
┃                                                               ┃
┃  May 25: "Risk Management in Contracts" [Watch]             ┃
┃          [Download Transcript] [PDF Notes]                  ┃
┃                                                               ┃
┃ ─────────────────────────────────────────────────────────   ┃
┃                                                               ┃
┃ 👥 PEER NETWORK CALLS (All Premium Members)                 ┃
┃                                                               ┃
┃  📅 June 20 @ 5:00 PM PT [RSVP]                             ┃
┃  "What We Got Wrong in Q2 (And How We Fixed It)"            ┃
┃  Location: Zoom (link sent day-of)                           ┃
┃  Attendees: 12 founders expected                             ┃
┃                                                               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

## 🏗️ TECHNICAL ARCHITECTURE: WHAT'S BEHIND THE SCENES?

```
┌──────────────────────────────────────┐
│   User Browser (Skool.com)           │
│   ├─ Landing page                    │
│   ├─ Course classrooms               │
│   ├─ Community discussions           │
│   ├─ Member profiles                 │
│   └─ Payment checkout                │
└──────────────────────────────────────┘
            │
            ├─────────────────┬──────────────────┬─────────────┐
            ↓                 ↓                  ↓             ↓
        ┌────────┐      ┌──────────┐      ┌──────────┐   ┌──────────┐
        │ Stripe │      │ Kit      │      │Supabase  │   │Optional  │
        │Payment │      │(Email)   │      │Analytics │   │Third-    │
        │Process │      │Platform  │      │Database  │   │party     │
        └────────┘      └──────────┘      └──────────┘   │Tools     │
            │                │                  │        └──────────┘
            └────────────────┴──────────────────┘
                        │
                ┌───────┴────────┐
                ↓                ↓
            Backend Data      Analytics
            (Enrollments,     (Dashboards,
             Payments)        Reports)
```

**Data Flow:**
1. User pays $49/mo via Skool checkout
2. Stripe processes payment (2.9% + $0.30)
3. Skool creates enrollment record
4. Kit sends welcome email automatically
5. Supabase logs event (optional, for your analytics)
6. User accesses course content via Skool
7. Completion/engagement tracked in Skool dashboard

---

## 💰 COST BREAKDOWN (Per Month)

| Component | Cost | Notes |
|-----------|------|-------|
| Skool Platform | $0 | 5% commission on sales |
| Stripe Fees | Included | 2.9% + $0.30 per transaction |
| Email (Kit) | $0-29 | Free up to 1K subscribers |
| Supabase | $0-25 | Free tier, scales to $25/mo |
| Your Time | Variable | Content creation + marketing |
| **Total Infrastructure** | **$0-54** | Before any revenue |

**At 100 Paying Members:**
```
Revenue: 100 × $49/mo = $4,900/month
├─ Skool (5%) = -$245
├─ Stripe (2.9%) = -$142
├─ Kit (basic) = -$0
├─ Supabase (free) = -$0
└─ Net to You = $4,513/month
```

---

## ✅ READINESS CHECKLIST

### ClassBuild + Skool: READY FOR LAUNCH

```
✅ Content Creation
   - General Contracting sample course: COMPLETE
   - AI Automation queued for generation
   - Fintech queued for generation
   - Quality validated (learning science embedded)

✅ Platform Hosting
   - Skool account: Ready
   - Stripe integration: Ready
   - Email system (Kit): Ready
   - Database schema (Supabase): Designed

✅ User Interface
   - Landing page: Template ready
   - Dashboard: Skool provides
   - Course viewer: Skool provides
   - Community: Skool provides

⏳ Marketing & Launch
   - Sales page copy: 1 week to customize
   - Email sequences: 1 week to write
   - LinkedIn strategy: Calendar ready
   - Lead magnet: Chapter 1 free

Total time to launch: 2-4 weeks
Capital required: $0-100 (first month)
```

---

## 🎯 FINAL ANSWER

**Q: Deep Tutor vs ClassBuild — which should we use?**

**A: ClassBuild + Skool (not DeepTutor)**

**Why:**
- ✅ ClassBuild generates professional courses in hours (vs weeks of manual work)
- ✅ Skool handles everything: hosting, payments, community (one platform)
- ✅ Launch in 2-4 weeks (vs 8-12 weeks with DeepTutor)
- ✅ $0 infrastructure cost (commission-based, not server-based)
- ✅ Proven learning science + engagement features built-in

**The Site Experience:**
- Professional course platform (looks like Skillshare/Coursera)
- Community features (leaderboards, discussions, peer connections)
- Resource center (500+ templates, audiobooks, videos)
- Premium coaching tier ($299/mo for 1:1 + community calls)
- Mobile-friendly (Skool is responsive)

**Next Step:**
Deploy to Skool this week. Get 20 beta users. Measure completion + NPS. Launch paid only if metrics validate.
