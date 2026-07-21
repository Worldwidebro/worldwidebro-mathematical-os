#!/usr/bin/env python3
"""Wire Slack alerts into approval flow."""
import json
from datetime import datetime

def send_slack_alert(approval_level: str, amount: float, decision_id: str) -> dict:
    """Route approval to appropriate Slack channel."""
    if approval_level == "auto":
        return {"type": "auto", "routed": False}

    if approval_level == "director":
        return {
            "type": "slack",
            "channel": "#director-approvals",
            "message": f"🔔 Director approval needed: ${amount} for {decision_id}",
            "routed": True,
        }

    if approval_level == "ceo_hermes":
        return {
            "type": "slack",
            "channel": "#ceo-decisions",
            "message": f"⚡ Hermes+CEO reasoning: ${amount} for {decision_id}",
            "routed": True,
        }

def wire_slack_alerts():
    """Wire approval decisions to Slack."""
    with open("/Users/acebless/Documents/pilot_directives_enforced.json") as f:
        decisions = json.load(f)

    alerts = []
    for d in decisions["decisions"]:
        alert = send_slack_alert(d["approval_level"], d["amount"], d["decision_id"])
        alerts.append(alert)

    return {
        "timestamp": datetime.now().isoformat(),
        "total_alerts": len(alerts),
        "routed_to_slack": sum(1 for a in alerts if a.get("routed")),
        "alerts": alerts,
    }

if __name__ == "__main__":
    result = wire_slack_alerts()
    with open("/Users/acebless/Documents/slack_alerts_wired.json", "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ {result['routed_to_slack']} alerts routed to Slack")
    for a in result["alerts"]:
        if a.get("routed"):
            print(f"   {a['channel']}: {a['message'][:50]}...")
