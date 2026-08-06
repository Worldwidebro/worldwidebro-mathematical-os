---
name: docs/agentic-systems/10-SECURITY-GOVERNANCE/AGENT-SECURITY
desc: ...
tags:
  - status/active
  - knowledge/current
id: agent-security
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
aliases:
  - "Agent Guardrails"
  - "Least Privilege Sandbox"
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/10-SECURITY-GOVERNANCE/AGENT-SECURITY
## Purpose
Establish security guidelines for autonomous agents, focusing on data protection, injection prevention, and boundary sandboxing.

## Core Concept
Agents executing commands require tight security boundaries. A compromised agent can execute destructive commands, exfiltrate credentials, or delete databases.

## Technical Details
1. **Least Privilege**: Grant the narrowest system permissions required for the task.
2. **Execution Sandboxing**: Run execution code inside isolated virtual runtimes (e.g., Docker or sandboxed shell sessions) with no host network access unless whitelisted.
3. **Input Sanitization**: Block prompt injection and tool-argument poisoning by validating arguments against JSON schemas before execution.

## Relations
- Restricts [[08-EXECUTION-AUTOMATION/AGENT-ACTION.md]]
