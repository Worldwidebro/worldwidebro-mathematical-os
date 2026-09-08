---
id: DOC-MAINT-001
aliases: ['MAINTENANCE']
tags: ['maintenance', 'operations', 'sysadmin']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Maintenance Windows & Reboot Procedures

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Maintenance Schedule
- **Standard Maintenance Window:** Sundays 02:00–04:00 UTC.
- Sequence: Backup verification -> Docker graceful stop -> OS updates -> Host reboot -> Docker healthcheck verification.

## 2. Connected Documents
- Patch Management: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/PATCH-MANAGEMENT|PATCH-MANAGEMENT.md]]
- Runbooks: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/RUNBOOKS|RUNBOOKS.md]]
- Disaster Recovery: [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|RESILIENCE.md]]
