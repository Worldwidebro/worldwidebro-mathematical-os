---
id: DOC-INFRA-REG-RSK-001
aliases: ['INFRASTRUCTURE-RISK-REGISTER']
tags: ['risk', 'register', 'mitigation']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Infrastructure Risk Register

> **Authority:** CP-027 & CP-028  
> **Status:** AUDITED — 2026-09-06  
> **Machine-Readable Registry:** [[_REGISTRIES/infrastructure_risk_registry.json|infrastructure_risk_registry.json]]

## 1. Authoritative Risk Matrix

| Risk ID | Title | Likelihood | Impact | Severity | Mitigation |
|---|---|---|---|---|---|
| `RSK-001` | Mac Studio Hardware Failure | LOW | CRITICAL | HIGH | Maintain MacBook Air warm standby |
| `RSK-002` | Docker Compose Stack Clutter | CERTAIN | MEDIUM | HIGH | Consolidate to single canonical compose file |
| `RSK-003` | 36GB Unified RAM Saturation | MEDIUM | HIGH | HIGH | Quantize models to 5-bit; enforce limits |
| `RSK-004` | Disconnected Langfuse Callback | CERTAIN | MEDIUM | MEDIUM | Enable callback in LiteLLM config |
| `RSK-005` | Bus Factor 1 on Solo Founder | HIGH | CRITICAL | CRITICAL | Machine-readable self-documenting runbooks |

## 2. Connected Documents
- Risk Overview: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-RISKS|INFRASTRUCTURE-RISKS.md]]
- Single Points of Failure: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/SINGLE-POINTS-OF-FAILURE|SINGLE-POINTS-OF-FAILURE.md]]
- Risk Control Plane: [[34-RISK/34-RISK|34-RISK]]
