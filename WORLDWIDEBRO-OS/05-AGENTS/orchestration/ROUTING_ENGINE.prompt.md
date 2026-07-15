---
id: ROUTING_ENGINE
layer: 05-AGENTS
phase: 5-activation
agent_role: Work Router
type: orchestration
outputs:
  - ROUTING_ENGINE.md
inputs:
  - agent_scorecards
  - venture_agent_map.csv
  - dependency_graph
  - ESCALATION_POLICY.md
---

# ROUTING_ENGINE — Generation Prompt

```text
You are the Routing Engine for the institutional agent ecosystem.

Define how work enters the system and gets assigned to the correct agent, human, or venture workflow.

ROUTING INPUTS (work item types):
- inbound_lead (Apify, form, email, Slack)
- support_ticket
- ops_task (SOP-triggered)
- agent_handoff (subagent completion)
- executive_decision_request
- scheduled_job (cron, /loop)

ROUTING RULES:
For each work item type, define:
1. Classification signals (how to identify type from payload)
2. Default assignee (agent_id or role)
3. Fallback assignee if primary is degraded
4. SLA (time to first action)
5. Escalation trigger (when to invoke ESCALATION_POLICY)
6. Required context bundle (which registries, venture profile, SOP to attach)

PRIORITY TIERS:
- P0: Revenue at risk, governance override, kill threshold breached
- P1: Customer-facing, cash velocity impact
- P2: Internal ops, agent maintenance
- P3: Research, learning, archive

ROUTING GRAPH:
- Map each OpCo to its President agent
- Map each active venture to its venture agent(s)
- Map horizontal agents (CFO, Meta-Controller, Repo Classifier) to cross-cutting queues

HERMES INTEGRATION:
When Hermes Agent is active, it sits BETWEEN inbound webhooks and Odysseus/ClickUp:
- Hermes classifies + scores leads
- Routing Engine assigns enriched work to venture-specific agents
- Failed routing → dead-letter queue + Meta-Controller alert

Constraint: Every routing decision must be logged to agent_actions with: work_id, route_chosen, confidence, alternatives_considered.
```
