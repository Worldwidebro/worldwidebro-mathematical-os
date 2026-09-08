---
id: DOC-04-NET-016
aliases: ['NETWORK-SEGMENTATION']
tags: ['network', 'network-segmentation', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]] | [[_REGISTRIES/network_registry.json]]

# Network Segmentation & Access Control

> **Authority:** CP-027 | **Status:** ACTIVE

- Subnet `100.64.0.0/10` isolated from public Internet.
- Docker bridge `172.18.0.0/16` isolates database containers from host loopback where applicable.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/network_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/API-GATEWAYS|API-GATEWAYS]]
- [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/ZERO-TRUST|ZERO-TRUST]]
- [[_REGISTRIES/network_registry.json|network_registry.json]]
