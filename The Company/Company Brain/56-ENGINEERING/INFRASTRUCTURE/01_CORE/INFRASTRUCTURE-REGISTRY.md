---
id: DOC-01-REG-001
aliases: ['INFRASTRUCTURE-REGISTRY']
tags: ['registry', 'schemas', 'contracts', 'core']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Infrastructure Registry Schema & Contracts

> **Authority:** CP-027  
> **Status:** ACTIVE  
> **Updated:** 2026-09-05

## Machine-Readable Registry System
All infrastructure data is canonically stored in JSON format under `_REGISTRIES/` to ensure full programmatic accessibility by AI agents, CLI scripts, and CI/CD pipelines:

1. `infrastructure_registry.json` — Master registry metadata and domain index.
2. `compute_registry.json` — Detailed compute units and hardware accelerators.
3. `host_registry.json` — Physical and virtual host configurations.
4. `device_registry.json` — Hardware devices and peripheral drives.
5. `storage_registry.json` — Disks, partitions, and persistent volume allocations.
6. `network_registry.json` — Tailscale mesh, LAN subnets, and bridges.
7. `dns_registry.json` — Split-DNS zones, MagicDNS, and public apex records.
8. `domain_registry.json` — Registered web domains and SSL properties.
9. `service_registry.json` — Managed and running service catalogs.
10. `container_registry.json` — Docker container inventory and status.
11. `database_registry.json` — Database instances, schemas, and ports.
12. `cloud_registry.json` — Cloud accounts, PaaS providers, and regions.
13. `deployment_registry.json` — 95 active deployed web endpoints.
14. `environment_registry.json` — Tiered environment specifications.
15. `endpoint_registry.json` — All active REST, gRPC, Bolt, and MCP endpoints.
16. `certificate_registry.json` — TLS/SSL certificates and expiration schedules.
17. `secret_registry.json` — Secret metadata and Bitwarden item pointers.
18. `backup_registry.json` — Backup jobs, retention limits, and schedules.
19. `recovery_registry.json` — Disaster recovery playbooks and RTO/RPO metrics.
20. `vendor_registry.json` — Hardware and service provider directory.
21. `infrastructure_cost_registry.json` — Detailed TCO and monthly operational costs.
22. `infrastructure_risk_registry.json` — Risk register with severity and mitigations.
23. `infrastructure_dependency_registry.json` — Graph edges connecting infrastructure components.

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
