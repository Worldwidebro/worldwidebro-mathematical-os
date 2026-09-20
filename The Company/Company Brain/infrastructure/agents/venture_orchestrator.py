"""
Venture Orchestrator (AGT-VENTURE-ORCH)
Decision layer with LLM Council deliberation
Receives tasks → classifies → councils deliberate → routes to execution layer
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
import asyncio

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper
from agent_discovery_engine import AgentDiscoveryEngine, OrchestratorDiscoveryClient
from agent_council import AgentCouncil
from venture_agent_template import VentureAgent


class VentureOrchestrator:
    """
    Central coordinator for all venture operations.
    
    Flow:
    1. Receive task from revenue loop
    2. Classify task requirements
    3. Discover candidate ventures
    4. Run council deliberation (ventures self-score task fit)
    5. Select top K ventures via consensus
    6. Parallelize execution to selected agents
    7. Aggregate + learn from outcomes
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.agent_id = "AGT-VENTURE-ORCH"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client
        self.discovery = AgentDiscoveryEngine(agent_type='orchestration')
        self.orchestrator_api = OrchestratorDiscoveryClient()
        self.council = AgentCouncil(memory_client, supabase_client)
        self.venture_agents = {}  # Cached venture agent instances

    async def initialize(self):
        """Initialize orchestrator and council."""
        session = await self.memory_wrapper.create_session(self.agent_id)
        await self.memory_wrapper.add_message(
            self.agent_id,
            "system",
            "Venture Orchestrator initialized",
        )
        await self.council.initialize()
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

    async def discover_candidate_ventures(
        self, filter_criteria: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Discover ventures that COULD handle the task.
        Returns candidate list with metadata for council deliberation.
        """
        response = await self.supabase.table("ventures").select(
            "id, name, status, readiness_pct, segment, sector, capabilities, confidence_score"
        ).filter(
            "status", "eq", "operating"
        ).gte(
            "readiness_pct", filter_criteria.get("min_readiness", 30)
        ).execute()

        ventures = response.data if response else []

        # Apply filters
        if filter_criteria.get("segment"):
            ventures = [
                v for v in ventures
                if v.get("segment") == filter_criteria["segment"]
            ]

        if filter_criteria.get("sector"):
            ventures = [
                v for v in ventures
                if v.get("sector") == filter_criteria["sector"]
            ]

        # Convert to candidate format
        candidates = [
            {
                "agent_id": f"AGT-VEN-{v['id'].split('-')[1]}",
                "venture_id": v["id"],
                "venture_name": v.get("name", v["id"]),
                "agent_type": "venture",
                "capabilities": v.get("capabilities", []),
                "confidence": v.get("confidence_score", 0.5),
                "readiness_pct": v.get("readiness_pct", 0),
                "approval_threshold": 500,
            }
            for v in ventures
        ]

        return candidates

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
        End-to-end task routing with council deliberation:
        1. Classify task requirements
        2. Discover candidate ventures
        3. Council deliberates (ventures self-score fit)
        4. Select top K by consensus
        5. Parallelize to selected agents
        6. Aggregate results + track revenue
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
        
        # Step 2: Discover candidates
        filter_criteria = task.get("filter_criteria", {
            "min_readiness": 50,
        })
        
        candidates = await self.discover_candidate_ventures(filter_criteria)
        
        if not candidates:
            return {
                "task_id": task_id,
                "status": "no_candidates",
                "candidates_found": 0,
                "filter": filter_criteria,
            }
        
        # Step 3: Council deliberation
        context = {
            "task_description": task_description,
            "budget": task.get("budget", 0),
            "urgency": task.get("urgency", "normal"),
            "min_readiness": filter_criteria.get("min_readiness", 30),
            "agent_type_needed": "venture",
        }
        
        council_decision = await self.council.deliberate(
            task_description=task_description,
            candidate_agents=candidates,
            context=context,
        )
        
        if council_decision["status"] != "deliberated":
            return {
                "task_id": task_id,
                "status": "deliberation_failed",
                "error": "Council could not deliberate",
            }
        
        # Step 4: Select top K ventures
        ranked_agents = council_decision.get("ranked_agents", [])
        max_ventures = task.get("max_parallel_ventures", 5)
        selected_agents = ranked_agents[:max_ventures]
        
        if not selected_agents:
            return {
                "task_id": task_id,
                "status": "no_selected_agents",
            }
        
        # Step 5: Parallelize execution
        execution_results = []
        tasks = []
        
        for agent_info in selected_agents:
            venture_id = agent_info["venture_id"]
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
        
        for agent_info, result in zip(selected_agents, results):
            venture_id = agent_info["venture_id"]
            council_score = agent_info.get("council_score", 0)
            
            if isinstance(result, Exception):
                execution_results.append({
                    "venture_id": venture_id,
                    "council_score": council_score,
                    "status": "failed",
                    "error": str(result),
                })
            else:
                execution_results.append({
                    "venture_id": venture_id,
                    "council_score": council_score,
                    "status": result.get("outcome", "unknown"),
                    "confidence": result.get("confidence", 0),
                    "trace_id": result.get("trace_id"),
                })
        
        # Step 6: Aggregate + learn
        successful = [r for r in execution_results if r["status"] == "completed"]
        
        # Update council confidence scores based on outcomes
        for result in execution_results:
            agent_id = f"AGT-VEN-{result['venture_id'].split('-')[1]}"
            was_successful = result["status"] == "completed"
            await self.council.learn_from_outcome(
                deliberation_id=task_id,
                selected_agent_id=agent_id,
                was_successful=was_successful,
            )
        
        # Log to Supabase
        trace_id = await self.memory_wrapper.log_decision(
            self.agent_id,
            task_id,
            f"Council routed to {len(selected_agents)} ventures: {[r['venture_id'] for r in selected_agents]}",
            confidence=(len(successful) / len(selected_agents)) if selected_agents else 0,
            outcome="completed" if successful else "partial",
        )
        
        await self.supabase.table("orchestrator_task_routes").insert({
            "task_id": task_id,
            "orchestrator_id": self.agent_id,
            "candidates_discovered": len(candidates),
            "council_score": council_decision.get("consensus_confidence", 0),
            "agents_selected": len(selected_agents),
            "agents_successful": len(successful),
            "agents_failed": len(execution_results) - len(successful),
            "task_intent": classification.get("intent"),
            "neo4j_trace_id": trace_id,
            "routed_at": datetime.utcnow().isoformat(),
        }).execute()
        
        return {
            "task_id": task_id,
            "status": "completed" if successful else "partial",
            "orchestrator_agent": self.agent_id,
            "council_decision": {
                "candidates_evaluated": len(candidates),
                "consensus_confidence": council_decision.get("consensus_confidence", 0),
                "agents_selected": len(selected_agents),
                "top_agent": selected_agents[0].get("venture_id") if selected_agents else None,
            },
            "execution_results": execution_results,
            "agents_successful": len(successful),
            "agents_failed": len(execution_results) - len(successful),
            "trace_id": trace_id,
        }

    async def monitor_portfolio(self) -> Dict[str, Any]:
        """
        Portfolio health check: readiness, burn rates, at-risk ventures.
        Runs hourly via Trigger.dev.
        """
        response = await self.supabase.table("ventures").select(
            "id, readiness_pct, status, burn_rate, runway_months"
        ).filter("status", "eq", "operating").execute()
        
        ventures = response.data if response else []
        
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
