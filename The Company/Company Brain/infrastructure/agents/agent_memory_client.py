"""
Agent Memory Client Wrapper
Session management + multi-type memory access
Each agent gets a session for short/long/reasoning memory
"""

from typing import Optional, Dict, Any, List
from dataclasses import dataclass
from datetime import datetime
import asyncio
import logging
from uuid import uuid4

from memory_config import MemoryClient

logger = logging.getLogger(__name__)


@dataclass
class AgentSession:
    """Per-agent session for maintaining context"""
    session_id: str
    agent_id: str
    user_id: Optional[str]
    started_at: datetime
    last_activity: datetime
    conversation_history: List[Dict] = None
    entity_context: Dict = None
    reasoning_traces: List[Dict] = None

    def __post_init__(self):
        if self.conversation_history is None:
            self.conversation_history = []
        if self.entity_context is None:
            self.entity_context = {}
        if self.reasoning_traces is None:
            self.reasoning_traces = []


class AgentMemoryClientWrapper:
    """
    Wraps memory_config.MemoryClient for agent use
    Manages sessions + provides convenient methods for agent logic
    """

    def __init__(self, memory_client: MemoryClient):
        self.memory_client = memory_client
        self.sessions: Dict[str, AgentSession] = {}
        self.agent_sessions: Dict[str, str] = {}  # agent_id -> session_id

    async def create_session(
        self,
        agent_id: str,
        user_id: Optional[str] = None
    ) -> AgentSession:
        """Create new session for agent"""
        session_id = str(uuid4())
        session = AgentSession(
            session_id=session_id,
            agent_id=agent_id,
            user_id=user_id,
            started_at=datetime.utcnow(),
            last_activity=datetime.utcnow()
        )

        self.sessions[session_id] = session
        self.agent_sessions[agent_id] = session_id

        logger.info(f"Created session {session_id} for agent {agent_id}")
        return session

    async def get_session(
        self,
        agent_id: str,
        or_create: bool = True
    ) -> Optional[AgentSession]:
        """Get agent's current session"""
        session_id = self.agent_sessions.get(agent_id)

        if session_id and session_id in self.sessions:
            session = self.sessions[session_id]
            session.last_activity = datetime.utcnow()
            return session

        if or_create:
            return await self.create_session(agent_id)

        return None

    async def add_message(
        self,
        agent_id: str,
        role: str,
        content: str,
        metadata: Optional[Dict] = None
    ) -> str:
        """Add message to agent's session"""
        session = await self.get_session(agent_id)

        # Add to memory
        msg_id = await self.memory_client.add_short_term_memory(
            session_id=session.session_id,
            role=role,
            content=content,
            metadata=metadata
        )

        # Add to local session
        session.conversation_history.append({
            "id": msg_id,
            "role": role,
            "content": content,
            "timestamp": datetime.utcnow().isoformat()
        })

        return msg_id

    async def get_conversation(
        self,
        agent_id: str,
        limit: int = 50
    ) -> List[Dict]:
        """Get conversation history for agent"""
        session = await self.get_session(agent_id)
        return session.conversation_history[-limit:]

    async def get_full_context(
        self,
        agent_id: str
    ) -> Dict[str, Any]:
        """Get complete context for agent decision-making"""
        session = await self.get_session(agent_id)

        # Get short-term memory
        short_term = await self.memory_client.get_short_term_context(
            session.session_id
        )

        # Get agent's reasoning history
        reasoning = await self.memory_client.get_agent_reasoning_history(
            agent_id,
            limit=20
        )

        return {
            "session_id": session.session_id,
            "agent_id": agent_id,
            "conversation": short_term,
            "recent_decisions": reasoning,
            "entities": session.entity_context,
            "session_start": session.started_at.isoformat(),
            "last_activity": session.last_activity.isoformat()
        }

    async def log_decision(
        self,
        agent_id: str,
        decision: str,
        reasoning: str,
        confidence: float,
        outcome: Optional[str] = None
    ) -> str:
        """Log agent decision for learning"""
        session = await self.get_session(agent_id)

        trace_id = await self.memory_client.add_reasoning_trace(
            agent_id=agent_id,
            session_id=session.session_id,
            decision=decision,
            reasoning=reasoning,
            confidence=confidence,
            outcome=outcome
        )

        session.reasoning_traces.append({
            "id": trace_id,
            "decision": decision,
            "confidence": confidence,
            "timestamp": datetime.utcnow().isoformat()
        })

        return trace_id

    async def add_entity(
        self,
        agent_id: str,
        name: str,
        entity_type: str,
        description: Optional[str] = None,
        attributes: Optional[Dict] = None
    ) -> str:
        """Add entity to agent's context"""
        session = await self.get_session(agent_id)

        entity_id = await self.memory_client.add_entity(
            name=name,
            entity_type=entity_type,
            description=description,
            attributes=attributes
        )

        session.entity_context[entity_id] = {
            "name": name,
            "type": entity_type,
            "description": description
        }

        return entity_id

    async def add_preference(
        self,
        agent_id: str,
        entity_id: str,
        category: str,
        preference: str,
        confidence: float = 0.7
    ):
        """Add learned preference for entity"""
        await self.memory_client.add_preference(
            entity_id=entity_id,
            category=category,
            preference=preference,
            confidence=confidence
        )

        logger.info(
            f"Agent {agent_id} learned preference: "
            f"{entity_id}.{category} = {preference}"
        )

    async def get_decision_history(
        self,
        agent_id: str,
        limit: int = 100
    ) -> List[Dict]:
        """Get agent's decision history for analysis"""
        return await self.memory_client.get_agent_reasoning_history(
            agent_id,
            limit=limit
        )

    async def close_session(self, agent_id: str):
        """Close agent's session"""
        session_id = self.agent_sessions.get(agent_id)
        if session_id and session_id in self.sessions:
            del self.sessions[session_id]
            del self.agent_sessions[agent_id]
            logger.info(f"Closed session {session_id} for agent {agent_id}")

    async def cleanup(self):
        """Cleanup all sessions"""
        self.sessions.clear()
        self.agent_sessions.clear()
        self.memory_client.close()


# Global instance (initialized in orchestrator)
_memory_wrapper: Optional[AgentMemoryClientWrapper] = None


async def get_memory_wrapper(memory_client: MemoryClient) -> AgentMemoryClientWrapper:
    """Get or create global memory wrapper"""
    global _memory_wrapper
    if _memory_wrapper is None:
        _memory_wrapper = AgentMemoryClientWrapper(memory_client)
    return _memory_wrapper


__all__ = [
    "AgentSession",
    "AgentMemoryClientWrapper",
    "get_memory_wrapper",
]
