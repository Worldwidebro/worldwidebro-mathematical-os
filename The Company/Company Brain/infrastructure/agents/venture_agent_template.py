"""
Venture Agent Template (Simplified)
AGT-VEN-001 to AGT-VEN-309: Execution layer for venture-specific operations
Receives routed tasks from Venture Orchestrator, executes, reports results
Max approval: $500 (operational expenses, customer success)
"""

from typing import Dict, Any, Optional
from datetime import datetime

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper
from session_manager import SessionManager
from trait_memory import TraitMemory
from approval_matrix import ApprovalMatrix


class VentureAgent:
    """
    Simplified venture agent - executes tasks routed by Venture Orchestrator.
    One instance per operating venture (309 total).
    """

    def __init__(
        self,
        venture_id: str,
        memory_client: MemoryClient,
        supabase_client,
        session_manager: SessionManager,
    ):
        self.venture_id = venture_id
        self.agent_id = f"AGT-VEN-{venture_id.split('-')[1]}"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.session_manager = session_manager
        self.trait_memory = TraitMemory(memory_client)
        self.approval_matrix = ApprovalMatrix()

    async def initialize(self):
        """Initialize venture agent session."""
        session = await self.memory_wrapper.create_session(self.agent_id)
        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Venture agent initialized for {self.venture_id}",
            metadata={"venture_id": self.venture_id},
        )
        return session

    async def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a routed task.
        Input: {task_type, task_data, urgency, budget}
        Output: {outcome, confidence, trace_id, metrics}
        """
        session = await self.memory_wrapper.get_session(self.agent_id)

        task_type = task.get("task_type", "unknown")
        task_data = task.get("task_data", {})
        
        await self.memory_wrapper.add_message(
            self.agent_id,
            "user",
            f"Execute {task_type}",
            metadata={"task_data": task_data},
        )

        # Task execution logic
        confidence = 0.8
        outcome = "completed"
        
        # Log to reasoning memory
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"{task_type}_{self.venture_id}_{datetime.utcnow().isoformat()}",
            str(task_data),
            confidence,
            outcome,
        )

        # Write to Supabase for visibility
        await self.supabase.table("venture_task_executions").insert({
            "venture_id": self.venture_id,
            "agent_id": self.agent_id,
            "task_type": task_type,
            "outcome": outcome,
            "confidence": confidence,
            "neo4j_trace_id": trace_id,
            "executed_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "venture_id": self.venture_id,
            "task_type": task_type,
            "outcome": outcome,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def report_metrics(self, metrics: Dict[str, float]) -> Dict[str, Any]:
        """Report venture metrics to shared database."""
        session = await self.memory_wrapper.get_session(self.agent_id)

        confidence = 0.95
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"report_metrics_{self.venture_id}",
            str(metrics),
            confidence,
            "reported",
        )

        await self.supabase.table("venture_metrics").insert({
            "venture_id": self.venture_id,
            "agent_id": self.agent_id,
            "metrics": metrics,
            "neo4j_trace_id": trace_id,
            "reported_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "venture_id": self.venture_id,
            "metrics": metrics,
            "confidence": confidence,
            "trace_id": trace_id,
        }

    async def escalate_exception(
        self, exception_type: str, severity: str, details: str
    ) -> Dict[str, Any]:
        """Escalate exceptions to function orchestrator."""
        session = await self.memory_wrapper.get_session(self.agent_id)

        # Route to appropriate function agent
        escalate_to = {
            "sales": "AGT-F001",
            "financial": "AGT-F002",
            "operations": "AGT-F003",
            "technical": "AGT-F004",
        }.get(exception_type, "AGT-E003")  # Default: COO

        confidence = 0.95
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"escalate_{exception_type}_{self.venture_id}",
            details,
            confidence,
            "escalated",
        )

        await self.supabase.table("venture_exceptions").insert({
            "venture_id": self.venture_id,
            "agent_id": self.agent_id,
            "exception_type": exception_type,
            "severity": severity,
            "details": details,
            "escalated_to": escalate_to,
            "neo4j_trace_id": trace_id,
            "escalated_at": datetime.utcnow().isoformat(),
        }).execute()

        return {
            "agent": self.agent_id,
            "venture_id": self.venture_id,
            "exception_type": exception_type,
            "severity": severity,
            "escalated_to": escalate_to,
            "trace_id": trace_id,
        }

    async def learn_from_outcome(self, outcome_type: str, was_successful: bool):
        """Learning loop: reinforce or penalize traits based on outcomes."""
        await self.trait_memory.reinforce_trait(
            self.venture_id,
            outcome_type,
            was_successful,
        )
