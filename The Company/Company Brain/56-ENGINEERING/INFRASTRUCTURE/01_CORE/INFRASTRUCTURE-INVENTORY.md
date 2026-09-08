---
id: DOC-01-INV-001
aliases: ['INFRASTRUCTURE-INVENTORY']
tags: ['inventory', 'hardware', 'assets', 'core']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Infrastructure Asset Inventory

> **Authority:** CP-027  
> **Status:** AUDITED  
> **Updated:** 2026-09-05

| Asset ID | Category | Name / Model | Specifications | Location / Mount | Status |
|---|---|---|---|---|---|
| `DEV-MAC-STUDIO-001` | Compute Host | Mac Studio M4 Max | 12 CPU, 32 GPU, 36GB UMA, 512GB SSD | HQ Primary Desk | LIVE_VERIFIED |
| `DEV-MACBOOK-AIR-001` | Compute Host | MacBook Air | 8 CPU, 8 GPU, 16GB UMA, 228GB SSD | Mobile Workstation | LIVE_VERIFIED |
| `DEV-DRIVE-LACIE-4TB` | Storage | LaCie 4TB Desktop HDD | 4TB, USB-C / Thunderbolt | `/Volumes/LaCie` (Studio) | LIVE_VERIFIED |
| `DEV-DRIVE-T7-2TB` | Storage | Samsung T7 Shield | 2TB (1.8TB formatted), USB 3.2 | `/Volumes/T7 Shield` (Air) | LIVE_VERIFIED |
| `NET-TAILSCALE-MESH` | Network | Tailscale Private Mesh | WireGuard Overlay, 100.64.0.0/10 | Virtual / Worldwide | LIVE_VERIFIED |
| `SRV-EXO-001` | Inference | exo MLX Engine | Qwen3.6-35B-A3B-5bit | Port 52415 (Studio) | LIVE_VERIFIED |
| `SRV-LITELLM-001` | AI Gateway | LiteLLM Router | Python / Docker Proxy | Port 4000 (Studio) | LIVE_VERIFIED |
| `SRV-NEO4J-001` | Database | civos_neo4j | Neo4j 5.x, APOC plugin | Ports 7474/7687 (Studio) | LIVE_VERIFIED |
| `SRV-QDRANT-001` | Database | civos_qdrant | Qdrant Vector Engine | Port 6333 (Studio) | LIVE_VERIFIED |
| `SRV-POSTGRES-001` | Database | PostgreSQL 16 | Relational Engine | Port 5432 (Studio) | LIVE_VERIFIED |
| `SRV-GRAFANA-001` | Observability | Grafana Dashboards | Metrics visualization | Port 3011 (Studio) | LIVE_VERIFIED |
| `CLD-VERCEL-PROD` | Cloud PaaS | Vercel Edge Hosting | 95 Active Deployed Sites | Global Edge | LIVE_VERIFIED |

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
