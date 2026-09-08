---
id: DOC-09-OBS-007
aliases: ['PERFORMANCE']
tags: ['observability', 'performance', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/09_OBSERVABILITY/OBSERVABILITY|OBSERVABILITY]] | [[_REGISTRIES/infrastructure_registry.json]]

# Performance Engineering & Latency Baselines

> **Authority:** CP-027 | **Status:** AUDITED

- Native `exo` Qwen 3.6 35B: ~35-45 tokens/second.
- LiteLLM routing overhead: < 8ms.
- Qdrant vector search: < 15ms.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/09_OBSERVABILITY/OBSERVABILITY|OBSERVABILITY]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/PORTS|PORTS]]
- [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]]
- [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
