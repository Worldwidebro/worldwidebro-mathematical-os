# C3: Agent Execution Dashboard

Visualizes token consumption, latency, and cost of agent runs in Grafana.

## 1. Panels
*   Total queries
*   Hallucination rate (%)
*   Spend per Venture ($)

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** Phase C1 (Grafana Dashboards Setup) completed; Supabase `agent_call_log` and `policy_decisions` populated with audit logs.
    *   **Dependencies:** Blocks CEO Command Center dashboard visibility.
*   **Verification Gate:**
    *   **Success Criteria:** Dashboard displays execution count and success rate graphs over 24h/7d windows.
    *   **Blockers:** Operational security monitoring is blind; compromised or looping agents won't trigger alerts, risking runaway API token costs.
