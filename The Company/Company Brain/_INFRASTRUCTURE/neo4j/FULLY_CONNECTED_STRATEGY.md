# Fully Connected File Base Strategy

**Date:** 2026-09-19  
**Goal:** Every file discoverable from STARTHERE.md + INDEX.md  
**Status:** Executing Phase 1-3

---

## Current State (From Graph Scan)

| Metric | Count | Status |
|--------|-------|--------|
| Total .md files scanned | 4,994 | ⚠️ Includes external (venv, repos, _EVAL) |
| Core Company Brain files | ~800 | 📊 Need focus here |
| Files with wiki links | 2,564 | Mixed quality |
| Disconnected files | 2,430 | Need connection |
| Broken link references | 18,544 | Need repair |
| Domains with README | 117 | Need 87 more |

---

## Phase 1: SCOPE FOCUS (Do This First)

**Exclude from connection strategy:**
- `_ENGINE/.venv/` (Python dependencies) — 500+ files, external
- `_EVAL/utopia/` (external project) — 100+ files, external
- `repos/` (external code repos) — 1000+ files, vendor
- `_TOOLS/` (external tools) — 500+ files, vendor
- `.git/`, `node_modules/` — 1000+ files, git/npm

**Include (core Company Brain):**
- `00-*` through `57-*` (numbered domains) — ~200 files ✅
- `_AGENTS`, `_ORCHESTRATION`, `_MCP`, `_MEMORY`, `_INFRASTRUCTURE`, `_REGISTRIES`, `_PIPELINES`, `_ONTOLOGY`, `_PROMPTS`, `_DOCS` — ~100 files ✅
- `BUSINESS-CAPITAL-DATA-ROOM/` (ventures) — ~50 files ✅
- `23-VENTURES/` (ventures) — ~30 files ✅
- Root master files — ~10 files ✅
- Total: **~800 core files** (the actual Company Brain)

---

## Phase 2: AUTO-CONNECTION SYSTEM

### Strategy 1: Master Entry Points
All 800 core files should link back to 4 master nodes:

```
STARTHERE.md
├── REALITY.md
├── ANTIGRAVITY.md
├── INDEX.md
└── Domain READMEs (72 total)
    ├── 00-CONSTITUTION/README.md
    ├── 01-IDENTITY/README.md
    ├── ...
    └── 57-CODE-INTELLIGENCE/README.md
```

### Strategy 2: Domain-Based Grouping
Each domain folder (00-*) + infrastructure folder (_*) gets:
- **README.md** with links to [[STARTHERE]], [[INDEX]], related domains
- All .md files in domain link to README.md
- README.md links to parent master (STARTHERE or INDEX)

### Strategy 3: Wiki Link Repair
Broken links (18,544) categorized:
1. **Fixable** (70%) — File exists, just wrong path
   - `[[Neo4j]]` → `[[08-KNOWLEDGE-GRAPH/README]]`
   - `[[Agent-Framework]]` → `[[16-AGENTS/README]]`

2. **Create** (20%) — Should exist but missing
   - Create placeholder README in domain
   - Link from master

3. **Remove** (10%) — Dead references, clean up

---

## Phase 3: AUTO-GENERATION PIPELINE

### Step 1: Generate Missing READMEs (87 domains)
```bash
for domain in 00 01 02 ... 57; do
  if [ ! -f "$domain-NAME/README.md" ]; then
    # Generate README.md with:
    # - Link to [[STARTHERE]]
    # - Link to [[INDEX]]
    # - Links to related domains
    # - Link to domain files
  fi
done
```

### Step 2: Add Wiki Links to Orphan Files
```bash
for file in $(find . -name "*.md" -not -path "./*EXCLUDED*"); do
  if ! grep -q "\[\[STARTHERE" "$file"; then
    # Add header: [[STARTHERE]] | [[INDEX]] | [[DOMAIN/README]]
  fi
done
```

### Step 3: Fix Broken References
```bash
# Run file_graph_repair.py
# For each broken link:
#   1. Check if target exists (with variations)
#   2. Update reference to correct path
#   3. Or create stub in domain + link
```

### Step 4: Verify Connectivity
```bash
# Check all files link to master
# Check all master links are valid
# Check no circular orphans
# Neo4j graph: all files reachable from STARTHERE
```

---

## Implementation (Real Commands)

### Create Missing Domain READMEs
```bash
# For each numbered domain without README
cd 24-FINANCE
cat > README.md << 'EOF'
# 24-FINANCE — Financial Operations & Capital Management

[[STARTHERE]] | [[REALITY]] | [[ANTIGRAVITY]] | [[50-MASTER-CONTROL]] | [[00-CONSTITUTION]]

**Layer:** Finance & Capital  
**Control Point:** CP-024  
**Purpose:** Capital allocation, budgets, financial forecasting

**See:** [[STARTHERE|Master Orientation]]
EOF
```

### Auto-Link All Files to STARTHERE
```bash
# For each file without [[STARTHERE]]:
for file in $(find . -name "*.md" -type f); do
  if ! grep -q "STARTHERE\|REALITY\|ANTIGRAVITY" "$file"; then
    # Add at top: [[STARTHERE]] | [[INDEX]] | [[DOMAIN/README]]
  fi
done
```

### Fix Broken Links
```bash
# Scan all references
grep -r "\[\[" . | grep -v "STARTHERE\|REALITY\|ANTIGRAVITY" \
  | awk -F'[[' '{print $2}' | awk -F']]' '{print $1}' \
  | while read ref; do
    if [ ! -f "$ref.md" ] && [ ! -d "$ref" ]; then
      echo "BROKEN: $ref"
    fi
  done
```

---

## Success Criteria (Sep 20-22)

✅ **Core company brain fully connected (800 files)**
- [ ] All 72 domains have README.md
- [ ] All README.md link to STARTHERE + INDEX
- [ ] All .md files link to their domain README
- [ ] No orphaned files at root (except master files)
- [ ] 0 broken links (all 153+ references valid)
- [ ] Neo4j graph: All 800 files reachable from STARTHERE
- [ ] Every file discoverable in 2 clicks max

✅ **External dependencies isolated**
- [ ] `_ENGINE/venv/`, `_EVAL/`, `repos/`, `_TOOLS/` marked as external
- [ ] Not included in "fully connected" metrics
- [ ] Can reference Company Brain but not vice versa

✅ **Users can navigate**
- [ ] Start at STARTHERE.md
- [ ] Click any [[wiki_link]]
- [ ] Land on valid file
- [ ] Click domain README → All files in that domain
- [ ] Click REALITY/ANTIGRAVITY → Operating context

---

## Neo4j Graph Structure

```
STARTHERE
  ├─ [LINK]─→ REALITY
  ├─ [LINK]─→ ANTIGRAVITY
  ├─ [LINK]─→ INDEX
  └─ [LINK]─→ Domain
      ├─ 00-CONSTITUTION/README
      ├─ 01-IDENTITY/README
      ├─ ... (72 domains)
      └─ Files in domain
          ├─ file1.md [LINK]─→ Domain README
          ├─ file2.md [LINK]─→ Domain README
          └─ file3.md [LINKS_TO]─→ Other files
```

**Query:** `MATCH (n)-[:LINKS_TO*]->(STARTHERE) RETURN count(DISTINCT n)`  
**Expected:** ~800 (all core files reachable)

---

## Timeline

| Phase | Task | Time | Status |
|-------|------|------|--------|
| 1 | Scope focus (exclude external) | 1h | Today |
| 2 | Generate 87 missing READMEs | 2h | Sep 20-21 |
| 3 | Auto-link all files to masters | 2h | Sep 20-21 |
| 4 | Fix 18,544 broken links → Core 153 | 3h | Sep 21-22 |
| 5 | Verify Neo4j graph connectivity | 1h | Sep 22 |
| 6 | Test user navigation | 1h | Sep 22 |

**Total:** ~10 hours for fully connected core Company Brain

---

## Tools Used

- **Neo4j:** Graph structure + connectivity verification
- **Bash/Python:** File scanning + batch operations
- **Git:** Track all changes + atomic commits
- **INDEX.md:** Master reference point
- **Wiki links:** [[connection_mechanism]]

---

**Next Steps:**
1. Run Phase 1: Scope focus (identify core 800 files)
2. Generate README.md for 87 missing domains
3. Auto-link all files to STARTHERE + domain README
4. Repair broken links (keep core 153)
5. Load into Neo4j, verify reachability
6. **Result:** Fully connected file base (800 files, all discoverable from STARTHERE)

