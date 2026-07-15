---
title: Venture completion definition
date: 2026-07-12
context: gsd-explore session, following marketing-readiness audit of 24 candidate ventures
---

# Venture completion definition

**A venture is "business-complete" when it shows nonzero revenue in 2 consecutive months.**

This is proof-of-model, not proof-of-scale. No dollar floor — $50/mo repeating counts the same as $5,000/mo repeating. The bar is "does this actually work as a business," not "is it big yet."

## Why this bar, not another

- First-dollar (1 sale) doesn't rule out a fluke — a friend, a one-off gift, a test transaction.
- 2 consecutive months rules out the fluke without requiring months of runway to prove it — lowest bar that still means something.
- No dollar floor was chosen deliberately: adding a floor conflates "does the model work" with "is it worth our time," which is a separate, later question (scale/prioritization), not a completion gate.

## Current state (as of 2026-07-12)

0 of ~24 candidate ventures (from `MARKETING-READINESS-CHECKLIST.csv`) have payments wired at all, so **none can currently be measured against this bar** — see the linked research question.

## Downstream implications

- `VENTURE-READINESS-SCORECARD.csv`'s existing `readiness_pct`/`readiness_tier` fields measure technical readiness (has_repo, has_revenue_model, capability_coverage_pct) — they do NOT measure this business-completion bar. The two are separate and shouldn't be conflated.
- The CivilizationOS iOS app idea (see seed) is explicitly gated behind ventures actually clearing this bar — there's no revenue data to visualize otherwise.
