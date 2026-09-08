---
id: DOC-11-RES-001
aliases: ['BACKUP-ARCHITECTURE']
tags: ['resilience', 'backup-architecture', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|RESILIENCE]] | [[_REGISTRIES/infrastructure_risk_registry.json]]

# Backup Storage Architecture & Topologies

> **Authority:** CP-027 | **Status:** ACTIVE

```text
  [ Mac Studio DBs ] ──Daily Dump──> [ /Volumes/LaCie/backups/ ]
                                               │
                                     Weekly Rsync Mirror
                                               │
                                               ▼
                                    [ /Volumes/T7 Shield/cold_archive/ ]
```

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|RESILIENCE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_risk_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/BACKUP-STORAGE|BACKUP-STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASE-BACKUPS|DATABASE-BACKUPS]]
- [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/AVAILABILITY-RISK|AVAILABILITY-RISK]]
- [[_REGISTRIES/infrastructure_risk_registry.json|infrastructure_risk_registry.json]]
