---
id: DOC-ASSET-DISP-001
aliases: ['ASSET-DISPOSAL']
tags: ['security', 'compliance', 'disposal']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Secure Asset Disposal & Data Sanitization

> **Authority:** CP-027 & CP-028  
> **Standard:** NIST SP 800-88 Rev 1 (Guidelines for Media Sanitization)  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Sanitization Mandates
- Internal Apple Silicon APFS volumes cryptographically erased via macOS Erase All Content and Settings (APFS key destruction).
- External drives (LaCie 4TB, T7 Shield) sanitized with multi-pass zero fill or hardware-level NVMe Secure Erase before transfer or disposal.

## 2. Connected Documents
- Decommissioning: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/DECOMMISSIONING|DECOMMISSIONING.md]]
- Security Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECURITY-INFRASTRUCTURE|SECURITY-INFRASTRUCTURE.md]]
- Lifecycle Overview: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-LIFECYCLE|INFRASTRUCTURE-LIFECYCLE.md]]
