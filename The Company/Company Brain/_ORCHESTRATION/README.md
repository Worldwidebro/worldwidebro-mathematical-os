# _ORCHESTRATION — Central Workflow & Agent Orchestration

[[STARTHERE]] | [[REALITY]] | [[ANTIGRAVITY]] | [[19-ORCHESTRATION]] | [[16-AGENTS]]

**Control Point:** CP-033 (Execution)  
**Purpose:** Agent dispatch, workflow routing, multi-agent coordination, tool invocation

**Key systems:**
- [[16-AGENTS/README|Agent Registry]] — All deployed agents
- [[_MCP/README|MCP Tools]] — Tool catalog for agents
- [[19-ORCHESTRATION/README|Orchestration Domain]] — Workflow definitions
- [[_INFRASTRUCTURE/omniroute/README|OmniRoute]] — Intelligent routing engine
- [[HARNESS-ENGINEERING/README|Agent Harness]] — Execution + evaluation

**How this works:**
1. Task arrives (user, webhook, schedule)
2. [[ANTIGRAVITY|Rule 44]] (9-step protocol) invoked
3. Agent dispatched via [[_INFRASTRUCTURE/omniroute/README|OmniRoute]]
4. Tool execution + telemetry
5. Verification + reporting

**See:** [[STARTHERE]] (Agent execution model)
