# Agent-to-Agent (A2A) Communication Protocol

This document defines the interface and payload specifications for communications between autonomous agents in the **AI-BOSS-OS** network layer.

## 1. Interaction Patterns

Agents interact using a asynchronous, message-based protocol modeled after Actor model patterns:

- **Request-Response (Query)**: A sender agent blocks (or yields context) awaiting a reply from a target agent.
- **Fire-and-Forget (Command)**: An agent dispatches a task notice to another agent and continues its execution loop without blocking.
- **Publish-Subscribe (Events)**: Agents publish system state notifications (e.g., `venture_created`, `audit_failed`) to shared event channels.

---

## 2. Message Payload Schema

All A2A payloads are serialized in standard JSON format containing tracing, envelope, and body metadata:

```json
{
  "message_id": "msg-8f99-e9edab3e75e6",
  "correlation_id": "corr-a53aafdf-8842-490a",
  "sender": {
    "agent_id": "CTO",
    "conversation_id": "a53aafdf-8842-490a-8f99-e9edab3e75e6"
  },
  "recipient": {
    "agent_id": "CFO",
    "conversation_id": "b64bbfef-9953-500b-9f00-f9febc3f86f7"
  },
  "timestamp": "2026-07-21T14:52:39Z",
  "priority": "HIGH",
  "payload": {
    "action": "REQUEST_BUDGET_APPROVAL",
    "parameters": {
      "venture_name": "Worldwidebro-SaaS",
      "amount_usd": 15000,
      "purpose": "Database scaling setup"
    }
  }
}
```

### Protocol Fields:
- `correlation_id`: Matches requests with responses across multi-agent workflows. Used by Langfuse for tracing nested prompts.
- `priority`: Determines task queue placement. High priority messages bypass execution throttles.
- `action`: Declares the capability target requested from the receiving agent.

---

## 3. Communication Pipelines

```text
+--------------+                +--------------+
|  CTO Agent   |                |  CFO Agent   |
+------+-------+                +-------^------+
       |                                |
       | 1. POST Message                | 4. Read Message
       v                                |
+------+--------------------------------+------+
|               Shared Inbox                   |
|     (PostgreSQL database / Core Table)       |
+----------------------------------------------+
```

1. **Write Phase**: The sender agent writes the payload node to the shared SQL/PostgreSQL database `iza_os_core` in the `agent_inbox` table.
2. **Notification Phase**: The control plane signals the recipient agent via standard database triggers or process events.
3. **Read Phase**: The recipient agent wakes up, pulls the message from the queue, processes the payload using its tools, and writes back a response with the matching `correlation_id`.
