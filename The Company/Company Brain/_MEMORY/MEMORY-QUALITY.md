# MEMORY-QUALITY — Truth States, Validation, and Assurance

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[REALITY]] | [[ANTIGRAVITY]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-QUA-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. Truth State Classification

Every assertion, entity, and memory atom in Company Brain carries one of the seven standardized truth states:

| Truth State | Definition | Operational Rule |
|---|---|---|
| `VERIFIED` | Confirmed by live execution, runtime probe, or physical transaction. | Full confidence ($1.0$). Permitted in automated pipelines. |
| `PROBABLE` | Strong corroborating evidence exists; awaiting final runtime confirmation. | High confidence ($0.8$). Requires sanity check before mutation. |
| `ASSUMED` | Declared as intention, design spec, or proposal; unproven. | Medium confidence ($0.4$). Must be clearly flagged as hypothesis. |
| `UNKNOWN` | Missing empirical data; unmeasured. | Confidence ($0.0$). Prompts an exploratory investigation task. |
| `DISPROVEN` | Empirically refuted by runtime failure or diagnostic probe. | Negative weight. Prevents repeating failed approaches. |
| `STALE` | Previously true, but validity window has elapsed without verification. | Low confidence ($0.2$). Requires immediate live probe. |
| `CONFLICTED` | Competing, contradictory assertions exist across nodes. | Halted state. Prompts operator or architect reconciliation. |

---

## 2. Validation Rules

1. **Rule of Evidence**: Runtime evidence always outranks documentation. Documentation outranks chat inferences.
2. **Never Elevate Without Proof**: Agents are strictly prohibited from silently converting an `ASSUMED` state into `VERIFIED` without executing concrete test proof (`ANTIGRAVITY.md` Rule #3).
3. **No Ghost References**: Links to external entities must include Wikidata QID or Wikipedia URL to ground semantic concepts.
