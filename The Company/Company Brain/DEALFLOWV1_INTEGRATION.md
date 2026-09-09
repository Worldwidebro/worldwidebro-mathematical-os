# DealFlowV1 ↔ Agent OS Integration

**Repo:** https://github.com/Worldwidebro/DealFlowV1  
**Purpose:** Pipeline visibility + deal tracking  
**Integration:** Orchestrator → DealFlow (every agent execution creates/updates deal)

---

## THE WIRING

```
Orchestrator executes task
    ↓
Result: {agent_id, task, outcome, confidence, cost}
    ↓
DealFlow webhook: create_or_update_deal
    {
      "venture": "OPS-001",
      "stage": "prospecting" | "proposal" | "closed_won" | "closed_lost",
      "amount": 2500,
      "agent_id": "AGT-004",
      "decision_confidence": 0.91,
      "last_activity": "agent_call",
      "next_step": "send_contract"
    }
    ↓
DealFlow pipeline updated
    ↓
Growth OS queries DealFlow API
    ↓
Dashboard shows: "$2,500 in prospecting, $1,200 in proposal"
```

**Add to orchestrator on Sep 12:**

```python
# In execution_registry.py:

def log_to_dealflow(agent_id, task, result):
    """Send execution result to DealFlow"""
    
    if result.venture_id:
        payload = {
            "venture": result.venture_id,
            "stage": result.deal_stage,
            "amount": result.deal_amount,
            "agent_id": agent_id,
            "decision_confidence": result.confidence,
            "last_activity": "agent_execution",
            "next_step": result.recommended_next_step
        }
        
        requests.post(
            "http://dealflow:3000/api/deals/update",
            json=payload
        )
```

**Result:** Every agent execution = pipeline update, visible in Growth OS + DealFlow real-time.

