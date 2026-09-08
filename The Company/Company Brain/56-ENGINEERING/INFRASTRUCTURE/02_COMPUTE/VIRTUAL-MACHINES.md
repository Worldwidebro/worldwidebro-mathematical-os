---
id: DOC-02-COMP-013
aliases: ['VIRTUAL-MACHINES']
tags: ['compute', 'virtual-machines', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]] | [[_REGISTRIES/compute_registry.json]]

# Virtual Machines & Hypervisors

> **Authority:** CP-027 | **Status:** AUDITED

- **macOS Virtualization.framework:** Powers the headless Linux kernel running Mac Studio's Docker Engine daemon.
- **Resource Constraints:** 6 vCPUs and 12GB RAM allocated to Docker Engine VM on Mac Studio to preserve 24GB RAM for native MLX `exo` inference.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/compute_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[_REGISTRIES/compute_registry.json|compute_registry.json]]
