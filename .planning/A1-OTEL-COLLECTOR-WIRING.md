# A1: Otel-Collector to Prometheus Wiring Guide

This guide details the steps to wire the OpenTelemetry Collector to your Prometheus server for routing metrics.

## 1. Prometheus Configuration (`prometheus.yml`)
Add the otel-collector job to scrape metrics:

```yaml
scrape_configs:
  - job_name: 'otel-collector'
    static_configs:
      - targets: ['localhost:8889', 'localhost:8888']
```

## 2. Otel Collector Configuration
Configure the Prometheus exporter in your collector config:

```yaml
exporters:
  prometheus:
    endpoint: "0.0.0.0:8889"
    namespace: "iza_os"
```

## 3. Verification
Verify metrics are flowing by checking the Prometheus graph UI at `http://localhost:9090` and searching for `otel_collector_` or `iza_os_` prefixes.

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** Prometheus and Otel-Collector services configured and running in Docker (established in Phase 1).
    *   **Dependencies:** Blocks Phase C1 (Grafana Dashboards) and Phase C3 (Agent Execution Dashboard).
*   **Verification Gate:**
    *   **Success Criteria:** Running `curl -s http://localhost:9090/api/v1/targets` returns the `otel-collector` job with status `UP`.
    *   **Blockers:** Agent and application metrics will not route to Prometheus, resulting in empty dashboards.
