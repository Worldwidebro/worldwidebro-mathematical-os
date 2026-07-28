# Performance Optimization

This document outlines the optimization loops for latency, API costs, and resource utilization.

---

## 1. Token Cost Controls (LiteLLM Routing)

All model calls are intercepted by the **OmniRoute Gateway** and optimized based on task complexity:

- **Routine tasks (Level 1)**: Routed automatically to cheap/fast models (`auto/fast` or `auto/cheap` like GPT-4o-mini / DeepSeek Chat).
- **Code Generation & Reasoning**: Routed to smart models (`auto/smart` or `auto/coding` like Claude 3.5 Sonnet).
- **Offline / Local Fallbacks**: Routed to self-hosted Ollama instances to eliminate external API expenses.

---

## 2. Execution Latency Auditing

- **Telemetry**: Prometheus scrape targets monitor latency per agent execution.
- **Trace logs**: Langfuse logs call-by-call latency and token costs.
- **Optimization Sweep**: Weekly routines identify slow nodes in the Neo4j graph and rebalance tasks to sibling agents.
