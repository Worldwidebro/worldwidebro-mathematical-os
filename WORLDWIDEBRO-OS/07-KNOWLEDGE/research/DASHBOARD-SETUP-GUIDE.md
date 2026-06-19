# Real-Time Dashboard Setup Guide

**Complete guide to running the dual-layer skill execution dashboard system**

---

## Overview

This guide covers:
- **Obsidian Layer** — Developer dashboard (queries + Dataview blocks)
- **Grafana Layer** — Executive dashboard (metrics + monitoring)
- **Data Pipeline** — DuckDB analytics + refresh automation
- **Architecture** — How data flows from Supabase → Dashboards

Related: [[skill-execution-framework]] | [[SKILL-PROGRESS-DASHBOARD]] | [[SKILL-PROGRESS-BY-SECTOR]] | [[REPOSITORY-INTELLIGENCE-SYSTEM]] | [[OBSIDIAN-GRAPH-STACK]]

---

## Architecture

```
Supabase (Source of Truth)
├── skill_executions table
├── venture_skill_roadmap table
├── skill_taxonomy table
└── ventures table
    ↓
DuckDB (Analytics Cache)
└── worldwidebro_os.duckdb
    ├── venture_progress view
    ├── sector_progress view
    ├── skill_timing view
    └── phase_blockers view
        ↓
        ├→ Obsidian Dataview (Developer View)
        │   └── .planning/SKILL-PROGRESS-DASHBOARD.md
        │   └── .planning/SKILL-PROGRESS-BY-SECTOR.md
        │
        └→ Grafana (Executive View)
            ├── provisioning/dashboards/skill-execution.json
            └── provisioning/dashboards/venture-health.json
```

---

## Quick Start

### 1. Verify DuckDB Database

```bash
# Check if database exists
ls -lh /Users/acebless/Documents/worldwidebro_os.duckdb

# Test connection
duckdb /Users/acebless/Documents/worldwidebro_os.duckdb "SELECT COUNT(*) FROM ventures;"
```

### 2. View Obsidian Dashboard

1. Open Obsidian vault
2. Navigate to `.planning/SKILL-PROGRESS-DASHBOARD.md`
3. All 6 Dataview blocks should render automatically
4. Click [[SKILL-PROGRESS-BY-SECTOR]] for sector deep-dives

### 3. Access Grafana Dashboard

```bash
# Start Grafana (if not running)
docker run -d -p 3000:3000 grafana/grafana

# Open browser
open http://localhost:3000

# Default login: admin / admin
# Dashboards available:
# - Skill Execution Metrics
# - Venture Health Portfolio
```

---

## Data Refresh

### Automatic Refresh (Recommended)

Set up cron job for 5-minute refresh:

```bash
# Edit crontab
crontab -e

# Add this line:
*/5 * * * * /Users/acebless/.claude/hooks/dashboard-refresh-5m.sh
```

### Manual Refresh

```bash
# Run refresh immediately
bash /Users/acebless/.claude/hooks/dashboard-refresh-5m.sh

# Check log
tail -f /Users/acebless/.claude/hooks/dashboard-refresh.log
```

---

## SQL Analytics Queries

All queries live in: `/Users/acebless/Documents/WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/`

| Query | Purpose | Updates |
|-------|---------|---------|
| `venture_progress.sql` | Completion % by venture | Real-time |
| `sector_progress.sql` | Sector-wide metrics | Real-time |
| `skill_timing.sql` | Skill performance benchmarks | Every 5 min |
| `phase_blockers.sql` | Skills blocking progress | Real-time |

Run any query manually:

```bash
duckdb /Users/acebless/Documents/worldwidebro_os.duckdb < venture_progress.sql
```

---

## Obsidian Dashboard Features

### Block 1: Top 20 Ventures by Completion %
- Shows venture_name, sector, stage, completion_%, blockers
- Color coded: ✅ no blockers, ⚠️ X blockers

### Block 2: Sectors by Average Completion %
- Bar chart showing sector health
- 🟢 Green (>70%), 🟡 Amber (40-70%), 🔴 Red (<40%)

### Block 3: Phase Distribution
- Pie chart of ventures in each phase (1-14)
- Indicates if ventures are progressing through phases evenly

### Block 4: Slowest 10 Skills
- Skill execution timing analysis
- Shows avg/max time, failure rate, adoption

### Block 5: Top Blockers
- 🚨 CRITICAL (>10 instances), ⚠️ HIGH (5-10)
- Shows which skills need unblocking first

### Block 6: Real-Time Execution Feed
- Last 20 skill executions
- Spot patterns: failures at certain times, slow phases, etc.

---

## Grafana Dashboard Features

### Dashboard 1: Skill Execution Metrics

**Panels:**
1. Top Ventures by Skill Executions (line graph)
2. Ventures by Sector (pie chart)
3. Total Blocked Skills (gauge)
4. Top 15 Slowest Skills (bar chart)
5. Critical & High Priority Blockers (table)

**Use for:** Executive overview of skill execution health

### Dashboard 2: Venture Health Portfolio

**Panels:**
1. Venture Completion Status (line graph)
2. All Ventures Health Summary (detailed table)
3. Sector Health - Average Completion % (bar chart)

**Use for:** Portfolio-level monitoring + sector benchmarking

---

## Configuration Files

### DuckDB Datasource (Grafana)
```
File: grafana/provisioning/datasources/duckdb.yml
URL: localhost:5432
Database: worldwidebro_os.duckdb
```

### Grafana Dashboards
```
Directory: grafana/provisioning/dashboards/
Files:
- skill-execution.json (5 panels)
- venture-health.json (3 panels)
```

### Automation Hooks
```
Directory: .claude/hooks/
Files:
- dashboard-refresh-5m.sh (run every 5 min)
- dashboard-sync-duckdb.sh (sync Supabase → DuckDB)
```

---

## Metrics Explained

| Metric | Definition | Healthy Range |
|--------|-----------|---|
| **Completion %** | Skills completed / Total skills | 75-100% |
| **Current Phase** | Max skill phase completed | Progressive through phases |
| **Blocked Skills** | Count of skills with status='blocked' | < 2 per venture |
| **Avg Execution Time** | Average skill execution time | Varies by skill |
| **Failure Rate** | Failed / Total executions | < 5% |
| **Sector Avg** | Avg completion % across sector | > 70% |

---

## Troubleshooting

### Dashboard not showing data

**Problem:** Dataview blocks show errors or no data

**Solution:**
1. Verify DuckDB database exists: `ls -lh worldwidebro_os.duckdb`
2. Check Obsidian has JavaScript support enabled
3. Run manual query: `duckdb worldwidebro_os.duckdb < venture_progress.sql`
4. Check browser console for errors (Cmd+Option+J on Mac)

### Grafana dashboards empty

**Problem:** Grafana panels show "No data"

**Solution:**
1. Verify DuckDB datasource is configured correctly
2. Test datasource connection in Grafana UI (Data Sources → DuckDB → Test)
3. Check that SQL queries are valid (run manually in DuckDB CLI)
4. Verify data exists: `duckdb worldwidebro_os.duckdb "SELECT COUNT(*) FROM venture_skill_roadmap;"`

### Slow query performance

**Problem:** Queries take >5 seconds

**Solution:**
1. Check DuckDB indexes exist (see schema file)
2. Run ANALYZE command: `duckdb db.duckdb "ANALYZE;"`
3. Limit result set: add LIMIT clause to queries
4. Profile query: `EXPLAIN ANALYZE SELECT ...;`

### Refresh script not running

**Problem:** Cron job not executing

**Solution:**
1. Verify script is executable: `ls -la .claude/hooks/dashboard-refresh-5m.sh`
2. Check cron logs: `log stream --predicate 'process == "cron"'`
3. Test script manually: `bash /Users/acebless/.claude/hooks/dashboard-refresh-5m.sh`
4. Verify crontab entry: `crontab -l`

---

## Performance Optimization

### DuckDB Tuning

```sql
-- Optimize DuckDB settings
PRAGMA threads=4;
PRAGMA memory_limit='4GB';
PRAGMA default_null_order='nulls_last';

-- Analyze table statistics
ANALYZE venture_skill_roadmap;
ANALYZE skill_executions;
```

### Query Optimization

```sql
-- Use LIMIT for large result sets
SELECT * FROM venture_progress LIMIT 100;

-- Use indexes for WHERE clauses
SELECT * FROM skill_executions WHERE venture_id = 'SAAS-001';

-- Aggregate before joining
SELECT sector, AVG(completion_pct) 
FROM venture_progress 
GROUP BY sector;
```

---

## Integration with Skill Framework

- Framework: [[skill-execution-framework]]
- Obsidian Dashboard: [[SKILL-PROGRESS-DASHBOARD]]
- Sector Dashboards: [[SKILL-PROGRESS-BY-SECTOR]]
- Queries: `/WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/`
- Data: `skill_executions`, `venture_skill_roadmap`, `skill_taxonomy` tables
- Obsidian sync: Every 5 minutes via cron
- Grafana refresh: Real-time + on-demand via UI

---

## Next Steps

1. ✅ Set up cron job for 5-min refresh
2. ✅ Open Obsidian dashboard
3. ✅ Access Grafana dashboards
4. ⏳ (Future) Supabase → DuckDB sync trigger
5. ⏳ (Future) ML predictions for completion times
6. ⏳ (Future) Slack alerts for blockers

---

## Files Summary

| File | Purpose | Location |
|------|---------|----------|
| venture_progress.sql | Venture completion metrics | analytics-queries/ |
| sector_progress.sql | Sector aggregations | analytics-queries/ |
| skill_timing.sql | Performance benchmarks | analytics-queries/ |
| phase_blockers.sql | Blocking skills | analytics-queries/ |
| SKILL-PROGRESS-DASHBOARD.md | Obsidian dashboard | .planning/ |
| SKILL-PROGRESS-BY-SECTOR.md | Sector deep-dives | .planning/ |
| skill-execution.json | Grafana dashboard 1 | grafana/dashboards/ |
| venture-health.json | Grafana dashboard 2 | grafana/dashboards/ |
| duckdb.yml | Datasource config | grafana/datasources/ |
| dashboard-refresh-5m.sh | Refresh automation | .claude/hooks/ |
| DASHBOARD-SETUP-GUIDE.md | This guide | Documents/ |

---

## Navigation Hub

### Dashboard Pages
- 📊 [[SKILL-PROGRESS-DASHBOARD]] — Main overview (6 Dataview blocks)
- 🌍 [[SKILL-PROGRESS-BY-SECTOR]] — Sector deep-dives (31 tabs)
- 📚 [[skill-execution-framework]] — Framework documentation

### Quick Links
- 🔧 **Setup:** See "Quick Start" section above
- 🛠️ **Troubleshooting:** See "Troubleshooting" section above
- ⚡ **Refresh:** See "Data Refresh" section above
- 📈 **Grafana:** Open http://localhost:3000

### Support

For issues or questions:
- Check this guide's troubleshooting section
- Review [[skill-execution-framework]] for data structure + table schemas
- Review [[SKILL-PROGRESS-DASHBOARD]] for block explanations
- Review [[SKILL-PROGRESS-BY-SECTOR]] for sector views
- Run queries manually in DuckDB CLI
- Check logs: `tail -f .claude/hooks/dashboard-refresh.log`

---

## Wiki Graph

```
                    [[skill-execution-framework]]
                    (master reference doc)
                              ↓
                        (296 skills,
                    venture_skill_roadmap,
                     skill_executions)
                         ↙      ↘
                    ↙             ↘
        [[SKILL-PROGRESS-      [[SKILL-PROGRESS-
         DASHBOARD]]            BY-SECTOR]]
         (overview view)        (sector views)
                ↓                   ↓
        (6 dataview blocks)   (31 sector tabs)
                ↓                   ↓
            THIS FILE ←──────────────→
         (setup guide)
         (refresh guide)
         (troubleshooting)

