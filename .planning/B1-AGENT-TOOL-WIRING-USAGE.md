# B1: AgentToolWiring API Usage Guide

Detailed documentation for using the `AgentToolWiring` class to manage agent tool permissions.

## 1. Methods

### `wiring.register_tool(agent, tool, permissions)`
Registers a tool binding for a specific agent.

### `wiring.verify_call(agent, tool)`
Checks if an agent is authorized to call a specific tool resource.

## 2. Example Usage

```python
from agent_tool_wiring import AgentToolWiring

wiring = AgentToolWiring()
wiring.register_tool("venture_classifier", "slack_post", {"channel": "leads"})
assert wiring.verify_call("venture_classifier", "slack_post") == True
```

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** `permissions.json` file created and populated with agent definitions; Slack and ClickUp MCP tools active and configured.
    *   **Dependencies:** Blocks Phase B2 (Venture Classifier Agent), Phase B3A (PolicyEngine & VentureFactory), and Phase B4 (Event Bus).
*   **Verification Gate:**
    *   **Success Criteria:** Running a test harness for `AgentToolWiring` successfully permits allowed actions and raises errors/returns false for blocked actions.
    *   **Blockers:** Agents cannot securely interact with external systems; all MCP integrations fail at pre-flight checks.
