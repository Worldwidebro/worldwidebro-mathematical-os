# Skill Progress by Sector

**Deep-dive dashboards for each of 31 sectors**

---

## How to Use This Dashboard

Each sector has its own detailed view showing:
- All ventures in that sector with their progress %
- Phase distribution for that sector
- Sector-specific blockers
- Which skills are most used in this sector

---

## Sector Overview Table

```dataviewjs
const duckdb = require('duckdb');
const fs = require('fs');

const sql = fs.readFileSync('/Users/acebless/Documents/WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/sector_progress.sql', 'utf8');

const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const results = conn.execute(sql).fetchAll();

const table = results.map(row => [
  row.sector,
  row.total_ventures,
  `${row.avg_completion_percentage}%`,
  row.ventures_completed,
  row.total_blocked_skills > 0 ? `⚠️ ${row.total_blocked_skills}` : '✅'
]);

dv.table(
  ['Sector', 'Ventures', 'Avg Complete', 'Fully Done', 'Blockers'],
  table
);
```

---

## All 31 Sectors

| # | Sector | Dashboard |
|----|--------|-----------|
| 1 | AI & Machine Learning | [[#AI & Machine Learning]] |
| 2 | Automation & Workflow | [[#Automation & Workflow]] |
| 3 | Business Services | [[#Business Services]] |
| 4 | Construction | [[#Construction]] |
| 5 | Content & Media | [[#Content & Media]] |
| 6 | Cryptocurrency & Blockchain | [[#Crypto & Blockchain]] |
| 7 | Education & Training | [[#Education & Training]] |
| 8 | Energy & Sustainability | [[#Energy & Sustainability]] |
| 9 | Equipment & Logistics | [[#Equipment & Logistics]] |
| 10 | Finance & Fintech | [[#Finance & Fintech]] |
| 11 | Food & Agriculture | [[#Food & Agriculture]] |
| 12 | Government & Compliance | [[#Government & Compliance]] |
| 13 | Healthcare & Wellness | [[#Healthcare & Wellness]] |
| 14 | Hospitality & Travel | [[#Hospitality & Travel]] |
| 15 | HR & Payroll | [[#HR & Payroll]] |
| 16 | Legal & IP | [[#Legal & IP]] |
| 17 | Marketing & Advertising | [[#Marketing & Advertising]] |
| 18 | Manufacturing | [[#Manufacturing]] |
| 19 | Marketplace & E-commerce | [[#Marketplace & E-commerce]] |
| 20 | Music & Entertainment | [[#Music & Entertainment]] |
| 21 | Network & Infrastructure | [[#Network & Infrastructure]] |
| 22 | Payments & Transactions | [[#Payments & Transactions]] |
| 23 | Real Estate | [[#Real Estate]] |
| 24 | Recruitment & Staffing | [[#Recruitment & Staffing]] |
| 25 | Retail & Commerce | [[#Retail & Commerce]] |
| 26 | Sales & CRM | [[#Sales & CRM]] |
| 27 | SaaS & Software | [[#SaaS & Software]] |
| 28 | Social & Community | [[#Social & Community]] |
| 29 | Supply Chain | [[#Supply Chain]] |
| 30 | Transportation | [[#Transportation]] |
| 31 | Video & Streaming | [[#Video & Streaming]] |

---

## AI & Machine Learning

```dataviewjs
const duckdb = require('duckdb');
const sector = 'AI & Machine Learning';
const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const ventures = conn.execute(`
  SELECT 
    v.venture_id, v.venture_name, v.stage,
    COUNT(*) as total_skills,
    COUNT(CASE WHEN vsr.status='completed' THEN 1 END) as completed,
    ROUND(COUNT(CASE WHEN vsr.status='completed' THEN 1 END)::FLOAT / NULLIF(COUNT(*), 0) * 100, 2) as completion_pct
  FROM venture_skill_roadmap vsr
  JOIN ventures v ON vsr.venture_id = v.venture_id
  WHERE v.sector = '${sector}'
  GROUP BY v.venture_id, v.venture_name, v.stage
  ORDER BY completion_pct DESC
`).fetchAll();

if (ventures.length > 0) {
  const table = ventures.map(v => [v.venture_name, v.stage, `${v.completion_pct}%`, `${v.completed}/${v.total_skills}`]);
  dv.table(['Venture', 'Stage', 'Complete', 'Progress'], table);
} else {
  dv.paragraph('No ventures in this sector');
}
```

---

## Automation & Workflow

[Similar block as above, replace sector name]

---

## Business Services

[Similar block as above, replace sector name]

---

## Construction

```dataviewjs
const duckdb = require('duckdb');
const sector = 'Construction';
const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const ventures = conn.execute(`
  SELECT 
    v.venture_id, v.venture_name, v.stage,
    COUNT(*) as total_skills,
    COUNT(CASE WHEN vsr.status='completed' THEN 1 END) as completed,
    ROUND(COUNT(CASE WHEN vsr.status='completed' THEN 1 END)::FLOAT / NULLIF(COUNT(*), 0) * 100, 2) as completion_pct
  FROM venture_skill_roadmap vsr
  JOIN ventures v ON vsr.venture_id = v.venture_id
  WHERE v.sector = '${sector}'
  GROUP BY v.venture_id, v.venture_name, v.stage
  ORDER BY completion_pct DESC
`).fetchAll();

if (ventures.length > 0) {
  const table = ventures.map(v => [v.venture_name, v.stage, `${v.completion_pct}%`, `${v.completed}/${v.total_skills}`]);
  dv.table(['Venture', 'Stage', 'Complete', 'Progress'], table);
} else {
  dv.paragraph('No ventures in this sector');
}
```

---

## SaaS & Software

```dataviewjs
const duckdb = require('duckdb');
const sector = 'SaaS & Software';
const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const ventures = conn.execute(`
  SELECT 
    v.venture_id, v.venture_name, v.stage,
    COUNT(*) as total_skills,
    COUNT(CASE WHEN vsr.status='completed' THEN 1 END) as completed,
    ROUND(COUNT(CASE WHEN vsr.status='completed' THEN 1 END)::FLOAT / NULLIF(COUNT(*), 0) * 100, 2) as completion_pct
  FROM venture_skill_roadmap vsr
  JOIN ventures v ON vsr.venture_id = v.venture_id
  WHERE v.sector = '${sector}'
  GROUP BY v.venture_id, v.venture_name, v.stage
  ORDER BY completion_pct DESC
`).fetchAll();

if (ventures.length > 0) {
  const table = ventures.map(v => [v.venture_name, v.stage, `${v.completion_pct}%`, `${v.completed}/${v.total_skills}`]);
  dv.table(['Venture', 'Stage', 'Complete', 'Progress'], table);
} else {
  dv.paragraph('No ventures in this sector');
}
```

---

## Sector Health Summary

| Metric | Calculation |
|--------|-------------|
| **Health Score** | (Avg Completion % × 0.7) + (1 - Blocker Ratio) × 0.3 |
| **Status** | 🟢 >80 = Good, 🟡 50-80 = Medium, 🔴 <50 = Critical |
| **Key Blocker** | Skill blocking most ventures in sector |
| **Fastest Phase** | Phase with highest completion % in sector |

---

## Export & Analysis

Export sector data:
```bash
duckdb /Users/acebless/Documents/worldwidebro_os.duckdb << 'SQL'
COPY (
  SELECT v.sector, v.venture_name, COUNT(*) as total_skills,
    COUNT(CASE WHEN vsr.status='completed' THEN 1 END) as completed
  FROM venture_skill_roadmap vsr
  JOIN ventures v ON vsr.venture_id = v.venture_id
  GROUP BY v.sector, v.venture_name
) TO 'sector_progress.csv' (FORMAT CSV, HEADER TRUE);
SQL
```

---

## Related

- [[SKILL-PROGRESS-DASHBOARD]] — Overall dashboard
- [[skill-execution-framework]] — Framework documentation
- Queries: /WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/

