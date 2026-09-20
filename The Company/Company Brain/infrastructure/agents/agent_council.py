"""
Agent LLM Council
Multiple agents deliberate and vote on task routing decisions
Pattern: candidate generation → deliberation → voting → selection → learning
"""

from typing import List, Dict, Any, Tuple
import asyncio
from datetime import datetime

from memory_config import MemoryClient
from agent_memory_client import AgentMemoryClientWrapper


class AgentCouncil:
    """
    LLM Council for collaborative agent selection.
    
    When multiple agents could handle a task:
    1. Generate candidates (possible agents)
    2. Each agent self-evaluates (score fit: 0-100)
    3. Aggregate votes (weighted by agent confidence)
    4. Select top K agents
    5. Learn from outcome (update confidence)
    """

    def __init__(self, memory_client: MemoryClient, supabase_client):
        self.council_id = "AGT-COUNCIL"
        self.memory_client = memory_client
        self.memory_wrapper = AgentMemoryClientWrapper(memory_client)
        self.supabase = supabase_client

    async def initialize(self):
        """Initialize council session."""
        session = await self.memory_wrapper.create_session(self.council_id)
        await self.memory_wrapper.add_message(
            self.council_id,
            "system",
            "Agent Council initialized",
        )
        return session

    async def deliberate(
        self,
        task_description: str,
        candidate_agents: List[Dict[str, Any]],
        context: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        """
        Run council deliberation.
        
        Input:
        - task_description: what needs to be done
        - candidate_agents: [{agent_id, agent_type, capabilities, confidence}, ...]
        - context: {venture_ids, segment, urgency, budget, ...}
        
        Output:
        - ranked_agents: sorted by council consensus score
        - deliberation_log: reasoning from each agent
        - recommendation: pick top agent or top K
        """
        if not candidate_agents:
            return {
                "status": "no_candidates",
                "ranked_agents": [],
                "deliberation_log": [],
            }

        await self.memory_wrapper.add_message(
            self.council_id,
            "system",
            f"Council deliberating: {len(candidate_agents)} candidates for '{task_description[:50]}...'",
        )

        # Step 1: Each candidate self-evaluates
        self_scores = await self._get_self_scores(
            task_description, candidate_agents, context
        )

        # Step 2: Aggregate votes
        ranked = self._aggregate_votes(candidate_agents, self_scores)

        # Step 3: Log deliberation
        trace_id = await self.memory_wrapper.log_decision(
            self.council_id,
            f"council_deliberation_{datetime.utcnow().isoformat()}",
            f"Task: {task_description[:100]}\nCandidates: {len(candidate_agents)}\nTop pick: {ranked[0]['agent_id'] if ranked else 'none'}",
            confidence=self._calculate_consensus_confidence(ranked),
            outcome="deliberated",
        )

        # Step 4: Return ranked decision
        return {
            "status": "deliberated",
            "task_description": task_description,
            "candidates_count": len(candidate_agents),
            "ranked_agents": ranked,
            "deliberation_log": self_scores,
            "top_recommendation": ranked[0] if ranked else None,
            "consensus_confidence": self._calculate_consensus_confidence(ranked),
            "trace_id": trace_id,
        }

    async def _get_self_scores(
        self,
        task_description: str,
        candidates: List[Dict[str, Any]],
        context: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        """
        Each candidate agent evaluates its own fit for the task.
        Returns: [{ agent_id, self_score (0-100), reasoning }, ...]
        """
        scores = []

        for candidate in candidates:
            agent_id = candidate.get("agent_id")
            capabilities = candidate.get("capabilities", [])
            agent_confidence = candidate.get("confidence", 0.5)

            # Score calculation:
            # - Capability match: how many required skills does agent have?
            # - Confidence: agent's past success rate
            # - Context fit: venture readiness, budget alignment

            capability_match = self._score_capability_match(
                task_description, capabilities
            )
            confidence_score = int(agent_confidence * 100)
            context_fit = self._score_context_fit(candidate, context)

            # Weighted average
            self_score = int(
                (capability_match * 0.5 + confidence_score * 0.35 + context_fit * 0.15)
            )

            scores.append(
                {
                    "agent_id": agent_id,
                    "self_score": self_score,
                    "capability_match": capability_match,
                    "confidence_score": confidence_score,
                    "context_fit": context_fit,
                    "reasoning": f"Fit: {capability_match}% capabilities, {confidence_score}% confidence, {context_fit}% context match",
                }
            )

        return scores

    def _score_capability_match(self, task: str, capabilities: List[str]) -> int:
        """Score how well agent's capabilities match task."""
        if not capabilities:
            return 0

        # Simple keyword matching (in production: use embedding similarity)
        task_lower = task.lower()
        matched = sum(1 for cap in capabilities if cap.lower() in task_lower)
        return int((matched / len(capabilities)) * 100)

    def _score_context_fit(self, agent: Dict[str, Any], context: Dict[str, Any]) -> int:
        """Score how well agent fits the operational context."""
        if not context:
            return 50

        fit_score = 50  # Neutral baseline

        # Budget alignment
        if context.get("budget"):
            agent_threshold = agent.get("approval_threshold", 5000)
            budget = context.get("budget")
            if budget <= agent_threshold:
                fit_score += 20

        # Agent type alignment
        agent_type = agent.get("agent_type")
        context_need = context.get("agent_type_needed")
        if agent_type == context_need:
            fit_score += 15

        # Venture readiness
        if context.get("min_readiness"):
            agent_readiness = agent.get("readiness_pct", 0)
            min_readiness = context.get("min_readiness", 30)
            if agent_readiness >= min_readiness:
                fit_score += 15

        return min(100, fit_score)

    def _aggregate_votes(
        self, candidates: List[Dict[str, Any]], scores: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Aggregate votes and return ranked agents."""
        # Merge scores back with candidate info
        ranked = []
        for score_entry in scores:
            candidate = next(
                (c for c in candidates if c["agent_id"] == score_entry["agent_id"]),
                None,
            )
            if candidate:
                ranked.append(
                    {
                        **candidate,
                        "council_score": score_entry["self_score"],
                        "score_breakdown": {
                            "capability_match": score_entry["capability_match"],
                            "confidence": score_entry["confidence_score"],
                            "context_fit": score_entry["context_fit"],
                        },
                        "reasoning": score_entry["reasoning"],
                    }
                )

        # Sort by council score (descending)
        ranked.sort(key=lambda x: x.get("council_score", 0), reverse=True)
        return ranked

    def _calculate_consensus_confidence(self, ranked_agents: List[Dict]) -> float:
        """
        Calculate confidence in the council's decision.
        High confidence if: top agent clearly wins, scores are well-distributed
        """
        if not ranked_agents:
            return 0.0

        if len(ranked_agents) == 1:
            return 0.8  # Only one option, decent confidence

        # Score gap between top 2 agents
        top_score = ranked_agents[0].get("council_score", 0)
        second_score = ranked_agents[1].get("council_score", 0)

        gap = top_score - second_score
        # Normalize gap to 0-1 confidence
        confidence = min(1.0, gap / 100.0)

        return max(0.5, confidence)  # Minimum 0.5 confidence

    async def learn_from_outcome(
        self, deliberation_id: str, selected_agent_id: str, was_successful: bool
    ):
        """
        Learning: update agent confidence based on outcome.
        Reinforces agents that succeed, penalizes failures.
        """
        # Query agent's current confidence
        response = await self.supabase.table("agent_confidence").select(
            "confidence_score, success_count, failure_count"
        ).filter("agent_id", "eq", selected_agent_id).single().execute()

        if not response.data:
            return

        current = response.data
        success_count = current.get("success_count", 0)
        failure_count = current.get("failure_count", 0)
        old_confidence = current.get("confidence_score", 0.5)

        # Bayesian update
        if was_successful:
            success_count += 1
        else:
            failure_count += 1

        # New confidence: (successes + 1) / (total + 2) with regularization
        new_confidence = (success_count + 1) / (success_count + failure_count + 2)

        # Update in Supabase
        await self.supabase.table("agent_confidence").update({
            "confidence_score": new_confidence,
            "success_count": success_count,
            "failure_count": failure_count,
            "last_updated": datetime.utcnow().isoformat(),
        }).filter("agent_id", "eq", selected_agent_id).execute()

        # Log learning trace
        await self.memory_wrapper.log_decision(
            self.council_id,
            f"learn_{deliberation_id}_{selected_agent_id}",
            f"Outcome: {'success' if was_successful else 'failure'}\nConfidence: {old_confidence:.2f} → {new_confidence:.2f}",
            confidence=new_confidence,
            outcome="learned",
        )
