#!/usr/bin/env python3
"""
WIRING #1: Feedback Logging

Adds outcome data to venture_loop execution.
Enables learning loop to score agents based on actual results.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

RUNLOG = Path("/Users/acebless/Documents/runs.jsonl")
FEEDBACK_LOG = Path("/Users/acebless/Documents/runs_feedback.jsonl")


def add_feedback(run_id: str, status: str, cost_or_error: str = "", duration_seconds: int = 0):
    """Log outcome of a venture_loop execution."""
    # Parse cost if numeric, otherwise treat as error message
    cost = None
    error = None
    try:
        cost = float(cost_or_error) if cost_or_error else None
    except ValueError:
        error = str(cost_or_error)

    feedback = {
        "run_id": run_id,
        "status": status,
        "cost": cost,
        "error": error,
        "duration_seconds": duration_seconds,
        "logged_at": datetime.now().isoformat(),
    }

    # Append to feedback log (JSON Lines)
    with open(FEEDBACK_LOG, "a") as f:
        f.write(json.dumps(feedback) + "\n")

    print(f"✅ Feedback: {run_id} → {status}")
    return feedback


def get_run_with_feedback(run_id: str) -> dict:
    """Get original run packet + its feedback."""
    original_run = None
    with open(RUNLOG) as f:
        for line in f:
            run = json.loads(line)
            if run.get("run_id") == run_id:
                original_run = run
                break

    feedback = None
    if FEEDBACK_LOG.exists():
        with open(FEEDBACK_LOG) as f:
            for line in f:
                fb = json.loads(line)
                if fb.get("run_id") == run_id:
                    feedback = fb
                    break

    return {"run": original_run, "feedback": feedback}


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 01_loop_feedback_collector.py <run_id> <status> [cost_or_error] [duration_seconds]")
        print("\nExample (success): 01_loop_feedback_collector.py 20260728T120000 success 45.50 120")
        print("Example (failure): 01_loop_feedback_collector.py 20260728T120000 failure 'Stripe timeout' 180")
        return

    run_id = sys.argv[1]
    status = sys.argv[2]
    cost_or_error = sys.argv[3] if len(sys.argv) > 3 else ""
    duration = int(sys.argv[4]) if len(sys.argv) > 4 else 0

    add_feedback(run_id, status, cost_or_error, duration)
    outcome = get_run_with_feedback(run_id)
    print(json.dumps(outcome, indent=2))


if __name__ == "__main__":
    main()
