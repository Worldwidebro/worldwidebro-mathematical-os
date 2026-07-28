#!/usr/bin/env python3
"""WIRING #2: Agent Scoring — Calculate success rates from runs + feedback"""
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timedelta

RUNLOG = Path("/Users/acebless/Documents/runs.jsonl")
FEEDBACK_LOG = Path("/Users/acebless/Documents/runs_feedback.jsonl")
SCORES_FILE = Path("/Users/acebless/Documents/agent_scores.jsonl")

def calculate_agent_scores(days_back=7):
    runs_by_id, feedback_by_id = {}, {}
    with open(RUNLOG) as f:
        for line in f:
            run = json.loads(line)
            runs_by_id[run.get("run_id")] = run
    if FEEDBACK_LOG.exists():
        with open(FEEDBACK_LOG) as f:
            for line in f:
                fb = json.loads(line)
                feedback_by_id[fb.get("run_id")] = fb

    cutoff = datetime.now() - timedelta(days=days_back)
    agent_stats = defaultdict(lambda: {"success": 0, "total": 0, "cost": 0})

    for run_id, run in runs_by_id.items():
        if run_id not in feedback_by_id:
            continue
        fb = feedback_by_id[run_id]
        ts = datetime.fromisoformat(run.get("ts", ""))
        if ts < cutoff:
            continue
        tools = run.get("tools_available", [])
        agent_key = "_".join(sorted(tools)) if tools else "unknown"
        agent_stats[agent_key]["total"] += 1
        if fb.get("status") == "success":
            agent_stats[agent_key]["success"] += 1
        if fb.get("cost"):
            agent_stats[agent_key]["cost"] += fb["cost"]

    scores = {}
    for agent, stats in agent_stats.items():
        success_rate = stats["success"] / stats["total"] if stats["total"] > 0 else 0
        avg_cost = stats["cost"] / stats["total"] if stats["total"] > 0 else 0
        scores[agent] = {
            "agent": agent,
            "success_rate": round(success_rate, 3),
            "total_runs": stats["total"],
            "avg_cost": round(avg_cost, 2),
            "calculated_at": datetime.now().isoformat(),
        }

    with open(SCORES_FILE, "a") as f:
        for agent, score in scores.items():
            f.write(json.dumps(score) + "\n")
    return scores

if __name__ == "__main__":
    scores = calculate_agent_scores(days_back=7)
    print(f"✅ Scored {len(scores)} agents")
    for agent, score in sorted(scores.items(), key=lambda x: x[1]["success_rate"], reverse=True)[:5]:
        print(f"  {agent}: {score['success_rate']*100:.1f}%")
