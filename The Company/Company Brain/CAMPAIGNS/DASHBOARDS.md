# DASHBOARDS — Grafana & Terminal Observability Visualizations

> **Canonical Document ID:** `DOC-DSH-CAM-001`  
> **Authority:** Observability (CP-041)  
> **Status:** ACTIVE SPECIFICATION

---

## 1. Live Dashboards

- **Executive Commercial Dashboard:** Grafana port `:3000` (UID: `camp-001-rev`).
  - Real-time gross cash collected.
  - Discovery calls completed vs target pacing curve.
  - Active pipeline SOWs pending signature.
- **Outbound Telemetry Dashboard:** Terminal CLI dashboard via `python3 -m civos.telemetry.campaign CAM-001`.

---

## 2. Master Links

- Measurement: [[CAMPAIGNS/MEASUREMENT]]
- Observability Core: [[41-OBSERVABILITY]]
