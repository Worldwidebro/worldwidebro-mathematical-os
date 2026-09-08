---
id: DOC-08-DEP-011
aliases: ['ENVIRONMENTS']
tags: ['deployment', 'environments', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|DEPLOYMENT]] | [[_REGISTRIES/infrastructure_dependency_registry.json]]

# Multi-Tier Environment Hierarchy

> **Authority:** CP-027 | **Status:** AUDITED

1. **Development:** Local engineering sandbox on MacBook Air (`aces-macbook-air-1`).
2. **Testing:** Disposable containers and automated regression runners.
3. **Staging:** Isolated pre-merge validation stack on Mac Studio.
4. **Production:** Mac Studio M4 Max daemon cluster + Vercel Global Edge Network.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|DEPLOYMENT]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_dependency_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECURITY-INFRASTRUCTURE|SECURITY-INFRASTRUCTURE]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/FAILOVER|FAILOVER]]
- [[_REGISTRIES/infrastructure_dependency_registry.json|infrastructure_dependency_registry.json]]
