---
id: PORTAL-TOOLS-001
title: "_TOOLS — Integrated Tooling & Local Knowledge Engines"
aliases: ["_TOOLS", "_TOOLS/README", "Integrated Tooling & Local Knowledge Engines"]
tags: [portal, tools]
status: ACTIVE
authority: "CP-001 / CP-027"
updated: 2026-09-12
---

[[STARTHERE]] | [[REALITY]] | [[INDEX]] | [[INDEX-DOMAINS-COMPLETE]]

# _TOOLS — Integrated Tooling & Local Knowledge Engines

> **Authority:** CP-001 / CP-027  
> **Status:** ACTIVE

## Overview
Developer tools and local repository intelligence engines coordinating code graphs, symbol-level blast-radius analysis, vector retrieval, and canonical entity graphs across WorldwideBro / Company Brain.

---

## 1. Unified Repository & Knowledge Engine Stack

| Tool | Engine / Technology | Primary Use Case | Invocation Command |
| :--- | :--- | :--- | :--- |
| **GitNexus** | LadybugDB + AST Graph + Cypher | Symbol context, call-flow graphs, blast radius / impact analysis across venture repos | `scripts/gitnexus <command>` |
| **gbrain** | PGLite (PostgreSQL in WASM/Node) + BM25 | Venture records, underwriting metrics, markdown document knowledge graph | `scripts/gbrain <command>` |
| **gstack** | Playwright + Chromium + KaTeX | Publication-grade vector PDF compilation and sprint review automation | `scripts/make-pdf <input.md>` |
| **Graphify** | NetworkX + AST Extractor | Multi-domain repository knowledge graph & community detection | `graphify query "<question>"` |
| **Repomix** | Token-optimized repo packer | Monorepo and code context bundling for agent context windows | `repomix --style xml` |
| **Madge** | AST module resolver | Polyglot module dependency trees & circular dependency auditing | `madge --circular <path>` |
| **Neo4j** | Graph DB (`100.87.214.70:7687`) | Master enterprise ontology: 3,440 nodes & 91,113 edges | `scripts/sync_gbrain_to_neo4j.py` |
| **SocratiCode** | Hybrid Semantic Graph (`STAR-1097`) | 40M+ LOC enterprise codebase intelligence & call flows | Starred capability #714 |

---

## 2. GitNexus Code Graph Usage

All 8 active venture codebases are indexed under `scripts/gitnexus`:
- `repos/lt-005-medical-courier-dispatch` (3,873 symbols, 4,650 edges)
- `repos/callcenter` (875 symbols, 1,036 edges)
- `repos/con-001-ace-construction` (1,309 symbols, 1,857 edges)
- `repos/lt-011-dispatch-software` (1,308 symbols, 1,444 edges)
- `repos/ops-staff-001-staffing` (4,756 symbols, 8,296 edges)
- `repos/re-001-worldwidebro-holdings` (1,362 symbols, 1,646 edges)
- `repos/worldwidebro-venture-portal` (570 symbols, 850 edges)
- `repos/worldwidebro-marketing-os` (51 symbols, 42 edges)

### Common Commands
```bash
# List all indexed repositories and status
scripts/gitnexus list

# Blast radius analysis: what breaks if you change a symbol
scripts/gitnexus impact <symbol_name> -r <repo_name>

# 360-degree symbol context: callers, callees, processes
scripts/gitnexus context <symbol_name> -r <repo_name>

# Trace shortest path between two symbols
scripts/gitnexus trace <from_symbol> <to_symbol> -r <repo_name>

# Execute Cypher graph query directly against repository AST
scripts/gitnexus cypher "MATCH (n:Function) RETURN n.name, n.filePath LIMIT 25" -r <repo_name>

# Re-index a repo after code modifications
scripts/gitnexus analyze --index-only "repos/<target-repo>"
```

---

## 3. Repomix & Madge Code Auditing

```bash
# Pack a codebase into a single AI-digestible XML context
repomix --include "src/**/*.ts" --output repomix-context.xml

# Audit circular dependencies in a venture repo
madge --circular repos/ops-staff-001-staffing/src
```

---

## 4. gbrain & Neo4j Knowledge Ingestion

```bash
# Query underwriting and venture metrics in gbrain
scripts/gbrain query "medical courier revenue model"

# Synchronize gbrain nodes to live Neo4j instance on Mac Studio
python3 scripts/sync_gbrain_to_neo4j.py
```

