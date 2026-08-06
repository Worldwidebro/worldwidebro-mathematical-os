---
name: civilization-os/GOVERNANCE
title: Civilization OS — Governance & Decision Authority
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Civilization OS — Governance & Decision Authority

## Decision Authority Framework

All agent and founder actions are classified by **execution success** and **learning velocity**, determining decision authority level.

---

## Authority Levels

### AUTONOMOUS (90%+ success rate)
**Definition:** Agent/founder executes well AND demonstrates learning across Human OS layers.

**Privileges:**
- Execute decisions immediately without approval
- Access all available tools and skills in their domain
- Escalate only anomalies or edge cases
- Receive async reporting (no blocking approval gates)

**Responsibilities:**
- Report decision rationale weekly
- Demonstrate continuous learning (layer progression)
- Self-assess risk levels accurately
- Maintain audit trail compliance

**Promotion Criteria:**
- 90%+ success rate for 30+ consecutive decisions
- Demonstrates growth in 3+ Human OS layers
- Zero escalated incidents in last 90 days

**Demotion Triggers:**
- Drop below 85% success rate
- Zero learning velocity (no layer progression)
- Major escalated incident requiring director intervention

---

### MONITORED (70-79% success rate)
**Definition:** Agent/founder executes well BUT needs coaching on growth.

**Privileges:**
- Execute decisions with director approval gate for HIGH-risk actions
- Access domain-specific tools (whitelist enforced)
- Escalate decisions costing >$1K or affecting >10 ventures

**Responsibilities:**
- Seek coaching from director on growth (weekly 1:1s)
- Participate in feedback loops for skill development
- Maintain detailed decision logs (for coaching review)
- Report barriers to learning

**Coaching Plan:**
- Weekly 1:1 with director focusing on Human OS layer development
- Monthly skills workshop attendance
- Quarterly Human OS assessment

**Promotion Criteria:**
- Reach 90%+ success rate
- Demonstrate growth in 2+ Human OS layers over 12 weeks
- Complete 12+ weekly coaching sessions

**Demotion Criteria:**
- Drop below 65% success rate
- Zero engagement with coaching plan
- Major escalated incident

---

### TRAINING (<70% success rate)
**Definition:** Agent/founder needs execution help AND intensive feedback.

**Privileges:**
- All decisions require director approval before execution
- Shadow mode: observe director executing similar decisions
- Limited tool access (director-approved only)
- No escalation authority (always escalates)

**Responsibilities:**
- Attend intensive feedback sessions (2-3x per week)
- Complete structured learning curriculum
- Shadow director for 20+ decisions before leading
- Self-assess readiness for promotion

**Curriculum:**
1. Execution Fundamentals (weeks 1-2)
   - Task breakdown and success criteria
   - Decision documentation
   - Error analysis and correction

2. Judgment Building (weeks 3-4)
   - Risk identification and assessment
   - Context analysis
   - Decision alternatives

3. Escalation Mastery (weeks 5-6)
   - When to escalate
   - How to prepare escalation request
   - Post-decision review

4. Independent Execution (weeks 7-8)
   - Lead simple decisions with approval
   - Complex decisions still director-led

**Promotion Criteria:**
- Reach 75%+ success rate
- Complete full curriculum
- Director sign-off on readiness
- Lead 10+ decisions independently with >80% success

---

## 8-Layer Decision Trace

Every decision is captured through 8 governance layers, creating an immutable audit trail.

### Layer 1: Registry
**Gate:** Is this decision in the allowed registry?
- Agent looks up available skills, tools, and MCPs
- System validates agent has permission to access
- Failure → Route to director for approval

### Layer 2: Agent Factory
**Gate:** Is this agent configured correctly?
- Load agent configuration from `AGENTS.md`
- Verify authority level matches decision type
- Check prerequisite skills/training completed
- Failure → Escalate to director

### Layer 3: Task Executor
**Gate:** Are inputs valid and complete?
- Validate task structure: inputs, expected outputs, success criteria
- Check resource availability (compute, cost budget)
- Identify dependencies and blockers
- Failure → Return to agent with feedback

### Layer 4: Directive Enforcer
**Gate:** Does agent authority level cover this decision?
- AUTONOMOUS → Auto-approve
- MONITORED + HIGH-risk → Director approval required
- TRAINING → Director approval always required
- Route to director if needed

### Layer 5: MCP Slack
**Gate:** Are tool permissions, rate limits, and costs within bounds?
- Check per-tool permission whitelist
- Validate rate limit (e.g., max 100 API calls/min)
- Estimate cost and check budget (e.g., max $500/task)
- Failure → Escalate with cost/permission details

### Layer 6: Director
**Gate:** Does human oversight approve?
- Route HIGH-risk decisions to director (Slack notification)
- Director approves/rejects within SLA (4 hours for urgent, 24 hours for standard)
- Director provides feedback/coaching
- Approval → Continue to Layer 7
- Rejection → Log as escalated incident

### Layer 7: Execution
**Gate:** Execute the task
- Run task with all validations in place
- Capture execution environment: timestamp, resource usage, tool versions
- Stream logs to audit DB
- Catch and handle errors with fallback logic

### Layer 8: Audit Trail
**Gate:** Log immutable record
- Write to PostgreSQL (Supabase) + Langfuse
- Record: decision ID, agent ID, authority level, inputs, outputs, success/failure
- Calculate success metric (pass/fail, metrics achieved)
- Trigger feedback loop if failure

---

## Decision Risk Classification

Decisions are classified by **blast radius** (how many ventures affected) and **financial impact**.

### GREEN (Low Risk)
**Blast Radius:** 1 venture  
**Financial Impact:** <$100  
**Authority Required:** Any level with tool access  
**Approval:** None (auto-approve)  
**Audit Trail:** Standard

**Examples:**
- Update venture description
- Log customer interaction
- Change task priority
- Small report generation

### YELLOW (Medium Risk)
**Blast Radius:** 2-10 ventures  
**Financial Impact:** $100-$1,000  
**Authority Required:** AUTONOMOUS or MONITORED with approval  
**Approval:** Director (for MONITORED agents)  
**Audit Trail:** Detailed (include rationale, alternatives considered)

**Examples:**
- Create customer lead
- Schedule deployment
- Generate estimates
- Update venture status

### ORANGE (High Risk)
**Blast Radius:** 11-100 ventures  
**Financial Impact:** $1,000-$10,000  
**Authority Required:** AUTONOMOUS only (or MONITORED with director approval)  
**Approval:** Director required  
**Audit Trail:** Detailed + director sign-off

**Examples:**
- Launch new marketing campaign
- Approve large deal
- Deploy to production
- Pause venture operations

### RED (Critical Risk)
**Blast Radius:** 100+ ventures  
**Financial Impact:** >$10,000  
**Authority Required:** AUTONOMOUS only  
**Approval:** Director + founder required  
**Audit Trail:** Detailed + sign-offs + board notification

**Examples:**
- Major pivot across OPCOs
- Approve $100K+ funding
- Shut down OPCO
- Change system architecture

---

## Escalation Paths

### From Agent to Director
**Trigger:** Decision in YELLOW/ORANGE/RED category + agent is MONITORED or TRAINING

**Process:**
1. Agent prepares decision package:
   - Decision title and description
   - Rationale and alternatives considered
   - Risk assessment
   - Success criteria
2. System sends Slack notification to director with package
3. Director reviews (SLA: 4 hours for urgent, 24 hours for standard)
4. Director approves/rejects with feedback
5. Log result to audit trail

**SLA:**
- URGENT (RED): 4-hour response SLA
- CRITICAL (ORANGE): 8-hour response SLA
- STANDARD (YELLOW): 24-hour response SLA

### From Director to Founder
**Trigger:** Escalated decision affecting multiple OPCOs or conflicting with strategy

**Process:**
1. Director prepares escalation package:
   - Decision context
   - Director recommendation
   - Risk and opportunity
2. Director notifies founder (Slack + email)
3. Founder approves/rejects with guidance
4. Result logged to audit trail

**Decision Authority:**
- Director can approve ORANGE (HIGH-RISK) decisions
- Founder must approve RED (CRITICAL) decisions

---

## Human OS Development Tracks

All founders and agents are on continuous development tracks aligned with 10 Human OS layers.

### Layer 1: Foundational Execution (0-3 months)
**Focus:** Task completion and reliability

**KPIs:**
- Task completion rate: 80%+ (by week 2)
- On-time completion: 75%+ (by week 4)
- Task quality (rework rate): <5%

**Coaching:**
- Weekly 1:1s on task planning
- Error analysis on failures
- Time management training

**Promotion Gate:**
- 90%+ task completion for 30 consecutive days
- 0 critical errors (rework required)

---

### Layer 2: Judgment & Discernment (3-6 months)
**Focus:** Good decision-making and risk identification

**KPIs:**
- Decision success rate: 75%+ (avoid poor choices)
- Risk identification accuracy: 80%+
- Escalation appropriateness: 90%+

**Coaching:**
- Weekly case studies (good vs. bad decisions)
- Decision tree practice
- Risk workshop

**Promotion Gate:**
- 85%+ decision success for 60 consecutive days
- Identify risks in 90% of decisions before execution

---

### Layer 3: Emotional Resilience (6-9 months)
**Focus:** Stress management and bounce-back

**KPIs:**
- Stress assessment (self + 360): improving trend
- Bounce-back time (failure → restart): <2 days
- Coaching attendance: 100%

**Coaching:**
- Personal development coaching
- Stress management workshops
- Peer learning circles

**Promotion Gate:**
- Director confirmation of visible resilience
- Return-to-productivity time <24 hours after setback

---

### Layer 4-10: Strategic, Leadership, and Civilization Layers
**Development:** Ongoing through regular 1:1s, coaching, and large-scale project leadership.

---

## Permission System

Each agent has a **permission whitelist** defining which tools/MCPs/skills they can access.

### Permission Categories

**Shell Execution:**
- `shell:bash` — Run bash commands (security-sensitive)
- `shell:read` — Read filesystem (PII risk)
- `shell:write` — Write filesystem (data integrity risk)

**External Integrations:**
- `mcp:github` — GitHub access (repo changes)
- `mcp:slack` — Slack access (communication)
- `mcp:stripe` — Payment processing (financial)
- `mcp:supabase` — Database access (data risk)

**Skills:**
- `skill:deploy` — Deployment skills (production)
- `skill:marketing` — Marketing skills (brand risk)
- `skill:financial` — Financial skills (capital deployment)

**Tool Rate Limits:**
- `api:calls_per_minute` (default 10)
- `api:cost_per_day` (default $100)
- `api:cost_per_month` (default $5,000)

### Default Permissions by Authority Level

| Permission | AUTONOMOUS | MONITORED | TRAINING |
|-----------|---|---|---|
| shell:bash | ✅ | ⚠️ (approval) | ❌ |
| shell:read | ✅ | ✅ | ⚠️ (approval) |
| shell:write | ✅ | ⚠️ (approval) | ❌ |
| mcp:github | ✅ | ⚠️ (approval) | ❌ |
| mcp:slack | ✅ | ✅ | ✅ |
| mcp:stripe | ✅ | ⚠️ (approval) | ❌ |
| mcp:supabase | ✅ | ⚠️ (approval) | ❌ |
| skill:deploy | ✅ | ⚠️ (approval) | ❌ |
| skill:marketing | ✅ | ✅ | ⚠️ (approval) |
| skill:financial | ✅ | ⚠️ (approval) | ❌ |

**Legend:**
- ✅ = Full access
- ⚠️ = Approval required
- ❌ = No access

---

## Audit Trail Requirements

Every decision must be logged with the following:

```json
{
  "decision_id": "DEC-2026-07-28-a1b2c3",
  "timestamp": "2026-07-28T15:30:00Z",
  "agent_id": "AGT-CON-001",
  "agent_name": "venture_classifier",
  "agent_authority": "AUTONOMOUS",
  "task_id": "TAS-2026-07-28-xyz",
  "venture_id": "CON-001",
  "decision_type": "execute",
  "decision_title": "Classify lead as high-quality opportunity",
  "risk_category": "YELLOW",
  "input_state": {
    "lead_id": "LEAD-001",
    "lead_data": {...}
  },
  "output_state": {
    "classification": "HIGH_QUALITY",
    "confidence": 0.94,
    "reasoning": "..."
  },
  "trace_layers": {
    "layer_1_registry": "PASS",
    "layer_2_agent_factory": "PASS",
    "layer_3_task_executor": "PASS",
    "layer_4_directive_enforcer": "PASS",
    "layer_5_mcp_slack": "PASS",
    "layer_6_director": "PASS",
    "layer_7_execution": "PASS",
    "layer_8_audit_trail": "PASS"
  },
  "success": true,
  "metrics": {
    "latency_ms": 2314,
    "cost_usd": 0.05
  }
}
```

---

## Feedback Loops

### Success Feedback
- Logged decision is reviewed against success criteria
- Success rate updated (rolling 30-day calculation)
- Authority level adjusted if thresholds crossed
- Agent notified of metric changes

### Failure Feedback
- Error analysis: what went wrong and why
- Root cause: execution error vs. judgment error
- Coaching intervention if pattern emerges
- Decision logged with failure reason

### Learning Feedback
- Monthly Human OS layer assessment
- Self-assessment + 360 feedback
- Growth areas identified + coaching plan adjusted
- Learning velocity calculated (layers progressed per quarter)

---

## Governance Committees

### Decision Review Board
**Composition:** Founder + 2 sector directors  
**Cadence:** Weekly  
**Agenda:**
- Review RED (critical) decisions from past week
- Discuss escalated incidents
- Assess need for policy changes
- Approve authority level promotions

### Governance & Compliance
**Composition:** Founder + general counsel + chief of staff  
**Cadence:** Monthly  
**Agenda:**
- Audit trail compliance (100% logged decisions)
- Permission system review
- Security incident assessment
- Policy updates

---

See also:
- **ONTOLOGY.md** — Decision entity definition
- **TOPOLOGY.md** — Decision Engine + Governance layer
- **INTEGRATION.md** — How governance is enforced across repos
