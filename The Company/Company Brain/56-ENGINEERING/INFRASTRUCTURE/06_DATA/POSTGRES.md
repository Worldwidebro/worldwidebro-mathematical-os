---
id: DOC-06-DATA-015
aliases: ['POSTGRES']
tags: ['data', 'postgres', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]] | [[_REGISTRIES/database_registry.json]]

# PostgreSQL 16 Operational Database

> **Authority:** CP-027 | **Status:** LIVE_VERIFIED

- Container: `postgres`
- Port: `5432`
- Storage: `/Volumes/LaCie/postgres/data`
- Config: `shared_buffers=256MB`, `max_connections=200`, UTF-8 encoding.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/database_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/EXTERNAL-STORAGE|EXTERNAL-STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/PORTS|PORTS]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/BACKUP|BACKUP]]
- [[_REGISTRIES/database_registry.json|database_registry.json]]
