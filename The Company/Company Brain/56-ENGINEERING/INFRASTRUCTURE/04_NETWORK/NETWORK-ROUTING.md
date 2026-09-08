---
id: DOC-04-NET-015
aliases: ['NETWORK-ROUTING']
tags: ['network', 'network-routing', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]] | [[_REGISTRIES/network_registry.json]]

# Routing Architecture & Gateway Rules

> **Authority:** CP-027 | **Status:** ACTIVE

- Local traffic routes via Ethernet LAN (`192.168.1.0/24`).
- Inter-node cluster traffic routes strictly over Tailscale tun0 interface.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/network_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/API-GATEWAYS|API-GATEWAYS]]
- [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/ZERO-TRUST|ZERO-TRUST]]
- [[_REGISTRIES/network_registry.json|network_registry.json]]
