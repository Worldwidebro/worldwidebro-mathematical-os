#!/usr/bin/env python3
"""Enforce directives on decisions."""
import json
from datetime import datetime

class DirectiveEnforcer:
    """Apply rules from DIRECTIVES/."""

    def enforce(self, decision: dict) -> dict:
        """Apply approval matrix to decision."""
        amount = decision.get("amount", 0)
        approval_level = self._get_level(amount)

        return {
            "decision_id": decision["task_id"],
            "amount": amount,
            "approval_level": approval_level,
            "rule": self._get_rule(approval_level),
            "enforced_at": datetime.now().isoformat(),
        }

    def _get_level(self, amount: float) -> str:
        if amount < 5000:
            return "auto"
        elif amount < 25000:
            return "director"
        else:
            return "ceo_hermes"

    def _get_rule(self, level: str) -> str:
        return {
            "auto": "Auto-approve, execute immediately",
            "director": "Escalate to director, await approval",
            "ceo_hermes": "CEO + Hermes reasoning, full deliberation",
        }[level]

def pilot():
    """Enforce on 3 pilot tasks."""
    with open("/Users/acebless/Documents/pilot_tasks.json") as f:
        tasks = json.load(f)

    enforcer = DirectiveEnforcer()
    decisions = [enforcer.enforce(t) for t in tasks["tasks"]]

    return {
        "timestamp": datetime.now().isoformat(),
        "decisions_enforced": len(decisions),
        "decisions": decisions,
    }

if __name__ == "__main__":
    result = pilot()
    with open("/Users/acebless/Documents/pilot_directives_enforced.json", "w") as f:
        json.dump(result, f, indent=2)
    print(f"✅ Enforced directives on {result['decisions_enforced']} decisions")
