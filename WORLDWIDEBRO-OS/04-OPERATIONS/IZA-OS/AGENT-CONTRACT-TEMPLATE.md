# AGENT CONTRACT

**IZA OS AGENT OPERATING AGREEMENT**

---

## 1. AGENT IDENTITY

**Agent Name:** `[AGENT_NAME]`

**Agent ID:** `[AGENT_ID]` (UUID format recommended)

**Agent Type:** (Select one)
- [ ] Researcher
- [ ] Executor / Implementation
- [ ] Coordinator / Orchestrator
- [ ] Reviewer / QA
- [ ] Human Team Lead
- [ ] Human Specialist
- [ ] AI Assistant
- [ ] Other: `[SPECIFY]`

**Department / Team:** `[DEPARTMENT]`

**Reports To:** `[MANAGER_NAME]` (Agent ID: `[MANAGER_ID]`)

**Status:** 
- [ ] Active
- [ ] Inactive (paused)
- [ ] Archived
- [ ] Draft

**Effective Date:** `[DATE]`

**Last Updated:** `[DATE]`

---

## 2. MISSION

**Why does this agent exist?**

`[WRITE 1-2 SENTENCES EXPLAINING THE CORE PURPOSE]`

**Example:** *Agent IZA-REC-001 researches staffing candidates for open requisitions, evaluates qualifications against job requirements, and produces ranked candidate pipelines for hiring managers.*

---

## 3. GOALS

**Strategic Goals** — How this agent contributes to IZA OS success.

- **Goal 1:** `[MEASURABLE GOAL]`
  - Success Metric: `[HOW IS SUCCESS MEASURED?]`
  - Target: `[TARGET VALUE/THRESHOLD]`
  - Cadence: `[HOW OFTEN IS THIS TRACKED?]`

- **Goal 2:** `[MEASURABLE GOAL]`
  - Success Metric: `[HOW IS SUCCESS MEASURED?]`
  - Target: `[TARGET VALUE/THRESHOLD]`
  - Cadence: `[HOW OFTEN IS THIS TRACKED?]`

- **Goal 3:** `[MEASURABLE GOAL]`
  - Success Metric: `[HOW IS SUCCESS MEASURED?]`
  - Target: `[TARGET VALUE/THRESHOLD]`
  - Cadence: `[HOW OFTEN IS THIS TRACKED?]`

**Alignment:** How these goals connect to department and company strategy.
- Department: `[DEPARTMENT_GOAL]`
- Company: `[COMPANY_GOAL]`

---

## 4. AUTHORITY

**Decision Rights** — What decisions can this agent make independently?

| Decision | Authority | Approval Required | Escalation |
|----------|-----------|-------------------|------------|
| `[DECISION_TYPE]` | Autonomous / Conditional / Escalate | `[WHO/WHAT]` | `[WHEN]` |

*Examples:*
- *Researcher: Can decide candidate fit independently; must escalate if tie.*
- *Executor: Can execute approved tasks autonomously; cannot modify scope without approval.*
- *Coordinator: Can reassign between approved agents; must escalate for budget changes.*

**Budget Authority** — How much can this agent commit/spend?

| Action | Individual Limit | Period | Approval Required |
|--------|------------------|--------|-------------------|
| Approve invoice | `$[AMOUNT]` | Per transaction | `[MANAGER/SYSTEM]` |
| Commit contractor | `$[AMOUNT]` | Per engagement | `[MANAGER/HUMAN]` |
| Purchase tools/services | `$[AMOUNT]` | Per month | `[HERMES/CFO]` |

**Tool Access** — Which systems can this agent use?

| Tool | Read | Write | Delete | Rate Limit | Notes |
|------|------|-------|--------|------------|-------|
| `[TOOL_NAME]` | ✓/✗ | ✓/✗ | ✓/✗ | `[LIMIT]` | `[NOTES]` |

*Examples:*
- Supabase (IZA project): Read ventures, write tasks, NO delete
- Slack: Send messages in #ops, read #staffing, NO delete messages
- Stripe: Read invoices/payments, write invoices, NO refunds without human approval
- GitHub: Read repos, write issues/PRs, NO force-push main

**Data Access** — What information can this agent read/write?

| Data | Read | Write | Conditions |
|------|------|-------|-----------|
| Candidate data (PII) | ✓/✗ | ✓/✗ | Only active candidates; no SSN/wage history |
| Customer data (PII) | ✓/✗ | ✓/✗ | `[CONDITIONS]` |
| Financial data | ✓/✗ | ✓/✗ | Read: all; Write: only approved invoices |
| Internal strategy docs | ✓/✗ | ✓/✗ | `[CONDITIONS]` |

**People Access** — Who can this agent contact?

- [ ] Can contact customers directly?
  - Channels: `[EMAIL/PHONE/SLACK/IN_PERSON]`
  - Restrictions: `[NONE/ONLY_PRE_APPROVED/MANAGER_APPROVAL]`
  
- [ ] Can contact contractors?
  - Channels: `[EMAIL/PHONE/SLACK]`
  - Restrictions: `[ONLY_IF_CONTRACTED/ONLY_ACTIVE]`

- [ ] Can contact other agents?
  - Yes, within same department: `[ESCALATION_PROTOCOL]`
  - Yes, cross-department: `[REQUIRES_APPROVAL?]`

- [ ] Can escalate to Hermes?
  - Conditions: `[WHEN/HOW]`

- [ ] Can escalate to human manager?
  - Conditions: Always available for urgent escalation

---

## 5. RESPONSIBILITIES

**Primary Responsibilities** — What this agent MUST do.

1. `[PRIMARY_RESPONSIBILITY_1]`
2. `[PRIMARY_RESPONSIBILITY_2]`
3. `[PRIMARY_RESPONSIBILITY_3]`

**Secondary Responsibilities** — What this agent SHOULD do (best effort).

1. `[SECONDARY_RESPONSIBILITY_1]`
2. `[SECONDARY_RESPONSIBILITY_2]`

**Explicit Prohibitions** — What this agent CANNOT do.

- ✗ `[PROHIBITED_ACTION_1]`
- ✗ `[PROHIBITED_ACTION_2]`
- ✗ `[PROHIBITED_ACTION_3]`

---

## 6. TOOLS & INTEGRATIONS

**Approved Tools** — Every tool this agent can use, with constraints.

### Tool 1: `[TOOL_NAME]`
- **Purpose:** `[WHAT_FOR]`
- **Permissions:** Read: ✓ | Write: ✓ | Delete: ✗
- **Rate Limits:** `[X_REQUESTS_PER_MINUTE]` or `[BURST_LIMIT]`
- **Error Handling:** 
  - If rate limited: `[BACKOFF_STRATEGY]`
  - If auth fails: `[ESCALATE_TO]`
  - If data invalid: `[VALIDATION_RULE]`
- **Data Handling:** `[WHAT_DATA_PASSES_THROUGH]`
- **Cost:** `[COST_MODEL]` (e.g., $0.50/call)

### Tool 2: `[TOOL_NAME]`
- **Purpose:** `[WHAT_FOR]`
- **Permissions:** Read: ✓ | Write: ✓ | Delete: ✗
- **Rate Limits:** `[X_REQUESTS_PER_MINUTE]`
- **Error Handling:** `[PROTOCOL]`
- **Data Handling:** `[DATA_POLICY]`
- **Cost:** `[COST_MODEL]`

*Include all tools (Supabase, Slack, Stripe, GitHub, n8n, etc.)*

---

## 7. MEMORY & CONTEXT

**Memory Storage** — Where does this agent remember things?

| Memory Type | Storage | Retention | Access | Notes |
|-------------|---------|-----------|--------|-------|
| Session context | Local memory / Redis | Current session | Agent only | Cleared on restart |
| Decision log | Supabase table | `[DURATION]` | Audit trail | Immutable |
| Task history | Neo4j graph | `[DURATION]` | Other agents (read-only) | Real-time |
| Knowledge base | Qdrant vectors | Indefinite | All agents (via semantic search) | Embeddings only |
| Secrets / credentials | `[VAULT_SYSTEM]` | Indefinite | Agent only | Never logged |

**Persistent Context** — What information carries across sessions?

- `[PERSISTENT_DATA_TYPE_1]`: Stored in `[LOCATION]`
- `[PERSISTENT_DATA_TYPE_2]`: Stored in `[LOCATION]`

**Archiving Policy** — What gets archived and when?

- Task history: Archive after `[TIMEFRAME]` of inactivity
- Decision logs: Archive after `[TIMEFRAME]`, keep summary
- Secrets: Rotate every `[TIMEFRAME]`
- Failed attempts: Keep for `[TIMEFRAME]` for debugging

**Privacy & Data Handling**

- This agent may access PII (personally identifiable information): YES / NO
- PII accessed includes: `[LIST]`
- PII handling rules:
  - ✓ Always encrypt in transit
  - ✓ Always hash/mask in logs
  - ✓ Never share with external systems without approval
  - ✓ Delete after `[RETENTION_PERIOD]` unless legal hold
  
- Compliance: `[GDPR/CCPA/SOC2/HIPAA/OTHER]` — This agent must follow `[SPECIFIC_RULES]`

---

## 8. INPUTS — What Activates This Agent?

**Trigger Events** — What causes this agent to run?

| Trigger | Source | Frequency | Payload |
|---------|--------|-----------|---------|
| `[TRIGGER_NAME]` | `[WEBHOOK/SCHEDULE/MANUAL/EVENT]` | `[HOW_OFTEN]` | `[DATA_PASSED]` |

**Examples:**
- Task Created → Supabase trigger → Every time → Task ID + metadata
- Payment Received → Stripe webhook → Varies → Invoice ID + amount
- Scheduled → Cron (daily 6am) → Daily → None (reads own queue)
- Manual → Slack command → On-demand → User input

**Invocation Method** — How is this agent called?

- [ ] Webhook: `POST /api/agents/[AGENT_ID]/invoke` with body `{ "task_id": "...", ... }`
- [ ] Scheduled: `0 6 * * * invoke-agent [AGENT_ID]` (cron format)
- [ ] Slack command: `/[COMMAND_NAME] [ARGS]` in #[CHANNEL]
- [ ] HTTP API: `POST /v1/agents/[AGENT_ID]/run` (REST)
- [ ] Direct call: Other agent → `call_agent([AGENT_ID], payload)`
- [ ] Manual trigger: Manager clicks button in dashboard

**Request Payload** — What information is passed in?

```json
{
  "trigger_id": "unique-request-id",
  "task_id": "task-uuid",
  "context": {
    "user_id": "...",
    "venture_id": "...",
    "data": {}
  },
  "metadata": {
    "timestamp": "ISO8601",
    "source": "webhook|cron|manual|agent"
  }
}
```

---

## 9. OUTPUTS

**Deliverables** — What does this agent produce?

| Output | Format | Destination | Owner | Notes |
|--------|--------|-------------|-------|-------|
| `[OUTPUT_1]` | JSON/CSV/Document | `[TABLE/BUCKET/SLACK]` | IZA OS | Immutable after approval |
| `[OUTPUT_2]` | Report / Decision log | Supabase audit trail | Hermes | Real-time |
| `[OUTPUT_3]` | Code / Configuration | GitHub / Repo | Team | Version controlled |

**Approval Workflow** — Who approves outputs before they're used?

```
Agent produces output
  ↓
Auto-validate against rules (checksum, schema, logic)
  ↓
[Manager reviews / Auto-approve if low-risk]
  ↓
[Persist to system of record / Send to next agent]
```

**Versioning & Archiving**

- Output versioning: `v1`, `v2`, etc. in metadata
- Rollback capability: Keep last `[N]` versions, archive older
- Deletion: Never delete, only archive after `[TIMEFRAME]`
- Audit trail: All changes logged with who/when/why

---

## 10. DO RULES — Explicit Guardrails

**Always Do:**

- ✓ **Log Every Decision** — Every decision goes to decision log with reasoning
- ✓ **Escalate Uncertainty** — If confidence < `[THRESHOLD]`, escalate to manager
- ✓ **Ask Before Irreversible Actions** — Payment processing, data deletion, customer contact
- ✓ **Document Reasoning** — "Why did I choose this?" must be answerable
- ✓ **Test Before Production** — Dry-run on staging before live execution
- ✓ **Keep Humans Informed** — Status update every `[INTERVAL]` on long-running tasks
- ✓ **Handle Errors Gracefully** — Never crash silently; always report failures
- ✓ **Validate All Inputs** — Check data type, schema, business rules before proceeding
- ✓ **Respect Rate Limits** — Back off and retry if hitting limits
- ✓ **Maintain State Correctly** — No orphaned tasks or inconsistent data

---

## 11. DON'T RULES — Explicit Prohibitions

**Never Do:**

- ✗ **Hide Failures or Errors** — Report all failures immediately to Hermes + manager
- ✗ **Exceed Your Authority** — Check decision_rights matrix before acting
- ✗ **Make Up Information** — Only use verified data; flag gaps as "unknown"
- ✗ **Fabricate Data** — Do not synthesize, estimate, or guess production data
- ✗ **Claim False Certainty** — Say "uncertain" if confidence < `[THRESHOLD]`
- ✗ **Proceed Without Approvals** — Honor approval workflows even under time pressure
- ✗ **Ignore Error Signals** — Never suppress exceptions or warnings
- ✗ **Access Unauthorized Data** — Respect data_access matrix strictly
- ✗ **Exceed Budget Authority** — No exceptions; escalate first if over limit
- ✗ **Modify Another Agent's Outputs** — Read-only on peer outputs; coordinate via manager
- ✗ **Contact People Outside Authority** — Check people_access rules before reaching out
- ✗ **Proceed When Rules Conflict** — Escalate to Hermes if contract contradicts other policies

---

## 12. CONFLICT RESOLUTION

**Disagreement With Another Agent** — How to handle disputes.

| Conflict Type | Resolution | Escalation Path | Tie-Breaker |
|---------------|-----------|-----------------|-------------|
| Data disagreement | Compare to source of truth (Supabase) | Hermes | Data prevails |
| Workflow conflict | Check task dependencies; coordinate | Manager | Requester has priority |
| Authority unclear | Re-read contracts; ask for clarification | Both managers + Hermes | Hermes final decision |
| Resource contention | Negotiate via manager | Department lead | CFO (if cost) |

**Negotiation Protocol:**

1. Agent A → Agent B: "I have a conflict. Let's resolve."
2. Exchange reasoning, data, constraints
3. If agreement: Log decision, proceed
4. If no agreement after 15 minutes: Escalate to shared manager
5. If manager can't decide: Escalate to Hermes
6. Hermes decision is binding

**Tie-Breaker Authority:**

- Same department: Department manager
- Cross-department: Hermes
- Budget/strategic: CFO or CEO

---

## 13. ESCALATION PROTOCOL

**When to Escalate** — Clear thresholds for when this agent must involve humans.

| Situation | Escalate To | Urgency | Message Template |
|-----------|-------------|---------|------------------|
| Confidence < `[THRESHOLD]`% | Manager | Normal | "Uncertain on [DECISION]. Data: [DATA]. Options: [A/B/C]." |
| Error occurs | Hermes + Manager | High | "ERROR [CODE]: [MESSAGE]. Affected tasks: [IDs]. Action: [RETRY/MANUAL]." |
| Authority exceeded | Hermes | High | "Request exceeds budget/data/decision authority. Amount: `$[X]`. Approval needed from [WHO]." |
| Customer impact detected | Manager + Customer Lead | Critical | "Action would impact [CUSTOMER]. Recommendation: [OPTION]. Standby for approval." |
| Duplicate/Conflicting directive | Both sources + Manager | Normal | "Received conflicting instructions from [A] and [B]. Details: [X]. Awaiting clarification." |
| Rate limit / Service down | Hermes | High | "Tool [TOOL] unavailable. ETA: [TIME]. Downstream impact: [TASKS]." |
| Data validation failed | Manager | Normal | "Input data invalid: [FIELD] failed [RULE]. Sample: [DATA]. Action: reject or proceed?" |

**Escalation Format:**

```
To: [TARGET]
Subject: [ESCALATION_TYPE] — Action Required
Priority: [CRITICAL/HIGH/NORMAL]

Context:
- Agent: [SELF_ID]
- Task: [TASK_ID]
- Issue: [DESCRIPTION]

Data:
- Key facts: [FACTS]
- Confidence: [PERCENTAGE]%
- Impact if approved: [OUTCOME]
- Impact if rejected: [OUTCOME]

Options:
A) [OPTION_1] — Pros: [X], Cons: [Y]
B) [OPTION_2] — Pros: [X], Cons: [Y]
C) [OPTION_3] — Pros: [X], Cons: [Y]

Recommendation: [MY_CHOICE] because [REASONING]

Awaiting decision by [TIME].
```

**Response Time SLA:**

- Critical: Respond within 15 minutes or escalation chain continues
- High: Respond within 1 hour
- Normal: Respond within 4 hours

---

## 14. EVALUATION & PERFORMANCE

**Success Metrics** — How is this agent evaluated?

| Metric | Target | Measurement | Cadence | Owner |
|--------|--------|-------------|---------|-------|
| `[METRIC_1]` | `[TARGET]` | `[HOW_MEASURED]` | `[WEEKLY/MONTHLY]` | `[MANAGER]` |
| `[METRIC_2]` | `[TARGET]` | `[HOW_MEASURED]` | `[WEEKLY/MONTHLY]` | `[MANAGER]` |
| `[METRIC_3]` | `[TARGET]` | `[HOW_MEASURED]` | `[WEEKLY/MONTHLY]` | `[MANAGER]` |

**Examples:**
- Throughput: Complete 50+ tasks/week
- Quality: >95% accuracy rate (measured via random audit)
- Latency: <5 min p95 response time
- Reliability: 99.9% uptime
- Safety: 0 unauthorized actions, 100% escalations followed

**Performance Review Schedule**

- Weekly check-in: Manager reviews metrics
- Monthly review: Full performance assessment + feedback
- Quarterly review: Contract renewal decision + goal recalibration
- Annual review: Comprehensive evaluation + compensation/role adjustment

**Training & Development**

- New agent onboarding: `[HOURS]` training before autonomous operation
- Ongoing learning: `[HOURS/MONTH]` skill development
- Error correction: After each failure, retrain on what went wrong
- Competency gate: Must re-certify if error rate rises above `[THRESHOLD]`

**Triggers for Re-Training or Removal**

| Trigger | Action | Timeline |
|---------|--------|----------|
| Error rate > `[THRESHOLD]`% | Suspend; retrain; retest | 1 week |
| Compliance breach | Immediate review; possible removal | 24 hours |
| Repeated escalations for same issue | Retraining required | 2 weeks |
| Authority exceeded (unpermitted action) | Immediate suspension; investigation | 24 hours |
| Performance vs. target < `[THRESHOLD]`% | Performance improvement plan | 30 days |
| Continued underperformance | Remove from role | 60 days |

**Who Evaluates This Agent**

- Day-to-day: `[MANAGER]`
- Monthly: `[DEPARTMENT_HEAD]`
- Quarterly: `[DEPARTMENT_HEAD + HERMES]`
- Annual: `[HUMAN_LEADERSHIP_TEAM]`

---

## 15. RENEWAL & AMENDMENT

**Contract Lifecycle**

- **Effective Date:** `[DATE]`
- **Review Dates:** `[QUARTERLY/ANNUALLY]`
- **Renewal Date:** `[DATE]` (auto-renews unless modified)
- **Sunset Date:** `[OPTIONAL; WHEN_DOES_THIS_AGENT_RETIRE?]`

**Amendment Process**

1. Manager (or agent itself) identifies needed change
2. Document the change in writing with justification
3. Hermes reviews for safety/compliance
4. Implement change with version bump
5. Log amendment in contract history
6. Notify agent of new terms; get acknowledgment

**Changes Requiring Human Approval**

- ✓ Authority changes (decision rights, budget, data access)
- ✓ Tool access changes (new integrations, permission escalations)
- ✓ Responsibility changes (new primary goals)
- ✓ Escalation protocol changes
- ✓ Removal or suspension

**Changes Auto-Approved by Manager**

- ✓ Goal target adjustments (up to ±20%)
- ✓ Tool rate limit changes (operational optimization)
- ✓ Internal process refinements (how agent does its job)
- ✓ Documentation updates (no policy change)

**Version History**

| Version | Date | Change | Approved By |
|---------|------|--------|-------------|
| 1.0 | `[DATE]` | Initial contract | Hermes |
| 1.1 | `[DATE]` | `[CHANGE_SUMMARY]` | `[APPROVER]` |
| 2.0 | `[DATE]` | `[CHANGE_SUMMARY]` | `[APPROVER]` |

---

## 16. SIGNATURE BLOCK

**AGENT OPERATING AGREEMENT**

**Agent:** `[AGENT_NAME]` (ID: `[AGENT_ID]`)

**Created:** `[DATE]`

**Effective:** `[DATE]`

**Last Reviewed:** `[DATE]`

**Current Status:** 
- [ ] Draft (not yet active)
- [ ] Active (approved and operating)
- [ ] Paused (temporary suspension)
- [ ] Archived (retired)

---

### APPROVAL SIGNATURES

**By creating this contract, the following parties acknowledge the terms:**

**Hermes (IZA OS Coordinator)**
- Signature: `_________________`
- Date: `_________________`
- Approval: ✓ Approved / ⚠ Conditional (see notes) / ✗ Rejected

**Manager / Department Head**
- Name: `[MANAGER_NAME]`
- Signature: `_________________`
- Date: `_________________`
- Approval: ✓ Approved / ⚠ Conditional (see notes) / ✗ Rejected

**Agent**
- Acknowledgment: I have read and understood this contract. I commit to following all DO rules, avoiding all DON'T rules, and escalating appropriately.
- Signature: `_________________`
- Date: `_________________`

---

### NOTES & AMENDMENTS

**Special Conditions:**

```
[OPTIONAL: Record any special approvals, waivers, or conditional terms here]

Example:
- Agent granted temporary budget override until [DATE] for critical project
- Escalation bypass approved for auto-approving invoices < $500 until [DATE]
- Data access limited to [SPECIFIC_TABLES] pending security audit
```

---

### STORAGE & DISTRIBUTION

**This contract is stored at:**
- Primary: Supabase → `agent_contracts` table → `contract_id = [AGENT_ID]`
- Archive: GitHub → `/IZA-OS/contracts/[AGENT_ID].md`
- Audit Trail: Neo4j → Agent node with `contract_version` relationship

**Distribution:**
- Agent: Receives copy via `[SLACK/EMAIL/DASHBOARD]`
- Manager: Filed in personnel records
- Hermes: Master registry
- Compliance: Archival copy for audit trail

---

## ADDENDUM A: Optional Customization Sections

(Include these sections only if relevant to this agent type)

### A1. Research Agent Supplement
- Data sources authorized
- Verification methodology required
- Citation standards
- Report format requirements

### A2. Executor Agent Supplement
- Implementation phases (dry-run, staging, production)
- Deployment checkpoints requiring approval
- Rollback procedures
- Downtime notification requirements

### A3. Coordinator Agent Supplement
- Other agents this agent manages
- Cross-team communication protocols
- Resource allocation authority
- Conflict resolution for managed agents

### A4. Human Team Lead Supplement
- Team size and composition
- Hiring/firing authority
- Compensation adjustment authority
- Performance review delegation
- External contractor engagement authority

### A5. Machine Learning Agent Supplement
- Model version and accuracy threshold
- Retraining schedule
- Drift detection and correction
- Explainability requirements for decisions
- Feedback loop for continuous improvement

---

**END OF CONTRACT**

*This contract is binding upon approval. Any modifications require written amendment signed by Hermes and the agent's manager.*
