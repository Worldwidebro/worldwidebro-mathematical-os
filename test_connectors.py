#!/usr/bin/env python3
"""
Integration test: All 3 connectors + runtime.
Tests: Policy check → Execution → Event publication → Audit log.
"""

import asyncio
import os
from runtime_agent_runtime import AgentRuntime


async def test_charge_with_policy():
    """Test: Hermes charges venture, policy checks runway."""
    supabase_key = os.getenv("SUPABASE_KEY")
    if not supabase_key:
        print("❌ SUPABASE_KEY not set. Skipping integration test.")
        return

    runtime = AgentRuntime(supabase_key)
    await runtime.connect()

    try:
        print("\n=== Test 1: Charge with sufficient runway (should APPROVE) ===")
        result = await runtime.execute_action(
            agent_id="hermes",
            action="charge",
            params={"amount": 97.00, "stripe_id": "pi_test_1"},
            venture_id="CON-001",
        )
        print(f"Result: {result}\n")

        print("=== Test 2: Deploy code (should APPROVE for active agent) ===")
        result = await runtime.execute_action(
            agent_id="hermes",
            action="deploy",
            params={"branch": "main", "repo": "ace-construction"},
            venture_id="CON-001",
        )
        print(f"Result: {result}\n")

        print("=== Test 3: Delete (should DENY - requires human approval) ===")
        result = await runtime.execute_action(
            agent_id="hermes",
            action="delete",
            params={},
            venture_id="CON-001",
        )
        print(f"Result: {result}\n")

    finally:
        await runtime.close()


if __name__ == "__main__":
    asyncio.run(test_charge_with_policy())
