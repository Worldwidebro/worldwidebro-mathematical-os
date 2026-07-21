#!/usr/bin/env python3
import os
import sys
import yaml
import asyncio
from typing import Dict, List, Any, Set
from datetime import datetime

# Add parent path to allow importing agent_engine
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from services.agent_engine import AgentRegistry, SimpleLangAgent, AgentTask
except ImportError:
    # Inline fallback imports if absolute path is different
    from agent_engine import AgentRegistry, SimpleLangAgent, AgentTask

class WorkflowDefinition:
    def __init__(self, yaml_content: str):
        self.data = yaml.safe_load(yaml_content) or {}
        self.name = self.data.get('name', 'Unnamed Workflow')
        self.steps = self.data.get('steps', [])
        self.trigger = self.data.get('trigger', 'manual')
    
    def get_dependencies(self) -> Dict[str, List[str]]:
        deps = {}
        for s in self.steps:
            deps[s['id']] = s.get('depends_on', [])
        return deps


class WorkflowRunner:
    def __init__(self):
        self.results = {}
        self.task_states = {} # pending, running, completed, failed

    def _topological_sort(self, deps: Dict[str, List[str]]) -> List[str]:
        # Simple Kahn's algorithm or DFS topological sort
        sorted_steps = []
        visited = set()
        temp = set()

        def visit(node):
            if node in temp:
                raise ValueError(f"Cycle detected in workflow dependencies: {node}")
            if node not in visited:
                temp.add(node)
                for edge in deps.get(node, []):
                    if edge in deps: # Verify dependency node exists
                        visit(edge)
                temp.remove(node)
                visited.add(node)
                sorted_steps.append(node)

        for step in deps:
            if step not in visited:
                visit(step)
        return sorted_steps

    async def run(self, workflow_def: WorkflowDefinition, on_step_callback=None) -> Dict[str, Any]:
        self.results = {}
        self.task_states = {s['id']: 'pending' for s in workflow_def.steps}
        deps = workflow_def.get_dependencies()
        
        try:
            sorted_steps = self._topological_sort(deps)
        except ValueError as e:
            return {"status": "failed", "error": str(e)}

        async def execute_step(step: Dict[str, Any]):
            step_id = step['id']
            self.task_states[step_id] = 'running'
            if on_step_callback:
                await on_step_callback(step_id, 'running', None)

            # Wait for dependencies to finish successfully
            for dep_id in deps.get(step_id, []):
                while dep_id not in self.results:
                    await asyncio.sleep(0.1)
                
                # Check if a dependency failed
                dep_res = self.results[dep_id]
                if isinstance(dep_res, dict) and dep_res.get('status') == 'failed':
                    self.task_states[step_id] = 'failed'
                    self.results[step_id] = {"status": "failed", "error": f"Dependency {dep_id} failed."}
                    if on_step_callback:
                        await on_step_callback(step_id, 'failed', self.results[step_id])
                    return

            # Dispatch task
            agent_name = step.get('agent', 'CEO Agent')
            agent_info = AgentRegistry.get_agent_info(agent_name) or {}
            capabilities = agent_info.get('capabilities', [])
            
            agent = SimpleLangAgent(agent_name, capabilities)
            task = AgentTask(
                id=step_id,
                type=step.get('type', 'default'),
                payload=step.get('params', {}),
                context={"workflow": workflow_def.name, "timestamp": str(datetime.now())}
            )
            
            try:
                # Add synthetic delay to simulate agent reasoning and work
                await asyncio.sleep(1.0)
                res = await agent.execute(task)
                self.results[step_id] = res
                self.task_states[step_id] = 'completed'
            except Exception as e:
                self.results[step_id] = {"status": "failed", "error": str(e)}
                self.task_states[step_id] = 'failed'
            
            if on_step_callback:
                await on_step_callback(step_id, self.task_states[step_id], self.results[step_id])

        # Run concurrent step tasks
        tasks = []
        for step in workflow_def.steps:
            tasks.append(execute_step(step))
            
        await asyncio.gather(*tasks)
        return {
            "status": "completed",
            "workflow": workflow_def.name,
            "results": self.results,
            "states": self.task_states
        }

if __name__ == '__main__':
    # Dry run sample
    workflow_yaml = """
    name: Launch New Venture
    steps:
      - id: market_research
        agent: CEO Agent
        params: { industry: "beauty", region: "US" }
      - id: business_plan
        agent: Finance Agent
        depends_on: [market_research]
        params: { target: "skincare" }
      - id: legal_setup
        agent: Operations Agent
        depends_on: [business_plan]
    """
    wd = WorkflowDefinition(workflow_yaml)
    runner = WorkflowRunner()
    async def log_step(sid, state, res):
        print(f"Step {sid} is now {state}. Output: {res}")
    asyncio.run(runner.run(wd, log_step))
