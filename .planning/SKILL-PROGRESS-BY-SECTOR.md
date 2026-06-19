# Skill Progress by Sector

**Deep-dive dashboards for each of 31 sectors**

Related: [[SKILL-PROGRESS-DASHBOARD]] | [[DASHBOARD-SETUP-GUIDE]] | [[skill-execution-framework]]

---

## Sector Overview Table

Shows completion % by sector for all 31 sectors.

| Sector | Ventures | Avg Complete | Fully Done | Blockers |
|--------|----------|--------------|-----------|----------|
| [All 31 sectors listed] | | | | |

---

## Individual Sector Dashboards

### AI & Machine Learning
[Dataview block: all ventures in this sector with completion %]

### Automation & Workflow
[Similar block]

### Business Services
[Similar block]

### Construction
[Similar block with construction venture data]

### SaaS & Software
[Similar block with SaaS venture data]

... (remaining 26 sectors follow same pattern)

---

## Sector Health Summary

| Metric | Calculation |
|--------|-------------|
| **Health Score** | (Avg Completion % × 0.7) + (1 - Blocker Ratio) × 0.3 |
| **Status** | 🟢 >80 = Good, 🟡 50-80 = Medium, 🔴 <50 = Critical |
| **Key Blocker** | Skill blocking most ventures in sector |
| **Fastest Phase** | Phase with highest completion % in sector |

---

## Navigation

### Related Dashboards
- 📊 [[SKILL-PROGRESS-DASHBOARD]] — Overall ventures + sectors overview
- 📚 [[DASHBOARD-SETUP-GUIDE]] — Setup, refresh, and troubleshooting
- 🏗️ [[skill-execution-framework]] — Framework + 296 skills reference

### Data Pipeline
- 🔍 **Analytics Queries:** /WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/
- 📋 **Sector SQL:** sector_progress.sql
- 💾 **Database:** DuckDB (worldwidebro_os.duckdb)

### Grafana Equivalent
- 📈 Venture Health Portfolio dashboard shows cross-sector metrics
- 🎯 Drill-down filtering by sector (Grafana variable)

---

## Export Data

Export sector data to CSV:

```bash
duckdb /Users/acebless/Documents/worldwidebro_os.duckdb << 'SQL'
COPY (
  SELECT v.sector, v.venture_name, 
    COUNT(*) as total_skills,
    COUNT(CASE WHEN vsr.status='completed' THEN 1 END) as completed
  FROM venture_skill_roadmap vsr
  JOIN ventures v ON vsr.venture_id = v.venture_id
  GROUP BY v.sector, v.venture_name
) TO 'sector_progress.csv' (FORMAT CSV, HEADER TRUE);
SQL
```

