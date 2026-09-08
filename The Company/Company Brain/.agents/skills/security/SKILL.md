---
name: security
description: Audits code, dependencies, environment configs, and registries for vulnerabilities, secrets leakage, and compliance risks. Use when reviewing code security, auditing npm/pip dependencies, or validating external integrations.
---


[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# Security & Compliance Skill

This skill operationalizes Rule 16 and Rule 26 of `ANTIGRAVITY.md`.

## Procedures

1. **Secret Scanning**:
   - Verify that `.env` files and credentials are in `.gitignore`.
   - Scan working directory diffs for accidental tokens (`gho_`, `sk-`, `ey...`, passwords).

2. **Dependency Supply Chain Audit**:
   - Python: `pip-audit` or `safety check`
   - Node: `npm audit`
   - Rust: `cargo audit`

3. **High-Risk Previews**:
   - For sensitive operations (database migrations, credential rotation, infrastructure destruction), generate a preview artifact (`SECURITY_PREVIEW.md`) and request explicit human approval before executing.
