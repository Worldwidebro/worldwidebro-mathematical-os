"""
Agent Discovery Engine
Agents query this at __init__ to discover available skills and capabilities
"""

import json
import asyncio
from typing import List, Dict, Optional
from pathlib import Path


class AgentDiscoveryEngine:
    """Runtime agent skill and capability discovery."""
    
    # Path to skills index (built by index_skills.py)
    SKILLS_INDEX_PATH = Path.home() / 'Documents/The Company/Company Brain/_REGISTRIES/CANONICAL/SKILLS-INDEX.json'
    
    # Agent tier to skill tier mapping
    AGENT_TIER_ACCESS = {
        'executive': ['tier1', 'tier2'],           # CEO/CFO/COO access top 2 tiers
        'function': ['tier1', 'tier2'],            # Sales/Finance/Ops/Tech orchestrators
        'venture': ['tier2', 'tier3'],             # Venture agents access standard + extended
        'integration': ['tier1', 'tier2', 'tier3'], # Integration agents access all
    }
    
    def __init__(self, agent_type: str = 'venture'):
        """Initialize discovery engine for an agent type."""
        self.agent_type = agent_type
        self.skills_index = self._load_skills_index()
    
    def _load_skills_index(self) -> Dict:
        """Load the skills index from disk."""
        try:
            with open(self.SKILLS_INDEX_PATH, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'metadata': {'total_skills': 0},
                'skills': {},
                'by_tier': {'tier1': [], 'tier2': [], 'tier3': []},
                'trigger_index': {},
                'tool_index': {},
            }
    
    def get_available_skills(self) -> List[str]:
        """Get all skills available to this agent type."""
        tiers = self.AGENT_TIER_ACCESS.get(self.agent_type, ['tier2'])
        skills = []
        for tier in tiers:
            skills.extend(self.skills_index.get('by_tier', {}).get(tier, []))
        return list(set(skills))
    
    def get_skills_by_trigger(self, trigger: str) -> List[str]:
        """Get skills matching a trigger phrase."""
        all_matches = self.skills_index.get('trigger_index', {}).get(trigger, [])
        available = self.get_available_skills()
        return [s for s in all_matches if s in available]
    
    def get_skills_by_tool(self, tool: str) -> List[str]:
        """Get skills that require a specific tool."""
        all_matches = self.skills_index.get('tool_index', {}).get(tool, [])
        available = self.get_available_skills()
        return [s for s in all_matches if s in available]
    
    def get_skill_metadata(self, skill_name: str) -> Optional[Dict]:
        """Get metadata for a specific skill."""
        return self.skills_index.get('skills', {}).get(skill_name)
    
    def discover(self) -> Dict:
        """Return full capability discovery landscape."""
        available_skills = self.get_available_skills()
        
        return {
            'agent_type': self.agent_type,
            'accessible_tiers': self.AGENT_TIER_ACCESS.get(self.agent_type, []),
            'total_available_skills': len(available_skills),
            'skills': available_skills,
            'discovery_metadata': {
                'total_indexed_skills': self.skills_index['metadata']['total_skills'],
                'unique_triggers': len(self.skills_index.get('trigger_index', {})),
                'unique_tools': len(self.skills_index.get('tool_index', {})),
            },
            'sampling': {
                'tier1_sample': self.skills_index['by_tier']['tier1'][:3],
                'tier2_sample': self.skills_index['by_tier']['tier2'][:5],
                'tier3_sample': self.skills_index['by_tier']['tier3'][:3],
            }
        }


class OrchestratorDiscoveryClient:
    """Client for discovering agent skills via Orchestrator Prime API."""
    
    ORCHESTRATOR_URL = "http://localhost:20128"
    
    async def classify_task(self, task_description: str, venture_id: str = None) -> Dict:
        """
        Classify a task to extract required skills.
        
        Returns dict with:
        - intent: what the task is trying to do
        - required_skills: skill IDs needed
        - required_capabilities: capability names
        - autonomy_suggested: L1, L2, or L3
        """
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.ORCHESTRATOR_URL}/api/orchestrator/classify-task",
                    json={
                        "description": task_description,
                        "venture": venture_id,
                    }
                ) as resp:
                    if resp.status == 200:
                        return await resp.json()
        except Exception as e:
            return {
                'error': str(e),
                'required_skills': [],
                'required_capabilities': [],
            }
    
    async def find_best_agents(self, required_skills: List[str]) -> List[Dict]:
        """
        Discover best agents for required skills.
        
        Returns ordered list of agents ranked by relevance.
        """
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.ORCHESTRATOR_URL}/api/orchestrator/find-best-agents",
                    json={'required_skills': required_skills}
                ) as resp:
                    if resp.status == 200:
                        return await resp.json()
        except Exception as e:
            return []
    
    async def execute_task_with_best_agent(
        self,
        task_description: str,
        venture_id: str = None
    ) -> Dict:
        """
        End-to-end: classify task → find agents → execute.
        
        Returns result from best agent.
        """
        # Classify the task
        classification = await self.classify_task(task_description, venture_id)
        
        if 'error' in classification:
            return classification
        
        # Find best agents
        required_skills = classification.get('required_skills', [])
        agents = await self.find_best_agents(required_skills)
        
        if not agents:
            return {'error': 'No agents available for this task'}
        
        # Execute with best agent
        best_agent = agents[0]
        
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.ORCHESTRATOR_URL}/api/orchestrator/execute-task",
                    json={
                        "task_id": f"TASK-{venture_id or 'ADHOC'}",
                        "description": task_description,
                        "agent_id": best_agent.get('id'),
                    }
                ) as resp:
                    if resp.status == 200:
                        return await resp.json()
        except Exception as e:
            return {'error': str(e)}
