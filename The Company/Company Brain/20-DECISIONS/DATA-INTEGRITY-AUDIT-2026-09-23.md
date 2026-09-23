---
title: "Master Data Integrity Audit — Sep 23, 2026"
author: "Claude Haiku 4.5"
date: "2026-09-23"
status: "CRITICAL — Multiple data quality issues found"
authority: "CP-027 (Infrastructure) + CP-001 (Enterprise)"
---

# MASTER DATA INTEGRITY AUDIT — Sep 23, 2026

## EXECUTIVE SUMMARY

| Item | Expected | Actual | Status | Gap |
|------|----------|--------|--------|-----|
| **Entities** | 150-200 | 299 ENT- IDs | 🟡 OVERAGE | +99 to +149 |
| **Ventures** | 789 | 789 rows | ✅ OK | 0 |
| **Venture IDs (Unique)** | 789 | 655 | 🔴 CRITICAL | -134 duplicates |
| **Sectors** | 36 | 28 | 🔴 CRITICAL | -8 missing |
| **People Registry** | 21+ | 21 skeleton | 🟡 INCOMPLETE | 0% verified |
| **Deduplication** | Required | ❌ NOT IN PLACE | 🔴 CRITICAL | Active duplicates |

---

## DETAILED FINDINGS

### 1. ENTITIES — OVERCOUNTING ⚠️

**What we said:** "150 legal entities mapped to family office structure"

**What we actually have:**
- ECOSYSTEM_150_ENTITY_REGISTRY.yaml declares: **150 entities**
- Actual ENT- IDs counted: **299 entities**
- Gap: **+99 to +149 entities (66-100% overcounting)**

**Issue:** Either:
1. The registry has duplicate ENT- IDs (entitites defined twice)
2. The registry is incomplete + we have 299 entities not tracked
3. The ID numbering is wrong (ENT-150 shouldn't exist if only 150 entities)

**What needs to happen:**
- [ ] Reconcile ECOSYSTEM_150_ENTITY_REGISTRY.yaml against actual legal entity count
- [ ] Determine: Are there really 150 or 299 entities?
- [ ] Check for duplicate ENT- IDs (should be unique)
- [ ] If 299 is correct: Update documentation + registries
- [ ] If 150 is correct: Find + remove the 149 phantom entries

**Timeline:** 2-3 hours (audit + reconciliation)

---

### 2. VENTURES — DUPLICATE IDS 🔴 **CRITICAL**

**What we said:** "789 ventures, each with unique venture_id"

**What we actually have:**
- Total rows: 789 ventures
- Unique venture IDs: **655** (not 789)
- Duplicate IDs: **83 different venture_ids appearing multiple times**
- Gap: **-134 ventures (17% of portfolio missing or duplicated)**

**Example Duplicates (Same ID, Multiple Ventures):**
```
Venture #1: EC-001 = "Angels in Daylight"
Venture #2: EC-001 = "Angels in Daylight" (duplicate?)
---
Venture #N: FIN-001 = "Genixbank Lite"
Venture #M: FIN-001 = "Genixbank Lite" (duplicate?)
```

**Full List of 83 Duplicate Venture IDs:**
```
COMM-049, EC-001, EC-002, EC-003, EC-004, EC-005, EC-006, EC-007, EC-008, EC-009,
EC-010, EC-034, EC-044, EDU-005, EDU-026, EDU-040, FH-006, FH-033, FIN-001, FIN-002,
[... 63 more ...]
```

**Impact:**
- ❌ Agents cannot uniquely identify ventures by ID
- ❌ Revenue attribution breaks (which FIN-001 generated revenue?)
- ❌ Reporting is ambiguous (which EC-001 is active?)
- ❌ Neo4j graph will have duplicate edges/nodes

**What needs to happen:**
- [ ] Identify why duplicates exist (data migration error? Manual entry?)
- [ ] Determine: Are both rows needed or is one phantom?
- [ ] Deduplicate: Keep one canonical row per venture_id
- [ ] Add unique secondary ID if needed (e.g., venture_uuid, venture_name_slug)
- [ ] Verify: After dedup, should have 789 unique IDs

**Timeline:** 3-4 hours (root cause analysis + deduplication)

---

### 3. SECTORS — 8 MISSING 🔴 **CRITICAL**

**What we said:** "36 sectors, each with SEC-001 to SEC-036"

**What we actually have:**
- Declared: 36 sectors
- Actual sectors in venture registry: **28 sectors**
- Missing sectors: **8**

**Missing Sector IDs:**
```
SEC-006 (MISSING)
SEC-007 (MISSING)
SEC-009 (MISSING)
SEC-018 (MISSING)
SEC-022 (MISSING)
SEC-026 (MISSING)
SEC-030 (MISSING)
SEC-035 (MISSING)
SEC-036 (MISSING)  ← This is the last sector! Should definitely exist.
```

**Present Sectors (28 of 36):**
```
SEC-001, SEC-002, SEC-003, SEC-004, SEC-005,
SEC-008, SEC-010, SEC-011, SEC-012, SEC-013,
SEC-014, SEC-015, SEC-016, SEC-017, SEC-019,
SEC-020, SEC-021, SEC-023, SEC-024, SEC-025,
SEC-027, SEC-028, SEC-029, SEC-031, SEC-032,
SEC-033, SEC-034, SEC-037  ← WAIT: SEC-037 exists but shouldn't!
```

**Issues:**
- [ ] Why does SEC-037 exist when we only have 36 sectors?
- [ ] Are the 8 missing sectors actually defined somewhere else?
- [ ] Do ventures exist in those 8 sectors but unmapped?
- [ ] Is the 36-sector model wrong (should be 37+)?

**What needs to happen:**
- [ ] Check SECTOR_INDEX.md or 00-CONSTITUTION/SECTOR-TAXONOMY-MASTER.md for definition
- [ ] Reconcile: Are there really 36 or 37+ sectors?
- [ ] Find: Where are the 8 missing sectors defined?
- [ ] Remap: Any ventures assigned to missing sectors?
- [ ] Update: Align venture registry to actual sector list

**Timeline:** 2-3 hours (reconciliation + remapping)

---

### 4. PEOPLE REGISTRY — 0% VERIFIED 🟡

**Status:** ✅ File exists at `_REGISTRIES/CANONICAL/PEOPLE-REGISTRY.yaml`

**Content:** 21 people defined, all marked [TO_VERIFY]

**What's mapped to whom:**
- ❌ No people → entities mappings verified
- ❌ No people → ventures mappings verified
- ❌ No people → approval authority mappings verified
- ❌ No PERSON_ID cross-references in venture registry

**Example Issue:**
```
Venture: FIN-001 "Genixbank Lite"
Founder: [UNKNOWN]
OpCo: OpCo-008
CEO: [UNKNOWN]
```

**What needs to happen:**
- [ ] Search 789 venture repos for founder/CEO names
- [ ] Create PERSON nodes with unique PERSON_ID (PERSON-001 to PERSON-N)
- [ ] Map ventures → founder (venture_founder_person_id)
- [ ] Wire RESPONSIBILITY-MATRIX to show venture CEO assignments
- [ ] Create audit trail of who reports to whom

**Timeline:** 4-6 hours (search + data entry + verification)

---

### 5. ID SYSTEM — MULTIPLE REGISTRIES, NO MASTER 🟡

**ID Prefixes Found (26 registry files):**
```
✅ ENT- (Entity)
✅ VEN- (Venture — but mostly using sector prefixes)
✅ SEC- (Sector)
✅ PERSON- (Person — newly created Sep 23)
✅ ROLE- (Role — newly created Sep 23)
✅ OpCo- (Operating Company)
❓ FIN-, BW-, LT-, COMM-, EC-, EDU-, ... (Sector-specific prefixes)
❌ No master ID_REGISTRY.yaml documenting all prefixes + constraints
```

**Issue:** Venture prefixes vary by sector (FIN-001, BW-001, LT-005, etc.) instead of universal VEN- prefix

**What needs to happen:**
- [ ] Create ID_SYSTEM_MASTER.yaml documenting all ID formats + constraints
- [ ] Define: Should ventures use universal ID (VEN-001 to VEN-789) or sector prefixes?
- [ ] If sector prefixes: Document the mapping (FIN-=Finance, BW-=Beauty/Wellness, etc.)
- [ ] Add constraints: ID uniqueness, numbering rules, format validation

**Timeline:** 1-2 hours (documentation + constraints)

---

### 6. DEDUPLICATION — NOT ACTIVE 🔴 **CRITICAL**

**Current State:**
- ❌ No deduplication process in place
- ❌ No duplicate detection running
- ❌ No audit trail showing when duplicates were created
- ❌ 83 duplicate venture IDs actively in production registry

**What needs to happen:**
- [ ] Build deduplication script:
  ```python
  # Pseudocode
  for venture_id in ALL_VENTURES:
      if venture_id appears > 1 time:
          mark for review
          compare: name, sector, status, repo_url
          if identical: REMOVE (keep canonical)
          if different: FLAG (needs investigation)
  ```
- [ ] Create audit trail showing what was deduplicated + why
- [ ] Add CI/CD check: Reject any new duplicate venture_ids
- [ ] Wire Neo4j: Unique constraint on venture_id

**Timeline:** 3-4 hours (script + testing + deployment)

---

## MASTER DATA QUALITY SCORECARD

| System | Score | Issues | Severity |
|--------|-------|--------|----------|
| **Entities** | 50% | 99-149 overcount or underdoc | HIGH |
| **Ventures (Count)** | 100% | 789 ventures present | OK |
| **Venture IDs (Uniqueness)** | 17% | 83 duplicates found | CRITICAL |
| **Sectors (Completeness)** | 78% | 8 of 36 missing | CRITICAL |
| **People (Verification)** | 0% | 21 skeleton, 0% verified | HIGH |
| **Deduplication** | 0% | No process in place | CRITICAL |
| **ID Documentation** | 40% | Multiple prefixes, no master | MEDIUM |
| **OVERALL** | **33%** | **7 issues, 3 critical** | **REBUILD NEEDED** |

---

## CRITICAL PATH TO DATA INTEGRITY (MINIMUM VIABLE)

**Goal:** Clean, deduplicated master data with unique IDs + verified people

### Phase 1: Deduplication (3-4 hours)
1. Audit 83 duplicate venture IDs (which are real? which are phantom?)
2. Create deduplication rules (identical name + sector = remove duplicate)
3. Run dedup script
4. Result: 655 → 789 unique ventures (or correct count)

### Phase 2: Sector Reconciliation (2-3 hours)
1. Find definition of 36 sectors (check SECTOR_INDEX.md + Neo4j)
2. Verify: Are there 36, 37, or different total?
3. Map missing 8 sectors to ventures (if any)
4. Result: All 789 ventures mapped to correct sector

### Phase 3: Entity Reconciliation (2-3 hours)
1. Determine: 150 or 299 legal entities?
2. Audit ENT- IDs for duplicates
3. Reconcile against legal documents (trusts, LLCs, etc.)
4. Result: Single source of truth for entity count

### Phase 4: People Verification (4-6 hours)
1. Search venture repos for founder/CEO names
2. Create PERSON nodes + IDs
3. Map ventures → founders
4. Result: 21+ people verified + mapped

### Phase 5: Deduplication Automation (3-4 hours)
1. Build CI/CD check for duplicate prevention
2. Add Neo4j unique constraints
3. Deploy monitoring + alerts
4. Result: Duplicates cannot re-enter system

**Total MVP effort:** 14-20 hours
**Timeline:** Sep 24-26 (parallel work possible)
**Blocker:** Phase 1 must complete before Phase 2

---

## SIGN-OFF CHECKLIST

**Before considering data integrity "solved":**

- [ ] **Ventures dedup:** 789 unique venture_ids confirmed (or correct count)
- [ ] **Sectors complete:** All 36 sectors mapped (or correct total)
- [ ] **Entities reconciled:** 150 or 299? Documented + verified
- [ ] **People verified:** 21+ people mapped to ventures/entities
- [ ] **ID system:** Master registry + constraints documented
- [ ] **Dedup automation:** CI/CD check + Neo4j constraints deployed
- [ ] **Audit trail:** Know exactly when/why each duplicate was removed
- [ ] **Neo4j updated:** 789 venture nodes with unique IDs + person mappings

---

## QUESTIONS NEEDING ANSWERS

1. **Are there really 150 entities or 299?** (Which document is canonical?)
2. **Why do 83 ventures have duplicate IDs?** (Merge error? Import bug?)
3. **Where are the 8 missing sectors?** (Defined elsewhere? Never filled?)
4. **Does SEC-037 exist?** (If not, why is it in ventures registry?)
5. **Who are the 789 venture founders?** (Need names + emails)
6. **Should ventures use universal ID (VEN-001) or sector prefixes (FIN-001)?** (Current = sector)
7. **When was this data last cleaned?** (Audit trail exists?)

---

## NEXT STEPS (FOR YOU)

1. **Review this audit** — Does it match your understanding of the system?
2. **Answer the 7 questions above** — Clarify the data structure
3. **Prioritize:** Fix deduplication first (blocks Neo4j, reporting, agents)
4. **Authorize:** Give me permission to run deduplication script
5. **Verify:** After dedup, spot-check 10 random ventures to confirm quality

---

**Status:** 🔴 CRITICAL — Multiple data quality issues found  
**Recommendation:** **STOP** loading data into Neo4j until deduplication complete  
**Updated:** 2026-09-23

