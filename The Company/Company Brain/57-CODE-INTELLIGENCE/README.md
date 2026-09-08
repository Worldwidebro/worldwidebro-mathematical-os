---
id: DOMAIN-57-GATEWAY
title: "57-CODE-INTELLIGENCE — Semantic Code Graph & AST Intelligence Domain"
aliases: ["57-CODE-INTELLIGENCE", "Code Intelligence Domain", "AST Intelligence"]
tags: ["code-intelligence", "graphify", "ast", "lsp", "repository-intelligence"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[13-REPOSITORIES/13-REPOSITORIES|13-REPOSITORIES]] | [[56-ENGINEERING/README|56-ENGINEERING]] | [[_PIPELINES/code-intelligence/README|Code Intel Pipeline]]

# 57-CODE-INTELLIGENCE — Semantic Code Graph & AST Intelligence Domain

> **Authority:** Code Intelligence & Quality Control Plane ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-027]])  
> **Primary Integration:** [[57-CODE-INTELLIGENCE/GRAFT_INTEGRATION|GRAFT_INTEGRATION.md]]  
> **Master Gateway:** [[57-CODE-INTELLIGENCE/57-CODE-INTELLIGENCE|57-CODE-INTELLIGENCE.md]]  
> **Status:** 🟢 ACTIVE — Semantic AST Hub (2026-09-06)

---

## 1. Executive Summary
The **Code Intelligence Domain** (`57-CODE-INTELLIGENCE`) builds and maintains semantic knowledge graphs across all 893 owned repositories and 904 external dependency repositories using AST parsing, LSP servers, Graphify, and tree-sitter.

---

## 2. Connected Subsystems
- **Graphify Knowledge Graph**: Managed via `graphify-out/` and `graphify update .`.
- **Pipeline Stage**: [[_PIPELINES/code-intelligence/README|Code Intelligence Pipeline (Stage 07)]].
- **LSP Indexing**: Governed by [[.agents/skills/lsp-index-engineer/SKILL|lsp-index-engineer]].
- **Repository Registry**: [[_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml]].
