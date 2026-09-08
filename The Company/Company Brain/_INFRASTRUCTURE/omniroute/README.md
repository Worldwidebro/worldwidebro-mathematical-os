---
id: INFRA-OMNIROUTE-HUB
title: "OmniRoute & LiteLLM Inference Infrastructure Hub"
aliases: ["_INFRASTRUCTURE/omniroute", "OmniRoute Infrastructure"]
tags: [infrastructure, omniroute, litellm, models, inference, routing, redis, neo4j]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[17-MODELS/17-MODELS|17-MODELS]] | [[56-ENGINEERING/README|56-ENGINEERING]] | [[CLAUDE]]

# OmniRoute & LiteLLM Inference Infrastructure Hub

> **Authority:** AI & Agent Control Plane ([[50-MASTER-CONTROL/CONTROL_MATRIX|CP-006]] / [[50-MASTER-CONTROL/CONTROL_MATRIX|CP-007]])  
> **Master Operating Contract:** [[ANTIGRAVITY.md]]  
> **Live Runtime State:** [[CLAUDE.md]]  
> **Status:** 🟢 ACTIVE — Operational Dynamic Inference Router (2026-09-06)

---

## 1. Service Topology & Port Mappings

| Service | Protocol / Port | Host / Mesh Address | Purpose |
|:---|:---|:---|:---|
| **OmniRoute v3.8.50** | HTTP `:20128` / `:3000` | `100.87.214.70:20128` | Multi-model dynamic routing, combo metrics, and cost guardrails |
| **LiteLLM Gateway** | HTTP `:4000` / `:4001` | `100.87.214.70:4000` | Unified OpenAI-compatible proxy across local and frontier models |
| **Exo MLX Cluster** | HTTP `:52415` | `100.87.214.70:52415` | Native Apple Silicon M4 Max MLX distributed model serving |
| **Redis Cache** | TCP `:6381` / `:6379` | `localhost:6381` | Low-latency prompt caching, session state, and deduplication |
| **Neo4j Graph** | Bolt `:7687` / `:7475` | `localhost:7687` | Capability and agent relationship routing graph |

---

## 2. Model Routing Tiers & Fallback Architecture
1. **Tier 1 (Fast Local Zero-Cost):** `exo` MLX `Qwen3.6-35B-A3B-5bit` on Mac Studio (`100.87.214.70`).
2. **Tier 2 (Edge Fallback):** Ollama `qwen2.5-coder:14b` or `llama3.1:8b` on T7 Shield / local storage.
3. **Tier 3 (Frontier Escalation):** Anthropic Claude 3.5 Sonnet / Opus or OpenAI o3 for high-risk legal and architecture decisions.

---

## 3. Documentation & Guides
- **Setup Guide:** [[_INFRASTRUCTURE/omniroute/SETUP|OmniRoute Setup Guide]]
- **Completion Report:** [[_INFRASTRUCTURE/omniroute/COMPLETION|Integration Completion Report]]
- **Hardware Registry:** [[_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml]]
- **Local Stack Registry:** [[_REGISTRIES/LOCAL_MODEL_AGENT_STACK_REGISTRY.md|LOCAL_MODEL_AGENT_STACK_REGISTRY.md]]
