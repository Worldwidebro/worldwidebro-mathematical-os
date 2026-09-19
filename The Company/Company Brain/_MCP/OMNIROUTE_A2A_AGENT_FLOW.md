# OmniRoute A2A Agent Integration Flow

**Phase:** Week 2 Task 2.1 Integration Pattern  
**Agent:** Lead Qualifier (test case)  
**Authority:** CP-012 (Agent Control Plane), CP-027 (Engineering)  
**Updated:** 2026-09-19

---

## End-to-End Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│ USER TASK INPUT                                                           │
│ "Score these 5 leads: [data]"                                            │
└────────────────────┬────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ OmniRoute /a2a (JSON-RPC 2.0 POST)                                      │
│ {                                                                         │
│   "jsonrpc": "2.0",                                                      │
│   "method": "message/send",                                              │
│   "params": {                                                            │
│     "skill": "lead-qualifier",                                           │
│     "messages": [{"role": "user", "content": "..."}],                   │
│     "metadata": {"model": "auto"}                                        │
│   }                                                                       │
│ }                                                                         │
└────────────────────┬────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ OmniRoute Smart Routing Skill                                            │
│ • Query AGENT_REGISTRY for "lead-qualifier" agent                        │
│ • Verify skills match: ["lead-scoring", "qualification"]                 │
│ • Check autonomy gate: L2 (human review for high-cost) ✅                │
│ • Validate tool permissions: [hubspot, supabase] ✅                      │
└────────────────────┬────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Lead Qualifier Agent Execution                                           │
│ • Receives: lead data, scoring context                                   │
│ • Processes: BANT framework (Budget, Authority, Need, Timeline)         │
│ • Outputs: JSON {leads: [{id, score, fit, recommendation}]}             │
│ • Cost: $0.15 per invocation                                            │
└────────────────────┬────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ OmniRoute Response (JSON-RPC)                                            │
│ {                                                                         │
│   "jsonrpc": "2.0",                                                      │
│   "result": {                                                            │
│     "task": {"id": "uuid", "state": "completed"},                        │
│     "artifacts": [{                                                      │
│       "type": "text",                                                    │
│       "content": "{\"scores\": [...]}"                                   │
│     }],                                                                  │
│     "metadata": {                                                        │
│       "cost_envelope": {                                                 │
│         "estimated": 0.15,                                               │
│         "actual": 0.14,                                                  │
│         "currency": "USD"                                                │
│       },                                                                 │
│       "policy_verdict": {                                                │
│         "allowed": true,                                                 │
│         "reason": "within autonomy budget"                               │
│       },                                                                 │
│       "routing_explanation": "Selected lead-qualifier (trust: 0.94, "   │
│                              "success: 92%, cost: $0.15)"                │
│     }                                                                    │
│   }                                                                       │
│ }                                                                         │
└────────────────────┬────────────────────────────────────────────────────┘
                     │
                     ├─────────────────────────────────┐
                     │                                 │
                     ▼                                 ▼
    ┌──────────────────────────────┐   ┌──────────────────────────────┐
    │ COST ENVELOPE BRIDGE          │   │ TASK EXECUTION LOGGER        │
    │                               │   │                              │
    │ Extract: cost_envelope        │   │ Log to task_executions table:│
    │ • estimated: 0.15             │   │ • task_id                    │
    │ • actual: 0.14                │   │ • agent_id (lead-qualifier)  │
    │ • currency: USD               │   │ • cost_actual: 0.14          │
    │                               │   │ • revenue_projected: 2500    │
    │ Calculate ROI:                │   │ • roi: 178.6x                │
    │ ROI = 2500 / 0.14 = 17857x    │   │ • status: completed          │
    │                               │   │ • metadata: {...}            │
    │ Insert to Supabase:           │   │                              │
    │ task_executions table ✅      │   └──────────────────────────────┘
    └──────────────────────────────┘

                     ▼

    ┌──────────────────────────────────────────────────┐
    │ DASHBOARD VISIBILITY                             │
    │                                                  │
    │ Agent: Lead Qualifier                           │
    │ ├─ Cost: $0.14 actual                           │
    │ ├─ Revenue Projected: $2,500                    │
    │ ├─ ROI: 17,857x                                 │
    │ ├─ Success Rate: 92%                            │
    │ └─ Tasks Completed: 1                           │
    └──────────────────────────────────────────────────┘

                     ▼

    ┌──────────────────────────────────────────────────┐
    │ DEAL CLOSURE (Later)                             │
    │                                                  │
    │ Deal closes: $2,500 (from lead scored today)    │
    │ ▼                                                │
    │ Revenue Attribution Bridge:                      │
    │ • Lookup: Which tasks contributed to this deal? │
    │ • Attribute: 100% to Lead Qualifier             │
    │ • Record: revenue_attributions table            │
    │   - agent_id: lead-qualifier                    │
    │   - revenue_attributed: $2,500                  │
    │   - roi_actual: 17,857x (verified)              │
    └──────────────────────────────────────────────────┘
```

---

## Key Data Flows

### 1. Agent Registration
```
lead-qualifier-a2a.json
    ↓
omniroute-agent-register.ts (POST /a2a, method: skills/register)
    ↓
OmniRoute Agent Registry
    ↓
/.well-known/agent.json (agent discovery)
```

### 2. Task Routing
```
User Task → OmniRoute /a2a (skill: lead-qualifier)
    ↓
Smart Routing Skill (checks AGENT_REGISTRY)
    ↓
Lead Qualifier Agent
    ↓
policy_verdict (allowed: true, reason: ...)
    ↓
cost_envelope (actual: $0.14)
```

### 3. Cost Flow
```
cost_envelope.actual ($0.14)
    ↓
COST_ENVELOPE_BRIDGE.ts
    ↓
Supabase task_executions table
    ↓
Dashboard KPI: Total Cost = sum(cost_actual)
```

### 4. Revenue Attribution
```
Lead Qualifier scores lead
    ↓
Deal closes ($2,500)
    ↓
REVENUE_ATTRIBUTION_BRIDGE.ts
    ↓
Supabase revenue_attributions table
    ↓
Dashboard KPI: Agent ROI = sum(revenue_attributed) / sum(cost_incurred)
```

---

## Technology Stack

| Layer | Component | Protocol |
|-------|-----------|----------|
| Client | User task | JSON text input |
| Gateway | OmniRoute | JSON-RPC 2.0 over HTTP POST |
| Routing | Smart Routing Skill | OmniRoute A2A interface |
| Agent | Lead Qualifier | OmniRoute A2A skill format |
| Persistence | Supabase PostgreSQL | REST API + realtime |
| Analytics | Dashboard | SQL queries to Supabase |

---

## Success Criteria (Task 2.1)

- [x] agent.json schema valid JSON
- [x] lead-qualifier-a2a.json conforms to schema
- [x] omniroute-agent-register.ts compiles and runs
- [x] COST_ENVELOPE_BRIDGE.ts extracts cost from A2A response
- [x] REVENUE_ATTRIBUTION_BRIDGE.ts tracks deal → agent attribution
- [x] OMNIROUTE_A2A_AGENT_FLOW.md documents end-to-end flow
- [x] Tests verify registration, routing, cost logging, revenue tracking

**Next:** Task 2.2 (E2E testing with actual OmniRoute at :3000)

---

**Reference:** OmniRoute A2A docs @ https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/frameworks/A2A-SERVER.md
