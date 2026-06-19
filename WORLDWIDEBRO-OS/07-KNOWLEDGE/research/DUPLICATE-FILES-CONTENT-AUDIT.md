# Duplicate Files Content Audit (Before Deletion)

**Purpose:** Identify unique information in each duplicate that must be merged before deletion

---

## 1. MASTER INDEX DUPLICATES

### File A: `00-MASTER-INDEX.md`
```bash
wc -l < /Users/acebless/Documents/00-MASTER-INDEX.md
head -50 /Users/acebless/Documents/00-MASTER-INDEX.md
```

### File B: `ORB-MASTER-CONNECTOR-2026-06-11.md`
```bash
wc -l < /Users/acebless/Documents/ORB-MASTER-CONNECTOR-2026-06-11.md
head -50 /Users/acebless/Documents/ORB-MASTER-CONNECTOR-2026-06-11.md
```

### File C: `civilization-os-local/MASTER-FOLDER-MAP.md`
```bash
wc -l < /Users/acebless/Documents/civilization-os-local/MASTER-FOLDER-MAP.md
head -50 /Users/acebless/Documents/civilization-os-local/MASTER-FOLDER-MAP.md
```

**Decision needed:**
- [ ] What unique references does ORB-MASTER have that 00-MASTER doesn't?
- [ ] What unique folder mappings does civilization-os-local have?
- [ ] Merge into 00-MASTER-INDEX.md or keep separate?

---

## 2. REPOSITORY REGISTRY DUPLICATES

### File A: `Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json` (904KB)
```bash
head -20 /Users/acebless/Documents/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json | jq .
```

### File B: `civilization-os-local/REPO_REGISTRY.json`
```bash
wc -l < /Users/acebless/Documents/civilization-os-local/REPO_REGISTRY.json
head -20 /Users/acebless/Documents/civilization-os-local/REPO_REGISTRY.json | jq . 2>/dev/null || head -20 /Users/acebless/Documents/civilization-os-local/REPO_REGISTRY.json
```

### File C: `WORLDWIDEBRO-OS/REGISTRIES/repository_registry_pilot.json`
```bash
wc -c < /Users/acebless/Documents/WORLDWIDEBRO-OS/REGISTRIES/repository_registry_pilot.json
```

**Decision needed:**
- [ ] Are these the SAME data (different timestamps)?
- [ ] Do they have different repo counts?
- [ ] Which one is most recent?
- [ ] Can others be deleted as backups?

---

## 3. VENTURE MAPPING DUPLICATES

### File A: `VENTURE-HANDLE-MAP.json` (Active)
```bash
cat /Users/acebless/Documents/VENTURE-HANDLE-MAP.json | head -20
```

### File B: `.planning/venture-hub-alignment.json` (Auto-synced)
```bash
cat /Users/acebless/Documents/.planning/venture-hub-alignment.json | head -20
```

### File C: `MC-OPERATIONS/config/ventures.json` (Legacy?)
```bash
cat /Users/acebless/Documents/MC-OPERATIONS/config/ventures.json 2>/dev/null | head -20 || echo "File not found or empty"
```

### File D: `The office/ventures.json` (Legacy?)
```bash
cat /Users/acebless/Documents/The\ office/ventures.json 2>/dev/null | head -20 || echo "File not found or empty"
```

**Decision needed:**
- [ ] Is VENTURE-HANDLE-MAP the authoritative source?
- [ ] Is .planning/venture-hub-alignment auto-synced from Supabase?
- [ ] Are MC-OPERATIONS and The office configs actually used?
- [ ] Can we delete configs or do they feed other systems?

---

## 4. ROADMAP DUPLICATES (20+ CON files)

### Sample: CON-001 vs CON-009 (Check structure)
```bash
wc -l /Users/acebless/Documents/CON-001-ACE-CONSTRUCTION-BANKABILITY-ROADMAP.md
wc -l /Users/acebless/Documents/CON-009-ROOFING-COMPANY-BANKABILITY-ROADMAP.md

echo "=== CON-001 structure ===" 
head -30 /Users/acebless/Documents/CON-001-ACE-CONSTRUCTION-BANKABILITY-ROADMAP.md | grep "^#"

echo "=== CON-009 structure ==="
head -30 /Users/acebless/Documents/CON-009-ROOFING-COMPANY-BANKABILITY-ROADMAP.md | grep "^#"
```

**Decision needed:**
- [ ] Are all 20 identical templates (can be replaced with CSV)?
- [ ] Does each have venture-specific information?
- [ ] Can we consolidate into a single template + data CSV?

---

## 5. STRATEGY DUPLICATES

### File A: `CONSOLIDATION-STRATEGY.md`
```bash
wc -l < /Users/acebless/Documents/CONSOLIDATION-STRATEGY.md
grep "^## " /Users/acebless/Documents/CONSOLIDATION-STRATEGY.md | head -10
```

### File B: `WORLDWIDEBRO-UNIFIED-OS/CAPITAL-TARGETING-STRATEGY.md`
```bash
wc -l < /Users/acebless/Documents/WORLDWIDEBRO-UNIFIED-OS/CAPITAL-TARGETING-STRATEGY.md 2>/dev/null || echo "Not found"
grep "^## " /Users/acebless/Documents/WORLDWIDEBRO-UNIFIED-OS/CAPITAL-TARGETING-STRATEGY.md 2>/dev/null | head -10
```

**Decision needed:**
- [ ] Does CAPITAL-TARGETING have unique content not in CONSOLIDATION-STRATEGY?
- [ ] Can it be merged as a section?

---

## 6. CHECKLIST DUPLICATES

### File A: `PHASE-1-ENTITY-FORMATION-CHECKLIST.md` (Keep?)
```bash
wc -l < /Users/acebless/Documents/PHASE-1-ENTITY-FORMATION-CHECKLIST.md
```

### File B: `AGENTIC-INBOX-IMPLEMENTATION-CHECKLIST.md` (Archive?)
```bash
wc -l < /Users/acebless/Documents/AGENTIC-INBOX-IMPLEMENTATION-CHECKLIST.md
```

### File C: `books/FRIDAY-LAUNCH-CHECKLIST.md` vs `edu-013-automated-empire-book/playbooks/FRIDAY-LAUNCH-CHECKLIST.md`
```bash
diff /Users/acebless/Documents/books/FRIDAY-LAUNCH-CHECKLIST.md \
     /Users/acebless/Documents/edu-013-automated-empire-book/playbooks/FRIDAY-LAUNCH-CHECKLIST.md 2>/dev/null || echo "Files differ"
```

**Decision needed:**
- [ ] Are FRIDAY-LAUNCH checklists identical?
- [ ] Which version is authoritative?

---

## ACTION: Run This Audit First

Before deleting ANYTHING:

1. For each duplicate category above, run the commands
2. Document what unique info exists in each
3. Plan merges (don't just delete)
4. Mark which are truly identical backups vs. which have different data

---

## Template for Recording Findings

```markdown
### Duplicate Group: [NAME]

Files involved:
1. PRIMARY: [file path] — [purpose]
2. DUPLICATE: [file path] — [purpose]
3. DUPLICATE: [file path] — [purpose]

Unique content in each:
- PRIMARY: [what's unique]
- DUPLICATE 1: [what's unique/different]
- DUPLICATE 2: [what's unique/different]

Merge plan:
- [ ] Merge DUPLICATE 1 data into PRIMARY
- [ ] Keep DUPLICATE 2 because [reason]
- [ ] Delete DUPLICATE 3 (identical to PRIMARY)

Confirmation:
- [ ] All unique data preserved
- [ ] References updated
- [ ] Safe to delete
```

---

## Status

This audit template is ready. Run the commands above to populate findings before executing any deletions.

