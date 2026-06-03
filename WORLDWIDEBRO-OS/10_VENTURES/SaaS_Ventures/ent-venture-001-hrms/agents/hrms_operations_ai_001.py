#!/usr/bin/env python3
"""HRMS Operations Agent: hourly cluster health checks with Slack reporting."""

import json
import sys
from datetime import datetime
from typing import Dict, Any, List

# Add parent directory to path for imports
from pathlib import Path
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from registry_loader import RegistryLoader
from monitoring_engine import MonitoringEngine


class OperationsAgent:
    """Hourly health check agent for cluster monitoring and SLA compliance."""

    def __init__(self):
        """Initialize agent with registry and monitoring engine."""
        self.loader = RegistryLoader()
        self.engine = MonitoringEngine(self.loader)
        self.agent_id = "hrms-operations-ai-001"
        self.slack_channel = "#hrms"

    def hourly_health_check(self) -> Dict[str, Any]:
        """Execute hourly cluster health check and report status."""
        # Step 1: Generate comprehensive health report from all tiers
        report = self.engine.generate_health_report()

        # Step 2: Check for SLA breaches
        alerts = self.check_sla_breaches(report)

        # Step 3: Validate deployment gates
        gate_breaches = self.check_deployment_gates(report)

        # Step 4: Post to Slack if critical alerts
        if alerts or gate_breaches:
            slack_msg = self.engine.export_for_slack()
            self.post_to_slack(slack_msg)

        # Step 5: Log health report to Supabase (placeholder for integration)
        self.log_health_report_to_supabase(report)

        return {
            "status": "completed",
            "timestamp": report["timestamp"],
            "alerts_count": len(alerts),
            "gate_breaches": len(gate_breaches),
            "message": f"Health check complete: {len(alerts)} alerts, {len(gate_breaches)} gate issues"
        }

    def check_sla_breaches(self, report: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for SLA breaches across all tiers and repos."""
        breaches = []

        # Check each tier's SLA targets
        for tier_key in ["tier_0_foundation", "tier_1_core_infrastructure", "tier_2_ventures", "tier_3_templates"]:
            tier_check = report.get("checks", {}).get(tier_key, {})
            tier_repos = tier_check.get("repos", {})

            for repo_name, repo_data in tier_repos.items():
                sla_targets = repo_data.get("sla_targets", {})
                # In a real implementation, would check against actual metrics
                # For now, just track that SLA targets exist for this repo
                if sla_targets:
                    # Example: Check if monitoring indicates SLA breach
                    # status = repo_data.get("status", "unknown")
                    # if status == "breached":
                    #     breaches.append({...})
                    pass

        return breaches

    def check_deployment_gates(self, report: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check deployment gate status for blockers."""
        breaches = []
        gates = report.get("checks", {}).get("deployment_gates", {})

        for gate_name, gate_data in gates.items():
            status = gate_data.get("status", "unknown")
            # Track gates that are blocking
            if status == "blocked_for_2h":
                breaches.append({
                    "severity": "warning",
                    "gate": gate_name,
                    "action": "investigate_blocker"
                })

        return breaches

    def post_to_slack(self, message: str) -> Dict[str, Any]:
        """Post health report to Slack #hrms channel."""
        # Placeholder for actual Slack integration
        # In production, would use slack_sdk.WebClient
        print(f"[SLACK] {self.slack_channel}")
        print(message)
        return {
            "ok": True,
            "channel": self.slack_channel,
            "timestamp": datetime.utcnow().isoformat()
        }

    def log_health_report_to_supabase(self, report: Dict[str, Any]) -> Dict[str, Any]:
        """Log health report to Supabase cluster_health table."""
        # Placeholder for Supabase integration
        # In production, would use supabase.table("cluster_health").insert(...)

        payload = {
            "timestamp": report.get("timestamp"),
            "agent_id": self.agent_id,
            "venture_id": report.get("venture_id"),
            "venture_name": report.get("venture_name"),
            # Extract tier statuses
            "tier_0_status": report.get("checks", {}).get("tier_0_foundation", {}).get("status", "unknown"),
            "tier_1_status": report.get("checks", {}).get("tier_1_core_infrastructure", {}).get("status", "unknown"),
            "tier_2_status": report.get("checks", {}).get("tier_2_ventures", {}).get("status", "unknown"),
            "tier_3_status": report.get("checks", {}).get("tier_3_templates", {}).get("status", "unknown"),
            "alerts_count": len(report.get("alerts", [])),
            "sla_breaches_count": len(report.get("sla_breaches", [])),
        }

        print(f"[SUPABASE] Would insert into cluster_health: {json.dumps(payload, indent=2)}")
        return payload

    def validate_agent_authority(self) -> Dict[str, Any]:
        """Check if agent has decision authority for operations."""
        repos = self.loader.get_agent_repos(self.agent_id)
        authority = repos.get("decision_authority")

        return {
            "agent_id": self.agent_id,
            "decision_authority": authority,
            "primary_repos": repos.get("primary_repos", []),
            "secondary_repos": repos.get("secondary_repos", []),
            "escalation_to": repos.get("escalation_to"),
            "monitoring_frequency": repos.get("monitoring_frequency")
        }


if __name__ == "__main__":
    # Initialize agent
    agent = OperationsAgent()

    # Validate agent authority
    print("=== Agent Authority ===")
    authority = agent.validate_agent_authority()
    print(json.dumps(authority, indent=2))

    print("\n=== Running Hourly Health Check ===")
    result = agent.hourly_health_check()
    print(json.dumps(result, indent=2))
