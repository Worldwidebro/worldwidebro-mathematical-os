---
id: REG-EVIDENCE-001
title: "EVIDENCE — Truth Ledger, Claims & Falsification Registry"
aliases: ["37-RESEARCH/EVIDENCE", "EVIDENCE", "Truth Ledger", "Falsification Registry"]
tags: ["research", "evidence", "truth", "claims", "verification", "falsification"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[REALITY]] | [[_ONTOLOGY/EVIDENCE_STANDARDS|EVIDENCE_STANDARDS]] | [[37-RESEARCH/37-RESEARCH|37-RESEARCH]] | [[42-EVALUATION/README|42-EVALUATION]]

# EVIDENCE.md — Truth Ledger, Claims & Falsification Registry

> **Canonical System ID:** `REG-EVIDENCE-001`  
> **Master Operating Law:** [[REALITY|REALITY.md]] & [[_ONTOLOGY/EVIDENCE_STANDARDS|EVIDENCE_STANDARDS.md]]  
> **Principle:** Every technical, market, or financial assertion in Company Brain must be backed by reproducible evidence. Unverified claims remain labeled as assumptions until falsified or verified.

---

## 1. Evidence Hierarchy (Grade A through E)

| Grade | Classification | Required Proof |
| :--- | :--- | :--- |
| **Grade A (Gold)** | **Audited Ground Truth** | Bank statement, processed Stripe payout, executed client contract, verified git commit test log, live server telemetry. |
| **Grade B (High)** | **Primary Official Data** | Federal government API (Census BDS, BLS, FRED, SEC 10-K), peer-reviewed journal paper with reproduced code. |
| **Grade C (Moderate)**| **Secondary Verified Research**| Non-replicated peer-reviewed paper, industry trade association survey, verified customer interview transcript. |
| **Grade D (Low)** | **Unverified Signal / Preprint** | arXiv preprint without code, competitor marketing claims, blog posts, unaudited pitch deck estimates. |
| **Grade E (Invalid)**| **Speculation / Hallucination** | Internal wishful thinking, ungrounded TAM estimations, unverified LLM assertions. |

---

## 2. Active Claims & Verification Ledger

```yaml
claims:
  CLM-001:
    statement: "95 projects are deployed and live on Vercel under the worldwidebro account."
    evidence_grade: "Grade A"
    evidence_source: "Vercel CLI worldwidebro API output (2026-09-05)"
    verified: true
    verified_by: "Antigravity Agent"
    artifact: "_REGISTRIES/CANONICAL/VERCEL_DEPLOYMENTS.json"

  CLM-002:
    statement: "177 owned repositories contain real software code manifests."
    evidence_grade: "Grade A"
    evidence_source: "Batched GitHub GraphQL API query across 887 repos (2026-09-05)"
    verified: true
    verified_by: "Antigravity Agent"
    artifact: "_REGISTRIES/CANONICAL/OWNED_REPO_CODE_REALITY.json"

  CLM-003:
    statement: "700 cataloged ventures represent operational companies with revenue."
    evidence_grade: "Grade E (FALSIFIED)"
    evidence_source: "REALITY.md & Bank ledger review (2026-09-05)"
    verified: false
    resolution: "FALSIFIED. Reclassified 690 ventures as SPECULATIVE."
    artifact: "REALITY.md"

  CLM-004:
    statement: "Mac Studio M4 Max runs OmniRoute and LiteLLM natively over Tailscale."
    evidence_grade: "Grade A"
    evidence_source: "Live Docker context inspect (civos_litellm:4000, omniroute:20128) - 2026-09-05"
    verified: true
    verified_by: "Antigravity Agent"
    artifact: "CLAUDE.md"
```
