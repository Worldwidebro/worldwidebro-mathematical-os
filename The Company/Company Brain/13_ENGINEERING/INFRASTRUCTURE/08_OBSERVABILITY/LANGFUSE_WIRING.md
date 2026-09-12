---
id: INFRA-OBS-002
title: Langfuse & OpenTelemetry Live Telemetry Wiring
aliases: ["LANGFUSE_WIRING", "Langfuse Wiring", "CAP-OBSERVABILITY"]
tags: [observability, langfuse, opentelemetry, litellm, omniroute, tracing]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[REALITY]] | [[13_ENGINEERING/INFRASTRUCTURE/08_OBSERVABILITY/OBSERVABILITY|OBSERVABILITY]] | [[LOCAL_MODEL_AGENT_STACK_REGISTRY]] | [[INDEX]]

# Langfuse & OpenTelemetry Telemetry Wiring

**Authority:** CP-027 (System Architecture & Infrastructure)  
**Status:** ✅ `OPERATIONAL & WIRED`  
**Gap Resolution:** Resolves `CAP-OBSERVABILITY` utilizing starred repository [`langfuse/langfuse`](https://github.com/langfuse/langfuse) (34,058 ★).

---

## 1. Live Runtime Architecture
- **Active Container:** `civos_langfuse` running `ghcr.io/langfuse/langfuse:2` on Mac Studio (`100.87.214.70:3003`).
- **Gateway Intercepts:**
  - **LiteLLM Gateway:** `civos_litellm` (`http://localhost:4000`).
  - **OmniRoute Gateway:** `omniroute` (`http://localhost:20128`).
- **Telemetry Ingestion:** OpenTelemetry Collector daemon listening on ports `:4317` (gRPC) and `:4318` (HTTP).

---

## 2. Gateway Callback Configuration

### A. LiteLLM Gateway Configuration (`litellm-config.yaml`)
To stream 100% of LLM completions, token counts, model latencies, and error states directly into Langfuse, ensure the following callback block is active in `/Volumes/T7 Shield/litellm-config.yaml`:

```yaml
litellm_settings:
  success_callback: ["langfuse", "otel"]
  failure_callback: ["langfuse", "otel"]

environment_variables:
  LANGFUSE_HOST: "http://civos_langfuse:3000"
  LANGFUSE_PUBLIC_KEY: "pk-lf-company-brain-master"
  LANGFUSE_SECRET_KEY: "sk-lf-company-brain-master"
  OTEL_EXPORTER_OTLP_ENDPOINT: "http://t7shield-otel-collector-1:4318"
```

### B. Python Agent Runtime Interceptor
For standalone agents (such as Hermes Agent or custom LangGraph pipelines), invoke the native Langfuse callback handler:

```python
from langfuse import Langfuse
from langfuse.openai import openai

langfuse = Langfuse(
    public_key="pk-lf-company-brain-master",
    secret_key="sk-lf-company-brain-master",
    host="http://100.87.214.70:3003"
)

# Automatic tracing wrapper around OpenAI / LiteLLM client
response = openai.chat.completions.create(
    model="auto/coding",
    messages=[{"role": "user", "content": "Execute venture gap audit"}],
    name="company-brain-gap-audit",
    metadata={"venture_id": "CON-001", "agent": "OpenHands"}
)
```

---

## 3. Observability Dashboard Verification
1. Open the live dashboard: `http://100.87.214.70:3003` (or via Tailscale mesh).
2. Inspect real-time traces:
   - **Generation Latency:** P50/P95 response times across native MLX `exo` (`:52415`) vs. cloud fallbacks.
   - **Cost Ledger:** Exact dollar accumulation measured by `tiktoken` BPE counter.
   - **Error Budget:** Instant alerts for rate limits or model timeouts.
