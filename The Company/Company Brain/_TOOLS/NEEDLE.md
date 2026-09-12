---
id: TOOL-NEEDLE-001
title: Needle — 14MB Edge & Mobile Function Routing Model
aliases: ["Needle", "needle", "CAP-EDGE-INFERENCE"]
tags: [tools, needle, edge, mobile, routing, function-calling]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[REALITY]] | [[13_ENGINEERING/INFRASTRUCTURE/03_COMPUTE/COMPUTE|COMPUTE]] | [[LOCAL_MODEL_AGENT_STACK_REGISTRY]] | [[INDEX]]

# Needle (`cactus-compute/needle`)

**Authority:** CP-027 (Infrastructure & Compute)  
**Status:** ✅ `ADOPTED & SPECIFIED` (`scripts/needle_route`)  
**Gap Resolution:** Resolves `CAP-EDGE-INFERENCE` utilizing starred repository [`cactus-compute/needle`](https://github.com/cactus-compute/needle) (9,992 ★).

---

## 1. System Overview
Needle is an ultra-compact (14MB footprint, 26M parameter) model engineered specifically for on-device function calling, intent classification, and command dispatch. It executes locally on Apple Silicon / CoreML / iOS with sub-millisecond latency and zero cloud dependence.

## 2. Integration with Company Brain
Needle functions as our **Tier-0 Edge Classifier**:
- Intercepts voice and text commands on mobile engineering nodes before routing.
- If intent matches simple local functions (e.g. status check, timer, dispatch alert), it resolves instantly offline.
- If intent requires complex multi-step reasoning, it delegates upstream to OmniRoute (`:20128`) over Tailscale mesh.

## 3. Invocation
```bash
./scripts/needle_route "Check dispatch status for LT-005"
```
