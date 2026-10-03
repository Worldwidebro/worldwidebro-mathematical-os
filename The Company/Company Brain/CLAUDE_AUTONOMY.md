---
type: autonomy-framework
canonical: false
authority: intelligence-platform-layer
version: 1.0
updated_at: 2026-10-02T23:45:00Z
relates_to: CLAUDE_MASTER_ONTOLOGY
---

# CLAUDE_AUTONOMY — Autonomy Levels & Gating

**Claude can operate at 4 levels: L0 (respond only) → L1 (assist) → L2 (execute) → L3 (autonomous).**

**Last updated:** 2026-10-02  
**Framework:** Laya ML confidence gating  
**Model:** Claude 5 Haiku/Sonnet  
**State:** Production-ready

---

## Autonomy Levels

### [[L0]] — Respond Only (No Action)
**Claude responds but takes NO external actions.**

**When to use:**
- Information queries
- Brainstorming
- Explanation requests
- Analysis only

**Characteristics:**
- No tool use
- No file writes
- No API calls
- No process execution
- No state modification

**Example:**
```
User: "Explain REST APIs"
Claude: [Provides explanation]
↓ No actions taken
```

---

### [[L1]] — Assist (Read + Suggest)
**Claude can READ, UNDERSTAND, and PROPOSE — but REQUIRES APPROVAL before execution.**

**When to use:**
- Code review suggestions
- Refactoring proposals
- Planning workflows
- Risk assessment

**Capabilities:**
- ✅ Read files
- ✅ Query databases (read-only)
- ✅ Analyze code
- ✅ Suggest changes
- ✅ Propose commands
- ❌ Execute without approval
- ❌ Commit without review
- ❌ Deploy without confirmation

**Workflow:**
```
Claude: "I suggest we refactor this function"
        [Proposes specific changes]
        [Shows diff]
        
User: "Approved" or "Rejected"
        ↓ (if approved)
Claude: [Executes only after confirmation]
```

**Approval gates:**
- Show diff before write
- Ask before deletion
- Confirm before commit
- Request permission for API calls

---

### [[L2]] — Execute (Tool Use + Verify)
**Claude EXECUTES tool calls and APIs with AUDIT TRAIL, but remains within supervised scope.**

**When to use:**
- Controlled feature development
- Automated bug fixing
- Build + test execution
- Data processing
- Pre-approved workflows

**Capabilities:**
- ✅ Read + write files
- ✅ Commit + push (to feature branches)
- ✅ Run tests + builds
- ✅ Query APIs
- ✅ Update databases (with constraints)
- ✅ Create resources (with guards)
- ❌ Merge to main
- ❌ Deploy to production
- ❌ Delete critical data

**Verification loop:**
```
User: "Implement feature X"
  ↓
Claude: [Plans approach]
  ↓
Claude: [Creates branch: feature/x]
  ↓
Claude: [Implements + tests]
  ↓
Claude: [Commits with audit trail]
  ↓
Claude: [Suggests PR to main]
  ↓
User: [Reviews + merges]
```

**Guardrails:**
- All actions logged to [[NEO4J]] (KG-007)
- SHA256 provenance on commits
- Rate-limited API calls
- Resource quotas enforced
- Rollback capability maintained

---

### [[L3]] — Autonomous (Multi-Step + Recovery)
**Claude operates INDEPENDENTLY on VERIFIED, HIGH-CONFIDENCE tasks with SELF-RECOVERY.**

**When to use:**
- Proven, repeatable workflows
- High-confidence tasks (score > 0.85)
- Emergency incident response
- Batch operations
- Scheduled maintenance

**Capabilities:**
- ✅ All L2 + more
- ✅ Merge to main (with CI passing)
- ✅ Deploy to staging
- ✅ Update production configs
- ✅ Escalate on errors
- ✅ Self-heal + retry
- ✅ Handle multi-step workflows
- ❌ Delete production data
- ❌ Deploy without monitoring

**Autonomous decision loop:**
```
Scheduled trigger: "Deploy staging"
  ↓
Claude: [Assess confidence]
  ↓ (if confidence > 0.85)
Claude: [Execute deployment]
  ↓
Claude: [Monitor health]
  ↓ (if errors detected)
Claude: [Automatic rollback]
  ↓ (if unrecoverable)
Claude: [Escalate to human]
  ↓ (notify Slack + ops team)
```

**Safety requirements:**
- Laya ML confidence ≥ 0.85
- Previous run success rate ≥ 95%
- Monitoring + alerting active
- Rollback procedure tested
- Human escalation defined

---

## Confidence Gating (Laya ML)

**All L1→L2→L3 transitions gated on Laya ML confidence score.**

### [[CONFIDENCE_SCORING]]

```
Score Range | Autonomy | Behavior | Example
------------|----------|----------|----------
0.0 - 0.40  | L0       | Report only | "This might work, but I'm uncertain"
0.40 - 0.60 | L1       | Suggest + require approval | "I recommend this approach. Confirm?"
0.60 - 0.85 | L2       | Execute + verify | "Implementing feature with audit trail"
0.85 - 1.0  | L3       | Autonomous | "Running proven workflow independently"
```

**Factors in confidence:**
- Task complexity
- Historical success rate
- Available context
- Tool availability
- Prior verification

**Example assessment:**
```python
from infrastructure.agents.laya_autonomy_mapper import ConfidenceMapper

mapper = ConfidenceMapper()
score = mapper.assess("Deploy to production")
# → 0.72 (L2: Execute with verification)

score = mapper.assess("Run daily backup")
# → 0.93 (L3: Autonomous execution)

score = mapper.assess("Implement new database schema")
# → 0.45 (L1: Suggest only)
```

---

## Human-in-the-Loop Gates

### [[APPROVAL_PATTERNS]]

**L1 → L2 Escalation:**
```yaml
Trigger: L1 task requires execution
Response: Ask user
User says: "Approve" or "Reject"
If approved: Proceed to L2 with audit
If rejected: Stop + explain alternative
```

**L2 → L3 Escalation:**
```yaml
Trigger: L2 task wants to escalate
Response: Check Laya confidence
If < 0.85: Require human approval
If ≥ 0.85 + all guards pass: Proceed to L3
If guards fail: Block + escalate
```

**Error Recovery:**
```yaml
Trigger: L3 task encounters error
Response: Attempt recovery
If recoverable: Self-heal + log
If unrecoverable: Escalate to human
Notification: Slack + ops team
Rollback: Automatic if monitoring detects failure
```

---

## Verification Framework

### [[READINESS_CHECKLIST]]

**Before L1→L2 transition:**
- [ ] Scope clearly defined
- [ ] Success criteria specified
- [ ] Error recovery plan exists
- [ ] Audit trail enabled
- [ ] User approval obtained

**Before L2→L3 transition:**
- [ ] Task historically successful (≥3 runs)
- [ ] Laya confidence score ≥ 0.85
- [ ] Monitoring + alerts active
- [ ] Rollback procedure tested
- [ ] Escalation path defined

### [[TESTING_REQUIREMENTS]]

**L1 tasks:**
- Manual walkthrough

**L2 tasks:**
- Unit tests
- Integration tests
- Staging environment
- Rollback test

**L3 tasks:**
- All L2 + full load test
- Chaos engineering test
- Canary deployment
- 10+ successful production runs

---

## Decision Logging (Neo4j)

**All autonomy decisions logged to [[NEO4J]] KG-007:**

```cypher
MATCH (d:Decision {type: 'AUTONOMY_LEVEL'})
RETURN d.task_id, d.confidence_score, d.level_assigned, d.timestamp
```

**Example entry:**
```json
{
  "decision_id": "DEC-20261002-001",
  "task": "Deploy feature X",
  "confidence_score": 0.78,
  "level_assigned": "L2",
  "reasoning": "High success rate + clear scope",
  "approved_by": "user",
  "timestamp": "2026-10-02T15:30:00Z",
  "sha256": "abc123def456...",
  "outcome": "SUCCESS"
}
```

---

## Production Config (Company Brain)

**Set autonomy levels in `.claude/CLAUDE.md`:**

```yaml
# Autonomy Configuration
autonomy:
  default_level: L1                    # Start conservatively
  
  l2_capable_tasks:
    - feature_development
    - bug_fixing
    - test_execution
    - build_operations
  
  l3_capable_tasks:
    - backup_procedures
    - monitoring_checks
    - scheduled_reports
    - incident_response
  
  confidence_threshold_l2: 0.60
  confidence_threshold_l3: 0.85
  
  escalation:
    slack_channel: "#ai-operations"
    pagerduty_enabled: true
    timeout_seconds: 300
```

---

## Examples

### Example 1: Feature Development (L2)
```
User: "Add user authentication to API"
  ↓
Claude: [Assesses confidence: 0.72]
  ↓ L2 gate
Claude: [Creates branch: feature/auth]
Claude: [Implements + tests]
Claude: [Commits with audit trail]
Claude: [Suggests PR]
User: [Reviews + merges]
```

### Example 2: Database Backup (L3)
```
Scheduled: Daily 2 AM backup
  ↓
Claude: [Assesses confidence: 0.91]
  ↓ L3 gate (verified task, 50+ successful runs)
Claude: [Executes backup autonomously]
Claude: [Monitors completion]
Claude: [Logs to Neo4j]
Claude: [Alerts on success]
```

### Example 3: Emergency Incident (L1→L2)
```
Alert: "Production database CPU 95%"
  ↓
Claude: [Analyzes issue]
Claude: [Confidence: 0.48 - too uncertain]
  ↓ L1 gate
Claude: [Proposes solutions to ops team]
Claude: "Try: 1) Increase pool size, 2) Add read replicas"
Ops: [Chooses option 1]
  ↓
Claude: [Confidence: 0.75 - approved]
  ↓ L2 gate
Claude: [Executes config change]
Claude: [Monitors impact]
Claude: [Verifies improvement]
```

---

## Related Frameworks

- [[TASK_EXECUTION_MASTER_ONTOLOGY]] — Task decomposition
- [[LAYA_VENTURE_SCORING]] — Confidence scoring
- [[REALITY]] — Verification against actual state
- [[OMNIROUTE]] — Model selection by autonomy level

---

**Canonical source:** [[CLAUDE_MASTER_ONTOLOGY]]  
**Decision engine:** Laya ML ConfidenceMapper  
**Logging:** Neo4j KG-007



---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
