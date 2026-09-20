"""
Session Manager — Multi-agent session coordination
When multiple agents work on same task (e.g., CEO + CFO on capital decision)
Coordinates context sharing + conflict resolution
"""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import asyncio
import logging
from enum import Enum

from agent_memory_client import AgentMemoryClientWrapper, AgentSession

logger = logging.getLogger(__name__)


class SessionState(Enum):
    ACTIVE = "active"
    AWAITING_APPROVAL = "awaiting_approval"
    COMPLETE = "complete"
    ESCALATED = "escalated"
    FAILED = "failed"


@dataclass
class SharedSession:
    """Session shared across multiple agents"""
    session_id: str
    primary_agent_id: str
    participants: Set[str] = field(default_factory=set)  # agent IDs
    state: SessionState = SessionState.ACTIVE
    created_at: datetime = field(default_factory=datetime.utcnow)
    last_updated: datetime = field(default_factory=datetime.utcnow)
    context: Dict = field(default_factory=dict)  # Shared context
    decision_log: List[Dict] = field(default_factory=list)  # Decisions made
    approval_status: Dict[str, str] = field(default_factory=dict)  # agent -> approved/rejected
    sla_deadline: Optional[datetime] = None


class SessionManager:
    """
    Manages shared sessions for multi-agent workflows
    Handles context propagation + conflict resolution
    """

    def __init__(self, memory_wrapper: AgentMemoryClientWrapper):
        self.memory_wrapper = memory_wrapper
        self.sessions: Dict[str, SharedSession] = {}
        self.agent_to_session: Dict[str, str] = {}  # agent_id -> session_id

    async def create_shared_session(
        self,
        primary_agent_id: str,
        participant_agents: List[str],
        context: Dict,
        sla_hours: int = 4
    ) -> SharedSession:
        """Create session for multi-agent workflow"""
        session_id = f"SHARED-{primary_agent_id}-{datetime.utcnow().timestamp()}"

        session = SharedSession(
            session_id=session_id,
            primary_agent_id=primary_agent_id,
            participants=set([primary_agent_id] + participant_agents),
            context=context,
            sla_deadline=datetime.utcnow() + timedelta(hours=sla_hours)
        )

        self.sessions[session_id] = session

        # Map all participants to this session
        for agent_id in session.participants:
            self.agent_to_session[agent_id] = session_id

        # Propagate context to all agents
        for agent_id in session.participants:
            await self._propagate_context(session_id, agent_id, context)

        logger.info(
            f"Created shared session {session_id}: "
            f"primary={primary_agent_id}, participants={participant_agents}"
        )

        return session

    async def add_participant(
        self,
        session_id: str,
        agent_id: str
    ):
        """Add agent to existing session"""
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")

        session = self.sessions[session_id]
        session.participants.add(agent_id)
        self.agent_to_session[agent_id] = session_id

        # Propagate context to new participant
        await self._propagate_context(session_id, agent_id, session.context)

        logger.info(f"Added agent {agent_id} to session {session_id}")

    async def _propagate_context(
        self,
        session_id: str,
        agent_id: str,
        context: Dict
    ):
        """Send shared context to agent"""
        agent_session = await self.memory_wrapper.get_session(agent_id)

        # Store context in agent's session
        agent_session.entity_context.update(context)

        # Add metadata message
        await self.memory_wrapper.add_message(
            agent_id=agent_id,
            role="system",
            content=f"Joined shared session {session_id}",
            metadata={"shared_context": context}
        )

    async def log_agent_decision(
        self,
        session_id: str,
        agent_id: str,
        decision: Dict
    ):
        """Log decision in shared session"""
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")

        session = self.sessions[session_id]

        # Add to session log
        session.decision_log.append({
            "agent_id": agent_id,
            "decision": decision,
            "timestamp": datetime.utcnow().isoformat()
        })

        session.last_updated = datetime.utcnow()

        # Propagate decision to other participants
        await self._broadcast_decision(session_id, agent_id, decision)

    async def _broadcast_decision(
        self,
        session_id: str,
        agent_id: str,
        decision: Dict
    ):
        """Broadcast agent's decision to other participants"""
        session = self.sessions[session_id]

        for participant_id in session.participants:
            if participant_id != agent_id:
                await self.memory_wrapper.add_message(
                    agent_id=participant_id,
                    role="system",
                    content=f"Agent {agent_id} decided: {decision.get('recommendation')}",
                    metadata={"decision": decision, "from_agent": agent_id}
                )

    async def record_approval(
        self,
        session_id: str,
        agent_id: str,
        decision: str  # "approved", "rejected", "needs_info"
    ):
        """Record agent's approval/rejection"""
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")

        session = self.sessions[session_id]
        session.approval_status[agent_id] = decision

        # Check if all approvals received
        if len(session.approval_status) == len(session.participants) - 1:  # -1 for primary agent
            await self._resolve_session(session_id)

    async def _resolve_session(self, session_id: str):
        """Resolve session when all approvals received"""
        session = self.sessions[session_id]

        # Check if all approved
        all_approved = all(
            status == "approved"
            for status in session.approval_status.values()
        )

        if all_approved:
            session.state = SessionState.COMPLETE
            logger.info(f"Session {session_id} COMPLETE - all participants approved")
        else:
            session.state = SessionState.ESCALATED
            logger.warn(f"Session {session_id} ESCALATED - not all approvals")

    async def get_session_status(self, session_id: str) -> Dict:
        """Get current status of shared session"""
        if session_id not in self.sessions:
            return {"error": "Session not found"}

        session = self.sessions[session_id]

        return {
            "session_id": session_id,
            "state": session.state.value,
            "primary_agent": session.primary_agent_id,
            "participants": list(session.participants),
            "decisions": len(session.decision_log),
            "approvals": session.approval_status,
            "created_at": session.created_at.isoformat(),
            "sla_deadline": session.sla_deadline.isoformat() if session.sla_deadline else None,
            "time_remaining_minutes": (
                (session.sla_deadline - datetime.utcnow()).total_seconds() / 60
                if session.sla_deadline else None
            )
        }

    async def check_sla_breaches(self) -> List[str]:
        """Find sessions that missed SLA"""
        now = datetime.utcnow()
        breached = []

        for session_id, session in self.sessions.items():
            if session.state == SessionState.ACTIVE and session.sla_deadline:
                if now > session.sla_deadline:
                    breached.append(session_id)
                    logger.error(f"SLA breach: session {session_id}")

        return breached

    async def escalate_session(self, session_id: str, reason: str):
        """Escalate session to higher-level approver"""
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")

        session = self.sessions[session_id]
        session.state = SessionState.ESCALATED
        session.context["escalation_reason"] = reason

        logger.warn(f"Escalated session {session_id}: {reason}")

    async def cleanup_old_sessions(self, days: int = 7):
        """Remove old completed sessions"""
        cutoff = datetime.utcnow() - timedelta(days=days)

        to_remove = [
            session_id for session_id, session in self.sessions.items()
            if session.state == SessionState.COMPLETE and session.last_updated < cutoff
        ]

        for session_id in to_remove:
            del self.sessions[session_id]

        logger.info(f"Cleaned up {len(to_remove)} old sessions")


__all__ = [
    "SessionState",
    "SharedSession",
    "SessionManager",
]
