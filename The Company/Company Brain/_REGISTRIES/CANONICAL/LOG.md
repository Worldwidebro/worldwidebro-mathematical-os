# Reconciliation Wiki — Timeline Log

**Purpose:** Append-only record of reconciliation work, discoveries, and milestones  
**Format:** `## [YYYY-MM-DD] [phase | ingest | query | lint | decision] | Title`  
**Updated:** 2026-09-23  
**Navigation:** [[STARTHERE|../../STARTHERE.md]] | [[INDEX|INDEX.md]] | [[DOMAIN-MAP|DOMAIN-MAP.md]] | [[LOG|LOG.md]]

---

## [2026-09-23] ingest | Data Scientist Phase 4-2 Analysis Complete

**Session:** Continuation of Sep 20-23 reconciliation analysis  
**Input:** ALL_789_VENTURES_36_SECTOR_ALIGNMENT_DEDUPED.csv, sector_classification_model.py, graft discovery  
**Output:** RECONCILIATION-ANALYSIS-WORKFLOW-2026-09-23.md (5-phase execution plan)

**Key Findings:**
- ✅ **Option 4 (Root Cause):** Registry pre-dedup (789) vs CSV post-dedup (655). 134 duplicates removed.
- ✅ **Option 3 (Classification Model):** 177 HIGH-CONFIDENCE misclassifications (tech-domain vs business-domain)
- ✅ **Option 2 (Workflow Design):** 5-phase reconciliation plan (Sep 26 - Oct 2) with SQL migrations, audit queries, verification

**Blockers:** 4 founder decisions pending (venture count, sector model, bases table, entities registry)

**Next:** Phase 1 execution (Sep 26) or Option 1 investigation (209 missing ventures)

---

## [2026-09-23] ingest | LLM Wiki Structure Established

**Input:** LLM Wiki pattern (personal knowledge base architecture)  
**Output:** INDEX.md (content-oriented catalog), LOG.md (chronological timeline)

**Decision:** Apply persistent wiki pattern to reconciliation work:
- Raw sources: CSV (immutable)
- Wiki: Registries + analysis documents (LLM-maintained)
- Schema: RECONCILIATION-ANALYSIS-WORKFLOW (structured process)

**Maintenance:** Index updated on every Phase completion; Log updated for discoveries & decisions

---

## [2026-09-23] ingest | Graft Codebase Discovery

**Query:** "venture reconciliation deduplication sector classification mapping"  
**Result:** 8 relevant functions found (merge_sector, merge_venture, neo4j_merge_classification, VentureOrchestrator, etc.)

**Integration:** Graph-native functions ready for Neo4j sync after Supabase reconciliation complete

---

## [2026-09-25] audit | Ground Truth Divergence Critical

**Discovery:** SUPABASE-RECONCILIATION-PLAN-2026-09-25.md created  

Three competing models:
- **CSV (Post-Dedup):** 655 unique ventures, 36 sectors, business-domain classified
- **Registries (Pre-Dedup):** 789 ventures claimed, 36 sectors, mixed classification
- **Supabase (Operational):** 580 real ventures, 25 categories, live state

**Status:** Phase 2 Base gate evaluation PAUSED until venture assignments verified

**Founder Decisions Required:**
1. Venture count reality (580 vs 789 gap)
2. Sector model direction (25 vs 36)
3. Bases table location (Supabase vs YAML)
4. Entities registry verification (legal_entities schema)

---

## [2026-09-25] audit | Phase 2 Critical Findings

**Source:** AUDIT-PHASE2-FINDINGS-2026-09-25.md

**Critical Finding #1: LT-005 & LT-011 Misclassification**
- Claimed: SEC-017 (Logistics)
- Truth: SEC-001 (Beauty & Wellness) per CSV
- Impact: BASE-017 incorrectly claims key ventures; BASE-001 assignment wrong
- Action: Query Supabase to resolve

**Critical Finding #2: Venture Count Errors (82-90%)**
- SEC-014: Registry 117 vs CSV 21 (-82%)
- SEC-024: Registry 243 vs CSV 24 (-90%)
- SEC-029: Registry 120 vs CSV 16 (-87%)
- Root cause: Registry built from pre-dedup counts
- Action: Accept CSV as truth; recalculate sector concentrations

**Critical Finding #3: SEC-012 Unmapped**
- Registry: "Healthcare — Staging (unknown count)"
- CSV: 4 real ventures exist
- Action: Create BASE-012; instantiate healthcare sector

**Status:** Base gate evaluation invalid until corrected

---

## [2026-09-24] ingest | Registry Freeze (Phase 1)

**Output:** REGISTRY-README-SEP24.md (canonical freeze documentation)

**Registries Locked:**
- SECTOR-REGISTRY.yaml (37 sectors, 10 active + 25 staging + 1 anomaly)
- OPCO-REGISTRY.yaml (35 OpCos)
- BASE-REGISTRY.yaml (36 bases, 11-point gate framework)
- VENTURE-REGISTRY.yaml (6 priority ventures, 783 staged)
- SECTOR-VENTURE-MANIFEST.csv (6 → 789 multidimensional classification, in-progress)

**Phase 2 Plan:** Classification audit (SEC-017, SEC-020, SEC-012, SEC-024, SEC-029, SEC-014)  
**Phase 2 Findings:** 3 catastrophic misclassifications detected; reconciliation initiated

---

## [2026-09-23] ingest | Deduplication Audit Complete

**Source:** ALL_789_VENTURES_36_SECTOR_ALIGNMENT_DEDUPED.csv  
**Input:** 789 original venture rows + duplicate detection analysis  
**Output:** DEDUPLICATION_AUDIT_2026-09-23.md

**Findings:**
- 655 unique ventures (after dedup)
- 134 duplicate rows removed (from 83 duplicate venture_ids)
- Strategy: Kept first occurrence; removed N-1 duplicates per venture_id
- Actual portfolio: ~83 unique ventures (not 789)

**Impact:** Registry counts are pre-dedup; CSV counts are ground truth

---

## [2026-09-23] ingest | Sector Classification Model Built

**Source:** sector_classification_model.py (graft discovery)  
**Algorithm:** Venture ID prefix + keyword matching

**Misclassification Detection:**
- FIN-* → incorrectly in SEC-032 (AI/ML) instead of SEC-008 (Finance)
- LT-* → scattered instead of consolidated in SEC-017 (Logistics)
- HR-*, MKT-* → mixed sectors instead of correct primary sector

**Output:** 177 HIGH-CONFIDENCE misclassifications flagged

**Recommendation:** Re-classify by business-domain (not technology-domain)

---

## [2026-09-20] query | Unit 1.1 Execution Complete

**Reference:** unit-1-1-execution-complete.md  

625 lines across 6 files. Cache logic verified 9/9 mock tests. Agent count: 310 in database.

---

## [2026-09-17] plan | Phase 2 Graph-Native Architecture

**Reference:** session-2026-09-17-phase-2-graph-native.md

Neo4j schema deployed (constraints, indexes, gates). YAML→Neo4j migration pipeline ready. 14-day execution checklist (Sep 17–Oct 1).

---

## Outstanding Items

### Pending Founder Decisions (Sep 25-26)

- [ ] **Decision 1:** Venture count reality (209 gap)
- [ ] **Decision 2:** Sector model direction (25 vs 36)
- [ ] **Decision 3:** Bases table location (Supabase vs YAML)
- [ ] **Decision 4:** Entities registry verification

### Pending Analysis (Option 1, Sep 24-26)

- [ ] Investigate 209 "missing" ventures (phantom, planned, or corrupt?)
- [ ] Cross-reference CSV vs Supabase vs Neo4j venture lists
- [ ] Identify phantom duplicates vs legitimate variants

### Pending Execution (Phases 1-5, Sep 26 - Oct 2)

- [ ] **Phase 1:** Supabase schema audit + category mapping
- [ ] **Phase 2:** Classification audit (177 misclassifications)
- [ ] **Phase 3:** Multidimensional venture lookup + Base assignments
- [ ] **Phase 4:** SQL migrations + table population (36 sectors, 35 OpCos, 36 Bases)
- [ ] **Phase 5:** Verification queries + registry sync

### Pending Integration (Oct 1-31)

- [ ] Base gate evaluation (11-point framework)
- [ ] Base WHOAMI.md creation (6 activated bases)
- [ ] Agent assignment + dispatch routers
- [ ] Revenue loop activation (OPS-001, LT-005, CALLCENTER)

---

## Maintenance Notes

- **Index:** Updated when new wiki pages created or major phases complete
- **Log:** Append-only; entries never deleted or modified (immutable timeline)
- **Cross-references:** Wiki links [[like-this]] track dependencies
- **Periodic Lint:** Check for contradictions, orphan pages, stale claims (weekly)

---

**Last Entry:** 2026-09-23  
**Next Update:** 2026-09-26 (after Phase 1 execution)  
**Lint Check:** 2026-09-30

---

## Control Base Reference

This document is mapped to [[B100|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B100]]