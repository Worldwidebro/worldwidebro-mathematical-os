---
references:
  - [[OPERATOR-REPOSITORY-INTELLIGENCE-FRAMEWORK]]
  - [[REPO-CLASSIFICATION-BOTTLENECK-RANKING.csv]]
---

# VENTURE BOTTLENECK ACTION PLAN
**Template: Query framework for operators to find the right repos for their venture's current stage**

**Usage:** Every venture is stuck on exactly one stage. Query the CSV for repos ranked by that stage. Implement the top 3.

---

## EXAMPLE: CON-011 (ELECTRICAL SERVICES) — STAGE 1

**Current Status:**
- Venture: CON-011 (Electrical contracting)
- Stage: 1 (Demand Creation)
- Problem: 5 leads/month, need 50
- Timeline: Month 1 (June 13 - July 13)

**Step 1: Query Stage 1 Repos (Sorted by Score)**

From `REPO-CLASSIFICATION-BOTTLENECK-RANKING.csv`, filter for Stage1_Demand, sort descending:

| Rank | Repo | Score | Why | Action |
|------|------|-------|-----|--------|
| 1 | YouTube Scripts | 10 | YouTube drives organic leads | Start 5 videos immediately |
| 2 | construction-content-topics | 9 | Content marketing generates traffic | Use as video outline reference |
| 3 | n8n | 9 | Consolidate 5+ lead sources | Build lead aggregation workflow |
| 4 | con-011-electrical-services | 8 | Live website is lead capture | Optimize form, traffic |
| 5 | rebrand-con-trade.js | 8 | Rapid site updates | Deploy improvements fast |
| 6 | Make.com | 8 | Alternative to n8n (lighter) | Backup if n8n too complex |
| 7 | Supabase | 7 | Lead database + tracking | Centralize all lead sources |
| 8 | Vercel | 7 | Fast website = good UX | Website performance matters |
| 9 | Next.js | 7 | Website framework | Website foundation |
| 10 | Resend | 6 | Automated follow-up | Send first reply email |

**Step 2: 30-Day Implementation Plan**

**Week 1 (June 13-19): TOP 3 ONLY**
```
Priority 1: n8n (9/10)
├── Task: Set up lead consolidation workflow
├── Sources: HomeAdvisor, Angi, SAM.gov, Google Local, Nextdoor
├── Destination: Supabase leads table
└── Time: 2-3 days
│
Priority 2: construction-content-topics (9/10)
├── Task: Create 5 YouTube videos
├── Source: Use CSV as content outline
├── Publish: YouTube channel (Electrical Construction channel)
└── Time: 2 days (script + record + upload)
│
Priority 3: Supabase (7/10)
├── Task: Build lead database schema
├── Schema: leads (id, source, email, phone, zip, status, notes)
├── Index: By source, by date, by conversion stage
└── Time: 1 day
```

**Week 2 (June 20-26): SUPPORT**
```
Priority 4: con-011-electrical-services website
├── Task: Optimize lead form (1 click, mobile-friendly)
├── Test: Mobile conversion rate
└── Time: 1 day

Priority 5: Resend (6/10)
├── Task: Auto-send first follow-up email within 2 hours
├── Template: "Thanks for contacting us, here's what to expect"
└── Time: 1 day
```

**Week 3-4 (June 27 - July 10): SCALE**
```
Priority 6: Make.com (if n8n struggles)
├── Task: Set up as backup automation
└── Time: 1 day (if needed)

Measure:
├── Leads from each source (n8n tracks)
├── Conversion rate by source
└── Cost per lead by source
```

**Step 3: Success Metrics (End of Month 1)**

| Metric | Target | Actual |
|--------|--------|--------|
| Total leads | 50 | \_\_\_ |
| From YouTube | 15 | \_\_\_ |
| From paid (Ads) | 20 | \_\_\_ |
| From organic (SEO, referral) | 10 | \_\_\_ |
| From Google Local/Maps | 5 | \_\_\_ |
| Conversion (email opened) | 40% | \_\_\_ |
| First follow-up sent | <2 hours | \_\_\_ |

**When you hit 50 leads/month: PIVOT TO STAGE 2**

---

## TEMPLATE: Any Venture, Any Stage

Use this template for any venture:

```
## [VENTURE_ID] ([VENTURE_NAME]) — STAGE [1-5]

**Current Status:**
- Venture: [ID] ([Name])
- Stage: [1/2/3/4/5] ([Stage Name])
- Problem: [What's blocking progress?]
- Timeline: [Month X]

**Step 1: Query Stage X Repos**

From REPO-CLASSIFICATION-BOTTLENECK-RANKING.csv:
- Filter for Stage[X]_[Bottleneck]
- Sort by score (descending)
- Select top 3-5

**Step 2: Implementation Plan**

Week 1: Priority 1-3 (highest score repos)
- Task: [specific action]
- Time: [days/hours]

Week 2: Priority 4-5 (support repos)
- Task: [specific action]
- Time: [days/hours]

**Step 3: Success Metrics**

| Metric | Target | Actual |
|--------|--------|--------|
| [KPI 1] | [target] | ___ |
| [KPI 2] | [target] | ___ |

**When done: PIVOT TO STAGE [X+1]**
```

---

## QUICK REFERENCE: TOP REPOS BY STAGE

**Stage 1 (Demand):** YouTube Scripts (10), construction-content-topics (9), n8n (9)
**Stage 2 (Sales):** Claude API (9), Resend (9), Supabase (9)
**Stage 3 (Fulfillment):** n8n (9), Temporal (9), Supabase (9)
**Stage 4 (Founder Removal):** Claude API (9), Grafana (8), Obsidian (8), Supabase (9)
**Stage 5 (Reinvestment):** Grafana (10), DuckDB (10), Supabase (9)

---

## HOW THIS CHANGES VENTURE EXECUTION

**Old (Technician) Approach:**
- We classified all 1,400 repos
- Scored them equally on 8 dimensions
- Venture leader looks at generic list
- "Which ones should I use?"
- Result: Paralysis, unclear what matters

**New (Operator) Approach:**
- Venture is stuck on Stage 1
- "What solves Stage 1?"
- Query returns 10 repos ranked for Stage 1 only
- Use top 3 this month
- "Hit Stage 1 goal? Move to Stage 2"
- Result: Clear execution path

---

## INTEGRATION WITH SUPABASE

This framework will live in Supabase:

```sql
-- Table: venture_bottleneck_stage
venture_id    | current_stage  | date_entered | success_metrics
CON-011       | 1              | 2026-06-13   | { leads: 50 }

-- Table: stage_repo_ranking  
venture_id    | stage | repo_name    | score | action_plan
CON-011       | 1     | n8n          | 9     | Build lead aggregation
CON-011       | 1     | YouTube...   | 10    | Create 5 videos

-- Query: What repos should CON-011 focus on RIGHT NOW?
SELECT repo_name, score, action_plan
FROM stage_repo_ranking
WHERE venture_id = 'CON-011' 
  AND stage = (SELECT current_stage FROM venture_bottleneck_stage WHERE venture_id = 'CON-011')
ORDER BY score DESC
LIMIT 3;

Result:
YouTube Scripts  | 10 | Create 5 videos
construction-... | 9  | Use as outline
n8n              | 9  | Build aggregation
```

---

**This is the operator action plan framework.**
Each venture queries once per month: "What repos solve my current bottleneck?" Execute top 3, measure, move to next stage.

