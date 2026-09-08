---
id: DOC-02-COMP-012
aliases: ['SERVERS']
tags: ['compute', 'servers', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]] | [[_REGISTRIES/compute_registry.json]]

# Dedicated Hardware Servers & Nodes

> **Authority:** CP-027 | **Status:** LIVE

## Primary Server Node: Mac Studio M4 Max (`DEV-MAC-STUDIO-001`)
- **Role:** Central database host, local MLX inference engine, Docker container server.
- **Hardware:** Apple M4 Max 12-core CPU, 32-core GPU, 16-core Neural Engine, 36GB Unified Memory.
- **Network Interfaces:** Tailscale WireGuard (`100.87.214.70`), Local Gigabit LAN (`192.168.1.11`).
- **Power & Cooling:** Continuous desktop power delivery, active dual-blower thermal management.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/compute_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[_REGISTRIES/compute_registry.json|compute_registry.json]]
