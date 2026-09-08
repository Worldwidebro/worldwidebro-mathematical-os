---
name: observability
description: Monitors metrics, logs, traces, and model routing telemetry across Grafana and Langfuse. Use when debugging performance bottlenecks, inspecting LiteLLM routing errors, checking agent traces, or verifying service health.
---


[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# Observability Skill

This skill operationalizes Rule 18 of `ANTIGRAVITY.md` and connects to the observability endpoints documented in `CLAUDE.md`.

## Observability Topology

- **Grafana Dashboard**: `http://100.87.214.70:3011` (Container: `t7shield-grafana-1`)
- **Langfuse Tracing**: `http://100.87.214.70:3003` (Container: `civos_langfuse`)
- **LiteLLM Metrics**: `http://100.87.214.70:4000`
- **OmniRoute Dashboard**: `http://100.87.214.70:20128/dashboard`

## Diagnostic Protocol

When diagnosing failures or latency:
1. Inspect container logs: `docker --context macstudio logs --tail 100 <container-name>`
2. Check LLM routing and token usage in Langfuse.
3. Validate API response times and cache hit ratios in Redis.
