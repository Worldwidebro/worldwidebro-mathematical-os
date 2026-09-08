# RESPECT-ESCALATION — Knowing When to Halt and Escalate

[[00_RESPECT/RESPECT|RESPECT]] | [[00_RESPECT/RESPECT-AGENCY|AGENCY]] | [[ANTIGRAVITY]]

> **Canonical Document ID:** `RSP-ESC-001`  
> **Authority:** Sovereign Operator & Executive Governance (CP-001 / CP-027)

---

## 1. Mandatory Escalation Triggers

An agent must immediately halt execution and escalate to the Sovereign Operator when:
1. **Ambiguous Intent with Irreversible Consequences**: e.g., Deleting an existing database volume, pushing destructive git changes, or dropping a table.
2. **Authority / Permission Conflicts**: e.g., Encountering an authentication failure where a token or secret is missing.
3. **Safety / Legal Violations**: e.g., Discovery of unredacted credentials or potential licensing violations.
4. **Architectural Contradictions**: e.g., Two authoritative documents give directly opposing directives that cannot be reconciled automatically.
5. **Repeated Unrecoverable Errors**: e.g., A command fails 3 times consecutively with identical stack traces despite parameter adjustments.

---

## 2. Escalation Protocol

When escalating:
1. State the exact conflict or blocker succinctly.
2. Provide the empirical evidence (error code, conflicting file lines).
3. Present 2–3 concrete options with trade-offs.
4. Explicitly request the operator's decision before resuming.
