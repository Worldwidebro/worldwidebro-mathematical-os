# CAMPAIGN-TAXONOMY — Canonical Identifiers & Schema Taxonomy

> **Canonical Document ID:** `DOC-TAX-CAM-001`  
> **Authority:** Knowledge Architecture (CP-008 / CP-027)  
> **Status:** ACTIVE TAXONOMY STANDARD

---

## 1. Canonical Prefix System

All campaign entities in Company Brain are assigned immutable, machine-readable identifiers registered in [`_REGISTRIES/ID_REGISTRY.yaml`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES/ID_REGISTRY.yaml):

```text
CAM-001 (Campaign)
  ├── OBJ-001 (Objective)
  ├── AUD-001 (Audience)
  │     ├── SEG-001 (Segment)
  │     └── PER-001 (Persona)
  ├── PROB-001 (Problem)
  ├── OFF-001 (Offer)
  ├── MSG-001 (Message)
  ├── CTA-001 (Call to Action)
  ├── CHN-001 (Channel)
  ├── CRE-001 (Creative Concept)
  │     └── AST-001 (Asset)
  ├── FUN-001 (Funnel)
  │     └── PG-001 (Landing Page)
  ├── EXP-001 (Experiment)
  │     └── HYP-001 (Hypothesis)
  ├── MET-001 (Metric)
  │     └── KPI-001 (KPI)
  ├── EVT-001 (Event)
  ├── UTM-001 (UTM Set)
  ├── BUD-001 (Budget)
  ├── RSK-001 (Risk)
  ├── LND-001 (Lead)
  ├── OPP-001 (Opportunity)
  ├── CUS-001 (Customer)
  ├── ORD-001 (Order)
  ├── REV-001 (Revenue)
  ├── EVD-001 (Evidence)
  └── LRN-001 (Learning)
```

---

## 2. Identifier Catalog & Definitions

| Prefix | Entity | Format | Description |
| :--- | :--- | :--- | :--- |
| **`CAM-`** | Campaign | `CAM-000001` | Sovereign coordinated go-to-market activity |
| **`CAMP-`** | Campaign Program | `CAMP-000001` | Multi-campaign strategic umbrella |
| **`OBJ-`** | Objective | `OBJ-000001` | Quantified singular target milestone |
| **`AUD-`** | Audience | `AUD-000001` | Target total addressable cohort |
| **`SEG-`** | Segment | `SEG-000001` | Homogeneous market subset |
| **`PER-`** | Persona | `PER-000001` | Detailed buyer or technical persona blueprint |
| **`INS-`** | Insight | `INS-000001` | Empirical customer or market observation |
| **`PROB-`** | Problem | `PROB-000001` | Quantified acute customer friction |
| **`OFF-`** | Offer | `OFF-000001` | Structured commercial value proposition |
| **`MSG-`** | Message | `MSG-000001` | Core copy narrative and value angle |
| **`POS-`** | Positioning | `POS-000001` | Category wedge and contrastive positioning |
| **`CTA-`** | Call to Action | `CTA-000001` | High-clarity user directive |
| **`CHN-`** | Channel | `CHN-000001` | Distribution or media delivery pathway |
| **`MED-`** | Media | `MED-000001` | Media specification and format |
| **`CRE-`** | Creative | `CRE-000001` | Creative concept or creative execution |
| **`AST-`** | Asset | `AST-000001` | Digital file, PDF, deck, image, or video |
| **`CNT-`** | Content | `CNT-000001` | Technical article, tear-down, or paper |
| **`FUN-`** | Funnel | `FUN-000001` | Multi-stage conversion architecture |
| **`PG-`** | Page | `PG-000001` | Web destination or landing page URL |
| **`EXP-`** | Experiment | `EXP-000001` | Controlled split test or causal study |
| **`HYP-`** | Hypothesis | `HYP-000001` | Falsifiable proposition under test |
| **`TST-`** | Test | `TST-000001` | Empirical test execution |
| **`MET-`** | Metric | `MET-000001` | Quantitative telemetry variable |
| **`KPI-`** | KPI | `KPI-000001` | Key Performance Indicator |
| **`EVT-`** | Event | `EVT-000001` | Conversion or behavioral telemetry event |
| **`UTM-`** | UTM | `UTM-000001` | Standardized parameter tracking taxonomy |
| **`BUD-`** | Budget | `BUD-000001` | Capital and resource allocation envelope |
| **`SPN-`** | Spend | `SPN-000001` | Realized expenditure record |
| **`ATR-`** | Attribution | `ATR-000001` | Fractional attribution credit record |
| **`RSK-`** | Risk | `RSK-000001` | Operational or enterprise risk entity |
| **`ASM-`** | Assumption | `ASM-000001` | Unverified operational assumption |
| **`DEP-`** | Dependency | `DEP-000001` | Critical operational prerequisite |
| **`APP-`** | Approval | `APP-000001` | Executive sign-off audit gate |
| **`OWN-`** | Owner | `OWN-000001` | Single-threaded accountable person |
| **`AGT-`** | Campaign Agent | `AGT-000001` | Autonomous subagent executing campaign role |
| **`LND-`** | Lead | `LND-000001` | Captured prospect record |
| **`OPP-`** | Opportunity | `OPP-000001` | Qualified commercial sales deal |
| **`CUS-`** | Customer | `CUS-000001` | Acquired transacting enterprise client |
| **`ORD-`** | Order | `ORD-000001` | Binding contract or statement of work |
| **`REV-`** | Revenue | `REV-000001` | Recognized cash deposit in escrow |
| **`EVD-`** | Evidence | `EVD-000001` | Empirical proof artifact or audit log |
| **`LRN-`** | Learning | `LRN-000001` | Post-campaign heuristic for Knowledge Core |
| **`SRC-`** | Source | `SRC-000001` | External provenance citation or document |
| **`CMP-`** | Competitor | `CMP-000001` | Competitor intelligence profile |
| **`BRD-`** | Brand | `BRD-000001` | Brand identity |
| **`PRD-`** | Product | `PRD-000001` | Product offering |
| **`VNT-`** | Venture | `VNT-000001` | Operating commercial venture |
| **`SITE-`**| Site | `SITE-000001`| Destination web domain property |
| **`URL-`** | URL | `URL-000001` | Specific digital resource location |

---

## 3. Master Links

- Master System: [[CAMPAIGNS/CAMPAIGN-OS]]
- ID Registry: [[_REGISTRIES/ID_REGISTRY.yaml]]
- Hierarchy: [[CAMPAIGNS/CAMPAIGN-HIERARCHY]]
- Classification: [[CAMPAIGNS/CAMPAIGN-CLASSIFICATION]]
