---
id: DOC-09-OBS-012
aliases: ['TRACING']
tags: ['observability', 'tracing', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/09_OBSERVABILITY/OBSERVABILITY|OBSERVABILITY]] | [[_REGISTRIES/infrastructure_registry.json]]

# Distributed Tracing & Langfuse Integration

> **Authority:** CP-027 | **Status:** AUDITED / REMEDIATION REQUIRED

- Langfuse container `civos_langfuse` is healthy on port `:3003`.
- **Known Gap:** Currently receiving 0 traces due to missing callback in `civos_litellm`. Immediate action is adding `success_callback: ["langfuse"]`.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/09_OBSERVABILITY/OBSERVABILITY|OBSERVABILITY]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/PORTS|PORTS]]
- [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]]
- [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
