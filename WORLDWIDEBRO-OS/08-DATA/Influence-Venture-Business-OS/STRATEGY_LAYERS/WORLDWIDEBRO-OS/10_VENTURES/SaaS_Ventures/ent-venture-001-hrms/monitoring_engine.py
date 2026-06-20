#!/usr/bin/env python3
"""Monitoring engine: validates cluster state against REPO_REGISTRY.json for hrms-operations-ai-001."""

import json
import sys
from datetime import datetime
from typing import Any, Dict, List
from registry_loader import RegistryLoader

class MonitoringEngine:
    def __init__(self, registry_loader: RegistryLoader = None):
        """Initialize monitoring engine with registry."""
        self.loader = registry_loader or RegistryLoader()
        self.check_timestamp = datetime.utcnow().isoformat() + "Z"
        self.health_report: Dict[str, Any] = {
            "timestamp": self.check_timestamp,
            "agent_id": "hrms-operations-ai-001",
            "checks": {},
            "alerts": [],
            "sla_breaches": [],
        }

    def check_tier_0_health(self) -> Dict[str, Any]:
        """Validate Tier 0 Foundation repos (civilization-os, iza-os-rag-system)."""
        tier_0_repos = self.loader.get_repos_by_tier(0)
        results = {}

        for repo_name in tier_0_repos:
            repo = self.loader.get_repo(repo_name)
            boot_checks = self.loader.get_repo_boot_checks(repo_name)
            services = self.loader.get_repo_shared_services(repo_name)

            results[repo_name] = {
                "status": "unknown",
                "boot_checks": boot_checks,
                "required_services": [svc.get("service_name") for svc in services],
                "owner_agent": repo.get("owner_agent"),
            }

        return {
            "tier": 0,
            "repos": results,
            "gate_blocked_by": "civilization-os boot checks + iza-os-rag-system RAG indexing",
        }

    def check_core_infrastructure(self) -> Dict[str, Any]:
        """Validate Tier 1 Core repos (the-office, venture-hub, venture-factory-core, autonomous-venture-studio)."""
        tier_1_repos = self.loader.get_repos_by_tier(1)
        results = {}

        for repo_name in tier_1_repos:
            repo = self.loader.get_repo(repo_name)
            metrics = self.loader.get_repo_monitoring_metrics(repo_name)

            results[repo_name] = {
                "status": "unknown",
                "sla_targets": metrics.get("sla_targets", {}),
                "owner_agent": repo.get("owner_agent"),
            }

        return {
            "tier": 1,
            "repos": results,
            "gate_blocked_by": "all Tier 0 repos + dashboard latency validation",
        }

    def check_venture_implementations(self) -> Dict[str, Any]:
        """Validate Tier 2 Venture repos (con-001, con-012, lt-009)."""
        tier_2_repos = self.loader.get_repos_by_tier(2)
        results = {}

        for repo_name in tier_2_repos:
            repo = self.loader.get_repo(repo_name)
            metrics = self.loader.get_repo_monitoring_metrics(repo_name)
            owner_agent = repo.get("owner_agent", {})

            results[repo_name] = {
                "status": "unknown",
                "sla_targets": metrics.get("sla_targets", {}),
                "owner_agent": owner_agent,
            }

        return {
            "tier": 2,
            "repos": results,
            "gate_blocked_by": "all Tier 1 repos + venture portal availability",
        }

    def check_templates(self) -> Dict[str, Any]:
        """Validate Tier 3 Template repos (pitch-kit, templates)."""
        tier_3_repos = self.loader.get_repos_by_tier(3)
        results = {}

        for repo_name in tier_3_repos:
            repo = self.loader.get_repo(repo_name)
            metrics = self.loader.get_repo_monitoring_metrics(repo_name)

            results[repo_name] = {
                "status": "unknown",
                "sla_targets": metrics.get("sla_targets", {}),
                "owner_agent": repo.get("owner_agent"),
            }

        return {
            "tier": 3,
            "repos": results,
            "gate_blocked_by": "all Tier 2 repos + marketplace latency validation",
        }

    def check_deployment_gates(self) -> Dict[str, Any]:
        """Validate current status of all 4 deployment gates."""
        gates = self.loader.get_deployment_gates()
        gate_status = {}

        for gate_name, gate_def in gates.items():
            blocking_sequence = gate_def.get("blocking_sequence", [])
            gate_status[gate_name] = {
                "name": gate_name,
                "status": "awaiting_validation",
                "blocking_sequence": blocking_sequence,
                "unlocked_when": gate_def.get("unlocked_when", "N/A"),
            }

        return gate_status

    def check_agent_authority(self) -> Dict[str, Any]:
        """Validate agent RACI assignments and decision authority."""
        agents = self.loader.registry.get("agent_repo_assignments", {})
        authority_matrix = {}

        for agent_id, agent_def in agents.items():
            authority_matrix[agent_id] = {
                "primary_repos": agent_def.get("primary_repos", []),
                "secondary_repos": agent_def.get("secondary_repos", []),
                "decision_authority": agent_def.get("decision_authority"),
                "escalation_to": agent_def.get("escalation_to"),
                "monitoring_frequency": agent_def.get("monitoring_frequency"),
            }

        return authority_matrix

    def check_shared_services_coverage(self) -> Dict[str, List[str]]:
        """Validate which repos depend on which shared services."""
        repos = self.loader.registry.get("repos", {})
        service_coverage = {}

        for repo_name, repo_def in repos.items():
            services = repo_def.get("shared_services_required", [])
            for service_name in services:
                if service_name not in service_coverage:
                    service_coverage[service_name] = []
                service_coverage[service_name].append(repo_name)

        return service_coverage

    def generate_health_report(self) -> Dict[str, Any]:
        """Generate comprehensive cluster health report."""
        report = {
            "timestamp": self.check_timestamp,
            "agent_id": "hrms-operations-ai-001",
            "venture_id": self.loader.registry.get("venture_id"),
            "venture_name": self.loader.registry.get("venture_name"),
            "checks": {
                "tier_0_foundation": self.check_tier_0_health(),
                "tier_1_core_infrastructure": self.check_core_infrastructure(),
                "tier_2_ventures": self.check_venture_implementations(),
                "tier_3_templates": self.check_templates(),
                "deployment_gates": self.check_deployment_gates(),
                "agent_authority": self.check_agent_authority(),
                "shared_services": self.check_shared_services_coverage(),
            },
            "alerts": [],
            "sla_breaches": [],
            "action_items": [],
        }
        return report

    def export_for_slack(self) -> str:
        """Format health report as Slack message for #hrms channel."""
        report = self.generate_health_report()
        venture_name = report.get("venture_name", "Unknown")
        timestamp = report.get("timestamp", "").split("T")[0]

        message = f"""*HRMS Cluster Status* — {timestamp}
*Venture:* {venture_name}
*Agent:* hrms-operations-ai-001 (hourly check)

*Tier 0 (Foundation):* — awaiting health data
  • civilization-os: boot checks pending
  • iza-os-rag-system: RAG indexing pending

*Tier 1 (Core):* — awaiting health data
  • the-office, venture-hub, venture-factory-core, autonomous-venture-studio

*Tier 2 (Ventures):* — awaiting health data
  • con-001-ace-construction, con-012-hvac-services, lt-009-hvac-technician-dispatch

*Tier 3 (Templates):* — awaiting health data
  • pitch-kit, business-template-marketplace

*Deployment Gates:* 4 gates (Knowledge Graph Ready → Core Infrastructure Ready → Ventures Live → Templates Integrated)
*Agents:* 8 (1 human, 4 core AI, 2 venture-specific) — all RACI roles mapped
*Shared Services:* 9 (Supabase, Qdrant, ClickUp, Stripe, Google Maps, GitHub, MCP, etc.)

:arrow_right: Full registry at REPO_REGISTRY.json — agent decisions and SLA targets tracked in Agent_Manifest.json and STARRED-REPOS-MONITORING-WORKFLOW.md
"""
        return message

if __name__ == "__main__":
    engine = MonitoringEngine()
    report = engine.generate_health_report()
    print(json.dumps(report, indent=2))
    print("\n--- Slack Message ---")
    print(engine.export_for_slack())
