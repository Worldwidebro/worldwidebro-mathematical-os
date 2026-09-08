---
id: DOC-06-DATA-004
aliases: ['DATABASE-ARCHITECTURE']
tags: ['data', 'database-architecture', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]] | [[_REGISTRIES/database_registry.json]]

# Polyglot Persistence Architecture

> **Authority:** CP-027 | **Status:** LIVE

```text
       ┌────────────────────────────────────────────────────────┐
       │               Company Brain Data Plane                 │
       └───────────────────────────┬────────────────────────────┘
                                   │
         ┌──────────────┬──────────┴───┬──────────────┬─────────┐
         ↓              ↓              ↓              ↓         ↓
     [ Neo4j ]      [ Qdrant ]    [ Postgres ]    [ Redis ]  [ MinIO ]
    (Graph Rels)  (Vectors/Sem)  (Relational)   (KV/Cache)   (S3 Object)
     Port 7687      Port 6333      Port 5432      Port 6379   Port 9000
         │              │              │              │         │
         └──────────────┴──────────┬───┴──────────────┴─────────┘
                                   ▼
                       /Volumes/LaCie/ (4TB Storage)
```

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/database_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/EXTERNAL-STORAGE|EXTERNAL-STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/PORTS|PORTS]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/BACKUP|BACKUP]]
- [[_REGISTRIES/database_registry.json|database_registry.json]]
