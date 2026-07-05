# Skill Execution Progress Dashboard

**Real-time visualization of 712 venture skill roadmap execution**

Last refreshed: `=this.file.mtime`

---

## Overview

This dashboard tracks progress through 14-phase skill execution workflow across all ventures and sectors.

Related: [[skill-execution-framework]] | [[SKILL-PROGRESS-BY-SECTOR]] | [[DASHBOARD-SETUP-GUIDE]]

---

## Block 1: Top 20 Ventures by Completion %

| Venture | Sector | Stage | Complete | Progress | Phase | Blockers |
|---------|--------|-------|----------|----------|-------|----------|
| [Show top 20 ventures sorted by completion %] | | | | | | |

**Interpretation:**
- **Complete %:** How far through their skill roadmap (0-100%)
- **Progress:** Completed skills / Total planned skills
- **Phase:** Current maximum skill phase (1-14)
- **Blockers:** ⚠️ = X skills blocked, ✅ = none blocked

---

## Block 2: Sectors by Average Completion %

Bar chart showing which sectors are progressing fastest.

**Color Legend:**
- 🟢 **Green (>70%):** Sector is progressing well
- 🟡 **Amber (40-70%):** Sector is mid-progress
- 🔴 **Red (<40%):** Sector needs attention

---

## Block 3: Phase Distribution Across All Ventures

Pie chart showing how many ventures are in each phase (1-14).

---

## Block 4: Slowest 10 Skills (Execution Time)

Which skills take longest to complete.

---

## Block 5: Top Blockers

Skills that are holding back the most ventures.

- 🚨 **CRITICAL:** >10 instances blocked
- ⚠️ **HIGH:** 5-10 instances blocked

---

## Block 6: Real-Time Execution Feed

Last 20 skill executions across all ventures.

---

## Dashboard Refresh

**Automatic:** Every 5 minutes via cron job
**Manual:** `bash /Users/acebless/.claude/hooks/dashboard-refresh-5m.sh`

---

## Navigation

### Related Dashboards
- 🌍 [[SKILL-PROGRESS-BY-SECTOR]] — Drill into individual sectors (31 total)
- 📚 [[DASHBOARD-SETUP-GUIDE]] — Setup instructions + troubleshooting
- 🏗️ [[skill-execution-framework]] — Framework documentation + 296 skills

### Data & Tools
- 📊 **Database:** /Users/acebless/Documents/worldwidebro_os.duckdb
- 🔍 **Queries:** /WORLDWIDEBRO-OS/08_RESEARCH/analytics-queries/
- 📈 **Grafana:** Skill Execution Metrics dashboard (http://localhost:3000)

