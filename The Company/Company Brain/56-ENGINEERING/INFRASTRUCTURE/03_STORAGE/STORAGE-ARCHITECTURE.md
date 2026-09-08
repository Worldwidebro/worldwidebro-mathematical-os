---
id: DOC-03-STOR-011
aliases: ['STORAGE-ARCHITECTURE']
tags: ['storage', 'storage-architecture', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]] | [[_REGISTRIES/storage_registry.json]]

# Tiered Storage Architecture

> **Authority:** CP-027 | **Status:** ACTIVE

```text
Tier 0 (Fast NVMe Internal):   Mac Studio SSD (512GB) / Air SSD (228GB)  -> OS & Binaries
Tier 1 (High-Cap External):    LaCie 4TB HDD (/Volumes/LaCie)            -> Active Databases
Tier 2 (High-Speed NVMe Ext):  Samsung T7 Shield 2TB (/Volumes/T7 Shield)-> Large Models
Tier 3 (Cold Archive):         Encrypted Snapshots / Offsite Mirror      -> Disaster Vault
```

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/storage_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]]
- [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/BACKUP-ARCHITECTURE|BACKUP-ARCHITECTURE]]
- [[_REGISTRIES/storage_registry.json|storage_registry.json]]
