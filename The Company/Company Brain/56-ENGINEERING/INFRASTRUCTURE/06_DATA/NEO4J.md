---
id: DOC-06-DATA-014
aliases: ['NEO4J']
tags: ['data', 'neo4j', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]] | [[_REGISTRIES/database_registry.json]]

# Neo4j Graph Database Specification

> **Authority:** CP-027 | **Status:** LIVE_VERIFIED

- Container: `civos_neo4j` (canonical instance)
- Bolt Port: `7687` | HTTP Port: `7474`
- Plugins: APOC enabled.
- Heap Settings: Initial 2GB, Max 4GB.
- Storage: `/Volumes/LaCie/neo4j/data`
- Note: Dead container `t7shield-neo4j-1` is crash-looping and flagged for removal.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/database_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/EXTERNAL-STORAGE|EXTERNAL-STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/PORTS|PORTS]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/BACKUP|BACKUP]]
- [[_REGISTRIES/database_registry.json|database_registry.json]]
