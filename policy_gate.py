#!/usr/bin/env python3
"""
Connector 3: Authorization policy engine + Agent Manifest enforcement.
Before action: agent → check manifest → policy → approved/denied/requires_approval + audit.

Agent Manifest (spec section 4.2):
  - Declares which tools agent can invoke
  - Per-tool constraints (e.g., max_amount_cents for payment tools)
  - Tool invocations blocked if not in manifest
"""

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from supabase import AsyncClient, create_client

logger = logging.getLogger(__name__)

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
AUDIT_TABLE = "audit_logs"
MANIFEST_TABLE = "agent_manifests"


class Decision(str, Enum):
    APPROVED = "approved"
    DENIED = "denied"
    REQUIRES_APPROVAL = "requires_approval"


@dataclass
class PolicyDecision:
    decision: Decision
    reason: str
    agent_id: str
    action: str
    venture_id: str | None


class PolicyGate:
    """Authorization checks before external actions."""

    def __init__(self, supabase_key: str):
        self.client = None
        self.supabase_key = supabase_key

    async def connect(self) -> None:
        self.client = await create_client(SUPABASE_URL, self.supabase_key)

    async def close(self) -> None:
        if self.client:
            await self.client.aclose()

    async def check_manifest(
        self, agent_id: str, tool_id: str, params: dict
    ) -> Optional[PolicyDecision]:
        """
        Check if agent is permitted to invoke a tool (per its manifest).
        Returns PolicyDecision if denied, None if permitted.
        """
        if not self.client:
            raise RuntimeError("PolicyGate not connected")

        try:
            resp = await self.client.table(MANIFEST_TABLE).select("tools").eq(
                "agent_id", agent_id
            ).single().execute()

            if not resp.data:
                return PolicyDecision(
                    Decision.DENIED,
                    f"No manifest found for agent {agent_id}",
                    agent_id,
                    f"invoke_tool:{tool_id}",
                    None,
                )

            tools = resp.data.get("tools", [])
            tool_manifest = next((t for t in tools if t.get("tool_id") == tool_id), None)

            if not tool_manifest:
                return PolicyDecision(
                    Decision.DENIED,
                    f"Tool {tool_id} not in manifest for {agent_id}",
                    agent_id,
                    f"invoke_tool:{tool_id}",
                    None,
                )

            permission = tool_manifest.get("permission")
            if permission == "request_only":
                return PolicyDecision(
                    Decision.REQUIRES_APPROVAL,
                    f"Agent {agent_id} can only request {tool_id}, not invoke",
                    agent_id,
                    f"invoke_tool:{tool_id}",
                    None,
                )

            # Check per-tool constraints (e.g., max_amount_cents)
            constraints = tool_manifest.get("constraints", {})
            for constraint_name, constraint_value in constraints.items():
                param_value = params.get(constraint_name)
                if param_value and param_value > constraint_value:
                    return PolicyDecision(
                        Decision.REQUIRES_APPROVAL,
                        f"{constraint_name}={param_value} exceeds constraint {constraint_value}",
                        agent_id,
                        f"invoke_tool:{tool_id}",
                        None,
                    )

            return None  # Permitted

        except Exception as e:
            logger.error(f"Manifest check failed: {e}")
            return PolicyDecision(Decision.DENIED, str(e), agent_id, f"invoke_tool:{tool_id}", None)

    async def check(
        self,
        agent_id: str,
        action: str,
        venture_id: str | None = None,
        tool_id: Optional[str] = None,
        tool_params: Optional[dict] = None,
    ) -> PolicyDecision:
        """Check if agent can perform action (deploy, charge, delete, update).

        Optional: verify tool invocation via manifest (if tool_id + tool_params provided).
        """
        if not self.client:
            raise RuntimeError("PolicyGate not connected")

        # 1. Check manifest if tool invocation
        if tool_id and tool_params:
            manifest_denial = await self.check_manifest(agent_id, tool_id, tool_params)
            if manifest_denial:
                await self.log_decision(manifest_denial)
                return manifest_denial

        # 2. Check action-specific policies
        if action == "deploy":
            return await self._check_deploy(agent_id, venture_id)
        elif action == "charge":
            return await self._check_charge(agent_id, venture_id)
        elif action == "delete":
            return PolicyDecision(
                Decision.DENIED,
                "Delete actions require human approval",
                agent_id,
                action,
                venture_id,
            )
        else:
            return PolicyDecision(
                Decision.DENIED, f"Unknown action: {action}", agent_id, action, venture_id
            )

    async def _check_deploy(self, agent_id: str, venture_id: str | None) -> PolicyDecision:
        """Deploy allowed if agent is active."""
        try:
            resp = await self.client.table("agent_identities").select("status").eq(
                "agent_key", agent_id
            ).single().execute()

            if not resp.data or resp.data.get("status") != "active":
                return PolicyDecision(
                    Decision.DENIED, f"Agent {agent_id} not active", agent_id, "deploy", venture_id
                )
            return PolicyDecision(
                Decision.APPROVED, f"Deploy allowed", agent_id, "deploy", venture_id
            )
        except Exception as e:
            logger.error(f"Deploy check failed: {e}")
            return PolicyDecision(Decision.DENIED, str(e), agent_id, "deploy", venture_id)

    async def _check_charge(self, agent_id: str, venture_id: str | None) -> PolicyDecision:
        """Charge allowed if venture has sufficient runway."""
        if not venture_id:
            return PolicyDecision(
                Decision.DENIED, "Charge requires venture_id", agent_id, "charge", venture_id
            )

        try:
            resp = await self.client.table("ventures").select("runway_months").eq(
                "id", venture_id
            ).single().execute()

            if not resp.data:
                return PolicyDecision(
                    Decision.DENIED, f"Venture {venture_id} not found", agent_id, "charge", venture_id
                )

            runway = resp.data.get("runway_months", 0)
            if runway < 3:
                return PolicyDecision(
                    Decision.REQUIRES_APPROVAL,
                    f"{runway}mo runway (threshold: 3mo)",
                    agent_id,
                    "charge",
                    venture_id,
                )

            return PolicyDecision(
                Decision.APPROVED, f"Runway: {runway}mo", agent_id, "charge", venture_id
            )
        except Exception as e:
            logger.error(f"Charge check failed: {e}")
            return PolicyDecision(Decision.DENIED, str(e), agent_id, "charge", venture_id)

    async def log_decision(self, decision: PolicyDecision) -> None:
        """Audit trail: log all policy decisions."""
        try:
            await self.client.table(AUDIT_TABLE).insert({
                "agent_id": decision.agent_id,
                "action": decision.action,
                "decision": decision.decision.value,
                "reason": decision.reason,
                "venture_id": decision.venture_id,
            }).execute()
            logger.info(f"[audit] {decision.agent_id} {decision.action} → {decision.decision.value}")
        except Exception as e:
            logger.error(f"Audit log failed: {e}")
