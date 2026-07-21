#!/usr/bin/env python3
"""
Hermes: Chief Operating Intelligence Agent
Coordinates capital allocation, decision routing, and venture sequencing.
Authority: <$5K auto-approve → director $5-25K → Hermes >$25K → human irreversible.
"""

import json
import os
from datetime import datetime
from anthropic import Anthropic

client = Anthropic()

system_prompt = """You are Hermes, Chief Operating Intelligence for Worldwidebro Holdings.

Role:
1. Route decisions: <$5K (auto-approve) → $5-25K (director) → >$25K (escalate) → irreversible (human)
2. Allocate capital across 18 OPCOs, 712 ventures
3. Resolve department conflicts
4. Track venture health, trigger interventions

Limits:
- Cannot override human on irreversible decisions
- Cannot hide failures
- Escalate when uncertain

When a decision arrives, respond with:
{
  "decision_id": "...",
  "venture_id": "...",
  "amount": ...,
  "authority_required": "auto_approve|director|hermes|human",
  "reasoning": "...",
  "action": "execute|escalate_to_director|escalate_to_human"
}

Be direct. One decision per turn. No explanation text outside JSON."""

def route_decision(amount: float, decision_type: str) -> str:
    """Return authority required based on amount and type."""
    if decision_type == "irreversible":
        return "human"
    if amount > 25000:
        return "hermes"
    if amount > 5000:
        return "director"
    return "auto_approve"

def evaluate(decision_data: dict) -> dict:
    """Send decision to Hermes for routing."""
    prompt = f"""Route this decision:
{json.dumps(decision_data, indent=2)}

Authority threshold: {route_decision(decision_data.get('amount', 0), decision_data.get('decision_type', ''))}"""

    response = client.messages.create(
        model="claude-opus-4.8",
        max_tokens=300,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}],
    )

    try:
        result = json.loads(response.content[0].text)
        result["routed_at"] = datetime.utcnow().isoformat()
        return result
    except json.JSONDecodeError:
        return {
            "error": "Invalid response format",
            "raw": response.content[0].text,
        }

def main():
    """Demo: route a $500 staffing placement (OPS-001)."""
    decision = {
        "decision_id": "dec_2026-07-20_001",
        "venture_id": "OPS-001",
        "decision_type": "placement_approval",
        "amount": 500,
        "context": "Candidate matched; payment due on completion",
    }

    print("Decision received:")
    print(json.dumps(decision, indent=2))
    print("\nHermes routing...\n")

    result = evaluate(decision)
    print("Hermes decision:")
    print(json.dumps(result, indent=2))
    print(f"\nAction: {result.get('action', 'unknown')}")
    print(f"Authority: {result.get('authority_required', 'unknown')}")

if __name__ == "__main__":
    main()
