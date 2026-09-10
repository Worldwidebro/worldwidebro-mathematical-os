# Unit 13: Orchestrator Implementation

**Specification & Implementation Plan**

---

## Overview

Implement the Orchestrator class that chains multiple capabilities into executable workflows.

**Scope:** 60 minutes  
**Priority:** Critical Path (enables E2E workflow automation)  
**Blocker:** Unit 10 (search_capabilities) + Unit 11 (execute_capability) complete ✅

---

## Architecture

### Workflow Definition (WFL-001)

```yaml
workflow_id: WFL-001
name: Sales Workflow (Research → Prep → Call → Summary)
stages:
  - stage_num: 1
    name: Account Research
    capabilities: [CAP-001]
    required_inputs: [company_name]
    outputs: {company_research, key_people, contact_recommendation}
  
  - stage_num: 2
    name: Call Summary
    capabilities: [CAP-003]
    required_inputs: [call_notes, prospect_name]
    outputs: {prospect_interest_level, action_items, follow_up_email_draft}
```

### Execution Flow

```
Orchestrator.execute(WFL-001, {company_name: 'WakeMed'})
  │
  ├─ Stage 1: Execute CAP-001 (account-research)
  │   Input: {company_name}
  │   Output: {company_research, key_people, ...}
  │   Merge into context
  │
  ├─ Stage 2: Execute CAP-003 (call-summary)
  │   Input: {call_notes, prospect_name}
  │   (Note: pause here for user to provide call notes)
  │
  └─ Return WorkflowExecutionResult with all stage outputs + metrics
```

---

## Implementation (capability_orchestrator.py)

### 8 Core Methods

| Method | Purpose | Status |
|--------|---------|--------|
| `load_workflow()` | Load workflow def + stages | ✅ IMPLEMENTED |
| `execute()` | Execute workflow end-to-end | ✅ IMPLEMENTED |
| `_execute_stage()` | Execute single stage (route to sequential/parallel) | ✅ IMPLEMENTED |
| `_execute_sequential()` | Execute capabilities in sequence, passing context | ✅ IMPLEMENTED |
| `_execute_parallel()` | Execute capabilities in parallel (Phase 1B) | 🟡 STUBBED |
| `_extract_inputs()` | Map execution context to capability inputs | ✅ IMPLEMENTED |
| `_handle_error()` | Error recovery (retry/fallback/escalate) | ✅ IMPLEMENTED |
| `_handle_pause()` | Pause workflow for user input + save state | ✅ IMPLEMENTED |

**Bonus method:**
- `resume_workflow()` — Resume from pause with new inputs

### Data Structures

```python
@dataclass
class StageResult:
    stage_id: str
    status: str  # COMPLETE, PAUSED, FAILED
    outputs: Dict[str, Any]
    cost: float
    tokens: int
    latency_ms: int

@dataclass
class WorkflowExecutionResult:
    workflow_id: str
    status: str  # COMPLETE, PAUSED, FAILED
    stage_results: Dict[str, StageResult]
    total_cost: float
    total_tokens: int
    latency_ms: int
```

---

## Test Cases (3)

### Test 1: Execute WFL-001 (End-to-End)

```
Input:
  workflow_id: 'WFL-001'
  initial_context: {'company_name': 'WakeMed'}

Execution Flow:
  Stage 1 (CAP-001): company_name → company_research, key_people
  Stage 2 (CAP-003): call_notes → action_items, follow_up_email
  
Expected Output:
  status: 'COMPLETE'
  stage_results: {
    'STAGE-1': {
      outputs: {company_research, key_people, ...},
      cost: 0.024,
      tokens: 2400,
      latency_ms: 500
    },
    'STAGE-2': {
      outputs: {prospect_interest_level, action_items, ...},
      cost: 0.032,
      tokens: 3200,
      latency_ms: 700
    }
  }
  total_cost: 0.056
  total_tokens: 5600
  latency_ms: 1200
```

### Test 2: Pause After Stage 1

```
Input:
  workflow_id: 'WFL-001'
  initial_context: {'company_name': 'WakeMed'}
  pause_after_stages: [1]

Expected Output:
  status: 'PAUSED'
  stage_results: {'STAGE-1': {...}}
  error: 'Paused after stage 1. Resume with updated context.'
  
Pause State Saved:
  pause_id: 'PAUSE-20260918120000'
  execution_context: {...}
  stage_num: 1
```

### Test 3: Resume Workflow

```
Input:
  pause_id: 'PAUSE-20260918120000'
  resume_inputs: {'call_notes': 'Lab director interested...'}

Execution Flow:
  Restore context from pause state
  Inject resume_inputs
  Execute remaining stages (Stage 2+)

Expected Output:
  status: 'COMPLETE'
  stage_results: {STAGE-1, STAGE-2, ...}
```

---

## Week 1 Revenue Workflow

```
Cold Call (Manual, with Script)
  ↓
Prospect interested? → Yes
  ↓
orchestrator.execute(WFL-001, {company_name}, pause_after_stages=[1])
  ├─ Stage 1: CAP-001 research → prospect_name, key_people
  ├─ Pause for manual call
  ↓
Capture call notes (manual transcription)
  ↓
orchestrator.resume_workflow(pause_id, {call_notes, call_transcript})
  ├─ Stage 2: CAP-003 summary → action_items, follow_up_email
  ├─ Complete
  ↓
Send follow-up email → Schedule trial
```

---

## Success Criteria

✅ **Orchestrator class compiles**
✅ **load_workflow() loads WFL-001 from Supabase**
✅ **execute() runs both stages end-to-end**
✅ **Context flows between stages**
✅ **Pause/resume mechanism works**
✅ **Metrics captured (latency, cost, tokens)**
✅ **Error handling for missing inputs**
✅ **Results logged to workflow_executions table**
✅ **Test cases pass**

---

## Files

- `_MCP/capability_orchestrator.py` (500+ LOC)
  - CapabilityOrchestrator class with 8 methods
  - StageResult, WorkflowExecutionResult dataclasses
  - Test cases defined

- `_MCP/UNIT-13-ORCHESTRATOR-SPEC.md` (this file)
  - Specification
  - Test cases
  - Integration guide

---

## Supabase Tables Required

**workflows** table
- ref_id (e.g., WFL-001)
- name
- stages (JSONB array)

**workflow_pauses** table
- pause_id
- workflow_id
- execution_id
- stage_num
- execution_context (JSONB)
- status
- created_at

**workflow_executions** table (optional, for audit logging)
- id
- workflow_id
- stage_results (JSONB)
- total_cost
- total_tokens
- latency_ms
- timestamp

---

## Next: Unit 14

**E2E Workflow Test (Happy Path)** (20 min)

1. Load WFL-001
2. Execute with company_name
3. Pause after Stage 1
4. Resume with call_notes
5. Verify all outputs present
6. Verify metrics captured

---

## Unit 13 Completion Checklist

- [ ] Orchestrator class implemented (8 methods)
- [ ] load_workflow() loads workflow definition
- [ ] execute() runs stages sequentially
- [ ] Context flows between stages
- [ ] Pause/resume working
- [ ] Error handling for edge cases
- [ ] Metrics captured (latency, cost, tokens)
- [ ] Code syntax valid
- [ ] Test cases defined
- [ ] Code committed
- [ ] Ready for Unit 14 (E2E testing)

---

**Status:** 🟡 IN PROGRESS (implementation complete, testing next)  
**Estimated Time Remaining:** 10 min (testing + commit)  
**Timeline:** Sep 18 (Phase 1A)
