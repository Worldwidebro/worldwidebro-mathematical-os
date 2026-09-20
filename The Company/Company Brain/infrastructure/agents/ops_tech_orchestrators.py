"""
Ops & Tech Orchestrators
AGT-F003 (Ops): SLA monitoring, exception handling
AGT-F004 (Tech): Deployment coordination, infrastructure decisions
Max approval: $3K (ops), $2.5K (tech)
"""

from typing import Dict, Any, List
from datetime import datetime

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper
from orchestrator_context import OrchestratorContext


class OpsOrchestrator:
    """
    Ops Orchestrator: monitors SLAs, coordinates exception handling, resource allocation
    Max approval: $3K
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.agent_id = "AGT-F003"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.context_assembler = OrchestratorContext(memory_client)

    async def check_sla_compliance(self) -> Dict[str, Any]:
        """
        Check SLA compliance across all ventures
        - Response times
        - Uptime
        - Delivery metrics
        - Flag breaches
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            "Checking SLA compliance across all ventures",
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
        """

        neo_session = self.memory_client.driver.session()
        slas = []
        breached_count = 0

        try:
            result = await neo_session.run(query)
            async for record in result:
                sla = {
                    "venture_id": record["venture_id"],
                    "sla_name": record["sla_name"],
                    "target": record["sla_target"],
                    "current": record["current_value"],
                    "status": record["status"],
                }
                slas.append(sla)
                if record["status"] == "breached":
                    breached_count += 1
        finally:
            await neo_session.close()

        confidence = 0.95

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            "check_sla_compliance",
            f"Total SLAs: {len(slas)}, Breached: {breached_count}",
            confidence,
            "breached" if breached_count > 0 else "compliant",
        )

        await self.supabase.table("sla_compliance").insert({
            "agent_id": self.agent_id,
            "total_slas": len(slas),
            "breached_count": breached_count,
            "status": "breached" if breached_count > 0 else "compliant",
            "neo4j_trace_id": trace_id,
            "checked_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "total_slas": len(slas),
            "breached_count": breached_count,
            "status": "breached" if breached_count > 0 else "compliant",
            "sla_details": slas,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def approve_ops_tool(
        self, tool_name: str, vendor: str, amount: float, justification: str
    ) -> Dict[str, Any]:
        """
        Approve operations tools/services ($3K max)
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        approved = amount <= 3000

        decision = "approved" if approved else "escalated_to_coo"
        confidence = 0.85
        recommendation = (
            f"APPROVE: ${amount} for {tool_name} from {vendor}"
            if approved
            else f"ESCALATE: ${amount} exceeds $3K ops tool limit"
        )

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"ops_tool_{tool_name}",
            justification,
            confidence,
            decision,
        )

        await self.supabase.table("financial_decisions").insert({
            "agent_id": self.agent_id,
            "decision_type": "ops_tool",
            "tool_name": tool_name,
            "vendor": vendor,
            "amount": amount,
            "decision": decision,
            "confidence": confidence,
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "tool_name": tool_name,
            "amount": amount,
            "decision": decision,
            "recommendation": recommendation,
            "confidence": confidence,
            "trace_id": trace_id,
        }


class TechOrchestrator:
    """
    Tech Orchestrator: deployment coordination, infrastructure decisions, monitoring
    Max approval: $2.5K
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.agent_id = "AGT-F004"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.context_assembler = OrchestratorContext(memory_client)

    async def approve_deployment(
        self, venture_id: str, environment: str, version: str, risk_level: str
    ) -> Dict[str, Any]:
        """
        Approve deployment to environment
        - Check risk level
        - Verify infrastructure readiness
        - Log decision
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Reviewing deployment: {venture_id} v{version} to {environment}",
        )

        # Check infrastructure readiness
        context = await self.context_assembler.assemble_context(
            venture_id, "deployment_readiness"
        )

        infrastructure_ok = context.get("infrastructure_status", "unknown") == "ready"

        if risk_level == "high":
            decision = "requires_cto_approval"
            confidence = 0.9
            recommendation = "ESCALATE: High-risk deployment requires CTO approval"
        elif not infrastructure_ok:
            decision = "blocked"
            confidence = 0.95
            recommendation = "BLOCKED: Infrastructure not ready"
        else:
            decision = "approved"
            confidence = 0.9
            recommendation = f"APPROVE: Deploy {venture_id} v{version} to {environment}"

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"deployment_{venture_id}_{version}",
            f"{environment}, risk={risk_level}",
            confidence,
            decision,
        )

        await self.supabase.table("deployment_decisions").insert({
            "agent_id": self.agent_id,
            "venture_id": venture_id,
            "version": version,
            "environment": environment,
            "risk_level": risk_level,
            "decision": decision,
            "confidence": confidence,
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "venture_id": venture_id,
            "version": version,
            "environment": environment,
            "decision": decision,
            "recommendation": recommendation,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def monitor_infrastructure(self) -> Dict[str, Any]:
        """
        Monitor infrastructure health across all ventures
        - Uptime
        - Resource utilization
        - Error rates
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            "Monitoring infrastructure health",
        )

        # Fetch infrastructure metrics from Neo4j
        query = """
        MATCH (v:Venture)-[:HAS_INFRASTRUCTURE]->(inf:Infrastructure)
        OPTIONAL MATCH (inf)-[:HAS_METRIC]->(m:InfraMetric)
        RETURN v.id as venture_id,
               inf.status as infra_status,
               COALESCE(m.uptime_pct, 0) as uptime_pct,
               COALESCE(m.error_rate, 0) as error_rate
        """

        neo_session = self.memory_client.driver.session()
        infrastructure_data = []
        degraded_count = 0

        try:
            result = await neo_session.run(query)
            async for record in result:
                uptime = record["uptime_pct"]
                error_rate = record["error_rate"]

                status = "healthy" if uptime > 0.99 and error_rate < 0.01 else "degraded"
                if status == "degraded":
                    degraded_count += 1

                infrastructure_data.append({
                    "venture_id": record["venture_id"],
                    "status": status,
                    "uptime": uptime,
                    "error_rate": error_rate,
                })
        finally:
            await neo_session.close()

        confidence = 0.95

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            "monitor_infrastructure",
            f"Total: {len(infrastructure_data)}, Degraded: {degraded_count}",
            confidence,
            "degraded" if degraded_count > 0 else "healthy",
        )

        await self.supabase.table("infrastructure_health").insert({
            "agent_id": self.agent_id,
            "total_infrastructure": len(infrastructure_data),
            "degraded_count": degraded_count,
            "status": "degraded" if degraded_count > 0 else "healthy",
            "neo4j_trace_id": trace_id,
            "monitored_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "total_infrastructure": len(infrastructure_data),
            "degraded_count": degraded_count,
            "status": "degraded" if degraded_count > 0 else "healthy",
            "infrastructure": infrastructure_data,
            "confidence": confidence,
            "trace_id": trace_id,
        }
