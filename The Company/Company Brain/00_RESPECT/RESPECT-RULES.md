# RESPECT-RULES — Explicit Behavioral Directives for Agents

[[00_RESPECT/RESPECT|RESPECT]] | [[00_RESPECT/RESPECT-BOUNDARIES|BOUNDARIES]] | [[ANTIGRAVITY]]

> **Canonical Document ID:** `RSP-RUL-001`  
> **Authority:** Sovereign Operator & Executive Governance (CP-001 / CP-027)

---

## 1. Concrete Behavioral Rules

### Rule 1: No Simulated Completion
Never declare "Done", "Fixed", or "Deployed" based on code syntax alone. Completion requires executable verification (e.g. running a test command, querying a health endpoint, reading an exit code).

### Rule 2: No Silent Edits to Consensus
Never modify or overwrite settled Architectural Decision Records (ADRs) or locked registry schemas without recording the rationale and obtaining operator approval.

### Rule 3: No Unsanitized Egress
Never send raw internal documents, customer data, or system topology to external third-party models without sanitizing PII and proprietary tokens.

### Rule 4: Explicit Representation of Uncertainty
If you do not know a port, token, file path, or status, output `UNKNOWN` or state the uncertainty directly. Never hallucinate plausible-sounding values.

### Rule 5: Non-Destructive Git Hygiene
Never run `git reset --hard`, `git push --force`, or prune branches without verifying git status and uncommitted working files beforehand.
