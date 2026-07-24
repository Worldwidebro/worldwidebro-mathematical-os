#!/usr/bin/env python3
"""
Agent Runtime: Core execution loop.
Integrates: PolicyGate (authorization) → Execution → EventBus (pub/sub) → Audit.
"""

import asyncio
import logging
import os
from typing import Any

from event_bus import EventBus
from policy_gate import PolicyGate
from supabase import AsyncClient, create_client

logger = logging.getLogger(__name__)

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"


class AgentRuntime:
    """Orchestrates policy → execution → event flow."""

    def __init__(self, supabase_key: str, redis_url: str = "redis://localhost:6379"):
        self.policy = PolicyGate(supabase_key)
        self.bus = EventBus(redis_url)
        self.supabase = None

    async def connect(self) -> None:
        """Connect to Supabase and Redis."""
        self.supabase = await create_client(SUPABASE_URL, self.policy.supabase_key)
        await self.policy.connect()
        await self.bus.connect()
        logger.info("✓ Runtime initialized (Policy + Bus + Supabase)")

    async def close(self) -> None:
        """Clean up connections."""
        await self.policy.close()
        await self.bus.close()
        if self.supabase:
            await self.supabase.aclose()

    async def execute_action(
        self, agent_id: str, action: str, params: dict[str, Any], venture_id: str | None = None
    ) -> dict[str, Any]:
        """
        Core flow: Policy check → Execute → Publish event → Audit.

        Actions: deploy, charge, update_venture, etc.
        Returns: {success: bool, result: any, decision: str}
        """
        logger.info(f"[{agent_id}] Executing {action} on {venture_id or 'global'}")

        # 1. Policy check
        decision = await self.policy.check(agent_id, action, venture_id)
        await self.policy.log_decision(decision)

        if decision.decision.value == "denied":
            logger.warning(f"[{agent_id}] {action} DENIED: {decision.reason}")
            return {"success": False, "result": None, "decision": "denied", "reason": decision.reason}

        if decision.decision.value == "requires_approval":
            logger.info(f"[{agent_id}] {action} pending approval: {decision.reason}")
            return {
                "success": False,
                "result": None,
                "decision": "requires_approval",
                "reason": decision.reason,
            }

        # 2. Execute (stub: actual implementation depends on action type)
        result = await self._execute(agent_id, action, params, venture_id)

        # 3. Publish event
        await self.bus.publish(f"{action}.completed", {
            "agent": agent_id,
            "action": action,
            "venture_id": venture_id,
            "result": result,
        })

        # 4. Return success
        logger.info(f"[{agent_id}] {action} completed")
        return {"success": True, "result": result, "decision": "approved"}

    async def _execute(
        self, agent_id: str, action: str, params: dict[str, Any], venture_id: str | None
    ) -> Any:
        """Execute the actual action (stub for action-specific handlers)."""
        if action == "charge":
            return await self._charge(venture_id, params)
        elif action == "deploy":
            return await self._deploy(venture_id, params)
        elif action == "update_venture":
            return await self._update_venture(venture_id, params)
        else:
            raise ValueError(f"Unknown action: {action}")

    async def _charge(self, venture_id: str | None, params: dict) -> dict:
        """Stub: Charge venture via Stripe."""
        logger.info(f"[charge] {venture_id} → ${params.get('amount', 0)}")
        return {"status": "charged", "venture_id": venture_id, "amount": params.get("amount")}

    async def _deploy(self, venture_id: str | None, params: dict) -> dict:
        """Stub: Deploy venture code."""
        logger.info(f"[deploy] {venture_id} → {params.get('branch', 'main')}")
        return {"status": "deployed", "venture_id": venture_id, "branch": params.get("branch")}

    async def _update_venture(self, venture_id: str | None, params: dict) -> dict:
        """Stub: Update venture metadata in Supabase."""
        logger.info(f"[update] {venture_id} with {params}")
        return {"status": "updated", "venture_id": venture_id}


async def main():
    """Example: charge a venture, with policy check + event publication."""
    supabase_key = os.getenv("SUPABASE_KEY")
    if not supabase_key:
        raise ValueError("SUPABASE_KEY not set")

    runtime = AgentRuntime(supabase_key)
    await runtime.connect()

    try:
        # Test: Hermes agent charges Ace Construction
        result = await runtime.execute_action(
            agent_id="hermes",
            action="charge",
            params={"amount": 97.00, "stripe_id": "pi_123"},
            venture_id="CON-001",
        )
        print(f"\nResult: {result}")

    finally:
        await runtime.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
