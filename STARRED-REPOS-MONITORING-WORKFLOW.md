# STARRED REPOS MONITORING WORKFLOW

**Date:** 2026-06-01  
**Repos:** 700 external projects  
**Frequency:** Quarterly (monthly for top 50)  

## Purpose

The 664+ starred repos are external reference implementations guiding sector strategy. This workflow ensures sector managers stay aware of upstream changes that could affect our ventures.

## Monitoring Schedule

| Frequency | Repos | Responsibility |
|-----------|-------|---|
| Monthly (priority) | Top 50 by stars | AI Agent + Sector Manager |
| Quarterly (standard) | Remaining 614 | AI Agent (async) |
| As-needed (critical) | Breaking changes | All agents notify immediately |

## Alert Triggers

AI agents monitor for:
- **Major releases** (vX.0.0) — escalate to sector manager
- **Deprecations** — evaluate migration path
- **Breaking API changes** — assess venture impact
- **Security advisories** — immediate escalation to CTO
- **Repository deprecated/archived** — plan alternative

## Decision Workflow

```
Upstream Change Detected
  ↓
AI Agent evaluates impact
  ↓
Sector Manager decides:
  ├─ ADOPT → Add to venture stack, open implementation task
  ├─ FORK → Create internal copy, version lock
  └─ IGNORE → Document rationale, monitor for future changes
```

## Integration

- **Feeds:** GitHub API (releases, tags, security advisories)
- **Output:** STARRED-REPOS-GOVERNANCE.csv (status + decision per repo)
- **Escalation:** Issues flagged in agent daily reports and sector dashboards

## Top 20 Priority Repos

See STARRED-REPOS-GOVERNANCE.csv for full list sorted by stars and last-updated date.

---

**Status:** Ready for quarterly audit cycle.
