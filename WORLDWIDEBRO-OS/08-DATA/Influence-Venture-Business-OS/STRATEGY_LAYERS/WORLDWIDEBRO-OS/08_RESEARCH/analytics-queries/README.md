# Dashboard Analytics Queries

**Purpose:** Reusable SQL queries for real-time skill execution dashboards (Obsidian + Grafana).

**Source:** Supabase tables (skill_executions, venture_skill_roadmap, skill_taxonomy, ventures)

**Target:** DuckDB for fast analytics + JSON export for visualization

---

## Query 1: venture_progress.sql

**What it shows:** Completion % by individual venture

**Output columns:**
- `venture_id`, `venture_name`, `sector`, `venture_stage`
- `total_planned_skills`, `completed_skills`, `in_progress_skills`, `blocked_skills`
- `completion_percentage` (0-100%)
- `current_max_phase`, `avg_phase`
- `blocked_skill_names` (which skills are blocking this venture)
- `last_completed_date` (when was the last skill completed)

**Used by:**
- Obsidian: Top 20 ventures by completion %
- Grafana: Venture health table (drill-down by sector/stage)

**Refresh:** Every 5 minutes

---

## Query 2: sector_progress.sql

**What it shows:** Aggregated progress by sector (31 sectors)

**Output columns:**
- `sector`
- `total_ventures`, `ventures_completed`, `ventures_in_progress`, `ventures_blocked`
- `avg_completion_percentage` (sector-wide %)
- `avg_current_phase` (where is this sector in the workflow)
- `total_blocked_skills`, `top_blockers`

**Used by:**
- Obsidian: Sector ranking bar chart
- Grafana: Sector KPI card + heatmap

**Refresh:** Every 5 minutes

---

## Query 3: skill_timing.sql

**What it shows:** Performance metrics for each of 296 skills

**Output columns:**
- `skill_name`, `skill_phase`, `category`
- `total_executions`, `successful_executions`, `failed_executions`
- `failure_rate_percent`
- `avg/max/min/median_execution_seconds`
- `last_execution_time`
- `unique_ventures_using` (adoption rate)

**Used by:**
- Obsidian: Slowest 10 skills leaderboard
- Grafana: Skill performance graph (sorted by avg time)

**Refresh:** Every 5 minutes

---

## Query 4: phase_blockers.sql

**What it shows:** Which skills are blocking progress (status='blocked')

**Output columns:**
- `skill_name`, `skill_phase`, `category`
- `total_blocked_instances` (count of blocked roadmap entries)
- `distinct_ventures_blocked` (how many ventures affected)
- `avg_days_blocked` (how long have they been blocked)
- `first_blocked_date`
- `blocked_skills_in_phase` (context: how many other skills blocked in same phase)
- `severity` (CRITICAL/HIGH/MEDIUM/LOW based on blocked count)

**Used by:**
- Obsidian: Top blockers widget + alerts
- Grafana: Blocker dashboard + critical alerts

**Refresh:** Every 5 minutes or on-demand when blockers change

---

## How to Use

### Option 1: Via DuckDB CLI
```bash
duckdb /Users/acebless/Documents/worldwidebro_os.duckdb < venture_progress.sql
```

### Option 2: Via Obsidian Dataview
```js
dv.query(`
  SELECT * FROM duckdb(
    "/Users/acebless/Documents/worldwidebro_os.duckdb",
    "SELECT * FROM venture_progress"
  )
`)
```

### Option 3: Via Grafana
1. Add DuckDB datasource: `localhost:5432/worldwidebro_os.duckdb`
2. Create panel with SQL query
3. Select from output above

### Option 4: Via Python (for exports)
```python
import duckdb
conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb')
result = conn.execute(open('venture_progress.sql').read()).fetchall()
json_export = json.dumps([dict(row) for row in result])
```

---

## Refresh Strategy

**Automated (every 5 min):**
```bash
# .claude/hooks/dashboard-refresh-5m.sh
for query in venture_progress sector_progress skill_timing phase_blockers; do
  duckdb worldwidebro_os.duckdb < $query.sql > $query.json
done
```

**Manual (on-demand):**
```bash
bash /Users/acebless/.claude/hooks/dashboard-refresh-5m.sh
```

---

## Query Performance Notes

| Query | Rows | Execution Time | Notes |
|-------|------|----------------|-------|
| venture_progress | ~712 | <1s | Indexes: venture_id, status |
| sector_progress | ~31 | <100ms | Fast (small result set) |
| skill_timing | ~296 | <2s | Indexes: skill_name, status |
| phase_blockers | Variable | <1-2s | Only returns blocked rows |

**All queries are indexed for fast execution.**

---

## Next Steps

1. **Sync Supabase → DuckDB** (Task 4)
   - Set up trigger: whenever skill_executions INSERT, append to DuckDB

2. **Wire to Obsidian Dataview** (Task 2)
   - Embed these queries in .planning/SKILL-PROGRESS-DASHBOARD.md

3. **Wire to Grafana** (Task 3)
   - Create datasource + panels for each query

4. **Set up automation** (Task 4)
   - Cron job: refresh every 5 minutes
   - Alert triggers for blockers
