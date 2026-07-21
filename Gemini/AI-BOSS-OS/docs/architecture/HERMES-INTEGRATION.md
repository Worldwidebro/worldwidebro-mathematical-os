# Hermes Agent Integration Architecture

This document describes the integration architecture of **Hermes** as the agent runtime within the **AI-BOSS-OS** ecosystem.

## 1. Role in Stack

Hermes functions as the **Agent Execution Engine** at the top layer of the AI-BOSS-OS:
- **State Management**: Orchestrates prompt lifecycle, local memory buffers, and session histories.
- **Tool Execution**: Directly executes code-intelligence scanners, database queries, and filesystem utilities.
- **Protocol Mediation**: Resolves capabilities to tool calls using standard Model Context Protocol (MCP).

---

## 2. Hermes → OmniRoute API Bridge

To leverage dynamic routing, cost reduction, and resilience, Hermes does not call upstream APIs (like Anthropic or OpenAI) directly. Instead, it directs all intelligence queries to the central **OmniRoute** load balancer on port `20128`.

```text
+-------------------+
|   Hermes Agent    |
+---------+---------+
          |
          |  OpenAI-Compatible Payload (JSON)
          v
+---------+---------+
|     OmniRoute     |  <-- Decides best LLM routing target
+---------+---------+
          |
          +-----------------+-----------------+
          |                 |                 |
          v                 v                 v
    +-----+-----+     +-----+-----+     +-----+-----+
    | Cloud APIs|     |  Ollama   |     |  Google   |
    | (Direct)  |     |(Port 11434)     |   API     |
    +-----------+     +-----------+     +-----------+
```

### Hermes Configuration
All Hermes nodes in the AI-BOSS-OS are provisioned with the following provider configuration (`hermes.yaml`):

```yaml
provider: openai-compatible
base_url: http://localhost:20128/v1
api_key: OMNIROUTE_KEY
model: auto
```

When Hermes submits a message, the request uses `model: auto` or a role-based router key (like `auto/coding`), and OmniRoute translates it to the most optimal model execution backend.

---

## 3. Operational Capabilities

### 3.1 Model Providers
Hermes is capable of communicating with any provider mapped under OmniRoute:
- **Commercial Cloud**: Anthropic (Sonnet 3.5), OpenAI (GPT-4o), Google (Gemini 1.5 Pro).
- **Local Runtimes**: Ollama, vLLM, and Colibri running private weights (Qwen2.5-Coder, DeepSeek-Coder).

### 3.2 Tool Integration & MCP
Hermes maps tools to LLMs by parsing capabilities from the centralized knowledge graph. It hosts local MCP servers to connect:
- **Filesystem**: Standard file workspace operations.
- **GitHub**: Repository state audits, pull requests, and commit logs.
- **Knowledge Bases**: Local Neo4j Knowledge Graph mappings.

### 3.3 Memory & Context Management
Hermes maintains a dual-layer memory layout:
1. **Short-Term Context**: Local session cache synced with PostgreSQL `iza_os_core`.
2. **Long-Term Vector Memory**: Local Qdrant collections mapped via RAG.

### 3.4 Agent-to-Agent (A2A) Messaging
Agents communicate using message-passing channels. Hermes serializes these interactions into local databases to ensure chronological tracking and audit logs.

### 3.5 Security & Sandbox Policies
All execution tools run within standard sandboxed environments. System-modifying commands require explicit control plane approval, preventing arbitrary code executions.
