---
description: Analyze A/B experiment significance, prune losing variants, and optimize budget allocations
globs: CAMPAIGNS/**
---

# /campaign-optimize Workflow

Run this workflow to execute scientific closed-loop optimization on an in-flight campaign.

## Steps:

1. **Evaluate Active Hypotheses & Tests:**
   - Read `_REGISTRIES/CAMPAIGN-EXPERIMENT-REGISTRY.json` and [[CAMPAIGNS/EXPERIMENTS.md]].
   - Calculate two-tailed z-score and p-value for active variant arms.
   - Check if sample size requirements (\(\ge 100\) per arm) have been met.

2. **Prune Underperforming Variants:**
   - If a variant is losing with \(p < 0.05\), terminate variant delivery.
   - Shift 100% of channel volume to the statistically winning hook.

3. **Tune Budget & Channel Reallocation:**
   - Compare CAC across channels (`CHN-OUT-001`, `CHN-LNK-001`, `CHN-CNT-001`).
   - Shift marginal budget into the channel producing the highest discovery call volume.

4. **Ingest Heuristics into Learning Register:**
   - Record statistical outcome in [[CAMPAIGNS/EXPERIMENT-RESULTS.md]].
   - Add confirmed customer behavioral heuristic to [[CAMPAIGNS/INSIGHTS-REGISTER.md]].
