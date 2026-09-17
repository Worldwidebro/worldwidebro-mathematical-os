---
title: Tool Gateway & Permissions Framework
id: TOOL-GATEWAY-PERMS
phase: Phase 2 (Local Autonomy)
updated: 2026-09-17
---

# Tool Gateway & Permissions Framework

**Goal:** Every agent action goes through permission check before execution.

## Tool Categories

### READ Tools (no approval needed)
- search files, query database, inspect git, read CRM
- Agent permission: any authenticated agent

### WRITE Tools (agent approval in registry)
- create lead, send email, create task, update CRM
- Agent permission: explicit grant required

### HIGH-RISK Tools (human approval required)
- transfer money, delete data, sign contract, publish, modify prod
- Agent permission: escalate to human, wait for approval

## Tool Registry Entry Format

```yaml
tool_id: send_email
risk_level: write
required_permissions:
  - email_access
  - domain_verified
approval_required: false
audit_log: true
rate_limit: 100/hour
```

## Flow

```
Agent requests action
  ↓
Tool Gateway checks:
  - Agent has permission?
  - Tool risk level?
  - Rate limit reached?
  ↓
Approve/Deny/Escalate
  ↓
If Escalate: notify human via dashboard
  ↓
Resume when human approves
```

## Integration

Wire to:
- OmniRoute (MCP gateway)
- Agent Registry (permissions field)
- Dashboard (approval notifications)

