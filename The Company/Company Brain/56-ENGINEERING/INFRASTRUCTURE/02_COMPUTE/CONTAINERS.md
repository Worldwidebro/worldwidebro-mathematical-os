---
id: DOC-02-COMP-002
aliases: ['CONTAINERS']
tags: ['compute', 'containers', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]] | [[_REGISTRIES/compute_registry.json]]

# Container Runtime & Docker Engines

> **Authority:** CP-027 | **Status:** LIVE / AUDITED

- **Docker Host:** Mac Studio (`docker --context macstudio`).
- **Running Containers:**
  - `civos_neo4j` (Up, Healthy, ports 7474/7687)
  - `civos_qdrant` (Up, Healthy, port 6333)
  - `civos_litellm` (Up, port 4000)
  - `civos_langfuse` (Up, port 3003)
  - `t7shield-grafana-1` (Up, port 3011)
  - `civos_webui` (Up, port 3010)
  - `postgres` (Up, port 5432)
- **Dead Containers:** `t7shield-neo4j-1` (Crash-looping, flagged for pruning).

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/compute_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[_REGISTRIES/compute_registry.json|compute_registry.json]]
