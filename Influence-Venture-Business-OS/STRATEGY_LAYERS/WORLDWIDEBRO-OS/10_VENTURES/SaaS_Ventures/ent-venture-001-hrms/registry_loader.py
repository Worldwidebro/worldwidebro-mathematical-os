#!/usr/bin/env python3
"""Registry loader: reads REPO_REGISTRY.json and validates cluster state for agents and dashboards."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

class RegistryLoader:
    def __init__(self, registry_path: str = "REPO_REGISTRY.json"):
        """Load and parse the central REPO_REGISTRY.json."""
        self.registry_path = Path(registry_path)
        self.registry: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        """Load registry from disk."""
        if not self.registry_path.exists():
            raise FileNotFoundError(f"Registry not found at {self.registry_path}")
        with open(self.registry_path, "r") as f:
            self.registry = json.load(f)

    def get_repo(self, repo_name: str) -> Optional[Dict[str, Any]]:
        """Get repo definition by name."""
        return self.registry.get("repos", {}).get(repo_name)

    def get_repos_by_tier(self, tier: int) -> List[str]:
        """Get all repos in a specific deployment tier."""
        return [name for name, repo in self.registry.get("repos", {}).items() if repo.get("tier") == tier]

    def get_deployment_sequence(self) -> List[str]:
        """Get repos ordered by deployment sequence."""
        repos = self.registry.get("repos", {})
        return sorted(repos.keys(), key=lambda r: repos[r].get("deployment_sequence", 999))

    def get_agent_repos(self, agent_id: str) -> Dict[str, List[str]]:
        """Get primary and secondary repos for an agent."""
        assignments = self.registry.get("agent_repo_assignments", {})
        agent = assignments.get(agent_id, {})
        return {
            "primary_repos": agent.get("primary_repos", []),
            "secondary_repos": agent.get("secondary_repos", []),
            "decision_authority": agent.get("decision_authority"),
            "escalation_to": agent.get("escalation_to"),
            "monitoring_frequency": agent.get("monitoring_frequency"),
        }

    def get_deployment_gates(self) -> Dict[str, Any]:
        """Get all deployment gates and their blocking criteria."""
        return self.registry.get("deployment_gates", {})

    def validate_repo_access(
        self, repo_name: str, agent_id: str, requires_mfa: bool = False
    ) -> Dict[str, Any]:
        """Validate whether an agent can access a repo."""
        repo = self.get_repo(repo_name)
        if not repo:
            return {"valid": False, "error": f"Repo {repo_name} not found in registry"}

        access_control = repo.get("access_control", {})
        required_roles = access_control.get("required_roles", [])
        mfa_required = access_control.get("mfa_required", False)

        # Check role-based access
        if agent_id not in required_roles:
            return {
                "valid": False,
                "error": f"Agent {agent_id} not in required roles: {required_roles}",
            }

        # Check MFA requirement
        if mfa_required and not requires_mfa:
            return {"valid": False, "error": f"MFA required for {repo_name}"}

        return {
            "valid": True,
            "repo_name": repo_name,
            "agent_id": agent_id,
            "access_tier": access_control.get("tier"),
            "data_classification": access_control.get("data_classification"),
        }

    def get_repo_dependencies(self, repo_name: str) -> Dict[str, List[str]]:
        """Get all dependencies (build, runtime, data) for a repo."""
        repo = self.get_repo(repo_name)
        if not repo:
            return {}
        return {
            "build_dependencies": repo.get("build_dependencies", []),
            "runtime_dependencies": repo.get("runtime_dependencies", []),
            "data_dependencies": repo.get("data_dependencies", []),
        }

    def get_repo_shared_services(self, repo_name: str) -> List[Dict[str, Any]]:
        """Get all shared services required by a repo."""
        repo = self.get_repo(repo_name)
        if not repo:
            return []
        service_names = repo.get("shared_services_required", [])
        shared_services = self.registry.get("shared_services", {})
        return [
            {"service_name": svc, "details": shared_services.get(svc, {})}
            for svc in service_names
        ]

    def get_repo_boot_checks(self, repo_name: str) -> List[Dict[str, Any]]:
        """Get startup validation requirements for a repo."""
        repo = self.get_repo(repo_name)
        if not repo:
            return []
        return repo.get("boot_checks", [])

    def get_repo_monitoring_metrics(self, repo_name: str) -> Dict[str, Any]:
        """Get SLA targets and monitoring metrics for a repo."""
        repo = self.get_repo(repo_name)
        if not repo:
            return {}
        return {
            "sla_targets": repo.get("sla_targets", {}),
            "monitoring_metrics": repo.get("monitoring_metrics", {}),
        }

    def get_exposed_apis(self, repo_name: str) -> List[Dict[str, Any]]:
        """Get all exposed API endpoints for a repo."""
        repo = self.get_repo(repo_name)
        if not repo:
            return []
        return repo.get("exposed_apis", [])

    def validate_deployment_gate(self, gate_name: str, current_state: Dict[str, Any]) -> Dict[str, Any]:
        """Validate whether a deployment gate can be unlocked."""
        gates = self.get_deployment_gates()
        gate = gates.get(gate_name, {})
        if not gate:
            return {"valid": False, "error": f"Gate {gate_name} not found"}

        validation_criteria = gate.get("validation_criteria", [])
        failed_checks = []

        for criterion in validation_criteria:
            check_name = criterion.get("check_name")
            required_state = criterion.get("required_state")
            if current_state.get(check_name) != required_state:
                failed_checks.append(
                    {
                        "check": check_name,
                        "required": required_state,
                        "current": current_state.get(check_name),
                    }
                )

        return {
            "valid": len(failed_checks) == 0,
            "gate_name": gate_name,
            "blocking_sequence": gate.get("blocking_sequence", []),
            "validation_criteria": gate.get("validation_criteria", []),
            "failed_checks": failed_checks,
        }

    def get_agent_sla_targets(self, agent_id: str) -> Dict[str, Any]:
        """Get SLA compliance targets for an agent's repos."""
        agent = self.registry.get("agents", {}).get(agent_id, {})
        primary_repos = agent.get("primary_repos", [])
        sla_by_repo = {}
        for repo_name in primary_repos:
            metrics = self.get_repo_monitoring_metrics(repo_name)
            sla_by_repo[repo_name] = metrics.get("sla_targets", {})
        return sla_by_repo

    def export_for_dashboard(self) -> Dict[str, Any]:
        """Export registry data formatted for dashboard display."""
        return {
            "venture_id": self.registry.get("venture_id"),
            "venture_name": self.registry.get("venture_name"),
            "as_of": self.registry.get("as_of"),
            "registry_owner": self.registry.get("registry_owner"),
            "last_updated": self.registry.get("last_updated"),
            "repos": {
                name: {
                    "tier": repo.get("tier"),
                    "deployment_sequence": repo.get("deployment_sequence"),
                    "owner_agent": repo.get("owner_agent"),
                    "status": repo.get("status"),
                    "sla_targets": repo.get("sla_targets", {}),
                }
                for name, repo in self.registry.get("repos", {}).items()
            },
            "agents": self.registry.get("agents", {}),
            "deployment_gates": self.get_deployment_gates(),
        }

if __name__ == "__main__":
    loader = RegistryLoader()
    print(f"Loaded registry for venture: {loader.registry['venture_name']}")
    print(f"Total repos: {len(loader.registry['repos'])}")
    print(f"Deployment sequence: {loader.get_deployment_sequence()}")
