# Model Usage and Execution Policies

This document outlines the governance policies and operational rules dictating how large language models (LLMs) are selected, configured, and consumed across the **AI-BOSS-OS** infrastructure.

## 1. Local-First Preference Policy

To minimize operational costs, ensure off-grid resilience, and protect sensitive business metrics, the AI-BOSS-OS mandates a **Local-First** model execution model:

- **Local Execution Target**: Any task classified as `LOW` risk that does not require deep cross-domain logical synthesis must be routed to local instances (e.g., Qwen2.5-Coder or Llama-3 running on Ollama port `11434` or Colibri).
- **Cloud Promotion**: Promotes tasks to cloud models (e.g., Claude 3.5 Sonnet, GPT-4o) only under the following conditions:
  1. The local model fails static syntactic validation or returns an execution error.
  2. The task is explicitly classified as `HIGH` importance by the Decision Engine.
  3. The prompt context size exceeds the local NPU memory boundaries (`> 32k` tokens).

---

## 2. Context Window and Token Budget Management

To manage costs and prevent context exhaustion, agents must adhere to the following token management boundaries:

```text
                  +--------------------------------+
                  |  Total Model Context Window    |
                  +--------------------------------+
                  |  [System Boilerplate]     (10%)|
                  |  [Retrieved RAG Context]  (50%)|
                  |  [Short-Term Conversation](30%)|
                  |  [Buffer/Generation Space](10%)|
                  +--------------------------------+
```

- **Compression Rules**: All inputs routed through OmniRoute are subjected to prompt filters (such as rtk proxy filters), removing duplicate lines, redundant system descriptions, and blank characters.
- **RAG Truncation**: Retrieval-augmented generation steps must restrict output segments to the top 5 most relevant chunks (maximum 8,000 tokens total) to conserve context.

---

## 3. Reliability and Timeout Parameters

To maintain system throughput, every model connection must specify operational timeouts:

- **Commercial Cloud Models**: Connection timeout must be capped at **15 seconds**; read/generation timeout is capped at **45 seconds**.
- **Local Models**: Connection timeout must be capped at **5 seconds**; read/generation timeout is capped at **90 seconds** (accounting for local CPU/GPU/NPU scheduling delays).
- **Retry Mechanism**: OmniRoute executes up to **3 retries** upon receiving standard HTTP connection failures before failing over to the alternative model listed in the routing table.
