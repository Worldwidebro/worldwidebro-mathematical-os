---
title: "Phase 2a Systems Wiring Checklist (Oct 2026)"
id: PHASE-2A-WIRING-CHECKLIST
authority: CP-001, CP-027, CP-032, CP-050
phase: Phase 2a (Oct 2026, Weeks 1-4)
updated: 2026-09-17
---

[[STARTHERE]] | [[20-DECISIONS/PHASE-2-RESEARCH-TO-REVENUE-ROADMAP]]

# Phase 2a Systems Wiring Checklist

**Goal:** Wire all agents, skills, tools, capabilities, and logic layers into a single discoverable, routable system.

**Timeline:** Oct 1-31, 2026 (4 weeks)  
**Team:** 2 engineers, 1 DevOps  
**Outcome:** Full system awareness—no scattered pieces, every agent useful and discoverable

---

## Week 1: Discovery & Registries

### Task 1.1: Link All READMEs to Integration Master
**Owner:** DevOps  
**Time:** 4 hours

- [ ] Add to every README.md top navigation:
  ```markdown
  [[_MCP/SYSTEMS-INTEGRATION-MASTER|← Integration Master]] | [[_REGISTRIES/CANONICAL/MASTER_DISCOVERY_INDEX.yaml|Discovery Index]]
  ```
- [ ] This creates backlink awareness across all 2,273 README files
- [ ] Use sed script: `_CLI/add-integration-links.sh`
- [ ] Test: 50 random READMEs to confirm links render

**Verification:** Every README has Integration Master backlink

---

### Task 1.2: Auto-Generate Agent Registry (265 Remaining Agents)
**Owner:** Engineer #1  
**Time:** 6 hours

**Script:** `_CLI/tag-agents.sh`

```bash
#!/bin/bash
# Read all 275 agents
# Extract: id, name, description from metadata
# Infer: domain (from filename)
# Assign: default logic layers (by domain)
# Assign: autonomy levels (default L1, override for known-good agents)
# Output: AGENT_REGISTRY.yaml entries

cd .claude/agents

for agent_file in *.md; do
  # Parse frontmatter
  id=$(grep "^id:" "$agent_file" | cut -d: -f2 | xargs)
  name=$(head -5 "$agent_file" | grep "^#" | sed 's/^# //' | head -1)
  description=$(grep "^description:" "$agent_file" | cut -d: -f2- | xargs)
  
  # Infer domain (e.g., engineering-* → 16-AGENTS)
  if [[ $agent_file =~ ^engineering ]]; then domain="16-AGENTS"; fi
  if [[ $agent_file =~ ^business ]]; then domain="01-IDENTITY"; fi
  if [[ $agent_file =~ ^design ]]; then domain="34-PRODUCT"; fi
  if [[ $agent_file =~ ^research ]]; then domain="42-RESEARCH-INTELLIGENCE"; fi
  if [[ $agent_file =~ ^marketing ]]; then domain="30-REVENUE"; fi
  if [[ $agent_file =~ ^academic ]]; then domain="37-RESEARCH"; fi
  
  # Default logic layers (by domain)
  case "$domain" in
    16-AGENTS) logic_layers="[LOGIC-049, LOGIC-050, LOGIC-067]" ;;
    01-IDENTITY) logic_layers="[LOGIC-001, LOGIC-049, LOGIC-061]" ;;
    34-PRODUCT) logic_layers="[LOGIC-019, LOGIC-045, LOGIC-049]" ;;
    42-RESEARCH-INTELLIGENCE) logic_layers="[LOGIC-007, LOGIC-037, LOGIC-045]" ;;
    30-REVENUE) logic_layers="[LOGIC-061, LOGIC-065, LOGIC-066]" ;;
    37-RESEARCH) logic_layers="[LOGIC-007, LOGIC-025, LOGIC-037]" ;;
    *) logic_layers="[LOGIC-049]" ;;
  esac
  
  # Generate YAML entry
  cat >> _REGISTRIES/CANONICAL/AGENT_REGISTRY.yaml << AGENT_EOF

  agent_${id}:
    id: agent-${id}
    name: "${name}"
    file_path: .claude/agents/${agent_file}
    description: "${description}"
    domain: "${domain}"
    logic_layers: ${logic_layers}
    control_planes: [CP-009]  # TODO: Set from logic_layers
    capabilities: []  # TODO: Extract from description
    required_skills: []  # TODO: Extract from description
    required_tools: []  # TODO: Extract from description
    required_mcps: []  # TODO: Extract from description
    autonomy_level: L1  # TODO: Override for known-good agents
    trustworthiness_score: 0.85  # TODO: Score after testing
    cost_per_use_usd: 1.00  # TODO: Calculate from model + context
    expected_duration_minutes: 45  # TODO: Profile from test runs
    success_rate_percent: 80  # TODO: Track from production
    last_verified: 2026-10-01
    sectors_applicable: []  # TODO: Determine
    ventures_deployed: []  # TODO: Track

AGENT_EOF
done
```

Steps:
- [ ] Write tag-agents.sh (if not exists)
- [ ] Run script: generates 265 agent entries
- [ ] Manual review: 50 agents (spot check for accuracy)
- [ ] Create override file: `AGENT_REGISTRY_OVERRIDES.yaml` (trustworthiness, autonomy level, capabilities)
- [ ] Merge overrides into main registry
- [ ] Test: Query 20 random agents by logic layer

**Verification:** All 275 agents in AGENT_REGISTRY.yaml with auto-generated metadata

---

### Task 1.3: Create Skill Registry (30+ Skills)
**Owner:** Engineer #2  
**Time:** 4 hours

**Script:** `_CLI/tag-skills.sh`

Search patterns:
```bash
find . -path "*/.claude/skills/*" -name "SKILL.md" -o \
       -path "*/src/skills/*" -name "*.js" -o \
       -path "*/.agents/*" -name "*.md" | head -30
```

For each skill:
- [ ] Extract: id, name, location, description
- [ ] Infer: which agents use it (grep agent file names)
- [ ] Assign: logic layers (manual)
- [ ] Assign: I/O schema (manual)
- [ ] Create: SKILL_REGISTRY.yaml entry

Expected skills (30+):
- Gitnexus (6 skills: debugging, refactoring, exploring, impact-analysis, guide, cli)
- Career-Ops (1 skill)
- Google-Maps-Scraper (1 skill)
- Dashboard-Builder (1 skill)
- Venture-Auditor (1 skill)
- Stripe-Integrator (1 skill)
- Plus 18+ more to discover

**SKILL_REGISTRY.yaml template:**
```yaml
skill:
  id: skill-gitnexus-debugging
  name: "GitNexus Debugging"
  location: worldwidebro-venture-portal/.claude/skills/gitnexus/gitnexus-debugging/
  agent_ids: [agent-backend-architect-001, agent-gitnexus-debugger-001]
  logic_layers: [LOGIC-049, LOGIC-050, LOGIC-051]
  input_schema: 
    file_path: string
    error_message: string
    context: object
  output_schema:
    diagnosis: string
    fix_plan: array
    code_changes: array
  success_rate_percent: 89
  last_verified: 2026-10-01
```

**Verification:** All 30+ skills discoverable and linked to agents

---

### Task 1.4: Create Tool Gateway Registry (20+ MCPs)
**Owner:** DevOps  
**Time:** 3 hours

**Tool Gateway Template:**
```yaml
tool:
  id: tool-neo4j-query-001
  name: "Neo4j Cypher Query"
  mcp: neo4j
  endpoint: bolt://100.87.214.70:7687
  risk_level: READ  # READ, WRITE, HIGH-RISK
  required_permissions: [graph_read, authentication_valid]
  agents_allowed: [all]
  rate_limit: 1000/hour
  cost_per_call_usd: 0.001
  timeout_seconds: 30
  fallback_tool: qdrant_semantic_search
  documentation_url: https://neo4j.com/docs/
  last_verified: 2026-10-01
```

For each of 20+ MCPs:
- [ ] Neo4j
- [ ] Qdrant
- [ ] PostgreSQL
- [ ] OmniRoute
- [ ] Make.com
- [ ] ClickUp
- [ ] Supabase
- [ ] Vercel
- [ ] Gmail
- [ ] Google Calendar
- [ ] Google Drive
- [ ] GitHub
- [ ] Stripe
- [ ] HubSpot
- [ ] Salesforce
- [ ] Slack
- [ ] Notion
- [ ] Claude Docs
- [ ] WebFetch
- [ ] WebSearch

**Verification:** All 20+ MCPs have permission rules + rate limits + cost + fallbacks

---

## Week 2: Dispatch Router Build

### Task 2.1: Design Agent Dispatch Router
**Owner:** Engineer #1  
**Time:** 4 hours

**File:** `repos/worldwidebro-agents/src/dispatcher/AgentDispatcher.js`

```javascript
class AgentDispatcher {
  constructor(agentRegistry, toolGateway, neo4jContext, omnirouteContext) {
    this.agents = agentRegistry;
    this.tools = toolGateway;
    this.graph = neo4jContext;
    this.router = omnirouteContext;
  }

  async dispatch(task) {
    // 1. PARSE: Classify task intent → logic layers
    const logicLayers = await this.classifyLogicLayers(task);
    console.log(`[DISPATCH] Task intent → Logics: ${logicLayers.join(', ')}`);

    // 2. FIND: Search agents by logic layers + domain + capability
    const candidates = this.agents.findByLogicLayers(logicLayers);
    if (!candidates.length) {
      return { error: 'NO_AGENTS_FOUND', task, logicLayers };
    }
    console.log(`[DISPATCH] Found ${candidates.length} candidate agents`);

    // 3. RANK: Score by trust, success rate, availability, cost
    const ranked = this.rankAgents(candidates, task);
    console.log(`[DISPATCH] Top candidate: ${ranked[0].name} (score: ${ranked[0].score})`);

    // 4. VALIDATE: Check tool permissions for top candidate
    const agent = ranked[0];
    const requiredTools = agent.required_tools;
    const permissions = await this.tools.checkPermissions(agent, requiredTools);
    
    if (!permissions.granted) {
      return { error: 'PERMISSION_DENIED', agent, missing_permissions: permissions.missing };
    }
    console.log(`[DISPATCH] Permissions granted for ${agent.name}`);

    // 5. ROUTE: Execute by autonomy level
    console.log(`[DISPATCH] Autonomy level: ${agent.autonomy_level}`);
    
    switch (agent.autonomy_level) {
      case 'L1':
        return this.routeToHuman(agent, task, ranked);
      case 'L2':
        return this.executeWithAssistance(agent, task, ranked);
      case 'L3':
        return this.executeAutonomous(agent, task, ranked);
      default:
        return { error: 'INVALID_AUTONOMY_LEVEL', agent };
    }
  }

  classifyLogicLayers(task) {
    // Use Claude to classify: "What logic layers does this task require?"
    // Returns: [LOGIC-xxx, LOGIC-yyy, ...]
  }

  rankAgents(candidates, task) {
    // Score by: trustworthiness, success_rate, cost, expected_duration
    // Return: sorted array of {agent, score}
  }

  routeToHuman(agent, task, ranked) {
    // Create task in ClickUp → Human review
    // Re-route if human approves
  }

  executeWithAssistance(agent, task, ranked) {
    // Execute agent with streaming output
    // Human can override at any step
  }

  executeAutonomous(agent, task, ranked) {
    // Execute agent without interruption
    // Log every decision for audit trail
  }
}
```

Steps:
- [ ] Create AgentDispatcher class skeleton
- [ ] Implement dispatch() method (5-step flow)
- [ ] Implement classifyLogicLayers() (call Claude)
- [ ] Implement rankAgents() (scoring algorithm)
- [ ] Implement routeToHuman() (ClickUp task creation)
- [ ] Implement executeWithAssistance() (streaming + human override)
- [ ] Implement executeAutonomous() (audit logging)

**Verification:** Dispatch router class compiles and methods have proper signatures

---

### Task 2.2: Wire Dispatch Router to Event Queue
**Owner:** Engineer #2  
**Time:** 4 hours

**Integration Points:**
- [ ] ClickUp webhook → new task → dispatch router
- [ ] Make.com scenario → event → dispatch router
- [ ] API endpoint → HTTP POST → dispatch router
- [ ] Scheduled cron job → check queue → dispatch router

**Event Queue Storage:** PostgreSQL `event_queue` table
```sql
CREATE TABLE event_queue (
  id UUID PRIMARY KEY,
  task_id VARCHAR,
  task_type VARCHAR,
  task_data JSONB,
  status VARCHAR (pending/dispatched/executing/complete/failed),
  assigned_agent_id VARCHAR,
  autonomy_level VARCHAR,
  created_at TIMESTAMP,
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  result JSONB,
  error JSONB,
  audit_trail JSONB
);
```

Steps:
- [ ] Create event queue table (if not exists)
- [ ] Build webhook handler for ClickUp
- [ ] Build webhook handler for Make.com
- [ ] Build HTTP API endpoint (POST /dispatch)
- [ ] Build cron job processor (poll queue every 5 min)
- [ ] Add logging to all entry points
- [ ] Test: 10 tasks from each entry point

**Verification:** Tasks from all 4 entry points successfully hit dispatch router

---

### Task 2.3: Test Dispatch Router (10-Agent Sample Set)
**Owner:** Engineer #1  
**Time:** 6 hours

Test matrix (10 test scenarios):

| Scenario | Agent | Task | Logics | Autonomy | Expected |
|----------|-------|------|--------|----------|----------|
| 1 | Business Strategist | "Market analysis for RE-001" | LOGIC-001, LOGIC-049, LOGIC-061 | L1 | Escalate to human |
| 2 | Backend Architect | "Design Neo4j schema" | LOGIC-025, LOGIC-049 | L2 | Execute with review gate |
| 3 | Research Discovery | "Find papers on semantic routing" | LOGIC-007, LOGIC-037 | L3 | Autonomous execution |
| 4 | Appointment Setter | "Schedule call at 2 PM tomorrow" | LOGIC-067 | L3 | Auto-schedule |
| 5 | Deal Closer | "Send contract to customer" | LOGIC-061, LOGIC-065 | L2 | Review before send |
| 6 | Douyin Strategist | "Plan Q1 campaign" | LOGIC-019, LOGIC-049 | L1 | Escalate to human |
| 7 | Healthcare Compliance | "Audit PHI handling in code" | LOGIC-049, LOGIC-050 | L1 | Escalate to legal |
| 8 | Data Consolidation | "Update dashboard with today's revenue" | LOGIC-013, LOGIC-045 | L3 | Autonomous |
| 9 | GitNexus Debugger | "Fix TypeScript error in component" | LOGIC-049, LOGIC-067 | L2 | Code review before merge |
| 10 | Obsidian Sync (Phase 2c) | "Sync Obsidian to Neo4j" | LOGIC-025, LOGIC-031 | L2 | Conflict resolution review |

For each scenario:
- [ ] Create test task in ClickUp
- [ ] Trigger dispatch
- [ ] Verify: correct agent selected
- [ ] Verify: correct autonomy level gate
- [ ] Verify: result logged to PostgreSQL
- [ ] Verify: audit trail complete

**Verification:** All 10 scenarios execute correctly with proper routing and autonomy gates

---

## Week 3: Capability & Research Routing

### Task 3.1: Extend Capability Registry
**Owner:** Engineer #2  
**Time:** 4 hours

Update `14-CAPABILITIES/README.md` and create `capability-registry.yaml`:

```yaml
capability:
  id: CAP-001-semantic-routing
  name: "Semantic Routing"
  description: "Route requests by semantic similarity using embeddings"
  domain: 34-PRODUCT
  logic_layers: [LOGIC-045, LOGIC-046, LOGIC-047]
  control_planes: [CP-008]
  agents_executing: [agent-backend-architect-001, agent-ai-router-001]
  required_mcps: [neo4j, qdrant]
  repositories: [worldwidebro-agents/routing, company-brain/context-assembly]
  research_sources: 
    - arXiv:2305.xxxxx
    - papers-with-code.com/semantic-routing
  ventures_using:
    - venture_id: LT-005
      deployment_date: 2026-09-15
      revenue_impact_monthly: 2000
  total_revenue_impact_annual: 24000
  readiness_score: 0.92
  last_verified: 2026-09-17
```

Steps:
- [ ] Map 300+ capabilities from `14-CAPABILITIES/solutions/CAP-*.md`
- [ ] For each capability:
  - [ ] Extract: id, name, description
  - [ ] Assign: logic layers (manual)
  - [ ] Assign: control planes
  - [ ] List: agents executing it
  - [ ] List: tools required
  - [ ] List: research sources
  - [ ] List: ventures deployed
  - [ ] Calculate: total revenue impact
- [ ] Create: capability-registry.yaml with all 300+ entries
- [ ] Wire to dispatch router: capability requests can find matching agents

**Verification:** All 300+ capabilities discoverable and linked to agents + ventures

---

### Task 3.2: Build Capability Resolver
**Owner:** Engineer #1  
**Time:** 4 hours

**File:** `repos/worldwidebro-agents/src/resolver/CapabilityResolver.js`

```javascript
class CapabilityResolver {
  constructor(capabilityRegistry, agentRegistry, ventureRegistry) {
    this.capabilities = capabilityRegistry;
    this.agents = agentRegistry;
    this.ventures = ventureRegistry;
  }

  async resolve(need) {
    // Input: venture need (string description)
    // Output: [matching capabilities + agents + revenue impact + readiness]

    // 1. Classify need → required capabilities
    const requiredCapabilities = await this.classifyNeed(need);

    // 2. Find matching capabilities
    const matches = this.capabilities.findByName(requiredCapabilities);

    // 3. For each match, find agents + cost + revenue impact
    const solutions = matches.map(cap => ({
      capability_id: cap.id,
      name: cap.name,
      agents: this.agents.findByCapability(cap.id),
      cost_to_deploy: this.estimateCost(cap),
      revenue_impact_annual: cap.total_revenue_impact_annual,
      readiness_score: cap.readiness_score,
      time_to_deploy_days: this.estimateTime(cap),
      ventures_already_using: cap.ventures_using,
    }));

    // 4. Rank by: readiness, ROI, time-to-deploy
    return solutions.sort((a, b) => {
      const roiA = a.revenue_impact_annual / (a.cost_to_deploy || 1);
      const roiB = b.revenue_impact_annual / (b.cost_to_deploy || 1);
      return roiB - roiA;  // Highest ROI first
    });
  }

  classifyNeed(need) {
    // Use Claude: "What capabilities does this venture need?"
    // Returns: [CAP-001, CAP-045, CAP-089, ...]
  }

  estimateCost(capability) {
    // Sum cost of all agents + tools required
  }

  estimateTime(capability) {
    // Based on readiness_score and complexity
  }
}
```

Steps:
- [ ] Create CapabilityResolver class
- [ ] Implement resolve() method (need → capabilities + agents + revenue)
- [ ] Implement classifyNeed() (Claude classification)
- [ ] Implement estimateCost() (agent + tool cost sum)
- [ ] Implement estimateTime() (readiness-based estimation)
- [ ] Wire to VEX dashboard: show "Recommended capabilities for LT-005"
- [ ] Test: 5 capability discovery workflows

**Verification:** CapabilityResolver successfully matches venture needs to capabilities + agents

---

### Task 3.3: Wire Research to Agent Deployment
**Owner:** Engineer #2  
**Time:** 3 hours

**Flow:** Research paper → Capability → Agent → Venture → Revenue

Steps:
- [ ] Create research-to-capability mapping (manual, first 20 papers)
  ```yaml
  research_mapping:
    paper_id: arXiv:2305.xxxxx
    paper_title: "Semantic Routing for LLMs"
    capability_enabled: CAP-001-semantic-routing
    evidence_level: VALIDATED_RESULT (level 8 of 11)
    agents_implementing: [agent-backend-architect-001]
    ventures_deployed: [LT-005]
    revenue_impact: +$2K/month
  ```
- [ ] Wire research discovery agent → automatically finds new papers
- [ ] Wire verification agent → validates against capabilities
- [ ] Wire adoption agent → recommends WATCH/PILOT/ADOPTED
- [ ] Test: Full research → capability → deployment flow (end-to-end)

**Verification:** Research discovery agent successfully surfaces adoptable capabilities

---

## Week 4: Testing & Documentation

### Task 4.1: End-to-End Integration Testing (50 Workflows)
**Owner:** Both engineers  
**Time:** 6 hours

Test categories (10 per category × 5 categories):

**Category 1: Dispatch Routing (10 tests)**
- [ ] L1 task escalates to human ✓
- [ ] L2 task executes with review gate ✓
- [ ] L3 task executes autonomously ✓
- [ ] Agent permission denied → fallback ✓
- [ ] Unknown task type → "no agents found" error ✓
- [ ] High-risk task → escalate ✓
- [ ] Cost estimate accurate ✓
- [ ] Latency < 2 seconds ✓
- [ ] Audit trail complete ✓
- [ ] Retry logic works on tool failure ✓

**Category 2: Capability Resolution (10 tests)**
- [ ] Venture need → matching capabilities ✓
- [ ] ROI ranking correct ✓
- [ ] Readiness score influences sorting ✓
- [ ] Cost estimation includes all agents ✓
- [ ] Time-to-deploy realistic ✓
- [ ] Already-deployed capabilities show revenue history ✓
- [ ] Can recommend 3+ alternative solutions ✓
- [ ] Handles "no matching capabilities" gracefully ✓
- [ ] Suggests custom implementation path if needed ✓
- [ ] Saves recommendation to audit log ✓

**Category 3: Skill Execution (10 tests)**
- [ ] Skill discoverable by agent ✓
- [ ] Skill callable via dispatch router ✓
- [ ] Input schema validated ✓
- [ ] Output schema produced ✓
- [ ] Success/failure tracked ✓
- [ ] Latency < expected_duration ✓
- [ ] Cost accurate ✓
- [ ] Error handling works ✓
- [ ] Can chain multiple skills ✓
- [ ] Rollback on failure works ✓

**Category 4: Tool Gateway (10 tests)**
- [ ] Rate limits enforced ✓
- [ ] Cost deducted from venture budget ✓
- [ ] Permission denied for unauthorized agents ✓
- [ ] Fallback tool works when primary fails ✓
- [ ] Timeout handled gracefully ✓
- [ ] All 20+ MCPs accessible ✓
- [ ] Authentication refreshed ✓
- [ ] Audit log complete for all calls ✓
- [ ] Cost tracking accurate ✓
- [ ] Tool health status tracked ✓

**Category 5: Research → Capability → Revenue (10 tests)**
- [ ] Discovery agent finds relevant papers ✓
- [ ] Verification agent validates claims ✓
- [ ] Synthesis agent connects related papers ✓
- [ ] Adoption agent makes recommendations ✓
- [ ] Capability deployment tracked ✓
- [ ] Revenue impact measured ✓
- [ ] Feedback loop captures outcomes ✓
- [ ] Learning improves future decisions ✓
- [ ] Can trace from paper to $revenue ✓
- [ ] Attribution model accurate ✓

**Run Tests:**
```bash
npm test -- --testPathPattern="integration" --verbose
```

Expected: 45+ passing, <5 flaky (ok for this phase)

**Verification:** 50/50 integration tests passing

---

### Task 4.2: Documentation & Wikis
**Owner:** Both engineers  
**Time:** 4 hours

- [ ] Update `_MCP/SYSTEMS-INTEGRATION-MASTER.md` with actual API signatures
- [ ] Document `AGENT_REGISTRY.yaml` format (done, but add examples)
- [ ] Document `SKILL_REGISTRY.yaml` format
- [ ] Document `TOOL_GATEWAY_REGISTRY.yaml` format
- [ ] Document `capability-registry.yaml` format
- [ ] Create `_DOCS/DISPATCH_ROUTER_GUIDE.md` (how to use dispatch router)
- [ ] Create `_DOCS/CAPABILITY_RESOLVER_GUIDE.md` (how to find capabilities)
- [ ] Create `_DOCS/RESEARCH_TO_REVENUE_GUIDE.md` (end-to-end flow)
- [ ] Link all new docs to `_DOCS/README.md`
- [ ] Update all 2,273 README.md backlinks (if not done in Week 1)

**Verification:** All documentation complete and discoverable

---

### Task 4.3: Phase 2b Planning (Capability Routing)
**Owner:** Engineer #1  
**Time:** 2 hours

- [ ] Review Phase 2a results
- [ ] Document what worked, what didn't
- [ ] Create Phase 2b plan for Nov 2026 (Capability Routing Deep Dive)
- [ ] Estimate: additional 2 weeks for enterprise capability deployment
- [ ] Plan: integration with VEX dashboard for venture capability recommendations

**Verification:** Phase 2b plan documented and ready for Oct 31 handoff

---

## Success Criteria (Phase 2a Complete)

✅ All 275 agents discoverable by logic layer + control plane  
✅ All 30+ skills callable by dispatch router  
✅ All 20+ tools have permission rules + rate limits + cost tracking  
✅ Dispatch router routing 80%+ of tasks correctly  
✅ L1 tasks escalating appropriately  
✅ L2 tasks executing with review gates  
✅ L3 tasks executing autonomously (90%+ success)  
✅ All 300+ capabilities mapped to agents + ventures + revenue  
✅ Capability resolver matching venture needs  
✅ Research discovery → capability → deployment working end-to-end  
✅ 50/50 integration tests passing  
✅ Zero scattered pieces—100% discoverability  
✅ Complete audit trail for all decisions  

---

## Budget & Resources

| Role | Hours | Rate | Cost |
|------|-------|------|------|
| Engineer #1 (dispatch, resolver, testing) | 40 | $75/h | $3,000 |
| Engineer #2 (registries, integration, skills) | 40 | $75/h | $3,000 |
| DevOps (infrastructure, scripts, CI/CD) | 20 | $85/h | $1,700 |
| **TOTAL** | **100** | | **$7,700** |

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Agent metadata incomplete | Dispatch quality | Auto-generation + manual spot-check + test |
| Tool failures block dispatch | System reliability | Fallback tools + graceful degradation |
| Permission model too strict | Blocks useful agents | Start permissive, tighten based on use |
| Performance < 2s latency | User experience | Cache agent rankings + profile hot paths |
| Autonomous L3 mistakes | Trust erosion | Require confidence threshold + audit trail |

---

**Status:** Ready to start Oct 1, 2026  
**Next:** Kick-off Phase 2a Week 1  
**Owner:** Tech Lead + Team

