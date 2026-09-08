---
id: DOC-07-RNT-004
aliases: ['DOCKER-COMPOSE']
tags: ['runtime', 'docker-compose', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]] | [[_REGISTRIES/infrastructure_registry.json]]

# Docker Compose Stacks & Consolidation

> **Authority:** CP-027 | **Status:** AUDITED / REMEDIATION REQUIRED

- Current Clutter: 4 parallel compose projects (`civos_*`, `t7shield-*`, `spinup-*`, `buzz-*`).
- Target: Consolidated `_INFRASTRUCTURE/docker-compose.yml` declaring only canonical services.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/PORTS|PORTS]]
- [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|DEPLOYMENT]]
- [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
