---
name: Documents Folder Reorganization Checklist
created: 2026-06-19
status: ready_for_execution
scope: Holdings + OPCOs + Ventures + Infrastructure
phases: 7 (Holdings → OPCOs → Ventures → Infrastructure → Archive → Verify → Commit)
timeline: 2 hours (1-2 days after landing job)
---

# 🏗️ WORLDWIDEBRO HOLDINGS FOLDER REORGANIZATION CHECKLIST

**Current State:** 50+ venture folders scattered, 5 holdings versions, 3 knowledge graphs  
**Target State:** Single Holdings folder → OPCOs → Ventures → Infrastructure  
**Timeline:** 2 hours of work (NOT blocking your job search)  
**Status:** Ready to execute when you land Lane A job

---

## PHASE 1: CONSOLIDATE HOLDINGS (Decide on Primary)

### ✅ Step 1.1: Audit Holdings Folders

Current holdings folders:
```
RE-001-Worldwidebro-Holdings/     ← Newest (6/1-6/17)
Worldwidebro-Holdings/             ← Older
WORLDWIDEBRO-OS/                   ← Archive candidate
Worldwidebro-Operating-System/     ← Duplicate candidate
WORLDWIDEBRO-UNIFIED-OS/           ← Experiment candidate
```

**Decision Required:** Which ONE becomes primary?

**Recommendation:** `RE-001-Worldwidebro-Holdings/` (most recent, legal entity format)

- [ ] Decide: Primary holdings folder

### ✅ Step 1.2: Backup Other Holdings Folders

```bash
# Create archive destination
mkdir -p 04-ARCHIVED/holdings-deprecated

# Archive the others (do NOT delete yet)
mv Worldwidebro-Holdings/ 04-ARCHIVED/holdings-deprecated/
mv WORLDWIDEBRO-OS/ 04-ARCHIVED/holdings-deprecated/
mv Worldwidebro-Operating-System/ 04-ARCHIVED/holdings-deprecated/
mv WORLDWIDEBRO-UNIFIED-OS/ 04-ARCHIVED/holdings-deprecated/
```

**Result:** Only `RE-001-Worldwidebro-Holdings/` remains as primary

- [ ] Archive deprecated holdings folders

### ✅ Step 1.3: Verify Primary Folder

```bash
ls -la RE-001-Worldwidebro-Holdings/
```

Should show your holdings files/structure inside.

- [ ] Confirm primary holdings folder works

---

## PHASE 2: CREATE OPCO STRUCTURE

### ✅ Step 2.1: Create 18 OPCO Directories

```bash
cd RE-001-Worldwidebro-Holdings/
mkdir -p opcos/con-construction      # Construction
mkdir -p opcos/sta-staffing          # Staffing
mkdir -p opcos/con-content           # Content Creation
mkdir -p opcos/bus-business          # Business Services
mkdir -p opcos/fin-finance           # Finance
mkdir -p opcos/edu-education         # Education
mkdir -p opcos/real-real-estate      # Real Estate
mkdir -p opcos/log-logistics         # Logistics
mkdir -p opcos/hlc-healthcare        # Healthcare
mkdir -p opcos/ret-retail            # Retail
mkdir -p opcos/gov-government        # Government
mkdir -p opcos/wealth-wealth         # Wealth Management
mkdir -p opcos/tech-technology       # Technology
mkdir -p opcos/ai-ai-services        # AI Services
mkdir -p opcos/market-marketplace    # Marketplace
mkdir -p opcos/ins-insurance         # Insurance
mkdir -p opcos/util-utilities        # Utilities
mkdir -p opcos/ener-energy           # Energy
```

**Count:** 18 OPCOs ready

- [ ] All 18 OPCO folders created
- [ ] Run: `ls -la opcos/ | wc -l` (should be 20 = 18 opcos + . + ..)

---

## PHASE 3: MOVE VENTURES INTO OPCOS

### CON (Construction OPCO)

```bash
cd /Users/acebless/Documents
mv CON-OS-BUILD/ RE-001-Worldwidebro-Holdings/opcos/con-construction/
```

- [ ] CON ventures moved

### STA (Staffing OPCO)

```bash
mv antwuan-johns-job-search/ RE-001-Worldwidebro-Holdings/opcos/sta-staffing/
mv staffing-os/ RE-001-Worldwidebro-Holdings/opcos/sta-staffing/
```

- [ ] STA ventures moved

### CON (Content Creation OPCO)

```bash
mv clip-farming-system/ RE-001-Worldwidebro-Holdings/opcos/con-content/
```

- [ ] CON-CONTENT ventures moved

### BUS (Business Services OPCO)

```bash
mv pitch-kit/ RE-001-Worldwidebro-Holdings/opcos/bus-business/
mv business-template-marketplace/ RE-001-Worldwidebro-Holdings/opcos/bus-business/
mv HIRING-PACKAGE-OPTION-D/ RE-001-Worldwidebro-Holdings/opcos/bus-business/
mv ec-051-ai-email-marketing/ RE-001-Worldwidebro-Holdings/opcos/bus-business/
```

- [ ] BUS ventures moved

### FIN (Finance OPCO)

```bash
mv fin-001-repo/ RE-001-Worldwidebro-Holdings/opcos/fin-finance/
mv fin-023-investment-portfolio-ai/ RE-001-Worldwidebro-Holdings/opcos/fin-finance/
mv fin-trading-stack/ RE-001-Worldwidebro-Holdings/opcos/fin-finance/
mv fin-ventures/ RE-001-Worldwidebro-Holdings/opcos/fin-finance/
mv magic-portfolio/ RE-001-Worldwidebro-Holdings/opcos/fin-finance/
mv genixbank-repo/ RE-001-Worldwidebro-Holdings/opcos/fin-finance/
```

- [ ] FIN ventures moved

### EDU (Education OPCO)

```bash
mv edu-013-automated-empire-book/ RE-001-Worldwidebro-Holdings/opcos/edu-education/
mv et-001-online-tutoring-platform/ RE-001-Worldwidebro-Holdings/opcos/edu-education/
mv Azriel-Fathering-Content/ RE-001-Worldwidebro-Holdings/opcos/edu-education/
mv generated-courses/ RE-001-Worldwidebro-Holdings/opcos/edu-education/
```

- [ ] EDU ventures moved

### TECH (Technology OPCO)

```bash
mv ai-venture-studio-template/ RE-001-Worldwidebro-Holdings/opcos/tech-technology/
mv Crucix/ RE-001-Worldwidebro-Holdings/opcos/tech-technology/
mv design-system-integrated/ RE-001-Worldwidebro-Holdings/opcos/tech-technology/
```

- [ ] TECH ventures moved

### OTHER OPCOs (as you find matching ventures)

Search for ventures matching other sectors:
```bash
# Find folders by pattern
ls -d */ | grep -E "^[a-z]{3}-[0-9]"  # Shows numbered ventures
```

- [ ] Remaining ventures moved to appropriate OPCOs

---

## PHASE 4: CONSOLIDATE INFRASTRUCTURE

### ✅ Step 4.1: Create Infrastructure Directory

```bash
cd /Users/acebless/Documents
mkdir -p infrastructure/agents
mkdir -p infrastructure/workflows
mkdir -p infrastructure/knowledge
mkdir -p infrastructure/automations
mkdir -p infrastructure/dashboards
mkdir -p infrastructure/databases
mkdir -p infrastructure/config
```

- [ ] Infrastructure directories created

### ✅ Step 4.2: Move Agents

```bash
# Consolidate all agent systems into one location
mv agents/ infrastructure/agents/core/
mv .agents/ infrastructure/agents/config/
mv dexter/ infrastructure/agents/dexter/
mv dexter-orchestrator/ infrastructure/agents/orchestration/
mv ai-boss-os/ infrastructure/agents/ai-boss/
mv autonomous-venture-studio/ infrastructure/agents/studio/
```

- [ ] All agent systems consolidated

### ✅ Step 4.3: Move Workflows

```bash
mv loops/ infrastructure/workflows/
mv make-workflows/ infrastructure/workflows/make/
mv thunderbolt/ infrastructure/workflows/thunderbolt/
mv mission-control/ infrastructure/workflows/mission-control/
```

- [ ] All workflow systems consolidated

### ✅ Step 4.4: Move Knowledge Systems

```bash
mkdir -p infrastructure/knowledge/graphs
mv "Knowledge Graph/" infrastructure/knowledge/graphs/primary/
mv LightRAG/ infrastructure/knowledge/lightrag/
mv iza-os-rag-system/ infrastructure/knowledge/iza-rag/
mv TrendRadar/ infrastructure/knowledge/trendradar/
mv graphify-out/ infrastructure/knowledge/graphify/
mv lightrag_data/ infrastructure/knowledge/lightrag/data/
```

- [ ] All knowledge systems consolidated

### ✅ Step 4.5: Move Databases

```bash
mv supabase/ infrastructure/databases/
mv migrates/ infrastructure/databases/ 2>/dev/null || true
```

- [ ] Database systems moved

### ✅ Step 4.6: Move Dashboards

```bash
mv grafana/ infrastructure/dashboards/
mv PLANE/ infrastructure/dashboards/
```

- [ ] Dashboard systems moved

### ✅ Step 4.7: Move Configuration

```bash
mkdir -p infrastructure/config/
mv .claude/ infrastructure/config/claude/
mv .cursor-free-vip/ infrastructure/config/cursor/
mv .grok/ infrastructure/config/grok/
mv .qwen/ infrastructure/config/qwen/
mv .ruff_cache/ infrastructure/config/ruff/
mv .planning/ infrastructure/config/planning/
```

- [ ] Configuration files organized

---

## PHASE 5: ARCHIVE TEMPORARY/EXPLORATION

### ✅ Step 5.1: Archive Exploration Folders

```bash
mkdir -p 04-ARCHIVED/exploration
mv comfy/ 04-ARCHIVED/exploration/ 2>/dev/null || true
mv MoneyPrinterV2/ 04-ARCHIVED/exploration/ 2>/dev/null || true
mv MoneyPrinterTurbo/ 04-ARCHIVED/exploration/ 2>/dev/null || true
mv RAG-Anything/ 04-ARCHIVED/exploration/ 2>/dev/null || true
mv osint_results/ 04-ARCHIVED/exploration/ 2>/dev/null || true
mv opensre/ 04-ARCHIVED/exploration/ 2>/dev/null || true
```

- [ ] Exploration folders archived

### ✅ Step 5.2: Keep Root Utilities

These stay at `/Users/acebless/Documents/` root:
```bash
# Keep these as-is:
- scripts/
- docs/
- Obsidian/
- .obsidian/
- integrations/
- integrations-venv/
- node_modules/
- repos/
```

- [ ] Root utilities confirmed

---

## PHASE 6: FINAL STRUCTURE VERIFICATION

### ✅ Step 6.1: Verify New Structure

```bash
cd /Users/acebless/Documents

# Count top-level folders (should be ~20-25)
ls -d */ | wc -l

# Verify Holdings exists
ls -la RE-001-Worldwidebro-Holdings/ | head -20

# Verify OPCOs exist
ls -la RE-001-Worldwidebro-Holdings/opcos/ | wc -l

# Verify Infrastructure exists
ls -la infrastructure/ | head -20
```

Expected results:
```
Top-level folders: ~20-25
Holdings subfolder: shows opcos/, plus your files
OPCOs count: 18+
Infrastructure folders: agents/, workflows/, knowledge/, etc
```

- [ ] Structure verified with commands above

### ✅ Step 6.2: Check for Strays

Find any venture-looking folders still at root:

```bash
cd /Users/acebless/Documents
# Find folders starting with sector codes
ls -d */ | grep -E "^(con|sta|fin|edu|tech|bus|ret|log|real|gov|wealth|health|ins|ener|util|market|ai)-"
```

Should return 0 results (all moved to OPCOs)

- [ ] No stray venture folders at root

### ✅ Step 6.3: Verify No Duplicates

```bash
# Check for duplicate folder names
find . -maxdepth 3 -type d -name "*wordwidebro*" -o -name "*holdings*" | sort
```

Should only show:
```
./RE-001-Worldwidebro-Holdings
./04-ARCHIVED/holdings-deprecated/[old versions]
```

- [ ] No duplicate holdings folders

---

## PHASE 7: GIT COMMIT

### ✅ Step 7.1: Check Git Status

```bash
cd /Users/acebless/Documents
git status
```

You'll see:
```
deleted:    [old holdings folders]
deleted:    [ventures moved]
renamed:    infrastructure/ [moved items]
```

### ✅ Step 7.2: Stage All Changes

```bash
git add -A
```

### ✅ Step 7.3: Verify Changes

```bash
git status --short | head -30
```

Should show all your moves/deletes

- [ ] Changes staged

### ✅ Step 7.4: Commit

```bash
git commit -m "$(cat <<'EOF'
refactor: Reorganize Holdings → OPCOs → Ventures → Infrastructure

## Structure Changes
- Consolidated holdings (5 versions → 1: RE-001-Worldwidebro-Holdings)
- Created 18 OPCO directories (con-construction, sta-staffing, etc)
- Organized 30+ ventures into respective OPCOs
- Unified infrastructure: agents (5→1), workflows (3→1), knowledge (3→1)
- Archived deprecated holdings + exploration folders to 04-ARCHIVED

## Benefits
✅ Single source of truth for Holdings
✅ Clear OPCO ownership boundaries  
✅ Ventures organized by sector
✅ Unified agent system location
✅ Consolidated knowledge graphs
✅ Easier navigation for 700+ venture ecosystem

## Before/After
Before: 50+ folders scattered, 5 holdings versions, unclear structure
After: Clean Holdings → OPCOs → Ventures + Infrastructure hierarchy

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
EOF
)"
```

### ✅ Step 7.5: Verify Commit

```bash
git log --oneline -1
git log -1 --stat | head -30
```

- [ ] Commit successful

### ✅ Step 7.6: Push to Remote

```bash
git push origin 2026-05-22-figt
```

- [ ] Changes pushed to origin

---

## FINAL VERIFICATION CHECKLIST

- [ ] Holdings consolidated (1 folder)
- [ ] OPCOs created (18 folders)
- [ ] Ventures moved into OPCOs (30+ folders)
- [ ] Infrastructure unified (agents/workflows/knowledge)
- [ ] Deprecated versions archived
- [ ] No duplicate folders
- [ ] Git add/commit successful
- [ ] Changes pushed to remote
- [ ] Can still access all files
- [ ] Git history preserved

---

## TIME ESTIMATE

| Phase | Time |
|-------|------|
| 1. Holdings | 15 min |
| 2. OPCOs | 10 min |
| 3. Ventures | 45 min |
| 4. Infrastructure | 30 min |
| 5. Archive | 15 min |
| 6. Verify | 10 min |
| 7. Git Commit | 5 min |
| **TOTAL** | **2 hours** |

---

## ROLLBACK (If Something Goes Wrong)

If you mess up and want to undo:

```bash
# Revert last commit (undoes all moves)
git reset --hard HEAD~1

# Files will go back to pre-reorganization state
```

Since you're using git, you can safely experiment. Worst case: revert.

---

## WHAT'S NEXT (After Reorganization)

### Agents Can Now Navigate
```
Holdings → OPCO → Venture → Project → Repository
```

### Knowledge Graph Can Reference
```
Organizational structure (Holdings → OPCO)
Venture relationships (Venture → Venture)
Agent responsibilities (Agent → Venture)
```

### Executive Dashboard Shows
```
Holdings Health
  ↓
OPCO Status (18 views)
  ↓
Venture Progress (700 ventures organized)
  ↓
Project Tracking
```

---

## ⚠️ IMPORTANT NOTES

1. **Do this AFTER you land the Lane A job** (not during applications)
2. **You have 2-3 hours uninterrupted** to avoid git conflicts
3. **All changes are reversible** (git history preserved)
4. **Your working files stay accessible** (just reorganized on disk)
5. **Agents will be able to navigate** much more effectively afterward

---

**Status:** Ready to execute  
**Blocking:** No (job search continues)  
**Reversible:** Yes (git + rollback available)  
**Estimated Time:** 2 hours

**When ready to execute, run the commands in order, checking off each item as you go.**

Questions before you start? (You can do this after Lane A job lands — no rush!)
