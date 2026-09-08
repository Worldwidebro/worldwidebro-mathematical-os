# 01-IDENTITY — Company Identity Registry

**Authority**: Authoritative registry of organizational entities (ventures, people, organizations, roles).

**Data source:** [[02-SOURCES]] (MCPs, APIs)  
**Flows to:** [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER]] → [[16-AGENTS]]

---

## Overview

Master identity graph for Company Brain: 500+ ventures classified into 36 operational industry sectors.

## Data Flow

```
[[02-SOURCES]] (ClickUp, HubSpot, etc.)
    ↓
[[06-ENTITY-RESOLUTION]] (deduplication)
    ↓
01-IDENTITY (this registry)
    ↓
[[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER]] (36 sectors)
    ↓
[[16-AGENTS]] (routing agents)
    ↓
[[52-PEOPLE]] (team assignments & approvals)
```

---

## Phase 1 Status ✅

- ✅ 500 ventures → 36-sector framework
- ✅ identity_registry.yaml created
- ✅ Wired to SECTOR-TAXONOMY
- ✅ Connected to AGENTS
- 🟡 NAICS mapping (Phase 2 ready)
- 🟡 People registry (Phase 3)

---

## Sector Summary

| Sector | Ventures | Status |
|---|---|---|
| AI & Robotics | 60 | Active |
| Retail & E-Commerce | 110 | Active |
| Software & SaaS | 30 | Active |
| Transportation & Logistics | 30 | Active |
| Financial Services | 36 | Active |
| Business Services | 25 | Active |
| Hospitality | 35 | Active |
| Media & Entertainment | 45 | Active |
| Personal Services | 65 | Active |
| Education & Training | 22 | Active |
| **Total** | **500** | **Phase 1 ✅** |

---

## Key Files

- `_REGISTRIES/identity_registry.yaml` — Venture-to-sector mapping
- `_REGISTRIES/ID_REGISTRY.yaml` — Entity ID system
- `_REGISTRIES/ventures-by-sector.yaml` — Venture organization

---

## Connected Domains

- [[02-SOURCES]] ← Data feeds (upstream)
- [[52-PEOPLE]] ← Person entities
- [[16-AGENTS]] ← Routing agents
- [[23-VENTURES]] ← Detailed venture records
- [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER]] → Sector structure
- [[06-ENTITY-RESOLUTION]] → Deduplication

---

## Next Phase

Phase 2: NAICS classification per venture

---

Last updated: 2026-09-02 | Owner: Hermes | Status: Phase 1 Complete ✅
