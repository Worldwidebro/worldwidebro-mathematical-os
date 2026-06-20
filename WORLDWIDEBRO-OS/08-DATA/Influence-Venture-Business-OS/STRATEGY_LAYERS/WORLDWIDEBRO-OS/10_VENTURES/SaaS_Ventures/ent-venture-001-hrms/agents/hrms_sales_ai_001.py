#!/usr/bin/env python3
"""HRMS Sales Agent: lead assignment with venture repo validation."""

import json
import sys
from datetime import datetime
from typing import Dict, Any
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from registry_loader import RegistryLoader


class SalesAgent:
    """Sales lead assignment agent with repo access validation and SLA tracking."""

    def __init__(self):
        """Initialize agent with registry loader."""
        self.loader = RegistryLoader()
        self.agent_id = "hrms-sales-ai-001"

    def assign_lead_to_venture(self, lead_id: str, venture_repo: str) -> Dict[str, Any]:
        """Assign lead to venture with access validation and SLA tracking."""
        # Step 1: Validate access to venture repo
        access = self.loader.validate_repo_access(venture_repo, self.agent_id)

        if not access["valid"]:
            # Cannot access venture, escalate to founder
            return self.escalate_to_founder(lead_id, f"Cannot access {venture_repo}: {access['error']}")

        # Step 2: Get SLA targets for deal routing
        metrics = self.loader.get_repo_monitoring_metrics(venture_repo)
        sla_targets = metrics.get("sla_targets", {})

        # Step 3: Validate Stripe integration availability (for payment processing)
        services = self.loader.get_repo_shared_services(venture_repo)
        service_names = [svc.get("service_name") for svc in services]

        if "Stripe" not in service_names:
            return self.escalate_to_founder(lead_id, f"Stripe not available for {venture_repo}")

        # Step 4: Route decision and log to Supabase
        decision = {
            "agent_id": self.agent_id,
            "decision_type": "lead_assignment",
            "lead_id": lead_id,
            "venture_repo": venture_repo,
            "access_tier": access.get("access_tier"),
            "sla_targets": sla_targets,
            "available_services": service_names,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "outcome": "assigned"
        }

        # Log decision to Supabase for SLA tracking
        self.log_decision_to_supabase(decision)
        return decision

    def escalate_to_founder(self, lead_id: str, reason: str) -> Dict[str, Any]:
        """Escalate lead assignment to founder when agent cannot process."""
        decision = {
            "agent_id": self.agent_id,
            "decision_type": "escalation_to_founder",
            "lead_id": lead_id,
            "reason": reason,
            "escalation_to": "hrms-founder-001",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "outcome": "escalated_to_founder"
        }
        self.log_decision_to_supabase(decision)
        return decision

    def log_decision_to_supabase(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        """Log sales decision to Supabase for SLA compliance tracking."""
        # Placeholder for Supabase integration
        # In production: supabase.table("sales_lead_assignments").insert(...)

        payload = {
            "agent_id": decision.get("agent_id"),
            "decision_type": decision.get("decision_type"),
            "lead_id": decision.get("lead_id"),
            "venture_repo": decision.get("venture_repo"),
            "access_tier": decision.get("access_tier"),
            "sla_targets": decision.get("sla_targets", {}),
            "outcome": decision.get("outcome"),
            "reason": decision.get("reason"),
            "timestamp": decision.get("timestamp")
        }

        print(f"[SUPABASE] Would insert into sales_lead_assignments: {json.dumps(payload, indent=2)}")
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
    agent = SalesAgent()

    print("=== Agent Authority ===")
    authority = agent.validate_agent_authority()
    print(json.dumps(authority, indent=2))

    print("\n=== Assigning Lead to Venture ===")
    result = agent.assign_lead_to_venture("LEAD-001", "con-001-ace-construction")
    print(json.dumps(result, indent=2))

    print("\n=== Assigning Lead to HVAC Services ===")
    result = agent.assign_lead_to_venture("LEAD-002", "con-012-hvac-services")
    print(json.dumps(result, indent=2))
