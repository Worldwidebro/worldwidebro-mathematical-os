---
title: Agent Loop Configuration (5 Workflows)
date: 2026-06-17
ventures: 712
systems: Supabase, Obsidian, ClickUp, Notion, GitHub
---

# 🤖 5 AGENT LOOPS FOR 712 VENTURES

## Loop 1: VENTURE DISCOVERY AGENT
**Purpose:** Search, filter, and surface opportunities across 712 ventures

### Loop Flow
```
1. Query Supabase (ventures table)
2. Filter by: sector, stage, health_score, revenue_ytd, status
3. Score ventures (health + revenue + growth potential)
4. Surface top 20 opportunities
5. Update Obsidian graph with highlights
6. Log decision to Supabase (venture_decisions table)
```

### Agent Actions (MCP)
- `mcp__claude_ai_Supabase__execute_sql` — Query ventures by criteria
- Update `venture_decisions` table with opportunity scores

### Example Trigger
```
"Find all construction ventures in 'planned' stage with 
health_score < 50 that need intervention"
```

### Output
- Ranked list in Supabase
- Marked in Obsidian graph
- Task created in ClickUp for each opportunity

---

## Loop 2: TASK AUTOMATION AGENT
**Purpose:** Create, assign, and manage workflow tasks for 712 ventures

### Loop Flow
```
1. Read venture requirements (skills needed)
2. Map to venture_skill_roadmap (Phase 1-14)
3. Create tasks in ClickUp per venture
4. Assign to owner_id (from ventures.owner_id)
5. Set due dates based on stage
6. Track completion in Supabase (tasks table)
```

### Relationship Model
```
Venture
  ├── owner_id (Contact/Human)
  ├── team_ids (Array of Contacts)
  └── tasks (Workflow items assigned to contacts)
```

### Agent Actions (MCP)
- `mcp__claude_ai_ClickUp__clickup_create_task` — Create venture tasks
- `mcp__claude_ai_ClickUp__clickup_update_task` — Update status
- `mcp__claude_ai_Supabase__execute_sql` — Log to tasks table

### Example Trigger
```
"Create onboarding tasks for all 'planned' stage ventures 
in construction sector, assign to respective owners"
```

### Workflow Chain
```
Phase 1 (Setup) → Create 5 tasks (init, research, planning, approval, kickoff)
Phase 2 (Discovery) → Create 3 tasks (market research, competitive analysis, target customer)
Phase 3 (Ideation) → Create 2 tasks (brainstorming, positioning)
...14 phases total
```

---

## Loop 3: NOTION SYNC AGENT
**Purpose:** Bulk expand 8 → 712 venture pages in Notion

### Loop Flow
```
1. Fetch all 712 ventures from Supabase
2. For each venture, check if Notion page exists
3. If not: Create new Notion page with template
4. If yes: Update with latest data (revenue, health, risks)
5. Set page properties: sector, stage, owner, health_score
6. Link to related ventures (graph_relations)
```

### Agent Actions (MCP)
- `mcp__claude_ai_Notion__notion-create-pages` — Create venture pages (batch)
- `mcp__claude_ai_Notion__notion-update-page` — Sync latest data
- `mcp__claude_ai_Supabase__execute_sql` — Query ventures + relationships

### Template Structure
```
Notion Page: [Venture Name]
├── Properties
│   ├── Sector (from ventures.sector)
│   ├── Stage (from ventures.stage)
│   ├── Owner (from ventures.owner_id)
│   ├── Health Score (from ventures.health_score)
│   └── Revenue (from ventures.revenue_ytd)
├── Relationships Block
│   └── Related Ventures (from graph_relations)
├── Tasks Section
│   └── ClickUp tasks embedded
└── Updates Log
    └── Last synced timestamp
```

### Example Trigger
```
"Sync all 712 ventures to Notion. Create if missing, 
update if already exists. Link related ventures."
```

### Batch Size
- 100 ventures per batch (Notion API limits)
- 7 batches total
- ~3 min per batch

---

## Loop 4: KNOWLEDGE GRAPH AGENT
**Purpose:** Analyze venture relationships, identify clusters, detect patterns

### Loop Flow
```
1. Query graph_relations table (venture-to-venture links)
2. Build relationship clusters (venture groups)
3. Identify:
   - Sister ventures (same sector, complementary)
   - Customer relationships (one venture sells to another)
   - Technology dependencies (one uses repo from another)
4. Score relationship strength (1-10)
5. Update Obsidian graph visualization
6. Log clusters to Supabase (new relationship records)
```

### Relationship Types (in graph_relations)
```
- "uses_tech_from" (venture A uses repos from venture B)
- "sells_to" (venture A is customer of venture B)
- "complements" (venture A + B work together)
- "competes_with" (venture A and B compete)
- "sister_venture" (venture A and B share owner/sector)
- "dependency" (venture A blocked by venture B)
```

### Agent Actions (MCP)
- `mcp__claude_ai_Supabase__execute_sql` — Query/update graph_relations
- Update Obsidian JSON (venture-hub-alignment.json)

### Example Trigger
```
"Analyze 712 ventures: find all sister ventures in 
construction sector, identify customer chains, 
score relationship strength 1-10"
```

### Output
```
Clusters found:
- Construction Ecosystem (45 ventures, 2.3 avg strength)
- Financial Services Mesh (38 ventures, 1.8 avg strength)
- Education Platform (22 ventures, 3.1 avg strength)
- Real Estate + Construction (19 ventures, 2.7 avg strength)
```

---

## Loop 5: REVENUE OPERATIONS AGENT
**Purpose:** Track metrics, flag risks, score ventures, forecast health

### Loop Flow
```
1. Read ventures table (revenue, costs, metrics)
2. Calculate KPIs:
   - CAC/LTV ratio
   - Churn rate
   - Burn rate (costs_mom vs revenue_ytd)
   - Health score (composite)
3. Identify risks:
   - Low revenue (<$5K/month)
   - High burn (>revenue)
   - CAC > LTV
   - Churn > 5%
4. Flag at-risk ventures (health < 40)
5. Create intervention tasks in ClickUp
6. Update venture_decisions with recommendations
```

### Metrics Dashboard (in Supabase)
```
Venture Health Score Calculation:
  = (Revenue/Target * 0.3) 
  + (LTV/CAC * 0.3)
  + (1 - Churn * 0.2)
  + (Runway_months / 12 * 0.2)

Risk Flags:
  🔴 RED (< 40):   Immediate action needed
  🟡 YELLOW (40-70): Monitor, may need support
  🟢 GREEN (> 70):  Healthy, scaling phase
```

### Agent Actions (MCP)
- `mcp__claude_ai_Supabase__execute_sql` — Calculate metrics
- `mcp__claude_ai_ClickUp__clickup_create_task` — Create intervention tasks
- Log to `venture_decisions` table

### Example Trigger
```
"Score all 712 ventures. Flag RED (health < 40). 
Create intervention tasks for each. Report top 20 
at-risk ventures with recommendations."
```

### Report Output
```
=== REVENUE OPERATIONS REPORT ===

🔴 AT-RISK (health < 40): 89 ventures
  - FIN-045: GenixBank Extensions (health: 28, high burn)
  - CON-122: LocalRoof (health: 35, CAC > LTV)
  - REAL-067: FlipProperties (health: 32, no revenue)

🟡 WATCH (health 40-70): 234 ventures
  - Healthy but no revenue yet
  - Good CAC/LTV, need to increase churn awareness
  
🟢 GREEN (health > 70): 389 ventures
  - Scaling successfully
  - Ready for capital allocation

💰 TOTAL REVENUE: $4.2M YTD
📉 AVG BURN RATE: $18K/month (declining trend)
📈 FORECAST: $6.8M by year-end (if 15% MoM growth)
```

---

## CONTACT, CUSTOMER, WORKFLOW RELATIONSHIPS

### Data Model

```
╔════════════════════════════════════════════════════════════╗
║                    VENTURE (Core Entity)                   ║
╠════════════════════════════════════════════════════════════╣
║ venture_id, name, sector, stage, owner_id, team_ids       ║
╚════════════════════════════════════════════════════════════╝
        ↓              ↓              ↓              ↓
        │              │              │              │
    [CONTACTS]    [CUSTOMERS]   [WORKFLOWS]   [RELATIONSHIPS]
        │              │              │              │
        ↓              ↓              ↓              ↓
  ┌──────────┐   ┌──────────┐  ┌──────────┐  ┌──────────┐
  │ owner_id │   │ graph_   │  │  tasks   │  │ graph_   │
  │ team_ids │   │relations │  │ (skill   │  │relations │
  │          │   │(sells_to)│  │execution)│  │          │
  └──────────┘   └──────────┘  └──────────┘  └──────────┘
```

### 1. CONTACTS = People managing ventures
```
Stored in ventures table:
  - owner_id: VARCHAR(100) → Who owns/manages venture
  - team_ids: TEXT → Array of team member IDs

Example:
  venture_id: CON-009
  owner_id: "antwuan-johns"
  team_ids: ["contractor-1", "contractor-2", "qc-person"]

Query by contact:
  SELECT * FROM ventures WHERE owner_id = 'antwuan-johns';
```

### 2. CUSTOMERS = Other ventures that buy from this one
```
Stored in graph_relations table:
  relation_type: "sells_to"
  
Example:
  from_venture_id: "MARKET-001" (marketplace)
  to_venture_id: "CON-009" (roofing company)
  relation_type: "sells_to"
  → MARKET-001 sells leads to CON-009

Query customers:
  SELECT to_venture_id FROM graph_relations 
  WHERE from_venture_id = 'CON-009' 
  AND relation_type = 'sells_to';
```

### 3. WORKFLOWS = Tasks assigned to contacts
```
Stored in tasks table:
  assigned_to: owner_id or team_member_id
  venture_id: Which venture the task is for
  status: pending | in_progress | completed

Example:
  task_id: TASK-001
  title: "Set up job portal for CON-009"
  assigned_to: "contractor-1"
  venture_id: "CON-009"
  status: "in_progress"

Also tracked in:
  - venture_skill_roadmap (14 phases, 296 skills)
  - skill_executions (audit trail of all skill runs)

Query workflows for a contact:
  SELECT * FROM tasks WHERE assigned_to = 'contractor-1';
  
Query workflows for a venture:
  SELECT * FROM tasks WHERE venture_id = 'CON-009';
```

### Full Workflow Loop Example

```
VENTURE: Roofing Marketplace (ROO-001)
├── CONTACT: Antwuan Johns (owner_id)
│   └── Team: ["contractor-A", "contractor-B"]
│
├── CUSTOMERS: [Roofing Companies that list jobs]
│   └── CON-009: LocalRoof Company (sells_to relation)
│   └── CON-010: RoofMaster (sells_to relation)
│
└── WORKFLOWS: [Tasks to build & scale]
    ├── Phase 1 (Setup)
    │   ├── Task: Research roofing market
    │   │   └── assigned_to: contractor-A
    │   ├── Task: Design platform architecture
    │   │   └── assigned_to: contractor-B
    │   └── Task: Create job board prototype
    │       └── assigned_to: contractor-A
    │
    ├── Phase 2 (Discovery)
    │   ├── Task: Interview 20 roofing companies
    │   │   └── assigned_to: contractor-B
    │   └── Task: Research competitor platforms
    │       └── assigned_to: contractor-A
    │
    └── Phase 3+ (Ideation, Build, Test, Launch...)
```

---

## HOW ALL 5 LOOPS INTERACT

```
┌─────────────────────────────────────────────────────────────┐
│         VENTURE DISCOVERY AGENT (Finds Opportunities)       │
│  Queries: health_score < 40, sector = construction, etc     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
        ┌──────────────────────────────┐
        │  TASK AUTOMATION AGENT       │
        │  (Create workflows for tasks)│
        │  Creates tasks in ClickUp    │
        │  Assigns to owner_id/team_id │
        └──────────┬───────────────────┘
                   │
        ┌──────────┴──────────┐
        ↓                     ↓
  ┌──────────────┐      ┌─────────────────┐
  │   NOTION     │      │ KNOWLEDGE GRAPH │
  │  SYNC AGENT  │      │  AGENT          │
  │  (Document) │      │  (Analyze)      │
  │  Creates    │      │  Finds clusters │
  │  pages for  │      │  & relationships│
  │  712 ventures│     │  Updates        │
  │  in Notion  │      │  graph_relations│
  └──────────────┘      └────────┬────────┘
                                 │
                                 ↓
                    ┌──────────────────────────┐
                    │ REVENUE OPS AGENT        │
                    │ (Score & Flag Risk)      │
                    │ Calculates health_score  │
                    │ Flags at-risk ventures   │
                    │ Creates intervention     │
                    │ tasks for RED ventures   │
                    └──────────────────────────┘
```

### Data Flow
```
Supabase (source of truth)
    ├── ventures (712 records)
    ├── tasks (workflow assignments)
    ├── graph_relations (venture relationships)
    ├── venture_decisions (opportunity scoring)
    └── skill_executions (audit trail)
        ↓
    Obsidian (visualization)
    ClickUp (task management)
    Notion (team documentation)
    All synced via agents
```

---

## STARTUP SEQUENCE

**Run in this order (can parallelize 2-5):**

1. **Venture Discovery** (5 min)
   - Scan all 712
   - Score health
   - Identify top 20 opportunities

2. **Task Automation** (10 min, parallel with #1)
   - Create tasks for all phases
   - Assign to owners/teams
   - Set dependencies

3. **Notion Sync** (15 min, parallel with #1-2)
   - Create 712 pages
   - Link relationships
   - Embed ClickUp tasks

4. **Knowledge Graph** (5 min, parallel with #1-3)
   - Analyze relationships
   - Create clusters
   - Update graph_relations

5. **Revenue Ops** (3 min, after Discovery)
   - Score all 712
   - Flag RED/YELLOW/GREEN
   - Create intervention tasks

**Total time to full execution: ~15-20 minutes**

---

## READY TO ACTIVATE?

All agents can start immediately:
- ✅ Supabase MCP connected
- ✅ ClickUp MCP connected  
- ✅ Notion MCP connected
- ✅ 712 ventures ready
- ✅ Relationships schema ready

**Trigger:**
```
Activate all 5 agent loops on 712 ventures
```
