---
id: DOC-02-COMP-010
aliases: ['MEMORY']
tags: ['compute', 'memory', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]] | [[_REGISTRIES/compute_registry.json]]

# Memory Management & UMA Headroom

> **Authority:** CP-027 | **Status:** AUDITED / CRITICAL CONSTRAINT

- **Total Capacity:** 36GB Unified Memory on Mac Studio.
- **Memory Budget Allocation:**
  - `exo` LLM (Qwen 3.6 35B 5-bit): **24GB**
  - Neo4j Heap + PageCache: **4GB**
  - PostgreSQL Shared Buffers: **1GB**
  - Qdrant Vector Cache: **2GB**
  - Docker VM & System Overhead: **5GB**
  - **Headroom Margin:** ~0GB (Tight headroom; requires strict swap and model offloading controls).

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/compute_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[_REGISTRIES/compute_registry.json|compute_registry.json]]
