# File Structure of All Duplicates

**Purpose:** Show what's in each duplicate before deciding to merge/delete

---

## CRITICAL DUPLICATES (Show Structure)

### 1. REPOSITORY REGISTRIES

```
File A: Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json
├── Size: 904KB (29,056 lines)
├── Format: JSON array of repo objects
├── Repos tracked: ~1,400+
├── Fields: name, PURPOSE, CATEGORY, TECH_STACK, stars, url, language, updated_at
├── Status: DEFINITIVE (primary source)
└── Last updated: ?

File B: civilization-os-local/REPO_REGISTRY.json
├── Size: 8KB (275 lines)
├── Format: JSON
├── Repos tracked: ~8 entries
├── Purpose: Local reference/subset
├── Status: BACKUP/OUTDATED
└── Connected to: civilization-os-local/ folder

File C: WORLDWIDEBRO-OS/REGISTRIES/repository_registry_pilot.json
├── Size: 104KB (3,201 lines)
├── Format: JSON
├── Repos tracked: ~50-100 (pilot set)
├── Purpose: Test/pilot version
├── Status: INTERMEDIATE (not production)
└── Connected to: repo_classification_pilot.py script
```

**Decision Tree:**
- Keep: `REPOSITORY-REGISTRY.json` (definitive)
- Delete or Archive: `civilization-os-local/REPO_REGISTRY.json` (subset) — but check if anything references it
- Delete or Archive: `repository_registry_pilot.json` (pilot) — but check if scripts depend on it

**⚠️ BEFORE DELETE:** Check what these reference:
```bash
grep -r "REPO_REGISTRY.json" /Users/acebless/Documents/ --include="*.py" --include="*.md"
grep -r "repository_registry_pilot" /Users/acebless/Documents/ --include="*.py" --include="*.md"
```

---

### 2. VENTURE MAPPINGS

```
File A: VENTURE-HANDLE-MAP.json
├── Size: 4KB (108 lines)
├── Format: JSON with system config
├── Contains: venture_id → handle/email mapping
├── Ventures: 712 defined, 10 documented
├── Purpose: Handle switching context
├── Status: ACTIVE/MAINTAINED
└── Last updated: 2026-06-11

File B: .planning/venture-hub-alignment.json
├── Size: 1KB (23 lines)
├── Format: JSON (minimal)
├── Contains: ?
├── Purpose: Auto-sync from Supabase
├── Status: ACTIVE (auto-generated)
└── Synced by: obsidian_graph_sync.py

File C: The office/ventures.json
├── Size: 232KB (59,367 lines)
├── Format: JSON (large dataset)
├── Contains: Complete venture data
├── Purpose: ?
├── Status: UNKNOWN (needs inspection)
└── Connected to: "The office" folder system

File D: MC-OPERATIONS/config/ventures.json
├── Size: ? 
├── Format: JSON
├── Purpose: ?
├── Status: UNKNOWN (needs inspection)
└── Connected to: MC-OPERATIONS folder
```

**Decision Tree:**
- Keep: `VENTURE-HANDLE-MAP.json` (definitely used for `venture` CLI command)
- Keep: `.planning/venture-hub-alignment.json` (auto-synced, used by Obsidian)
- Inspect: `The office/ventures.json` — if contains unique data, need to merge
- Inspect: `MC-OPERATIONS/config/ventures.json` — if contains unique data, need to merge

**⚠️ BEFORE DELETE:** Check what references these:
```bash
grep -r "The office/ventures.json" /Users/acebless/Documents/ --include="*.py" --include="*.md" --include="*.sh"
grep -r "MC-OPERATIONS/config/ventures.json" /Users/acebless/Documents/ --include="*.py"
```

---

### 3. MASTER INDEXES

```
File A: 00-MASTER-INDEX.md
├── Size: 6KB (197 lines)
├── Format: Markdown with YAML frontmatter
├── Contains: References to [[memory files]] and ORBs
├── Purpose: Central knowledge index
├── Status: ACTIVE
└── Last updated: ?

File B: ORB-MASTER-CONNECTOR-2026-06-11.md
├── Size: ?
├── Format: Markdown
├── Contains: ORB connections/references
├── Purpose: ORB mapping
├── Status: UNKNOWN
└── Last updated: 2026-06-11

File C: civilization-os-local/MASTER-FOLDER-MAP.md
├── Size: ?
├── Format: Markdown
├── Contains: Folder structure mapping
├── Purpose: File system navigation
├── Status: UNKNOWN
└── Connected to: civilization-os-local/ folder
```

**⚠️ BEFORE DELETE:** Check if any docs link to them:
```bash
grep -r "ORB-MASTER-CONNECTOR" /Users/acebless/Documents/ --include="*.md"
grep -r "MASTER-FOLDER-MAP" /Users/acebless/Documents/ --include="*.md"
```

---

### 4. ROADMAP DUPLICATES (20 CON files)

```
Example Structure:
File: CON-009-ROOFING-COMPANY-BANKABILITY-ROADMAP.md

Sections (check if all 20 are identical):
├── Header with venture info
├── 12-Month Timeline
├── Capital Needs
├── Revenue Projections
├── Risk Assessment
├── Operational Requirements
├── Execution Checklist
└── Success Metrics

Question: Are all 20 CON files IDENTICAL structure with only data changing?

If yes → Replace with:
├── CON-TEMPLATE.md (structure only)
└── CON-VENTURES-DATA.csv (venture-specific data)

If no → Need to identify which have UNIQUE sections
```

**⚠️ VERIFICATION:**
```bash
# Check if all CON files are identical
md5sum /Users/acebless/Documents/CON-*.md | sort | uniq -c
# If count > 1, files differ
```

---

### 5. CHECKLIST DUPLICATES

```
File A: books/FRIDAY-LAUNCH-CHECKLIST.md
File B: edu-013-automated-empire-book/playbooks/FRIDAY-LAUNCH-CHECKLIST.md

Question: Are these IDENTICAL?

If yes → Keep ONE, delete other
If no → Merge unique items from both

Check with:
diff /Users/acebless/Documents/books/FRIDAY-LAUNCH-CHECKLIST.md \
     /Users/acebless/Documents/edu-013-automated-empire-book/playbooks/FRIDAY-LAUNCH-CHECKLIST.md
```

---

### 6. STRATEGY DUPLICATES

```
File A: CONSOLIDATION-STRATEGY.md
├── Size: ?
├── Sections: ?
├── Purpose: Overall strategy
└── Status: ACTIVE

File B: WORLDWIDEBRO-UNIFIED-OS/CAPITAL-TARGETING-STRATEGY.md
├── Size: ?
├── Sections: ?
├── Purpose: Capital targeting
└── Status: UNKNOWN (subset or duplicate?)

Question: Is CAPITAL-TARGETING a SECTION of CONSOLIDATION, or UNIQUE strategy?

If SUBSET → Merge into CONSOLIDATION-STRATEGY.md as ## Capital Targeting
If UNIQUE → Keep separate or merge carefully
```

---

## INSPECTION CHECKLIST

Before deleting ANY duplicate, answer:

- [ ] **Is it referenced?** `grep -r "filename" /Users/acebless/ --include="*.py" --include="*.md"`
- [ ] **Does a script read it?** Check for file paths in Python/shell scripts
- [ ] **Is it auto-synced?** (Like venture-hub-alignment.json from Supabase)
- [ ] **Is unique data in it?** Compare content not just filenames
- [ ] **Are there dependencies?** (One file feeds another)

---

## NEXT STEPS

1. Run the verification commands above
2. Fill in this template with findings
3. Create a MERGE PLAN showing what data goes where
4. THEN delete with confidence

---

