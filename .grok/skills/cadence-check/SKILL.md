# Cadence Check — Automated Sector Ownership Audit

## What it does

Reads `SECTOR-OWNERSHIP-REGISTRY.csv`, flags unassigned sectors and sectors past their cadence window, and posts updates to Slack.

**Status report:**
- ✅ OK: sectors on schedule
- 🔄 STALE: sectors past cadence (default 30d)
- ⚠️ UNASSIGNED: sectors with no owner

## Run it

```bash
# Dry run (preview Slack message)
python3 .grok/skills/cadence-check/cadence-check.py --dry-run

# Post to Slack (requires webhook URL)
python3 .grok/skills/cadence-check/cadence-check.py --slack-webhook https://hooks.slack.com/...
```

## Loop integration

The Loop system runs this daily via the daily-triage pattern. It:
1. Reads the registry (no external network call)
2. Compares `last_updated` vs `cadence_days`
3. Formats a Slack block message
4. Posts to the designated webhook (if configured)
5. Returns status to STATE.md

## Cost

Low (CSV read + optional HTTP POST to Slack). ~1-5 tokens per run (no LLM calls).

## Exit codes

- `0`: Script ran (OK or STALE or UNASSIGNED sectors detected)
- `1`: Registry not found or Slack post failed

## Dependencies

- Python 3.9+
- `requests` library (for Slack posting)
- `SECTOR-OWNERSHIP-REGISTRY.csv` file exists

## Cadence options

Edit `SECTOR-OWNERSHIP-REGISTRY.csv`:
- `cadence_days`: number of days between required updates (0 = no cadence)
- `last_updated`: ISO date (YYYY-MM-DD) of last content update
- `status`: "OWNED" or "UNASSIGNED"
- `slack_channel`: where to post alerts for this sector

## Future enhancements

- Auto-update `last_updated` when sector page is deployed
- Per-sector webhooks (one for each OPCO channel)
- Escalation: post to #ventures-unassigned after 2+ missed cadences
