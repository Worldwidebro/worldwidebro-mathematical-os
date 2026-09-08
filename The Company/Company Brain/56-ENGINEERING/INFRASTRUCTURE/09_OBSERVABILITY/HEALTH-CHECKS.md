---
id: DOC-09-OBS-002
aliases: ['HEALTH-CHECKS']
tags: ['observability', 'health-checks', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/09_OBSERVABILITY/OBSERVABILITY|OBSERVABILITY]] | [[_REGISTRIES/infrastructure_registry.json]]

# Active Health Checks & Probes

> **Authority:** CP-027 | **Status:** LIVE

- Neo4j HTTP probe: `curl -f http://localhost:7474`
- Qdrant probe: `curl -f http://localhost:6333/health`
- Postgres probe: `pg_isready -U admin`

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/09_OBSERVABILITY/OBSERVABILITY|OBSERVABILITY]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/PORTS|PORTS]]
- [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]]
- [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
