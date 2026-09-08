---
id: DOC-06-DATA-005
aliases: ['DATABASE-BACKUPS']
tags: ['data', 'database-backups', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]] | [[_REGISTRIES/database_registry.json]]

# Automated Database Backup Routines

> **Authority:** CP-027 | **Status:** ACTIVE

- Neo4j: Daily APOC / database dump to `/Volumes/LaCie/backups/neo4j`.
- PostgreSQL: Daily `pg_dumpall` to `/Volumes/LaCie/postgres/backups`.
- Qdrant: Snapshot API export triggered weekly.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/database_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/EXTERNAL-STORAGE|EXTERNAL-STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/PORTS|PORTS]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/BACKUP|BACKUP]]
- [[_REGISTRIES/database_registry.json|database_registry.json]]
