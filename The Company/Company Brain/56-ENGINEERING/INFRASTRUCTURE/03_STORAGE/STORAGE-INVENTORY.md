---
id: DOC-03-STOR-012
aliases: ['STORAGE-INVENTORY']
tags: ['storage', 'storage-inventory', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]] | [[_REGISTRIES/storage_registry.json]]

# Storage Volume & Drive Inventory

> **Authority:** CP-027 | **Status:** AUDITED

| Volume ID | Device | Mount Point | Capacity | Used | Available | Primary Purpose |
|---|---|---|---|---|---|---|
| `VOL-STUDIO-INT` | Mac Studio Internal SSD | `/` | 512GB | 194GB | 318GB | macOS, Docker VM, Local Cache |
| `VOL-STUDIO-LACIE`| LaCie Desktop HDD | `/Volumes/LaCie` | 4TB | ~450GB | ~3.5TB | Neo4j, Qdrant, Postgres, Dumps |
| `VOL-AIR-INT` | MacBook Air Internal SSD | `/` | 228GB | 194GB | 34GB | Dev Repositories, Brain Root |
| `VOL-AIR-T7` | Samsung T7 Shield NVMe | `/Volumes/T7 Shield` | 1.8TB | 889GB | 911GB | Local LLM Weights & Shards |

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/storage_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/BACKUP-ARCHITECTURE|BACKUP-ARCHITECTURE]]
- [[_REGISTRIES/storage_registry.json|storage_registry.json]]
