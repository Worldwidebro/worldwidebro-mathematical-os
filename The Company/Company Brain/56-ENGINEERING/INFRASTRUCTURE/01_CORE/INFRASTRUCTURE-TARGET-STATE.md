---
id: DOC-01-TARG-001
aliases: ['INFRASTRUCTURE-TARGET-STATE']
tags: ['target-state', 'future-architecture', 'core']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Target Infrastructure State

> **Authority:** CP-027  
> **Status:** APPROVED TARGET  
> **Updated:** 2026-09-05

## 1. Target Single-Instance Architecture
The target state consolidates Mac Studio's competing compose projects into a single, clean, declarative Docker Compose file (`_INFRASTRUCTURE/docker-compose.yml`):
- Exactly **1 Neo4j instance** (`neo4j:5.x`, ports 7474/7687).
- Exactly **1 Qdrant instance** (`qdrant:latest`, port 6333).
- Exactly **1 PostgreSQL 16 instance** (port 5432).
- Exactly **1 Redis instance** (port 6379).
- Exactly **1 LiteLLM instance** (port 4000) with wired Langfuse callback.
- Exactly **1 Grafana instance** (port 3011) with auto-provisioned dashboards.
- Exactly **1 Langfuse instance** (port 3003) actively recording all traces.
- All dead, duplicate, and crash-looping containers eliminated.

## 2. Automated Drift & Policy Verification
Continuous verification via OPA / Conftest policy-as-code and automated drift detection scripts comparing declared compose state against running Docker daemon containers.

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
