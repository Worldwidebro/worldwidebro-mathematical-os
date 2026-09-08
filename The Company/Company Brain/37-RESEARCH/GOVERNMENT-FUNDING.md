---
id: RES-FUND-001
title: "GOVERNMENT-FUNDING — Federal Grants, Contracts & SBIR Opportunities"
tags: [research, funding, grants, sbir, sttr, sam-gov, capital]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[37-RESEARCH/README|37-RESEARCH]] | [[24-FINANCE/24-FINANCE|Finance]] | [[23-VENTURES/23-VENTURES|Ventures]]

# GOVERNMENT-FUNDING.md — Federal Grants, Contracts & Procurement Intelligence

> **Authority:** Capital & Legal Control Plane (CP-020 / CP-031)  
> **Feeds:** SBIR/STTR (`SRC-SBIR`), Grants.gov (`SRC-GRANTS`), USAspending (`SRC-USASPENDING`), SAM.gov  
> **Purpose:** Non-dilutive capital acquisition, government contracting, and public procurement opportunities for Company Brain ventures.

---

## 1. The Federal Funding Engine

```text
  AGENCY (DoD, NIH, NSF, DoE, DOT)
     │
     ▼
  PROGRAM (SBIR / STTR / Discretionary Grant / RFP)
     │
     ▼
  SOLICITATION / TOPIC (Open contract or grant opportunity)
     │
     ▼
  TECHNOLOGY / DOMAIN (e.g. Autonomous Logistics, Workforce Automation, AI Verification)
     │
     ▼
  VENTURE MATCH (Filtered against Company Brain Venture Registry)
     │
     ▼
  APPLICATION / PROPOSAL (Authored via Hermes / Specialized Agents)
     │
     ▼
  AWARD / CONTRACT (Non-dilutive capital into operating account)
```

---

## 2. Agency Relevance Matrix

| Federal Agency | Primary Programs | Target Ventures | Grant/Contract Types |
| :--- | :--- | :--- | :--- |
| **Department of Transportation (DOT)** | University Transportation Centers, ITS Solicitations | **`LT-005` & `LT-011`** | Intelligent transportation systems, route efficiency, fleet emissions reduction |
| **National Institutes of Health (NIH)** | SBIR Phase I/II (NIGMS, NCI) | **`LT-005` (Medical Courier)** | Biological specimen transport integrity, cold-chain monitoring, HIPAA compliance |
| **Department of Labor (DOL)** | Workforce Innovation & Opportunity (WIOA) | **`OPS-001` (Staffing)** | Automated apprentice tracking, blue-collar candidate credentialing platforms |
| **National Science Foundation (NSF)** | America's Seed Fund (TIP Directorate) | **OmniRoute / Company Brain** | Multi-agent orchestration, distributed edge AI, bitemporal knowledge graphs |
| **Small Business Administration (SBA)** | 8(a) Business Development, HUBZone | All OpCos | Small business prime contractor set-asides, direct-award sole-source contracts |

---

## 3. SBIR / STTR Tracking Pipeline (`SRC-SBIR`)

### Phase Mechanics
- **Phase I (Feasibility):** $50,000 to $300,000 (6-12 months) — Proving technical feasibility.
- **Phase II (Prototype Development):** $750,000 to $2,000,000 (24 months) — Building working software/hardware.
- **Phase III (Commercialization / Sole-Source):** Unlimited non-SBIR federal funding or private revenue. Can receive non-competitive sole-source federal procurement contracts based on Phase I/II work.

### Automated Scraping & Solicitations Ingestion
```python
# API Ingestion Target: https://api.sbir.gov/v1/solicitations.json
# Auto-matches keywords (logistics, scheduling, multi-agent, staffing, routing)
# against canonical venture requirements in CAPABILITY_REGISTRY.yaml
```

---

## 4. USAspending.gov & Federal Procurement (`SRC-USASPENDING`)

### Contract Intelligence
- **Tracking Expiring Contracts:** Identify 5-year federal vendor contracts coming up for recompete within 6–12 months.
- **Subcontracting Opportunities:** Match prime contractors (e.g. Lockheed, Booz Allen, Leidos) who are legally required to subcontract 20-30% of award value to small businesses.
- **Vendor Set-Asides:** Track opportunities restricted to Small Business (SB), Veteran-Owned (VOSB), and HUBZone vendors.

---

## Connected Entities & Portals
- **Master Research OS:** [[37-RESEARCH/RESEARCH-OS]]
- **Source Registry:** [[37-RESEARCH/SOURCE-REGISTRY]]
- **Venture Capital & Capital Layer:** [[24-FINANCE/24-FINANCE]]
- **Opportunities Engine:** [[37-RESEARCH/OPPORTUNITIES]]
