---
id: DOC-04-NET-010
aliases: ['NETWORK-DNS']
tags: ['network', 'network-dns', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]] | [[_REGISTRIES/network_registry.json]]

# Split-DNS & MagicDNS Architecture

> **Authority:** CP-027 | **Status:** LIVE

- Internal names resolve via Tailscale MagicDNS: `mac-studio.ts.net`, `aces-macbook-air-1.ts.net`.
- External names resolve via 1.1.1.1 / Cloudflare.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/network_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/API-GATEWAYS|API-GATEWAYS]]
- [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/ZERO-TRUST|ZERO-TRUST]]
- [[_REGISTRIES/network_registry.json|network_registry.json]]
