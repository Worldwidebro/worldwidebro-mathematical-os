---
id: DOC-04-NET-011
aliases: ['NETWORK-FIREWALL']
tags: ['network', 'network-firewall', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]] | [[_REGISTRIES/network_registry.json]]

# Host Firewall & Ingress Rules (pfctl)

> **Authority:** CP-027 | **Status:** ACTIVE

- macOS Packet Filter (`pfctl`) active.
- Default Inbound: Block all on external interfaces (`en0`).
- Allowed Inbound: WireGuard UDP traffic on Tailscale interface.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/network_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/API-GATEWAYS|API-GATEWAYS]]
- [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/ZERO-TRUST|ZERO-TRUST]]
- [[_REGISTRIES/network_registry.json|network_registry.json]]
