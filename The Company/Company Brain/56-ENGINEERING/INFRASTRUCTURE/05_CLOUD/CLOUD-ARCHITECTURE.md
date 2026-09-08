---
id: DOC-05-CLD-002
aliases: ['CLOUD-ARCHITECTURE']
tags: ['cloud', 'cloud-architecture', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/05_CLOUD/CLOUD|CLOUD]] | [[_REGISTRIES/infrastructure_registry.json]]

# Hybrid Local-First Cloud Architecture

> **Authority:** CP-027 | **Status:** ACTIVE

```text
       [ Global Users / Customers ]
                    │
                    ▼
       ┌────────────────────────┐
       │   Vercel Edge Network  │ (95 Frontend Venture Sites)
       └────────────┬───────────┘
                    │
            HTTPS Edge Calls
                    │
                    ▼
       ┌────────────────────────┐
       │ Tailscale Mesh Ingress │
       └────────────┬───────────┘
                    │
                    ▼
       ┌────────────────────────┐
       │   Mac Studio M4 Max    │ (Local Graph, Vector DB, MLX)
       └────────────────────────┘
```

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/05_CLOUD/CLOUD|CLOUD]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/SERVERLESS|SERVERLESS]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK-CDN|NETWORK-CDN]]
- [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]]
- [[23-VENTURES]]
