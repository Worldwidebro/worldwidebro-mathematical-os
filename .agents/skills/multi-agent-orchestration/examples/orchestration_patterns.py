"""
Multi-Agent Orchestration Patterns

Implements sequential, parallel, hierarchical, and consensus orchestration.
"""

from typing import List, Dict, Any, Optional
import asyncio
from abc import ABC, abstractmethod


class Agent(ABC):
    """Base agent class."""

    def __init__(self, name: str, role: str, goal: str):
        """Initialize agent."""
        self.name = name
        self.role = role
        self.goal = goal

    @abstractmethod
    def work(self, task: str) -> str:
        """Execute task."""
        pass

    async def work_async(self, task: str) -> str:
        """Execute task asynchronously."""
        return self.work(task)


class SimpleAgent(Agent):
    """Simple agent implementation."""

    def __init__(self, name: str, role: str, goal: str):
        """Initialize simple agent."""
        super().__init__(name, role, goal)

    def work(self, task: str) -> str:
        """Simulate agent work."""
        return f"{self.name}: Completed task - {task[:50]}..."


class SequentialOrchestrator:
    """Orchestrate agents to work sequentially."""

    def __init__(self, agents: List[Agent]):
        """
        Initialize orchestrator with agents.

        Args:
            agents: List of agents to orchestrate
        """
        self.agents = agents
        self.execution_log = []

    def execute(self, initial_task: str) -> Dict[str, Any]:
        """
        Execute agents sequentially.

        Args:
            initial_task: Initial task description

        Returns:
            Execution results dictionary
        """
        current_input = initial_task
        results = {}

        for agent in self.agents:
            result = agent.work(current_input)
            results[agent.name] = result
            self.execution_log.append({
                "agent": agent.name,
                "role": agent.role,
                "task": current_input,
                "result": result,
            })
            # Next agent uses this agent's output
            current_input = result

        return {
            "type": "sequential",
            "results": results,
            "final_output": current_input,
            "execution_log": self.execution_log,
        }


class ParallelOrchestrator:
    """Orchestrate agents to work in parallel."""

    def __init__(self, agents: List[Agent]):
        """Initialize parallel orchestrator."""
        self.agents = agents
        self.execution_log = []

    async def execute_async(self, task: str) -> Dict[str, Any]:
        """
        Execute agents in parallel.

        Args:
            task: Task description

        Returns:
            Execution results dictionary
        """
        # Create async tasks for all agents
        tasks = [agent.work_async(task) for agent in self.agents]

        # Execute all in parallel
        results_list = await asyncio.gather(*tasks)

        results = {
            agent.name: result
            for agent, result in zip(self.agents, results_list)
        }

        self.execution_log.append({
            "type": "parallel",
            "task": task,
            "agents": [a.name for a in self.agents],
            "results": results,
        })

        return {
            "type": "parallel",
            "results": results,
            "execution_log": self.execution_log,
        }

    def execute(self, task: str) -> Dict[str, Any]:
        """Execute agents synchronously (sequential fallback)."""
        return asyncio.run(self.execute_async(task))


class HierarchicalOrchestrator:
    """Orchestrate agents in hierarchical structure."""

    def __init__(self, manager_agent: Agent, specialist_teams: Dict[str, List[Agent]]):
        """
        Initialize hierarchical orchestrator.

        Args:
            manager_agent: Manager agent
            specialist_teams: Dict of team names to lists of agents
        """
        self.manager = manager_agent
        self.specialist_teams = specialist_teams
        self.execution_log = []

    def execute(self, main_task: str) -> Dict[str, Any]:
        """
        Execute with hierarchical structure.

        Args:
            main_task: Main task for manager

        Returns:
            Execution results
        """
        team_results = {}

        # Manager assigns tasks to teams
        for team_name, agents in self.specialist_teams.items():
            # Each team works on their aspect
            team_task = f"{main_task} - Team: {team_name}"
            team_result = {}

            for agent in agents:
                result = agent.work(team_task)
                team_result[agent.name] = result

            team_results[team_name] = team_result

            self.execution_log.append({
                "team": team_name,
                "agents": [a.name for a in agents],
                "results": team_result,
            })

        # Manager synthesizes results
        manager_result = self.manager.work(
            f"Synthesize findings from: {list(team_results.keys())}"
        )

        return {
            "type": "hierarchical",
            "team_results": team_results,
            "manager_synthesis": manager_result,
            "execution_log": self.execution_log,
        }


class GraphOrchestrator:
    """
    Graph-based orchestration with explicit dependency edges.

    Eliminates false dependencies: phases 1-4 run parallel (no real edges).
    Only phase 5 waits on 4 (real edge: spec needs plan).
    """

    def __init__(self, graph: Dict[str, Any]):
        """Initialize with {nodes: [{id, agent}], edges: [{from, to}]}"""
        self.nodes = {n["id"]: n for n in graph["nodes"]}
        self.edges = graph["edges"]
        self.execution_log = []
        self._build_dependency_map()

    def _build_dependency_map(self):
        """Build reverse map: node_id → dependencies."""
        self.dependencies = {nid: [] for nid in self.nodes}
        for edge in self.edges:
            self.dependencies[edge["to"]].append(edge["from"])

    async def execute_async(self, task: str) -> Dict[str, Any]:
        """Execute respecting explicit edges only."""
        results = {}
        completed = set()

        while len(completed) < len(self.nodes):
            ready = [
                nid for nid in self.nodes
                if nid not in completed
                and all(dep in completed for dep in self.dependencies[nid])
            ]

            if not ready:
                raise RuntimeError(f"Circular dependency in graph")

            outputs = await asyncio.gather(*[
                self.nodes[nid]["agent"].work_async(task) for nid in ready
            ])

            for nid, output in zip(ready, outputs):
                results[nid] = output
                completed.add(nid)

        return {"type": "graph", "results": results, "log": self.execution_log}


class LayeredFanInOrchestrator:
    """
    Consolidate large result sets without context collapse.

    Layer 1: Summarize batches (30-50 nodes each) in parallel
    Layer 2: Consolidate batch summaries into final report
    """

    def __init__(self, batch_size: int = 30, summarizer: Optional[Agent] = None,
                 consolidator: Optional[Agent] = None):
        self.batch_size = batch_size
        self.summarizer = summarizer or SimpleAgent("summarizer", "summary", "summarize")
        self.consolidator = consolidator or SimpleAgent("consolidator", "synthesis", "consolidate")

    async def _summarize_batch(self, batch: List[Dict[str, Any]]) -> str:
        """Summarize one batch (Layer 1)."""
        text = "\n".join([f"{r['id']}: {r['output'][:100]}" for r in batch])
        return await self.summarizer.work_async(f"Summarize: {text}")

    async def execute_layered_fanin(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Execute two-layer consolidation."""
        if len(results) < self.batch_size:
            final = await self.consolidator.work_async(f"Consolidate: {results}")
            return {"type": "fanin", "final_report": final}

        batches = [results[i:i+self.batch_size] for i in range(0, len(results), self.batch_size)]
        summaries = await asyncio.gather(*[self._summarize_batch(b) for b in batches])
        final = await self.consolidator.work_async(f"Consolidate summaries: {summaries}")
        return {"type": "fanin", "batch_count": len(batches), "final_report": final}


class SafeConsolidationOrchestrator:
    """Detect silent node failures before consolidation."""

    def __init__(self, expected_count: int):
        self.expected_count = expected_count

    async def execute_safe(self, results: List[Dict[str, Any]],
                          consolidator: Agent) -> Dict[str, Any]:
        """Consolidate only if node count matches expected."""
        actual = len(results)
        if actual < self.expected_count:
            return {
                "type": "error_missing_nodes",
                "expected": self.expected_count,
                "actual": actual,
                "missing": self.expected_count - actual,
                "warning": f"WARNING: {self.expected_count - actual} nodes failed silently",
            }
        return {"type": "consolidated", "result": await consolidator.work_async(f"Consolidate: {results}")}
        self.debate_history = []

    def execute(self, question: str, rounds: int = 2) -> Dict[str, Any]:
        """
        Execute debate and reach consensus.

        Args:
            question: Question for debate
            rounds: Number of debate rounds

        Returns:
            Consensus results
        """
        # Round 1: Initial positions
        positions = {}
        for agent in self.agents:
            position = agent.work(f"Argue your position on: {question}")
            positions[agent.name] = position
            self.debate_history.append({
                "round": 1,
                "agent": agent.name,
                "position": position,
            })

        # Additional rounds: Response to others
        for round_num in range(2, rounds + 1):
            for agent in self.agents:
                other_positions = {
                    name: pos
                    for name, pos in positions.items()
                    if name != agent.name
                }
                response = agent.work(
                    f"Respond to these positions: {str(other_positions)}"
                )
                self.debate_history.append({
                    "round": round_num,
                    "agent": agent.name,
                    "response": response,
                })

        # Mediator reaches consensus
        consensus = self.mediator.work(
            f"Synthesize consensus from debate on: {question}"
        )

        return {
            "type": "consensus",
            "question": question,
            "initial_positions": positions,
            "debate_rounds": rounds,
            "consensus": consensus,
            "debate_history": self.debate_history,
        }


class AdaptiveOrchestrator:
    """Adapt orchestration based on progress."""

    def __init__(self, agents: List[Agent]):
        """Initialize adaptive orchestrator."""
        self.agents = agents
        self.execution_log = []

    def execute_with_adaptation(
        self,
        initial_task: str,
        progress_threshold: float = 0.7,
        quality_threshold: float = 0.6,
    ) -> Dict[str, Any]:
        """
        Execute with adaptive workflow changes.

        Args:
            initial_task: Initial task
            progress_threshold: Threshold for adding resources
            quality_threshold: Threshold for adding validation

        Returns:
            Adaptive execution results
        """
        results = {}
        current_task = initial_task
        active_agents = self.agents.copy()

        for iteration in range(3):
            # Execute with current agents
            iteration_results = {}
            for agent in active_agents:
                result = agent.work(current_task)
                iteration_results[agent.name] = result

            results[f"iteration_{iteration}"] = iteration_results

            # Assess progress
            progress = self._calculate_progress(iteration_results)
            quality = self._calculate_quality(iteration_results)

            log_entry = {
                "iteration": iteration,
                "agents": [a.name for a in active_agents],
                "progress": progress,
                "quality": quality,
            }

            # Adapt based on progress
            if progress < progress_threshold and iteration < 2:
                # Add more agents
                log_entry["adaptation"] = "Added specialist agent"
                self.execution_log.append(log_entry)
            elif quality < quality_threshold and iteration < 2:
                # Add validation step
                log_entry["adaptation"] = "Added validation agent"
                self.execution_log.append(log_entry)
            else:
                self.execution_log.append(log_entry)

        return {
            "type": "adaptive",
            "results": results,
            "adaptations": self.execution_log,
        }

    @staticmethod
    def _calculate_progress(results: Dict) -> float:
        """Calculate progress score."""
        # Simple heuristic based on results
        return min(len(results) / 3.0, 1.0)

    @staticmethod
    def _calculate_quality(results: Dict) -> float:
        """Calculate quality score."""
        # Simple heuristic
        return 0.7  # Placeholder


class WorkflowGraph:
    """Define workflow as directed acyclic graph (DAG)."""

    def __init__(self):
        """Initialize workflow graph."""
        self.nodes = {}
        self.edges = []

    def add_node(self, node_id: str, agent: Agent) -> None:
        """Add agent node."""
        self.nodes[node_id] = agent

    def add_edge(self, from_node: str, to_node: str) -> None:
        """Add dependency edge."""
        self.edges.append((from_node, to_node))

    def execute_dag(self, initial_task: str) -> Dict[str, Any]:
        """
        Execute workflow as DAG.

        Args:
            initial_task: Initial task

        Returns:
            Execution results
        """
        results = {}
        ready_nodes = self._find_ready_nodes()

        while ready_nodes:
            for node_id in ready_nodes:
                agent = self.nodes[node_id]
                # Get input from dependencies
                task_input = self._get_node_input(node_id, results, initial_task)
                result = agent.work(task_input)
                results[node_id] = result

            ready_nodes = self._find_ready_nodes(completed=set(results.keys()))

        return {
            "type": "dag",
            "results": results,
            "nodes": list(self.nodes.keys()),
            "edges": self.edges,
        }

    def _find_ready_nodes(self, completed: Optional[set] = None) -> List[str]:
        """Find nodes with all dependencies completed."""
        if completed is None:
            completed = set()

        ready = []
        for node_id in self.nodes:
            if node_id not in completed:
                dependencies = [
                    from_node
                    for from_node, to_node in self.edges
                    if to_node == node_id
                ]
                if all(dep in completed for dep in dependencies):
                    ready.append(node_id)

        return ready

    def _get_node_input(
        self, node_id: str, results: Dict, initial_task: str
    ) -> str:
        """Get input for node from dependencies."""
        dependencies = [
            from_node for from_node, to_node in self.edges if to_node == node_id
        ]
        if not dependencies:
            return initial_task
        # Combine outputs from dependencies
        return " + ".join(results.get(dep, "") for dep in dependencies)
