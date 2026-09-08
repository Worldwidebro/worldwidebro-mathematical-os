---
id: REG-CANONICAL-HUB
title: "CANONICAL — Master System Registries & Golden Record Gateway"
aliases: ["CANONICAL", "_REGISTRIES/CANONICAL", "Golden Records Gateway", "Master Data Dictionary"]
tags: [registry, canonical, golden-record, repositories, capabilities, sites, vercel, dependencies]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[_REGISTRIES/README|Registries Hub]] | [[REALITY]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]]

# CANONICAL — Master System Registries & Golden Record Gateway

> **Authority:** System Architecture & Infrastructure Control Plane ([[50-MASTER-CONTROL/CONTROL_MATRIX|CP-027]])  
> **Master Operating Contract:** [[ANTIGRAVITY.md]] (Rule 6: Data Integrity — Never silently overwrite canonical registries)  
> **Location:** `_REGISTRIES/CANONICAL/`  
> **Status:** 🟢 ACTIVE — Canonical Source of Truth (2026-09-06)

---

## 1. Executive Overview
The `_REGISTRIES/CANONICAL/` directory is the authoritative golden record repository of Company Brain. It maintains the machine-readable ground truth across all 893 owned code repositories, 904 external capability supply chain dependencies, 700+ ventures, and production digital properties.

---

## 2. Canonical Datasets Inventory & Data Dictionary

| Canonical Dataset | Format | Size | Purpose & Scope | Upstream Subsystem | Primary Consumers |
|:---|:---|:---|:---|:---|:---|
| `REPOSITORY_REGISTRY.yaml` | YAML | 856 KB | Canonical registry of all **893 owned repositories** (`CB-REPO-000001` to `CB-REPO-000893`), including AST reality, branch status, primary languages, and sector assignments. | GitHub Ingestion | [[13-REPOSITORIES/13-REPOSITORIES|13-REPOSITORIES]] • [[56-ENGINEERING/README|56-ENGINEERING]] |
| `CAPABILITY_REGISTRY.yaml` | YAML | 16 KB | Master catalog of core system capabilities across all 35 operational sectors. | Capability Mapping | [[14-CAPABILITIES/CAPABILITIES_INDEX|14-CAPABILITIES]] • [[50-MASTER-CONTROL/CONTROL_MATRIX|Control Matrix]] |
| `EXTERNAL_CAPABILITY_UNIVERSE.yaml` | YAML | 10 KB | Catalog of **904 starred open-source packages** (31.3M+ stars) across 10 capability layers. | OSINT & GitHub Sync | [[_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY|External Universe]] • [[09-KNOWLEDGE/Awesome-Lists|Awesome Lists]] |
| `SITES_REGISTRY.yaml` | YAML | 27 KB | Canonical registry of verified digital properties, custom domains, routes, and web applications. | Domain & DNS Sync | [[_TEMPLATES/SITE_TEMPLATE|Site Template]] • [[23-VENTURES/23-VENTURES|23-VENTURES]] |
| `OWNED_REPO_CODE_REALITY.json` | JSON | 145 KB | AST-parsed physical code reality, exported classes, functions, and runnable entry points. | AST Ingestion | [[57-CODE-INTELLIGENCE/57-CODE-INTELLIGENCE|57-CODE-INTEL]] • [[42-EVALUATION/README|42-EVALUATION]] |
| `OWNED_REPO_DEPENDENCIES.json` | JSON | 113 KB | Comprehensive package manifest dependency graph across npm, pip, cargo, and go. | Graft & AST Parser | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/DEPENDENCY-RISK|Dependency Mgmt]] |
| `VERCEL_DEPLOYMENTS.json` | JSON | 15 KB | Active production serverless deployments (95 verified deployments), HTTP health, and runtime versions. | Vercel Edge API | [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|Deployment Engine]] |
| `VENTURE_CORRELATION_MATRIX.json` | JSON | 420 KB | Tripartite golden correlation matrix mapping **789 Ventures** to **605 GitHub Repos** and **95 Vercel Deployments**. | System Audit & Reconciler | [[23-VENTURES/README|23-VENTURES]] • [[_REGISTRIES/VENTURE_REGISTRY|VENTURE_REGISTRY]] |
| `CAPABILITY_GAP_MATRIX.yaml` | YAML | 5 KB | Deficit analysis identifying required technical capabilities lacking full internal implementation. | Gap Analysis | [[14-CAPABILITIES/solutions/CAP-001|Capabilities Solutions]] |
| `CAPABILITY_GAP_REPORT.yaml` | YAML | 1 KB | Summary report with priority mitigation paths and external OSS acquisition recommendations. | Architecture Review | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] |
| `UNTAGGED_REPOS.csv` | CSV | 116 KB | Inventory of unclassified repositories undergoing automated tagging and sector reconciliation. | Portfolio Scanner | [[_REGISTRIES/repositories/README|Repositories Registry]] |

---

## 3. Governance & Immutability Rules
1. **Append & Versioned Updates Only:** Canonical records must never be truncated or blindly overwritten. All updates must be validated by AST parsers or runtime probes.
2. **Tripartite Link Minimum:** Any entity defined in canonical registries must link to an Obsidian documentation page, a control point, and a parent sector.
3. **Reality Ground Truth:** In accordance with [[REALITY.md]], an entry in `REPOSITORY_REGISTRY.yaml` or `SITES_REGISTRY.yaml` outranks aspirational documentation.

---

## 4. Connected Subsystems
- **Master Registries Portal:** [[_REGISTRIES/README|Master Registries]]
- **Owned Repositories Catalog:** [[_REGISTRIES/OWNED_REPOSITORIES_INVENTORY|Owned Repositories Inventory]]
- **External Capabilities Universe:** [[_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY|External Universe Inventory]]
- **Engineering Hub:** [[56-ENGINEERING/README|56-ENGINEERING]]
- **Master Control Hub:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
