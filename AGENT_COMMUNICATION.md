---
title: Agent Communication & vex-api Integration
version: 1.0
date: 2026-07-30
companion: [[AGENT_PROTOCOL.md]], [[AGENT_ONTOLOGY.md]]
---

# Agent Communication & vex-api Integration

**Purpose**: Wire agent-to-agent messages through vex-api webhooks. Extends [[AGENT_PROTOCOL.md]] with operational routing.

---

## Message Flow

```
Agent A executes task
  ↓ logs to Neo4j + Redis
vex-api webhook fires
  ↓ routes via type
Agent B receives
  ↓ acknowledges
Audit trail (Supabase)
```

---

## vex-api Routes

**POST /agents/{agent_id}/message**
```json
{
  "from": "SalesAgent-CON-001",
  "to": "FinanceAgent-CON-001",
  "type": "REQUEST",
  "subject": "Evaluate financing",
  "payload": {"lead_id": "L-123", "amount": 50000}
}
→ 200 {acknowledged: true}
```

**GET /agents/{agent_id}/inbox**
```json
→ [{from, type, subject, timestamp}, ...]
```

---

## Storage

**Neo4j**: `(a1:Agent)-[:COMMUNICATES_WITH {message_count}]->(a2:Agent)`

**Supabase**: `agent_messages(from, to, type, payload, timestamp)`

---

## Version History

- **v1.0 (2026-07-30)**: Agent communication via vex-api webhooks.

