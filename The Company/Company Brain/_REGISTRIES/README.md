---
id: PORTAL-REGISTRIES-001
aliases: ["REGISTRIES", "Master Registries Portal", "Canonical Registries Hub"]
tags: ["registries", "canonical", "inventory", "single-source-of-truth"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[07-ONTOLOGY/45-ONTOLOGIES-MASTER|ONTOLOGIES]]

# _REGISTRIES — Master System Registries Portal

> **Authority:** Infrastructure Control Plane (CP-027) & Knowledge Control Plane (CP-013)  
> **Purpose:** Authoritative single-source-of-truth portal indexing all 23 machine-readable JSON/YAML registries, 13 sub-registry directories, and canonical entity catalogs.

---

## 1. Sub-Registry Directories

| Subdirectory | Focus / Scope | Subdirectory Gateway |
|---|---|---|
| `CANONICAL/` | Canonical repositories, capabilities, and system inventories | [[_REGISTRIES/CANONICAL/README|CANONICAL Registries]] |
| `repositories/` | Verified code repositories, owned packages, and starred ecosystems | [[_REGISTRIES/repositories/README|Repositories Registry]] |
| `services/` | System daemons, background workers, and internal APIs | [[_REGISTRIES/services/README|Services Registry]] |
| `tools/` | Internal CLI tools, utility scripts, and automation hooks | [[_REGISTRIES/tools/README|Tools Registry]] |
| `integrations/` | External third-party API keys, webhooks, and integrations | [[_REGISTRIES/integrations/README|Integrations Registry]] |
| `coverage/` | Test suites, AST verification reports, and test coverage matrices | [[_REGISTRIES/coverage/README|Coverage Registry]] |
| `SHADOW_WORK/` | Background shadow tasks, deferred audits, and staging queues | [[_REGISTRIES/SHADOW_WORK/README|Shadow Work Registry]] |
| `control-points/` | The 38 architectural control points and decision boundaries | [[_REGISTRIES/control-points|Control Points]] |
| `agents/` | Metadata profiles for autonomous routing and execution agents | [[16-AGENTS/README|Agents Directory]] |
| `RECONCILIATION_2026_09_01/` | Universal portfolio reconciliation audits and import scripts | [[_REGISTRIES/RECONCILIATION_2026_09_01/COMPANY_BRAIN_AUDIT_REPORT|Audit Report]] |

---

## 2. Machine-Readable Infrastructure & Operational Registries

| Registry File | Type | Description | Link |
|---|---|---|---|
| `INFRASTRUCTURE_REGISTRY.yaml` | YAML | Canonical physical/virtual hardware inventory and models | [[_REGISTRIES/INFRASTRUCTURE_REGISTRY.yaml|INFRASTRUCTURE_REGISTRY.yaml]] |
| `infrastructure_registry.json` | JSON | Hardware host IP mappings and Tailscale mesh nodes | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]] |
| `infrastructure_dependency_registry.json` | JSON | Inter-service dependencies, database links, and network paths | [[_REGISTRIES/infrastructure_dependency_registry.json|infrastructure_dependency_registry.json]] |
| `infrastructure_cost_registry.json` | JSON | Monthly FinOps breakdown ($309/mo TCO) | [[_REGISTRIES/infrastructure_cost_registry.json|infrastructure_cost_registry.json]] |
| `infrastructure_risk_registry.json` | JSON | Single points of failure (SPOF) and disaster mitigation matrix | [[_REGISTRIES/infrastructure_risk_registry.json|infrastructure_risk_registry.json]] |
| `network_registry.json` | JSON | Port allocations, Tailscale CIDR, MagicDNS, and ingress rules | [[_REGISTRIES/network_registry.json|network_registry.json]] |
| `database_registry.json` | JSON | PostgreSQL, Neo4j, Qdrant, and Redis connection topologies | [[_REGISTRIES/database_registry.json|database_registry.json]] |
| `storage_registry.json` | JSON | APFS internal SSDs, LaCie 4TB HDD, and Samsung T7 Shield | [[_REGISTRIES/storage_registry.json|storage_registry.json]] |
| `cloud_registry.json` | JSON | Vercel edge deployments (95 sites), GitHub, and multi-cloud exits | [[_REGISTRIES/cloud_registry.json|cloud_registry.json]] |
| `container_registry.json` | JSON | Active Docker containers on `macstudio` daemon | [[_REGISTRIES/container_registry.json|container_registry.json]] |
| `service_registry.json` | JSON | Running background processes, FastMCP bridge, and MLX exo | [[_REGISTRIES/service_registry.json|service_registry.json]] |
| `LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml` | YAML | Benchmarks, quantization levels, and 4-tier fallback rules | [LLM Hardware Registry](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml) |
| `ventures-by-sector.yaml` | YAML | 722 ventures classified across 35 vertical business sectors | [[_REGISTRIES/ventures-by-sector.yaml|ventures-by-sector.yaml]] |
| `repositories-by-sector.yaml` | YAML | 893 owned repositories mapped across 35 vertical business sectors | [[_REGISTRIES/repositories-by-sector.yaml|repositories-by-sector.yaml]] |
| `external-capabilities-by-sector.yaml` | YAML | 904 starred repositories (31.3M+ stars) mapped across 35 vertical business sectors | [[_REGISTRIES/external-capabilities-by-sector.yaml|external-capabilities-by-sector.yaml]] |
| `agents-by-sector.yaml` | YAML | 18 specialized agent archetypes mapped across 35 vertical business sectors | [[_REGISTRIES/agents-by-sector.yaml|agents-by-sector.yaml]] |
| `control-planes-by-sector.yaml` | YAML | Mapping of control planes to vertical sectors | [[_REGISTRIES/control-planes-by-sector.yaml|control-planes-by-sector.yaml]] |
| `capabilities-by-sector.yaml` | YAML | Capability solution mappings by business sector | [[_REGISTRIES/capabilities-by-sector.yaml|capabilities-by-sector.yaml]] |
| `capability_id_registry.yaml` | YAML | Authoritative ID catalog for all capabilities | [[_REGISTRIES/capability_id_registry.yaml|capability_id_registry.yaml]] |
| `resource-linking.yaml` | YAML | Entity relationship and resource crosswalk definitions | [[_REGISTRIES/resource-linking.yaml|resource-linking.yaml]] |
| `CAMPAIGN-OBJECTIVE-REGISTRY.json` | JSON | Target conversions and revenue metrics for marketing | [[_REGISTRIES/CAMPAIGN-OBJECTIVE-REGISTRY.json|CAMPAIGN-OBJECTIVE-REGISTRY.json]] |
| `EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md` | Markdown | Master catalog of all 904 external starred supply chain repositories | [[_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md|EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md]] |
| `STARRED_REPOS_DEPENDENCY_ANALYSIS.json` | JSON | Dependency analysis of 903 starred open-source libraries | [[_REGISTRIES/RECONCILIATION_2026_09_01/STARRED_REPOS_DEPENDENCY_ANALYSIS.json|STARRED_REPOS_DEPENDENCY_ANALYSIS.json]] |
