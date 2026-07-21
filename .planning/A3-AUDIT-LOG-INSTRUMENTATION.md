# A3: Audit Log Instrumentation

Enforces security traceability by tracking all agent action execution steps.

## 1. Instrumentation Pattern
Every agent call must publish a pre-dispatch and post-execution record:

```python
from policy_engine import PolicyEngine

policy = PolicyEngine()
# Log pre-flight check
allowed = policy.pre_flight_check(agent_name, tool_name, args)
if not allowed:
    raise PermissionError("Action blocked by governance policies.")
```

## 2. Table Schema
Ensure the `policy_decisions` table in Supabase logs the following payload:
*   `agent_name`
*   `tool_name`
*   `args_hash`
*   `decision` (allow/deny)
*   `timestamp`

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** Supabase database tables (`policy_decisions`, `agent_call_log`, `agent_cost_log`) must be created first (via SQL in `OS-BUILD-GUIDE-SPRINT-1.md`).
    *   **Dependencies:** Blocks B2 (Venture Classifier Agent) and B3A (Venture Factory) which require automated audit logging.
*   **Verification Gate:**
    *   **Success Criteria:** Running a mockup agent action successfully inserts a row into the `policy_decisions` table with correct schema fields.
    *   **Blockers:** Agent execution fails with database syntax errors when executing `PolicyEngine.audit()`.
