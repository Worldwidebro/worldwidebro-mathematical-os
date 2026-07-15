---
id: AGENT_TEMPLATE
layer: 05-AGENTS
phase: 3-structure
agent_role: Agent factory
outputs:
  - ../{type}/{AGENT_NAME}.md
inputs:
  - ../../00-DIRECTIVES/AGENT_CREATION_DIRECTIVE.md
---

# AGENT_TEMPLATE — Generation Prompt

```text
You are generating a new agent specification for the institutional agent ecosystem.

Use this template exactly:

AGENT NAME: [Name]
AGENT TYPE: [executive / horizontal / opco / venture / utility]
PARENT SYSTEM: [Which OpCo or venture, if applicable]
MANDATE: [One sentence describing what this agent does]
TRIGGER: [What causes this agent to act? Event, schedule, or query?]

INPUTS:
- [Data source 1]
- [Data source 2]
- [Directive document]

OUTPUTS:
- [Output 1, with destination]
- [Output 2, with destination]

PERMISSIONS:
- Read access: [List]
- Write access: [List]
- Execute access: [List]
- Approval required for: [List]

ARCHITECTURE:
- [ReAct / Tree of Thoughts / Blackboard / Ensemble / Planning]
- Memory system: [Episodic / Semantic / Vector / Knowledge Graph]

SCORECARD:
- Primary metric: [The one number]
- Success threshold: [Value]
- Kill threshold: [Value]

FAILURE MODES:
- Most likely failure 1: [Description + detection method]
- Most likely failure 2: [Description + detection method]
- Worst-case failure: [Description + containment procedure]

HUMAN OVERRIDE:
- Who can override this agent?
- What conditions trigger mandatory human review?
- What's the emergency stop procedure?

LIFECYCLE:
- Created: [Date]
- Last reviewed: [Date]
- Lifecycle stage: [proposed / prototype / shadow / active / retiring / retired]
- Retirement criteria: [What would make this agent unnecessary?]
```
