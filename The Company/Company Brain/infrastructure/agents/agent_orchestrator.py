"""
Agent Orchestrator — Routes tasks to specialized agents
Coordinates context assembly, decision logging, approval enforcement
"""

import asyncio
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from enum import Enum
import yaml
import logging
from datetime import datetime

from memory_config import MemoryClient, MemorySettings

logger = logging.getLogger(__name__)


class TaskType(Enum):
    """Task types dispatched to agents"""
    VENTURE_HEALTH_CHECK = "venture_health_check"
    COLD_CALL_DISPATCH = "cold_call_dispatch"
    FINANCIAL_FORECAST = "financial_forecast"
    RESOURCE_ALLOCATION = "resource_allocation"
    ESCALATION_DECISION = "escalation_decision"
    APPROVAL_REQUEST = "approval_request"
    DEAL_EVALUATION = "deal_evaluation"
    PORTFOLIO_ANALYSIS = "portfolio_analysis"


@dataclass
class Task:
    """Represents a unit of work for agents"""
    id: str
    type: TaskType
    agent_id: str
    context: Dict[str, Any]
    priority: int = 1  # 1=low, 5=critical
    parent_task: Optional[str] = None
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow()


@dataclass
class Decision:
    """Agent decision output"""
    task_id: str
    agent_id: str
    decision_type: str
    recommendation: str
    reasoning: str
    confidence: float
    requires_approval: bool = False
    approval_agent: Optional[str] = None
    timestamp: datetime = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


class AgentDispatchRouter:
    """Routes tasks to specialized agents by capability + domain"""

    def __init__(self, registry_path: str, memory_client: MemoryClient):
        self.memory_client = memory_client
        self.registry = self._load_registry(registry_path)
        self.agents = {}
        self.tasks_in_flight = {}

    def _load_registry(self, path: str) -> Dict:
        """Load agent registry from YAML"""
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    async def route_task(self, task: Task) -> Decision:
        """
        Route task to agent based on:
        1. Task type → agent capability
        2. Domain → agent domain mapping
        3. Agent availability + capacity
        """
        logger.info(f"Routing task {task.id} ({task.type.value}) to agent {task.agent_id}")

        # Find best agent(s) for this task
        candidates = self._find_agent_candidates(task)
        if not candidates:
            raise ValueError(f"No agents available for {task.type.value}")

        # Select primary agent (highest capability match)
        selected_agent = candidates[0]

        # Assemble context from Neo4j
        context = await self._assemble_context(task, selected_agent)

        # Execute agent
        decision = await self._execute_agent(selected_agent, task, context)

        # Log decision to reasoning memory
        await self.memory_client.add_reasoning_trace(
            agent_id=selected_agent['id'],
            session_id=task.id,
            decision=decision.recommendation,
            reasoning=decision.reasoning,
            confidence=decision.confidence,
            outcome=None  # Filled in later by learning loop
        )

        # Check if approval needed
        if decision.requires_approval:
            decision = await self._route_to_approval(decision)

        return decision

    def _find_agent_candidates(self, task: Task) -> List[Dict]:
        """Find agents that can handle this task"""
        candidates = []

        for agent_data in self.registry['agents'].values():
            # Skip if agent not ready for deployment
            if agent_data.get('deployment_phase') != 'week_4':
                continue

            # Match by capability
            if self._can_handle_task(agent_data, task.type):
                candidates.append(agent_data)

        # Sort by tier priority (executive > function > venture)
        tier_priority = {'executive': 0, 'function': 1, 'venture': 2}
        candidates.sort(
            key=lambda a: tier_priority.get(a['tier'], 99)
        )

        return candidates

    def _can_handle_task(self, agent: Dict, task_type: TaskType) -> bool:
        """Check if agent has capability for task"""
        capabilities = agent.get('capabilities', [])
        required = self._get_required_capabilities(task_type)
        return all(cap in capabilities for cap in required)

    def _get_required_capabilities(self, task_type: TaskType) -> List[str]:
        """Map task type to required agent capabilities"""
        capability_map = {
            TaskType.VENTURE_HEALTH_CHECK: ['neo4j_context_assembly', 'readiness_scoring'],
            TaskType.COLD_CALL_DISPATCH: ['crm_integration', 'decision_logging'],
            TaskType.APPROVAL_REQUEST: ['approval_enforcement', 'decision_logging'],
            TaskType.ESCALATION_DECISION: ['escalation_routing', 'reasoning_trace'],
        }
        return capability_map.get(task_type, ['neo4j_context_assembly'])

    async def _assemble_context(self, task: Task, agent: Dict) -> Dict:
        """
        Assemble agent context from:
        1. Task input context
        2. Neo4j short-term memory (conversation)
        3. Neo4j long-term memory (entities, preferences)
        4. Agent confidence scores (learned)
        """
        context = dict(task.context)  # Start with task context

        # Add short-term memory (conversation history)
        short_term = await self.memory_client.get_short_term_context(task.id)
        context['conversation_history'] = short_term

        # Add agent's reasoning history (for confidence learning)
        reasoning = await self.memory_client.get_agent_reasoning_history(
            agent['id'],
            limit=20
        )
        context['recent_decisions'] = reasoning

        return context

    async def _execute_agent(
        self,
        agent: Dict,
        task: Task,
        context: Dict
    ) -> Decision:
        """Execute agent's decision logic"""
        # In production, this would be:
        # - Call agent's execute() method
        # - Which calls OmniRoute /api/tool/execute for external actions
        # - Which logs to reasoning memory

        # For now, placeholder
        logger.info(f"Executing agent {agent['id']} with task {task.id}")

        decision = Decision(
            task_id=task.id,
            agent_id=agent['id'],
            decision_type=task.type.value,
            recommendation="Execute standard ops",
            reasoning="Context assembled successfully",
            confidence=0.85,
            requires_approval=context.get('amount', 0) > agent.get('approval_threshold', 1000)
        )

        return decision

    async def _route_to_approval(self, decision: Decision) -> Decision:
        """Route decision to approval agent if needed"""
        # Find appropriate approval agent (CEO/CFO/COO)
        approval_agent_id = self._find_approval_agent(decision)

        logger.info(f"Routing decision {decision.task_id} to {approval_agent_id}")
        decision.approval_agent = approval_agent_id
        decision.requires_approval = False  # Mark as routed

        return decision

    def _find_approval_agent(self, decision: Decision) -> str:
        """Find correct approval agent based on decision amount"""
        # Simplified: route to CEO for high-value decisions
        return "AGT-E001"  # CEO

    async def close(self):
        """Cleanup"""
        self.memory_client.close()


async def main():
    """Example orchestration flow"""

    # Initialize
    memory_settings = MemorySettings()
    memory_client = MemoryClient(memory_settings)
    orchestrator = AgentDispatchRouter(
        registry_path="./agent_registry.yaml",
        memory_client=memory_client
    )

    # Create task
    task = Task(
        id="TASK-0001",
        type=TaskType.VENTURE_HEALTH_CHECK,
        agent_id="AGT-VEN-OPS-001",
        context={"venture_id": "OPS-001"}
    )

    # Route and execute
    decision = await orchestrator.route_task(task)
    print(f"Decision: {decision.recommendation} (confidence: {decision.confidence})")

    await orchestrator.close()


if __name__ == "__main__":
    asyncio.run(main())
