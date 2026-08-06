---
name: AGENT_PERMISSIONS
title: Agent Permissions & Authorization
desc: ...
version: 1.0
date: 2026-07-30
companion: [[AGENT-BRACKET-STANDARD.md]], [[SECURITY.md]]
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Agent Permissions & Authorization

**Purpose**: Define what each agent can/cannot do. Enable secure multi-agent orchestration with least-privilege access.

---

## Permission Bracket

```yaml
[PERMISSION]
AGENT: BuildAgent
ACTION: Deploy to production
GRANTED: YES
SCOPE:
  - Can: Deploy main branch
  - Cannot: Delete databases
  - Cannot: Access secrets directly
EXPIRES: 2026-08-30
GRANTED_BY: CTO Agent
```

---

## Authorization Levels

```
LEVEL_0: READ_ONLY (query only)
LEVEL_1: RECOMMEND (suggest actions)
LEVEL_2: EXECUTE_APPROVED (run pre-approved workflows)
LEVEL_3: EXECUTE_LIMITED (autonomous within guardrails)
LEVEL_4: AUTONOMOUS (self-directed)
LEVEL_5: STRATEGIC (business decisions)
```

---

## Storage

Neo4j + Supabase (agent_permissions table):
```
Agent A -[GRANTED_PERMISSION_TO]-> Resource B
  scope: {can: [...], cannot: [...]}
  expiry: 2026-08-30
```

---

## Version History
- **v1.0 (2026-07-30)**: Agent permissions model.
