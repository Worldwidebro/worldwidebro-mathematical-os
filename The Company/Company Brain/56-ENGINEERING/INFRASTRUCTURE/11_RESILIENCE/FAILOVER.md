---
id: DOC-11-RES-008
aliases: ['FAILOVER']
tags: ['resilience', 'failover', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|RESILIENCE]] | [[_REGISTRIES/infrastructure_risk_registry.json]]

# Failover Procedures & LiteLLM Fallback Chains

> **Authority:** CP-027 | **Status:** LIVE_VERIFIED

- LiteLLM automatic fallback routing:
  - `qwen-heavy` (Local 35B) -> `claude-3-5-sonnet` (Cloud fallback)
  - `qwen-fast` (Local 35B) -> `claude-3-5-haiku` (Cloud fallback)
- Host failover: Re-attaching external drives or spinning up standby docker stack on MacBook Air.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|RESILIENCE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_risk_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/BACKUP-STORAGE|BACKUP-STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASE-BACKUPS|DATABASE-BACKUPS]]
- [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/AVAILABILITY-RISK|AVAILABILITY-RISK]]
- [[_REGISTRIES/infrastructure_risk_registry.json|infrastructure_risk_registry.json]]
