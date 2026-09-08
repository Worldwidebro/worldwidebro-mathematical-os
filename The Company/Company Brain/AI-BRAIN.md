---
id: PORTAL-AI-BRAIN-ALIAS-001
aliases: ["AI-BRAIN", "AI Brain", "Intelligence Core", "Cognitive Engine"]
tags: ["ai", "agents", "models", "knowledge-graph", "memory", "omniroute"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[CLAUDE]] | [[16-AGENTS]] | [[17-MODELS]] | [[08-KNOWLEDGE-GRAPH]] | [[10-MEMORY]]

# AI-BRAIN — Company Brain Artificial Intelligence Core Portal

> **Authority:** Model Control Plane (CP-007) & Agent Control Plane (CP-006)  
> **Purpose:** Master gateway for autonomous intelligence, neural routing, knowledge persistence, and continuous multi-agent execution.

---

## 1. AI Subsystem Architecture

```mermaid
graph TD
    Client["Inference Request / Task"] --> Router["OmniRoute (:20128) & LiteLLM (:4000)"]
    Router --> LocalEngine["Mac Studio M4 Max exo (:52415)<br/>mlx-community/Qwen3.6-35B-A3B-5bit"]
    Router --> OllamaEngine["Mac Studio Ollama (:11434)<br/>qwen2.5-coder:14b / nomic-embed-text"]
    Router --> CloudFailover["Cloud Backup<br/>Claude Sonnet / Haiku / OpenAI"]
    LocalEngine --> Knowledge["Knowledge Core<br/>Neo4j (:7687) & Qdrant (:6333)"]
    Knowledge --> Memory["Agent Memory Substrate<br/>[[10-MEMORY]] & [[_MEMORY]]"]
    Memory --> Agents["Autonomous Agent Fleet<br/>[[16-AGENTS]] & FastMCP Tools"]
```

---

## 2. Core AI Subsystems

### Inference & Model Routing
- [[17-MODELS/17-MODELS|17-MODELS]]: Unified model catalog and runtime profiles.
- [LLM Hardware Compatibility Registry](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml): Measured benchmarks and 4-tier model fallback rules.
- [[_INFRASTRUCTURE/omniroute/README|OmniRoute Gateway]]: Multi-provider traffic routing, token budget guards, and Tailscale mesh gateway.

### Knowledge, Graph & Vectors
- [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH]]: Neo4j graph database hosting 3,308 Repos, 722 Ventures, and 20,363 edges (`bolt://100.87.214.70:7687`).
- [[11-INDEXING/11-INDEXING|11-INDEXING]]: Qdrant vector database (`:6333`) providing semantic embeddings via `nomic-embed-text`.
- `graphify-out/`: AST-level deterministic code and documentation knowledge graph.

### Agents & Tools
- [[16-AGENTS/16-AGENTS|16-AGENTS]]: Autonomous routing agents (`AGT-001` through `AGT-005`, plus specialized subagents).
- [[.agents/agents/engineering-database-optimizer|Database Optimizer Agent]]: Query plan and schema tuning specialist.
- [Company Brain FastMCP Server](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_MCP/fastmcp_server.py): 9 native infrastructure and control plane tools.

### Memory & Learning
- [[10-MEMORY/10-MEMORY|10-MEMORY]]: Layer 10 cognitive memory substrate.
- [[_MEMORY/MEMORY-POLICY|MEMORY-POLICY]]: Epistemic retention and token compaction governance.
- [[44-LEARNING/44-LEARNING|44-LEARNING]]: Continuous evaluation and learning loops.
