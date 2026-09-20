"""
CFO Agent — Cash Flow, Forecasting, Financial Planning
Finance-focused decisions: payroll, vendor payments, tax strategy
Writes to Neo4j reasoning memory + Supabase for VEX visibility
"""

from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta
from decimal import Decimal

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper
from approval_matrix import ApprovalMatrix
from orchestrator_context import OrchestratorContext


class CFOAgent:
    """
    CFO Agent for financial decisions, cash management, forecasting
    - Approval threshold: $10K
    - Escalation: to CEO if >$10K
    - Confidence threshold: 0.8
    - Memory: Working (current cash state) + Episodic (past 20 financial decisions) + Semantic (seasonal patterns)
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.agent_id = "AGT-E002"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.approval_matrix = ApprovalMatrix()
        self.context_assembler = OrchestratorContext(memory_client)

    async def approve_vendor_payment(
        self, vendor_id: str, amount: float, category: str, memo: str
    ) -> Dict[str, Any]:
        """
        Approve vendor payment (payroll, expenses, etc.)
        - Check threshold ($10K max)
        - Auto-escalate if > $10K
        - Log to Neo4j
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        # Assemble financial context
        context = await self.context_assembler.assemble_context(
            entity_id=vendor_id, context_type="vendor_payment"
        )

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Processing {category} payment to {vendor_id}: ${amount}",
            metadata={"context": context},
        )

        # Check cash availability
        available_cash = context.get("cash_position", 0)
        can_afford = amount <= available_cash

        # Check approval threshold
        approved = amount <= 10000 and can_afford
        escalate = amount > 10000

        if approved:
            decision_outcome = "approved"
            recommendation = f"APPROVE: ${amount} payment to {vendor_id} ({category})"
            confidence = 0.9 if can_afford else 0.6
        elif escalate:
            decision_outcome = "escalated_to_ceo"
            recommendation = f"ESCALATE: ${amount} exceeds CFO threshold ($10K). Requires CEO approval."
            confidence = 0.85
        else:
            decision_outcome = "rejected"
            recommendation = f"REJECT: Insufficient cash (available: ${available_cash}, requested: ${amount})"
            confidence = 0.95

        # Log to Neo4j
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"vendor_payment_{vendor_id}",
            f"{category}: {memo}",
            confidence,
            decision_outcome,
        )

        # Write to Supabase for VEX
        await self.supabase.table("financial_decisions").insert({
            "agent_id": self.agent_id,
            "vendor_id": vendor_id,
            "amount": amount,
            "category": category,
            "decision": decision_outcome,
            "confidence": confidence,
            "available_cash": available_cash,
            "can_afford": can_afford,
            "recommendation": recommendation,
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "vendor_id": vendor_id,
            "amount": amount,
            "decision": decision_outcome,
            "recommendation": recommendation,
            "confidence": confidence,
            "escalate": escalate,
            "trace_id": trace_id,
        }

    async def cash_flow_forecast(self, horizon_days: int = 90) -> Dict[str, Any]:
        """
        Generate cash flow forecast for next N days
        - Aggregate revenue from all ventures
        - Project expenses
        - Identify cash crunch periods
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Generating {horizon_days}-day cash flow forecast",
        )

        # Fetch financial metrics from Neo4j
        query = """
        MATCH (v:Venture)
        OPTIONAL MATCH (v)-[:HAS_REVENUE]->(r:Revenue {period: 'mtd'})
        OPTIONAL MATCH (v)-[:HAS_CASH]->(c:CashPosition)
        RETURN v.id as venture_id,
               COALESCE(r.amount, 0) as revenue_mtd,
               COALESCE(c.amount, 0) as cash_position
        LIMIT 100
        """

        neo_session = self.memory_client.driver.session()
        ventures_financial = []
        total_cash = 0
        total_revenue = 0

        try:
            result = await neo_session.run(query)
            async for record in result:
                ventures_financial.append({
                    "venture_id": record["venture_id"],
                    "revenue_mtd": record["revenue_mtd"],
                    "cash": record["cash_position"],
                })
                total_cash += record["cash_position"]
                total_revenue += record["revenue_mtd"]
        finally:
            await neo_session.close()

        # Simple projection: assume current revenue rate + conservative burn
        monthly_revenue = total_revenue
        monthly_burn = total_revenue * 0.3  # Assume 30% expense ratio
        projected_cash_at_horizon = max(
            0, total_cash + (monthly_revenue - monthly_burn) * (horizon_days / 30)
        )

        cash_runway_months = (
            (total_cash / monthly_burn) if monthly_burn > 0 else float("inf")
        )
        at_risk = cash_runway_months < 3

        confidence = 0.75  # Forecasts are inherently uncertain

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            "cash_flow_forecast",
            f"Forecast: runway {cash_runway_months:.1f}mo, projected cash ${projected_cash_at_horizon:,.0f}",
            confidence,
            "at_risk" if at_risk else "healthy",
        )

        # Write to Supabase for VEX dashboard
        await self.supabase.table("cash_flow_forecast").insert({
            "agent_id": self.agent_id,
            "horizon_days": horizon_days,
            "current_cash": total_cash,
            "monthly_revenue": monthly_revenue,
            "monthly_burn": monthly_burn,
            "projected_cash_at_horizon": projected_cash_at_horizon,
            "runway_months": cash_runway_months,
            "at_risk": at_risk,
            "neo4j_trace_id": trace_id,
            "forecast_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "horizon_days": horizon_days,
            "current_cash": total_cash,
            "total_revenue_mtd": total_revenue,
            "monthly_burn": monthly_burn,
            "projected_cash": projected_cash_at_horizon,
            "runway_months": cash_runway_months,
            "at_risk": at_risk,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def quarterly_tax_planning(self, quarter: str) -> Dict[str, Any]:
        """
        Quarterly tax strategy assessment
        - Review anticipated income
        - Recommend deductions
        - Plan estimated tax payments
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Planning tax strategy for Q{quarter}",
        )

        # This would integrate with tax accounting systems
        # For now, log the decision to Neo4j
        confidence = 0.7  # Tax planning requires external expert validation

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"quarterly_tax_planning_q{quarter}",
            f"Quarterly tax assessment for Q{quarter}",
            confidence,
            "requires_expert_review",
        )

        await self.supabase.table("financial_decisions").insert({
            "agent_id": self.agent_id,
            "decision_type": "tax_planning",
            "quarter": quarter,
            "decision": "requires_expert_review",
            "confidence": confidence,
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "decision": "requires_expert_review",
            "quarter": quarter,
            "confidence": confidence,
            "trace_id": trace_id,
        }
