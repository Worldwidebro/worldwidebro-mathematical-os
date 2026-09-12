[[STARTHERE]] | [[20-DECISIONS/README|Decisions Index]] | [[REALITY]]

# Wiki Link Gaps Analysis — Venture ↔ ClickUp ↔ Sector ↔ Control Plane

**Analysis Date:** Sep 9, 2026  
**Status:** 🔴 **CRITICAL GAPS IDENTIFIED**

---

## Summary: 25+ Wiki Link Gaps Found

| What's Missing | Count | Impact | Effort |
|---|---|---|---|
| Venture index pages | 5 | **HIGH** | 2.5h |
| Control plane → venture links | 5 | **HIGH** | 1.5h |
| Sector → venture links | 4 | **HIGH** | 1h |
| ClickUp documentation pages | 6 | Medium | 2h |
| **TOTAL** | **20** | — | **~7h** |

---

## 🔴 CRITICAL GAP #1: No Venture Index Pages

**Missing:** [[OPS-001]], [[CON-001]], [[LT-005]], [[LT-011]], [[RE-001]]

Each venture exists only as:
- ✅ Scripts (`/scripts/OPS-001-SALES-COACH.md`)
- ✅ Pipelines (`/decisions/OPS-001-SALES-PIPELINE.md`)
- ❌ **No central venture page** (no [[OPS-001]] link)

**Impact:** Someone at [[SEC-014-Staffing]] has no way to find [[OPS-001]].

---

## 🔴 CRITICAL GAP #2: Control Plane ↔ Venture Links Missing

**Missing Connections:**
```
[[CP-023-Sales]] → should link to: OPS-001, CON-001, LT-005, LT-011, RE-001
[[CP-026-Operations]] → should link to: CON-001, LT-005, LT-011
[[CP-020-Finance]] → should link to: LT-005, RE-001
[[CP-025-People]] → should link to: OPS-001
[[CP-001-Enterprise]] → should link to: RE-001
```

**Impact:** Can't navigate from "Sales (CP-023)" to "What ventures are we selling?"

---

## 🔴 CRITICAL GAP #3: Sector ↔ Venture Links Missing

**Missing Connections:**
```
[[SEC-014-Staffing]] → OPS-001 (missing)
[[SEC-002-Construction]] → CON-001 (missing)
[[SEC-017-Logistics]] → LT-005, LT-011 (missing)
[[SEC-020-RealEstate]] → RE-001 (missing)
```

**Impact:** Sector pages are dead-ends; can't drill down to ventures.

---

## 🔴 CRITICAL GAP #4: ClickUp Not in Wiki

**Missing Pages:**
```
[[ClickUp-Workspace-9013677375]] (Antwuan Johns — 59 folders)
[[ClickUp-Workspace-90141555791]] (Medical Courier — 33 folders)
[[ClickUp-Folder-Staffing-Operations]]
[[ClickUp-Folder-Construction]]
[[ClickUp-Folder-Logistics-Transport]]
[[ClickUp-Folder-Real-Estate]]
```

**Impact:** ClickUp is a separate system; no wiki links guide users to tasks.

---

## ✅ What's Working

- ✅ ClickUp folder mapping (correct)
- ✅ Sector taxonomy (complete)
- ✅ Control plane assignments (correct)
- ✅ CSV converter (ready)

**The gap is ONLY in wiki documentation.**

---

## 🎯 Navigation Examples (Why This Matters)

**User asking: "Where are my sales calls?"**

Current (with gaps):
```
User: Open [[CP-023-Sales]]
Result: No venture links
User: Manually type ClickUp folder ID in browser
```

Desired (after closing gaps):
```
User: Open [[CP-023-Sales]]
Result: See [[OPS-001]], [[CON-001]], [[LT-005]], [[LT-011]], [[RE-001]]
User: Click [[OPS-001]]
Result: See [[ClickUp-Folder-Staffing-Operations]] link
User: Click ClickUp link
Result: 48 cold call tasks (ready to execute)
```

---

## Complete Correlation Map (Use for Index Pages)

| Venture | Sector | Control Planes | ClickUp Workspace | ClickUp Folder |
|---------|--------|---|---|---|
| **OPS-001** | SEC-014 | CP-023, CP-025, CP-026 | Antwuan Johns (9013677375) | Staffing Ops (1000210000000685) |
| **CON-001** | SEC-002 | CP-026, CP-012, CP-023 | Antwuan Johns (9013677375) | Construction (901318114591) |
| **LT-005** | SEC-017 | CP-023, CP-026, CP-020 | Medical Courier (90141555791) | Lead Gen (901411978075) |
| **LT-011** | SEC-017 | CP-026, CP-023 | Antwuan Johns (9013677375) | Logistics (901317788910) |
| **RE-001** | SEC-020 | CP-001, CP-020, CP-023 | Antwuan Johns (9013677375) | Real Estate (901318114592) |

---

## Priority Order (Next 7 Days)

1. **Sep 11-14:** Execute cold calls (don't wait for wiki)
2. **Sep 15:** Create 5 venture index pages (2.5h)
3. **Sep 16:** Update 5 control plane pages (1.5h)
4. **Sep 17:** Update 4 sector pages (1h)
5. **Sep 18:** Create 6 ClickUp documentation pages (2h)

**Total time to close all gaps: ~7 hours**

---

## When You're Ready: Template for [[OPS-001]]

```markdown
# [[OPS-001]] — CareerOps Staffing

**Sector:** [[SEC-014-Staffing]]
**Control Planes:** [[CP-023-Sales]], [[CP-025-People]], [[CP-026-Operations]]
**ClickUp:** [[ClickUp-Folder-Staffing-Operations]] (Folder 1000210000000685)

## Operations
- Scripts: [[OPS-001-SALES-COACH.md]]
- Pipeline: [[OPS-001-SALES-PIPELINE.md]]
- Call List: 48 prospects (calls/OPS-001-FINAL-CALL-LIST.csv)

## Links
- Vercel: https://ops-staff-001-staffing.vercel.app
- Repo: https://github.com/worldwidebro/ops-001-staffing
- ClickUp List: "Sep 11-14 Cold Calls (OPS-001)"
```

---

**Status:** Gaps documented | System operational | Wiki pending | Execute Sep 11

