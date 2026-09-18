---
title: Tool Gateway & Permissions Framework
id: TOOL-GATEWAY-PERMS
phase: Phase 2 (Local Autonomy)
updated: 2026-09-17
---

[[STARTHERE]] | [[REALITY]] | [[20-DECISIONS/PHASE-2-RESEARCH-TO-REVENUE-ROADMAP]]

# Tool Gateway & Permissions Framework

**Authority:** [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml|LOGIC-055 through LOGIC-060]] (Thought/Decision layer)  
**Part of:** [[20-DECISIONS/PHASE-2-RESEARCH-TO-REVENUE-ROADMAP|Phase 2 Research-to-Revenue Engine]] → Research Agent System (Jan 2027)  
**Related:** [[_DOCS/LOGIC-ARCHITECTURE-FRAMEWORK.md|Logic Architecture Framework]] (L2/L3 autonomous execution patterns)

**Goal:** Every agent action goes through permission check before execution, enforcing [[RESPECT|20 governance rules]] and [[ANTIGRAVITY|45 operating principles]].

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

