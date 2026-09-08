---
id: DOC-01-ARCH-001
aliases: ['INFRASTRUCTURE-ARCHITECTURE']
tags: ['architecture', 'core', 'tiers']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Infrastructure Architecture

> **Authority:** CP-027  
> **Status:** AUDITED  
> **Updated:** 2026-09-05

## 1. Multi-Tier Architecture
The Company Brain infrastructure is organized into four discrete operational tiers:

1. **Edge Tier (Cloud / CDN):**
   - Vercel global serverless edge network running 95 venture frontends.
   - Cloudflare DNS and edge routing.
2. **Mesh Gateway Tier (Ingress / Control):**
   - Tailscale WireGuard private overlay network.
   - OmniRoute v3.8.50 distributed gateway (`:20128`).
   - LiteLLM unified model router (`:4000`).
3. **Execution Tier (Compute & Inference):**
   - Mac Studio M4 Max (12-core CPU, 32-core GPU, 36GB unified RAM).
   - MacBook Air (8-core CPU, 16GB unified RAM).
   - Native Apple MLX inference via `exo` (`:52415`).
4. **Persistence Tier (Databases & Storage):**
   - Neo4j Knowledge Graph (`:7687`/`:7474`) on LaCie 4TB.
   - Qdrant Vector Engine (`:6333`) on LaCie 4TB.
   - PostgreSQL 16 Operational DB (`:5432`) on LaCie 4TB.
   - Redis 7.x In-Memory State (`:6379`).

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
