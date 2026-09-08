---
id: KNOW-AWE-001
title: "Awesome Lists — Curated Knowledge Repositories"
aliases: ["Awesome-Lists", "Awesome Lists", "09-KNOWLEDGE/Awesome-Lists", "External Curated Repositories"]
tags: ["knowledge", "awesome-lists", "external-capabilities", "ecosystem", "catalog"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]] | [[14-CAPABILITIES/CAPABILITIES_INDEX|CAPABILITIES_INDEX]] | [[_REGISTRIES/README|Registries Hub]] | [[REALITY]]

# Awesome Lists: Curated Knowledge & Capability Universe

> **Authority:** Knowledge Architecture (CP-009) & Capability Supply Chain  
> **Source Registry:** [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml|EXTERNAL_CAPABILITY_UNIVERSE.yaml]]  
> **Status:** ACTIVE — Indexed & Verified (2026-09-06)

---

## 1. Overview
Within Company Brain, **Awesome Lists** represent verified, community-curated directories of open-source libraries, frameworks, architectures, and datasets. They serve as our first fallback and solution discovery index when an internal venture or autonomous agent encounters an unmapped capability need.

---

## 2. Core Curated Indexes & Supply Chain

| Curated Stream | Primary Upstream Repository | Purpose & Utilization |
|:---|:---|:---|
| **Awesome Ecosystem Master** | `sindresorhus/awesome` (58k★) | Top-level solution discovery layer across all software disciplines |
| **External Capability Universe** | [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml|EXTERNAL_CAPABILITY_UNIVERSE.yaml]] | 904 Wikidata-grounded external capability supply chain nodes |
| **Awesome Self-Hosted** | `awesome-selfhosted/awesome-selfhosted` | Local-first, private cloud, and air-gapped infrastructure candidates |
| **Awesome Python / MLX** | `vinta/awesome-python` | Machine learning, data extraction, and Mac Apple Silicon tooling |
| **Awesome MCP Servers** | `punkpeye/awesome-mcp-servers` | Extensible Model Context Protocol tools for Antigravity and Claude |

---

## 3. Querying & Capability Gap Resolution
When an agent is tasked with building or discovering a tool:
1. **Internal Cache:** Query [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|Neo4j (:7687)]] for existing internal implementations (`177 code-bearing repos`).
2. **Capability Solution Matrix:** Cross-reference [[14-CAPABILITIES/CAPABILITY_SOLUTION_MATRIX.json|CAPABILITY_SOLUTION_MATRIX.json]] (`CAP-001` through `CAP-300`).
3. **Awesome Lists Search:** Use [[09-KNOWLEDGE/Query-Engine|Query Engine]] to semantically match requirements against cached Awesome List README vectors in [[10-MEMORY/10-MEMORY|Qdrant (:6333)]].
4. **Adoption Decision:** Record decision in [[_REGISTRIES/CANONICAL/CAPABILITY_GAP_MATRIX.yaml|CAPABILITY_GAP_MATRIX.yaml]] with verdict `ADOPT`, `EXTRACT`, or `IGNORE`.

---

## 4. Connected Navigation
- Knowledge Gateway: [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]]
- Query Engine: [[09-KNOWLEDGE/Query-Engine|Query Engine]]
- Relational Graph: [[09-KNOWLEDGE/Neo4j|Neo4j Graph Database]]
- World Model: [[09-KNOWLEDGE/Utopia-World-Model|Utopia Enterprise World Model]]
- Rollout Roadmap: [[50-MASTER-CONTROL/INSTALLATION_PHASES|INSTALLATION_PHASES.md (Phase 3)]]
- External Capability Inventory: [[_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md]]
