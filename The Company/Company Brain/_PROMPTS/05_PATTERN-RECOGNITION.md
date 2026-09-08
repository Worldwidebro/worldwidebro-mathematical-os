# 05 — Pattern Recognition Prompt

[[_MEMORY/MEMORY-OS]] | [[_MEMORY/MEMORY-CONSOLIDATION]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|MASTER-PROTOCOL]]

> **Prompt Stack Tier:** 08 (Pattern Recognition)  
> **Question:** *Have we seen this pattern before?*

---

## 1. Directive

Compare the current task, error, or operational situation against historical knowledge bases:
- Previous operational incidents
- Previous project trajectories
- Previous failure modes and root causes
- Proven successful workflows and architecture patterns
- Recurring operational bottlenecks

---

## 2. Structured Output Format

When an agent detects a recurring pattern, it must emit:

```yaml
pattern_detection:
  pattern_name: "STDOUT_LOGGING_CORRUPTS_MCP_JSONRPC"
  confidence: 0.95
  previous_instances:
    - "OmniRoute driverFactory console.debug on 2026-09-05"
    - "Neo4j driver verbose logging on 2026-08-14"
  similarities:
    - "Third-party dependency writes non-JSON diagnostic messages to process.stdout"
    - "FastMCP client fails with Unexpected token JSON parse error"
  differences:
    - "Target language was Node.js ESM in instance 1, Python in instance 2"
  recommended_response:
    - "Intercept process.stdout and filter non-JSON lines or redirect to process.stderr"
    - "Wrap entrypoint in dedicated adapter script before registering with MCP client"
```
