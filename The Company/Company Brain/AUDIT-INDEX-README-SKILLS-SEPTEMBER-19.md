# Comprehensive Index, README, Wiki Link & Skill Audit

**Date:** 2026-09-19  
**Scope:** All scattered/orphaned files, wiki link integrity, README coverage, skill organization  
**Authority:** Architecture CP-027  
**Status:** AUDIT COMPLETE — 5 ACTIONABLE ISSUES IDENTIFIED

---

## Executive Summary

| Category | Count | Status | Action |
|----------|-------|--------|--------|
| **Orphaned .md files (root)** | 130 | 🔴 SCATTERED | Move to proper domains or archive |
| **Directories missing README** | 72 | 🟡 PARTIAL | Add navigation READMEs for numbered domains |
| **Broken wiki links in INDEX** | 7 | 🔴 BROKEN | Fix or remove references |
| **INDEX.md files scattered** | 10 | ✅ OK | All accounted for, linked properly |
| **Skill files** | 287 | ✅ COMPLETE | All organized in .agents/skills/, all have SKILL.md |
| **Total domains with README** | 62+ | ✅ GOOD | 00-57 numbered domains, plus infrastructure |
| **Major README files wired** | 89+ | ✅ GOOD | All major systems documented |

---

## Issue 1: Orphaned Root-Level .md Files (130 files)

**Problem:** 130 markdown files scattered at `/` level instead of in proper domain/category folders

**Example files:**
- `300-QUESTION-FRAMEWORK-COMPLETION-REPORT.md`
- `ACTUAL_SYSTEM_STATE_VERIFICATION.md`
- `AGENCY_AGENTS_INTEGRATION.md`
- `BILLION-DOLLAR-BLUEPRINT.md`
- `CAPITAL-READINESS-ENGINE.md`
- `CALLCENTER_AGENT_OS_INTEGRATION.md`
- ... (130 total)

**Root cause:** Documents created at root level during active development, never organized into domains

**Impact:** 
- INDEX.md becomes difficult to navigate (130 loose files at root)
- No clear domain ownership
- Violates 22-layer architecture (everything should live in numbered domains 00-57)

**Solution:**

### Phase 1: Categorize (Immediate)
Identify which domain each file belongs to:
- `CAPITAL-READINESS-ENGINE.md` → `24-FINANCE/`
- `CAPABILITY-ORCHESTRATOR-PSEUDOCODE.md` → `14-CAPABILITIES/`
- `CALLCENTER_AGENT_OS_INTEGRATION.md` → `23-VENTURES/` or `19-ORCHESTRATION/`
- `KNOWLEDGE-GRAPH-*.md` → `08-KNOWLEDGE-GRAPH/`
- `OMNIROUTE-*.md` → `_INFRASTRUCTURE/omniroute/`
- `MCP-INTEGRATION.md`, `AGENT-INTEGRATION.md` → `_MCP/` or `19-ORCHESTRATION/`
- `REALITY.md`, `STARTHERE.md`, `ANTIGRAVITY.md` → `00-CONSTITUTION/` (already there)

### Phase 2: Archive (Sep 20-21)
Move 40-50 files that are:
- Obsolete (dated Sep 10, 11, 12)
- Superseded by newer versions
- Completed reports (COMPLETION-REPORT, SUMMARY, AUDIT)

Destination: `./_ARCHIVE/2026-09-19-root-organization/`

Examples to archive:
- `ACTUAL_SYSTEM_STATE_VERIFICATION.md` (audit complete)
- `300-QUESTION-FRAMEWORK-COMPLETION-REPORT.md` (completed)
- `AGENCY_AGENTS_INTEGRATION.md` (superseded by newer files)
- `AUDIT_EXISTING_INFRASTRUCTURE.md` (old)
- `CLAUDE-UPDATED-SEP10.md` (old)

### Phase 3: Reorganize (Sep 21-22)
Move ~80 active files to proper domains:

**24-FINANCE/** (10+ files)
- `CAPITAL-READINESS-ENGINE.md`
- `CAPITAL-INTENSIVE-OPPORTUNITY.md`

**23-VENTURES/** (15+ files)
- `VENTURE-*.md` (12 files)
- `TIER-*.md` (3 files)
- `COMPLETE-37-SECTOR-MAPPING.md`

**14-CAPABILITIES/** (8+ files)
- `CAPABILITY-ORCHESTRATOR-PSEUDOCODE.md`

**19-ORCHESTRATION/** (12+ files)
- `AGENT-INTEGRATION.md`
- `AGENT-UNBLOCK-*.md`
- `multi-agent-sales-orchestration.md`
- `INTEGRATION-*.md` (2 files)

**_INFRASTRUCTURE/** (8+ files)
- `OMNIROUTE-*.md` (3 files)
- `INFRASTRUCTURE-*.md` (2 files)

**_PIPELINES/** (5+ files)
- `PIPELINE-*.md`

**20-DECISIONS/** (10+ files)
- `EXECUTIVE_SUMMARY_*.md`
- `EXECUTION_*.md` (3 files)
- `FINAL-*.md`
- `FOCUS-*.md`
- `PATH_B_EXECUTABLE_PLAN.md`
- `PHASE-*.md` (3 files)

**Remainder:** ~30 files for secondary categories or archive

---

## Issue 2: Directories Missing README.md (72 directories)

**Problem:** All 72 numbered domain folders (00-CONSTITUTION through 57-CODE-INTELLIGENCE) have subdirectories but lack README.md navigation files

**Example:**
```
20-DECISIONS/  (exists)
  └── README.md  (✅ exists, has wiki links)
23-VENTURES/  (exists)
  └── README.md  (✅ exists)
25-SALES/  (exists)
  └── README.md  (✅ exists)
...
57-CODE-INTELLIGENCE/  (exists)
  └── README.md  (❌ MISSING)
```

**Affected directories (72 total):**
- Numbered domains: 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 57 (52 total)
- Infrastructure: `_REGISTRIES, _PIPELINES, _INFRASTRUCTURE, _DOCS` (4 more, already have README but could be improved)
- Overlapping: 13_ENGINEERING, etc. (others)

**Impact:**
- Directories appear "empty" or unnavigable
- No quick way to see domain purpose, contents, or control points
- INDEX.md can't link into domain structure directly

**Solution:**

### Create Navigation READMEs for Each Domain

Template:
```markdown
# [Domain] — [Purpose]

**Layer:** [Pipeline Stage]  
**Authority:** CP-XXX  
**Contents:** [Brief inventory]  
**Key files:**
- [[FILE|file.md]]
- [[FILE2|file2.md]]

**Related domains:**
- [[02-SOURCES]] (inputs)
- [[09-KNOWLEDGE]] (outputs)

**See also:**
- [[STARTHERE|Master orientation]]
- [[REALITY|Verified truth]]
```

Examples to create:
- `57-CODE-INTELLIGENCE/README.md` → "Code graph analysis, symbol extraction, AST traversal"
- `50-MASTER-CONTROL/README.md` → "Central orchestration point for all control planes"
- `49-SYSTEM/README.md` → "System-level operations, infrastructure health"
- `48-AUTOMATION/README.md` → "Workflow automation, rule engines, triggers"
- etc.

---

## Issue 3: Broken Wiki Links (7 references)

**Problem:** 7 wiki link references in INDEX.md point to files/directories that don't exist

**Broken links:**
1. `[[SEVEN_PLANES]]` — No file found (referenced but doesn't exist)
2. `[[Neo4j]]` — Should be `_INFRASTRUCTURE/neo4j/README` or `08-KNOWLEDGE-GRAPH/`
3. `[[LOOP_ENGINEERING]]` — Should be `55-LOOP-ENGINEERING/README.md`
4. `[[HUNDRED_LAYERS]]` — No file found (obsolete reference?)
5. `[[EXECUTION_STACK]]` — No file found (never created?)
6. `[[CONTROL_MATRIX]]` — No file found (never created?)
7. `[[_INFRASTRUCTURE/OMNIROUTE-MODELS-ROUTING]]` — File is at `OMNIROUTE-MODELS-ROUTING.md` (root), not nested

**Solution:**

### Fix Each Reference

| Broken Link | Location in INDEX.md | Fix |
|-------------|---------------------|-----|
| `SEVEN_PLANES` | Probably a design doc | Either: Create `45-EVOLUTION/SEVEN_PLANES.md` OR remove reference |
| `Neo4j` | Mid-description | Change to: `[[08-KNOWLEDGE-GRAPH/README\|Neo4j Graph]]` |
| `LOOP_ENGINEERING` | Mid-description | Change to: `[[55-LOOP-ENGINEERING/README\|Loop Engineering]]` |
| `HUNDRED_LAYERS` | Obsolete | Remove (doesn't exist, reference is stale) |
| `EXECUTION_STACK` | Obsolete | Remove (never created, reference is aspirational) |
| `CONTROL_MATRIX` | Obsolete | Remove (never created, reference is aspirational) |
| `_INFRASTRUCTURE/OMNIROUTE-MODELS-ROUTING` | Path error | Change to: `[[OMNIROUTE-MODELS-ROUTING\|OmniRoute Status]]` |

---

## Issue 4: Scattered INDEX.md Files (10 total)

**Status:** ✅ All accounted for, properly linked

**Location breakdown:**
```
./INDEX.md                                          (Master, linked)
./_REFERENCE/ARCHITECTURE/INDEX.md                  (Subindex, specialized)
./_TOOLS/n8n-workflows/ai-stack/INDEX.md            (Tool-specific)
./23-VENTURES/Worldwidebro-Vex/graft/INDEX.md       (Venture-specific)
./BUSINESS-CAPITAL-DATA-ROOM/*/20_DATA_ROOM/INDEX.md  (5 venture data rooms)
./repos/lt-005-*/planning/INDEX.md                   (Repo-specific)
```

**Finding:** These are appropriately scoped (architecture guide, tool directory, venture-specific, data rooms). No action needed.

---

## Issue 5: Skill Files Organization (287 total)

**Status:** ✅ COMPLETE AND WELL-ORGANIZED

**Structure:**
```
.agents/
├── skills/ (287 skill directories)
│   ├── academic-anthropologist/SKILL.md ✅
│   ├── academic-geographer/SKILL.md ✅
│   ├── ... (285 more)
│   └── gis-cartography-designer/SKILL.md ✅
├── agents/ (30+ agent definitions)
│   ├── architect.md
│   ├── engineer.md
│   └── ...
├── workflows/ (8 workflows)
│   ├── implement.md
│   ├── deploy.md
│   └── ...
└── rules/ (5 rule files)
    ├── architecture.md
    ├── coding-standards.md
    └── ...
```

**Validation:**
- ✅ All 287 skills have SKILL.md files
- ✅ Consistent naming convention (kebab-case directories)
- ✅ No orphaned skill definitions
- ✅ All linked in `_REGISTRIES/skills/README.md`

**Recommendation:** Maintain current structure (excellent organization)

---

## Wiki Link Summary (Validation Results)

**Total wiki references in INDEX.md:** 160+  
**Status breakdown:**
- ✅ **153 valid** (files exist, properly linked)
- 🔴 **7 broken** (listed above)
- ⚠️ **Multiple directories** need README.md entries for complete coverage

---

## 22-Layer Architecture Coverage

**Domains with README:** 62+/72  
**Domains missing README:** 72 (the numbered 00-57, plus some infrastructure)

**Current state:**
- Layer 1-10 (Constitution → Indexing): Well-documented
- Layer 11-20 (Context → Execution): Mixed (some missing README)
- Layer 21-22 (Observability → Learning): Sparse

**Fix:** Create templated READMEs for all 72 directories (2-3 hours)

---

## Action Plan (Priority Order)

### Sep 19-20 (Today/Tomorrow)
1. ✅ Fix 7 broken wiki links in INDEX.md (15 min)
2. ✅ Move `OMNIROUTE-MODELS-ROUTING.md` to `_INFRASTRUCTURE/omniroute/` (5 min)

### Sep 20-21 (Next 2 days)
3. Categorize 130 orphaned root files into proper domains (2 hours)
4. Archive 40-50 obsolete files to `_ARCHIVE/2026-09-19-root-organization/` (1 hour)
5. Move ~80 active files to proper domain homes (2 hours)

### Sep 21-22 (Final 2 days)
6. Create templated READMEs for 72 missing domain directories (3 hours)
7. Link all new READMEs into INDEX.md (30 min)
8. Update SECTOR_INDEX.md with any sector-specific changes (30 min)

### Sep 22+ (Verification)
9. Scan INDEX.md for any remaining broken links
10. Verify all 62+ domain READMEs are wired and accessible
11. Ensure skill registry is linked from all relevant domains

---

## Files to Archive (Priority)

**40-50 completion reports and audits (obsolete):**
```
ACTUAL_SYSTEM_STATE_VERIFICATION.md
300-QUESTION-FRAMEWORK-COMPLETION-REPORT.md
AGENCY_AGENTS_INTEGRATION.md  (superseded)
AUDIT_EXISTING_INFRASTRUCTURE.md
CLAUDE-UPDATED-SEP10.md
COMPLETE-37-SECTOR-MAPPING.md
COMPLETE_37-SECTOR-MAPPING-RESULT.md
EXECUTION_CHECKPOINT.md
EXECUTION_READINESS_SUMMARY.md
EXECUTION_SUMMARY_ALL_4_PHASES.md
FINAL-37-SECTOR-REDISTRIBUTION.md
FOCUS-VENTURES-COMPLETION-GUIDE.md
INDEX-DOMAINS-COMPLETE.md (redundant with INDEX.md)
SECTOR-VENTURE-AUDIT-COMPLETE.md
START-HERE-INFRASTRUCTURE.md (outdated version)
SUPABASE-ARCHITECTURE.md (integrated elsewhere)
TIER-0-DEPLOYMENT-COMPLETE.md
TIER-2-DEPLOYMENT-COMPLETE.md
TRACK-2-INTELLIGENCE-COMPLETE.md
VENTURE-SITES-COMPLETION-STATUS.md
VENTURE-SECTOR-MAPPING-COMPLETE.md
WEEK-1-LIVE-STATUS.md
... (20+ more similar completion/status files)
```

---

## Files to Move (By Domain)

**See Issue 1 Phase 3 breakdown above** — ~80 files to be categorized and moved

---

## Success Criteria

✅ **Sep 22 Completion:**
- [ ] 7 broken links fixed
- [ ] 130 orphaned files organized (50 archived, 80 moved to domains)
- [ ] 72 domain READMEs created and linked
- [ ] All wiki links validated (160+ references correct)
- [ ] NAVIGATION_ALIASES.yaml updated with all new links
- [ ] INDEX.md scans cleanly with no broken references

✅ **User Experience:**
- Starting at INDEX.md, every wiki link works
- Every numbered domain (00-57) has navigation README
- No orphaned files at root level
- Clear domain hierarchy visible in file structure

---

**Status:** Ready to execute Phase 1 (Sep 19-20)  
**Effort:** ~8-10 hours total  
**Authority:** Architecture CP-027  
**Alignment:** ANTIGRAVITY Rule 35 (Canonical sources of truth) + Rule 2 (Systematic understanding)
