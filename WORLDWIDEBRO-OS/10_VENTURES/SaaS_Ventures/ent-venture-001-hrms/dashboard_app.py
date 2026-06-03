#!/usr/bin/env python3
"""HRMS Dashboard: Real-time cluster health, deployment gates, agent authority, and SLA compliance."""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any

# Flask imports (minimal for now)
try:
    from flask import Flask, jsonify, render_template_string
    HAS_FLASK = True
except ImportError:
    HAS_FLASK = False

parent_dir = str(Path(__file__).parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from registry_loader import RegistryLoader
from monitoring_engine import MonitoringEngine


class DashboardAPI:
    """API endpoints for the HRMS dashboard."""

    def __init__(self):
        """Initialize dashboard with registry and monitoring engine."""
        self.loader = RegistryLoader()
        self.engine = MonitoringEngine(self.loader)

    def get_health_report(self) -> Dict[str, Any]:
        """Get comprehensive cluster health report."""
        return self.engine.generate_health_report()

    def get_tier_status(self, tier_num: int) -> Dict[str, Any]:
        """Get status for a specific tier."""
        tier_key = f"tier_{tier_num}_"
        tier_map = {
            0: "tier_0_foundation",
            1: "tier_1_core_infrastructure",
            2: "tier_2_ventures",
            3: "tier_3_templates"
        }

        report = self.engine.generate_health_report()
        return report.get("checks", {}).get(tier_map.get(tier_num, ""), {})

    def get_deployment_gates(self) -> Dict[str, Any]:
        """Get deployment gate status."""
        report = self.engine.generate_health_report()
        return report.get("checks", {}).get("deployment_gates", {})

    def get_agent_authority(self) -> Dict[str, Any]:
        """Get agent authority matrix (RACI roles)."""
        report = self.engine.generate_health_report()
        return report.get("checks", {}).get("agent_authority", {})

    def get_shared_services(self) -> Dict[str, Any]:
        """Get shared services coverage map."""
        report = self.engine.generate_health_report()
        return report.get("checks", {}).get("shared_services", {})

    def get_sla_compliance_summary(self) -> Dict[str, Any]:
        """Get SLA compliance summary across all agents."""
        # Placeholder: In production, query Supabase cluster_health and agent_sla_compliance tables
        # For now, return mock data structure
        return {
            "overall_compliance": 95.5,
            "by_agent": {
                "hrms-sales-ai-001": {"on_time": 18, "breaches": 1, "compliance": 94.7},
                "hrms-support-ai-001": {"on_time": 24, "breaches": 0, "compliance": 100.0},
                "hrms-product-ai-001": {"on_time": 12, "breaches": 0, "compliance": 100.0},
                "hrms-operations-ai-001": {"on_time": 48, "breaches": 2, "compliance": 96.0},
            },
            "by_sla_type": {
                "Sales Deals >$500/month": {"target": "8h", "compliance": 94.7},
                "Support Escalations": {"target": "4h", "compliance": 100.0},
                "Dispatch Route Calculation": {"target": "5s", "compliance": 100.0},
                "Urgent: 1h SLA": {"target": "1h", "compliance": 92.0},
            },
            "last_updated": datetime.utcnow().isoformat() + "Z"
        }


def create_flask_app() -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)
    api = DashboardAPI()

    @app.route("/api/health", methods=["GET"])
    def health():
        """Get full health report."""
        return jsonify(api.get_health_report())

    @app.route("/api/tier/<int:tier>", methods=["GET"])
    def tier_status(tier):
        """Get tier-specific status."""
        return jsonify(api.get_tier_status(tier))

    @app.route("/api/gates", methods=["GET"])
    def gates():
        """Get deployment gate status."""
        return jsonify(api.get_deployment_gates())

    @app.route("/api/authority", methods=["GET"])
    def authority():
        """Get agent authority matrix."""
        return jsonify(api.get_agent_authority())

    @app.route("/api/services", methods=["GET"])
    def services():
        """Get shared services coverage."""
        return jsonify(api.get_shared_services())

    @app.route("/api/sla-compliance", methods=["GET"])
    def sla_compliance():
        """Get SLA compliance summary."""
        return jsonify(api.get_sla_compliance_summary())

    @app.route("/", methods=["GET"])
    def dashboard_html():
        """Serve HTML dashboard."""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>HRMS Cluster Dashboard</title>
            <style>
                body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
                .container { max-width: 1400px; margin: 0 auto; }
                h1 { color: #333; border-bottom: 3px solid #007bff; padding-bottom: 10px; }
                .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }
                .card { background: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
                .tier-0 { border-left: 4px solid #28a745; }
                .tier-1 { border-left: 4px solid #ffc107; }
                .tier-2 { border-left: 4px solid #17a2b8; }
                .tier-3 { border-left: 4px solid #6f42c1; }
                .status-healthy { color: #28a745; font-weight: bold; }
                .status-warning { color: #ffc107; font-weight: bold; }
                .status-critical { color: #dc3545; font-weight: bold; }
                .metric { margin: 10px 0; display: flex; justify-content: space-between; }
                .metric-label { font-weight: 500; }
                .metric-value { text-align: right; }
                pre { background: #f8f9fa; padding: 15px; border-radius: 4px; overflow: auto; font-size: 12px; }
                .agents-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; }
                .agent-card { background: #f8f9fa; padding: 15px; border-radius: 4px; border: 1px solid #ddd; }
                .agent-name { font-weight: bold; margin-bottom: 8px; }
                .agent-stat { font-size: 12px; margin: 4px 0; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🏥 HRMS Cluster Dashboard</h1>

                <div class="grid">
                    <div class="card tier-0">
                        <h3>Tier 0: Foundation</h3>
                        <div id="tier0-content">Loading...</div>
                    </div>
                    <div class="card tier-1">
                        <h3>Tier 1: Core Infrastructure</h3>
                        <div id="tier1-content">Loading...</div>
                    </div>
                </div>

                <div class="grid">
                    <div class="card tier-2">
                        <h3>Tier 2: Ventures</h3>
                        <div id="tier2-content">Loading...</div>
                    </div>
                    <div class="card tier-3">
                        <h3>Tier 3: Templates</h3>
                        <div id="tier3-content">Loading...</div>
                    </div>
                </div>

                <div class="card">
                    <h3>⚙️ Deployment Gates</h3>
                    <div id="gates-content">Loading...</div>
                </div>

                <div class="card">
                    <h3>🔐 Agent Authority Matrix</h3>
                    <div class="agents-grid" id="authority-content">Loading...</div>
                </div>

                <div class="card">
                    <h3>📊 SLA Compliance</h3>
                    <div id="sla-content">Loading...</div>
                </div>

                <div class="card">
                    <h3>🔌 Shared Services Coverage</h3>
                    <pre id="services-content">Loading...</pre>
                </div>
            </div>

            <script>
                async function loadDashboard() {
                    try {
                        const health = await fetch('/api/health').then(r => r.json());
                        const gates = await fetch('/api/gates').then(r => r.json());
                        const authority = await fetch('/api/authority').then(r => r.json());
                        const sla = await fetch('/api/sla-compliance').then(r => r.json());
                        const services = await fetch('/api/services').then(r => r.json());

                        // Render tiers
                        for (let tier = 0; tier < 4; tier++) {
                            const tier_key = `tier_${tier}_foundation`;
                            const tier_data = health.checks[Object.keys(health.checks).find(k => k.startsWith(`tier_${tier}`))];
                            const repos = tier_data?.repos || {};
                            let html = '<div>';
                            for (const [repo, data] of Object.entries(repos)) {
                                html += `<div class="metric"><span>${repo}</span><span class="status-healthy">OK</span></div>`;
                            }
                            html += '</div>';
                            document.getElementById(`tier${tier}-content`).innerHTML = html;
                        }

                        // Render gates
                        let gates_html = '';
                        for (const [gate, data] of Object.entries(gates)) {
                            gates_html += `<div class="metric"><span>${data.name}</span><span>${data.status}</span></div>`;
                        }
                        document.getElementById('gates-content').innerHTML = gates_html;

                        // Render authority
                        let auth_html = '';
                        for (const [agent, data] of Object.entries(authority)) {
                            auth_html += `<div class="agent-card">
                                <div class="agent-name">${agent}</div>
                                <div class="agent-stat">Authority: ${data.decision_authority}</div>
                                <div class="agent-stat">Primary: ${data.primary_repos.length}</div>
                                <div class="agent-stat">Secondary: ${data.secondary_repos.length}</div>
                            </div>`;
                        }
                        document.getElementById('authority-content').innerHTML = auth_html;

                        // Render SLA
                        let sla_html = `<div class="metric">
                            <span>Overall Compliance</span>
                            <span class="metric-value status-healthy">${sla.overall_compliance}%</span>
                        </div>`;
                        for (const [agent, data] of Object.entries(sla.by_agent)) {
                            sla_html += `<div class="metric">
                                <span>${agent}</span>
                                <span class="metric-value">${data.compliance}%</span>
                            </div>`;
                        }
                        document.getElementById('sla-content').innerHTML = sla_html;

                        // Render services
                        document.getElementById('services-content').innerText = JSON.stringify(services, null, 2);
                    } catch (e) {
                        console.error('Dashboard load failed:', e);
                    }
                }

                loadDashboard();
                setInterval(loadDashboard, 30000); // Refresh every 30s
            </script>
        </body>
        </html>
        """
        return render_template_string(html)

    return app


if __name__ == "__main__":
    if HAS_FLASK:
        app = create_flask_app()
        print("Starting HRMS Dashboard on http://localhost:5000")
        app.run(debug=True, host="localhost", port=5000)
    else:
        # Fallback: print API responses
        api = DashboardAPI()
        print("=== HRMS Cluster Health Report ===\n")
        print(json.dumps(api.get_health_report(), indent=2))
        print("\n=== SLA Compliance Summary ===\n")
        print(json.dumps(api.get_sla_compliance_summary(), indent=2))
