# Task Plan — WORLDWIDEBRO-OS Canonical Consolidation

## Goal
Collapse ~22 competing "OS/holdings/studio" roots + ~384 loose root files into ONE canonical
`WORLDWIDEBRO-OS/` tree (00-COMMAND → 10-STATUS). Move folders to their correct layer,
consolidate duplicates, retire the husks, build the registry layer as source of truth.

## Locked Decisions
- Migration stance: **Consolidate salvageable content → retire/delete old roots**
- Registry-driven; update relevant files as we move
- Target = user's v1 spec: 00-COMMAND, 00-DIRECTIVES, 01-EXECUTIVES, 02-GOVERNANCE,
  03-PORTFOLIO, 04-OPERATIONS, 05-AGENTS, 06-TECHNOLOGY, 07-KNOWLEDGE, 08-DATA,
  09-DASHBOARDS, 10-STATUS

## Safety Rules
1. NO `rm` of any OS root until its unique content is confirmed migrated (husks retired last).
2. Build artifacts (node_modules, graphify-out 701M, *-venv, moneyprinter-output) are
   gitignored + left in place, NOT migrated.
3. LIVE software/infra (supabase, grafana, nginx, LightRAG, docker-compose, active venture
   code repos) is REGISTERED in 08-DATA registries, NOT physically moved — moving breaks
   hardcoded paths in CLAUDE.md + docker-compose. Only docs/markdown consolidate physically.
4. Git tag `backup-pre-os-migration` = restore point.

## Phases
| # | Phase | Status |
|---|-------|--------|
| 0 | Git safety net (.gitignore, backup tag) | DONE (tag @ de982cf) |
| 1 | Build canonical skeleton (164 dirs) + README anchor | DONE (anchors: README; directives/council pending) |
| 2 | Full migration map in findings.md | DONE |
| 3 | Move loose md (242->7) + fold 22 doc-roots | DONE |
| 4 | Relocate 49 venture/tech/agent repos + 23 infra/ops folders | DONE (root 108->16) |
| 5 | Backbone relocated + 49 files ref-rewritten | DONE (commit de615a3) |
| 6 | Git commits (fe8d949, de615a3) + backup tag | DONE |
| 7 | BLOCKED: pause background automations recreating old root paths | NEEDS USER |

## BLOCKER (2026-06-19 ~20:20)
Active automations recreate moved folders at OLD root paths faster than moves land:
- crontab `*/15 git_auto_sync.sh` (Civilization OS) — auto-commits+pulls, RESTORES moved
  tracked files to root. Proven: commits 68fca77, b492adc appeared mid-session (not mine).
- crontab `*/5 monitor-xyops.sh`, `0 6 obsidian-daily-sync.py` (points at OLD
  WORLDWIDEBRO-OS/07_AUTOMATIONS underscore path)
- launchd: com.izaos.daily-triage / weekly-connections / weekly-rag-ingest
ACTION NEEDED: user pauses these (`crontab -e` comment out; `launchctl unload ~/Library/
LaunchAgents/com.izaos.*`), THEN final root cleanup sticks. Do NOT disable without user OK.

## Backbone blast radius (measured)
- venture-hub: 9 CLAUDE.md refs + 12 root .py scripts (run-from-root, relative paths)
- Influence-VBO: 5 CLAUDE.md refs + 7 root .py scripts
- Obsidian: app vault (absolute path in app config); scripts: run-from-root
- Both folders = part of main repo (git mv works). Recommendation: REGISTER in 08-DATA,
  leave in place (moving rewrites 28+ live refs for marginal tidiness).
- CLAUDE.md refs fixed so far: ORB-MASTER-CONNECTOR, Azriel, The office(ORB2), grafana.

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| zsh `for p in $PROTECTED` does NOT word-split → protection check no-op'd; ORB-MASTER-CONNECTOR moved to frameworks despite protect-list | Batch A | No data lost (file in 07-KNOWLEDGE/frameworks); fixed CLAUDE.md ref line 673. FUTURE: use explicit array `PROTECTED=(a b c)` + `for p in "${PROTECTED[@]}"` |

## Referenced root items (MOVE requires path-fix in CLAUDE.md/MEMORY.md)
Influence-Venture-Business-OS(4), venture-hub(bare-form), scan_repositories.py(2),
populate_venture_knowledge_graph.py, obsidian_graph_sync.py, grafana, docker-compose.yml,
worldwidebro_os.duckdb, operating_system_schema.sql, repo_classification_phase1.py,
.venture-shell-config, KNOWLEDGE-GRAPH-DASHBOARD.md, WORLDWIDEBRO-UNIFIED-COMPANY-ROADMAP-2026.md,
ELECTRICAL-SECTOR-DEPLOYMENT-2026-06-11.md, SUPABASE-SQL-REFERENCE-OPTIMIZED.md,
"The office"(=ORB2 in CLAUDE.md, `.claude/get-shit-done/`), Azriel-Fathering-Content
DONE: ORB-MASTER-CONNECTOR-2026-06-11.md → 07-KNOWLEDGE/frameworks (ref fixed)

## Progress log
- Batch A: 65 loose .md + 15 session logs moved (root .md 242→162). CON→CONSTRUCTION/docs(21),
  FIN/TRADING→FINANCIAL/docs(10), ORB/PHASE/SCALE/SYSTEM/etc→07-KNOWLEDGE/frameworks(34).
