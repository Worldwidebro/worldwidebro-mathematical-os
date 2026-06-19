"""Graph Memory — Updates reputation + learning graph"""
import uuid
from datetime import datetime
from flask import Flask, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

class GraphMemory:
    def update_graph_memory(self, deal_id: str, completion_data: dict) -> dict:
        contractor_id = completion_data.get("contractor_id")
        quality = completion_data.get("quality_rating", 85)
        speed = completion_data.get("speed_rating", 85)
        compliance = completion_data.get("compliance_rating", 85)
        efficiency = completion_data.get("efficiency_rating", 85)
        communication = completion_data.get("communication_rating", 85)
        
        score = (quality*0.40 + speed*0.25 + compliance*0.20 + efficiency*0.10 + communication*0.05)
        tier = "S" if score >= 90 else "A" if score >= 80 else "B" if score >= 70 else "C"
        
        update_id = f"update_{uuid.uuid4().hex[:8]}"
        supabase.table("graph_updates").insert({
            "id": update_id, "deal_id": deal_id, "contractor_id": contractor_id,
            "score": round(score, 1), "tier": tier, "created_at": datetime.utcnow().isoformat()
        }).execute()
        
        return {
            "graph_update_id": update_id,
            "deal_id": deal_id,
            "contractor_new_score": round(score, 1),
            "contractor_new_tier": tier,
            "entities_updated": 1,
            "relationships_created": 1
        }

memory = GraphMemory()

@app.route("/mcp/tools/update_graph_memory", methods=["POST"])
def update():
    payload = request.get_json()
    return jsonify(memory.update_graph_memory(payload.get("deal_id"), payload.get("completion_data"))), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8005, debug=True)
