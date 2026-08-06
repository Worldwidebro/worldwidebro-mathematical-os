---
name: AGENT-BRACKET-STANDARD
title: Agent Bracket Standard (Agent Command Protocol)
desc: ...
version: 1.0
date: 2026-07-30
owner: Hermes Agent
applies: All agents in ecosystem (Hermes, BuildAgent, SalesAgent, etc.)
companion: [[TAGGING-STANDARD.md]] (venture command protocol)
related: [[AGENT_ONTOLOGY.md]], [[AGENT_PROTOCOL.md]], [[AGENT_SPEC.md]]
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Agent Bracket Standard (Agent Command Protocol)

**Purpose**: Define standardized bracket vocabulary for agent commands, directives, and state management. Enables Hermes and sub-agents to parse commands consistently, maintain state, and coordinate work across 712 ventures.

**Parallel to**: [[TAGGING-STANDARD.md]] but for agents instead of ventures. Creates enterprise-wide **synergy** through standardized command language.

---

## Synergy: How Agent Brackets Enable Value Creation

### Cross-Agent Coordination
```
Sales Agent (finds lead)
  → [[MESSAGE]] to Finance Agent
    [FROM] Sales Agent [TO] Finance Agent
    [PAYLOAD] {loan_request}
    ↓ Finance evaluates (using [[DECISION]] brackets)
    → [RESPONSE] Approved/Denied
      ↓ Sales Agent updates [[STATE]]
        → Finance Agent receives acknowledgment [[MESSAGE]]
```

**Synergy Created**: Sales + Finance cooperation = qualified leads → financing → revenue

### Memory Sharing Between Agents
```
BuildAgent learns via [[MEMORY]]:
  "Deploy to staging first → 5% fewer production errors"
  
Later: SalesAgent queries BuildAgent's [[MEMORY]]
  "Should we expedite launch?"
  
BuildAgent recommends: "LEVEL_2 approval required" (from [[MEMORY]])
```

**Synergy**: Knowledge learned by one agent improves decisions for another

### Capability Synergy (via Neo4j)
```
All agents report [[STATE]] + [[EVALUATION]] metrics to Neo4j
  Agent A IMPROVES Capability X
  Agent B DEPENDS_ON Capability X
  → Neo4j query: "What agents can help with Capability X?"
  → Hermes orchestrates collaboration
```

---

## Agent Identity Brackets

Define the agent itself:

```
[AGENT] Hermes
[AGENT_ID] AGENT-001
[AGENT_TYPE] ORCHESTRATOR_AGENT
[AGENT_ROLE] Venture Operations Orchestrator
[AGENT_VERSION] 2.1.0
[AGENT_OWNER] Worldwidebro Holdings
[AGENT_STATUS] ACTIVE
[AGENT_SCOPE] All Ventures (712)
```

### Required Fields
- `[AGENT]` — Agent name (e.g., Hermes, BuildAgent, SalesAgent)
- `[AGENT_TYPE]` — Category ([[AGENT_ONTOLOGY.md]] lists 13 types)
- `[AGENT_ROLE]` — What the agent does (see [[AGENT_SPEC.md]])
- `[AGENT_SCOPE]` — What it operates on (venture ID, sector, or "All Ventures")

### Agent Types
EXECUTIVE | MANAGER | WORKER | RESEARCH | ANALYST | ENGINEERING | SALES | MARKETING | FINANCE | LEGAL | OPERATIONS | SECURITY | DATA

See [[AGENT_ONTOLOGY.md]] for full definitions and Neo4j relationships.

---

## Agent Autonomy Levels

Critical for controlling risk (maps to [[AGENT_PERMISSIONS.md]]):

```
[AUTONOMY_LEVEL] LEVEL_2

LEVEL_0 = Observe (read-only, report findings)
LEVEL_1 = Recommend (suggest actions, human decides)
LEVEL_2 = Execute Approved (run pre-approved workflows)
LEVEL_3 = Execute Limited (autonomous within guardrails)
LEVEL_4 = Autonomous (self-directed execution)
LEVEL_5 = Strategic (make business decisions)
```

**Examples**:
- Hermes: LEVEL_3 (autonomous within [[vex-api]] contracts)
- CFO Agent: LEVEL_2 (must approve large transactions)
- BuildAgent: LEVEL_3 (run builds, wait for manual deploy approval)
- SecurityAgent: LEVEL_2 (flag issues, wait for approval to remediate)

See [[AGENT_PERMISSIONS.md]] for authorization model.

---

## Task Execution Format

Standard task envelope (maps to [[AGENT_SPEC.md]] input/output schema):

```
[AGENT] Engineering Agent

[TASK] Deploy Website

[VENTURE] CON-001

[OBJECTIVE] Get production URL live

[INPUTS]
  - Repository: worldwidebro/con-ventures
  - Build command: npm run build
  - Deploy target: Vercel production

[ACTIONS]
  - Build application
  - Run tests
  - Deploy to Vercel
  - Verify health checks

[OUTPUTS]
  - Deployment report (success/failure)
  - Production URL
  - Health check results
  - Rollback commands (if needed)

[TIMELINE] 2 hours

[APPROVALS_REQUIRED] CTO Agent

[STATUS] IN_PROGRESS
```

Status values: PENDING → IN_PROGRESS → BLOCKED → TESTING → READY → DEPLOYED → FAILED

See [[AGENT_LIFECYCLE.md]] for full state machine.

---

## Agent Planning Brackets

Multi-step reasoning (stores in Neo4j, enables [[AGENT_MEMORY.md]] PROCEDURAL memory):

```
[PLAN]

[GOAL] Launch LT-005 logistics platform

[STEPS]
  1. Audit infrastructure (Network Agent)
  2. Build dispatch workflow (Engineering Agent)
  3. Connect payments (Finance Agent)
  4. Load test (QA Agent)
  5. Deploy (DevOps Agent)
  6. Go live (Operations Agent)

[DEPENDENCIES]
  - Step 2 blocks Step 3
  - Step 4 blocks Step 5

[RISKS]
  - Database migration could cause downtime
  - Payment integration may need Stripe review

[TIMELINE] 2 weeks

[OWNER] Operations Agent
```

Dependencies enable workflow orchestration (see [[AGENT_ONTOLOGY.md]] ORCHESTRATES relationship).

---

## Agent Memory Brackets

Persistent intelligence storage (mapped in [[AGENT_MEMORY.md]]):

```
[MEMORY]

[AGENT] Hermes

[MEMORY_TYPE] EPISODIC
  - Last action: Routed CON-001 to FIN-042
  - Timestamp: 2026-07-30T14:32:00Z
  - Result: Success (lead converted)
  - Stored in: Supabase + Redis

[MEMORY_TYPE] SEMANTIC
  - CON-001 specializes in: Construction project management
  - CON-001 partnerships: LT-012 (logistics), FIN-042 (financing), RE-001 (real estate)
  - Success pattern: Construction leads → Finance pre-qualification → 60% conversion
  - Stored in: Neo4j graph

[MEMORY_TYPE] PROCEDURAL
  - How to route lead: Check lead amount → Check credit score → Check industry → Route
  - How to validate CRM sync: POST to webhook → verify in database → log result
  - Stored in: Codebase + playbook docs

[MEMORY_TYPE] REFLECTIVE
  - Learned: Referral revenue depends on credit score gate (not just lead volume)
  - Improved: Added credit check step to routing logic
  - Confidence increase: 85% → 95% success rate
  - Stored in: [[AGENT_EVALUATION.md]] improvement log
```

Memory types enable synergies across agent teams (see [[AGENT_MEMORY.md]] for full architecture).

---

## Agent State Brackets

Current status snapshot (syncs to Neo4j, enables [[AGENT_ONTOLOGY.md]] HAS_STATE relationship):

```
[STATE]

[AGENT] BuildAgent

[ACTIVE_TASK] Deploy CON-001

[CURRENT_GOAL] Get production URL live

[PROGRESS] 60% (build + test done, deploy pending)

[BLOCKERS]
  - Waiting for: CTO Agent approval
  - SLA: 30 min approval window
  - Escalate if: Exceeded 1 hour

[LAST_ACTION] Ran test suite, all passed (2 min ago)

[NEXT_ACTION] Request CTO approval for deploy

[HEALTH] HEALTHY (no errors)

[DECISIONS_PENDING]
  - Should deploy to staging first? (recommendation: YES)
```

---

## Agent Decision Brackets

Structured decision-making (creates Neo4j [[AGENT_ONTOLOGY.md]] DECIDES relationship):

```
[DECISION]

[QUESTION] Should we launch CON-001?

[EVIDENCE]
  - Tests: ✅ All passing
  - Revenue pipeline: ✅ 50 qualified leads
  - Compliance: ✅ Legal approved terms
  - Infrastructure: ✅ Production ready
  - Team: ✅ Support on standby

[CRITERIA]
  1. All tests pass (from [[CI_CD.md]] standard)
  2. Revenue pipeline exists (from [[CAPABILITY_MAP.md]])
  3. No security issues (from [[SECURITY.md]])
  4. Stakeholder sign-off

[CONFIDENCE] HIGH (95%)

[RECOMMENDATION] LAUNCH

[APPROVALS_REQUIRED]
  - CEO Agent: APPROVED
  - CTO Agent: APPROVED
  - Finance Agent: APPROVED

[STATUS] APPROVED

[LOGGED_TO] Neo4j as DECISION node (audit trail in [[AGENT_ONTOLOGY.md]])
```

---

## Agent Communication Brackets

Multi-agent messaging (implements [[AGENT_PROTOCOL.md]]):

```
[MESSAGE]

[FROM] Sales Agent
[TO] Finance Agent

[TYPE] REQUEST

[SUBJECT] Evaluate financing for qualified lead

[PAYLOAD]
  {
    "lead_id": "L-12345",
    "customer": "ABC Corp",
    "loan_amount_usd": 50000,
    "project_type": "commercial_construction"
  }

[EXPECTED_RESPONSE] Financing recommendation (approve/deny/need_docs)

[DEADLINE] 4 hours

[PRIORITY] P1 (urgent)

[ACKNOWLEDGED] ✅ Yes
[ACKNOWLEDGED_AT] 2026-07-30T14:33:00Z

[RESPONSE_STATUS] PENDING
```

Creates synergy: Sales finds lead → Finance evaluates → Partnership revenue (see [[VENTURE-ECOSYSTEM-VOCABULARY.md]] REFERS_CLIENTS relationship).

---

## Agent Permission Brackets

Authorization & governance (detailed in [[AGENT_PERMISSIONS.md]]):

```
[PERMISSION]

[AGENT] BuildAgent

[ACTION] Deploy to production

[RESOURCE] CON-001 Vercel project

[GRANTED] YES

[GRANTED_BY] CTO Agent

[EXPIRES] 2026-08-30

[SCOPE]
  - Can: Deploy main branch only
  - Cannot: Deploy feature branches
  - Cannot: Delete databases
  - Cannot: Access production secrets directly (see [[SECURITY.md]])

[AUDIT_TRAIL]
  - Granted: 2026-07-30 by CTO
  - Last used: 2026-07-30 14:32 (successful deploy)
  - Revoked if: No use for 30 days

[STATUS] ACTIVE
```

---

## Agent Tool Use Brackets

Track tool execution (logged in [[AGENT_ECONOMICS.md]]):

```
[TOOL_CALL]

[AGENT] Engineering Agent

[TOOL] GitHub

[ACTION] Create Repository

[INPUTS]
  - repo_name: con-001-ace-construction
  - visibility: private
  - template: venture-template (from [[REPOSITORY_STANDARD.md]])

[RESULT] SUCCESS

[OUTPUT]
  - Repository URL: github.com/worldwidebro/con-ventures/con-001-ace-construction
  - Clone command: git clone https://...
  - Next: Push initial commit

[ERROR_COUNT] 0

[EXECUTION_TIME] 2.1 seconds

[COST_USD] 0.00

[ANALYTICS] 
  - Stored in: Redis cache + Supabase logs_telemetry
  - Feeds: [[AGENT_EVALUATION.md]] performance tracking
```

---

## Agent Evaluation Brackets

Performance measurement (detailed in [[AGENT_EVALUATION.md]]):

```
[EVALUATION]

[AGENT] Hermes

[METRIC] Success Rate

[TARGET] 95% (from [[AGENT_SPEC.md]] SLA)

[ACTUAL] 95.2%

[PERIOD] Last 7 days (1,204 routing decisions)

[BREAKDOWN]
  - Referral routing: 98% success (400 decisions)
  - Capability matching: 93% success (300 decisions)
  - Workflow orchestration: 92% success (504 decisions)

[IMPROVEMENTS]
  - Added credit score gate → +3% referral success
  - Improved capability scoring → +2% accuracy

[CONFIDENCE] HIGH

[STATUS] EXCEEDING_TARGET

[NEXT_IMPROVEMENT] Test multi-venture routing (targeting 97% by 2026-08-15)
```

---

## Agent Economics Brackets

Cost tracking & ROI (detailed in [[AGENT_ECONOMICS.md]]):

```
[ECONOMICS]

[AGENT] Marketing Agent

[PERIOD] July 2026

[COSTS]
  - API calls: 50,000 × $0.001 = $50 (tracked in Supabase)
  - Compute: 80 hours × $0.10/hour = $8
  - Total: $58

[REVENUE_GENERATED] $4,500 (via leads → conversions)

[ROI] 7,655% (revenue / cost)

[EFFICIENCY]
  - Cost per lead: $0.12
  - Revenue per lead: $90
  - Margin per lead: $89.88

[BUDGET] $500/month (from [[AGENT_SPEC.md]] cost limits)

[BUDGET_USED] $58 (11.6%)

[STATUS] EFFICIENT (well under budget, high ROI)

[RECOMMENDATION] Scale agent → increase budget to $1,000/month
```

Enables portfolio optimization (see [[VENTURE-ECOSYSTEM-VOCABULARY.md]] ALLOCATES_CAPITAL_TO).

---

## Agent Hierarchy Brackets

Multi-agent orchestration (Neo4j [[AGENT_ONTOLOGY.md]] SUPERVISES relationship):

```
[HIERARCHY]

[SUPERVISOR] CEO Agent (LEVEL_5)
  ├─ Delegates to: CTO Agent (LEVEL_3)
  │   ├─ Delegates to: BuildAgent (LEVEL_3)
  │   ├─ Delegates to: SecurityAgent (LEVEL_2)
  │   └─ Delegates to: DeployAgent (LEVEL_2)
  │
  ├─ Delegates to: CFO Agent (LEVEL_2)
  │   ├─ Delegates to: FinanceAgent (LEVEL_2)
  │   └─ Delegates to: AuditAgent (LEVEL_1)
  │
  └─ Delegates to: Operations Agent (LEVEL_3)
      ├─ Delegates to: SalesAgent (LEVEL_3)
      └─ Delegates to: MarketingAgent (LEVEL_3)

[ESCALATION_PATH]
  If BlockedAgent finds blocker
    → Escalate to Supervisor Agent
    → Supervisor evaluates options
    → Supervisor delegates to appropriate agent
    → If unsolved after 1 hour
      → Escalate to CEO Agent
      → CEO decides autonomously (LEVEL_5)
```

Enables synergy: Agents can route to best-fit partner without asking (via [[AGENT_MEMORY.md]] learned patterns).

---

## Complete Agent Command Example

Full directive with all brackets (integrated with venture system):

```
[AGENT] Hermes

[AGENT_TYPE] ORCHESTRATOR_AGENT

[AUTONOMY_LEVEL] LEVEL_3

[VENTURE] CON-001

[TASK] Connect CON-001 to Finance Referral Pipeline

[OBJECTIVE] Enable 10% revenue share from qualified finance referrals

[PLAN]
  STEP 1: Audit CON-001 data quality
  STEP 2: Verify FIN-042 capability exists
  STEP 3: Create referral partnership contract
  STEP 4: Wire Webhook + API connection (via [[vex-api]])
  STEP 5: Test end-to-end pipeline
  STEP 6: Deploy to production

[TIMELINE] 4 hours

[APPROVALS_REQUIRED]
  - CON-001 owner
  - FIN-042 owner

[TOOLS]
  - GitHub (clone templates from [[REPOSITORY_STANDARD.md]])
  - vex-api (register referral from [[API_STANDARDS.md]])
  - Supabase (test webhook from [[DATA_MODEL.md]])
  - Neo4j (update relationship graph from [[AGENT_ONTOLOGY.md]])

[OUTPUTS]
  - Referral partnership contract (signed)
  - Webhook endpoint (verified via [[OBSERVABILITY.md]])
  - Revenue share structure (documented)
  - Neo4j relationship created (REFERS_CLIENTS from [[VENTURE-ECOSYSTEM-VOCABULARY.md]])
  - Success metrics dashboard (real-time tracking)

[MONITORING]
  - Referrals/week (tracked in [[AGENT_EVALUATION.md]])
  - Revenue/week (tracked in [[AGENT_ECONOMICS.md]])
  - Conversion rate (KPI from [[AGENT_SPEC.md]])
  - System health (from [[CI_CD.md]] health checks)

[STATUS] IN_PROGRESS

[ESCALATION]
  If blocked > 1 hour: Escalate to CEO Agent
  If high-risk decision: Get human approval

[AUDIT_LOG]
  - Started: 2026-07-30T14:00:00Z
  - By: System (Hermes)
  - Expected completion: 2026-07-30T18:00:00Z
  - Logged to: Supabase audit_log + Neo4j decision trail
```

**Synergy Summary**: This single directive coordinates:
- Sales Agent (finds lead)
- Finance Agent (evaluates)
- Engineering Agent (wires API)
- Operations Agent (monitors)
- CEO Agent (approves)
= Revenue partnership activated for all 712 ventures to learn from

---

## Version History
- **v1.0 (2026-07-30)**: Agent bracket standard with 14 bracket categories (identity, autonomy, task, planning, memory, state, decision, communication, permission, tool, evaluation, economics, hierarchy, audit). Integrated with [[TAGGING-STANDARD.md]], [[VENTURE-ECOSYSTEM-VOCABULARY.md]], and 25-document architecture.
