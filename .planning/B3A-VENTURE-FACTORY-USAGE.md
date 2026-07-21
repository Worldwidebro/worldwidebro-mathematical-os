# B3A: VentureFactory API Reference

Provisioning factory for individual ventures.

## 1. Methods

### `factory.create(name, sector, opco)`
Provisions GitHub repo, Supabase schema, ClickUp workspace, and Grafana dashboard.

## 2. Code Example
```python
from venture_factory import VentureFactory

factory = VentureFactory()
factory.create("Acme Build", "CON", "CON-001")
```

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** `venture_factory.py` script created; API tokens for GitHub, ClickUp, and Grafana set in `.env`; `policy_engine.py` is functional.
    *   **Dependencies:** Blocks B3B (Dependency Mapping) and C2 (Venture Health Dashboard).
*   **Verification Gate:**
    *   **Success Criteria:** Invoking `factory.create()` successfully provisions a new GitHub repository, inserts the matching Supabase schema, creates a ClickUp space, and deploys a Grafana dashboard.
    *   **Blockers:** Inability to provision new ventures dynamically, blocking scalable multi-venture OS expansion.
