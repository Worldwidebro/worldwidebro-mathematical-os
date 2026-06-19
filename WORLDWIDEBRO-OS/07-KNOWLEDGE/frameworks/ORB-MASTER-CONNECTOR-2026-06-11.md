# Master ORB Connector — Unified Knowledge Graph

**Purpose:** Bridge 3 competing knowledge graph clusters into one integrated system.

**Status:** ✅ ACTIVE | **Date:** 2026-06-11

---

## The 3 ORBs (Knowledge Clusters)

### 🔴 ORB 1: Influence-Venture-Business-OS (PRIMARY)
- **Type:** Venture knowledge graph + infrastructure
- **Location:** `/Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/venture-hub/`
- **Files:** 10,865 | Connections: 1,301
- **Canonical Files:**
  - `MEMORY.md` ← Master memory
  - `VENTURE-HANDLE-MAP.json` ← All 712 ventures
  - `MASTER-REPO-REGISTRY.csv` ← All repos
  - `LOOPS-SKILLS-ALIGNMENT-VENTURES.md` ← Loop execution

**Reference as:** `[[VENTURE-MASTER]]` (ORB 1)

---

### 🔴 ORB 2: The office (PROCESS/WORKFLOW)
- **Type:** Agent orchestration + execution workflows
- **Location:** `/The office/.claude/get-shit-done/`
- **Files:** 2,400 | Connections: 103
- **Canonical Workflows:**
  - `workflows/plan-phase.md` ← Planning
  - `workflows/execute-phase.md` ← Execution
  - `workflows/verify-work.md` ← Verification

**Reference as:** `[[PLAN-WORKFLOW]]`, `[[EXECUTE-WORKFLOW]]`, `[[VERIFY-WORKFLOW]]` (ORB 2)

---

### 🟡 ORB 3: edu-013-automated-empire-book (VALIDATION)
- **Type:** Content atomization + loop proof-of-concept
- **Location:** `/edu-013-automated-empire-book/`
- **Files:** 17 | Connections: 19
- **Canonical Files:**
  - `LOOPS.md` ← Venture loop execution
  - `infrastructure/SUPABASE-SCHEMA-BOOKS.sql` ← Schema

**Reference as:** `[[CONTENT-TESTBED]]` (ORB 3)

---

## UNIFIED REFERENCE NAMES (Use Across All 3 ORBs)

| Hub Name | Actual File | ORB | Reference |
|----------|------------|-----|-----------|
| Venture Master | VENTURE-HANDLE-MAP.json | 1 | `[[VENTURE-MASTER]]` |
| Repo Master | MASTER-REPO-REGISTRY.csv | 1 | `[[REPO-MASTER]]` |
| Loop Framework | LOOPS-SKILLS-ALIGNMENT-VENTURES.md | 1 | `[[LOOP-FRAMEWORK]]` |
| Master Memory | MEMORY.md | 1 | `[[MASTER-MEMORY]]` |
| Data Sources | DATA-SOURCES.md | 1 | `[[DATA-SOURCES]]` |
| Plan Workflow | plan-phase.md | 2 | `[[PLAN-WORKFLOW]]` |
| Execute Workflow | execute-phase.md | 2 | `[[EXECUTE-WORKFLOW]]` |
| Verify Workflow | verify-work.md | 2 | `[[VERIFY-WORKFLOW]]` |
| Content Testbed | LOOPS.md | 3 | `[[CONTENT-TESTBED]]` |

---

## EXECUTION FLOW: ORBs Connected

```
VENTURE DEFINED (ORB 1)
    ↓ [[VENTURE-MASTER]]
VENTURE CONFIG LOADED
    ↓ [[LOOP-FRAMEWORK]]
LOOP STAGES MAPPED
    ↓ [[PLAN-WORKFLOW]]
┌─────────────────────────────────────┐
│ ORB 2: THE OFFICE                   │
│ Plan Phase → Execution → Verification│
└─────────────────────────────────────┘
    ↓ [[CONTENT-TESTBED]]
PROOF OF CONCEPT (ORB 3)
    ↓ [[EXECUTE-WORKFLOW]]
Loop Executed
    ↓ Feedback
LOOP DATA → ORB 1 (update memory)
```

---

## HOW TO REFERENCE (Standard Pattern)

### In ORB 1 (Venture files):
```yaml
---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[PLAN-WORKFLOW]]
---

As documented in [[LOOP-FRAMEWORK]], this venture executes via [[PLAN-WORKFLOW]].
```

### In ORB 2 (Workflow files):
```yaml
---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[CONTENT-TESTBED]]
---

This workflow executes ventures from [[VENTURE-MASTER]] using [[LOOP-FRAMEWORK]].
Test execution in [[CONTENT-TESTBED]].
```

### In ORB 3 (Testbed/Validation):
```yaml
---
references:
  - [[LOOP-FRAMEWORK]]
  - [[EXECUTE-WORKFLOW]]
  - [[MASTER-MEMORY]]
---

This proof-of-concept demonstrates [[LOOP-FRAMEWORK]] execution via [[EXECUTE-WORKFLOW]].
```

---

## STATUS: ORBS CONNECTED ✅

**Integration Points:**
- ✅ ORB 1 ↔ ORB 2: Ventures execute via workflows
- ✅ ORB 2 ↔ ORB 3: Workflows validated in testbed  
- ✅ ORB 3 ↔ ORB 1: Feedback updates venture config

**Now use these standardized reference names in all new files.**

See: `/Users/acebless/.claude/CLAUDE.md` (updated with unified reference guide)
