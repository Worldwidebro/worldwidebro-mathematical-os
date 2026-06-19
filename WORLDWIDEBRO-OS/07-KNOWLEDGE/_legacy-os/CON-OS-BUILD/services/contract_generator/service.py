"""
Contract Generator Service — Auto-generates 4 contract types
Client, Contractor, Referral, Platform agreements
"""

import uuid
from datetime import datetime
from flask import Flask, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

SERVICE_PORT = 8002
SERVICE_NAME = "contract_generator"


class ContractTemplate:
    """Contract template generator"""

    CLIENT_CONTRACT = """CLIENT AGREEMENT
Date: {date}
Client: {client_name}
Contractor: {contractor_name}
Job: {job_title}
Budget: ${budget}
Timeline: {timeline}
Scope: {job_description}
Terms:
- Final cost: ${budget}
- Payment due upon completion
- Changes require written approval
"""

    CONTRACTOR_AGREEMENT = """CONTRACTOR LABOR AGREEMENT
Date: {date}
Contractor: {contractor_name}
Job: {job_title}
Labor Rate: ${labor_rate}/hour
Timeline: {timeline}
Payment: 50% at start, 50% at completion
"""

    REFERRAL_AGREEMENT = """REFERRAL COMMISSION AGREEMENT
Date: {date}
Referrer: {referrer_name}
Job: {job_title}
Project Value: ${budget}
Commission: {referral_percent}% = ${referral_amount}
Payment: Upon completion via {payment_method}
"""

    PLATFORM_TERMS = """PLATFORM TERMS
Project: {job_title}
Date: {date}
Platform Fee: {platform_percent}% = ${platform_fee}
Services: Contractor matching, contracts, payments, disputes
"""


class ContractGeneratorService:
    """Generate contracts from deals"""

    def __init__(self, supabase_client):
        self.db = supabase_client

    def generate_contracts(self, deal_id: str, deal_data: dict) -> dict:
        """Generate all 4 contract types"""

        try:
            deal = self.db.table("deals").select("*").eq("id", deal_id).execute()
            if not deal.data:
                return {"error": "DEAL_NOT_FOUND", "code": 404}

            deal = deal.data[0]

            labor_amount = deal["budget"] * 0.40
            referral_amount = deal["budget"] * 0.10
            platform_amount = deal["budget"] * 0.12

            contracts = {}

            client_contract = ContractTemplate.CLIENT_CONTRACT.format(
                date=datetime.now().strftime("%Y-%m-%d"),
                client_name=deal.get("contact_name", "Client"),
                contractor_name="[Contractor Name]",
                job_title=deal["job_title"],
                budget=deal["budget"],
                timeline=deal.get("timeline", "standard"),
                job_description=deal.get("job_description", "")
            )
            contracts["client"] = client_contract

            contractor_agreement = ContractTemplate.CONTRACTOR_AGREEMENT.format(
                date=datetime.now().strftime("%Y-%m-%d"),
                contractor_name="[Contractor Name]",
                job_title=deal["job_title"],
                labor_rate=int(labor_amount / 40),
                timeline=deal.get("timeline", "standard")
            )
            contracts["contractor"] = contractor_agreement

            referral_agreement = ContractTemplate.REFERRAL_AGREEMENT.format(
                date=datetime.now().strftime("%Y-%m-%d"),
                referrer_name=deal.get("referrer_id", "Referrer"),
                job_title=deal["job_title"],
                budget=deal["budget"],
                referral_percent=10,
                referral_amount=int(referral_amount),
                payment_method="Bank Transfer"
            )
            contracts["referral"] = referral_agreement

            platform_terms = ContractTemplate.PLATFORM_TERMS.format(
                job_title=deal["job_title"],
                date=datetime.now().strftime("%Y-%m-%d"),
                platform_percent=12,
                platform_fee=int(platform_amount)
            )
            contracts["platform"] = platform_terms

            contract_id = f"contracts_{deal_id}_{uuid.uuid4().hex[:6]}"
            contract_record = {
                "id": contract_id,
                "deal_id": deal_id,
                "contracts": contracts,
                "status": "ready_for_signing",
                "created_at": datetime.utcnow().isoformat()
            }

            self.db.table("contracts").insert(contract_record).execute()

            return {
                "deal_id": deal_id,
                "contract_id": contract_id,
                "contracts_generated": list(contracts.keys()),
                "status": "ready_for_signing",
                "contract_count": len(contracts),
                "created_at": contract_record["created_at"]
            }

        except Exception as e:
            return {"error": "SERVICE_ERROR", "message": str(e), "code": 500}


generator_service = ContractGeneratorService(supabase)


@app.route("/mcp/tools/generate_contracts", methods=["POST"])
def generate_contracts():
    """MCP endpoint: generate_contracts"""
    try:
        payload = request.get_json()
        deal_id = payload.get("deal_id")

        if not deal_id:
            return jsonify({"error": "INVALID_INPUT"}), 400

        result = generator_service.generate_contracts(deal_id, payload)

        if "error" in result:
            return jsonify(result), result.get("code", 400)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": "SERVICE_ERROR", "message": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": SERVICE_NAME,
        "timestamp": datetime.utcnow().isoformat()
    }), 200


if __name__ == "__main__":
    print(f"🚀 {SERVICE_NAME} service starting on port {SERVICE_PORT}")
    app.run(host="0.0.0.0", port=SERVICE_PORT, debug=True)
