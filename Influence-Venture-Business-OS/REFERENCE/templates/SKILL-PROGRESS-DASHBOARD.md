# Skill Execution Progress Dashboard

**Real-time visualization of 712 venture skill roadmap execution**

Last refreshed: `=this.file.mtime`

---

## Overview

This dashboard tracks progress through 14-phase skill execution workflow across all ventures and sectors. Use this to:
- 🎯 **Monitor venture progress** — see which ventures are on track
- 📊 **Identify blockers** — find which skills are holding back progress
- ⏱️ **Optimize skill performance** — see which skills take longest
- 🚀 **Sector benchmarking** — compare sectors' progression

---

## Block 1: Top 20 Ventures by Completion %

Ventures closest to completion (highest completion percentage first)

```dataviewjs
const duckdb = require('duckdb');
const fs = require('fs');

// Read query file
const sql = fs.readFileSync('/Users/acebless/Documents/WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/venture_progress.sql', 'utf8');

// Execute via DuckDB
const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const results = conn.execute(sql).fetchAll();

// Transform to table format
const table = results.slice(0, 20).map(row => [
  row.venture_name,
  row.sector,
  row.venture_stage,
  `${row.completion_percentage}%`,
  `${row.completed_skills}/${row.total_planned_skills}`,
  row.current_max_phase,
  row.blocked_skills > 0 ? `⚠️ ${row.blocked_skills}` : '✅'
]);

dv.table(
  ['Venture', 'Sector', 'Stage', 'Complete', 'Progress', 'Phase', 'Blockers'],
  table
);
```

**Interpretation:**
- **Complete %:** How far through their skill roadmap (0-100%)
- **Progress:** Completed skills / Total planned skills
- **Phase:** Current maximum skill phase (1-14)
- **Blockers:** ⚠️ = X skills blocked, ✅ = none blocked

---

## Block 2: Sectors by Average Completion %

Bar chart: which sectors are progressing fastest

```dataviewjs
const duckdb = require('duckdb');
const fs = require('fs');

// Read query
const sql = fs.readFileSync('/Users/acebless/Documents/WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/sector_progress.sql', 'utf8');

const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const results = conn.execute(sql).fetchAll();

// Create bar chart
const data = {
  labels: results.map(r => r.sector),
  datasets: [{
    label: 'Avg Completion %',
    data: results.map(r => r.avg_completion_percentage),
    backgroundColor: results.map(r => 
      r.avg_completion_percentage > 70 ? '#10b981' :
      r.avg_completion_percentage > 40 ? '#f59e0b' :
      '#ef4444'
    )
  }]
};

dv.bar(data);
```

**Color Legend:**
- 🟢 **Green (>70%):** Sector is progressing well
- 🟡 **Amber (40-70%):** Sector is mid-progress
- 🔴 **Red (<40%):** Sector needs attention

---

## Block 3: Phase Distribution Across All Ventures

Pie chart: how many ventures are in each phase

```dataviewjs
const duckdb = require('duckdb');

const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const results = conn.execute(`
  SELECT 
    skill_phase,
    COUNT(DISTINCT venture_id) as ventures_in_phase
  FROM venture_skill_roadmap
  GROUP BY skill_phase
  ORDER BY skill_phase ASC
`).fetchAll();

const phaseNames = [
  'Setup', 'Research', 'Strategy', 'Planning', 'Design', 
  'Implementation', 'Testing', 'Polish', 'Documentation', 
  'Release', 'Growth', 'Operations', 'Advanced', 'Domain'
];

const data = {
  labels: results.map((r, i) => `Phase ${r.skill_phase}: ${phaseNames[r.skill_phase - 1]}`),
  datasets: [{
    data: results.map(r => r.ventures_in_phase),
    backgroundColor: [
      '#3b82f6', '#8b5cf6', '#ec4899', '#f97316',
      '#eab308', '#84cc16', '#22c55e', '#10b981',
      '#14b8a6', '#06b6d4', '#0ea5e9', '#6366f1',
      '#a855f7', '#d946ef'
    ]
  }]
};

dv.pie(data);
```

**What this shows:**
- Each slice = ventures in that phase
- Larger slices = more ventures at that phase
- Ideally should be a smooth distribution (not bunched in early phases)

---

## Block 4: Slowest 10 Skills (Execution Time)

Which skills take longest to complete

```dataviewjs
const duckdb = require('duckdb');
const fs = require('fs');

const sql = fs.readFileSync('/Users/acebless/Documents/WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/skill_timing.sql', 'utf8');

const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const results = conn.execute(sql).fetchAll();

// Filter for only executed skills and sort by avg time
const slowest = results
  .filter(r => r.total_executions > 0)
  .slice(0, 10);

const table = slowest.map(row => [
  row.skill_name,
  row.skill_phase,
  row.total_executions,
  `${row.avg_execution_seconds}s`,
  `${row.max_execution_seconds}s`,
  `${row.failure_rate_percent}%`,
  row.unique_ventures_using
]);

dv.table(
  ['Skill', 'Phase', 'Runs', 'Avg Time', 'Max Time', 'Failure %', 'Used By'],
  table
);
```

**Interpretation:**
- **Avg Time:** How long does this skill typically take?
- **Max Time:** Worst-case execution (may indicate waiting on external services)
- **Failure %:** How often does this skill fail?
- **Used By:** Number of different ventures that have run this skill

---

## Block 5: Top Blockers

Skills that are holding back the most ventures

```dataviewjs
const duckdb = require('duckdb');
const fs = require('fs');

const sql = fs.readFileSync('/Users/acebless/Documents/WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/phase_blockers.sql', 'utf8');

const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const results = conn.execute(sql).fetchAll();

// Filter only CRITICAL and HIGH severity
const criticalBlockers = results.filter(r => 
  r.severity === 'CRITICAL' || r.severity === 'HIGH'
);

if (criticalBlockers.length === 0) {
  dv.paragraph('✅ No critical blockers detected!');
} else {
  const table = criticalBlockers.map(row => [
    row.severity === 'CRITICAL' ? '🚨' : '⚠️',
    row.skill_name,
    row.skill_phase,
    row.total_blocked_instances,
    row.distinct_ventures_blocked,
    row.avg_days_blocked
  ]);
  
  dv.table(
    ['', 'Skill', 'Phase', 'Blocked', 'Ventures', 'Days'],
    table
  );
}
```

**What this shows:**
- 🚨 **CRITICAL:** >10 instances of this skill blocked
- ⚠️ **HIGH:** 5-10 instances blocked
- **Days:** How long have ventures been waiting

---

## Block 6: Real-Time Execution Feed

Last 20 skill executions across all ventures

```dataviewjs
const duckdb = require('duckdb');

const conn = duckdb.connect('/Users/acebless/Documents/worldwidebro_os.duckdb');
const results = conn.execute(`
  SELECT 
    venture_id,
    skill_name,
    skill_phase,
    status,
    ROUND(execution_time_ms / 1000, 2) as duration_seconds,
    completed_at,
    error_message
  FROM skill_executions
  ORDER BY completed_at DESC
  LIMIT 20
`).fetchAll();

const table = results.map(row => [
  row.venture_id,
  row.skill_name,
  row.skill_phase,
  row.status === 'completed' ? '✅' : '❌',
  `${row.duration_seconds}s`,
  row.completed_at ? new Date(row.completed_at).toLocaleString() : '-'
]);

dv.table(
  ['Venture', 'Skill', 'Phase', 'Status', 'Duration', 'Time'],
  table
);
```

**What this shows:**
- Real-time stream of which skills just executed
- ✅ = Success, ❌ = Failed
- Use to spot patterns (e.g., Phase 6 always fails around 3pm)

---

## Dashboard Refresh

This dashboard auto-refreshes data from:
- **Source:** Supabase (skill_executions, venture_skill_roadmap)
- **Cache:** DuckDB (worldwidebro_os.duckdb)
- **Refresh Rate:** Every 5 minutes (via cron job)

**Last sync:** See timestamp at top of page

**Manual refresh:**
```bash
bash /Users/acebless/.claude/hooks/dashboard-refresh-5m.sh
```

---

## Metadata

- **Database:** /Users/acebless/Documents/worldwidebro_os.duckdb
- **Queries:** /Users/acebless/Documents/WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/
- **Related:** [[SKILL-PROGRESS-BY-SECTOR]]
- **Skill Framework:** [[skill-execution-framework]]

