# B3A: PolicyEngine API Reference

Reference guide for enforcing permission boundaries.

## 1. Initialization
```python
from policy_engine import PolicyEngine
engine = PolicyEngine(config_path="permissions.json")
```

## 2. Check Execution
```python
# Returns Boolean
allowed = engine.pre_flight_check("venture_classifier", "ClickUp", {"action": "create_task"})
```

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** `policy_engine.py` script written, `permissions.json` config created, and Supabase tables `policy_decisions`, `agent_call_log`, `agent_cost_log` deployed.
    *   **Dependencies:** Blocks B2 (Venture Classifier Agent) and B3A (Venture Factory).
*   **Verification Gate:**
    *   **Success Criteria:** Running local policy checks for rate limit, spending limits, and tool permissions returns expected boolean results and logs decisions correctly.
    *   **Blockers:** Security boundaries cannot be verified; agents could exceed budget or rate limit bounds unchecked.
