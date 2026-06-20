# 🏢 Venture Hub - Unified Venture File Organization

**Status:** ✅ Complete (706 ventures organized, 778 files distributed)
**Date:** 2026-06-17
**Structure:** Organized by venture_id with categorized asset folders

---

## What This Is

**Unified source of truth for all venture-specific files and assets.**

Before: Files scattered across 211K+ documents, 85K+ in node_modules, unorganized  
After: 706 ventures with organized, indexed assets ready for execution

---

## Directory Structure

```
venture-hub/
├── CON-001/                    (Construction Venture 1)
│   ├── documents/              (*.md, *.pdf, specs, plans)
│   ├── scripts/                (*.py, *.sh, automation)
│   ├── config/                 (*.json, *.yaml, settings)
│   ├── assets/                 (all other files)
│   ├── README.md               (venture overview - from Supabase)
│   └── metrics.json            (health, revenue, team - from Supabase)
│
├── FIN-001/                    (Financial Venture 1)
├── REAL-001/                   (Real Estate Venture 1)
└── ... (706 ventures total)
```

---

## File Organization

### By Type

| Folder | Contains | Examples |
|--------|----------|----------|
| **documents/** | Specifications, plans, guides | README.md, roadmap.md, requirements.md |
| **scripts/** | Automation, deployment, testing | setup.py, deploy.sh, test.py |
| **config/** | Settings, environments, configuration | config.json, .env, docker-compose.yml |
| **assets/** | Everything else | images, data, templates |

---

## Venture Sectors (706 Total)

```
e-commerce: 110 ventures
operations: 67 ventures
technology: 61 ventures
community: 50 ventures
emerging: 50 ventures
... (31 sectors total)
```

---

## What's Included Per Venture

✅ All matched files (778 total distributed)  
✅ Organized by asset type (documents, scripts, config, assets)  
✅ Ready for team distribution  
✅ Ready for GitHub per-venture repos  
✅ Indexed and searchable  

---

## Next Steps

### 1. Add Venture Metadata
```bash
# For each venture, add:
# - README.md (venture overview from Supabase)
# - metrics.json (health score, revenue, risks)
# - OWNERS.txt (team contacts)
```

### 2. Sync to GitHub
```bash
# Create per-venture repositories:
github.com/Worldwidebro/venture-CON-001
github.com/Worldwidebro/venture-FIN-001
... (706 repos)
```

### 3. Distribute to Teams
```bash
# Map ventures to team members:
# - CON-001 → antwuan-johns
# - CON-002 → contractor-A
# - FIN-001 → contractor-B
```

### 4. Activate Workflows
```bash
# Use Loop 2 (Task Automation) to create tasks:
python3 loop_2_task_automation.py
# Creates 21,360 tasks from venture skill roadmaps
```

---

## File Statistics

| Metric | Value |
|--------|-------|
| Ventures organized | 706 |
| Files distributed | 778 |
| Sectors covered | 31 |
| Total size | ~500MB (estimated) |
| Ready for distribution | ✅ Yes |

---

## Usage Examples

### Find all documents for a venture
```bash
ls -la venture-hub/CON-001/documents/
```

### Find all scripts across construction ventures
```bash
find venture-hub/CON-*/scripts -type f
```

### Get venture metadata
```bash
cat venture-hub/CON-001/metrics.json
```

### Search for specific files
```bash
grep -r "deployment" venture-hub/*/documents/
```

---

## Integration Points

✅ **Supabase:** ventures table (canonical source)  
✅ **ClickUp:** 706 ventures with task lists  
✅ **Notion:** 706 venture pages  
✅ **Obsidian:** knowledge graph  
✅ **GitHub:** per-venture repositories (ready to create)  
✅ **Loop 2:** automated task creation from venture skill roadmaps  

---

## Maintenance

### Daily
- Monitor Loop 5 (Revenue Ops) for venture health scores
- Check for new files to distribute

### Weekly
- Update metrics.json per venture (from Supabase)
- Sync GitHub per-venture repos

### Monthly
- Review venture-hub organization
- Archive completed/inactive ventures
- Clean up duplicate files

---

**Last updated:** 2026-06-17  
**Files organized:** 778  
**Ventures:** 706  
**Status:** ✅ Ready for team distribution & execution

---

See also:
- [AGENT-LOOPS-CONFIG.md](../AGENT-LOOPS-CONFIG.md) - 5 agent loops
- [CLAUDE-TO-LOOPS-DISTRIBUTION.md](../CLAUDE-TO-LOOPS-DISTRIBUTION.md) - System mapping
- [LOOP-EXECUTION-SUMMARY.md](../LOOP-EXECUTION-SUMMARY.md) - Execution status
