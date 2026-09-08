---
id: INFRA-SUB-OLLAMA
title: "Ollama Local Inference Service Infrastructure"
aliases: ["_INFRASTRUCTURE/ollama", "Ollama Infrastructure"]
tags: [infrastructure, ollama, local-inference, qwen, llama, edge]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/README|56-ENGINEERING]] | [[CLAUDE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]]

# Ollama Local Inference Service Infrastructure

Infrastructure hosting Ollama background inference daemon (`:11434`) for edge and fallback execution.

## Architecture & Serving
- **Models Domain Hub:** [[17-MODELS/17-MODELS|17-MODELS]]
- **OmniRoute Router:** [[_INFRASTRUCTURE/omniroute/README|OmniRoute]]
- **Hardware Registry:** [[_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml]]
- **Live Infrastructure State:** [[CLAUDE.md]]
