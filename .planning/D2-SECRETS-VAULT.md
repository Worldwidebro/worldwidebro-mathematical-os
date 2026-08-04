# D2: HashiCorp Secrets Vault Setup

Secrets vault integration and key rotation workflows.

## 1. CLI Commands
Use `vault kv put secret/key` to store private tokens.

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** HashiCorp Vault service running (established in Phase 1); credentials from `.env` prepared for migration.
    *   **Dependencies:** Blocks secure production deployment pipelines and team accesses.
*   **Verification Gate:**
    *   **Success Criteria:** Querying secrets via Python client returns valid API keys without keeping plaintext keys in git or local `.env` files.
    *   **Blockers:** Exposure of credentials in plaintext on disk/git repositories violating compliance rules.
