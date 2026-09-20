"""
Orchestrator Context Assembly
Builds rich context from Neo4j for agent decision-making
Combines working memory, episodic memory, semantic memory, and learned traits
"""

from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta

from memory_config import MemoryClient


class OrchestratorContext:
    """
    Assembles complete context for agent decisions
    Sources:
    - Working memory: current task + recent conversation
    - Episodic memory: past decisions + outcomes
    - Semantic memory: entity traits, patterns, learned preferences
    - Reasoning memory: decision traces, confidence scores
    """

    def __init__(self, memory_client: MemoryClient):
        self.memory_client = memory_client

    async def assemble_context(
        self, entity_id: str, context_type: str = "general"
    ) -> Dict[str, Any]:
        """
        Assemble complete context for an entity (venture, prospect, etc.)
        Returns: operational metrics, historical decisions, learned traits, reasoning traces
        """

        session = self.memory_client.driver.session()

        try:
            # 1. Fetch entity metrics (operational/financial)
            metrics = await self._fetch_entity_metrics(session, entity_id, context_type)

            # 2. Fetch decision history (episodic memory)
            decisions = await self._fetch_decision_history(session, entity_id)

            # 3. Fetch learned traits (semantic memory)
            traits = await self._fetch_learned_traits(session, entity_id)

            # 4. Fetch reasoning traces (recent decisions)
            traces = await self._fetch_reasoning_traces(session, entity_id)

            # Assemble into context dict
            context = {
                "entity_id": entity_id,
                "context_type": context_type,
                "assembled_at": datetime.utcnow().isoformat(),
                **metrics,  # Operational metrics
                "decision_history": decisions,
                "learned_traits": traits,
                "reasoning_traces": traces,
            }

            return context

        finally:
            await session.close()

    async def _fetch_entity_metrics(
        self, session, entity_id: str, context_type: str
    ) -> Dict[str, Any]:
        """
        Fetch operational metrics based on context type
        """

        if context_type == "capital_deployment":
            query = """
            MATCH (v:Venture {id: $id})
            OPTIONAL MATCH (v)-[:HAS_METRIC]->(m:Metric {type: 'readiness'})
            OPTIONAL MATCH (v)-[:HAS_CASH]->(c:CashPosition)
            OPTIONAL MATCH (v)-[:HAS_TEAM]->(t:Team)
            OPTIONAL MATCH (v)-[:HAS_REVENUE]->(r:Revenue {period: 'mtd'})
            RETURN v.name as venture_name,
                   COALESCE(m.value, 0.0) as readiness_pct,
                   COALESCE(c.amount, 0) as cash_position,
                   COALESCE(SIZE(t.members), 0) as team_size,
                   COALESCE(r.amount, 0) as revenue_mtd
            """

        elif context_type == "vendor_payment":
            query = """
            MATCH (c:Company {id: $id})
            OPTIONAL MATCH (c)-[:HAS_CASH]->(cash:CashPosition)
            OPTIONAL MATCH (c)-[:HAS_PAYABLE]->(p:Payable)
            RETURN c.name as vendor_name,
                   COALESCE(cash.amount, 0) as cash_position,
                   COALESCE(SUM(p.amount), 0) as pending_payables
            """

        elif context_type == "operational_readiness":
            query = """
            MATCH (v:Venture {id: $id})
            OPTIONAL MATCH (v)-[:HAS_METRIC]->(m:Metric)
            OPTIONAL MATCH (v)-[:HAS_TEAM]->(t:Team)
            OPTIONAL MATCH (v)-[:HAS_INFRASTRUCTURE]->(inf:Infrastructure)
            RETURN v.name as venture_name,
                   COALESCE((m WHERE m.type='readiness').value, 0.0) as readiness_pct,
                   COALESCE(SIZE(t.members), 0) as team_size,
                   COALESCE(inf.status, 'unknown') as infrastructure_status
            """

        else:  # general context
            query = """
            MATCH (e {id: $id})
            OPTIONAL MATCH (e)-[:HAS_METRIC]->(m)
            OPTIONAL MATCH (e)-[:HAS_CASH]->(c)
            RETURN e.name as entity_name,
                   COALESCE(m.value, 0.0) as readiness_pct,
                   COALESCE(c.amount, 0) as cash_position
            LIMIT 1
            """

        result = await session.run(query, {"id": entity_id})
        record = await result.single()

        if record:
            return {k: record[k] for k in record.keys()}
        else:
            return {"entity_id": entity_id, "entity_found": False}

    async def _fetch_decision_history(
        self, session, entity_id: str, limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Fetch past decisions about this entity (episodic memory)
        """

        query = """
        MATCH (r:ReasoningTrace)-[:ABOUT]->(e {id: $id})
        RETURN r.id as trace_id,
               r.decision as decision,
               r.outcome as outcome,
               r.confidence as confidence,
               r.timestamp as timestamp
        ORDER BY r.timestamp DESC
        LIMIT $limit
        """

        result = await session.run(query, {"id": entity_id, "limit": limit})
        records = await result.data()

        decisions = []
        for record in records:
            decisions.append({
                "trace_id": record["trace_id"],
                "decision": record["decision"],
                "outcome": record["outcome"],
                "confidence": record["confidence"],
                "timestamp": record["timestamp"],
            })

        return decisions

    async def _fetch_learned_traits(
        self, session, entity_id: str
    ) -> Dict[str, Any]:
        """
        Fetch learned traits for entity (semantic memory)
        Traits with confidence >= 0.75 are considered strong
        """

        query = """
        MATCH (e {id: $id})-[:HAS_TRAIT]->(t:Trait)
        RETURN t.category as category,
               t.value as value,
               t.confidence as confidence,
               t.observations as observations
        ORDER BY t.confidence DESC
        """

        result = await session.run(query, {"id": entity_id})
        records = await result.data()

        traits = {}
        strong_traits = {}

        for record in records:
            category = record["category"]
            traits[category] = {
                "value": record["value"],
                "confidence": record["confidence"],
                "observations": record["observations"],
            }

            if record["confidence"] >= 0.75:
                strong_traits[category] = record["value"]

        return {"all_traits": traits, "strong_traits": strong_traits}

    async def _fetch_reasoning_traces(
        self, session, entity_id: str, hours: int = 24, limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Fetch recent reasoning traces (decision audit trail)
        Helps understand what was decided and why
        """

        cutoff = datetime.utcnow() - timedelta(hours=hours)

        query = """
        MATCH (r:ReasoningTrace)
        WHERE r.timestamp > $cutoff
        OPTIONAL MATCH (r)-[:ABOUT]->(e {id: $id})
        WHERE e IS NOT NULL
        RETURN r.id as trace_id,
               r.agent_id as agent_id,
               r.decision as decision,
               r.reasoning as reasoning,
               r.confidence as confidence,
               r.outcome as outcome,
               r.timestamp as timestamp
        ORDER BY r.timestamp DESC
        LIMIT $limit
        """

        result = await session.run(
            query, {"id": entity_id, "cutoff": cutoff.isoformat(), "limit": limit}
        )
        records = await result.data()

        traces = []
        for record in records:
            traces.append({
                "trace_id": record["trace_id"],
                "agent_id": record["agent_id"],
                "decision": record["decision"],
                "reasoning": record["reasoning"],
                "confidence": record["confidence"],
                "outcome": record["outcome"],
                "timestamp": record["timestamp"],
            })

        return traces
