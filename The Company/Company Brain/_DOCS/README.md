---
id: PORTAL-DOCS-HELPER-001
title: "_DOCS — System Documentation, Architecture & Reference Gateway"
aliases: ["_DOCS", "_DOCS/README", "System Docs", "Architecture Docs"]
tags: ["docs", "architecture", "guides", "procedures", "reference", "api"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[_DOCS/architecture|System Architecture Master]] | [[CLAUDE]] | [[REALITY]]

# _DOCS — System Documentation, Architecture & Reference Gateway

> **Authority:** System Architecture Control Plane ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-027]])  
> **Master Architecture Gateway:** [[_DOCS/architecture|architecture.md]]  
> **Status:** 🟢 ACTIVE — Documentation Portal (2026-09-06)

---

## 1. Executive Summary

The **`_DOCS/`** directory provides technical architecture specifications, developer guides, operating procedures, and API references for Company Brain:

```text
_DOCS/
├── architecture.md     # Master System Architecture Gateway
├── architecture/       # Detailed component diagrams and subsystem deep dives
├── guides/             # Developer onboarding and operation tutorials
├── procedures/         # Standard Operating Procedures (SOPs) and runbooks
├── api/                # Internal API specifications and protocol definitions
└── reference/          # Hardware specs, network configs, and cheat sheets
```

---

## 2. Core Documentation Links

### Architecture & Logic Layers
- **Logic Architecture Framework**: [[_DOCS/LOGIC-ARCHITECTURE-FRAMEWORK.md]] — 72 logic layers, 12 domains, autonomous loop patterns, control plane mapping
- **Logic Layers Registry**: [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml|Master Registry]] — Queryable registry of all 72 logics mapped to domains, control planes, agents
- **Master Architecture**: [[_DOCS/architecture|architecture.md]] — Covers all 50 numbered domains, 7 control planes, 10 cognitive pipelines, and hardware topology

### Knowledge & Ontology
- **Typed Wikilinks Guide**: [[_DOCS/TYPED-WIKILINKS-GUIDE.md]] — Relationship-typed markdown syntax (relationship::[[Target]]), 15 relationship families, markdown-to-RDF mapping
- **Company Brain Ontology (RDF/XML)**: [[_ONTOLOGY/COMPANY-BRAIN-ONTOLOGY.xml]] — Master machine-readable ontology with entity types, relationships, domains, control planes
- **Research Intelligence Layer**: [[_ONTOLOGY/RESEARCH-INTELLIGENCE-LAYER.xml]] — Research entity types, relationships, evidence hierarchy (11 levels), adoption states

### Pipelines & Integration
- **Graph Ingestion Pipeline**: [[_PIPELINES/GRAPH-INGESTION-PIPELINE.md]] — 10-stage pipeline from Markdown → XML/RDF → Neo4j, with Python examples and query patterns
- **Research Intelligence Operations**: [[42-RESEARCH-INTELLIGENCE/README.md]] — Research-to-revenue pipeline, 20 research sections, research agent workflows

### Infrastructure & Runtime
- **Hardware & Runtime Reality**: [[CLAUDE.md]]
- **Operational Infrastructure**: [[_INFRASTRUCTURE/README]]
- **FastMCP Tooling**: [[_MCP/README]]
- **CLI Utilities**: [[_CLI/README]]

## _DOCS Document Index

- [[_DOCS/AGENTS_DISCOVERY_INVOCATION_GUIDE|AGENTS_DISCOVERY_INVOCATION_GUIDE]]
- [[_DOCS/COMPLETE-ENTERPRISE-OS-ARCHITECTURE|COMPLETE-ENTERPRISE-OS-ARCHITECTURE]]
- [[_DOCS/WIKI-PAGES-50-MASTER-LIST|WIKI-PAGES-50-MASTER-LIST]]
- [[_DOCS/WORLDWIDEBRO-COMPLETE-ARCHITECTURE|WORLDWIDEBRO-COMPLETE-ARCHITECTURE]]
