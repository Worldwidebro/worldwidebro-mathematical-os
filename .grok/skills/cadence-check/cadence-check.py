#!/usr/bin/env python3
"""
Cadence Check Loop Task — Read SECTOR-OWNERSHIP-REGISTRY.csv and post Slack updates
for unassigned sectors and sectors past their cadence window.

Usage:
  python cadence-check.py [--dry-run] [--slack-webhook URL]
"""
import csv
import json
from datetime import datetime, timedelta
from pathlib import Path
import sys
import requests
import argparse


def load_registry(path):
    """Load sector ownership registry CSV."""
    registry = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            registry.append(row)
    return registry


def check_cadence(sector, today=None):
    """Check if sector is past cadence window."""
    if today is None:
        today = datetime.now().date()

    if sector["status"] == "UNASSIGNED":
        return "UNASSIGNED", 0

    if sector["cadence_days"] == "0":
        return "OK", 0

    try:
        last_updated = datetime.strptime(sector["last_updated"], "%Y-%m-%d").date()
        cadence_days = int(sector["cadence_days"])
        days_since = (today - last_updated).days

        if days_since > cadence_days:
            return "STALE", days_since
        else:
            return "OK", days_since
    except (ValueError, KeyError):
        return "ERROR", 0


def format_slack_message(sectors_by_status):
    """Format Slack message for sector updates."""
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📊 Sector Ownership Cadence Check",
                "emoji": True
            }
        }
    ]

    # Unassigned sectors
    unassigned = sectors_by_status.get("UNASSIGNED", [])
    if unassigned:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*⚠️ {len(unassigned)} Unassigned Sectors (need owner):*\n" +
                        "\n".join([f"• {s['sector_label']} ({s['sector_slug']})" for s in unassigned])
            }
        })

    # Stale sectors
    stale = sectors_by_status.get("STALE", [])
    if stale:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*🔄 {len(stale)} Stale Sectors (update due):*\n" +
                        "\n".join([f"• {s['sector_label']} ({s['days_since']}d old)" for s in stale])
            }
        })

    if not unassigned and not stale:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "✅ All sectors on schedule"
            }
        })

    blocks.append({
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": f"Updated: {datetime.now().isoformat()}"
            }
        ]
    })

    return {"blocks": blocks}


def post_slack(webhook_url, message):
    """Post message to Slack webhook."""
    try:
        response = requests.post(webhook_url, json=message, timeout=10)
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Slack post failed: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Sector cadence check loop")
    parser.add_argument("--dry-run", action="store_true", help="Don't post to Slack")
    parser.add_argument("--slack-webhook", default=None, help="Slack webhook URL")
    parser.add_argument("--registry", default="WORLDWIDEBRO-OS/08-DATA/registries/SECTOR-OWNERSHIP-REGISTRY.csv",
                       help="Path to registry CSV")
    args = parser.parse_args()

    registry_path = Path(args.registry)
    if not registry_path.is_absolute():
        registry_path = Path("/Users/acebless/Documents") / registry_path

    if not registry_path.exists():
        print(f"Registry not found: {registry_path}", file=sys.stderr)
        sys.exit(1)

    # Load and check
    registry = load_registry(registry_path)
    sectors_by_status = {"UNASSIGNED": [], "STALE": [], "OK": []}

    for sector in registry:
        status, days = check_cadence(sector)
        sector["days_since"] = days
        if status == "UNASSIGNED":
            sectors_by_status["UNASSIGNED"].append(sector)
        elif status == "STALE":
            sectors_by_status["STALE"].append(sector)
        else:
            sectors_by_status["OK"].append(sector)

    # Print summary
    print(f"✅ OK: {len(sectors_by_status['OK'])} sectors")
    print(f"🔄 STALE: {len(sectors_by_status['STALE'])} sectors")
    print(f"⚠️  UNASSIGNED: {len(sectors_by_status['UNASSIGNED'])} sectors")

    # Post to Slack if webhook provided
    message = format_slack_message(sectors_by_status)

    if args.dry_run:
        print("\n[DRY RUN] Would post to Slack:")
        print(json.dumps(message, indent=2))
    elif args.slack_webhook:
        if post_slack(args.slack_webhook, message):
            print("✅ Posted to Slack")
        else:
            sys.exit(1)
    else:
        print("(use --slack-webhook to post, or --dry-run to preview)")

    return 0 if (not sectors_by_status["UNASSIGNED"] and not sectors_by_status["STALE"]) else 0


if __name__ == "__main__":
    sys.exit(main())
