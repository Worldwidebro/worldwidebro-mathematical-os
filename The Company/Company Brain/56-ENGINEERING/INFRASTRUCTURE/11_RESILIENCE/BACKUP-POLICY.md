---
id: DOC-11-RES-002
aliases: ['BACKUP-POLICY']
tags: ['resilience', 'backup-policy', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|RESILIENCE]] | [[_REGISTRIES/infrastructure_risk_registry.json]]

# Canonical Backup Policy Directives

> **Authority:** CP-027 | **Status:** ENFORCED

- Neo4j graph and PostgreSQL transactional databases backed up daily at 02:00 and 03:00.
- Retention: 30 daily snapshots, 12 monthly archives.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|RESILIENCE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_risk_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/BACKUP-STORAGE|BACKUP-STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASE-BACKUPS|DATABASE-BACKUPS]]
- [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/AVAILABILITY-RISK|AVAILABILITY-RISK]]
- [[_REGISTRIES/infrastructure_risk_registry.json|infrastructure_risk_registry.json]]
