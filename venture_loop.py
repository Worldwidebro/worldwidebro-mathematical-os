#!/usr/bin/env python3
"""
venture_loop.py — the first closed execution loop (Phase 1 template).

Turns a trigger into a dispatch-ready ACTION PACKET, reusing what already exists:
  trigger -> retrieve.py (repos+venture) -> Neo4j (capabilities+tools) -> action packet
The last mile (create ClickUp task / HubSpot lead) is done via MCP/Zapier from the packet —
this script DECIDES; the MCP layer DISPATCHES. Phases 2-4 reuse this unchanged per venture.

Also appends every run to runs.jsonl = the run/experiment log (the "black box recorder").

Local only (Ollama + Qdrant + Neo4j). No new framework.

Usage:
  python3 venture_loop.py "PS-024-Recruiting-Agency" "Need a senior recruiter lead, remote"
  python3 venture_loop.py "CON-001-ACE-CONSTRUCTION" "Client needs 5 electricians in Charlotte"
"""
import json
import os
import sys
from datetime import datetime

from dotenv import load_dotenv
from neo4j import GraphDatabase
from supabase import create_client
import retrieve  # reuse the existing retrieval engine

load_dotenv()  # picks up SUPABASE_URL / SUPABASE_KEY from ~/.env

NEO4J = ("bolt://localhost:7687", ("neo4j", "ventures2026"))
RUNLOG = "/Users/acebless/Documents/runs.jsonl"


def venture_tools_and_caps(venture_id):
    d = GraphDatabase.driver(NEO4J[0], auth=NEO4J[1])
    with d.session() as s:
        rec = s.run("""
            MATCH (v:Venture {id:$id})
            OPTIONAL MATCH (v)-[:NEEDS]->(c:Capability)
            OPTIONAL MATCH (c)<-[:PROVIDES]-(m:MCP)
            OPTIONAL MATCH (v)-[:BELONGS_TO]->(o:OPCO)
            RETURN v.name AS name, o.id AS opco,
                   collect(DISTINCT c.name) AS caps,
                   collect(DISTINCT m.name) AS tools
        """, id=venture_id).single()
    d.close()
    return rec


def build_packet(venture_id, trigger):
    bundle = retrieve.retrieve(trigger, k=5)          # repos + venture match
    info = venture_tools_and_caps(venture_id)
    if not info or not info["name"]:
        return {"error": f"venture {venture_id} not found in graph"}
    tools = [t for t in info["tools"] if t]
    repos = [r["name"] for r in bundle["repos"][:5]]

    # decide dispatch targets from the venture's tool set
    crm = "HubSpot" if "HubSpot" in tools else ("Airtable" if "Airtable" in tools else "Supabase")
    task_tool = "ClickUp"  # ops always to ClickUp

    packet = {
        "run_id": datetime.now().strftime("%Y%m%dT%H%M%S"),
        "ts": datetime.now().isoformat(),
        "venture_id": venture_id,
        "venture": info["name"],
        "opco": info["opco"],
        "trigger": trigger,
        "capabilities_needed": info["caps"],
        "tools_available": tools,
        "repos_to_use": repos,
        "dispatch": {
            task_tool: {
                "action": "create_task",
                "name": f"[{info['name']}] {trigger[:60]}",
                "description": f"Trigger: {trigger}\nVenture: {info['name']} (OPCO {info['opco']})\n"
                               f"Capabilities: {', '.join(info['caps'])}\n"
                               f"Candidate repos: {', '.join(repos)}\nTools: {', '.join(tools)}",
            },
            crm: {
                "action": "create_lead",
                "name": trigger[:80],
                "source": f"venture_loop:{venture_id}",
            },
        },
    }
    return packet


def log_to_supabase(packet):
    """Insert a pending row into venture_executions. Returns the row id, or
    None if Supabase isn't configured (script still works via runs.jsonl)."""
    url, key = os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")
    if not url or not key:
        return None
    sb = create_client(url, key)
    row = {
        "venture_id": packet["venture_id"],
        "request": packet["trigger"],
        "capabilities": packet["capabilities_needed"],
        "matched_repos": packet["repos_to_use"],
        "workflow": "venture_loop",
        "status": "pending",
        "result": {"dispatch": packet["dispatch"], "run_id": packet["run_id"]},
    }
    res = sb.table("venture_executions").insert(row).execute()
    return res.data[0]["id"] if res.data else None


def main():
    # Handle --deploy flag (called by capital-routing.ts)
    if len(sys.argv) >= 3 and sys.argv[1] == '--deploy':
        try:
            payload = json.loads(sys.argv[2])
            for venture_id in payload.get('ventures', []):
                trigger = f"Capital Deployment: {payload.get('decision_id', 'unknown')}"
                packet = build_packet(venture_id, trigger)
                if "error" not in packet:
                    print(json.dumps(packet, indent=2))
                    with open(RUNLOG, "a") as f:
                        f.write(json.dumps(packet) + "\n")
                    log_to_supabase(packet)
            return
        except json.JSONDecodeError as e:
            print(f"error: invalid JSON payload: {e}", file=sys.stderr)
            return

    # Original trigger-based flow
    if len(sys.argv) < 3:
        print(__doc__)
        return
    venture_id, trigger = sys.argv[1], " ".join(sys.argv[2:])
    packet = build_packet(venture_id, trigger)
    print(json.dumps(packet, indent=2))
    with open(RUNLOG, "a") as f:
        f.write(json.dumps(packet) + "\n")
    if "error" not in packet:
        execution_id = log_to_supabase(packet)
        note = f"venture_executions row {execution_id}" if execution_id else "SUPABASE_URL/KEY not set, skipped"
        print(f"\n[logged to runs.jsonl | {note} | dispatch via MCP/Zapier: "
              f"{', '.join(packet['dispatch'].keys())}]", file=sys.stderr)


if __name__ == "__main__":
    main()
