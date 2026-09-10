# Unit 12: Anthropic Sales Plugin Wiring

**Specification & Validation**

---

## Overview

Wire Anthropic Sales Plugin into `execute_capability()` routing layer so CAP-001 (account-research) and CAP-003 (call-summary) invoke plugin skills directly.

**Scope:** 20 minutes  
**Priority:** Critical Path (enables Week 1 revenue workflow)  
**Blocker:** None (Unit 11 complete)

---

## What Gets Wired

### Anthropic Sales Plugin
- **Installed via:** `claude plugins add knowledge-work-plugins/sales`
- **Skills used:** account-research, call-summary
- **Documentation:** `/tmp/knowledge-work-plugins/sales/README.md`

### Capabilities

| Capability | Plugin Skill | Input | Output |
|------------|--------------|-------|--------|
| **CAP-001** | `account-research` | `company_name` | `company_research`, `key_people`, `contact_recommendation` |
| **CAP-003** | `call-summary` | `call_notes`, `prospect_name` | `prospect_interest_level`, `action_items`, `follow_up_email_draft` |

---

## Implementation

### Router Update (openwork_mcp_tools.py)

`_execute_anthropic_skill()` now:

1. **Routes by ref_id** (CAP-001, CAP-003) or skill_name
2. **Validates inputs** (company_name for research, call_notes for summary)
3. **Returns structured output** matching plugin skill response schema
4. **Captures metrics** (tokens, cost) for each execution
5. **Handles errors** gracefully (missing inputs, plugin unavailable)

### Plugin Integration Points

```python
# Unit 12 Implementation:
if ref_id == 'CAP-001':
    # Call: plugin.account_research(company_name)
    # Returns: company_research + key_people + contact_recommendation
    
if ref_id == 'CAP-003':
    # Call: plugin.call_summary(call_notes)
    # Returns: prospect_interest_level + action_items + follow_up_email_draft
```

---

## Test Cases (2)

### Test 1: Account Research (CAP-001)

```
Input:
  capability_id: 'CAP-001'
  inputs: {'company_name': 'WakeMed'}

Expected Output:
  status: 'success'
  output.company_name: 'WakeMed'
  output.company_research: {...}
  output.key_people: [...]
  output.contact_recommendation: 'Start with Lab Director...'
  
Latency: < 5000 ms
Tokens: 2400
Cost: $0.024
```

### Test 2: Call Summary (CAP-003)

```
Input:
  capability_id: 'CAP-003'
  inputs: {
    'call_notes': 'Lab director said they process 300+ specimens/day...',
    'prospect_name': 'WakeMed Labs'
  }

Expected Output:
  status: 'success'
  output.prospect_name: 'WakeMed Labs'
  output.prospect_interest_level: 'interested'
  output.specimen_volume_confirmed: '300/day'
  output.pain_signals: ['delays', 'compliance_risk', 'cost_pressure']
  output.key_points: [
    'Currently uses generic courier service',
    'Processes 300+ specimens per day',
    'Pain point: delayed results affecting patient care',
    'Pain point: compliance audit risk with current vendor'
  ]
  output.action_items: [
    {action: 'Send trial agreement (5 free deliveries)', ...},
    {action: 'Schedule onboarding call with operations manager', ...},
    {action: 'Prepare HIPAA compliance brief for their audit', ...}
  ]
  output.follow_up_email_draft: (realistic email with value prop + trial offer)
  
Latency: < 5000 ms
Tokens: 3200
Cost: $0.032
```

---

## Success Criteria

✅ **CAP-001 test passes**
- Input validation working (company_name required)
- Output includes all required keys
- Metrics captured correctly

✅ **CAP-003 test passes**
- Input validation working (call_notes required)
- Output includes all required keys
- Follow-up email draft is realistic

✅ **Error handling**
- Missing inputs return error status + error message
- Unknown capabilities return error
- Exceptions caught gracefully

✅ **Integration with execute_capability()**
- Router correctly dispatches to _execute_anthropic_skill()
- Output logged to capability_executions table
- Execution ID + timestamp included

✅ **Week 1 revenue workflow**
- Cold call (manual) → call notes → CAP-003 summary → follow-up email
- Prospect research (CAP-001) feeds into call prep

---

## Files Modified

- `_MCP/openwork_mcp_tools.py`: Updated `_execute_anthropic_skill()` (lines 403-505)
  - Added ref_id-based routing (CAP-001, CAP-003)
  - Added input validation
  - Added structured output matching plugin schema
  - Added error handling

---

## Execution Flow (Week 1 Revenue)

```
Cold Call with Script
  ↓
Prospect interested? → Yes
  ↓
Capture call notes (manual transcription)
  ↓
execute_capability(CAP-003, {call_notes})
  ↓
_execute_anthropic_skill() routes to call-summary
  ↓
Output: prospect_interest, action_items, follow_up_email_draft
  ↓
Send follow-up email + schedule trial
```

---

## Next: Unit 13

**Orchestrator Implementation** (60 min)

Wire the Orchestrator class to compose workflows:
1. Load WFL-001 definition (stages array)
2. Execute stage sequence (research → prep → call → summary)
3. Pass outputs between stages
4. Handle pause/resume for manual approvals
5. Log workflow execution

---

## Unit 12 Completion Checklist

- [ ] _execute_anthropic_skill() updated with plugin wiring
- [ ] CAP-001 test passes
- [ ] CAP-003 test passes
- [ ] Error cases handled
- [ ] Output schema matches UNIT-11-EXECUTE-CAPABILITY-SPEC.md
- [ ] Metrics (latency, tokens, cost) captured
- [ ] Code committed
- [ ] Ready for Unit 13 (Orchestrator)

---

**Status:** 🟡 IN PROGRESS (wiring complete, testing next)  
**Estimated Time Remaining:** 15 min (testing + commit)  
**Timeline:** Sep 17 (Phase 1A)
