---
id: DOC-TECH-DEBT-001
aliases: ['TECHNICAL-DEBT']
tags: ['engineering', 'refactoring', 'technical-debt', 'pruning']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Technical Debt Audit & Clutter Remediation

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Active Technical Debt Registry
- **Stale Docker Containers:** Eliminated 2026-09-05 (resolved duplicate compose stacks down to canonical `civos_*`).
- **Orphaned Repositories:** 618 venture placeholder repos scheduled for archival into `_ARCHIVE/` or prune list.
- **Disconnected Observability:** LiteLLM Langfuse callback configuration pending.

## 2. Connected Documents
- Decommissioning Ledger: [[KILL-LIST]]
- Prohibited Activities: [[STOP-DOING]]
- Cost Optimization: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/COST-OPTIMIZATION|COST-OPTIMIZATION.md]]
- Historical Changes: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-CHANGELOG|INFRASTRUCTURE-CHANGELOG.md]]
