[[STARTHERE]] | [[AGENTS.md]] | [[ANTIGRAVITY.md]]

# Workflow: Deploy (`/deploy`)

**Objective:** Safely deploy services, databases, or configuration updates to Mac Studio or cloud endpoints.

## Steps

1. **Pre-Deployment Check**:
   - Verify all tests pass on clean working tree.
   - Confirm target host connectivity: `ssh macstudio` or Tailscale ping `100.87.214.70`.
2. **Execute Deployment**:
   - Execute deployment via `_CLI/bin/cb infrastructure deploy --phase <N>`.
3. **Observability & Smoke Tests**:
   - Query `/health` or status endpoints.
   - Verify logs in Grafana (`:3011`) and traces in Langfuse (`:3003`).
4. **Document Outcome**:
   - Record deployed version, commit hash, and status in deployment logs.
