---
id: DOC-COST-OPT-001
aliases: ['COST-OPTIMIZATION', 'Infrastructure Optimization']
tags: ['finops', 'optimization', 'efficiency', 'cogs']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Cost Optimization Playbooks

> **Authority:** CP-020 & CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Core Optimization Strategies
1. **Local-First Inference Priority:** Route coding and analytical reasoning to Mac Studio M4 Max native MLX (`exo` on `:52415`) and Ollama (`:11434`), cutting third-party cloud API costs by 75%+.
2. **Structural Token Compression:** Utilize AST pruning and context compression to minimize context bloat before sending prompts to LiteLLM.
3. **Storage Tiering:** Offload cold backups and historical database dumps to LaCie 4TB and Samsung T7 Shield external drives, avoiding expensive cloud object storage fees.
4. **Container Memory Trimming:** Enforce strict Docker memory limits to prevent macOS memory pressure and swapping.

## 2. Connected Documents
- FinOps Overview: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/FINOPS|FINOPS.md]]
- Unit Cost Metrics: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/UNIT-COST|UNIT-COST.md]]
- Technical Debt Remediation: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/TECHNICAL-DEBT|TECHNICAL-DEBT.md]]
- Operating Budget: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-BUDGET|INFRASTRUCTURE-BUDGET.md]]
