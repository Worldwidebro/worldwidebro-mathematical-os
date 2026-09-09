# CALLCENTER ↔ AGENT OS INTEGRATION (Sep 12-19)

**Current state:** Callcenter OS exists (VAPI-based) but routes calls manually  
**Target state:** Inbound calls → Orchestrator routes → Agent handles → Live conversation

---

## THE INBOUND LOOP (Missing from Path B)

```
Inbound Call (Callcenter OS)
    ↓
Intent Extraction ("I need warehouse staffing")
    ↓
Webhook: route_inbound_call(intent, caller_context)
    ↓
Orchestrator receives:
  - intent: "find_candidates"
  - responsibility_id: "RESP-001"
  - caller: {name, company, role, budget, timeline}
    ↓
Orchestrator queries Neo4j:
  "Who provides RESPONSIBILITY (find_candidates)?"
  Response: AGT-004 (Sales Agent) + AGT-020 (Research)
    ↓
Orchestrator returns:
  - agent_id: "AGT-004"
  - context: {
      candidates: [from AGT-020 search],
      similar_deals: [from Neo4j history],
      script: [call script from ClickUp],
      fee: "$2,500 placement"
    }
    ↓
Callcenter OS connects call to: /api/agent-calls/AGT-004
    ↓
AGT-004 Agent (running on server) receives:
  - caller_context
  - real-time call audio stream
    ↓
AGT-004 responds:
  - "Hi, I found 3 candidates. Here's why they're a fit..."
  - Reads from real-time context (candidates, similar deals)
  - Quotes fee
  - Collects caller acceptance
    ↓
Call recorded + stored
    ↓
Execution logged:
  - execution_registry.jsonl: {agent: AGT-004, duration: 12min, result: "placement_quoted"}
  - Neo4j: Caller → OPPORTUNITY relationship created
  - ClickUp: Task created "Follow up: Candidate review"
  - Growth OS: "+$2,500 pipeline"
```

---

## IMPLEMENTATION (Sep 12-19)

### Step 1: Intent Classifier (Sep 12, 1 hour)
**File:** `_MCP/intent_classifier.py`

```python
class IntentClassifier:
    """Extract responsibility_id from caller speech"""
    
    def classify(self, caller_intent_text, caller_company=None):
        """
        Input: "I need warehouse staff"
        Output: {responsibility_id: "RESP-001", confidence: 0.95}
        """
        # Map common intents to responsibilities:
        intent_map = {
            "staff|hire|recruit": "RESP-001",  # find_candidates
            "construction|build": "RESP-002",  # assess_site
            "deliver|logistics": "RESP-003",  # route_shipment
            "consult|advise": "RESP-004",     # provide_guidance
        }
        
        for pattern, resp_id in intent_map.items():
            if re.search(pattern, caller_intent_text, re.I):
                return {"responsibility_id": resp_id, "confidence": 0.95}
        
        return {"responsibility_id": None, "confidence": 0}
```

**Wiring:** Callcenter OS IVR calls this on call arrival

### Step 2: Orchestrator Webhook (Sep 12, 2 hours)
**File:** `_MCP/fastmcp_agent_orchestrator.py` (add endpoint)

```python
@mcp.tool()
def route_inbound_call(intent_text: str, caller_name: str, caller_company: str, budget: float = None):
    """Route inbound call to best agent"""
    
    # 1. Classify intent
    classifier = IntentClassifier()
    intent = classifier.classify(intent_text, caller_company)
    
    if not intent['responsibility_id']:
        return {
            "error": "Unable to classify intent",
            "escalate_to": "human"
        }
    
    # 2. Query Neo4j for agent
    orch = AgentOrchestrator(...)
    agents = orch.find_agents_for_responsibility(intent['responsibility_id'])
    best_agent = agents[0]  # Ranked by success_rate
    
    # 3. Get context for agent
    context = orch.get_context_for_agent(
        agent_id=best_agent.agent_id,
        caller_company=caller_company,
        budget=budget
    )
    
    # 4. Return routing decision
    return {
        "agent_id": best_agent.agent_id,
        "agent_name": best_agent.name,
        "endpoint": f"/api/agent-calls/{best_agent.agent_id}",
        "context": context,
        "confidence": intent['confidence']
    }
```

**Wiring:** Callcenter OS calls this endpoint on call arrival

### Step 3: Agent Call Handler (Sep 13, 4 hours)
**File:** `_MCP/agent_call_handler.py`

```python
class AgentCallHandler:
    """Receive live call, route to agent, stream responses"""
    
    async def handle_call(self, agent_id, caller_context, audio_stream):
        """
        Receive inbound call stream
        Send agent responses back to caller
        Log execution
        """
        
        # 1. Get agent instance
        agent = self.registry.get_agent(agent_id)
        
        # 2. Create task from caller context
        task = Task(
            id=f"CALL-{uuid.uuid4()}",
            objective=caller_context['intent'],
            caller=caller_context,
            audio_stream=audio_stream
        )
        
        # 3. Execute agent with real-time context
        result = await agent.execute(task, context={
            'live_call': True,
            'caller_data': caller_context,
            'similar_deals': self.get_similar_deals(agent_id, caller_context),
            'script': self.get_call_script(agent_id)
        })
        
        # 4. Stream response back to caller
        yield result.response_text
        
        # 5. Log execution
        self.log_call_execution(agent_id, task, result)
        
        # 6. Update growth OS
        self.update_growth_os(agent_id, result)
```

**Wiring:** Callcenter OS streams call audio to this handler

### Step 4: Call Execution Logger (Sep 13, 1 hour)
**File:** `_MCP/call_execution_logger.py`

```python
class CallExecutionLogger:
    def log_call(self, agent_id, caller, call_duration, result, audio_path):
        """Log to execution_registry + Neo4j"""
        
        # 1. Log to jsonl
        record = {
            "run_id": f"CALL-{uuid.uuid4()}",
            "agent_id": agent_id,
            "type": "inbound_call",
            "caller": {
                "name": caller['name'],
                "company": caller['company'],
                "budget": caller.get('budget')
            },
            "duration_seconds": call_duration,
            "result": result.status,
            "confidence": result.confidence,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        with open("_REGISTRIES/execution_registry.jsonl", 'a') as f:
            f.write(json.dumps(record) + '\n')
        
        # 2. Create Neo4j relationship
        self.neo4j.run("""
            MATCH (a:AGENT {id: $agent_id})
            MERGE (c:CALLER {name: $caller_name, company: $company})
            CREATE (a)-[e:HANDLED_CALL]->(c)
            SET e.result = $result, e.timestamp = $timestamp
        """, agent_id=agent_id, caller_name=caller['name'], 
            company=caller['company'], result=result.status, 
            timestamp=datetime.utcnow().isoformat())
        
        # 3. Create ClickUp task
        self.clickup.create_task(
            name=f"Follow-up: {caller['company']} — {result.status}",
            description=f"Call with {caller['name']} at {caller['company']}",
            custom_fields={
                "agent": agent_id,
                "caller_budget": caller.get('budget'),
                "next_step": result.next_action
            }
        )
        
        # 4. Update Growth OS
        self.growth_os.update_pipeline(
            venture="OPS-001",  # or dynamic based on agent
            event="call_received",
            caller_company=caller['company'],
            budget=caller.get('budget'),
            result=result.status
        )
```

---

## WIRING DIAGRAM (How Callcenter ↔ Orchestrator Connect)

```
CALLCENTER OS (VAPI)
    ├─ Inbound call arrives
    ├─ Extract caller: {name, company, intent, budget}
    │
    └─→ HTTP POST to: /api/route-inbound-call
        {intent_text, caller_name, caller_company, budget}
            ↓
        ORCHESTRATOR KERNEL
            ├─ Intent Classifier: "staff" → RESP-001
            ├─ Query Neo4j: "Who handles RESP-001?" → AGT-004
            ├─ Get context: candidates, similar deals, script
            └─→ HTTP 200: {agent_id: "AGT-004", endpoint: "/api/agent-calls/AGT-004", context: {...}}
                ↓
        CALLCENTER OS
            ├─ WebSocket connect to: /ws/agent-calls/AGT-004
            ├─ Stream caller audio to agent
            └─→ Receive agent responses, play to caller
                ↓
        AGENT CALL HANDLER
            ├─ Receive audio stream
            ├─ Run AGT-004.execute(task, real_time_context)
            ├─ Stream responses back: "Found 3 candidates..."
            └─→ Log to execution_registry.jsonl + Neo4j
                ↓
        GROWTH OS + CLICKUP
            ├─ Update pipeline: "+$2,500 (OPS-001, AGT-004 handled)"
            └─ Create task: "Follow-up: Candidate review"
```

---

## CALLCENTER FILES (Sep 12-19)

```
_MCP/
├── intent_classifier.py                (classify caller intent → responsibility)
├── agent_call_handler.py               (receive call → stream responses)
├── call_execution_logger.py            (log to jsonl + Neo4j + ClickUp + Growth OS)
├── fastmcp_agent_orchestrator.py       (ADD endpoint: route_inbound_call)
└── websocket_call_router.py            (OPTIONAL: WebSocket for live call streams)

_INFRASTRUCTURE/
├── callcenter-config.yaml              (VAPI → Orchestrator webhook)
└── call-system-tests.py                (simulate inbound calls, test routing)
```

---

## SUCCESS CRITERIA (Sep 19)

✅ Inbound call → Intent classified → Agent routed (< 3 seconds)  
✅ Agent receives live caller context (candidate list, pricing, script)  
✅ Agent speaks to caller with full information  
✅ Call logged: execution_registry.jsonl + Neo4j + ClickUp + Growth OS  
✅ Next agent queries call history → better context → better decisions

---

## EXAMPLE: OPS-001 PLACEMENT CALL

```
CALLER: "Hi, I'm looking for warehouse staff in Charlotte"
↓
CALLCENTER: Classifies as RESP-001 (find_candidates)
↓
ORCHESTRATOR: Routes to AGT-004 (Sales Agent)
↓
AGT-004 (via call handler) receives context:
  {
    "caller": "John Smith, ABC Logistics",
    "budget": "$18/hr base",
    "candidates": [
      {name: "James B.", experience: "5yr", wage_expectation: "$17/hr", available: "immediately"},
      {name: "Maria G.", experience: "3yr", wage_expectation: "$16/hr", available: "2 weeks"},
      {name: "DeShawn K.", experience: "8yr", wage_expectation: "$19/hr", available: "negotiable"}
    ],
    "similar_deals": [
      {company: "XYZ Shipping", placement_date: "3 months ago", success: true}
    ],
    "script": "Hi John! I found 3 qualified candidates..."
  }
↓
AGT-004 speaks: "Hi John! I found 3 qualified candidates...
  James is available immediately at $17/hr with 5 years experience.
  Maria is available in 2 weeks at $16/hr.
  DeShawn has 8 years experience, asking $19/hr.
  
  Based on similar placements, James is your best fit.
  That's a $2,500 placement fee. Want to move forward?"
↓
CALLER: "Yes, let's do James"
↓
EXECUTION LOGGED:
  - execution_registry.jsonl: {agent: AGT-004, type: call, result: placement_quoted}
  - Neo4j: Caller → Opportunity created
  - ClickUp: "Follow-up: Confirm James placement with John Smith"
  - Growth OS: "+$2,500 (OPS-001)"
```

---

## TIMING

- **Sep 12:** Intent classifier + orchestrator webhook (3 hours)
- **Sep 13:** Agent call handler + execution logger (5 hours)
- **Sep 14:** Integration test + call scripts (4 hours)
- **Sep 15-19:** Live call routing + monitoring

**Result:** By Sep 19, inbound calls routed to agents automatically. Revenue captured in real-time.

