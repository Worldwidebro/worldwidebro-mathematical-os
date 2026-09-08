---
id: DOC-DEP-RSK-001
aliases: ['DEPENDENCY-RISK']
tags: ['dependency', 'risk', 'supply-chain']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Upstream Dependency & Supply Chain Risks

> **Authority:** CP-027 & CP-028  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Supply Chain Vulnerabilities
- Risk: Malicious or breaking npm/pip package updates.
- Mitigation: Lockfiles committed, AST scanning prior to container build.

## 2. Connected Documents
- Dependency Registry: [[_REGISTRIES/infrastructure_dependency_registry.json|infrastructure_dependency_registry.json]]
- Starred Repos Analysis: [[_REGISTRIES/RECONCILIATION_2026_09_01/STARRED_REPOS_DEPENDENCY_ANALYSIS.json|STARRED_REPOS_DEPENDENCY_ANALYSIS.json]]
- Supply Chain Security: [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SUPPLY-CHAIN-SECURITY|SUPPLY-CHAIN-SECURITY.md]]
