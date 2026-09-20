"""
Finance Orchestrator (AGT-F002)
Consolidates P&L, triggers CFO approvals for >$10K, tracks financial health
Max approval: $2K
"""

from typing import Dict, Any
from datetime import datetime

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper
from orchestrator_context import OrchestratorContext


class FinanceOrchestrator:
    """
    Function agent: coordinates financial operations across ventures
    - P&L consolidation
    - Expense tracking + CFO escalation ($10K threshold)
    - Financial health monitoring
    - Reporting to CFO
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.agent_id = "AGT-F002"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.context_assembler = OrchestratorContext(memory_client)

    async def consolidate_p_l(self, period: str = "mtd") -> Dict[str, Any]:
        """
        Consolidate P&L across all ventures
        - Revenue aggregation
        - Expense aggregation
        - Gross margin calculation
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Consolidating P&L for {period}",
        )

        # Fetch financial metrics from Neo4j
        query = """
        MATCH (v:Venture)
        OPTIONAL MATCH (v)-[:HAS_REVENUE]->(r:Revenue {period: $period})
        OPTIONAL MATCH (v)-[:HAS_EXPENSE]->(e:Expense {period: $period})
        RETURN v.id as venture_id,
               COALESCE(r.amount, 0) as revenue,
               COALESCE(SUM(e.amount), 0) as expenses
        """

        neo_session = self.memory_client.driver.session()
        total_revenue = 0
        total_expenses = 0
        ventures = []

        try:
            result = await neo_session.run(query, {"period": period})
            async for record in result:
                ven_revenue = record["revenue"]
                ven_expenses = record["expenses"]
                total_revenue += ven_revenue
                total_expenses += ven_expenses

                ventures.append({
                    "venture_id": record["venture_id"],
                    "revenue": ven_revenue,
                    "expenses": ven_expenses,
                    "margin": (ven_revenue - ven_expenses) / ven_revenue if ven_revenue > 0 else 0,
                })
        finally:
            await neo_session.close()

        gross_profit = total_revenue - total_expenses
        gross_margin = (gross_profit / total_revenue) if total_revenue > 0 else 0

        confidence = 0.95

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"consolidate_p_l_{period}",
            f"Revenue: ${total_revenue:,.0f}, Expenses: ${total_expenses:,.0f}",
            confidence,
            "monitored",
        )

        # Write to Supabase
        await self.supabase.table("consolidated_p_l").insert({
            "period": period,
            "total_revenue": total_revenue,
            "total_expenses": total_expenses,
            "gross_profit": gross_profit,
            "gross_margin": gross_margin,
            "venture_count": len(ventures),
            "neo4j_trace_id": trace_id,
            "consolidated_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "period": period,
            "total_revenue": total_revenue,
            "total_expenses": total_expenses,
            "gross_profit": gross_profit,
            "gross_margin": gross_margin,
            "ventures": ventures,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def trigger_cfo_approval(
        self, expense_id: str, amount: float, category: str, justification: str
    ) -> Dict[str, Any]:
        """
        Trigger CFO approval for expenses >$10K
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        if amount > 10000:
            decision = "escalated_to_cfo"
            recommendation = f"ESCALATE to CFO: ${amount} {category} requires approval"
            confidence = 0.9
        elif amount <= 2000:
            decision = "approved"
            recommendation = f"APPROVE: ${amount} {category} within $2K limit"
            confidence = 0.9
        else:
            decision = "escalated_to_cfo"
            recommendation = f"ESCALATE to CFO: ${amount} {category} exceeds $2K threshold"
            confidence = 0.85

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"expense_approval_{expense_id}",
            justification,
            confidence,
            decision,
        )

        await self.supabase.table("financial_decisions").insert({
            "agent_id": self.agent_id,
            "expense_id": expense_id,
            "amount": amount,
            "category": category,
            "decision": decision,
            "confidence": confidence,
            "recommendation": recommendation,
            "neo4j_trace_id": trace_id,
            "decided_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "expense_id": expense_id,
            "amount": amount,
            "decision": decision,
            "recommendation": recommendation,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def monitor_burn_rate(self, venture_id: str) -> Dict[str, Any]:
        """
        Monitor burn rate for individual venture
        - Current monthly burn
        - Trend (increasing/stable/decreasing)
        - Runway estimate
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        # Fetch expense trend from Neo4j
        query = """
        MATCH (v:Venture {id: $venture_id})-[:HAS_EXPENSE]->(e:Expense)
        RETURN DATE(e.recorded_at) as expense_date,
               SUM(e.amount) as daily_burn
        ORDER BY expense_date DESC
        LIMIT 30
        """

        neo_session = self.memory_client.driver.session()
        burn_data = []

        try:
            result = await neo_session.run(query, {"venture_id": venture_id})
            async for record in result:
                burn_data.append({
                    "date": record["expense_date"],
                    "burn": record["daily_burn"],
                })
        finally:
            await neo_session.close()

        # Calculate average daily burn
        avg_daily_burn = sum(b["burn"] for b in burn_data) / len(burn_data) if burn_data else 0
        monthly_burn = avg_daily_burn * 30

        # Get cash position for runway
        context = await self.context_assembler.assemble_context(
            venture_id, "venture_burn_rate"
        )
        cash = context.get("cash_position", 0)
        runway_months = (cash / monthly_burn) if monthly_burn > 0 else float("inf")

        at_risk = runway_months < 3

        confidence = 0.9

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"monitor_burn_{venture_id}",
            f"Monthly burn: ${monthly_burn:,.0f}, Runway: {runway_months:.1f}mo",
            confidence,
            "at_risk" if at_risk else "healthy",
        )

        await self.supabase.table("burn_rate_monitoring").insert({
            "venture_id": venture_id,
            "monthly_burn": monthly_burn,
            "cash_position": cash,
            "runway_months": runway_months,
            "at_risk": at_risk,
            "neo4j_trace_id": trace_id,
            "monitored_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "venture_id": venture_id,
            "monthly_burn": monthly_burn,
            "cash_position": cash,
            "runway_months": runway_months,
            "at_risk": at_risk,
            "confidence": confidence,
            "trace_id": trace_id,
        }
