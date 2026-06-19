"""Orchestrator — Routes deals to agents"""
import uuid
from datetime import datetime
from flask import Flask, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

class Orchestrator:
    def route_deal(self, deal_id: str, event: str) -> dict:
        agent_map = {
            "deal_submitted": "coo_agent_1",
            "job_started": "ops_agent_1",
            "job_completed": "finance_agent_1",
            "dispute": "legal_agent_1"
        }
        task_id = f"task_{uuid.uuid4().hex[:8]}"
        return {
            "deal_id": deal_id,
            "event": event,
            "agent_assigned": agent_map.get(event, "coo_agent_1"),
            "task_id": task_id,
            "created_at": datetime.utcnow().isoformat()
        }

orchestrator = Orchestrator()

@app.route("/mcp/tools/route_deal", methods=["POST"])
def route():
    payload = request.get_json()
    return jsonify(orchestrator.route_deal(payload.get("deal_id"), payload.get("event"))), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8004, debug=True)
