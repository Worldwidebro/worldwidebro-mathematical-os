# KILL-CRITERIA — Terminal Campaign Termination Conditions

> **Canonical Document ID:** `DOC-KIL-CAM-001`  
> **Authority:** Executive Governance (CP-001)  
> **Status:** MANDATORY TERMINATION SPECIFICATION  
> **Canonical Aliases:** [[CAMPAIGNS/PIVOT-CRITERIA.md]], [[CAMPAIGNS/SCALE-CRITERIA.md]]

---

## 1. The 4 Operational Decision Gates

```text
EVALUATION TELEMETRY ──> SHOULD WE: CONTINUE? OPTIMIZE? SCALE? PIVOT? KILL?
```

### Gate 1: SCALE CRITERIA
- **Condition:** 3 paid audits closed within first 15 discovery calls (\(\ge 20\%\) close rate) with CAC < $400.
- **Action:** Increase outbound send volume by 100% and commission 2 additional delivery engineers.

### Gate 2: PIVOT CRITERIA
- **Condition:** High reply rate (>10%) but >60% of prospects drop off due to code privacy fears.
- **Action:** Pivot offer packaging from managed audit to self-hosted enterprise scanner license ($5,000).

### Gate 3: PAUSE CRITERIA
- **Condition:** Delivery team reaches maximum concurrent capacity (3 audits in-flight simultaneously).
- **Action:** Temporarily pause outbound sending for 7 business days until deliverables are handed off.

### Gate 4: KILL CRITERIA (Terminal Termination)
- **Condition:** 300 targeted accounts reached \(\to\) at least 10 discovery calls held \(\to\) **0 contracts signed**, with consensus objection that token costs are not a top-3 priority.
- **Action:** Terminate `CAM-001` permanently. Conduct blameless post-mortem. Reallocate remaining budget.

---

## 2. Master Links

- Stop Rules: [[CAMPAIGNS/STOP-RULES]]
- Post-Mortem: [[CAMPAIGNS/POST-MORTEM]]
