---
id: DOC-03-STOR-002
aliases: ['BACKUP-STORAGE']
tags: ['storage', 'backup-storage', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]] | [[_REGISTRIES/storage_registry.json]]

# Backup Storage Media & Snapshots

> **Authority:** CP-027 | **Status:** ACTIVE

- Automated database backups stored in `/Volumes/LaCie/postgres/backups` and `/Volumes/LaCie/backups/neo4j`.
- Mirrored to secondary hardware `/Volumes/T7 Shield/cold_archive`.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/storage_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/BACKUP-ARCHITECTURE|BACKUP-ARCHITECTURE]]
- [[_REGISTRIES/storage_registry.json|storage_registry.json]]
