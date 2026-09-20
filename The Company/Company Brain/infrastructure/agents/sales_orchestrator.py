"""
Sales Orchestrator (AGT-F001)
Routes leads by venture, manages pipeline, tracks conversion
Max approval: $5K (sales incentives, demo costs)
"""

from typing import Dict, Any, List
from datetime import datetime

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper
from orchestrator_context import OrchestratorContext


class SalesOrchestrator:
    """
    Function agent: coordinates sales activities across ventures
    - Lead routing to appropriate ventures
    - Pipeline management (Neo4j)
    - Conversion tracking + learning loop
    - Sales incentive approval ($5K max)
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.agent_id = "AGT-F001"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.context_assembler = OrchestratorContext(memory_client)

    async def route_lead(
        self, lead_id: str, prospect_name: str, segment: str
    ) -> Dict[str, Any]:
        """
        Route inbound lead to appropriate venture
        - Segment matching (high-intent, high-value, etc.)
        - Venture readiness assessment
        - Assignment + notification
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Routing lead {lead_id}: {prospect_name} ({segment})",
        )

        # Fetch best-matching venture from Neo4j
        query = """
        MATCH (v:Venture)
        WHERE v.segment = $segment
        OPTIONAL MATCH (v)-[:HAS_METRIC]->(m:Metric {type: 'readiness'})
        RETURN v.id as venture_id,
               v.name as venture_name,
               COALESCE(m.value, 0.0) as readiness
        ORDER BY readiness DESC
        LIMIT 1
        """

        neo_session = self.memory_client.driver.session()
        try:
            result = await neo_session.run(query, {"segment": segment})
            record = await result.single()

            if record:
                venture_id = record["venture_id"]
                readiness = record["readiness"]

                decision = "routed"
                confidence = 0.85 if readiness > 0.5 else 0.65
                recommendation = f"Route to {venture_id} ({readiness:.0%} ready)"
            else:
                venture_id = None
                decision = "no_matching_venture"
                confidence = 0.8
                recommendation = "No ready venture for segment. Hold in queue."
        finally:
            await neo_session.close()

        # Log decision
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"route_lead_{lead_id}",
            f"Segment: {segment}",
            confidence,
            decision,
        )

        # Write to Supabase
        await self.supabase.table("lead_routing").insert({
            "lead_id": lead_id,
            "prospect_name": prospect_name,
            "segment": segment,
            "routed_to": venture_id,
            "decision": decision,
            "confidence": confidence,
            "neo4j_trace_id": trace_id,
            "routed_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "lead_id": lead_id,
            "routed_to": venture_id,
            "decision": decision,
            "recommendation": recommendation,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def track_pipeline(self, venture_id: str) -> Dict[str, Any]:
        """
        Aggregate pipeline for a venture
        - Count by stage (lead, qualified, proposal, negotiation, won)
        - Calculate conversion rates
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        # Fetch pipeline from Neo4j
        query = """
        MATCH (v:Venture {id: $venture_id})-[:HAS_LEAD]->(l:Lead)
        RETURN l.stage as stage, COUNT(*) as count
        GROUP BY l.stage
        """

        neo_session = self.memory_client.driver.session()
        pipeline = {}
        total_leads = 0

        try:
            result = await neo_session.run(query, {"venture_id": venture_id})
            async for record in result:
                stage = record["stage"]
                count = record["count"]
                pipeline[stage] = count
                total_leads += count
        finally:
            await neo_session.close()

        # Calculate conversion rate (won / total)
        won = pipeline.get("won", 0)
        conversion_rate = (won / total_leads) if total_leads > 0 else 0

        confidence = 0.95

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"track_pipeline_{venture_id}",
            f"Total: {total_leads}, Conversion: {conversion_rate:.0%}",
            confidence,
            "monitored",
        )

        # Write to Supabase
        await self.supabase.table("sales_pipeline").insert({
            "venture_id": venture_id,
            "total_leads": total_leads,
            "stage_breakdown": pipeline,
            "conversion_rate": conversion_rate,
            "neo4j_trace_id": trace_id,
            "tracked_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "venture_id": venture_id,
            "total_leads": total_leads,
            "pipeline": pipeline,
            "conversion_rate": conversion_rate,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def approve_sales_incentive(
        self, rep_id: str, incentive_type: str, amount: float, reasoning: str
    ) -> Dict[str, Any]:
        """
        Approve sales rep incentive ($5K max)
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        approved = amount <= 5000

        decision = "approved" if approved else "escalated_to_ceo"
        confidence = 0.85
        recommendation = (
            f"APPROVE: ${amount} {incentive_type} for {rep_id}"
            if approved
            else f"ESCALATE: ${amount} exceeds $5K sales incentive limit"
        )

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"sales_incentive_{rep_id}",
            reasoning,
            confidence,
            decision,
        )

        await self.supabase.table("financial_decisions").insert({
            "agent_id": self.agent_id,
            "decision_type": "sales_incentive",
            "rep_id": rep_id,
            "amount": amount,
            "incentive_type": incentive_type,
            "decision": decision,
            "confidence": confidence,
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "rep_id": rep_id,
            "amount": amount,
            "decision": decision,
            "recommendation": recommendation,
            "confidence": confidence,
            "trace_id": trace_id,
        }
