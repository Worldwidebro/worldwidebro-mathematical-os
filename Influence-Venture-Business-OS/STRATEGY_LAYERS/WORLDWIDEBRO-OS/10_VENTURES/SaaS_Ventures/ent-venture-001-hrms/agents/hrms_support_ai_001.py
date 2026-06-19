#!/usr/bin/env python3
"""HRMS Support Agent: escalation decisions with SLA tracking."""

import json
import sys
from datetime import datetime
from typing import Dict, Any
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from registry_loader import RegistryLoader


class SupportAgent:
    """Customer support escalation agent with SLA compliance tracking."""

    def __init__(self):
        """Initialize agent with registry loader."""
        self.loader = RegistryLoader()
        self.agent_id = "hrms-support-ai-001"

    def handle_escalation(self, escalation_type: str, ticket_id: str) -> Dict[str, Any]:
        """Handle customer escalation with authority validation and SLA tracking."""
        # Step 1: Check if I have authority to escalate
        repos = self.loader.get_agent_repos(self.agent_id)
        authority = repos.get("decision_authority")

        if authority != "operational":
            # No escalation authority, escalate to founder
            return self.escalate_to_founder(ticket_id, "No escalation authority")

        # Step 2: Get SLA targets for this escalation type
        # SLA targets are stored per repo, aggregate for support function
        sla_targets = {}
        for repo_name in repos.get("primary_repos", []):
            metrics = self.loader.get_repo_monitoring_metrics(repo_name)
            sla_targets.update(metrics.get("sla_targets", {}))

        # Map escalation types to SLA targets
        sla_map = {
            "general_inquiry": "Support Inquiries: 8h SLA",
            "technical_issue": "Support Escalations: 4h SLA",
            "urgent_outage": "Urgent: 1h SLA",
            "billing_dispute": "Payment Disputes: 24h SLA",
            "compliance_issue": "Compliance/Audit: 48h SLA",
        }
        sla_target = sla_map.get(escalation_type, "Support: 8h SLA")

        # Step 3: Validate access to venture-hub for customer lookup
        access = self.loader.validate_repo_access("venture-hub", self.agent_id)
        if not access["valid"]:
            return self.escalate_to_founder(ticket_id, f"Cannot access venture-hub: {access['error']}")

        # Step 4: Route decision and log to Supabase
        decision = {
            "agent_id": self.agent_id,
            "decision_type": escalation_type,
            "sla_target": sla_target,
            "ticket_id": ticket_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "resolution_time": None,
            "outcome": "processed"
        }

        # Log decision to Supabase for SLA tracking
        self.log_decision_to_supabase(decision)
        return decision

    def escalate_to_founder(self, ticket_id: str, reason: str) -> Dict[str, Any]:
        """Escalate decision to founder when agent cannot handle."""
        decision = {
            "agent_id": self.agent_id,
            "decision_type": "escalation_to_founder",
            "ticket_id": ticket_id,
            "reason": reason,
            "escalation_to": "hrms-founder-001",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "outcome": "escalated_to_founder"
        }
        self.log_decision_to_supabase(decision)
        return decision

    def log_decision_to_supabase(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        """Log escalation decision to Supabase for SLA compliance tracking."""
        # Placeholder for Supabase integration
        # In production: supabase.table("agent_sla_compliance").insert(...)

        payload = {
            "agent_id": decision.get("agent_id"),
            "decision_type": decision.get("decision_type"),
            "ticket_id": decision.get("ticket_id"),
            "sla_target": decision.get("sla_target", "N/A"),
            "outcome": decision.get("outcome"),
            "reason": decision.get("reason"),
            "timestamp": decision.get("timestamp")
        }

        print(f"[SUPABASE] Would insert into agent_sla_compliance: {json.dumps(payload, indent=2)}")
        return payload

    def validate_agent_authority(self) -> Dict[str, Any]:
        """Validate agent authority and repo access."""
        repos = self.loader.get_agent_repos(self.agent_id)
        authority = repos.get("decision_authority")

        # Check access to primary repos
        access_status = {}
        for repo in repos.get("primary_repos", []):
            access = self.loader.validate_repo_access(repo, self.agent_id)
            access_status[repo] = access.get("valid")

        return {
            "agent_id": self.agent_id,
            "decision_authority": authority,
            "primary_repos": repos.get("primary_repos", []),
            "secondary_repos": repos.get("secondary_repos", []),
            "repo_access": access_status,
            "escalation_to": repos.get("escalation_to"),
            "monitoring_frequency": repos.get("monitoring_frequency")
        }


if __name__ == "__main__":
    agent = SupportAgent()

    print("=== Agent Authority ===")
    authority = agent.validate_agent_authority()
    print(json.dumps(authority, indent=2))

    print("\n=== Handling Technical Escalation ===")
    result = agent.handle_escalation("technical_issue", "TICKET-12345")
    print(json.dumps(result, indent=2))

    print("\n=== Handling Billing Dispute ===")
    result = agent.handle_escalation("billing_dispute", "TICKET-12346")
    print(json.dumps(result, indent=2))
