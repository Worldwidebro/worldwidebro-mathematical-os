---
id: PORTAL-SCRIPTS-001
title: "scripts — Autonomous Automation & Pipeline Utilities"
aliases: ["scripts", "Automation Scripts", "Pipeline Utilities"]
tags: ["scripts", "python", "automation", "pipelines", "neo4j", "ontologies"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[CLAUDE]] | [[56-ENGINEERING/README|56-ENGINEERING]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[_CLI/README|_CLI Gateway]]

# scripts — Autonomous Automation & Pipeline Utilities

> **Authority:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|Infrastructure Control Plane (CP-027)]]  
> **Runtime Environment:** Python 3.11+ / Neo4j Bolt / FastMCP  
> **Status:** 🟢 ACTIVE — Production Utilities

---

## 1. Directory Overview

The `scripts/` directory provides high-throughput automation scripts for ontology compilation, Neo4j knowledge graph ingestion, capability extraction, and automated crosswalk generation across the 700+ ventures and 35 business sectors.

---

## 2. Active Production Scripts

| Script | Purpose | Connected Systems |
|---|---|---|
| `ingest_canonical_to_neo4j.py` | Ingests canonical YAML registries into Neo4j graph nodes & edges | [[_REGISTRIES/CANONICAL/README|Canonical Registries]] → [[07-ONTOLOGY/README|Neo4j]] |
| `map_technical_capabilities.py` | Extracts and indexes technical capabilities from codebase ASTs | [[14-CAPABILITIES/README|14-CAPABILITIES]] |
| `extract_manifest_dependencies.py` | Parses `package.json`, `requirements.txt`, `Cargo.toml` | [[13-REPOSITORIES/README|13-REPOSITORIES]] |
| `heal_sector_taxonomy_and_starthere.py` | Re-indexes sector taxonomies and validates navigation breadcrumbs | [[SECTORS/README|SECTORS Gateway]] |
| `build_45_ontologies_crosswalk.py` | Compiles the unified crosswalk between business domains and ontologies | [[07-ONTOLOGY/45-ONTOLOGIES-MASTER|45 Ontologies Master]] |

---

## 3. Usage & Execution Protocols

```bash
# Ingest all canonical registries into Neo4j
python3 scripts/ingest_canonical_to_neo4j.py

# Recompile domain crosswalks
python3 scripts/build_45_ontologies_crosswalk.py
```

---

## 4. Upstream & Downstream Connections

- **Upstream:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] | [[56-ENGINEERING/README|56-ENGINEERING]]
- **Downstream:** [[_REGISTRIES/README|_REGISTRIES]] | [[_PIPELINES/README|_PIPELINES]] | [[_INFRASTRUCTURE/README|_INFRASTRUCTURE]]
