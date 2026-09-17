---
title: Model Router Architecture
id: MODEL-ROUTER-ARCH
phase: Phase 2 (Local Autonomy)
updated: 2026-09-17
---

# Model Router Architecture

**Goal:** Route 80% of reasoning to local Ollama, reserve Claude for 20% highest-value work.

## Available Models

| Model | Size | Speed | Use Case | Cost |
|-------|------|-------|----------|------|
| qwen2.5-coder | 8.9G | Fast | Classification, extraction | $0 |
| hermes3 | 4.6G | Medium | Reasoning, analysis | $0 |
| llama3.1 | 4.9G | Fastest | Summarization, routing | $0 |
| Claude Sonnet | Cloud | - | Complex reasoning | $0.003-0.01 |
| Claude Opus | Cloud | - | Strategic decisions | $0.015-0.05 |

## Routing Rules

```
classify/extract → qwen2.5-coder (local)
  ↓
analyze/reason/plan → hermes3 (local)
  ↓
novel_strategy/legal/architecture → Claude (cloud, auth required)
  ↓
fallback → llama3.1 (local)
```

## Cost Model

- **Local-first (80/20 split):** ~$3-5/month
- **Claude-only approach:** ~$15-30/month
- **Savings: 70-80%** ✅

## Integration

Wire to:
- [[TOOL-GATEWAY-PERMISSIONS]] (authorization)
- [[AUTONOMOUS-LOOP-SPECIFICATION]] (UNDERSTAND step)
- [[CAPABILITY_REGISTRY]] (model hints)
- OmniRoute (MCP gateway)

