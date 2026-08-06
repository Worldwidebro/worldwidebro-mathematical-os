import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


class PortfolioEvent:
    """Canonical event envelope shared across the portfolio agent OS.

    Every action in every venture emits one of these so the event bus can
    live-update the Neo4j graph, Postgres warehouse, vector store, metrics,
    audit log, dashboards, alerts, and the learning system.
    """

    def __init__(
        self,
        *,
        holding_id: str,
        opco_id: str,
        sector: str,
        venture_id: str,
        team_id: str,
        agent_id: str,
        workflow_id: str,
        run_id: str,
        task_id: str,
        action: str,
        status: str,
        confidence: float,
        tools: List[str],
        timestamp: str,
        human_approval_required: bool = False,
        payload: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.holding_id = holding_id
        self.opco_id = opco_id
        self.sector = sector
        self.venture_id = venture_id
        self.team_id = team_id
        self.agent_id = agent_id
        self.workflow_id = workflow_id
        self.run_id = run_id
        self.task_id = task_id
        self.action = action
        self.status = status
        self.confidence = confidence
        self.tools = tools
        self.timestamp = timestamp
        self.human_approval_required = human_approval_required
        self.payload = payload or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "holding_id": self.holding_id,
            "opco_id": self.opco_id,
            "sector": self.sector,
            "venture_id": self.venture_id,
            "team_id": self.team_id,
            "agent_id": self.agent_id,
            "workflow_id": self.workflow_id,
            "run_id": self.run_id,
            "task_id": self.task_id,
            "action": self.action,
            "status": self.status,
            "confidence": self.confidence,
            "tools": self.tools,
            "timestamp": self.timestamp,
            "human_approval_required": self.human_approval_required,
            "payload": self.payload,
        }


class PortfolioEventBus:
    """In-memory channel that holds emitted events.

    A stand-in that mirrors the event-bus contract consumed by Neo4j,
    Postgres, Qdrant, metrics, and audit. Swap the `record` method for a
    real transport when integrating with the shared substrate.
    """

    def __init__(self) -> None:
        self._events: List[PortfolioEvent] = []

    def record(self, event: PortfolioEvent) -> None:
        self._events.append(event)

    def drain(self) -> List[PortfolioEvent]:
        """Return and clear captured events for a given run."""
        events = self._events
        self._events = []
        return events

    def by_run(self, run_id: str) -> List[PortfolioEvent]:
        return [e for e in self._events if e.run_id == run_id]


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


class PortfolioOrigin:
    """Identifiers grounding a venture's runs in the portfolio OS.

    The dispatch service below is one instance (`LT-011`) of the
    transportation sector under Worldwidebro Holdings.
    """

    HOLDING_ID = "worldwidebro-holdings"
    SECTOR = "transportation"
    TEAM_ID = "dispatch-ops"
    WORKFLOW_ID = "dispatch_v1"

    def __init__(self, opco_id: str = "opco-tran-01", venture_id: str = "venture-lt-011") -> None:
        self.opco_id = opco_id
        self.venture_id = venture_id