---
title: Add business_complete tracking to venture registries
date: 2026-07-12
priority: medium
---

# Add business_complete tracking to venture registries

Extend venture tracking to measure the completion bar defined in `[[venture-completion-definition]]`: nonzero revenue in 2 consecutive months.

## What's needed

- A place to record monthly revenue per venture (doesn't exist yet — no registry currently has a revenue-by-month field)
- A derived `business_complete` flag (true once 2 consecutive nonzero months are recorded)
- Decide: extend `VENTURE-READINESS-SCORECARD.csv` with new columns, or create a separate `VENTURE-REVENUE-TRACKING.csv` and join on `venture_id`

## Blocked on

See `[[per-venture-revenue-capture]]` research question — none of the 24 candidate ventures have payments wired yet, so there's no revenue signal to record. This todo can't produce real data until that's resolved for at least one venture.
