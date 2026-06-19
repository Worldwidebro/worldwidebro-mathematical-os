"""Payout Engine — Splits payment per model"""
import uuid, json
from datetime import datetime
from flask import Flask, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

class PayoutEngine:
    def trigger_payment_distribution(self, deal_id: str, total: float) -> dict:
        try:
            splits = [
                {"type": "labor", "amount": round(total * 0.40, 2), "percent": 40},
                {"type": "subcontractor", "amount": round(total * 0.20, 2), "percent": 20},
                {"type": "referral", "amount": round(total * 0.10, 2), "percent": 10},
                {"type": "platform", "amount": round(total * 0.12, 2), "percent": 12},
                {"type": "reserve", "amount": round(total * 0.08, 2), "percent": 8}
            ]
            payment_id = f"pay_{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:6]}"
            supabase.table("payments").insert({
                "id": payment_id, "deal_id": deal_id, "total_payment": total,
                "splits": splits, "status": "routing", "created_at": datetime.utcnow().isoformat()
            }).execute()
            return {"payment_id": payment_id, "total_payment": total, "splits": splits, "status": "routing"}
        except Exception as e:
            return {"error": "SERVICE_ERROR", "message": str(e), "code": 500}

engine = PayoutEngine()

@app.route("/mcp/tools/trigger_payment_distribution", methods=["POST"])
def trigger():
    payload = request.get_json()
    result = engine.trigger_payment_distribution(payload.get("deal_id"), payload.get("total_payment"))
    return jsonify(result), 200 if "error" not in result else 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003, debug=True)
