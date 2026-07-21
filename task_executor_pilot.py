#!/usr/bin/env python3
"""Execute 3 task types. Approval matrix enforced."""
import json
from datetime import datetime

def get_approval_level(amount: float) -> str:
    """Route to approval level: auto (<$5K), director ($5K-$25K), ceo_hermes (>$25K)"""
    if amount < 5000:
        return "auto"
    elif amount < 25000:
        return "director"
    else:
        return "ceo_hermes"

def execute_task(agent_id: str, task_type: str, amount: float = 0) -> dict:
    """Execute task with approval check."""
    approval = get_approval_level(amount)
    status = "executed" if approval == "auto" else "pending_approval"

    return {
        "task_id": f"task-{datetime.now().timestamp()}",
        "agent_id": agent_id,
        "task_type": task_type,
        "amount": amount,
        "approval_required": approval,
        "status": status,
        "created_at": datetime.now().isoformat(),
    }

def pilot_tasks() -> dict:
    """Execute 3 task types (1 each)."""
    tasks = [
        execute_task("CON-001-CEO", "estimate-job", amount=8500),  # director approval
        execute_task("FIN-001-CTO", "risk-score", amount=0),  # auto
        execute_task("LOG-001-CFO", "dispatch-job", amount=3200),  # auto
    ]

    return {
        "timestamp": datetime.now().isoformat(),
        "total_tasks": len(tasks),
        "auto_executed": sum(1 for t in tasks if t["status"] == "executed"),
        "pending_approval": sum(1 for t in tasks if t["status"] == "pending_approval"),
        "tasks": tasks,
    }

if __name__ == "__main__":
    result = pilot_tasks()
    with open("/Users/acebless/Documents/pilot_tasks.json", "w") as f:
        json.dump(result, f, indent=2)
    print(f"✅ {result['total_tasks']} tasks: {result['auto_executed']} auto, {result['pending_approval']} await approval")
