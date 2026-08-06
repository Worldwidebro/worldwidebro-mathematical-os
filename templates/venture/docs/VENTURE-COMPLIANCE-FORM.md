---
name: templates/venture/docs/VENTURE-COMPLIANCE-FORM
title: 'Venture Compliance & Agent Governance Form: {{VENTURE_NAME}}'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Venture Compliance & Agent Governance Form: {{VENTURE_NAME}}

## 1. Credentials & Secrets Compliance
- All API tokens and passwords must be stored in the remote Supabase `agent_credentials` table (encrypted).
- No raw keys are permitted in repository code files or local workspace configs.

## 2. Agent Authorization Boundaries
- **Capital Deployments**: Auto-approved up to \$100,000. All higher allocations require manual OPCO/CFO review.
- **Workflow Autonomy**: Enabled for standard routines. Exceptions must be escalated to the Governance Council.

## 3. Auditing & Logging
- Every agent routine execution must log to `runs.jsonl`.
- Feedback outcomes must be logged using [01_loop_feedback_collector.py](file:///Users/acebless/Documents/01_loop_feedback_collector.py).
