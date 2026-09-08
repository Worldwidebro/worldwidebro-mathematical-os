# CAMPAIGN-ARCHITECTURE — System Architecture & Component Mapping

> **Canonical Document ID:** `DOC-ARC-CAM-001`  
> **Authority:** System Architecture (CP-027)  
> **Status:** ACTIVE ARCHITECTURAL SPECIFICATION

---

## 1. Multi-Layer Component Architecture

CAMPAIGN-OS is partitioned into 7 modular structural planes:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 1. STRATEGIC & GOVERNANCE PLANE                                        │
│    - North Star Alignment    - Objective Setting    - RACI Ownership   │
│    - Policy Constraints      - Stop-Rules           - Capital Limits   │
├────────────────────────────────────────────────────────────────────────┤
│ 2. MARKET & AUDIENCE PLANE                                             │
│    - TAM Segmentation        - ICP Blueprints       - Persona Stages   │
│    - Pain Telemetry          - Intent Catalysts     - Belief Mapping   │
├────────────────────────────────────────────────────────────────────────┤
│ 3. COMMERCIAL & PROPOSITION PLANE                                      │
│    - Grand Slam Offers       - Tiered Pricing       - Value Equations  │
│    - Risk Reversals          - Guarantee Contracts  - Urgency Triggers │
├────────────────────────────────────────────────────────────────────────┤
│ 4. CREATIVE & MESSAGING PLANE                                          │
│    - Core Narratives         - Hook Permutations    - Copy Variations  │
│    - Visual Assets (AST)     - Video Teardowns      - Creative Matrix  │
├────────────────────────────────────────────────────────────────────────┤
│ 5. DISTRIBUTION & CHANNEL PLANE                                        │
│    - Outbound Sequences      - LinkedIn InMail      - Search Keywords  │
│    - Paid Social Ads         - Technical Content    - Direct Mail      │
├────────────────────────────────────────────────────────────────────────┤
│ 6. FUNNEL & CONVERSION PLANE                                           │
│    - Edge Landing Pages (PG) - Qualification Logic  - Cal.com Sched    │
│    - SOW Contract Vault      - Escrow Checkout      - Sales Handoff    │
├────────────────────────────────────────────────────────────────────────┤
│ 7. OBSERVABILITY, TESTING & LEARNING PLANE                             │
│    - UTM Tracking Telemetry  - A/B Hypotheses (EXP) - Causal Lift      │
│    - Neo4j Knowledge Graph   - Attribution Ledger   - Retrospectives   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Directory Structure & File Map

```text
CAMPAIGNS/
├── CAMPAIGN.md                   # Canonical individual campaign exemplar (CAM-001)
├── CAMPAIGN-OS.md                # Operating system master engine
├── CAMPAIGN-MODEL.md             # Formal mathematical formulation
├── CAMPAIGN-ARCHITECTURE.md      # Structural architecture (this file)
├── CAMPAIGN-LIFECYCLE.md         # 16-stage lifecycle specification
├── CAMPAIGN-STRATEGY.md          # Strategy and competitive positioning
├── CAMPAIGN-PLANNING.md          # End-to-end campaign planning SOP
├── CAMPAIGN-POLICY.md            # Policies, limits, brand safety
├── CAMPAIGN-STANDARDS.md         # Quality bars, proof standards
│
├── CAMPAIGN-REGISTRY.md          # Portfolio campaign ledger
├── CAMPAIGN-TAXONOMY.md          # Identifier prefixes and schemas
├── CAMPAIGN-CLASSIFICATION.md    # Multi-dimensional classification
├── CAMPAIGN-HIERARCHY.md         # Enterprise-to-experiment hierarchy
├── CAMPAIGN-RELATIONSHIPS.md     # Relational graph map & predicates
├── CAMPAIGN-TYPES.md             # 34 standard campaign types
│
├── OBJECTIVES.md / CAMPAIGN-GOALS.md / PRIMARY-OBJECTIVE.md ...
├── AUDIENCES.md / SEGMENTS.md / PERSONAS.md / ICP.md ...
├── POSITIONING.md / MESSAGING.md / CORE-MESSAGE.md ...
├── OFFER.md / OFFERS.md / PRICING.md / GUARANTEES.md ...
├── CHANNELS.md / MEDIA.md / MEDIA-PLAN.md / CHANNELS/ ...
├── CREATIVE.md / COPY.md / DESIGN.md / VIDEO.md ...
├── CONTENT.md / CONTENT-CALENDAR.md / EDITORIAL.md ...
├── FUNNELS.md / LANDING-PAGES.md / LEAD-CAPTURE.md ...
├── BUDGET.md / CAC.md / ROAS.md / UNIT-ECONOMICS.md ...
├── TIMELINE.md / SCHEDULE.md / LAUNCH.md ...
├── MEASUREMENT.md / TRACKING.md / KPIS.md / UTM.md ...
├── EXPERIMENTATION.md / HYPOTHESES.md / A-B-TESTING.md ...
├── OPTIMIZATION.md / PERFORMANCE.md / BUDGET-OPTIMIZATION.md ...
├── COMPETITIVE-INTELLIGENCE.md / AD-LIBRARY.md ...
├── LAUNCH-CHECKLIST.md / QA.md / PRE-LAUNCH.md ...
├── RISKS.md / ASSUMPTIONS.md / STOP-RULES.md / KILL-CRITERIA.md ...
├── GOVERNANCE.md / OWNERSHIP.md / RACI.md ...
├── COMPLIANCE.md / LEGAL-REVIEW.md / CLAIMS.md ...
├── CAMPAIGN-REPORT.md / POST-MORTEM.md / INSIGHTS-REGISTER.md ...
├── AI-CAMPAIGNS.md / CAMPAIGN-AGENTS.md / CAMPAIGN-AUTOMATION.md ...
└── CAMPAIGN-CHANGELOG.md
```

---

## 3. Data Flow Architecture

1. **Static Configuration Layer:** Defined in YAML frontmatter and Markdown files in `CAMPAIGNS/`.
2. **Machine-Readable Registry Layer:** Normalized JSON files in `_REGISTRIES/` for programmatic querying by subagents and CLI scripts.
3. **Graph Knowledge Layer:** Loaded into Neo4j via predicates defined in `_RELATIONSHIPS/CAMPAIGN-RELATIONSHIPS.md`.
4. **Runtime Telemetry Layer:** Ingested via webhooks and LiteLLM/OmniRoute tracking into Prometheus, Grafana, and Postgres.

---

## 4. Integration with AntiGravity Rules

- **Rule #1 (North Star):** Direct progression from Strategy to Cash to Learning.
- **Rule #2 (Reuse First):** Leverages existing commercial offers and tool stacks.
- **Rule #3 & #4 (No Fake Completion / No Placeholder Architecture):** Fully populated real-world schemas; zero TODO comments or mock APIs.
- **Rule #6 (Data Integrity):** Versioned updates to registries in `_REGISTRIES/`.

---

## 5. Related Files

- Master Operating Contract: [[ANTIGRAVITY.md]]
- Operating System: [[CAMPAIGNS/CAMPAIGN-OS]]
- Canonical Campaign: [[CAMPAIGNS/CAMPAIGN]]
