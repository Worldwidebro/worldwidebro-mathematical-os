---
id: DOC-01-CURR-001
aliases: ['INFRASTRUCTURE-CURRENT-STATE']
tags: ['state', 'current-state', 'audit', 'core']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Current Infrastructure State (Audited Reality)

> **Authority:** CP-027  
> **Status:** AUDITED LIVE  
> **Updated:** 2026-09-05

## Verified Operating Realities
1. **Host Connectivity:** Mac Studio (`100.87.214.70`) and MacBook Air (`100.121.17.63`) are online via Tailscale mesh.
2. **Local Inference:** Native MLX serving via `exo` on port `:52415` running `mlx-community/Qwen3.6-35B-A3B-5bit`. Ollama is dead/uninstalled.
3. **Database Layer:** `civos_neo4j` is healthy on ports `:7474`/`:7687`; `civos_qdrant` is healthy on port `:6333`; PostgreSQL is healthy on port `:5432`.
4. **Cloud Layer:** 95 sites deployed and routing on Vercel Edge.

## Critical Anomalies & Clutter
- **Duplicate Compose Projects:** Mac Studio runs 4 overlapping Docker Compose projects (`civos_*`, `t7shield-*`, `spinup-*`, `buzz-*`). Confirmed running concurrently: 2x Neo4j, 2x Qdrant, 2x Langfuse, 3x Redis, 3x Postgres.
- **Crash-Looping Container:** `t7shield-neo4j-1` is in continuous crash loop due to deprecated Neo4j 4.x configuration parameter.
- **Port Misunderstandings:** Port 3010 is Open WebUI; Grafana is on port 3011.
- **Langfuse Disconnected:** `civos_langfuse` is running healthy on port 3003 but receiving zero LLM traces because LiteLLM lacks the callback hook.

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
