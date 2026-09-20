"""
CEO Agent — Strategic Direction & Capital Allocation
Highest authority, longest decision horizons, biggest capital thresholds
Writes decisions to Neo4j reasoning memory + Supabase for VEX visibility
"""

from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper
from approval_matrix import ApprovalMatrix
from orchestrator_context import OrchestratorContext


class StrategicDecision(Enum):
    VENTURE_ACQUISITION = "venture_acquisition"
    CAPITAL_DEPLOYMENT = "capital_deployment"
    STRATEGIC_PIVOT = "strategic_pivot"
    BOARD_COMMUNICATION = "board_communication"


class CEOAgent:
    """
    CEO Agent for strategic decisions, capital allocation, board reporting
    - Approval threshold: $50K (highest)
    - Confidence threshold: 0.85
    - Memory: Working (current decision) + Episodic (past 20 decisions) + Semantic (learned patterns)
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.agent_id = "AGT-E001"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.approval_matrix = ApprovalMatrix()
        self.context_assembler = OrchestratorContext(memory_client)

    async def evaluate_capital_deployment(
        self, venture_id: str, amount: float, reasoning: str
    ) -> Dict[str, Any]:
        """
        Evaluate capital deployment decision
        - Check approval threshold ($50K max for CEO)
        - Assemble full venture context from Neo4j
        - Use reasoning harness for high-confidence decision
        - Log to Neo4j reasoning memory
        """

        # Create session for this decision
        session = await self.memory_wrapper.create_session(self.agent_id)

        # Assemble context from Neo4j + Supabase
        context = await self.context_assembler.assemble_context(
            entity_id=venture_id, context_type="capital_deployment"
        )

        # Add message to session history
        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Evaluating capital deployment: ${amount} to {venture_id}",
            metadata={"context": context},
        )

        # Determine decision and confidence
        decision_data = {
            "venture_id": venture_id,
            "amount": amount,
            "reasoning": reasoning,
            "venture_readiness": context.get("readiness_pct", 0),
            "current_cash": context.get("cash_position", 0),
            "team_size": context.get("team_size", 0),
        }

        # Confidence increases with readiness + cash position
        confidence = min(
            0.95,
            (context.get("readiness_pct", 0.5) + context.get("cash_position", 0) / 1000000) / 2,
        )

        # Check approval threshold
        approved = amount <= 50000
        if not approved:
            decision_outcome = "escalated_to_board"
            recommendation = f"ESCALATE: ${amount} exceeds CEO threshold. Requires board vote."
        else:
            decision_outcome = "approved"
            recommendation = f"APPROVE: Deploy ${amount} to {venture_id}"

        # Log decision to Neo4j reasoning memory
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"capital_deployment_{venture_id}",
            reasoning,
            confidence,
            decision_outcome,
        )

        # Write to shared Supabase for VEX visibility
        await self.supabase.table("executive_decisions").insert({
            "agent_id": self.agent_id,
            "venture_id": venture_id,
            "decision_type": "capital_deployment",
            "amount": amount,
            "decision": decision_outcome,
            "confidence": confidence,
            "reasoning": reasoning,
            "recommendation": recommendation,
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "venture_id": venture_id,
            "amount": amount,
            "decision": decision_outcome,
            "recommendation": recommendation,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def strategic_pivot_assessment(
        self, pivot_rationale: str, affected_ventures: list
    ) -> Dict[str, Any]:
        """
        Assess strategic pivot (requires board vote, logs to Neo4j)
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Assessing strategic pivot affecting {len(affected_ventures)} ventures",
            metadata={"rationale": pivot_rationale},
        )

        # Assess impact across ventures
        venture_impacts = []
        for ven_id in affected_ventures:
            context = await self.context_assembler.assemble_context(
                entity_id=ven_id, context_type="strategic_impact"
            )
            venture_impacts.append({
                "venture_id": ven_id,
                "readiness": context.get("readiness_pct", 0),
                "impact_severity": "high" if context.get("readiness_pct", 0) > 0.7 else "low",
            })

        confidence = 0.8  # Strategic decisions are inherently uncertain

        # Log to Neo4j
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            "strategic_pivot",
            pivot_rationale,
            confidence,
            "requires_board_vote",
        )

        # Write to Supabase
        await self.supabase.table("executive_decisions").insert({
            "agent_id": self.agent_id,
            "venture_id": None,  # Affects multiple
            "decision_type": "strategic_pivot",
            "decision": "requires_board_vote",
            "confidence": confidence,
            "reasoning": pivot_rationale,
            "affected_ventures": len(affected_ventures),
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "decision": "strategic_pivot",
            "affected_ventures": venture_impacts,
            "requires_board_vote": True,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def portfolio_health_check(self) -> Dict[str, Any]:
        """
        Daily portfolio health assessment
        - Check aggregate readiness across all ventures
        - Identify at-risk ventures
        - Log findings to Neo4j
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        # Fetch all ventures from Neo4j
        query = """
        MATCH (v:Venture)
        OPTIONAL MATCH (v)-[:HAS_METRIC]->(m:Metric {type: 'readiness'})
        RETURN v.id as venture_id, COALESCE(m.value, 0.0) as readiness
        LIMIT 100
        """

        neo_session = self.memory_client.driver.session()
        ventures = []
        try:
            result = await neo_session.run(query)
            async for record in result:
                ventures.append({
                    "venture_id": record["venture_id"],
                    "readiness": record["readiness"],
                })
        finally:
            await neo_session.close()

        # Calculate portfolio metrics
        portfolio_readiness = sum(v["readiness"] for v in ventures) / len(ventures) if ventures else 0
        at_risk = [v for v in ventures if v["readiness"] < 0.3]

        confidence = 0.9

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            "portfolio_health_check",
            f"Portfolio readiness: {portfolio_readiness:.2%}. At-risk: {len(at_risk)}",
            confidence,
            "monitored",
        )

        # Write to Supabase for VEX dashboard
        await self.supabase.table("portfolio_health").insert({
            "checked_by": self.agent_id,
            "total_ventures": len(ventures),
            "portfolio_readiness": portfolio_readiness,
            "at_risk_count": len(at_risk),
            "neo4j_trace_id": trace_id,
            "checked_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "portfolio_readiness": portfolio_readiness,
            "total_ventures": len(ventures),
            "at_risk_ventures": len(at_risk),
            "at_risk_ids": [v["venture_id"] for v in at_risk],
            "confidence": confidence,
            "trace_id": trace_id,
        }
