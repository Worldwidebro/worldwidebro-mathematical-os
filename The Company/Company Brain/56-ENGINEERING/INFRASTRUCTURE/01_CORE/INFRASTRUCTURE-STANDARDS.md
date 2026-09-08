---
id: DOC-01-STD-001
aliases: ['INFRASTRUCTURE-STANDARDS']
tags: ['standards', 'specifications', 'core']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Infrastructure Engineering Standards

> **Authority:** CP-027  
> **Status:** ACTIVE  
> **Updated:** 2026-09-05

## 1. Resource Naming Conventions
- **Hosts:** `HOST-<SYSTEM>-<ROLE>-<INDEX>` (e.g., `HOST-MAC-STUDIO-001`)
- **Devices:** `DEV-<TYPE>-<NAME>-<INDEX>` (e.g., `DEV-DRIVE-LACIE-4TB`)
- **Services:** `SRV-<NAME>-<INDEX>` (e.g., `SRV-NEO4J-001`)
- **Volumes:** `VOL-<HOST>-<NAME>` (e.g., `VOL-STUDIO-LACIE`)
- **Registries:** `REG-<DOMAIN>-<INDEX>` (e.g., `REG-COMPUTE-001`)

## 2. Port Allocation Standard
- Ports `3000-3099`: Web interfaces & developer portals.
- Ports `4000-4999`: API proxies & model routers (LiteLLM: 4000).
- Ports `5000-5999`: Database management & telemetry.
- Ports `6000-6999`: Vector stores & caching (Qdrant: 6333, Redis: 6379).
- Ports `7000-7999`: Graph database interfaces (Neo4j: 7474, 7687).
- Ports `20000-20999`: Proprietary mesh gateways (OmniRoute: 20128).
- Ports `52000-52999`: Native ML inference runtimes (exo: 52415).

## 3. Git & Configuration Standards
- All changes must be verified through `git status && git diff`.
- No credentials, tokens, or plain private keys may ever be committed.

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
