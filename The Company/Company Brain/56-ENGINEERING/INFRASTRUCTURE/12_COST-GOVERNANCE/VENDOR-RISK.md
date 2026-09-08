---
id: DOC-VEND-RSK-001
aliases: ['VENDOR-RISK']
tags: ['vendors', 'risk', 'lock-in']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Vendor Risk Assessment & Lock-In

> **Authority:** CP-020 & CP-028  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Vendor Lock-In Mitigations
- Zero proprietary API bindings: LiteLLM abstracts all LLM calls to standard OpenAI-compatible schemas.
- Zero cloud database lock-in: Neo4j, PostgreSQL, and Qdrant run 100% on local Docker volumes.

## 2. Connected Documents
- Vendor Exit: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/VENDOR-EXIT|VENDOR-EXIT.md]]
- Cloud Exit Strategy: [[56-ENGINEERING/INFRASTRUCTURE/05_CLOUD/CLOUD-EXIT|CLOUD-EXIT.md]]
- Risk Register: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-RISK-REGISTER|INFRASTRUCTURE-RISK-REGISTER.md]]
