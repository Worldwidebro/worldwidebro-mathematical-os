# RESPECT-BOUNDARIES — Inviolable Limits and Constraints

[[00_RESPECT/RESPECT|RESPECT]] | [[00_RESPECT/RESPECT-RULES|RULES]] | [[STARTHERE]]

> **Canonical Document ID:** `RSP-BND-001`  
> **Authority:** Sovereign Operator & Executive Governance (CP-001 / CP-027)

---

## 1. System Invariants (What Must Never Be Crossed)

1. **The Credential Boundary**: Under no circumstances may plaintext passwords, private keys, or API tokens be committed to Git or stored in vector embeddings. Use Bitwarden CLI (`SEC-BITWARDEN-001`).
2. **The Workspace Boundary**: Tools must never write or mutate files outside authorized workspace mounts without explicit operator permission.
3. **The Financial Boundary**: No financial transaction, payment dispatch, contract signing, or DNS modification may occur autonomously without human authorization.
4. **The Registry Integrity Boundary**: Never overwrite `_REGISTRIES/` files blindly; use atomic, versioned, or append updates.
5. **The Memory Boundary**: Never treat a model's high subjective confidence as a substitute for empirical test verification.
