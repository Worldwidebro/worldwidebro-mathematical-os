"""
Venture Orchestrator (AGT-VENTURE-ORCH)
Decision layer: receives tasks, classifies, discovers ready ventures, routes to execution layer
Coordinates 309 venture agents across portfolio
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
import asyncio

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper
from agent_discovery_engine import AgentDiscoveryEngine, OrchestratorDiscoveryClient
from venture_agent_template import VentureAgent


class VentureOrchestrator:
    """
    Central coordinator for all venture operations.
    - Receives tasks from revenue loops
    - Classifies task requirements
    - Discovers ready ventures
    - Distributes to execution layer
    - Aggregates results + tracks revenue
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.agent_id = "AGT-VENTURE-ORCH"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.discovery = AgentDiscoveryEngine(agent_type='orchestration')
        self.orchestrator_api = OrchestratorDiscoveryClient()
        self.venture_agents = {}  # Cached venture agent instances

    async def initialize(self):
        """Initialize orchestrator session."""
        session = await self.memory_wrapper.create_session(self.agent_id)
        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            "Venture Orchestrator initialized",
        )
        return session

    async def get_venture_agent(
        self, venture_id: str, session_manager
    ) -> VentureAgent:
        """Get or create a venture agent instance."""
        if venture_id not in self.venture_agents:
            agent = VentureAgent(
                venture_id,
                self.memory_client,
                self.supabase,
                session_manager,
            )
            await agent.initialize()
            self.venture_agents[venture_id] = agent
        return self.venture_agents[venture_id]

    async def discover_ready_ventures(self, filter_criteria: Dict[str, Any]) -> List[str]:
        """
        Discover ventures ready for a task.
        
        Filter criteria:
        - segment: industry/segment filter
        - min_readiness: minimum readiness % (0-100)
        - max_ventures: max number to parallelize to
        - sector: geographic or business sector
        """
        # Query Supabase for venture status
        response = await self.supabase.table("ventures").select(
            "id, status, readiness_pct, segment, sector"
        ).filter(
            "status", "eq", "operating"
        ).gte(
            "readiness_pct", filter_criteria.get("min_readiness", 30)
        ).execute()

        ventures = response.data if response else []

        # Apply segment filter
        if filter_criteria.get("segment"):
            ventures = [
                v for v in ventures
                if v.get("segment") == filter_criteria["segment"]
            ]

        # Apply sector filter
        if filter_criteria.get("sector"):
            ventures = [
                v for v in ventures
                if v.get("sector") == filter_criteria["sector"]
            ]

        # Limit parallelization
        max_ventures = filter_criteria.get("max_ventures", 10)
        venture_ids = [v["id"] for v in ventures[:max_ventures]]

        return venture_ids

    async def classify_task(self, task_description: str) -> Dict[str, Any]:
        """Classify task using Orchestrator API."""
        classification = await self.orchestrator_api.classify_task(
            task_description
        )
        
        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            f"Classified task: {classification.get('intent')}",
            metadata=classification,
        )
        
        return classification

    async def route_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        End-to-end task routing:
        1. Classify task requirements
        2. Discover ready ventures
        3. Parallelize to execution layer
        4. Aggregate results
        5. Track revenue attribution
        """
        task_id = task.get("task_id", f"TASK-{datetime.utcnow().isoformat()}")
        task_description = task.get("description", "")
        
        # Step 1: Classify
        classification = await self.classify_task(task_description)
        
        if "error" in classification:
            return {
                "task_id": task_id,
                "status": "failed",
                "error": classification["error"],
            }
        
        # Step 2: Discover ready ventures
        filter_criteria = task.get("filter_criteria", {
            "min_readiness": 50,
            "max_ventures": 10,
        })
        
        ready_ventures = await self.discover_ready_ventures(filter_criteria)
        
        if not ready_ventures:
            return {
                "task_id": task_id,
                "status": "no_ready_ventures",
                "ventures_found": 0,
                "filter": filter_criteria,
            }
        
        # Step 3: Parallelize to venture agents
        execution_results = []
        tasks = []
        
        for venture_id in ready_ventures:
            agent = await self.get_venture_agent(venture_id, None)
            tasks.append(
                agent.execute_task({
                    "task_type": classification.get("intent", "general"),
                    "task_data": task.get("task_data", {}),
                    "urgency": task.get("urgency", "normal"),
                    "budget": task.get("budget", 0),
                })
            )
        
        # Run all in parallel
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for venture_id, result in zip(ready_ventures, results):
            if isinstance(result, Exception):
                execution_results.append({
                    "venture_id": venture_id,
                    "status": "failed",
                    "error": str(result),
                })
            else:
                execution_results.append({
                    "venture_id": venture_id,
                    "status": result.get("outcome", "unknown"),
                    "confidence": result.get("confidence", 0),
                    "trace_id": result.get("trace_id"),
                })
        
        # Step 4: Aggregate results
        successful = [r for r in execution_results if r["status"] == "completed"]
        failed = [r for r in execution_results if r["status"] == "failed"]
        
        # Step 5: Track revenue attribution
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            task_id,
            f"Routed to {len(ready_ventures)} ventures: {', '.join(ready_ventures)}",
            confidence=(len(successful) / len(ready_ventures)) if ready_ventures else 0,
            outcome="completed" if successful else "partial",
        )
        
        # Log to Supabase for analytics
        await self.supabase.table("orchestrator_task_routes").insert({
            "task_id": task_id,
            "orchestrator_id": self.agent_id,
            "ventures_routed": len(ready_ventures),
            "ventures_successful": len(successful),
            "ventures_failed": len(failed),
            "task_intent": classification.get("intent"),
            "neo4j_trace_id": trace_id,
            "routed_at": datetime.utcnow().isoformat(),
        }).execute()
        
        return {
            "task_id": task_id,
            "status": "completed" if successful else "partial",
            "orchestrator_agent": self.agent_id,
            "ventures_routed": len(ready_ventures),
            "ventures_successful": len(successful),
            "ventures_failed": len(failed),
            "results": execution_results,
            "trace_id": trace_id,
        }

    async def parallelize_decision(self, task: Dict[str, Any]) -> str:
        """
        Decide: should we parallelize or serialize execution?
        
        Returns: "parallelize" | "serialize" | "single_venture"
        """
        urgency = task.get("urgency", "normal")
        budget = task.get("budget", 0)
        
        # High urgency + high budget → serialize (focus one venture)
        if urgency == "critical" and budget > 5000:
            return "serialize"
        
        # Standard task → parallelize to ready ventures
        return "parallelize"

    async def monitor_portfolio(self) -> Dict[str, Any]:
        """
        Portfolio health check: readiness, burn rates, at-risk ventures.
        Runs hourly via Trigger.dev.
        """
        # Query venture metrics
        response = await self.supabase.table("ventures").select(
            "id, readiness_pct, status, burn_rate, runway_months"
        ).filter("status", "eq", "operating").execute()
        
        ventures = response.data if response else []
        
        # Categorize
        healthy = [v for v in ventures if v["readiness_pct"] >= 50]
        at_risk = [v for v in ventures if v["readiness_pct"] < 50]
        critical_burn = [v for v in ventures if v["runway_months"] < 3]
        
        confidence = 0.95
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            "portfolio_health_check",
            f"Healthy: {len(healthy)}, At-Risk: {len(at_risk)}, Critical: {len(critical_burn)}",
            confidence,
            "monitored",
        )
        
        await self.supabase.table("portfolio_health").insert({
            "healthy_count": len(healthy),
            "at_risk_count": len(at_risk),
            "critical_burn_count": len(critical_burn),
            "total_ventures": len(ventures),
            "neo4j_trace_id": trace_id,
            "checked_at": datetime.utcnow().isoformat(),
        }).execute()
        
        return {
            "agent": self.agent_id,
            "healthy": len(healthy),
            "at_risk": len(at_risk),
            "critical_burn": len(critical_burn),
            "total": len(ventures),
            "trace_id": trace_id,
        }
