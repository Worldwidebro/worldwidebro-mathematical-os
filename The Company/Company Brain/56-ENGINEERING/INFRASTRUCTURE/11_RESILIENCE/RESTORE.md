---
id: DOC-11-RES-013
aliases: ['RESTORE']
tags: ['resilience', 'restore', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|RESILIENCE]] | [[_REGISTRIES/infrastructure_risk_registry.json]]

# Restoration Runbooks & Step-by-Step Procedures

> **Authority:** CP-027 | **Status:** AUDITED

- Scripted restoration commands for Neo4j (`neo4j-admin database load`) and Postgres (`psql < backup.sql`).

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|RESILIENCE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_risk_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/BACKUP-STORAGE|BACKUP-STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASE-BACKUPS|DATABASE-BACKUPS]]
- [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/AVAILABILITY-RISK|AVAILABILITY-RISK]]
- [[_REGISTRIES/infrastructure_risk_registry.json|infrastructure_risk_registry.json]]
