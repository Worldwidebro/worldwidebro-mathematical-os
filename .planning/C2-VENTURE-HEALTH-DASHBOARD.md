# C2: Venture Health Dashboard Setup

Maps venture readiness scorecard statistics to Grafana dashboards.

## 1. Metrics tracked
*   Runway (days)
*   GitHub commit activity
*   ClickUp task completion rates

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** Phase C1 (Grafana Dashboards Setup) completed; `VENTURE-READINESS-SCORECARD.csv` statistics synchronizing to the database.
    *   **Dependencies:** Blocks CEO Command Center visualization and high-level health tracking.
*   **Verification Gate:**
    *   **Success Criteria:** Grafana displays active gauges for venture readiness, runways, and risk scores matching the CSV/database data.
    *   **Blockers:** Leadership cannot see aggregated readiness or risk metrics across the 712 ventures, leading to lack of operational control.
