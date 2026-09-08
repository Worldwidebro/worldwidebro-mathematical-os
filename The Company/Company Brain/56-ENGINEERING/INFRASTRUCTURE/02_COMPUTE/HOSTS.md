---
id: DOC-02-COMP-006
aliases: ['HOSTS']
tags: ['compute', 'hosts', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]] | [[_REGISTRIES/compute_registry.json]]

# Host Inventory & Node Mapping

> **Authority:** CP-027 | **Status:** AUDITED

| Host Identifier | Hostname | IP (Tailscale) | IP (LAN) | Architecture | Role |
|---|---|---|---|---|---|
| `HOST-MAC-STUDIO-001` | `mac-studio` | `100.87.214.70` | `192.168.1.11` | arm64 (Apple Silicon) | Primary Database & Inference Host |
| `HOST-MACBOOK-AIR-001` | `aces-macbook-air-1` | `100.121.17.63` | DHCP | arm64 (Apple Silicon) | Mobile Engineering Workstation |
| `HOST-OMNIROUTE-NODE` | `omniroute-6da9315f` | `100.80.229.113` | N/A | virtual (Tailscale) | AI Provider Gateway & MCP Hub |
| `HOST-VERCEL-EDGE` | `vercel-edge-global` | Dynamic | Dynamic | Anycast Edge | Frontend Serverless Runtimes |

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/compute_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[_REGISTRIES/compute_registry.json|compute_registry.json]]
