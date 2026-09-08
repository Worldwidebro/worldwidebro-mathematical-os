---
description: Audit active campaign telemetry, spend pacing, CAC, and conversion rate variances
globs: CAMPAIGNS/**
---

# /campaign-audit Workflow

Run this workflow to conduct a deep telemetry and financial audit of an active campaign.

## Steps:

1. **Query Telemetry & Ingested Events:**
   - Query event log in `_REGISTRIES/CAMPAIGN-EVENT-REGISTRY.json` or local telemetry database.
   - Calculate total accounts contacted, opens, positive replies, and booked calls.

2. **Reconcile Financial Spend & Cash:**
   - Read `_REGISTRIES/CAMPAIGN-BUDGET-REGISTRY.json` and compare actual spend against pacing curve.
   - Verify cash collected in escrow ledgers.
   - Calculate realized CAC, CPA, and ROAS.

3. **Evaluate Stop-Rules & Decision Gates:**
   - Check against [[CAMPAIGNS/STOP-RULES.md]] and [[CAMPAIGNS/KILL-CRITERIA.md]].
   - Flag any deliverability anomalies (bounce > 2%, unsubscribes > 0.5%).
   - Determine whether the campaign should: CONTINUE, OPTIMIZE, SCALE, PAUSE, or KILL.

4. **Update Result Registry:**
   - Update `_REGISTRIES/CAMPAIGN-RESULT-REGISTRY.json` with reconciled metrics.
