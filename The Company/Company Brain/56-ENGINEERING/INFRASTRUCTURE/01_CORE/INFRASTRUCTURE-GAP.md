---
id: DOC-01-GAP-001
aliases: ['INFRASTRUCTURE-GAP']
tags: ['gap-analysis', 'roadmap', 'core']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Infrastructure Gap Analysis

> **Authority:** CP-027  
> **Status:** ACTIVE  
> **Updated:** 2026-09-05

| Component | Current Reality (Audited) | Target Architecture | Gap Severity | Remediation Action |
|---|---|---|---|---|
| **Docker Stacks** | 4 competing compose projects running simultaneously | Single canonical `docker-compose.yml` | HIGH | Teardown non-canonical stacks (`t7shield-*`, `spinup-*`, `buzz-*`) |
| **Neo4j** | 1 healthy (`civos_neo4j`), 1 crash-looping (`t7shield-neo4j-1`) | 1 healthy canonical instance | MEDIUM | Delete `t7shield-neo4j-1` container and prune dead volume |
| **Observability** | Langfuse running but receiving 0 traces | LiteLLM streaming all agent calls to Langfuse | MEDIUM | Add `success_callback: ["langfuse"]` in `civos_litellm` config |
| **Model Routing** | LiteLLM using `simple-shuffle` round-robin | Scored routing (`latency-based-routing`) | LOW | Update LiteLLM `router_settings.routing_strategy` |
| **Embeddings** | Broken route (points to dead Ollama) | Local MLX or cloud embeddings provider | MEDIUM | Reconfigure `embed` model endpoint in LiteLLM |
| **Registries** | Fragmented yaml files | 23 synchronized JSON registries in `_REGISTRIES/` | RESOLVED | Generated complete machine-readable registries |

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
