---
id: PORTAL-REVIEW-RECEIPTS-001
title: "review-receipts/ — Quality Assurance & Code Review Receipt Log"
aliases: ["review-receipts", "review-receipts/README", "Review Receipts", "QA Receipts"]
tags: ["receipts", "code-review", "qa", "audit", "grading"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[_EVAL/README|Operational Evaluation Hub]] | [[42-EVALUATION/README|42-EVALUATION]] | [[ANTIGRAVITY]]

# review-receipts/ — Quality Assurance & Code Review Receipt Log

> **Authority:** Performance & Quality Control Plane ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-028]])  
> **Primary Ledger:** `review-receipts/receipts.jsonl`  
> **Status:** 🟢 ACTIVE — Review Receipts Stream (2026-09-06)

---

## 1. Executive Summary

The **`review-receipts/`** directory maintains `review-receipts.jsonl`, the dedicated ledger for automated code reviews, architectural gate approvals, and security audits:
- **Reviewer Identity**: Specializing QA subagent (`qa.md`, `reality-checker`, `security-appsec-engineer`).
- **Verdict States**: `APPROVED`, `CHANGES_REQUESTED`, `REJECTED`.
- **Enforcement**: Upholds Rule 3 of [[ANTIGRAVITY.md]] (Strictly zero fake completion).
