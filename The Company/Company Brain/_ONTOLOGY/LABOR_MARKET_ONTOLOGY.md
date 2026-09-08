---
id: ONT-LABOR-001
title: "Labor Market & Workforce Capability Ontology (12 Layers)"
aliases: ["Labor Market Ontology", "Workforce Ontology", "Taxonomy", "Labor Taxonomy", "OPS-001 Ontology", "ONT-LABOR-001"]
tags: ["ontology", "labor", "workforce", "taxonomy", "soc", "onet", "naics", "ops-001", "matching-engine"]
status: ACTIVE
authority: "System Architecture & Labor Market Control Plane (CP-028) / OPS-001"
updated: 2026-09-07
---

[[STARTHERE]] | [[INDEX]] | [[REALITY]] | [[23-VENTURES/OPS-001|OPS-001 (CareerOps)]] | [[05-PEOPLE/05-PEOPLE|ONT-012 (People)]] | [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|ONT-001 (Economic)]]

# Labor Market & Workforce Capability Ontology (v0.1)

> **Authority:** WorldwideBro / OPS-001 Staffing Operating System (OWN-PRIV-0008)  
> **Master Codebase:** [`repos/ops-staff-001-staffing`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing)  
> **Crosswalk:** Bridges [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|ONT-001 (Economic)]] and [[05-PEOPLE/05-PEOPLE|ONT-012 (People)]]  
> **Standards Alignment:** BLS SOC (2018), O*NET 28.0, NAICS 2022, BLS OEWS, ESCO v1.1  

---

## 1. Executive Philosophy & Grounded Architecture

In conventional staffing platforms, matching relies on **job titles** (e.g. "Software Engineer" vs. "Backend Developer" vs. "Application Developer"), leading to extreme friction, keyword guessing, and missed placements.

In **OPS-001**, the labor market is modeled as a computable directed bipartite graph decoupling titles from functional capability:

```text
LABOR MARKET GRAPH
│
├── INDUSTRY (NAICS 2-4 Digit)
│   └── SECTOR (NAICS 6-Digit)
│       └── OCCUPATION (BLS SOC 6-Digit / O*NET 8-Digit)
│           └── JOB FAMILY (Functional Cluster)
│               └── ROLE / TITLE (Marketplace Variant)
│                   ├── SKILLS (Hard, Soft, Technical, Tooling)
│                   ├── KNOWLEDGE (Domain & Procedural Rules)
│                   ├── EXPERIENCE (Proficiency & Track Record)
│                   ├── CREDENTIALS (Licenses, Certifications, Clearances)
│                   ├── TASKS (Generalized & Detailed Activities)
│                   ├── TOOLS / TECHNOLOGIES (Software, Machinery)
│                   ├── RESPONSIBILITIES (Scope, Authority, Deliverables)
│                   └── REQUIREMENTS (Physical, Availability, Mobility)
│
├── EMPLOYER NODE
│   ├── Organization ID (UUID / Canonical Entity)
│   ├── Work Sites & Locations (Geo-Coordinates, Facility Type)
│   ├── Industry & Sector Codes (NAICS Verified)
│   ├── Workforce Demand (Headcount, Urgency, Shift Times)
│   ├── Open Job Orders (Structured Capability Requirements)
│   └── Billing Terms (MSA Signed, Rate Schedule, Net 15/30)
│
└── WORKER NODE (Talent Network)
    ├── Candidate ID (UUID / Identity Verified)
    ├── Primary & Secondary Occupations (SOC Mapped)
    ├── Verified Skills & Competencies (Weighted Taxonomy)
    ├── Experience Log (Years, Verified Roles, Quantified Metrics)
    ├── Active Credentials (License Numbers, Issuing Authority, Expiration)
    ├── Availability & Schedule (Shifts, Days, Notice Period)
    ├── Geolocation Preferences (Max Distance, Transportation Mode)
    ├── Target Compensation (Min Acceptable Pay Cents, Desired Pay Cents)
    └── Compliance Dossier (I-9 Eligibility, W-4, Drug Screen, FCRA)
```

---

## 2. Canonical Definitions in OPS-001

1. **Employer**: A commercial or institutional legal entity (`organizations`) requiring productive labor capability, possessing verified billing/creditworthiness, and executing a binding [[repos/ops-staff-001-staffing/contracts/MASTER-SERVICES-AGREEMENT.md|Master Services Agreement (MSA)]].
2. **Job (Job Order)**: A discrete, funded demand requisition (`job_orders`) specifying labor capability (occupation, required skills, credentials, minimum experience), shift schedule, work site, and bill/pay rates.
3. **Occupation**: An authoritative category of economic activity (BLS SOC / O*NET) defining standardized tasks, competencies, and labor market benchmarks regardless of idiosyncratic employer titles.
4. **Skill**: A discrete, demonstrable cognitive, technical, physical, or procedural competence (e.g. `SKILL-TRADES-001`: Conduit Bending; `SKILL-HC-001`: IV Therapy; `SKILL-TECH-001`: Distributed Systems).
5. **Worker (Candidate)**: An authenticated individual (`candidates`) possessing verified identity, right to work (Form I-9 / W-4), validated skill/credential profile, and explicit availability.

---

## 3. The 12 Discrete Layers

| Layer | Dimension | Definition | Authoritative Source / Format | Seed Example |
| :--- | :--- | :--- | :--- | :--- |
| **L01** | **Industry** | Macroeconomic classification | NAICS 2-Digit | `IND-CONST` (Construction - NAICS 23) |
| **L02** | **Sector** | Sub-industry domain | NAICS 4-6 Digit | `SEC-ELECTRICAL` (Electrical Contractors - NAICS 238210) |
| **L03** | **Occupation** | Standardized labor function | BLS SOC 6-Digit / O*NET | `OCC-TRADES-001` (Electrician - SOC 47-2111.00) |
| **L04** | **Job Family** | Related capability cluster | O*NET Job Family | `FAM-ELECTRICAL-POWER` (Electrical Installation & Wiring) |
| **L05** | **Role / Title** | Marketplace position name | Internal / Employer | Journeyman Commercial Electrician |
| **L06** | **Tasks** | Observable activities | O*NET DWA / Generalized Work | Run conduit, terminate switchgear, read schematics |
| **L07** | **Skills** | Technical & hard competencies | Granular Taxonomy UUID | `SKILL-TRADES-001` (Conduit Bending), `SKILL-TRADES-002` (NEC) |
| **L08** | **Knowledge** | Theoretical & regulatory | Curricular / Standards | National Electrical Code (NEC 2023), Arc Flash Safety |
| **L09** | **Credentials** | Verifiable licenses/certs | State Licensing Boards | `CRED-TRADES-001` (NC State Journeyman License), OSHA 30 |
| **L10** | **Experience** | Depth & track record | Years, Past Roles, Projects | 4+ years commercial installation, verifiable foreman ref |
| **L11** | **Work Conditions** | Environment & physical | Physical demands / Schedule | Indoors/Outdoors, lifts 50 lbs, standing 8h, Day Shift |
| **L12** | **Compensation** | Pay/Bill economics | BLS OEWS / Cent Pricing | Pay: $32.00/hr ($3,200c), Bill: $50.00/hr ($5,000c) [36% Margin] |

---

## 4. 8 High-Value Seed Sectors

OPS-001 restricts its initial liquidity sprint to 8 high-demand, high-margin sectors:

1. **Skilled Trades**: Commercial Electricians, HVAC Service Techs, Commercial Plumbers (`SEC-ELECTRICAL`, `SEC-HVAC`, `SEC-PLUMBING`).
2. **Transportation & Logistics**: CDL-A Drivers, Warehouse Supervisors, Logistics Coordinators (`SEC-LOGISTICS-OPS`).
3. **Healthcare**: Registered Nurses (RN), Certified Medical Assistants (CMA), Phlebotomists (`SEC-CLINICAL-NURSING`, `SEC-AMBULATORY`).
4. **Technology**: Full Stack Engineers, DevOps / Cloud SREs, Systems Architects (`SEC-SOFTWARE-DEV`, `SEC-CLOUD-INFRA`).
5. **Manufacturing & Industrial**: CNC Machinists, Industrial Maintenance Mechanics, Welders (`SEC-INDUSTRIAL-MFG`).
6. **Administrative & Clerical**: Executive Assistants, Operations Coordinators, Medical Schedulers (`SEC-ADMIN-OPS`).
7. **Sales & Business Development**: B2B Account Executives, SDRs, Field Sales Reps (`SEC-B2B-SALES`).
8. **Customer Service & Support**: Technical Support Specialists, Client Success Agents (`SEC-TECH-SUPPORT`).

---

## 5. Computable 6-Dimension Matching Engine

Matching in OPS-001 is evaluated via deterministic vector/attribute scoring:

$$\text{Match Score} = 0.25 S_{\text{occ}} + 0.30 S_{\text{skill}} + 0.15 S_{\text{exp}} + 0.10 S_{\text{cred}} + 0.10 S_{\text{loc}} + 0.10 S_{\text{comp}}$$

1. **Occupation Fit ($S_{\text{occ}}$, 25%)**: Exact SOC match = 100%; same family = 75%; same sector = 50%; unrelated = 0%.
2. **Skill Fit ($S_{\text{skill}}$, 30%)**: Percentage of required skills possessed by candidate: $\frac{|\text{Skills}_{\text{candidate}} \cap \text{Skills}_{\text{job}}|}{|\text{Skills}_{\text{job}}|}$.
3. **Experience Fit ($S_{\text{exp}}$, 15%)**: $\ge \text{Req}$ = 100%; within 1 year = 50%; $< \text{Req}-1$ = 0%.
4. **Credential Fit ($S_{\text{cred}}$, 10%)**: All mandatory licenses verified = 100%; partial = 50%; none = 0%.
5. **Location Fit ($S_{\text{loc}}$, 10%)**: Remote = 100%; same metro = 100%; willing to relocate = 75%; mismatch = 0%.
6. **Compensation Feasibility ($S_{\text{comp}}$, 10%)**: Job max $\ge$ Candidate min = 100%; gap $\le 10\%$ = 75%; gap $\le 20\%$ = 50%; gap $> 20\%$ = 0%.

---

## 6. Binding Contract & Compliance Foundation

Every placement is legally backed by executed contracts in `repos/ops-staff-001-staffing/contracts/`:
- **Client Master Services Agreement**: [`MASTER-SERVICES-AGREEMENT.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing/contracts/MASTER-SERVICES-AGREEMENT.md) (Net 15/30 terms, 1.5x overtime billing, direct hire conversion fees 20%-10%).
- **Worker Agreement**: [`WORKER-CONTRACTOR-AGREEMENT.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing/contracts/WORKER-CONTRACTOR-AGREEMENT.md) (W-2 contingent worker employment, timesheet submission rules, safety, NDA).
- **Rate Schedule Addendum**: [`RATE-SCHEDULE-ADDENDUM.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing/contracts/RATE-SCHEDULE-ADDENDUM.md) (Gross margin targeting 35-37%, payroll tax burden accounting: FICA 7.65%, FUTA 0.6%, SUTA 2.7%, Workers' Comp 3.5%).
- **Compliance Packet**: [`W4-I9-COMPLIANCE-PACKET.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing/contracts/W4-I9-COMPLIANCE-PACKET.md) (Form I-9 employment verification, W-4 withholding, FCRA background check consent).

---

## 7. Connected Systems & Cross-References

- **Venture Master**: [[23-VENTURES/OPS-001|23-VENTURES/OPS-001 (CareerOps Platform)]]
- **Foundational People Ontology**: [[05-PEOPLE/05-PEOPLE|05-PEOPLE (ONT-012)]]
- **Foundational Economic Ontology**: [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|ONT-001 (Economic Ontology)]]
- **Machine Schemas**: [`repos/ops-staff-001-staffing/schemas/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing/schemas)
- **Seed Taxonomy**: [`repos/ops-staff-001-staffing/taxonomy/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing/taxonomy)
- **12 Cold Call Sprint**: [`repos/ops-staff-001-staffing/CALL-TRACKING-TEMPLATE.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing/CALL-TRACKING-TEMPLATE.md)
- **Candidate Sourcing**: [`repos/ops-staff-001-staffing/CANDIDATE-SOURCING-PLAN.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing/CANDIDATE-SOURCING-PLAN.md)
- **Matching Engine Code**: [`repos/ops-staff-001-staffing/api/match-score.js`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/repos/ops-staff-001-staffing/api/match-score.js)
