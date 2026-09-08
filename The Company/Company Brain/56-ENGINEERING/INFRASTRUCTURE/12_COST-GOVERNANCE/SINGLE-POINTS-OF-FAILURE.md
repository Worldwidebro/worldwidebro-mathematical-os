---
id: DOC-SPOF-001
aliases: ['SINGLE-POINTS-OF-FAILURE', 'SPOF']
tags: ['resilience', 'spof', 'risk']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Single Points of Failure (SPOF) Deep Dive

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Identified Single Points of Failure
1. **Physical Host:** Mac Studio M4 Max is single host for production Neo4j, Qdrant, and PostgreSQL databases.
2. **External Drive:** LaCie 4TB drive is single target for active database volumes.
3. **Human Factor:** Solo operator bus factor 1.

## 2. Connected Documents
- Resilience SPOF Analysis: [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/SINGLE-POINTS-OF-FAILURE|11_RESILIENCE SPOF]]
- Risk Register: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-RISK-REGISTER|INFRASTRUCTURE-RISK-REGISTER.md]]
- Disaster Recovery: [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/DISASTER-RECOVERY|DISASTER-RECOVERY.md]]
