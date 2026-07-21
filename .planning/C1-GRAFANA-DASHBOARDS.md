# C1: Grafana Dashboard Templates Setup

Details setup of Grafana dashboards and provisioning files.

## 1. Setup
Place dashboards under `/etc/grafana/provisioning/dashboards/`.

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** Grafana container running on port 3000 (established in Phase 1); Prometheus scraping Otel-Collector (Phase A1).
    *   **Dependencies:** Blocks Phase C2 (Venture Health Dashboard) and Phase C3 (Agent Execution Dashboard).
*   **Verification Gate:**
    *   **Success Criteria:** Dashboard JSON files successfully imported via Grafana REST API or dashboard provisioning, returning `200 OK` responses.
    *   **Blockers:** Dashboards must be configured manually from scratch on every stack rebuild or system recovery.
