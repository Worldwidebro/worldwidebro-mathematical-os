#!/usr/bin/env python3
"""
Connector 3: Authorization policy engine.
Before action: agent → policy → approved/denied/requires_approval + audit log.
"""

import logging
from dataclasses import dataclass
from enum import Enum

from supabase import AsyncClient, create_client

logger = logging.getLogger(__name__)

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
AUDIT_TABLE = "audit_logs"


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

    async def check(
        self, agent_id: str, action: str, venture_id: str | None = None
    ) -> PolicyDecision:
        """Check if agent can perform action (deploy, charge, delete, update)."""
        if not self.client:
            raise RuntimeError("PolicyGate not connected")

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
