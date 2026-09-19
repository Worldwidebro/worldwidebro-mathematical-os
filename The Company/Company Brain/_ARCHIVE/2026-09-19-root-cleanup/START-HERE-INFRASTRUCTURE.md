[[STARTHERE]] | [[REALITY]] | [[CLAUDE]] | [[00_RESPECT/RESPECT|RESPECT]] | [[INDEX]] | [[OMNIROUTE-STATUS]] | [[OMNIROUTE-MODELS-ROUTING]] | [[KNOWLEDGE-GRAPH-OMNIROUTE-INTEGRATION]] | [[REPOSITORY-INTELLIGENCE-SYSTEM]]

# START HERE — Infrastructure & Compute Fabric Gateway

> **Canonical Guide ID:** `GUIDE-INF-001`  
> **Domain:** Engineering & Distributed Systems  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
> **Status:** ACTIVE RUNTIME STATE — Updated 2026-09-06

---

## 1. Physical Node Topology & Tailscale Mesh
**See [[DEVICE-STORAGE-TOPOLOGY]] for complete device mapping, storage architecture, and cross-device access patterns**

- **Network Backbone:** [[Tailscale]] Encrypted Mesh (`Worldwidebro@`)
- **Primary Brain Node:** [[Mac Studio]] M4 Max (`100.87.214.70`) — Storage: [[/Volumes/LaCie]] (4TB external USB-C)
- **Mobile Engineering Node:** [[MacBook Air]] M-Series (`100.121.17.63`) — Storage: [[/Volumes/T7 Shield]] (2TB external USB-C)
- **OmniRoute Tunnel Gateway:** `100.80.229.113:20128` (OmniRoute daemon on Mac Studio)

## 2. Active Model Engines & Routing
See [[OMNIROUTE-STATUS]] for complete live system status | [[OMNIROUTE-MODELS-ROUTING]] for model inventory & routing architecture
- **Traffic Controller:** [[OmniRoute]] daemon running locally on port `:20128` (`http://localhost:20128`) and Mac Studio (`http://100.87.214.70:20128`).
- **FastMCP Agent Adapter:** `/Users/acebless/.omniroute/bin/antigravity-mcp.mjs` (exposing 110 tools) — See [[OMNIROUTE-KNOWLEDGE-GRAPH]] for MCP integration.
- **Heavy Model Engine:** Native Apple Silicon MLX via [[exo]] (`http://100.87.214.70:52415/v1`, Qwen3.6-35B — 1 of 120 catalog models).
- **Local Model Engine:** [[Ollama]] Local (`http://localhost:11434`, 6 live models: `qwen2.5-coder:14b`, `llama3.1:8b`, `hermes3:latest`, others).
- **Model Gateway:** [[LiteLLM]] Router (`http://100.87.214.70:4000`) — See routing architecture in [[OMNIROUTE-MODELS-ROUTING]].

## 3. Databases & Secrets
See [[KNOWLEDGE-GRAPH-OMNIROUTE-INTEGRATION]] for complete integration architecture
- **Knowledge Graph:** [[Neo4j]] Community/Enterprise (`bolt://100.87.214.70:7687`, HTTP console `:7474`) — 20,363 edges, 789 ventures tracked. See [[EXTERNAL_CAPABILITY_UNIVERSE.yaml|_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml]] for 904 external starred repos mapped.
- **Vector Search:** [[Qdrant]] Vector Engine (`http://100.87.214.70:6333`) — 17,236 vectors indexed for semantic retrieval.
- **Relational Database:** [[PostgreSQL]] 16 (`localhost:5432` / Mac Studio) — Supabase backend.
- **Zero-Knowledge Secrets:** [[Bitwarden]] CLI (`/opt/homebrew/bin/bw`, `SEC-BITWARDEN-001`).
- **Telemetry Platform:** [[OpenObserve]] (`http://100.87.214.70:5080`) — Observability dashboards &amp; log aggregation.

## 4. Canonical Infrastructure Registries
See [[OMNIROUTE-MODELS-ROUTING]] for model routing architecture using these registries

**Repository Intelligence System:** [[REPOSITORY-INTELLIGENCE-SYSTEM]] (8-phase pipeline for 904 starred repos)
- [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml]] — 904 external starred repos → capabilities → ventures (See [[REPOSITORY-INTELLIGENCE-SYSTEM]])
- [[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml]] — 300+ owned capabilities mapped to models and ventures

**Operational Registries:**
- [[_REGISTRIES/INFRASTRUCTURE_REGISTRY.yaml]] — Authoritative master hardware, node, and daemon registry.
- [[_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml]] — Quantization, context window, and model sizing rules for tier 1/2/3 routing decisions.
- [[_REGISTRIES/network_registry.json]] — Tailscale mesh subnet & DNS mappings.
- [[_REGISTRIES/database_registry.json]] — Port mappings, volumes, and connection URIs.
- [[_REGISTRIES/storage_registry.json]] — LaCie, T7 Shield, and internal disk budgets.
