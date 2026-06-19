#!/usr/bin/env python3
"""HRMS Product Agent: dispatch route calculation with service availability validation."""

import json
import sys
from datetime import datetime
from typing import Dict, Any
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from registry_loader import RegistryLoader


class ProductAgent:
    """Product agent for dispatch route calculation with dependency validation."""

    def __init__(self):
        """Initialize agent with registry loader."""
        self.loader = RegistryLoader()
        self.agent_id = "hrms-product-ai-001"

    def calculate_dispatch_route(self, request_id: str, technician_id: str) -> Dict[str, Any]:
        """Calculate dispatch route with service availability validation."""
        # Step 1: Check dispatch engine dependencies
        dispatch_repo = "lt-009-hvac-technician-dispatch"

        # Get shared services required by dispatch engine
        services = self.loader.get_repo_shared_services(dispatch_repo)
        service_names = [svc.get("service_name") for svc in services]

        # Step 2: Validate access to con-012 (secondary repo for technician data)
        access = self.loader.validate_repo_access("con-012-hvac-services", self.agent_id)

        if not access["valid"]:
            return self.escalate_to_founder(request_id, f"Cannot access con-012-hvac-services: {access['error']}")

        # Step 3: Get SLA target for dispatch route calculation
        metrics = self.loader.get_repo_monitoring_metrics(dispatch_repo)
        sla_targets = metrics.get("sla_targets", {})

        # Step 4: Validate Google Maps integration (required for route calculation)
        if "Google Maps" not in service_names:
            return self.escalate_to_founder(request_id, "Google Maps not available for route calculation")

        # Step 5: Route decision and log to Supabase
        decision = {
            "agent_id": self.agent_id,
            "decision_type": "dispatch_route_calculation",
            "request_id": request_id,
            "technician_id": technician_id,
            "dispatch_repo": dispatch_repo,
            "required_services": service_names,
            "sla_targets": sla_targets,
            "access_tier": access.get("access_tier"),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "outcome": "route_calculated"
        }

        # Log decision to Supabase for SLA tracking
        self.log_decision_to_supabase(decision)
        return decision

    def escalate_to_founder(self, request_id: str, reason: str) -> Dict[str, Any]:
        """Escalate route calculation to founder when agent cannot process."""
        decision = {
            "agent_id": self.agent_id,
            "decision_type": "escalation_to_founder",
            "request_id": request_id,
            "reason": reason,
            "escalation_to": "hrms-founder-001",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "outcome": "escalated_to_founder"
        }
        self.log_decision_to_supabase(decision)
        return decision

    def log_decision_to_supabase(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        """Log dispatch decision to Supabase for SLA compliance tracking."""
        # Placeholder for Supabase integration
        # In production: supabase.table("dispatch_decisions").insert(...)

        payload = {
            "agent_id": decision.get("agent_id"),
            "decision_type": decision.get("decision_type"),
            "request_id": decision.get("request_id"),
            "technician_id": decision.get("technician_id"),
            "dispatch_repo": decision.get("dispatch_repo"),
            "required_services": decision.get("required_services", []),
            "sla_targets": decision.get("sla_targets", {}),
            "access_tier": decision.get("access_tier"),
            "outcome": decision.get("outcome"),
            "reason": decision.get("reason"),
            "timestamp": decision.get("timestamp")
        }

        print(f"[SUPABASE] Would insert into dispatch_decisions: {json.dumps(payload, indent=2)}")
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
    agent = ProductAgent()

    print("=== Agent Authority ===")
    authority = agent.validate_agent_authority()
    print(json.dumps(authority, indent=2))

    print("\n=== Calculating Dispatch Route ===")
    result = agent.calculate_dispatch_route("REQ-001", "TECH-12345")
    print(json.dumps(result, indent=2))

    print("\n=== Calculating Dispatch Route (Multiple Technicians) ===")
    result = agent.calculate_dispatch_route("REQ-002", "TECH-67890")
    print(json.dumps(result, indent=2))
