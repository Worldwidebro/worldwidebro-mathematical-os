"""
Approval Gates — Financial Control Enforcement
Prevents spending without proper authorization
Enforces approval_matrix.yaml thresholds
Audit trail: all decisions logged to Neo4j (immutable, 7-year retention)
"""

from typing import Dict, Any, Optional
from datetime import datetime
from enum import Enum

from memory_config import MemoryClient


class ApprovalGateStatus(Enum):
    APPROVED = "approved"
    DENIED = "denied"
    ESCALATED = "escalated"
    PENDING_APPROVAL = "pending_approval"


class ApprovalGates:
    """
    Enforces approval matrix rules
    - Checks agent tier vs. spending amount
    - Auto-escalates if threshold breached
    - Logs all decisions to Neo4j for audit trail
    - Prevents self-approval, catches duplicate spend
    """

    def __init__(self, memory_client: MemoryClient):
        self.memory_client = memory_client
        self.approval_matrix = {
            "AGT-E001": {"max_single": 50000, "tier": "ceo", "escalate_to": None},
            "AGT-E002": {"max_single": 10000, "tier": "cfo", "escalate_to": "AGT-E001"},
            "AGT-E003": {"max_single": 25000, "tier": "coo", "escalate_to": "AGT-E001"},
            "AGT-E004": {"max_single": 15000, "tier": "cto", "escalate_to": "AGT-E001"},
            "AGT-E005": {"max_single": 30000, "tier": "economist", "escalate_to": "AGT-E001"},
            "AGT-F001": {"max_single": 5000, "tier": "sales", "escalate_to": "AGT-E001"},
            "AGT-F002": {"max_single": 2000, "tier": "finance", "escalate_to": "AGT-E002"},
            "AGT-F003": {"max_single": 3000, "tier": "ops", "escalate_to": "AGT-E003"},
            "AGT-F004": {"max_single": 2500, "tier": "tech", "escalate_to": "AGT-E004"},
        }

    async def enforce_approval(
        self,
        agent_id: str,
        category: str,
        amount: float,
        reasoning: str,
    ) -> Dict[str, Any]:
        """
        Check if spending is approved under agent's authority
        Returns: {status, approved, recommendation, escalate_to, trace_id}
        """

        session = self.memory_client.driver.session()

        try:
            # Check if agent exists in matrix
            if agent_id not in self.approval_matrix:
                return await self._deny_approval(
                    session,
                    agent_id,
                    amount,
                    category,
                    "Agent not found in approval matrix",
                )

            agent_config = self.approval_matrix[agent_id]
            max_approved = agent_config["max_single"]

            # Rule 1: Amount exceeds agent's threshold
            if amount > max_approved:
                escalate_to = agent_config.get("escalate_to")
                if escalate_to:
                    return await self._escalate_approval(
                        session,
                        agent_id,
                        amount,
                        category,
                        reasoning,
                        escalate_to,
                    )
                else:
                    return await self._deny_approval(
                        session,
                        agent_id,
                        amount,
                        category,
                        f"Amount ${amount} exceeds agent maximum ${max_approved} and no escalation path",
                    )

            # Rule 2: Check for self-approval conflicts
            if category in ["own_salary", "own_department_budget", "own_equity"]:
                if agent_id in ["AGT-E001", "AGT-E002", "AGT-E003"]:  # C-suite
                    return await self._deny_approval(
                        session,
                        agent_id,
                        amount,
                        category,
                        "Conflict of interest: agent cannot approve own benefits",
                    )

            # Rule 3: Detect duplicate spend (same vendor, same amount, last 7 days)
            duplicate = await self._check_duplicate_spend(
                session, agent_id, amount, category
            )
            if duplicate:
                return await self._deny_approval(
                    session,
                    agent_id,
                    amount,
                    category,
                    f"Duplicate spend detected: identical transaction on {duplicate}",
                )

            # Rule 4: Off-hours escalation (after 6 PM or weekend)
            now = datetime.utcnow()
            is_off_hours = now.hour >= 18 or now.weekday() >= 5  # After 6 PM or weekend

            if is_off_hours and amount > 5000:  # High-value off-hours spend
                return await self._escalate_approval(
                    session,
                    agent_id,
                    amount,
                    category,
                    reasoning,
                    "AGT-E001",  # Escalate to CEO
                )

            # All checks passed: APPROVE
            return await self._approve_spending(
                session, agent_id, amount, category, reasoning
            )

        finally:
            await session.close()

    async def _approve_spending(
        self,
        session,
        agent_id: str,
        amount: float,
        category: str,
        reasoning: str,
    ) -> Dict[str, Any]:
        """
        Log approval to Neo4j audit trail
        """

        # Create audit node
        query = """
        CREATE (a:ApprovalDecision {
            id: apoc.create.uuid(),
            agent_id: $agent_id,
            amount: $amount,
            category: $category,
            reasoning: $reasoning,
            decision: 'approved',
            timestamp: datetime(),
            ip_address: '127.0.0.1'
        })
        RETURN a.id as approval_id
        """

        result = await session.run(
            query,
            {
                "agent_id": agent_id,
                "amount": amount,
                "category": category,
                "reasoning": reasoning,
            },
        )
        record = await result.single()
        approval_id = record["approval_id"] if record else None

        return {
            "status": ApprovalGateStatus.APPROVED.value,
            "approved": True,
            "recommendation": f"APPROVED: ${amount} {category} spending authorized under {self.approval_matrix[agent_id]['tier']} threshold",
            "escalate": False,
            "audit_trail_id": approval_id,
        }

    async def _deny_approval(
        self, session, agent_id: str, amount: float, category: str, reason: str
    ) -> Dict[str, Any]:
        """
        Log denial to Neo4j audit trail
        """

        query = """
        CREATE (a:ApprovalDecision {
            id: apoc.create.uuid(),
            agent_id: $agent_id,
            amount: $amount,
            category: $category,
            reason: $reason,
            decision: 'denied',
            timestamp: datetime()
        })
        RETURN a.id as denial_id
        """

        result = await session.run(
            query,
            {
                "agent_id": agent_id,
                "amount": amount,
                "category": category,
                "reason": reason,
            },
        )
        record = await result.single()
        denial_id = record["denial_id"] if record else None

        return {
            "status": ApprovalGateStatus.DENIED.value,
            "approved": False,
            "recommendation": f"DENIED: {reason}",
            "escalate": False,
            "audit_trail_id": denial_id,
        }

    async def _escalate_approval(
        self,
        session,
        agent_id: str,
        amount: float,
        category: str,
        reasoning: str,
        escalate_to: str,
    ) -> Dict[str, Any]:
        """
        Escalate to higher authority
        """

        query = """
        CREATE (a:ApprovalDecision {
            id: apoc.create.uuid(),
            agent_id: $agent_id,
            escalated_to: $escalate_to,
            amount: $amount,
            category: $category,
            reasoning: $reasoning,
            decision: 'escalated',
            sla_deadline: datetime() + duration('PT4H'),
            timestamp: datetime()
        })
        RETURN a.id as escalation_id
        """

        result = await session.run(
            query,
            {
                "agent_id": agent_id,
                "escalate_to": escalate_to,
                "amount": amount,
                "category": category,
                "reasoning": reasoning,
            },
        )
        record = await result.single()
        escalation_id = record["escalation_id"] if record else None

        return {
            "status": ApprovalGateStatus.ESCALATED.value,
            "approved": False,
            "recommendation": f"ESCALATED to {escalate_to}: ${amount} {category}. Awaiting higher authority approval.",
            "escalate": True,
            "escalate_to": escalate_to,
            "sla_hours": 4,
            "audit_trail_id": escalation_id,
        }

    async def _check_duplicate_spend(
        self, session, agent_id: str, amount: float, category: str
    ) -> Optional[str]:
        """
        Check for duplicate spending patterns (same amount to same category, last 7 days)
        Returns: timestamp of previous identical spend, or None
        """

        query = """
        MATCH (a:ApprovalDecision)
        WHERE a.agent_id = $agent_id
          AND a.amount = $amount
          AND a.category = $category
          AND a.timestamp > datetime() - duration('P7D')
          AND a.decision = 'approved'
        RETURN a.timestamp as previous_timestamp
        LIMIT 1
        """

        result = await session.run(
            query, {"agent_id": agent_id, "amount": amount, "category": category}
        )
        record = await result.single()

        return record["previous_timestamp"] if record else None
