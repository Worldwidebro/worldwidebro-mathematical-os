"""
Agent Layer: Executive Role Registry + Runtime
===============================================

Three things kept separate:
- Role = numbered seat with schema (data, in roles dict)
- Agent = software that can occupy a seat (code)
- Person = human who can also occupy a seat

An agent never pretends to be a human. It's bound to a ROLE_NUMBER,
inherits that role's authority/KPIs/approval gates, and hands off when
a step requires a human seat.
"""

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Any, Callable, Optional, Protocol


# ---- ROLE REGISTRY ----

class HumanRequired(str, Enum):
    NEVER     = "never"
    OPTIONAL  = "optional"
    APPROVAL  = "approval"
    ALWAYS    = "always"


@dataclass(frozen=True)
class Role:
    """A numbered organizational seat. Not a person. Not an agent."""
    number: int
    name: str
    department: str
    purpose: str
    authority: tuple[str, ...] = ()
    inputs: tuple[str, ...] = ()
    outputs: tuple[str, ...] = ()
    decisions: tuple[str, ...] = ()
    skills: tuple[str, ...] = ()
    tools: tuple[str, ...] = ()
    mcps: tuple[str, ...] = ()
    agents: tuple[int, ...] = ()
    workflows: tuple[str, ...] = ()
    upstream: tuple[int, ...] = ()
    downstream: tuple[int, ...] = ()
    manager: Optional[int] = None
    kpis: tuple[str, ...] = ()
    cost: str = "opex"
    revenue_impact: str = "indirect"
    human_required: HumanRequired = HumanRequired.APPROVAL
    ai_capable: bool = True
    approval_required: bool = False

    @property
    def id(self) -> str:
        return f"R{self.number:03d}"

    def __repr__(self) -> str:
        return f"<{self.id} {self.name} [{self.department}]>"


# Simplified master registry (key roles shown; extend as needed)
ROLES: dict[int, Role] = {
    1: Role(1, "CEO", "Executive Leadership", "Overall company strategy and results"),
    4: Role(4, "Chief of Staff", "Executive Leadership", "Coordinates CEO and cross-functional execution"),
    24: Role(24, "Product Manager", "Product Management", "Owns product outcome"),
    57: Role(57, "Software Engineer", "Software Engineering", "Software development"),
    87: Role(87, "Agent Engineer", "AI / ML", "Builds AI agents and agent systems"),
    114: Role(114, "SDET", "Quality / Testing", "Software engineering for testing"),
    164: Role(164, "Account Executive", "Sales", "Closes deals"),
    165: Role(165, "SDR", "Sales", "Creates sales opportunities"),
    221: Role(221, "Controller", "Finance", "Accounting controls"),
    340: Role(340, "AI Operations Director", "AI Automation", "Enterprise AI operations"),
    348: Role(348, "AI Evaluation Engineer", "AI Automation", "Measures agent/model performance"),
}

# Autonomy defaults
_HUMAN_ALWAYS  = {1, 221}
_AGENT_NATIVE  = set(range(340, 350))
_MONEY_ROLES   = {164, 167, 168, 221, 226}


def _apply_defaults() -> None:
    for n, r in list(ROLES.items()):
        hr, ai, ap = HumanRequired.APPROVAL, True, False
        if n in _HUMAN_ALWAYS:
            hr, ai, ap = HumanRequired.ALWAYS, False, True
        elif n in _AGENT_NATIVE:
            hr, ai, ap = HumanRequired.OPTIONAL, True, False
        if n in _MONEY_ROLES:
            ap = True
        ROLES[n] = replace(r, human_required=hr, ai_capable=ai,
                           approval_required=ap)


_apply_defaults()


# ---- AGENT RUNTIME ----

class LLM(Protocol):
    """Pluggable: OpenAI, Anthropic, vLLM, mock."""
    def complete(self, system: str, user: str, **kw) -> str: ...


@dataclass
class ToolSpec:
    name: str
    description: str
    fn: Callable[..., Any]
    mcp: Optional[str] = None
    requires_approval: bool = False


@dataclass
class Task:
    goal: str
    inputs: dict = field(default_factory=dict)
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    parent_id: Optional[str] = None
    from_role: Optional[int] = None


@dataclass
class AgentResult:
    ok: bool
    role_number: int
    output: dict
    handoff_to: Optional[int] = None
    requires_approval: bool = False
    cost_usd: float = 0.0
    tokens: int = 0
    trace: list[str] = field(default_factory=list)
    started_at: float = field(default_factory=time.time)
    ended_at: float = 0.0

    def finish(self) -> AgentResult:
        self.ended_at = time.time()
        return self

    @property
    def duration_ms(self) -> float:
        return (self.ended_at - self.started_at) * 1000


class BaseAgent:
    """A software occupant of exactly one numbered seat."""

    role_number: int = -1
    capabilities: tuple[str, ...] = ()

    def __init__(
        self,
        role_obj: Role,
        llm: LLM,
        tools: Optional[dict[str, ToolSpec]] = None,
    ) -> None:
        self.role = role_obj
        self.llm = llm
        self.tools = tools or {}
        self.memory: list[dict] = []

    def system_prompt(self) -> str:
        r = self.role
        return (
            f"You are the agent occupying seat {r.id}: {r.name}.\n"
            f"Department: {r.department}\n"
            f"Purpose: {r.purpose}\n"
            f"Human oversight: {r.human_required.value}\n"
            "Act only within this seat. Hand off rather than overreach."
        )

    def execute(self, task: Task) -> dict:
        """Override. Return the seat's output payload."""
        raise NotImplementedError

    def run(self, task: Task) -> AgentResult:
        result = AgentResult(
            ok=False,
            role_number=self.role.number,
            output={},
            trace=[f"{self.role.id}:{task.id} begin"],
        )
        try:
            payload = self.execute(task)
            result.output = payload
            result.ok = True
            result.trace.append(f"{self.role.id}: execute ok")
        except Exception as exc:
            result.output = {"error": str(exc)}
            result.trace.append(f"{self.role.id}: error {exc!r}")
            return result.finish()

        if self.role.approval_required:
            result.requires_approval = True
            result.trace.append(f"{self.role.id}: queued for human approval")
            return result.finish()

        nxt = getattr(self, "_next_role", None)
        if nxt is not None:
            result.handoff_to = nxt
            result.trace.append(f"{self.role.id}: handoff -> R{nxt:03d}")

        self.memory.append({"task": task.id, "output": result.output})
        return result.finish()

    def call_llm(self, user: str, **kw) -> str:
        return self.llm.complete(self.system_prompt(), user, **kw)

    def use_tool(self, name: str, **kwargs) -> Any:
        if name not in self.tools:
            raise KeyError(f"tool '{name}' not bound to {self.role.id}")
        spec = self.tools[name]
        if spec.requires_approval:
            raise PermissionError(f"tool '{name}' requires human approval")
        return spec.fn(**kwargs)


AGENT_CLASSES: dict[int, type[BaseAgent]] = {}


def register(*role_numbers: int):
    """Bind an agent class to one or more seat numbers."""
    def deco(cls: type[BaseAgent]) -> type[BaseAgent]:
        for n in role_numbers:
            if n not in ROLES:
                raise KeyError(f"unknown role number {n}")
            AGENT_CLASSES[n] = cls
            cls.role_number = n
        return cls
    return deco


class GenericRoleAgent(BaseAgent):
    """Fallback for unspecialized seats."""
    def execute(self, task: Task) -> dict:
        prompt = (
            f"Task: {task.goal}\n"
            f"Inputs: {task.inputs}\n"
            "Produce the deliverable this seat owns."
        )
        plan = self.call_llm(prompt)
        return {
            "seat": self.role.id,
            "deliverable": plan,
            "authority_used": list(self.role.authority),
        }


@register(87, 344)
class AgentEngineerAgent(BaseAgent):
    """Builds AI agents."""
    def execute(self, task: Task) -> dict:
        requirement = task.inputs.get("requirement", task.goal)
        design = self.call_llm(
            f"Requirement: {requirement}\n"
            "Return: agent spec, tools needed, approval policy, evals."
        )
        return {"seat": self.role.id, "agent_spec": design}


@register(348)
class AIEvaluationAgent(BaseAgent):
    """Scores other agents."""
    def execute(self, task: Task) -> dict:
        target_role = task.inputs["target_role"]
        samples = task.inputs.get("samples", [])
        scores = [
            {"input": s, "score": self._score(s), "pass": self._score(s) > 0.7}
            for s in samples
        ]
        pass_rate = (sum(s["pass"] for s in scores) / len(scores)) if scores else 0
        return {
            "seat": self.role.id,
            "target_role": target_role,
            "pass_rate": pass_rate,
            "regression": pass_rate < 0.9,
            "details": scores,
        }

    def _score(self, sample: Any) -> float:
        try:
            return float(str(sample)[0])
        except (ValueError, IndexError):
            return 0.5


@dataclass
class Event:
    kind: str
    role_number: int
    task_id: str
    detail: dict = field(default_factory=dict)


class Runtime:
    """Holds agents, tools, and the audit log."""

    def __init__(self, llm: LLM, tools: Optional[dict[str, ToolSpec]] = None):
        self.llm = llm
        self.tools = tools or {}
        self._agents: dict[int, BaseAgent] = {}
        self.events: list[Event] = []

    def agent_for(self, role_number: int) -> BaseAgent:
        if role_number in self._agents:
            return self._agents[role_number]
        role_obj = ROLES[role_number]
        cls = AGENT_CLASSES.get(role_number, GenericRoleAgent)
        agent = cls(role_obj, self.llm, self.tools)
        self._agents[role_number] = agent
        return agent

    def dispatch(self, task: Task, role_number: int) -> AgentResult:
        agent = self.agent_for(role_number)
        self.events.append(Event("dispatch", role_number, task.id,
                                 {"goal": task.goal}))
        result = agent.run(task)
        self.events.append(Event("result", role_number, task.id,
                                 {"ok": result.ok, "approval": result.requires_approval}))
        return result

    def run_chain(self, task: Task, start_role: int,
                  max_hops: int = 12) -> list[AgentResult]:
        """Follow handoffs until a human gate or failure."""
        trail: list[AgentResult] = []
        current, hops = start_role, 0
        while current is not None and hops < max_hops:
            res = self.dispatch(task, current)
            trail.append(res)
            if res.requires_approval or not res.ok:
                break
            current = res.handoff_to
            hops += 1
        return trail


# ---- COMPANY MODEL ----

@dataclass
class Person:
    name: str
    kind: str = "human"


@dataclass
class SeatOccupant:
    seat: int
    occupant: Person | str
    kind: str


class Company:
    """COMPANY -> DEPARTMENTS -> TEAMS -> ROLES -> (PERSON | AGENT)"""

    def __init__(self, name: str, runtime: Runtime):
        self.name = name
        self.runtime = runtime
        self.seats: dict[int, list[SeatOccupant]] = {n: [] for n in ROLES}

    def assign_human(self, person: Person, *role_numbers: int) -> Company:
        for n in role_numbers:
            self.seats[n].append(SeatOccupant(n, person, "human"))
        return self

    def deploy_agent(self, role_number: int, label: Optional[str] = None) -> Company:
        role_obj = ROLES[role_number]
        if not role_obj.ai_capable:
            raise PermissionError(
                f"{role_obj.id} {role_obj.name} is a human-only seat"
            )
        label = label or f"agent:{role_obj.id}"
        self.seats[role_number].append(
            SeatOccupant(role_number, label, "agent")
        )
        return self

    def deploy_agents(self, *role_numbers: int) -> Company:
        for n in role_numbers:
            self.deploy_agent(n)
        return self

    def coverage(self) -> dict:
        total = len(ROLES)
        filled = sum(1 for occ in self.seats.values() if occ)
        by_agent = sum(1 for occ in self.seats.values()
                       if any(o.kind == "agent" for o in occ))
        return {
            "total_seats": total,
            "filled": filled,
            "agent_occupied": by_agent,
            "vacant": total - filled,
        }


# ---- DEMO ----

class MockLLM:
    def complete(self, system: str, user: str, **kw) -> str:
        return f"[Completed] {user.strip()[:80]}"


if __name__ == "__main__":
    rt = Runtime(llm=MockLLM())
    acme = Company("Acme Corp", rt)
    acme.assign_human(Person("Antwuan"), 1)
    acme.deploy_agents(87, 348, 165, 164)
    print("Coverage:", acme.coverage())

    task = Task(goal="Evaluate agent performance", inputs={"target_role": 165})
    result = rt.dispatch(task, 348)
    print(f"\nResult: {result.ok}, Approval required: {result.requires_approval}")
