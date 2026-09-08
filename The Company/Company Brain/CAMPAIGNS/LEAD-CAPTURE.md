# LEAD-CAPTURE — Capture Mechanisms & Enrichments

> **Canonical Document ID:** `DOC-LCP-CAM-001`  
> **Authority:** Growth Operations (CP-006)  
> **Status:** ACTIVE SPECIFICATION

---

## 1. Automated Lead Capture & Enrichment

When a lead books a call or replies positively:
1. Email address is parsed and sent to Apollo / Clearbit API for real-time firmographic enrichment.
2. GitHub repository public metadata is queried to calculate estimated codebase size and primary languages.
3. Opportunity record is automatically created in `_REGISTRIES/CAMPAIGN-REGISTRY.json`.

---

## 2. Master Links

- Funnels: [[CAMPAIGNS/FUNNELS]]
- Qualification: [[CAMPAIGNS/QUALIFICATION]]
