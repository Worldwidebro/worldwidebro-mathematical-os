---
title: CLAUDE.md Distribution Across 5 Agent Loops
date: 2026-06-17
ventures: 712
purpose: Map all CLAUDE.md systems to agent execution loops
---

# 📊 CLAUDE.md → Agent Loops Distribution Map

## What's in CLAUDE.md (8 Major Systems)

| System | Lines | Content | Where Used |
|--------|-------|---------|-----------|
| Slack Integration | 6-13 | Post metrics, blockers, task status | All loops |
| Tailscale VPN | 15-235 | Private network infrastructure | Infrastructure only |
| Docker Services | 238-378 | Neo4j, Redis, Grafana, PostgreSQL | Infrastructure only |
| Worldwidebro Academy | 390-435 | 30-layer curriculum + content system | Loop 1 (Discovery) |
| Venture Handle Management | 438-467 | Git config per venture | Loop 2 (Task Auto) |
| Repository Intelligence | 470-525 | 1,592 repos × 10 attributes | Loop 4 (Knowledge Graph) |
| Unified Company Roadmap | 528-625 | 4-layer capital system, 12-month plan | Loop 5 (Revenue Ops) |
| Knowledge Graph & Scripts | 636-882 | Supabase sync, DuckDB, Chroma | Loop 4 + Loop 5 |
| Skill Execution Framework | 885+ | 296 skills × 14 phases | Loop 2 (Task Auto) |

---

## Loop 1: VENTURE DISCOVERY ← Distribution from CLAUDE.md

### Systems Used:
1. **Worldwidebro Academy (390-435)**
   - 30-layer curriculum for education ventures
   - Find ventures ready for content atomization

2. **Unified Company Roadmap (528-625)**
   - 4-layer capital system
   - Sector sequencing: Q1 = Construction/Staffing, Q2 = Real Estate/Education, etc.
   - Filter opportunities by layer + sector

3. **Slack Integration (6-13)**
   - Post top 10 opportunities to #niche-mastery
   - Format: "venture_id | opportunity_type | risk_level | layer"

### Loop 1 Pseudocode
```
FOR sector IN [construction, staffing, education, real_estate, finance]:
  construction_ventures = SUPABASE.ventures 
    WHERE sector=sector 
    AND stage IN [planned, validation] 
    AND health_score < 50
  
  SCORE each venture BY:
    - health_score
    - revenue_ytd  
    - growth_potential
    - capital_layer_fit
  
  RANK top 20 opportunities
  POST to Slack: "{venture_id} | Opportunity | Risk | Layer"
```

---

## Loop 2: TASK AUTOMATION ← Distribution from CLAUDE.md

### Systems Used:
1. **Skill Execution Framework (885+)**
   - 296 skills × 14 workflow phases
   - Map skills to ClickUp tasks
   - Set dependencies between tasks

2. **Venture Handle Management (438-467)**
   - venture_id → GitHub handle + email
   - Assign tasks to correct contact
   - Set git config per venture

3. **Knowledge Graph Scripts (636-882)**
   - venture_skill_roadmap table
   - Task dependencies and blocking relationships
   - Skill execution audit trail

### Loop 2 Pseudocode
```
FOR venture IN all_ventures:
  handle = GET venture_handle(venture.venture_id)
  SET_GIT_CONFIG(handle)
  
  roadmap = SUPABASE.venture_skill_roadmap 
    WHERE venture_id = venture.venture_id
  
  FOR skill_row IN roadmap ORDER BY planned_order:
    task = CREATE_CLICKUP_TASK(
      title = "[Phase {skill_phase}] {skill_name}",
      assigned_to = venture.owner_id,
      venture_id = venture.venture_id
    )
    
    FOR blocked_skill IN skill_row.blocks_skills:
      SET_TASK_DEPENDENCY(task → blocked_skill_task)
    
    LOG skill_execution(venture_id, "task_automation", "pending")
```

---

## Loop 3: NOTION SYNC ← Distribution from CLAUDE.md

### Systems Used:
1. **Knowledge Graph Scripts (636-882)**
   - ventures table (venture_id, name, sector, stage, owner_id, health_score, revenue_ytd)
   - graph_relations table (relationships between ventures)
   - venture_decisions table (opportunity scores)

2. **Unified Company Roadmap (528-625)**
   - 4-layer capital system
   - Add "layer" context to Notion pages

3. **Repository Intelligence (470-525)**
   - Top 3 repos per venture by strategic_value + reusability_score
   - Map repos to Notion "repos" property

### Loop 3 Pseudocode
```
ventures = SUPABASE.ventures

FOR batch OF 100 ventures IN ventures:
  FOR venture IN batch:
    notion_page = FIND_OR_CREATE_NOTION_PAGE(venture.venture_id)
    
    UPDATE notion_page WITH:
      sector: venture.sector
      stage: venture.stage
      owner: venture.owner_id
      health_score: venture.health_score
      layer: GET_CAPITAL_LAYER(venture)
      related_ventures: GRAPH_RELATIONS(venture.venture_id)
      repos: TOP_3_REPOS(venture.venture_id)
    
    SET last_synced = NOW()
```

---

## Loop 4: KNOWLEDGE GRAPH ← Distribution from CLAUDE.md

### Systems Used:
1. **Knowledge Graph & Scripts (636-882)**
   - populate_venture_knowledge_graph.py (extract entities + relationships)
   - obsidian_graph_sync.py (export to JSON)
   - graph_relations table (relationship types: "sells_to", "uses_tech_from", "sister_venture", etc.)

2. **Repository Intelligence (470-525)**
   - 10 attributes: PURPOSE, CATEGORY, CAPABILITIES, DEPENDENCIES, TECH_STACK, REUSABILITY_SCORE, REVENUE_POTENTIAL, STRATEGIC_VALUE, RELATED_VENTURES, RELATED_REPOS
   - Map repos to ventures by strategic_value + reusability

3. **Data Layer (703-776)**
   - DuckDB for fast analytics queries
   - Chroma for semantic search (embeddings for ventures, capabilities, components)
   - 3-layer system: Supabase (source) → DuckDB (analytics) → Chroma (semantic)

### Loop 4 Pseudocode
```
FOR venture IN all_ventures:
  # 1. Find sister ventures (same sector)
  sisters = SUPABASE.ventures WHERE sector=venture.sector
  FOR sister IN sisters LIMIT 5:
    CREATE_GRAPH_RELATION(
      from=venture.venture_id,
      to=sister.venture_id,
      type="sister_venture",
      strength=8
    )
  
  # 2. Map repos used by venture
  top_repos = GET_TOP_REPOS(venture.venture_id)
  FOR repo IN top_repos:
    other_ventures = FIND_VENTURES_USING_REPO(repo.repo_id)
    FOR other IN other_ventures:
      CREATE_GRAPH_RELATION(
        from=venture.venture_id,
        to=other.venture_id,
        type="uses_tech_from",
        strength=repo.strategic_value / 10
      )
  
  # 3. Semantic similarity (Chroma)
  similar = CHROMA.search(venture.name + venture.summary, n_results=5)
  FOR result IN similar:
    CREATE_GRAPH_RELATION(
      from=venture.venture_id,
      to=result.venture_id,
      type="complements",
      strength=result.distance
    )

# 4. Export to Obsidian
EXPORT_TO_OBSIDIAN({
  entities: all_ventures,
  relationships: SUPABASE.graph_relations
})
UPDATE_FILE('.planning/venture-hub-alignment.json', obsidian_data)
```

---

## Loop 5: REVENUE OPERATIONS ← Distribution from CLAUDE.md

### Systems Used:
1. **Unified Company Roadmap (528-625)**
   - 4-layer capital system: Layer 1 ($5-15K), Layer 2 ($20-30K), Layer 3 ($24-75K), Layer 4 ($8-15K)
   - 12-month revenue targets: Start $0, reach $57K-135K/month
   - 71-81 operational ventures by year-end
   - Sector execution order: Construction → Real Estate → Logistics → Government

2. **Knowledge Graph & Scripts (636-882)**
   - DuckDB queries for real-time aggregations
   - Calculate KPIs: CAC/LTV, churn_rate, burn_rate, health_score
   - Query: COUNT(*) GROUP BY sector, SUM(revenue_ytd), AVG(health_score)

3. **Data Layer (703-776)**
   - Supabase tables: ventures (revenue_ytd, costs_mom, health_score, cac, ltv, churn_rate)
   - DuckDB: Fast analytics + aggregations
   - Grafana: Real-time dashboards (configured, ready for metrics)

4. **Slack Integration (6-13)**
   - Post real-time metrics to #niche-mastery
   - Format: "venture | revenue_status | KPI | action_required"
   - Log: MRR, contacts, repos, task progress

### Loop 5 Pseudocode
```
ventures = DUCKDB.query("SELECT * FROM ventures")

# 1. Calculate health for all 712
FOR venture IN ventures:
  health = CALCULATE(
    (revenue_ytd / revenue_target) * 0.3 +
    (ltv / cac) * 0.3 +
    (1 - churn_rate) * 0.2 +
    (runway_months / 12) * 0.2
  )
  
  UPDATE_SUPABASE(ventures, {health_score: health}, venture.venture_id)

# 2. Group by layer and calculate totals
layer1_revenue = SUM(revenue_ytd) WHERE layer=1
layer2_revenue = SUM(revenue_ytd) WHERE layer=2
total_revenue = layer1_revenue + layer2_revenue

# 3. Assign risk colors
red_ventures = venues WHERE health_score < 40       # 🔴
yellow_ventures = ventures WHERE health_score 40-70 # 🟡
green_ventures = ventures WHERE health_score > 70   # 🟢

# 4. Post to Slack
POST #niche-mastery:
  "Current revenue: ${total_revenue}/month (target: $57K-135K)
   🔴 RED: {red_count}, 🟡 YELLOW: {yellow_count}, 🟢 GREEN: {green_count}
   Layer 1: ${layer1_revenue}, Layer 2: ${layer2_revenue}
   On track: {total_revenue >= 57000}"

# 5. Create intervention tasks for RED ventures
FOR venture IN red_ventures LIMIT 20:
  CREATE_CLICKUP_TASK(
    title="[URGENT] Revenue intervention: {venture.name}",
    assigned_to=venture.owner_id,
    priority=CRITICAL,
    description="Health: {health}. Revenue: ${revenue}. Intervention needed."
  )
```

---

## Complete Distribution Summary

```
CLAUDE.md (1,100+ lines)
    │
    ├─→ Loop 1 (Discovery)           [5 min]
    │   ├─ Worldwidebro Academy
    │   ├─ Unified Roadmap (4-layer)
    │   └─ Slack Integration
    │
    ├─→ Loop 2 (Task Automation)     [10 min]
    │   ├─ Skill Framework (296 skills × 14 phases)
    │   ├─ Venture Handles (git config)
    │   └─ Knowledge Graph (skill roadmap)
    │
    ├─→ Loop 3 (Notion Sync)         [15 min]
    │   ├─ Knowledge Graph (entity export)
    │   ├─ Unified Roadmap (layer context)
    │   └─ Repository Intelligence (top repos)
    │
    ├─→ Loop 4 (Knowledge Graph)     [5 min]
    │   ├─ Knowledge Graph (relationships)
    │   ├─ Repository Intelligence (10 attributes)
    │   ├─ Chroma (semantic search)
    │   └─ Obsidian (JSON export)
    │
    └─→ Loop 5 (Revenue Ops)         [3 min, continuous]
        ├─ Unified Roadmap (4-layer capital)
        ├─ Data Layer (DuckDB + Grafana)
        ├─ Slack Integration (KPI posting)
        └─ Intervention (RED venture tasks)
```

---

## How to Execute (Sequence)

**Run in this order:**

1. **Loop 1** (5 min) — Identify top 20 opportunities
   - ✅ Scan 712 ventures
   - ✅ Score by health + layer fit
   - ✅ Post to Slack

2. **Loop 2** (10 min) — Create tasks for those opportunities
   - ✅ Read skill roadmap
   - ✅ Create ClickUp tasks per phase
   - ✅ Assign to owner_id + set dependencies

3. **Loop 3** (15 min) — Sync all 712 to Notion
   - ✅ Create 712 Notion pages
   - ✅ Add properties (sector, stage, layer, health)
   - ✅ Link related ventures + repos

4. **Loop 4** (5 min) — Analyze relationships
   - ✅ Find sister ventures, tech dependencies
   - ✅ Score relationship strength
   - ✅ Export to Obsidian

5. **Loop 5** (continuous) — Monitor revenue + flag risks
   - ✅ Score all 712 daily
   - ✅ Flag RED/YELLOW/GREEN
   - ✅ Post to Slack
   - ✅ Create intervention tasks

---

## What's NOT Distributed (Infrastructure)

- **Tailscale VPN** (15-235): One-time setup, maintains all connections
- **Docker Services** (238-378): Skipped (not needed)
- **Slack Integration** (6-13): Used by all 5 loops for communication

---

## Ready to Run All 5 Loops?

**Yes. Everything is distributed and ready to execute on 712 ventures.**

Next: Activate the loops with:
```
All 5 agent loops activated on 712 ventures
Loop sequence: Discovery → Task Automation → Notion Sync → Knowledge Graph → Revenue Ops (continuous)
```
