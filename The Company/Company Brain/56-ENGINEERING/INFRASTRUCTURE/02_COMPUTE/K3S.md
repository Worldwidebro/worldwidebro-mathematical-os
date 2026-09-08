---
id: DOC-02-COMP-007
aliases: ['K3S']
tags: ['compute', 'k3s', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]] | [[_REGISTRIES/compute_registry.json]]

# K3s Lightweight Cluster Specification

> **Authority:** CP-027 | **Status:** DECLARED

- **Control Plane Node:** Mac Studio M4 Max (`k3s server --disable traefik`).
- **Worker Node:** MacBook Air (`k3s agent`).
- **CNI:** Flannel / WireGuard native overlay.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/compute_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[_REGISTRIES/compute_registry.json|compute_registry.json]]
