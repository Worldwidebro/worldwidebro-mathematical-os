"""
COO Agent — Operations, Resource Allocation, SLA Monitoring
Operations-focused: venture readiness, resource scaling, SLA enforcement
Writes to Neo4j reasoning memory + Supabase for VEX visibility
"""

from typing import Dict, Any, List
from datetime import datetime

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper
from approval_matrix import ApprovalMatrix
from orchestrator_context import OrchestratorContext


class COOAgent:
    """
    COO Agent for operations, resource allocation, venture scaling
    - Approval threshold: $25K
    - Escalation: to CEO if >$25K
    - Confidence threshold: 0.82
    - Responsibilities: venture readiness, headcount, equipment, facility leases, SLA monitoring
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.agent_id = "AGT-E003"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.approval_matrix = ApprovalMatrix()
        self.context_assembler = OrchestratorContext(memory_client)

    async def evaluate_venture_readiness(self, venture_id: str) -> Dict[str, Any]:
        """
        Assess venture operational readiness
        - Team size, infrastructure, process maturity
        - Compare against readiness threshold (30%)
        - Escalate if below threshold
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        # Assemble operational context from Neo4j
        context = await self.context_assembler.assemble_context(
            entity_id=venture_id, context_type="operational_readiness"
        )

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Evaluating operational readiness for {venture_id}",
            metadata={"context": context},
        )

        readiness = context.get("readiness_pct", 0)
        team_size = context.get("team_size", 0)
        below_threshold = readiness < 0.3

        # Determine recommendation
        if below_threshold:
            decision_outcome = "escalate_to_ceo"
            recommendation = f"ESCALATE: {venture_id} readiness {readiness:.0%} below 30% threshold. Requires strategic intervention."
            confidence = 0.95
        elif readiness < 0.6:
            decision_outcome = "monitor_closely"
            recommendation = f"MONITOR: {venture_id} readiness {readiness:.0%}. Recommend resource infusion or restructuring."
            confidence = 0.85
        else:
            decision_outcome = "operational_health"
            recommendation = f"HEALTHY: {venture_id} readiness {readiness:.0%}. Continue monitoring."
            confidence = 0.9

        # Log to Neo4j
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"venture_readiness_{venture_id}",
            f"Readiness: {readiness:.0%}, Team: {team_size}",
            confidence,
            decision_outcome,
        )

        # Write to Supabase for VEX
        await self.supabase.table("operational_decisions").insert({
            "agent_id": self.agent_id,
            "venture_id": venture_id,
            "decision_type": "venture_readiness",
            "readiness_pct": readiness,
            "team_size": team_size,
            "decision": decision_outcome,
            "confidence": confidence,
            "recommendation": recommendation,
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "venture_id": venture_id,
            "readiness_pct": readiness,
            "team_size": team_size,
            "decision": decision_outcome,
            "recommendation": recommendation,
            "confidence": confidence,
            "escalate": below_threshold,
            "trace_id": trace_id,
        }

    async def approve_headcount_addition(
        self, venture_id: str, num_people: int, role: str, salary_total: float
    ) -> Dict[str, Any]:
        """
        Approve headcount addition (max $25K, max 5 people per quarter)
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        context = await self.context_assembler.assemble_context(
            entity_id=venture_id, context_type="headcount_planning"
        )

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Evaluating headcount addition: {num_people} {role}(s) at ${salary_total:,.0f}",
            metadata={"context": context},
        )

        # Check thresholds
        within_salary = salary_total <= 25000
        within_headcount = num_people <= 5
        venture_readiness = context.get("readiness_pct", 0) > 0.5

        if within_salary and within_headcount and venture_readiness:
            decision_outcome = "approved"
            recommendation = f"APPROVE: Add {num_people} {role}(s) to {venture_id} at ${salary_total:,.0f}"
            confidence = 0.88
        elif not venture_readiness:
            decision_outcome = "rejected"
            recommendation = f"REJECT: {venture_id} readiness too low ({context.get('readiness_pct', 0):.0%}). Build capacity first."
            confidence = 0.92
        elif not within_salary:
            decision_outcome = "escalated_to_ceo"
            recommendation = f"ESCALATE: ${salary_total:,.0f} exceeds COO threshold ($25K). Requires CEO approval."
            confidence = 0.9
        else:
            decision_outcome = "escalated_to_ceo"
            recommendation = f"ESCALATE: {num_people} headcount exceeds quarterly limit (5). Requires strategic approval."
            confidence = 0.85

        # Log to Neo4j
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"headcount_addition_{venture_id}",
            f"{num_people} {role}(s)",
            confidence,
            decision_outcome,
        )

        # Write to Supabase
        await self.supabase.table("operational_decisions").insert({
            "agent_id": self.agent_id,
            "venture_id": venture_id,
            "decision_type": "headcount_addition",
            "num_people": num_people,
            "role": role,
            "salary_total": salary_total,
            "decision": decision_outcome,
            "confidence": confidence,
            "recommendation": recommendation,
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "venture_id": venture_id,
            "num_people": num_people,
            "role": role,
            "salary_total": salary_total,
            "decision": decision_outcome,
            "recommendation": recommendation,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def sla_health_check(self) -> Dict[str, Any]:
        """
        Monitor SLA compliance across all ventures
        - Response times, uptime, delivery metrics
        - Flag breaches for immediate remediation
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            "Running SLA health check across all ventures",
        )

        # Fetch SLA metrics from Neo4j
        query = """
        MATCH (v:Venture)-[:HAS_SLA]->(s:SLA)
        OPTIONAL MATCH (s)-[:LATEST_METRIC]->(m:SLAMetric)
        RETURN v.id as venture_id,
               s.name as sla_name,
               s.target as sla_target,
               COALESCE(m.current_value, 0) as current_value,
               COALESCE(m.status, 'unknown') as status
        LIMIT 200
        """

        neo_session = self.memory_client.driver.session()
        sla_metrics = []
        breached = []

        try:
            result = await neo_session.run(query)
            async for record in result:
                metric = {
                    "venture_id": record["venture_id"],
                    "sla_name": record["sla_name"],
                    "target": record["sla_target"],
                    "current": record["current_value"],
                    "status": record["status"],
                }
                sla_metrics.append(metric)

                if record["status"] == "breached":
                    breached.append(metric)
        finally:
            await neo_session.close()

        confidence = 0.95

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            "sla_health_check",
            f"SLA health: {len(sla_metrics)} metrics, {len(breached)} breached",
            confidence,
            "breached" if breached else "healthy",
        )

        # Write to Supabase for VEX dashboard
        await self.supabase.table("sla_health").insert({
            "agent_id": self.agent_id,
            "total_slas": len(sla_metrics),
            "breached_count": len(breached),
            "status": "breached" if breached else "healthy",
            "neo4j_trace_id": trace_id,
            "checked_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "total_slas": len(sla_metrics),
            "breached_count": len(breached),
            "status": "breached" if breached else "healthy",
            "breached_ventures": [b["venture_id"] for b in breached],
            "confidence": confidence,
            "trace_id": trace_id,
        }
