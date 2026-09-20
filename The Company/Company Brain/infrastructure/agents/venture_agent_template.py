"""
Venture Agent Template
Base class for 309 venture-specific agents (AGT-VEN-001 to AGT-VEN-309)
Each venture gets: working memory, episodic memory, semantic memory, shared databases
Max approval: $500 (operational expenses, customer success, small tools)
"""

from typing import Dict, Any, Optional
from datetime import datetime

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper, AgentSession
from session_manager import SessionManager
from trait_memory import TraitMemory
from approval_matrix import ApprovalMatrix


class VentureAgent:
    """
    Base class for venture-specific agents
    - Per-venture Neo4j session for memory isolation
    - Access to approval matrix ($500 max)
    - Integration with shared databases (Neo4j + Supabase)
    - Learning loop (confidence scoring)
    """

    def __init__(
        self,
        venture_id: str,
        memory_client: MemoryClient,
        supabase_client,
        session_manager: SessionManager,
    ):
        self.venture_id = venture_id
        self.agent_id = f"AGT-VEN-{venture_id.split('-')[1]}"  # e.g., AGT-VEN-001
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.session_manager = session_manager
        self.trait_memory = TraitMemory(memory_client)
        self.approval_matrix = ApprovalMatrix()

    async def initialize(self) -> AgentSession:
        """
        Initialize venture agent session
        - Create per-venture Neo4j session
        - Load working memory
        - Initialize trait learning
        """

        session = await self.memory_wrapper.create_session(self.agent_id)

        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Venture agent initialized for {self.venture_id}",
            metadata={"venture_id": self.venture_id},
        )

        return session

    async def execute_operational_task(
        self, task_type: str, task_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Execute standard venture operational task
        - Customer outreach
        - Sales follow-up
        - Support escalation
        - Metric reporting
        """

        session = await self.memory_wrapper.get_session(self.agent_id)

        # Add task to conversation history
        await self.memory_wrapper.add_message(
            self.agent_id,
            "user",
            f"Execute {task_type}",
            metadata={"task_data": task_data},
        )

        # Determine task outcome
        confidence = 0.8
        outcome = "completed"
        recommendation = f"Executed {task_type} for {self.venture_id}"

        # Log decision to reasoning memory
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"{task_type}_{self.venture_id}",
            str(task_data),
            confidence,
            outcome,
        )

        # Write to Supabase for VEX visibility
        await self.supabase.table("venture_tasks").insert({
            "venture_id": self.venture_id,
            "agent_id": self.agent_id,
            "task_type": task_type,
            "task_data": task_data,
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

    async def report_metrics(
        self, metrics: Dict[str, float]
    ) -> Dict[str, Any]:
        """
        Report venture metrics to shared database
        - Revenue, pipeline, team size, readiness
        - Aggregated for portfolio views
        """

        session = await self.memory_wrapper.get_session(self.agent_id)

        confidence = 0.95

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"report_metrics_{self.venture_id}",
            f"Metrics: {metrics}",
            confidence,
            "reported",
        )

        # Write to Supabase
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
        """
        Escalate exceptions to function orchestrator
        - Readiness below threshold
        - Budget breach
        - SLA violation
        """

        session = await self.memory_wrapper.get_session(self.agent_id)

        # Escalate to appropriate function agent based on type
        escalate_to = {
            "sales": "AGT-F001",  # Sales Orchestrator
            "financial": "AGT-F002",  # Finance Orchestrator
            "operations": "AGT-F003",  # Ops Orchestrator
            "technical": "AGT-F004",  # Tech Orchestrator
        }.get(exception_type, "AGT-E003")  # Default to COO

        confidence = 0.95

        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            f"escalate_{exception_type}_{self.venture_id}",
            details,
            confidence,
            "escalated",
        )

        # Write to Supabase for exception tracking
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

    async def learn_from_outcome(
        self, outcome_type: str, was_successful: bool
    ) -> None:
        """
        Learning loop: reinforce or penalize traits based on outcomes
        - Increases confidence for correct predictions
        - Decreases for wrong ones
        - Decays old learnings over time
        """

        await self.trait_memory.reinforce_trait(
            self.venture_id,
            outcome_type,
            was_successful,
        )
