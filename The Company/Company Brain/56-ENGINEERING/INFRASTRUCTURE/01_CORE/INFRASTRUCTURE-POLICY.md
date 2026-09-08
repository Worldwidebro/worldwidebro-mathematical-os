---
id: DOC-01-POL-001
aliases: ['INFRASTRUCTURE-POLICY']
tags: ['policy', 'governance', 'directives', 'core']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Infrastructure Policy & Governance Directives

> **Authority:** CP-027  
> **Standard:** NIST SP 800-204C & NIST SP 800-207  
> **Status:** ACTIVE  
> **Updated:** 2026-09-05

## Policy Directives
1. **Zero Public Ingress Policy (POL-INFRA-001):** No host within the internal infrastructure network may expose unauthenticated open ports to the public Internet. All administrative and API access must route through encrypted Tailscale mesh tunnels or authenticated Cloudflare/Vercel edge gateways.
2. **Ephemeral Secret Injection (POL-INFRA-002):** Secrets must never reside in persistent plain text on disk or in repository commits. Secrets are fetched just-in-time from Bitwarden CLI (`bw`) into memory.
3. **Canonical Persistence Policy (POL-INFRA-003):** All production stateful data (Neo4j graph, Qdrant vectors, PostgreSQL databases) must reside on designated persistent storage volumes (`/Volumes/LaCie`) and never within ephemeral container write layers.
4. **No Duplicate Stacks (POL-INFRA-004):** No duplicate service containers (e.g., multiple Neo4j or Redis instances) may run concurrently on the same host unless explicitly designated as active-passive failover pairs.

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
