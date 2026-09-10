# OPENWORK-MCP-WRAPPER-DESIGN.md
**Unit 5: OpenWork MCP Wrapper for HealthRoute Capability Discovery & Execution**

---

## OVERVIEW

OpenWork is an MCP server that enables agents to:
1. **Discover** capabilities by domain, fit score, tags, dependencies
2. **Execute** capabilities (route to correct skill/MCP/tool)
3. **Compose** workflows (multi-step orchestration)
4. **Track** execution, costs, results

**Architecture:**
```
Agent Query
    ↓
OpenWork MCP
├── search_capabilities() → [CAP-001, CAP-003, ...]
├── execute_capability(CAP-001) → Route to Anthropic Sales Plugin
├── compose_workflow(WFL-001) → Chain CAP-001 → CAP-002 → CAP-003
└── track_execution() → Store result + cost in Supabase
    ↓
Result to Agent
```

---

## MCP SERVER DESIGN

### Server Interface (3 core tools)

```python
class OpenWorkMCP:
    """
    OpenWork MCP server for HealthRoute capability routing.
    Implements Model Context Protocol for agent-native capability discovery.
    """
    
    def search_capabilities(
        self,
        domain: str = None,
        fit_gte: int = 80,
        tags: List[str] = None,
        requires_mcp: str = None,
        vertical: str = None
    ) -> List[CapabilityEntry]:
        """
        Search Capability Registry by multiple dimensions.
        
        Examples:
            - search_capabilities(domain='sales')
            - search_capabilities(fit_gte=80, vertical='medical')
            - search_capabilities(tags=['hipaa', 'compliance'])
            - search_capabilities(requires_mcp='MCP-SUPABASE')
        
        Returns: List of matching capabilities with metadata
        """
        pass
    
    def execute_capability(
        self,
        capability_id: str,
        inputs: Dict,
        context: Dict = None
    ) -> ExecutionResult:
        """
        Execute a capability. Routes to correct handler (Anthropic skill, MCP tool, custom).
        
        Examples:
            - execute_capability('CAP-001', {'company_name': 'WakeMed'})
            - execute_capability('CAP-003', {'call_notes': '...'})
        
        Execution flow:
            1. Lookup capability metadata
            2. Validate inputs against capability schema
            3. Route to handler (plugin, MCP, custom)
            4. Execute with timeout + error handling
            5. Log execution + cost to Supabase
            6. Return result
        
        Returns: ExecutionResult (output, latency, tokens, cost)
        """
        pass
    
    def compose_workflow(
        self,
        workflow_id: str,
        start_stage: int = 1,
        context: Dict = None
    ) -> WorkflowResult:
        """
        Execute a multi-stage workflow. Chains capabilities and passes context.
        
        Example workflow (WFL-001):
            Stage 1: CAP-001 (research) 
                → outputs: company_intel
            Stage 2: CAP-002 (call-prep)
                → inputs: company_intel
                → outputs: call_agenda, talking_points
            Stage 3: <user calls via Vapi>
            Stage 4: CAP-003 (call-summary)
                → inputs: call_transcript
                → outputs: action_items, follow_up_email
            Stage 5: CAP-004 (outreach)
                → inputs: action_items + company_intel
                → outputs: follow_up_message
        
        Returns: WorkflowResult (stage outputs, total cost, status)
        """
        pass
```

### Pseudo-Code Implementation

```python
# ============================================================================
# SEARCH CAPABILITIES
# ============================================================================

def search_capabilities(domain, fit_gte, tags, requires_mcp, vertical):
    """Query Capability Registry in Supabase + Neo4j"""
    
    # Build SQL query
    sql = """
        SELECT * FROM capabilities
        WHERE 1=1
    """
    params = []
    
    if domain:
        sql += " AND category = %s"
        params.append(domain)
    
    if fit_gte:
        sql += " AND healthroute_fit >= %s"
        params.append(fit_gte)
    
    if vertical:
        sql += " AND vertical = %s OR vertical = 'general'"
        params.append(vertical)
    
    if tags:
        # Array contains any tag
        sql += f" AND tags && %s"
        params.append(tags)
    
    if requires_mcp:
        # Neo4j: Find capabilities that depend on this MCP
        neo4j_query = """
            MATCH (c:Capability)-[:REQUIRES_MCP]->(m:MCP)
            WHERE m.id = $mcp_id
            RETURN c
        """
        neo4j_results = neo4j_execute(neo4j_query, mcp_id=requires_mcp)
        cap_ids = [r['c']['id'] for r in neo4j_results]
        sql += " AND id = ANY(%s)"
        params.append(cap_ids)
    
    # Execute
    results = supabase.query(sql, params)
    return results


# ============================================================================
# EXECUTE CAPABILITY
# ============================================================================

def execute_capability(capability_id, inputs, context):
    """Route and execute a single capability"""
    
    start_time = time.time()
    
    try:
        # 1. Lookup capability
        capability = supabase.from_('capabilities').select('*') \
            .eq('id', capability_id).single().execute()
        
        # 2. Validate inputs
        validate_inputs(inputs, capability['inputs']['required'])
        
        # 3. Route by type
        if capability['execution']['type'] == 'skill':
            result = execute_skill(capability, inputs, context)
        
        elif capability['execution']['type'] == 'mcp_tool':
            result = execute_mcp_tool(capability, inputs, context)
        
        elif capability['execution']['type'] == 'workflow':
            result = execute_workflow(capability['id'], context)
        
        else:
            raise ValueError(f"Unknown type: {capability['execution']['type']}")
        
        # 4. Calculate cost
        latency_ms = (time.time() - start_time) * 1000
        tokens_used = estimate_tokens(result, capability['execution']['model'])
        cost = cost_estimate(
            model=capability['execution']['model'],
            tokens=tokens_used
        )
        
        # 5. Log execution
        log_execution(
            capability_id=capability_id,
            inputs=inputs,
            output=result,
            latency_ms=latency_ms,
            tokens_used=tokens_used,
            cost=cost,
            status='success'
        )
        
        # 6. Return
        return ExecutionResult(
            output=result,
            latency_ms=latency_ms,
            tokens_used=tokens_used,
            cost=cost,
            status='success'
        )
    
    except Exception as e:
        latency_ms = (time.time() - start_time) * 1000
        log_execution(
            capability_id=capability_id,
            inputs=inputs,
            error=str(e),
            latency_ms=latency_ms,
            status='error'
        )
        return ExecutionResult(
            error=str(e),
            status='error'
        )


# ============================================================================
# EXECUTE SKILL (e.g., Anthropic Sales Plugin)
# ============================================================================

def execute_skill(capability, inputs, context):
    """Route to Anthropic Sales Plugin or custom skill"""
    
    skill_name = capability['skill']['name']
    
    if capability['source'] == 'anthropic':
        # Invoke Anthropic plugin directly
        # (assumes Sales Plugin is installed and configured)
        
        if skill_name == 'account-research':
            # Anthropic's built-in
            result = invoke_anthropic_skill(
                skill='account-research',
                prompt=f"Research {inputs['company_name']}"
            )
        
        elif skill_name == 'call-summary':
            result = invoke_anthropic_skill(
                skill='call-summary',
                prompt=f"Summarize call: {inputs['call_notes']}"
            )
        
        else:
            result = invoke_anthropic_skill(
                skill=skill_name,
                inputs=inputs
            )
    
    elif capability['source'] == 'custom':
        # Invoke custom skill via Claude
        result = invoke_claude_direct(
            system=capability['skill']['description'],
            user_message=format_inputs_to_prompt(inputs)
        )
    
    return result


# ============================================================================
# EXECUTE MCP TOOL
# ============================================================================

def execute_mcp_tool(capability, inputs, context):
    """Route to MCP tool (e.g., Librarian, Supabase)"""
    
    mcp_id = capability['dependencies']['mcps'][0]['mcp_id']
    
    if mcp_id == 'MCP-LIBRARIAN':
        # Invoke Librarian MCP for knowledge retrieval
        result = mcp_call(
            server='librarian',
            method='search',
            query=inputs.get('query'),
            vault_path=context.get('vault_path')
        )
    
    elif mcp_id == 'MCP-SUPABASE':
        # Invoke Supabase MCP for data operations
        result = mcp_call(
            server='supabase',
            method=inputs.get('method', 'query'),
            query=inputs.get('query'),
            table=inputs.get('table')
        )
    
    elif mcp_id == 'MCP-NEO4J':
        # Invoke Neo4j MCP for knowledge graph
        result = mcp_call(
            server='neo4j',
            method='query',
            cypher=inputs.get('cypher'),
            params=inputs.get('params', {})
        )
    
    return result


# ============================================================================
# COMPOSE WORKFLOW
# ============================================================================

def compose_workflow(workflow_id, start_stage, context):
    """Execute multi-stage workflow with context passing"""
    
    # 1. Lookup workflow definition
    workflow = get_workflow(workflow_id)
    
    # 2. Execute stages sequentially
    stage_results = {}
    workflow_context = context or {}
    
    for stage_num in range(start_stage, len(workflow['stages']) + 1):
        stage = workflow['stages'][stage_num - 1]
        
        # Get capabilities for this stage
        capabilities = stage['capabilities']
        
        # If multiple, execute in parallel (optional)
        stage_outputs = {}
        for cap_id in capabilities:
            # Pass context from previous stages
            result = execute_capability(
                capability_id=cap_id,
                inputs=workflow_context,  # Pass accumulated context
                context=workflow_context
            )
            
            stage_outputs[cap_id] = result
            
            # Merge output into workflow context for next stage
            workflow_context.update(result.output)
        
        stage_results[f"stage_{stage_num}"] = stage_outputs
    
    # 3. Return workflow result
    return WorkflowResult(
        workflow_id=workflow_id,
        stage_results=stage_results,
        final_output=workflow_context,
        total_cost=sum([r.cost for r in flatten(stage_results.values())]),
        status='success'
    )


# ============================================================================
# LOGGING & TRACKING
# ============================================================================

def log_execution(capability_id, inputs, output=None, error=None,
                  latency_ms=0, tokens_used=0, cost=0, status='success'):
    """Log execution to Supabase for audit + cost tracking"""
    
    supabase.from_('capability_executions').insert({
        'id': generate_ulid(),
        'capability_id': capability_id,
        'inputs': json.dumps(inputs),
        'output': json.dumps(output) if output else None,
        'error': error,
        'latency_ms': latency_ms,
        'tokens_used': tokens_used,
        'cost_usd': cost,
        'status': status,
        'timestamp': datetime.now().isoformat()
    }).execute()
```

---

## INTEGRATION WITH CAPABILITY REGISTRY

### Supabase Tables

```sql
-- capabilities: Machine-readable registry entries
CREATE TABLE capabilities (
    id VARCHAR PRIMARY KEY,
    ref_id VARCHAR UNIQUE,
    name VARCHAR,
    description TEXT,
    category VARCHAR,
    source VARCHAR,
    skill JSONB,
    inputs JSONB,
    outputs JSONB,
    execution JSONB,
    dependencies JSONB,
    healthroute_fit INTEGER,
    tags TEXT[],
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- capability_executions: Audit log
CREATE TABLE capability_executions (
    id ULID PRIMARY KEY,
    capability_id VARCHAR REFERENCES capabilities(id),
    inputs JSONB,
    output JSONB,
    error TEXT,
    latency_ms INTEGER,
    tokens_used INTEGER,
    cost_usd DECIMAL,
    status VARCHAR,
    timestamp TIMESTAMP
);

-- workflows: Composite capability sequences
CREATE TABLE workflows (
    id VARCHAR PRIMARY KEY,
    name VARCHAR,
    stages JSONB,
    created_at TIMESTAMP
);
```

### Neo4j Relationships

```cypher
-- Capability graph
MATCH (c:Capability {id: 'CAP-001'})
RETURN c

-- Dependency traversal
MATCH (c1:Capability)-[:REQUIRES_MCP]->(m:MCP)
MATCH (c1:Capability)-[:DEPENDS_ON]->(c2:Capability)
MATCH (w:Workflow)-[:CONTAINS]->(c:Capability)
RETURN *
```

---

## AGENT USAGE PATTERNS

### Pattern 1: Single Capability Execution

```
Agent Query: "Research WakeMed before my call"

→ OpenWork search_capabilities(domain='sales', fit_gte=80)
  ← Returns: [CAP-001 (account-research), ...]

→ OpenWork execute_capability('CAP-001', {'company_name': 'WakeMed'})
  ← Returns: Company research with intel

→ Agent presents to user
```

### Pattern 2: Workflow Composition

```
Agent Query: "Prepare for calls to my Tier-0 prospects"

→ OpenWork compose_workflow('WFL-001', start_stage=1)
  ← Stage 1: CAP-001 (research all 10 prospects)
  ← Stage 2: CAP-002 (prep for each call)
  ← Outputs: 10 call agendas ready

→ Agent: "Ready for calls. Let's start with WakeMed at 8 AM"
```

### Pattern 3: Workflow + Decision Gate

```
Agent Query: "Should we pivot to email outreach?"

→ OpenWork search_capabilities(domain='sales', tags=['conversion', 'email'])
  ← Returns: [CAP-004 (draft-outreach), CAP-005 (forecast), ...]

→ Evaluate: "We called 10 prospects → 0 interested → 80% fail rate"

→ Decision: Pivot to email (CAP-004)
  ← Execute with different value props

→ Track: Conversion rate improvement in capability_executions
```

---

## PHASE 1A IMPLEMENTATION ROADMAP

| Task | Effort | Timeline | Owner |
|------|--------|----------|-------|
| **Set up Supabase tables** | 2h | Sep 16 | DevOps |
| **Implement search_capabilities()** | 3h | Sep 16-17 | Backend |
| **Implement execute_capability()** | 4h | Sep 17-18 | Backend |
| **Implement compose_workflow()** | 3h | Sep 18-19 | Backend |
| **Wire Anthropic Sales Plugin** | 2h | Sep 17 | Backend |
| **Test with 5 capabilities** | 2h | Sep 19 | QA |
| **Deploy MCP server** | 1h | Sep 19 | DevOps |

---

## SUCCESS METRICS (Unit 5)

✅ **Design complete:** 3 core tools (search, execute, compose)  
✅ **Pseudo-code ready:** Implementation templates for Phase 1A  
✅ **Integration plan:** Supabase tables + Neo4j relationships  
✅ **Usage patterns:** 3 agent scenarios documented  

**Phase 1A Launch Ready:** Sep 16-19, 2026

---

**Unit 5 Complete:** ✅ OpenWork MCP wrapper designed  
**Next:** Unit 6 — Build orchestrator pseudo-code for multi-capability workflows (Sonnet, 20 min)

