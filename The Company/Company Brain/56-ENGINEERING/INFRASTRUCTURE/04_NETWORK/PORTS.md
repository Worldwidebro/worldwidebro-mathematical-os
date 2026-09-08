---
id: DOC-04-NET-019
aliases: ['PORTS']
tags: ['network', 'ports', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]] | [[_REGISTRIES/network_registry.json]]

# Canonical Port Registry

> **Authority:** CP-027 | **Status:** AUDITED / ENFORCED

| Port | Protocol | Bound Service | Host Node | Status |
|---|---|---|---|---|
| `3003` | HTTP | Langfuse Tracing (`civos_langfuse`) | mac-studio | LIVE |
| `3010` | HTTP | Open WebUI (`civos_webui`) | mac-studio | LIVE |
| `3011` | HTTP | Grafana Dashboards (`t7shield-grafana-1`)| mac-studio | LIVE |
| `4000` | HTTP | LiteLLM Router (`civos_litellm`) | mac-studio | LIVE |
| `5432` | TCP/SQL | PostgreSQL 16 (`postgres`) | mac-studio | LIVE |
| `6333` | HTTP/REST| Qdrant Vector DB (`civos_qdrant`) | mac-studio | LIVE |
| `6379` | TCP | Redis In-Memory Cache | mac-studio | LIVE |
| `7474` | HTTP | Neo4j Browser UI (`civos_neo4j`) | mac-studio | LIVE |
| `7687` | Bolt | Neo4j Bolt Protocol (`civos_neo4j`)| mac-studio | LIVE |
| `20128`| HTTP | OmniRoute AI Gateway | mac-studio | LIVE |
| `52415`| HTTP | exo Native MLX Inference Server | mac-studio | LIVE |

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/network_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/API-GATEWAYS|API-GATEWAYS]]
- [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/ZERO-TRUST|ZERO-TRUST]]
- [[_REGISTRIES/network_registry.json|network_registry.json]]
