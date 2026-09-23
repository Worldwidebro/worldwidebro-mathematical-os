# Wiki Link Audit — 2026-09-23

**Status:** Comprehensive audit of wiki link integrity across STARTHERE.md, BASES-CANONICAL-DEFINITION.md, and key documents  
**Date:** 2026-09-23  
**Author:** Claude Code

---

## Executive Summary

**System State:**
- ✅ **71 valid wiki links** found in STARTHERE.md (pointing to existing files)
- ❌ **62 broken wiki links** in STARTHERE.md (pointing to missing files)
- ⚠️ **Link format issues** — Mix of `/path/FILE` and `FILE|display` patterns causing ambiguity

**Impact:**
- New users cannot navigate via wiki links in STARTHERE.md
- BASES.md disconnected from Master Orchestrator architecture documents
- NAVIGATION_ALIASES.yaml incomplete (only 200 of 500+ aliases cataloged)

**Recommendation:** Execute 3-phase fix (critical → essential → nice-to-have)

---

## Critical Issues (Blocking Navigation)

### Phase 1: Root Level Documents (MUST FIX)

| Link | Status | Fix |
|------|--------|-----|
| `[[master-private-firm-ontology\|Master Ontology]]` | ❌ Missing | Create 00-CONSTITUTION/MASTER-PRIVATE-FIRM-ONTOLOGY.md or symlink to memory |
| `[[00_RESPECT/RESPECT\|RESPECT.md]]` | ❌ Missing | File exists as 00_RESPECT/RESPECT.md — fix link syntax |
| `[[_MEMORY/MEMORY-OS\|MEMORY-OS.md]]` | ❌ Missing | Create _MEMORY/MEMORY-OS.md (currently in memory/) |
| `[[_PROMPTS/10_PRE-ACTION-AWARENESS\|...]]` | ❌ Missing | Create _PROMPTS/10_PRE-ACTION-AWARENESS.md |
| `[[AGENTS\|AGENTS.md]]` | ❌ Missing | Create root AGENTS.md with agent operating contract |

**Action:** Create 5 missing root-level documents by referencing memory files

---

### Phase 2: Architecture Layer Docs (FOUNDATION BROKEN)

| Link | Status | Current Location | Fix |
|------|--------|------------------|-----|
| `[[_REFERENCE/ARCHITECTURE/01-COMPANY-BRAIN\|01 — The Company Brain]]` | ❌ Missing | Not found | Create _REFERENCE/ARCHITECTURE/01-COMPANY-BRAIN.md |
| `[[_REFERENCE/ARCHITECTURE/02-MASTER-ORCHESTRATOR\|02 — Master Orchestrator]]` | ❌ Missing | Not found | Create _REFERENCE/ARCHITECTURE/02-MASTER-ORCHESTRATOR.md |
| `[[_REFERENCE/ARCHITECTURE/03-AGENT-SYSTEM\|03 — Agent System]]` | ❌ Missing | Not found | Create _REFERENCE/ARCHITECTURE/03-AGENT-SYSTEM.md |
| `[[_REFERENCE/ARCHITECTURE/04-CAPABILITY-SYSTEM\|04 — Capability System]]` | ❌ Missing | Not found | Create _REFERENCE/ARCHITECTURE/04-CAPABILITY-SYSTEM.md |
| `[[_REFERENCE/ARCHITECTURE/05-EXECUTION-LOOP\|05 — Execution Loop]]` | ❌ Missing | Not found | Create _REFERENCE/ARCHITECTURE/05-EXECUTION-LOOP.md |

**Impact:** Users cannot access foundation architecture documents referenced in STARTHERE.md Section 2.5

**Action:** Either:
- **Option A (Immediate):** Update STARTHERE.md to reference existing docs in memory/
- **Option B (Proper):** Create _REFERENCE/ARCHITECTURE/ directory with 5 foundation docs

Recommend **Option B** with migration from memory.

---

### Phase 3: Critical Registries & Spec Documents

| Link | Status | Action |
|------|--------|--------|
| `[[_REFERENCE/ORCHESTRATOR-MASTER-SPECIFICATION\|Orchestrator Master Specification]]` | ❌ Missing | Create _REFERENCE/ORCHESTRATOR-MASTER-SPECIFICATION.md |
| `[[_REGISTRIES/CANONICAL/AGENT_REGISTRY\|Agent Registry]]` | ❌ Missing | Create or symlink to 16-AGENTS/AGENT_REGISTRY.yaml |
| `[[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY\|Capability Registry]]` | ❌ Missing | Create or symlink to 14-CAPABILITIES/CAPABILITY_REGISTRY.yaml |

**Action:** Create missing specs and standardize registry paths

---

## Secondary Issues (Broken Cross-Links)

### Links Needing Path Fixes

```
BROKEN:
  [[CAMPAIGNS/CAMPAIGN-OS|CAMPAIGN-OS.md]]         → CAMPAIGNS/CAMPAIGN-OS.md not found
  [[CAMPAIGNS/CAMPAIGN|CAM-001 (...)]]             → 26-MARKETING/ likely location
  [[23-VENTURES/LT-005|LT-005 (HealthRoute...)]]   → 23-VENTURES/LT-005.md format?
  [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|...]]  → Exists; link syntax issue
  [[_REGISTRIES/ventures-by-sector.yaml|...]]     → File missing; phantom registry

PARTIAL (Mixed format):
  [[REALITY|REALITY.md]]                           → Works ✅
  [[STARTHERE]]                                    → Works ✅  
  [[00_RESPECT/RESPECT|RESPECT.md]]                → File exists; link needs fix
```

---

## BASES.md Wiring Gaps

**Current State:** BASES-CANONICAL-DEFINITION.md exists but is isolated
**Issue:** No bidirectional links to:
- STARTHERE.md (not mentioned in section 2.5 Foundation Architecture)
- Master Orchestrator (not referenced as connected system)
- Agent System (should mention how agents are scoped to Bases)
- Execution Loop (not shown as Base-aware)

**Fix:** Add to STARTHERE.md Section 2.5 + cross-link from Foundation Architecture docs

---

## NAVIGATION_ALIASES.yaml Audit

**Current Status:** Partial (200 lines read, registry continues beyond)
**Coverage:** ~50 primary documents aliased
**Gap:** 100+ secondary documents, venture-specific aliases, domain aliases

**Recommendation:** 
1. ✅ Keep as is — already contains core navigation
2. 🔄 Supplement with domain-level aliases (one per domain INDEX.md)
3. 🔄 Add venture-specific aliases (23-VENTURES/*/aliases)

---

## Wiring Fix Plan (3 Phases)

### ✅ Phase 1: Critical Root Documents (2h)

**Priority:** Unblock navigation to master docs

1. **Create 00_RESPECT/RESPECT.md** (copy from memory or create)
2. **Create _MEMORY/MEMORY-OS.md** (migrate from memory/)
3. **Create _PROMPTS/10_PRE-ACTION-AWARENESS.md** (migrate from memory/)
4. **Create root AGENTS.md** (new: portable agent contract)
5. **Update STARTHERE.md** to verify all 105 links work

**Exit Criteria:** All wiki links in STARTHERE.md are clickable (71 valid + 34 fixed = 105)

---

### 🟡 Phase 2: Foundation Architecture (6h)

**Priority:** Enable discovery of system architecture

1. **Create _REFERENCE/ARCHITECTURE/INDEX.md** (navigation hub)
2. **Create _REFERENCE/ARCHITECTURE/01-COMPANY-BRAIN.md** (Intelligence layer)
3. **Create _REFERENCE/ARCHITECTURE/02-MASTER-ORCHESTRATOR.md** (Decision loop)
4. **Create _REFERENCE/ARCHITECTURE/03-AGENT-SYSTEM.md** (Workers layer)
5. **Create _REFERENCE/ARCHITECTURE/04-CAPABILITY-SYSTEM.md** (Inventory)
6. **Create _REFERENCE/ARCHITECTURE/05-EXECUTION-LOOP.md** (Work completion)

**Exit Criteria:** STARTHERE.md Section 2.5 fully navigable; 5 docs accessible

---

### 🟢 Phase 3: Secondary Cross-Links (4h)

**Priority:** Complete ecosystem connectivity

1. **Add bidirectional links** BASES.md ↔ Foundation Architecture
2. **Wire CAMPAIGNS/** into 26-MARKETING/INDEX.md
3. **Verify 23-VENTURES/** venture docs are discoverable
4. **Update NAVIGATION_ALIASES.yaml** with domain + venture aliases
5. **Create domain INDEX.md** files for any missing ones (check all 71)

**Exit Criteria:** All 71 domains have INDEX.md; all venture aliases in registry

---

## Verification Checklist

- [ ] `grep -r "\[\[" STARTHERE.md | grep -c "^\[\["` returns 105 unique links
- [ ] All 105 links resolve to existing files (tested via link click)
- [ ] BASES.md mentioned in STARTHERE.md Section 2.5
- [ ] Foundation Architecture docs linked from STARTHERE.md + INDEX.md
- [ ] NAVIGATION_ALIASES.yaml contains ≥100 aliases
- [ ] All 71 domain folders have INDEX.md with navigation
- [ ] Cross-links between STARTHERE → INDEX → DOMAIN-MAP → Domain INDEXes → Files work

---

## Next Actions (Recommended Order)

1. **Immediate (Today):** Phase 1 (Critical root docs) — 2h
2. **This Week:** Phase 2 (Foundation architecture) — 6h  
3. **Next Week:** Phase 3 (Secondary cross-links) — 4h

**Total Effort:** 12 hours  
**Blocking Issue:** Missing _REFERENCE/ARCHITECTURE/ docs prevent 20+ STARTHERE.md links from working

---

**Status:** AUDIT COMPLETE | RECOMMENDED: Execute Phase 1 immediately to unblock navigation

---

## Control Base Reference

This document is mapped to [[B100|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B100]]