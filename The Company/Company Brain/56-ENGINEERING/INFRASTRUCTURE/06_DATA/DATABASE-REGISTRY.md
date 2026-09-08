---
id: DOC-06-DATA-009
aliases: ['DATABASE-REGISTRY']
tags: ['data', 'database-registry', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]] | [[_REGISTRIES/database_registry.json]]

# Database Instances Registry

> **Authority:** CP-027 | **Status:** AUDITED

| DB ID | Engine | Container | Port | Persistent Path | Role | Status |
|---|---|---|---|---|---|---|
| `DB-NEO4J-001` | Neo4j 5.x | `civos_neo4j` | 7474, 7687 | `/Volumes/LaCie/neo4j/data` | Knowledge Graph | LIVE_CANONICAL |
| `DB-QDRANT-001` | Qdrant | `civos_qdrant` | 6333 | `/Volumes/LaCie/qdrant/storage`| Vector Semantic Store | LIVE_CANONICAL |
| `DB-POSTGRES-001`| Postgres 16 | `postgres` | 5432 | `/Volumes/LaCie/postgres/data` | Operational Relational DB| LIVE_CANONICAL |
| `DB-REDIS-001` | Redis 7.x | `redis` | 6379 | In-Memory / AOF | Response Cache & State | LIVE_CANONICAL |

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/database_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/EXTERNAL-STORAGE|EXTERNAL-STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/PORTS|PORTS]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/BACKUP|BACKUP]]
- [[_REGISTRIES/database_registry.json|database_registry.json]]
