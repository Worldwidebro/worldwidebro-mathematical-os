# File Reorganization Audit — 2026-07-27

**Goal:** Categorize all Documents files into 01_AI_BRAIN vs 02_PROJECTS folders for unified structure.

---

## CATEGORY A: AI Brain Files (01_AI_BRAIN)

### 01-PROMPTS (System Directives)
| Current File | Target | Purpose |
|--------------|--------|---------|
| .planning/COMPANY-BRAIN-OS-LAYER-MAPPING.md | worldwidebro-boss-prompt.md | System prompt |
| .planning/AGENT-OPERATIONS.md | agent-operations-guide.md | Agent role definitions |
| .planning/AGENTS.md | agent-registry-reference.md | Agent taxonomy |
| .planning/COMMANDS.md | command-taxonomy.md | Command reference |

### 02-REASONING_FRAMEWORKS (Decision Logic)
| Current File | Target | Purpose |
|--------------|--------|---------|
| VENTURE-READINESS-SCORECARD.csv | venture-readiness-framework.csv | Scoring rubric |
| .planning/BACKWARDS-ROADMAP-712-VENTURES.md | venture-sequencing-logic.md | Sequencing rules |
| .planning/COMPLETION-DISTANCE-MAP.md | venture-completion-matrix.md | Progress tracking |
| .planning/CON-001-AUTOMATION-COST-BREAKDOWN.md | capital-allocation-example.md | Cost model example |
| .planning/FRAMEWORK-ANALYSIS.md | framework-analysis.md | Framework audit |

### 03-KNOWLEDGE_GRAPH (Structured Facts)
| Current File | Target | Purpose |
|--------------|--------|---------|
| REPOSITORY-REGISTRY.json | repository-registry.json | Repo catalog |
| .planning/KNOWLEDGE-GRAPH-DASHBOARD.md | knowledge-graph-schema.md | Graph documentation |
| (empty) | entity-taxonomy.json | Entities + relationships |
| (empty) | sector-definitions.json | Sector taxonomy |

### 04-EXECUTION_LOOPS (Workflows)
| Current File | Target | Purpose |
|--------------|--------|---------|
| .planning/30-DAY-SPRINT-TO-OPERATIONAL.md | 30-day-sprint-loop.md | Operational loop |
| .planning/4-WEEK-RESEARCH-PLAN.md | research-sprint-loop.md | Research workflow |
| .planning/CON-001-LOOPS.md | con-sector-loop-example.md | Sector-specific loop |
| .planning/NEXUSDISPATCH-PHASE1-SPRINTS.md | nexus-deployment-loop.md | Deployment workflow |

### 05-MEMORY_CHECKPOINTS (Session Records)
| Current File | Target | Purpose |
|--------------|--------|---------|
| .planning/2026-07-19_SESSION-CLOSURE-CHECKLIST.md | session-2026-07-19.md | Session record |
| .planning/2026-07-19_SYSTEM-ARCHITECTURE-SYNTHESIS.md | session-2026-07-19-architecture.md | Session analysis |
| .planning/CHAT-2026-07-21-DATA-PIPELINE-SUMMARY.md | session-2026-07-21.md | Session record |
| (future sessions) | session-{YYYY-MM-DD}.md | Automated by session-wrap skill |

### 06-AUDIT_TRAILS (Transparency Logs)
| Current File | Target | Purpose |
|--------------|--------|---------|
| .planning/BLOCKERS-AND-TASKS-2026-07-23.md | blockers-log.md | Blocker tracking |
| .planning/INGEST-CONFLICTS.md | conflict-resolution-log.md | Conflict log |

---

## CATEGORY B: Projects Files (02_PROJECTS)

### Sector Organization (CON, FIN, LT, RE, TECH, COMM)
```
02_PROJECTS/
├── CON/
│   ├── sector-os.md (construction operating system)
│   ├── ventures/
│   │   ├── CON-001/
│   │   │   ├── venture.json
│   │   │   ├── STATUS.md
│   │   │   ├── ROADMAP.md
│   │   │   └── docs/
│   │   └── CON-002/
│   └── status.csv (all CON ventures)
├── FIN/
├── LT/
├── RE/
├── TECH/
├── COMM/
├── _shared/ (design tokens, API clients, utilities)
├── _templates/ (venture bootstrap templates)
└── _deployments/ (Vercel, Railway, Supabase configs)
```

**Files to map to ventures:**
- .planning/CON-001-*.md → 02_PROJECTS/CON/CON-001/docs/
- venture.json files → 02_PROJECTS/{SECTOR}/{venture}/venture.json
- VENTURE-READINESS-SCORECARD.csv → 02_PROJECTS/{SECTOR}/status.csv (split per sector)

---

## CATEGORY C: Keep Hidden (System Configuration)

| Folder | Reason |
|--------|--------|
| .claude/ | User preferences + skills + settings |
| .git/ | Version control metadata |
| .obsidian/ | Obsidian vault config |
| .gitnexus/ | GitNexus index + cache |
| .mcp.json | MCP server configuration |
| .grok/, .qwen/ | Local LLM configs |

---

## CATEGORY D: Keep at Root

| File | Reason |
|------|--------|
| 00_COMMAND_CENTER/MASTER-HANDBOOK.md | Central index |
| docker-compose.yml | Infrastructure reference |
| CLAUDE.md | Project-level instructions |
| .claude/CLAUDE.md | Workspace-level instructions |

---

## CATEGORY E: Deprecate or Archive

| File | Status | Action |
|------|--------|--------|
| .planning/ENVIRONMENT-VARIABLES-REFERENCE.md | Stale | Archive + recreate in 05_OPERATIONS (future folder) |
| .planning/DOCKER-COMPOSE-UPDATES.md | Stale | Archive to deployment history |
| .planning/D1-N8N-DEPLOYMENT.md | Obsolete | Archive (n8n replaced by Zapier per memory) |
| .planning/D2-SECRETS-VAULT.md | Stale | Archive to 05_OPERATIONS/SECRETS-MANAGEMENT |
| .planning/LOOP.md | Stale | Migrate to 01_AI_BRAIN/04-EXECUTION_LOOPS/loop-examples.md |
| .planning/MAPS.md | Stale | Archive to 06_KNOWLEDGE/REFERENCE |
| .planning/LIVE-SITES-INDEX.md | Current | Migrate to 02_PROJECTS/_LIVE-DEPLOYMENTS.md |

---

## Migration Plan

### PHASE 1: Folder Creation (DONE)
- ✅ 01_AI_BRAIN/ structure + README.md
- ✅ 02_PROJECTS/ structure + README.md
- ✅ Three skills: brain, process-brain, session-wrap

### PHASE 2: File Migration (THIS WEEK)

**Batch A — High Priority (Prompts + Frameworks)**
1. Move COMPANY-BRAIN-OS-LAYER-MAPPING.md → 01_AI_BRAIN/01-PROMPTS/worldwidebro-boss-prompt.md
2. Move VENTURE-READINESS-SCORECARD.csv → 01_AI_BRAIN/02-REASONING_FRAMEWORKS/venture-readiness-framework.csv
3. Move BACKWARDS-ROADMAP-712-VENTURES.md → 01_AI_BRAIN/02-REASONING_FRAMEWORKS/venture-sequencing-logic.md
4. Move REPOSITORY-REGISTRY.json → 01_AI_BRAIN/03-KNOWLEDGE_GRAPH/repository-registry.json
5. Commit: `git commit -m "refactor: move AI Brain core files (prompts + frameworks)"`

**Batch B — Medium Priority (Execution Loops + Sessions)**
1. Move .planning/30-DAY-SPRINT-TO-OPERATIONAL.md → 01_AI_BRAIN/04-EXECUTION_LOOPS/
2. Move .planning/CON-001-LOOPS.md → 01_AI_BRAIN/04-EXECUTION_LOOPS/
3. Archive session records → 01_AI_BRAIN/05-MEMORY_CHECKPOINTS/session-{date}.md
4. Commit: `git commit -m "refactor: move execution loops + session records"`

**Batch C — Medium Priority (Audit Trails)**
1. Move .planning/BLOCKERS-AND-TASKS-2026-07-23.md → 01_AI_BRAIN/06-AUDIT_TRAILS/blockers-log.md
2. Move .planning/INGEST-CONFLICTS.md → 01_AI_BRAIN/06-AUDIT_TRAILS/conflict-resolution-log.md
3. Commit: `git commit -m "refactor: move audit trails to 01_AI_BRAIN"`

**Batch D — Venture Migration (LATER)**
1. Create 02_PROJECTS/{CON,FIN,LT,RE,TECH,COMM}/ventures/{venture}/docs/
2. Move .planning/CON-001-*.md → 02_PROJECTS/CON/CON-001/docs/
3. Create venture.json for each venture with metadata
4. Split VENTURE-READINESS-SCORECARD.csv into per-sector status.csv files

### PHASE 3: Validation & Cleanup (AFTER MIGRATION)
1. Run GitNexus impact analysis (verify no broken imports)
2. Run SocratiCode symbol search (find orphaned references)
3. Run `/brain` skill audit (verify categorization correctness)
4. Archive old .planning/ folder to .archive/planning-{date}/ if no remaining files
5. Update git history comment with categorization rationale

---

## Tool Usage for Audit

| Tool | Command | Purpose |
|------|---------|---------|
| **GitNexus** | `gitnexus impact --file {file} --direction downstream` | Verify file moves won't break references |
| **SocratiCode** | `socraticode search "\.planning/"` | Find lingering .planning/ references |
| **Graphify** | `graphify --before FILE-REORGANIZATION-AUDIT.md --after actual-result` | Visualize structure transformation |
| **Sourcegraph** | Search for "\.planning/" across all files | Catch regex patterns that reference old paths |

---

## Rollback Plan

If migration causes issues, git makes rollback simple:
```bash
# See what moved
git log --oneline | head -20

# Revert a specific batch
git revert {commit-hash}

# Or reset to before migration
git reset --hard {pre-migration-commit}
```

---

## Summary

**Total files to migrate: ~40**
- AI Brain: ~28 files (prompts, frameworks, loops, sessions, audits)
- Projects: ~8 files (venture-specific docs)
- Archive/Delete: ~4 files (stale/obsolete)

**Effort:** 2-3 hours (mostly moving + validation)
**Risk:** Low (all git-reversible)
**Benefit:** Single source of truth structure, scalable, aligns with T7 Shield

---

**Ready for user approval to proceed with Phase 2 (Migration)**
