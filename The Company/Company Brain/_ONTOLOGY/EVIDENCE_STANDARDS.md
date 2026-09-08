---
id: ONT-EVIDENCE-001
title: "Evidence & Provenance Standards"
aliases: ["_ONTOLOGY/EVIDENCE_STANDARDS", "Evidence & Provenance Standards"]
tags: [ontology, evidence, provenance, reality, verification]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[REALITY]] | [[EVIDENCE]] | [[07-ONTOLOGY/README|Ontology Hub]] | [[42-EVALUATION/README|Evaluation]]

# Evidence & Provenance Standards

**Principle:** Every claim, decision, and outcome in the Company Brain must be backed by evidence. This document defines how evidence is captured, verified, and tracked.

---

## Evidence Requirements by Entity Type

### Decisions (DEC)
**Minimum required:**
- **Source documents** — at least 1 document/analysis/report supporting the decision
- **Confidence score** — 0-1 estimate of decision quality (0.5 = moderate, 0.8+ = high confidence)
- **Decision maker** — who made the decision and on what date
- **Rationale** — 1-3 sentence explanation of reasoning
- **Authority** — who has authority to make this decision (CEO, Board, etc.)

**Example:**
```yaml
ref_id: DEC-000042
name: "Consolidate Telecommunications Sector"
date_made: 2026-09-01
made_by: PER-000001
authority: "Chief Strategy Officer"
confidence: 0.85
rationale: "SEC-021 and SEC-036 represent the same vertical"
evidenced_by:
  - ANL-000005
  - DST-000012
verification_date: 2026-09-01
```

---

### Outcomes (OUT)
**Minimum required:**
- **Measurement** — quantified result (revenue, growth %, quality score)
- **Time period** — when the outcome occurred
- **Measurement method** — how the metric was calculated
- **Confidence** — 0-1 (test results 0.95+, survey data 0.6-0.8, estimates 0.3-0.6)
- **Evidence source** — dataset, query, report, or system record

**Example:**
```yaml
ref_id: OUT-000183
name: "Q3 Revenue Growth"
metric_type: "revenue_increase_pct"
value: 15.3
unit: "percent"
time_period: "2026-07-01 to 2026-09-30"
measurement_method: "Calculated from database"
confidence: 0.98
source: DST-000087
verified_date: 2026-10-15
verified_by: PER-000012
```

---

### Lessons (LES)
**Minimum required:**
- **Source outcome** — which outcome/experiment produced this lesson
- **Pattern observation** — what pattern was observed
- **Applicability** — where/when this applies
- **Confidence** — 0-1 (0.9+ = strong pattern, 0.5-0.7 = emerging pattern)
- **Next action** — what should change based on this lesson

**Example:**
```yaml
ref_id: LES-000009
name: "Early Customer Feedback Accelerates Product-Market Fit"
source_outcome: OUT-000156
pattern: "Ventures with weekly interviews reached PMF 40% faster"
applicability: "B2B SaaS ventures with <$2M ARR"
confidence: 0.88
evidence:
  - data: 12 ventures tracked over 18 months
  - source: RES-000045
next_action: "Allocate 10% of venture budget to customer discovery"
verified_date: 2026-08-30
```

---

### Metrics/KPIs (MTR, KPI)
**Minimum required:**
- **Definition** — exact calculation/formula
- **Data source** — which system/table/query produces this
- **Refresh frequency** — how often updated
- **Confidence** — 0-1 (system-calculated = 1.0, manual = 0.7, estimated = 0.4)
- **Owner** — who maintains this metric
- **Verification cadence** — how often checked against reality

**Example:**
```yaml
ref_id: KPI-000087
name: "Customer Acquisition Cost (CAC)"
definition: "SUM(spend) / COUNT(customers)"
data_source: "analytics.cac_monthly"
refresh_frequency: "Daily at 02:00 UTC"
confidence: 0.95
owner: TEA-000034
verification_cadence: "Quarterly"
last_verified: 2026-09-01
```

---

### Policies & Standards (POL, STD)
**Minimum required:**
- **Authority** — who established this policy
- **Rationale** — why this policy exists (legal, operational, risk)
- **Enforcement** — mandatory or recommended
- **Compliance evidence** — how compliance is verified
- **Last reviewed** — when policy was last validated

**Example:**
```yaml
ref_id: POL-000012
name: "Data Privacy Policy"
authority: "Legal & Compliance"
rationale: "GDPR compliance and customer trust"
date_established: 2025-01-15
last_reviewed: 2026-08-30
enforcement: "MANDATORY"
compliance_check: "Quarterly audit of access logs"
evidence_of_compliance:
  - AUD-000034
  - CTL-000156
```

---

### Risks & Mitigations (RIK, MIT)
**Minimum required:**
- **Risk description** — what could go wrong
- **Probability** — 0-1 (0.1 = rare, 0.5 = moderate, 0.9+ = probable)
- **Impact** — 0-1 (0.3 = low, 0.9+ = critical)
- **Detection method** — how we'd detect this risk
- **Mitigation** — what we do to reduce risk
- **Owner** — who's responsible

**Example:**
```yaml
ref_id: RIK-000042
name: "Key Person Dependency"
description: "CEO departure disrupts strategy"
probability: 0.15
impact: 0.85
risk_score: 0.1275
detection_method: "Board signals, insurance policy monitoring"
mitigation:
  - MIT-000089  # Succession plan
  - MIT-000090  # VP-level ownership
  - MIT-000091  # Key person insurance
owner: PER-000156
last_reviewed: 2026-07-01
```

---

## Confidence Score Guidelines

| Score | Meaning | Valid for | Examples |
|-------|---------|-----------|----------|
| 0.95–1.0 | High confidence | Critical decisions | System-calculated metrics, peer-reviewed analysis |
| 0.85–0.94 | Good confidence | Strategic decisions | Expert assessment, multi-source validation |
| 0.70–0.84 | Moderate confidence | Tactical decisions | Single peer review, 3-6 months data |
| 0.50–0.69 | Emerging signal | Hypotheses, tests | Early hypothesis, <3 months data |
| 0.30–0.49 | Low confidence | Exploration only | Early assessment, limited data |
| <0.30 | Speculative | Not for decisions | Untested assumptions |

---

## Evidence Source Types

### Primary (High Credibility)
- System-calculated data (databases, APIs, dashboards)
- Peer-reviewed documents
- Third-party audits (SOC 2, security, financial)
- Controlled experiments

### Secondary (Moderate Credibility)
- Analyst reports from reputable firms
- Internal expert assessment
- Verified customer feedback
- Historical data with quality audit

### Tertiary (Use with Caution)
- Surveys or self-reported data
- Internal estimates
- Anecdotal evidence
- News articles or market commentary

---

## Verification Process

### Initial Claim
1. **Document the claim** — Decision, outcome, or insight
2. **List sources** — What evidence backs this
3. **Assess confidence** — 0-1 based on source quality
4. **Name authority** — Who verified or is responsible

### Quarterly Review
1. **Check data freshness** — Is source data still current?
2. **Validate assumptions** — Have underlying assumptions held?
3. **Verify confidence** — Is score still accurate?
4. **Update evidence** — Add new sources or refresh old ones

### Annual Deep Audit
1. **Spot-check 10%** of high-confidence claims
2. **Re-validate authority** — Is person still in role?
3. **Assess for obsolescence** — Is claim still relevant?
4. **Update or retire** — Refresh or mark as historical

---

## Recording Evidence in Wiki

**Format for wiki links:**

```markdown
# Some Decision

[[Decision DEC-000042]] consolidated [[Sector SEC-021]] and [[Sector SEC-036]]
based on analysis showing 40% overlap.

**Evidence:**
- [[Analysis ANL-000005]]: "Telecommunications sector taxonomy study"
- [[Dataset DST-000012]]: Venture distribution by sector (95% confidence)
- **Verified by:** [[Garry Tan PER-000001]] on 2026-09-01
- **Confidence:** 0.85 (Expert assessment + data support)
```

---

## Relationship-Level Evidence

When creating EVIDENCED_BY relationships:

```yaml
relationship:
  source: DEC-000042
  target: ANL-000005
  type: "EVIDENCED_BY"
  properties:
    confidence: 0.85
    authority: "Chief Strategy Officer"
    verification_date: "2026-09-01"
    credibility: "PRIMARY"
```

---

## Evidence for Different Domains

### Organizational Claims (01-IDENTITY, 23-VENTURES)
- Requirement: Venture registration, cap table, legal docs
- Verification: Database query + legal review

### Capability Claims (14-CAPABILITIES, 15-SKILLS)
- Requirement: Implementation proof (code), test coverage >80%, peer review
- Verification: GitHub repo + CI/CD pass

### Financial Claims (24-FINANCE)
- Requirement: Audit trail, signed approval, reconciliation
- Verification: Finance system + auditor signature

### Execution Claims (22-EXECUTION, 43-OUTCOMES)
- Requirement: Loop execution log, metrics snapshot, outcome measurement
- Verification: Execution tracking system + manual spot-check

---

## Quality Standards

1. **No orphaned decisions** — Every decision must have ≥1 evidence source
2. **Quarterly refresh** — Dates >3 months old must be re-verified
3. **Authority attribution** — Every claim names decision maker or source authority
4. **Confidence transparency** — Confidence scores visible in all decisions
5. **Traceability** — Audit trail shows who verified what and when

**Status:** Active | **Last Updated:** 2026-09-01
---

## Connected Subsystems
- **Reality Ledger:** [[REALITY]]
- **Evidence Proofs:** [[EVIDENCE]]
- **Ontology Architecture:** [[07-ONTOLOGY/README|07-ONTOLOGY]]
- **Evaluation Domain Hub:** [[42-EVALUATION/README|42-EVALUATION]]
- **Master Control:** [[50-MASTER-CONTROL/50-MASTER-CONTROL]]
