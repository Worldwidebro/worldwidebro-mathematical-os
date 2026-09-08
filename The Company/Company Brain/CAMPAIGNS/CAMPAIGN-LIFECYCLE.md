# CAMPAIGN-LIFECYCLE — The 16-Stage Campaign Lifecycle

> **Canonical Document ID:** `DOC-LIF-CAM-001`  
> **Authority:** Operational Governance (CP-006 / CP-027)  
> **Status:** ACTIVE LIFECYCLE SPECIFICATION

---

## 1. Lifecycle Overview

Campaigns in Company Brain are not static marketing documents; they are dynamic, stateful entities that transition through an explicit 16-stage lifecycle:

```text
IDEA ──> RESEARCH ──> OPPORTUNITY ──> BRIEF ──> STRATEGY ──> PLANNING ──> APPROVAL ──> PRODUCTION
                                                                                              │
KNOWLEDGE <── LEARNING <── POST-MORTEM <── DECISION-GATE <── OPTIMIZATION <── MEASUREMENT <── QA ──< LAUNCH
                                                  │
                                                  ├── SCALE
                                                  ├── PIVOT
                                                  ├── PAUSE
                                                  └── KILL
```

---

## 2. Detailed Stage Protocols

### Stage 1: IDEA
- **Trigger:** Market observation, customer complaint, competitive opening, or founder hypothesis.
- **Artifact:** Rough concept note or draft record.
- **Gate:** Does this align with venture priorities and North Star?

### Stage 2: RESEARCH
- **Activities:** TAM analysis, competitor ad analysis, scraping customer complaints, analyzing forum sentiment.
- **Artifact:** Research brief linking to [[CAMPAIGNS/COMPETITIVE-INTELLIGENCE]].
- **Gate:** Is there verified, empirical market friction?

### Stage 3: OPPORTUNITY
- **Activities:** Financial modeling, revenue projection, pricing elasticity evaluation.
- **Artifact:** Business case with expected return.
- **Gate:** Projected ROAS \(\ge 3.0x\) or CAC payback \(< 60\) days.

### Stage 4: BRIEF
- **Activities:** Formulating the standardized creative and operational brief.
- **Artifact:** [[CAMPAIGNS/CREATIVE-BRIEF]].
- **Gate:** Clear scope, single-threaded owner, unambiguous target audience.

### Stage 5: STRATEGY
- **Activities:** Formulating the core narrative, message hierarchy, Grand Slam offer structure, and channel mix.
- **Artifacts:** [[CAMPAIGNS/CAMPAIGN-STRATEGY]], [[CAMPAIGNS/OFFER-STRATEGY]].
- **Gate:** Strong differentiated positioning vs key competitors.

### Stage 6: PLANNING
- **Activities:** Work breakdown structure, milestone scheduling, budget allocation, RACI assignments.
- **Artifacts:** [[CAMPAIGNS/CAMPAIGN-PLANNING]], [[CAMPAIGNS/BUDGET]].
- **Gate:** Critical path dependencies scheduled; capital allocated.

### Stage 7: APPROVAL
- **Activities:** Executive sign-off, legal compliance review, claim substantiation check.
- **Artifacts:** [[CAMPAIGNS/APPROVALS]], [[CAMPAIGNS/LEGAL-REVIEW]].
- **Gate:** Sovereign Operator approval recorded in metadata header.

### Stage 8: PRODUCTION
- **Activities:** Copywriting, visual asset design, video production, landing page coding, tracking parameter injection.
- **Artifacts:** Creative variants, live landing pages, email sequence scripts.
- **Gate:** All creative assets match brand design tokens and editorial standards.

### Stage 9: QA & PRE-FLIGHT
- **Activities:** Full functional audit: test form submissions, verify UTM tracking, validate Stripe webhook, check responsive mobile UI, test CRM sync.
- **Artifact:** [[CAMPAIGNS/LAUNCH-CHECKLIST]].
- **Gate:** 100% check of all items on the Go/No-Go punchlist.

### Stage 10: LAUNCH
- **Activities:** Zero-hour coordination: unpausing campaigns, enabling email sequence triggers, publishing landing pages.
- **Artifact:** [[CAMPAIGNS/LAUNCH]].
- **Gate:** Live telemetry confirmation within 15 minutes of release.

### Stage 11: DELIVERY & FLIGHTING
- **Activities:** Continuous media delivery, pacing management, email blast execution, inbound lead routing.
- **Artifact:** [[CAMPAIGNS/FLIGHTING]].
- **Gate:** Spend pacing conforms to daily budget bounds.

### Stage 12: MEASUREMENT
- **Activities:** Ingesting conversion events, monitoring CPA, ROAS, click-through rates, and pipeline generation.
- **Artifact:** [[CAMPAIGNS/MEASUREMENT]].
- **Gate:** Telemetry flowing cleanly into Grafana and Neo4j.

### Stage 13: OPTIMIZATION
- **Activities:** Statistical A/B test analysis, killing losing ad variants, shifting budget to winning channels, refreshing fatigued copy.
- **Artifact:** [[CAMPAIGNS/OPTIMIZATION]].
- **Gate:** Continuous marginal improvement in target KPI.

### Stage 14: DECISION GATE (SCALE / PIVOT / PAUSE / KILL)
- **Evaluation:** Evaluates performance against pre-established [[CAMPAIGNS/STOP-RULES]] and [[CAMPAIGNS/KILL-CRITERIA]].
- **Outcomes:**
  - `SCALE`: Exceeds KPI targets with favorable unit economics \(\to\) Increase budget by 20–50%.
  - `PIVOT`: High engagement but low conversion \(\to\) Revise landing page or offer guarantee.
  - `PAUSE`: Deliverability issue or tracking anomaly detected \(\to\) Halt media pending fix.
  - `KILL`: Target KPI breached stop threshold \(\to\) Terminate immediately to protect capital.

### Stage 15: POST-MORTEM & REPORT
- **Activities:** Blameless review of operational failures, financial reconciliation of revenue vs spend, attribution calculation.
- **Artifacts:** [[CAMPAIGNS/POST-MORTEM]], [[CAMPAIGNS/CAMPAIGN-REPORT]].
- **Gate:** Final financial figures recorded in `_REGISTRIES/CAMPAIGN-RESULT-REGISTRY.json`.

### Stage 16: KNOWLEDGE & LEARNING LOOP
- **Activities:** Distilling actionable heuristics, storing winning copy formulas, updating customer persona blueprints, ingestion into Knowledge Core.
- **Artifact:** [[CAMPAIGNS/INSIGHTS-REGISTER]].
- **Gate:** Permanent update committed to Company Brain graph.

---

## 3. Related Documents

- Master System: [[CAMPAIGNS/CAMPAIGN-OS]]
- Planning Guide: [[CAMPAIGNS/CAMPAIGN-PLANNING]]
- Launch Checklist: [[CAMPAIGNS/LAUNCH-CHECKLIST]]
- Kill Criteria: [[CAMPAIGNS/KILL-CRITERIA]]
