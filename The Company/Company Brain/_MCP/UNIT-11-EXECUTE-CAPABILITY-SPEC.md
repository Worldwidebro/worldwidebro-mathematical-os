# Unit 11: execute_capability() MCP Tool

**Specification & Validation Plan**

---

## Overview

Implement the second MCP tool for OpenWork: `execute_capability()`

This tool routes capabilities to the correct execution handler (Anthropic plugin, OSS framework, internal MCP) and logs results to Supabase for audit tracking.

---

## Function Signature

```python
def execute_capability(
    capability_id: str,
    inputs: Dict[str, Any],
    context: Optional[Dict] = None
) -> Dict[str, Any]:
    """
    Execute a capability. Routes to correct handler based on source.
    
    Returns:
    {
        'status': 'success|error|timeout',
        'output': {...},
        'execution_id': str,
        'latency_ms': int,
        'tokens_used': int,
        'cost_usd': float,
        'timestamp': str
    }
    """
```

---

## Routing Logic

### By Source

| Source | Capabilities | Handler | Routing |
|--------|--------------|---------|---------|
| **anthropic** | CAP-001, CAP-003 | Anthropic Sales Plugin | Call skill directly via MCP |
| **awesome-claude-code** | CAP-101, CAP-401 | OSS framework | Query GitHub repo / reference material |
| **internal** | CAP-201 | Custom MCP wrapper | Supabase audit logging |

### By Capability Type

| Capability | Type | Execution |
|------------|------|-----------|
| **CAP-001** | account-research | Anthropic plugin skill (web search + enrichment) |
| **CAP-003** | call-summary | Anthropic plugin skill (LLM extraction) |
| **CAP-101** | agentic-patterns | Reference material (no execution, return docs) |
| **CAP-401** | librarian-mcp | Query Obsidian vault via Librarian MCP |
| **CAP-201** | HIPAA compliance | Log to Supabase audit table |

---

## Test Cases (5)

| # | Test Name | Capability | Inputs | Expected Status | Expected Keys |
|----|-----------|-----------|--------|-----------------|----------------|
| 1 | Account research | CAP-001 | `{company_name: 'WakeMed'}` | success | `[company_research, key_people]` |
| 2 | Call summary | CAP-003 | `{call_notes: '...'}` | success | `[prospect_interest, action_items]` |
| 3 | Agentic patterns | CAP-101 | `{}` | success | `[pattern, use_cases]` |
| 4 | Librarian MCP | CAP-401 | `{query: 'objection'}` | success | `[vault, results]` |
| 5 | HIPAA audit | CAP-201 | `{prospect_name: 'WakeMed', data_accessed: [...]}` | success | `[audit_log_id, compliance_status]` |

**Passing all 5 tests = ✅ Unit 11 DONE**

---

## Execution Flow

```
User → execute_capability(CAP-001, {company_name})
           ↓
    Lookup metadata (Neo4j)
           ↓
    Validate inputs
           ↓
    Route by source:
    ├─ anthropic → Anthropic Sales Plugin
    ├─ awesome-claude-code → OSS handler
    └─ internal → Custom MCP wrapper
           ↓
    Execute handler
           ↓
    Log to Supabase (capability_executions table)
           ↓
    Return result + metrics (latency, tokens, cost)
```

---

## Handler Implementations

### Handler 1: Anthropic Skills (CAP-001, CAP-003)

```python
def _execute_anthropic_skill(capability, inputs):
    skill_name = capability.get('skill', {}).get('name')
    
    if skill_name == 'account-research':
        # Call: anthropic_plugin.account_research(inputs['company_name'])
        return {
            'status': 'success',
            'output': {
                'company_research': '...',
                'key_people': [...],
                'recent_news': [...]
            },
            'tokens': 2000,
            'cost': 0.02
        }
    
    elif skill_name == 'call-summary':
        # Call: anthropic_plugin.call_summary(inputs['call_notes'])
        return {
            'status': 'success',
            'output': {
                'prospect_interest': 'interested|maybe|no',
                'specimen_volume': '300/day',
                'action_items': [...],
                'follow_up_email': '...'
            },
            'tokens': 1500,
            'cost': 0.015
        }
```

### Handler 2: OSS Skills (CAP-101, CAP-401)

```python
def _execute_oss_skill(capability, inputs):
    skill_name = capability.get('slug')
    
    if skill_name == 'agentic-workflow-patterns':
        # Reference material only
        return {
            'status': 'success',
            'output': {
                'pattern': 'orchestrator-workers',
                'use_cases': [...]
            },
            'tokens': 0,
            'cost': 0
        }
    
    elif skill_name == 'librarian-mcp':
        # Query Obsidian vault
        return {
            'status': 'success',
            'output': {
                'vault': 'HealthRoute Obsidian',
                'results': [
                    {'note': 'Objection Handling', 'relevance': 0.95},
                    {'note': 'Trial Pitch Template', 'relevance': 0.88}
                ]
            },
            'tokens': 500,
            'cost': 0.005
        }
```

### Handler 3: Internal Skills (CAP-201)

```python
def _execute_internal_skill(capability, inputs):
    if capability.get('slug') == 'healthroute-hipaa-compliance':
        # Log to Supabase
        return {
            'status': 'success',
            'output': {
                'audit_log_id': 'AUDIT-20260917...',
                'compliance_status': 'HIPAA_COMPLIANT',
                'phi_accessed': inputs.get('data_accessed'),
                'hipaa_concern_level': inputs.get('concern_level')
            },
            'tokens': 500,
            'cost': 0.0
        }
```

---

## Logging & Audit Trail

Every execution is logged to Supabase `capability_executions` table:

```sql
INSERT INTO capability_executions (
    id, capability_id, inputs, output, status,
    latency_ms, tokens_used, cost_usd, timestamp
) VALUES (
    'EXEC-20260917123456-CAP-001',
    'CAP-001',
    '{"company_name": "WakeMed"}',
    '{"company_research": "..."}',
    'success',
    8234,  -- latency in milliseconds
    2000,  -- tokens consumed
    0.02,  -- cost in USD
    '2026-09-17T12:34:56Z'
)
```

**Audit benefits:**
- Cost tracking per capability
- Performance monitoring (latency trends)
- Error tracking + resolution
- Compliance logging (who accessed what data)

---

## Success Criteria

✅ **Functional:**
- All 5 test cases pass
- Correct routing by source
- Handler implementations work
- Results enriched with metrics
- Logging functional

✅ **Performance:**
- Execution latency < 60s per capability
- Logging < 1s (async is fine)
- No blocking I/O
- Proper timeout handling

✅ **Error Handling:**
- Invalid capability ID → error status
- Bad inputs → validation error
- Handler crash → caught and logged
- Supabase down → fallback (log to console)

✅ **Audit:**
- All executions logged to Supabase
- Metrics captured (latency, tokens, cost)
- Timestamps precise (ISO 8601)

---

## Integration with Other Units

**Unit 10 (search_capabilities):**
- search() returns list of capabilities
- User picks one
- Call execute_capability(picked_id, inputs)

**Unit 12 (Sales Plugin wiring):**
- Anthropic plugin installed locally
- execute_capability routes CAP-001, CAP-003 to it

**Unit 13 (Orchestrator):**
- Orchestrator chains capabilities
- execute_capability called by Orchestrator._execute_stage()
- Results flow to next stage

---

## Deployment

**Sep 17-18 (Phase 1A):**
1. Implement execute_capability() in openwork_mcp_tools.py
2. Test all 5 test cases
3. Verify logging to Supabase
4. If all pass → proceed to Unit 12

**Code location:** `_MCP/openwork_mcp_tools.py`

**Dependencies:**
- neo4j-driver (read capability metadata)
- supabase-py (write to audit log)
- anthropic plugin (for CAP-001, CAP-003)
- librarian-mcp (for CAP-401)

---

## Validation Checklist

Before marking Unit 11 complete:

- [ ] All 5 test cases pass
- [ ] Correct routing by source
- [ ] Handler implementations working
- [ ] Metrics captured (latency, tokens, cost)
- [ ] Logging to Supabase working
- [ ] Error handling + graceful fallback
- [ ] Latency < 60s per execution
- [ ] Code reviewed
- [ ] Unit 12 ready (Sales Plugin wiring)

---

**Status:** Ready for implementation (Sep 17-18)  
**Est. time:** 45 min  
**Blockers:** None (Unit 10 complete, handlers designed)

