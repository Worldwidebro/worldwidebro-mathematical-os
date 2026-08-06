---
name: AGENT_PROTOCOL
title: Agent Communication Protocol
desc: ...
version: 1.0
date: 2026-07-30
companion: [[AGENT-BRACKET-STANDARD.md]], [[AGENT_SPEC.md]]
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Agent Communication Protocol

**Purpose**: How agents send messages, delegate tasks, request approvals, and coordinate workflows.

---

## Message Format

```yaml
[MESSAGE]
FROM: Sales Agent
TO: Finance Agent
TYPE: REQUEST
SUBJECT: Evaluate financing
PAYLOAD: {lead_id, loan_amount}
EXPECTED_RESPONSE: Financing recommendation
DEADLINE: 4 hours
PRIORITY: P1
ACKNOWLEDGED: YES
```

---

## Handoff Workflow

1. Agent A delegates to Agent B
2. Agent B acknowledges (< 1 sec)
3. Agent B executes
4. Agent B returns result
5. Agent A records outcome in memory

---

## Storage

- Event Bus: Webhooks
- State Sync: Redis (2 sec heartbeat)
- Graph: Neo4j COMMUNICATES_WITH edges
- Audit: Supabase message_log

---

## Version History
- **v1.0 (2026-07-30)**: Agent communication protocol.
