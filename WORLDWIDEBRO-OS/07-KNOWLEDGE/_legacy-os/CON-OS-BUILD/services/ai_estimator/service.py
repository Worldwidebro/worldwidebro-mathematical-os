"""AI Estimating Service — Auto-estimates job costs"""
import json
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

class AIEstimator:
    LABOR_RATES = {
        "drywall": 85, "flooring": 95, "electrical": 120,
        "plumbing": 110, "hvac": 105, "roofing": 130
    }
    
    MATERIAL_MARKUPS = {
        "drywall": 1.35, "flooring": 1.40, "electrical": 1.45,
        "plumbing": 1.40, "hvac": 1.35, "roofing": 1.45
    }
    
    REGIONAL_FACTORS = {
        "charlotte": 0.95, "new_york": 1.25, "florida": 1.05,
        "california": 1.20, "texas": 0.92, "default": 1.0
    }

    def estimate(self, job_data):
        location = job_data.get("location", "default").lower()
        trade = job_data.get("trade", "drywall")
        hours = job_data.get("hours", 0)
        materials = job_data.get("materials", {})
        
        regional_factor = self.REGIONAL_FACTORS.get(location, 1.0)
        labor_cost = hours * self.LABOR_RATES.get(trade, 85) * regional_factor
        
        material_cost = sum(qty * self.MATERIAL_MARKUPS.get(trade, 1.35) * regional_factor 
                           for qty in materials.values())
        
        total = labor_cost + material_cost
        return {
            "labor_cost": round(labor_cost, 2),
            "material_cost": round(material_cost, 2),
            "total_estimate": round(total, 2),
            "platform_profit": round(total * 0.12, 2),
            "confidence": 0.82
        }

estimator = AIEstimator()

@app.route("/mcp/tools/estimate_job", methods=["POST"])
def estimate():
    return jsonify(estimator.estimate(request.get_json())), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8006, debug=True)
