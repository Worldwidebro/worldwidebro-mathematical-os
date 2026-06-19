"""
Deal Intake Service — Entry point for construction deals
Receives referrals, classifies them, triggers contract generation
"""

import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional
from flask import Flask, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)

# Initialize Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Service config
SERVICE_PORT = 8001
SERVICE_NAME = "deal_intake"


class DealClassifier:
    """Classify incoming construction deals"""

    @staticmethod
    def estimate_profit(budget: float, sector: str) -> float:
        """Estimate platform profit from deal budget"""
        sector_margins = {
            "CON-011": 0.24,
            "CON-010": 0.22,
            "CON-001": 0.20,
            "default": 0.18
        }
        margin = sector_margins.get(sector, sector_margins["default"])
        platform_cut = 0.12
        return budget * platform_cut

    @staticmethod
    def calculate_deal_score(budget: float, urgency: str, sector: str) -> float:
        """Score deal on 0-100 scale"""
        base_score = 50

        if budget > 100000:
            base_score += 20
        elif budget > 50000:
            base_score += 15
        elif budget > 25000:
            base_score += 10

        urgency_scores = {"urgent": 15, "standard": 5, "flexible": 0}
        base_score += urgency_scores.get(urgency, 0)

        sector_scores = {
            "CON-011": 10,
            "CON-010": 8,
            "CON-020": 5,
        }
        base_score += sector_scores.get(sector, 0)

        return min(base_score, 100)


class DealIntakeService:
    """Main deal intake service"""

    def __init__(self, supabase_client):
        self.db = supabase_client
        self.classifier = DealClassifier()

    def submit_referral(self, payload: Dict) -> Dict:
        """Receive + classify a new construction deal"""

        required = ["contact_id", "job_title", "budget"]
        if not all(k in payload for k in required):
            return {
                "error": "INVALID_INPUT",
                "message": f"Missing required fields: {required}",
                "code": 400
            }

        contact_id = payload["contact_id"]
        job_title = payload["job_title"]
        budget = float(payload["budget"])
        timeline = payload.get("timeline", "standard")
        sector = payload.get("sector", "CON-001")
        contractor_ids = payload.get("contractor_ids", [])
        referrer_id = payload.get("referrer_id")

        deal_id = f"deal_{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:6]}"

        estimated_profit = self.classifier.estimate_profit(budget, sector)
        deal_score = self.classifier.calculate_deal_score(budget, timeline, sector)

        deal_record = {
            "id": deal_id,
            "contact_id": contact_id,
            "contact_name": payload.get("contact_name"),
            "job_title": job_title,
            "job_description": payload.get("job_description"),
            "budget": budget,
            "timeline": timeline,
            "sector": sector,
            "contractor_ids": contractor_ids,
            "referrer_id": referrer_id,
            "estimated_profit": estimated_profit,
            "deal_score": deal_score,
            "status": "pending_contract",
            "created_at": datetime.utcnow().isoformat(),
            "metadata": {
                "source": "referral_network",
                "auto_classified": True
            }
        }

        try:
            response = self.db.table("deals").insert(deal_record).execute()

            return {
                "deal_id": deal_id,
                "status": "pending_contract",
                "estimated_profit": estimated_profit,
                "deal_score": deal_score,
                "next_step": "Auto-generated contracts sent. Awaiting signature.",
                "contracts_ready": True,
                "agent_assigned": "coo_agent_1",
                "created_at": deal_record["created_at"]
            }

        except Exception as e:
            return {
                "error": "DB_ERROR",
                "message": str(e),
                "code": 500
            }


intake_service = DealIntakeService(supabase)


@app.route("/mcp/tools/submit_referral", methods=["POST"])
def submit_referral():
    """MCP endpoint: submit_referral"""
    try:
        payload = request.get_json()
        result = intake_service.submit_referral(payload)

        if "error" in result:
            return jsonify(result), result.get("code", 400)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": "SERVICE_ERROR",
            "message": str(e),
            "code": 500
        }), 500


@app.route("/health", methods=["GET"])
def health():
    """Health check"""
    return jsonify({
        "status": "healthy",
        "service": SERVICE_NAME,
        "timestamp": datetime.utcnow().isoformat()
    }), 200


if __name__ == "__main__":
    print(f"🚀 {SERVICE_NAME} service starting on port {SERVICE_PORT}")
    app.run(host="0.0.0.0", port=SERVICE_PORT, debug=True)
