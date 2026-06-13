---
references:
  - [[VENTURE-MASTER]]
  - REPOSITORY-INTELLIGENCE-VOCABULARY
  - CONSTRUCTION-STREET-PHILOSOPHY
---

# OPERATOR REPOSITORY INTELLIGENCE FRAMEWORK
**Strategic Reframe: Repos Get Ranked By Bottleneck, Not Classified Equally**

**Core Principle:** A repository's value = how well it solves the current bottleneck for this specific venture.

---

## THE 5 OPERATOR BOTTLENECKS

Every venture is stuck on exactly one of these:

### **STAGE 1: DEMAND CREATION**
Problem: Nobody knows you exist | Constraint: Zero leads
```
Operator questions:
- Which repos aggregate leads from 5+ sources?
- Which repos automate lead capture?
- Which repos measure lead source ROI?
- How do we get from 0 to 50 leads/month?
```

### **STAGE 2: SALES CONVERSION**
Problem: Lots of leads, low close rate | Constraint: Sales is manual
```
Operator questions:
- Which repos automate qualification?
- Which repos systematize follow-up?
- Which repos create sales visibility (CRM)?
- How do we get from 20% to 40% close rate?
```

### **STAGE 3: FULFILLMENT AT SCALE**
Problem: Profitable but doesn't scale | Constraint: Founder does all work
```
Operator questions:
- Which repos systematize processes?
- Which repos coordinate teams?
- Which repos remove founder from daily work?
- How do we 2x revenue with same team?
```

### **STAGE 4: FOUNDER REMOVAL**
Problem: Team exists, founder still bottleneck | Constraint: Knowledge isn't documented
```
Operator questions:
- Which repos capture processes?
- Which repos let team make decisions independently?
- Which repos measure team performance?
- How do we remove founder from decisions?
```

### **STAGE 5: REINVESTMENT & SCALE**
Problem: System works, scale it | Constraint: Don't know where to spend next dollar
```
Operator questions:
- Which repos show ROI by channel?
- Which repos measure unit economics?
- Which repos optimize profitability?
- Where do we 2x spending for best return?
```

---

## REPO RANKINGS BY BOTTLENECK (Context-Dependent)

### **FOR STAGE 1 VENTURES (Demand Creation)**
Ranking: "Which repo solves lead generation?"

| Repo | Score | Why | Action |
|------|-------|-----|--------|
| n8n | 9/10 | Consolidates leads from HomeAdvisor, Angi, SAM.gov, Nextdoor | Set up automation workflows |
| construction-content-topics.csv | 8/10 | Content marketing drives organic leads via YouTube, blog, SEO | Start content production |
| Supabase | 7/10 | Centralized lead database, track source, pipeline | Build lead tracking |
| Vercel | 7/10 | Website is lead entry point, optimize for conversion | Improve lead capture form |
| Resend | 6/10 | Automate first follow-up, improve response time | Set up email sequences |
| Google Ads | 9/10 | Paid lead generation (if CAC < LTV) | Test ad campaigns |
| Nextdoor / Community | 7/10 | Hyper-local, high-trust referrals | Organic local presence |

### **FOR STAGE 2 VENTURES (Sales Conversion)**
Ranking: "Which repo converts leads to customers?"

| Repo | Score | Why | Action |
|------|-------|-----|--------|
| Supabase (CRM) | 9/10 | Single view of lead, close rate tracking | Build CRM system |
| LangGraph | 8/10 | AI qualification (saves salesperson time) | Auto-qualify leads |
| n8n | 8/10 | Automated follow-up sequences, trigger-based | Build nurture flows |
| Stripe | 7/10 | Revenue visibility, subscription metrics | Track closed deals |
| Resend | 6/10 | Reliable email delivery, templates | Improve email reliability |

### **FOR STAGE 3 VENTURES (Fulfillment at Scale)**
Ranking: "Which repo scales delivery without founder?"

| Repo | Score | Why | Action |
|------|-------|-----|--------|
| Supabase | 9/10 | Project status, team visibility, founder can delegate | Build project data model |
| n8n | 9/10 | Automate status updates, handoffs, no manual work | Create workflow automation |
| Temporal | 8/10 | Orchestrate multi-step project execution | Manage complex workflows |
| Obsidian | 8/10 | Document all processes, team executes | Create process wiki |
| GitHub | 7/10 | Version-controlled SOPs, anyone can reference | Store procedures |

### **FOR STAGE 4 VENTURES (Founder Removal)**
Ranking: "Which repo makes team independent?"

| Repo | Score | Why | Action |
|------|-------|-----|--------|
| Obsidian | 9/10 | Institutional knowledge, team doesn't ask founder | Document decision frameworks |
| Supabase | 9/10 | Dashboards let team make decisions without founder | Build self-serve metrics |
| LangGraph | 8/10 | Automate repeatable decisions, founder exception-handler | Automate 80% of decisions |
| DuckDB | 7/10 | Team runs own reports, founder not bottleneck | Enable team analytics |
| GitHub | 7/10 | SOPs stored, team references without asking | Keep procedures updated |

### **FOR STAGE 5 VENTURES (Reinvestment & Scale)**
Ranking: "Which repo optimizes spending?"

| Repo | Score | Why | Action |
|------|-------|-----|--------|
| DuckDB | 10/10 | Analytics: which lead source = best ROI? | Analyze unit economics |
| Grafana | 9/10 | Real-time CAC vs LTV by channel, profit trending | Build dashboard |
| Supabase | 9/10 | Revenue by source, cost by project, margin | Track financials |
| Stripe | 8/10 | Payment data, churn signals, revenue forecast | Monitor revenue health |

---

## PROGRESSION PATH (Typical Timeline)

```
MONTHS 1-3: STAGE 1 (Demand)
├── Focus: Get to 50 leads/month
├── Key repos: n8n, construction-content-topics, Supabase
├── Owner: Founder (sales)
└── When done: Move to Stage 2

MONTHS 3-6: STAGE 2 (Sales)
├── Focus: Get to 40% close rate
├── Key repos: Supabase (CRM), LangGraph (qualification), n8n (sequences)
├── Owner: Hired salesperson
└── When done: Move to Stage 3

MONTHS 6-9: STAGE 3 (Fulfillment)
├── Focus: 2x revenue with same team
├── Key repos: Supabase, n8n, Obsidian, Temporal
├── Owner: Hired delivery manager
└── When done: Move to Stage 4

MONTHS 9-12: STAGE 4 (Founder Removal)
├── Focus: Founder not in daily operations
├── Key repos: Obsidian, Supabase, LangGraph
├── Owner: Full team
└── When done: Move to Stage 5

MONTH 12+: STAGE 5 (Reinvestment)
├── Focus: 2x ad spend, optimize channels
├── Key repos: DuckDB, Grafana, Supabase
├── Owner: Growth team
└── When done: Repeat for next venture
```

---

## EXAMPLE: CON-011 (ELECTRICAL) RIGHT NOW

**Current Stage: 1 (Demand Creation)**  
**Current Problem: 5 leads/month (need 50)**

**Operator Questions:**
1. Which repos get us to 50 leads/month fastest?
2. Which repos consolidate leads from multiple sources?
3. Which repos measure which source works?

**Repo Ranking for CON-011:**
1. **n8n** (9/10) → Consolidate leads from HomeAdvisor, Angi, SAM.gov, Nextdoor
2. **construction-content-topics.csv** (8/10) → Content marketing for organic traffic
3. **Supabase** (7/10) → Lead tracking, source analytics
4. **Vercel** (7/10) → Website optimization for lead capture
5. **Resend** (6/10) → Automated follow-up

**30-Day Action Plan:**
```
Week 1: Set up n8n to pull leads from 4 sources into Supabase
Week 2: Create 5 YouTube videos from construction-content-topics
Week 3: Optimize website landing page for electrical leads
Week 4: Measure which source is cheapest (CAC), double that
→ Goal: 50 leads/month by end of Month 1
```

**When you hit 50 leads/month:** Pivot to Stage 2
- New repos: Supabase CRM, LangGraph AI qualification, n8n follow-up sequences
- Focus: Convert 20% → 40% close rate

---

## WHY THIS CHANGES EVERYTHING

**Technician approach:**
- Classify all 1,400 repos
- Score them equally on 8 dimensions
- 2 weeks of work
- Result: Generic database of repos

**Operator approach:**
- Identify which bottleneck you're stuck on TODAY
- Find the 3-5 repos that solve THAT bottleneck
- Implement in 2 days
- Result: Actual progress on your venture

**For CON-011:** You don't need DuckDB analytics (Stage 5) today. You need n8n to aggregate leads (Stage 1).

---

## THE NEW REPOSITORY INTELLIGENCE SYSTEM

**Old:** Repository → Classification → Score (1-10) → Database

**New:** Venture Stage → Bottleneck → Repo Ranking by Context → Action Plan

**Stored in:** Bottleneck-specific tables (not generic "repo score")

```
Stage1_Demand_Repos
├── n8n (9/10)
├── construction-content-topics (8/10)
└── ...

Stage2_Sales_Repos
├── Supabase (9/10)
├── LangGraph (8/10)
└── ...

Stage3_Fulfillment_Repos
├── Supabase (9/10)
├── n8n (9/10)
└── ...

[etc for Stages 4-5]
```

**Each venture queries its current stage, gets its ranked repo list, executes the top 3.**

---

This is the operator lens. Ready to restructure everything?

