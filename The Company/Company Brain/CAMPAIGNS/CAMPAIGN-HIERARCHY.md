# CAMPAIGN-HIERARCHY — Structural Hierarchy from Venture to Experiment

> **Canonical Document ID:** `DOC-HIE-CAM-001`  
> **Authority:** System Architecture (CP-027)  
> **Status:** ACTIVE SPECIFICATION

---

## 1. The 6-Level Hierarchy

Campaign entities are strictly nested to preserve traceability from holding company goals down to individual ad variations:

```text
LEVEL 1: HOLDING / ENTERPRISE (WorldwideBro / ORG-001)
   └── LEVEL 2: OPERATING VENTURE (VNT-001 / WorldwideBro Commercial)
         └── LEVEL 3: CAMPAIGN PROGRAM (CAMP-REV-2026-Q3: Enterprise Infrastructure Monetization)
               └── LEVEL 4: CAMPAIGN (CAM-001: Local AI & Repo Intelligence Audit)
                     ├── LEVEL 5: CAMPAIGN FLIGHT / CHANNEL (CHN-OUT-001: Outbound Sequence Wave 1)
                     │     └── LEVEL 6: EXPERIMENT / VARIANT (EXP-001: Cost Angle vs Security Angle)
                     └── LEVEL 5: CAMPAIGN FLIGHT / CHANNEL (CHN-LNK-001: LinkedIn Direct Outreach)
```

---

## 2. Inheritance Rules

1. **Budget Inheritance:** Child campaigns draw capital strictly from the parent program allocation.
2. **Policy Inheritance:** All flights and creative variants inherit brand safety, claim verification, and data privacy policies from Level 1.
3. **Attribution Rollup:** Telemetry from Level 6 experiments rolls up to Level 4 campaigns and aggregates into Level 2 venture revenue.

---

## 3. Master Links

- Master System: [[CAMPAIGNS/CAMPAIGN-OS]]
- Taxonomy: [[CAMPAIGNS/CAMPAIGN-TAXONOMY]]
- Registry: [[CAMPAIGNS/CAMPAIGN-REGISTRY]]
