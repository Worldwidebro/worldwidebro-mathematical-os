#!/usr/bin/env python3
"""Spawn 10 venture agents (CEO/CTO/CFO per venture). Pilot for scaling to 712."""
import json
from datetime import datetime

PILOT_VENTURES = [
    "CON-001", "CON-002", "STA-001", "RE-001", "EDU-001",
    "FIN-001", "LOG-001", "TECH-001", "HEALTH-001", "RETAIL-001"
]

AGENT_ROLES = ["CEO", "CTO", "CFO"]

VENTURE_DB = {
    "CON-001": {"opco": "Construction", "stage": "active", "mrr": 5000},
    "CON-002": {"opco": "Construction", "stage": "building", "mrr": 0},
    "STA-001": {"opco": "Staffing", "stage": "active", "mrr": 3500},
    "RE-001": {"opco": "RealEstate", "stage": "active", "mrr": 8000},
    "EDU-001": {"opco": "Education", "stage": "planning", "mrr": 0},
    "FIN-001": {"opco": "Finance", "stage": "active", "mrr": 12000},
    "LOG-001": {"opco": "Logistics", "stage": "active", "mrr": 6500},
    "TECH-001": {"opco": "Technology", "stage": "building", "mrr": 0},
    "HEALTH-001": {"opco": "Healthcare", "stage": "planning", "mrr": 0},
    "RETAIL-001": {"opco": "Retail", "stage": "active", "mrr": 2000},
}

def spawn_agent(venture_id: str, role: str) -> dict:
    """Create one agent instance."""
    venture = VENTURE_DB[venture_id]
    return {
        "agent_id": f"{venture_id}-{role}",
        "venture_id": venture_id,
        "role": role,
        "opco": venture["opco"],
        "status": "spawned",
        "created_at": datetime.now().isoformat(),
        "task_queue": [],
    }

def spawn_venture(venture_id: str) -> dict:
    """Create 3 agents for one venture."""
    agents = {}
    for role in AGENT_ROLES:
        agent = spawn_agent(venture_id, role)
        agents[agent["agent_id"]] = agent
    return {"venture_id": venture_id, "agents": agents}

def pilot() -> dict:
    """Spawn agents for 10 ventures."""
    return {
        "timestamp": datetime.now().isoformat(),
        "venture_count": len(PILOT_VENTURES),
        "agent_count": len(PILOT_VENTURES) * len(AGENT_ROLES),
        "ventures": {v: spawn_venture(v) for v in PILOT_VENTURES},
    }

if __name__ == "__main__":
    agents = pilot()
    with open("/Users/acebless/Documents/pilot_agents.json", "w") as f:
        json.dump(agents, f, indent=2)
    print(f"✅ {agents['agent_count']} agents for {agents['venture_count']} ventures")
