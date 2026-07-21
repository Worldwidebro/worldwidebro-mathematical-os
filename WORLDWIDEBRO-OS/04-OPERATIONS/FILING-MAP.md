# Filing Map: Consolidate Scattered Docs into WORLDWIDEBRO-OS

**Problem:** ~110 files scattered in `/Documents` root. No structure.  
**Solution:** Move into WORLDWIDEBRO-OS by category.

---

## Quick Map

| Category | Target Folder | Count | Files |
|----------|---|---|---|
| **Operations** | `/04-OPERATIONS/EXECUTION/` | 30 | PHASE-1B-INTEGRATED-BLUEPRINT, OS-BUILD-GUIDE, OPERATIONS-RUNBOOK, etc. |
| **Infrastructure** | `/04-OPERATIONS/INFRASTRUCTURE/WIRING/` | 25 | A1-A3, B1-B4, C1-C4, D1-D2 wiring files |
| **Knowledge** | `/07-KNOWLEDGE/PLAYBOOKS/` | 20 | 4-WEEK-RESEARCH-PLAN, REPO-INTELLIGENCE, FRAMEWORK-ANALYSIS, etc. |
| **Ventures** | `/03-PORTFOLIO/ventures/active/{ID}/docs/` | 15 | CON-001-*, OPS-001-*, EC-111-* venture-specific docs |
| **Strategy** | `/02-GOVERNANCE/STRATEGY/` | 12 | LIVE-SITES-INDEX, PAGES-AND-AGENTS-ROADMAP, SECTOR-PAGES-*, etc. |
| **References** | `/07-KNOWLEDGE/REFERENCES/` | 8 | SUPABASE-SQL-REFERENCE, AGENT-OPERATIONS, policy_engine-REFERENCE |
| **Activation** | `/04-OPERATIONS/ACTIVATION/` | 3 | TECH-VENTURES-ACTIVATION-*.json, VENTURE-DEPENDENCY-RESOLUTION |

**Total:** ~110 files → consolidated into 7 categories

---

## Stay in /Documents Root (Symlinks)

- `AGENTS.md` → `/04-OPERATIONS/IZA-OS/AGENTS.md`
- `CLAUDE.md` → `AGENTS.md`
- `STATE.md` → `/04-OPERATIONS/STATE.md` (single source of truth)

---

## Example Consolidation

### Before (Scattered)
```
/Documents/
  PHASE-1B-INTEGRATED-BLUEPRINT.md
  OS-BUILD-GUIDE-SPRINT-1.md
  OPERATIONS-PLAYBOOK-CONSOLIDATED.md
  A1-OTEL-COLLECTOR-WIRING.md
  B1-AGENT-TOOL-WIRING-USAGE.md
  4-WEEK-RESEARCH-PLAN.md
  CON-001-AUTOMATION-PLAN.md
  [+100 more scattered files]
```

### After (Organized)
```
/WORLDWIDEBRO-OS/
  02-GOVERNANCE/STRATEGY/
    LIVE-SITES-INDEX.md
    PAGES-AND-AGENTS-ROADMAP.md
  03-PORTFOLIO/ventures/active/
    CON-001/docs/
      AUTOMATION-PLAN.md
      AUTOMATION-COST-BREAKDOWN.md
    OPS-001/docs/
      WOTC-REGISTRATION-GUIDE.md
  04-OPERATIONS/
    EXECUTION/
      PHASE-1B-INTEGRATED-BLUEPRINT.md ✅
      OS-BUILD-GUIDE-SPRINT-1.md
      OPERATIONS-PLAYBOOK-CONSOLIDATED.md
    INFRASTRUCTURE/WIRING/
      A1-OTEL-COLLECTOR-WIRING.md
      B1-AGENT-TOOL-WIRING-USAGE.md
    ACTIVATION/
      TECH-VENTURES-ACTIVATION-PLAN.json
  07-KNOWLEDGE/
    PLAYBOOKS/
      4-WEEK-RESEARCH-PLAN.md
      REPO-INTELLIGENCE-COMPLETION-GUIDE.md
    REFERENCES/
      SUPABASE-SQL-REFERENCE-OPTIMIZED.md
      AGENT-OPERATIONS.md
```

---

## Next Steps

1. Use this map as reference for file consolidation
2. Preserve git history: move files, don't copy
3. Create symlinks for root-level reference files
4. Update all cross-file links to new locations
5. Commit: "chore: consolidate scattered docs into WORLDWIDEBRO-OS structure"

Result: One canonical location per file type. Searchable. Maintainable.
