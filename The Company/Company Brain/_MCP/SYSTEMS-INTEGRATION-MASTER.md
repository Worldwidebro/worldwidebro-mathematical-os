---
id: SYSTEMS-INTEGRATION-MASTER
title: "Systems Integration Master — Agent Dispatch, Tool Coordination, Full Awareness"
authority: [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml|CP-001, CP-027, CP-032, CP-050]]
phase: Phase 1 Complete → Phase 2 Execution Ready
updated: 2026-09-17
---

[[STARTHERE]] | [[INDEX]] | [[REALITY]] | [[ANTIGRAVITY]]

# Systems Integration Master

**Goal:** Every agent, skill, MCP, tool, capability, and research opportunity is mutually discoverable and routable. No scattered pieces. Full system awareness.

---

## INVENTORY: WHAT WE HAVE

### A. Agents (275 total)
**Location:** `.claude/agents/` (master agent library)

**Organized by Domain:**
- Academic (anthropologist, psychologist, historian, geographer, statistician, narratologist)
- Business (strategist, CFO, CMO, operations, sales, customer success)
- Engineering (architect, backend, frontend, mobile, DevOps, database, security)
- Design (UI, UX, branding, accessibility, visual storytelling, inclusive design)
- Specialized (healthcare, legal, compliance, fintech, construction, real estate)

**Sub-inventories:**
- Business venture agents: VEX portfolio (venture-portal), OmniRoute context, Neo4j awareness
- Douyin/Bilibili/Xiaohongshu/WeChat specialists (Chinese market)
- Tier-0 venture agents: OPS-001 (staffing), LT-005 (medical courier), CALLCENTER, CON-001, RE-001, LT-011
- Research agents: discovery, verification, synthesis, adoption (Phase 2 ready)

**Gap:** Agents not wired to logic layers, control planes, or capability registries.

---

### B. Skills (30+ across system)

**Primary Skills Systems:**
| System | Location | Scope | Status |
|--------|----------|-------|--------|
| **Gitnexus** | `worldwidebro-venture-portal/.claude/skills/gitnexus/` | Code exploration, debugging, refactoring, impact analysis | ✅ Ready |
| **Career-Ops** | `career-ops/.claude/skills/career-ops/` | Career consulting workflow | ✅ Ready |
| **Google Maps Scraper** | `con-001/google-maps-scraper/.claude/skills/` | Lead discovery for construction | ✅ Ready |
| **WorldwideBro Agents** | `worldwidebro-agents/src/skills/` | Agent framework, OmniRoute routing, Neo4j context | ✅ Ready |
| **Dashboard Builder** | `deliv-713/Claude/.claude/agents/dashboard-builder.md` | Analytics & metrics | ✅ Ready |
| **Venture Auditor** | `deliv-713/Claude/.claude/agents/venture-auditor.md` | Readiness assessment | ✅ Ready |

**Gap:** Skills not discoverable by agent dispatch system. No unified skill registry.

---

### C. MCPs & Tools (20+ live)

**Active MCPs:**
- Neo4j (bolt://100.87.214.70:7687)
- Qdrant (http://100.87.214.70:6333)
- PostgreSQL (localhost:5433)
- OmniRoute (http://100.87.214.70:3000) — 110 tools, routing engine
- Make.com (scenarios, workflows, data stores)
- ClickUp (tasks, time tracking, project management)
- Supabase (database, edge functions, auth)
- Vercel (deployments, analytics, edge functions)
- Gmail, Google Calendar, Google Drive
- HubSpot, Salesforce
- Slack, Notion, Claude Docs
- Stripe, GitHub, WebFetch, WebSearch

**Gap:** Tools not explicitly routed to agent capabilities or logic layers. No master tool registry.

---

### D. Logic Layers (72 organized)

**Location:** [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml]] (queryable)

**12 Domains × 6 Layers each = 72 Logic Layers**
| Domain | Logics | Control Plane | Agent Assignment | Status |
|--------|--------|---------------|------------------|--------|
| 1. WORLD | LOGIC-001–006 | CP-001 | Strategic vision agents | 🟡 Partial |
| 2. OBSERVATION | LOGIC-007–012 | CP-002 | Data collection + research agents | 🟡 Partial |
| 3. DATA | LOGIC-013–018 | CP-003 | ETL agents, data engineers | 🟡 Partial |
| 4. INFORMATION | LOGIC-019–024 | CP-004 | Knowledge extraction agents | 🟡 Partial |
| 5. KNOWLEDGE | LOGIC-025–030 | CP-005 | Knowledge graph agents | ✅ Ready |
| 6. MEMORY | LOGIC-031–036 | CP-006 | Retrieval + memory agents | ✅ Ready |
| 7. RETRIEVAL | LOGIC-037–042 | CP-007 | Query + indexing agents | ✅ Ready |
| 8. CONTEXT | LOGIC-043–048 | CP-008 | Assembly + ranking agents | ✅ Ready |
| 9. COGNITION | LOGIC-049–054 | CP-009 | Analysis + reasoning agents | 🟡 Partial |
| 10. THOUGHT | LOGIC-055–060 | CP-010 | Generation + creativity agents | 🟡 Partial |
| 11. DECISION | LOGIC-061–066 | CP-011 | Choice architecture agents | 🟡 Partial |
| 12. ACTION | LOGIC-067–072 | CP-012 | Execution + workflow agents | 🟡 Partial |

**Gap:** Only 40% of logic layers have assigned agents. Rest are orphaned.

---

### E. Typed Wikilinks & Ontology

**Location:** [[_ONTOLOGY/COMPANY-BRAIN-ONTOLOGY.xml]], [[_ONTOLOGY/RESEARCH-INTELLIGENCE-LAYER.xml]]

**15 Relationship Families:**
- ORGANIZATION (hierarchies, roles)
- BUSINESS (ventures, revenue, metrics)
- AGENTS (capabilities, permissions)
- CAPABILITIES (skills, techniques)
- SOFTWARE (repos, dependencies)
- WORKFLOWS (processes, automation)
- BUSINESS LOGIC (rules, constraints)
- DECISIONS (choices, outcomes)
- KNOWLEDGE (papers, evidence)
- STATE/EVENT (status, transitions)
- EVALUATION (scoring, assessment)
- DEPENDENCY (requires, blocks)
- TEMPORAL (scheduled, recurring)
- GOVERNANCE (approvals, authorities)
- LEARNING (feedback, improvements)

**Gap:** Relationship types defined but not enforced in agent routing or tool calls.

---

### F. Research Intelligence Base (42-RESEARCH-INTELLIGENCE)

**20 Sections:** Sources, Papers, Authors, Topics, Methods, Models, Datasets, Benchmarks, Repositories, Claims, Evidence, Experiments, Results, Hypotheses, Opportunities, Research Agents, Workflows, Evaluations, Adoption Decisions

**11-Level Evidence Hierarchy:** Observation → Source → Paper → Claim → Evidence → Experiment → Replication → Validated Result → Capability → Agent Workflow → Business Outcome

**Gap:** Research discoveries not automatically surfaced to relevant agents or capabilities.

---

### G. Obsidian Knowledge Graph (ObsidianWorldwidebroVault)

**Status:** Vault exists, 40+ sessions, not actively wired to Neo4j or agent dispatch.

**Gap:** Obsidian is a read-only reference, not a live bidirectional knowledge source for agents.

---

### H. Open Knowledge Integration

**Status:** Not yet wired.

**Gap:** Open Knowledge system exists but no bridge to Company Brain workflows.

---

## CRITICAL GAPS (Priority Order)

### GAP #1: Agent Dispatch Router
**Problem:** 275 agents exist but no system to:
- Match task type → appropriate agent(s)
- Route to local Ollama vs. cloud Claude
- Check permissions via tool gateway
- Track autonomy level (L1/L2/L3)

**Impact:** Agents sit idle. Tasks not automatically routed.

**Solution:** Build `AGENT_DISPATCH_ROUTER.js` that:
- Reads task (from ClickUp, Make, webhook, etc.)
- Queries agent registry against logic layers
- Selects best-fit agent(s)
- Checks TOOL_GATEWAY permissions
- Routes to L1 (human approval) / L2 (assisted) / L3 (autonomous)
- Returns results to job queue

---

### GAP #2: Master Agent Registry
**Problem:** 275 agents defined but:
- Not discoverable by dispatch router
- Not tagged with logic layers, control planes, or capabilities
- Not indexed by tool requirements or skill dependencies
- Not rated for trustworthiness/autonomy level

**Impact:** Dispatch router can't match tasks to agents intelligently.

**Solution:** Create `_REGISTRIES/CANONICAL/AGENT_REGISTRY.yaml`:
```yaml
agent:
  id: agent-business-strategist-001
  name: Business Strategist
  file_path: .claude/agents/business-strategist.md
  domain: 01-IDENTITY
  logic_layers: [LOGIC-001, LOGIC-049, LOGIC-061]
  control_planes: [CP-001, CP-009, CP-011]
  capabilities: [market-analysis, competitive-positioning, strategy-design]
  required_skills: [research, synthesis, storytelling]
  required_tools: [neo4j, qdrant, webfetch, websearch]
  required_mcps: [claude-ai-Make, claude_ai_Google_Drive]
  autonomy_level: L1  # L1=human approval, L2=assisted, L3=autonomous
  trustworthiness_score: 0.92
  cost_per_use_usd: 0.50
  expected_duration_minutes: 45
  success_rate_percent: 94
  last_verified: 2026-09-17
```

Repeat for all 275 agents.

---

### GAP #3: Skill Registry & Wiring
**Problem:** 30+ skills exist in 6+ different locations but:
- Not indexed in any registry
- Not linked to agents that use them
- Not mapped to logic layers or capabilities
- Discovery is manual (know the URL)

**Impact:** Skills not discoverable. Agents can't call them reliably.

**Solution:** Create `_REGISTRIES/CANONICAL/SKILL_REGISTRY.yaml`:
```yaml
skill:
  id: skill-gitnexus-debugging-001
  name: "GitNexus Debugging"
  location: worldwidebro-venture-portal/.claude/skills/gitnexus/gitnexus-debugging/SKILL.md
  agent_ids: [engineering-software-architect, engineering-mobile-app-builder]
  logic_layers: [LOGIC-049, LOGIC-050, LOGIC-051]
  required_tools: [github, bash]
  input_schema: { file_path: string, error_message: string, context: object }
  output_schema: { diagnosis: string, fix_plan: array, code_changes: array }
  success_rate_percent: 89
  last_verified: 2026-09-17
```

---

### GAP #4: Tool Gateway Registry
**Problem:** 20+ MCPs exist but no master registry of:
- Which tools do what
- Which agents have permission to call them
- Rate limits, cost, timeout
- Risk level (READ/WRITE/HIGH-RISK)
- Fallback tools if primary fails

**Impact:** Dispatch can't validate tool permissions. No rate limiting. No cost tracking.

**Solution:** Create `_REGISTRIES/CANONICAL/TOOL_GATEWAY_REGISTRY.yaml`:
```yaml
tool:
  id: tool-neo4j-query-001
  name: "Neo4j Cypher Query"
  mcp: neo4j
  risk_level: READ
  required_permissions: [graph_read, authentication_valid]
  agents_allowed: [all]
  rate_limit: 1000/hour
  cost_per_call_usd: 0.001
  timeout_seconds: 30
  fallback_tool: qdrant_semantic_search
  last_verified: 2026-09-17
```

---

### GAP #5: Capability Registry Wiring
**Problem:** 300+ capabilities exist but not:
- Mapped to agents that execute them
- Mapped to logic layers that enable them
- Mapped to research opportunities that created them
- Discoverable by ventures needing them

**Impact:** Capabilities orphaned. Ventures can't find what they need.

**Solution:** Extend `14-CAPABILITIES/README.md` with:
```yaml
capability:
  id: CAP-001-semantic-routing
  name: "Semantic Routing"
  description: "Route requests by semantic similarity"
  logic_layers: [LOGIC-045, LOGIC-046, LOGIC-047]
  agents_executing: [agent-ai-assistant-001, agent-dispatch-router-001]
  repositories: [worldwidebro-agents/routing, company-brain/context-assembly]
  research_sources: [arXiv:2305.xxxxx, papers-with-code.com/semantic-routing]
  ventures_using: [LT-005, OPS-001, CALLCENTER]
  revenue_impact_usd: 24000  # annual per deployment
  readiness_score: 0.92
```

---

## WIRING PLAN (Execute in Order)

### Phase 2a: Dispatch & Discovery (Oct 2026, 2 weeks)
1. Create `AGENT_REGISTRY.yaml` (all 275 agents tagged to logic layers + control planes)
2. Create `SKILL_REGISTRY.yaml` (30+ skills discoverable)
3. Create `TOOL_GATEWAY_REGISTRY.yaml` (20+ MCPs with permissions)
4. Build `AGENT_DISPATCH_ROUTER.js` (task → best agent(s) → L1/L2/L3 routing)
5. Wire dispatch router to ClickUp webhook + Make.com scenarios
6. Test: 10 end-to-end task flows (each logic layer → assigned agent → tool call → result)

### Phase 2b: Capability Routing (Nov 2026, 2 weeks)
1. Extend `CAPABILITY_REGISTRY.yaml` (300+ capabilities mapped to agents + research)
2. Build `CAPABILITY_RESOLVER.js` (venture need → matching capability(ies) + agents + revenue impact)
3. Wire capability resolver to VEX portfolio dashboard
4. Test: 5 venture capability discovery workflows

### Phase 2c: Research-to-Agent Pipeline (Dec 2026, 2 weeks)
1. Wire research discovery agent → finds relevant papers
2. Verification agent → validates claims against capabilities
3. Synthesis agent → connects research to existing capabilities
4. Adoption agent → recommends deployment to ventures
5. Test: Research paper → deployed capability (end-to-end)

### Phase 2d: Obsidian ↔ Graph Bridge (Jan 2027, 2 weeks)
1. Build `OBSIDIAN_SYNC.js` (watch Obsidian vault, push changes to Neo4j)
2. Build `NEO4J_TO_OBSIDIAN.js` (query Neo4j, render as Obsidian notes)
3. Wire Open Knowledge integration
4. Test: Bidirectional knowledge sync (editing Obsidian updates graph, updating graph reflects in Obsidian)

### Phase 2e: Autonomous L3 Execution (Feb-Mar 2027, 4 weeks)
1. Lock autonomy levels for each agent (trust scores, success rates)
2. Build L3 approval gates (confidence threshold → auto-approve, else escalate)
3. Build audit log for all L3 decisions
4. Test: 20 L3 workflows executing without human intervention
5. Build learning feedback loop (outcomes → improve future decisions)

---

## IMMEDIATE ACTIONS (This Week)

### 1. Wire All READMEs to This Document
Add to every README.md header:
```markdown
[[_MCP/SYSTEMS-INTEGRATION-MASTER|← System Integration Master]]
```

This creates backlink awareness across all 2,273 READMEs.

### 2. Create Master Discovery Index
File: `_REGISTRIES/CANONICAL/MASTER_DISCOVERY_INDEX.yaml`

```yaml
discovery_index:
  agents: _REGISTRIES/CANONICAL/AGENT_REGISTRY.yaml (275 agents)
  skills: _REGISTRIES/CANONICAL/SKILL_REGISTRY.yaml (30+ skills)
  tools: _REGISTRIES/CANONICAL/TOOL_GATEWAY_REGISTRY.yaml (20+ MCPs)
  capabilities: 14-CAPABILITIES/README.md + capability-registry.yaml (300+)
  logic_layers: _REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml (72 logics)
  control_planes: _REGISTRIES/CANONICAL/control-planes-by-sector.yaml (30 CPs)
  research: 42-RESEARCH-INTELLIGENCE/README.md (20 sections)
  ventures: _REGISTRIES/CANONICAL/ventures-by-sector.yaml (789 ventures)
  repositories: _REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml (1,740 repos)
```

### 3. Build Dispatch Router Skeleton
File: `repos/worldwidebro-agents/src/dispatcher/AgentDispatcher.js`

```javascript
class AgentDispatcher {
  constructor(agentRegistry, toolGateway, neo4jContext) {
    this.agentRegistry = agentRegistry;
    this.toolGateway = toolGateway;
    this.neo4j = neo4jContext;
  }

  async dispatch(task) {
    // 1. Parse task intent → logic layer(s)
    const logicLayers = await this.classifyLogicLayers(task);
    
    // 2. Find agents supporting those layers
    const candidates = this.agentRegistry.findByLogicLayers(logicLayers);
    
    // 3. Rank by trust score, success rate, availability
    const ranked = this.rankAgents(candidates, task);
    
    // 4. Check tool permissions for top candidate
    const agent = ranked[0];
    const permissions = await this.toolGateway.checkPermissions(agent, task);
    
    // 5. Route by autonomy level
    if (agent.autonomy_level === 'L1') {
      return { status: 'waiting_human_approval', agent, task };
    } else if (agent.autonomy_level === 'L2') {
      return await this.executeWithAssistance(agent, task);
    } else {
      return await this.executeAutonomous(agent, task);
    }
  }
}
```

### 4. Create Agent Tagging Script
Script: `_CLI/tag-agents.sh`

Reads all 275 agents, extracts metadata, builds AGENT_REGISTRY.yaml with:
- Domain inference from filename
- Logic layer assignment (manual override support)
- Control plane association
- Tool requirements scanning
- Autonomy level defaults

---

## SUCCESS CRITERIA (Phase 2 Complete)

✅ Every agent discoverable by task type  
✅ Every skill callable by dispatch router  
✅ Every tool has permission rules + cost tracking  
✅ Every capability routable to ventures needing it  
✅ Every research paper connected to capable agents  
✅ 80%+ of tasks auto-dispatched without human decision  
✅ L3 autonomous workflows executing reliably (90%+ success rate)  
✅ Obsidian ↔ Neo4j bidirectional sync  
✅ Revenue impact measurable (research → capability → venture → $)  
✅ Zero scattered/orphaned pieces (100% discoverability)

---

## ARCHITECTURE DIAGRAM

```
USER TASK
    ↓
[AGENT_DISPATCH_ROUTER.js]
    ├─ Parse intent → logic layers
    ├─ Query AGENT_REGISTRY (275 agents)
    ├─ Query TOOL_GATEWAY_REGISTRY (20+ MCPs)
    ├─ Query CAPABILITY_REGISTRY (300+ capabilities)
    └─ Query LOGIC_LAYERS_REGISTRY (72 logics)
    ↓
[RANKED AGENT CANDIDATES]
    ├─ Trust score
    ├─ Success rate
    ├─ Availability
    └─ Permission check
    ↓
[AUTONOMY LEVEL GATE]
    ├─ L1: Escalate to human → approval
    ├─ L2: Execute with assistant oversight
    └─ L3: Execute autonomously (log audit trail)
    ↓
[SKILL + TOOL EXECUTION]
    ├─ Load skill(s)
    ├─ Call tool(s) via MCP
    ├─ Track cost, latency, success
    └─ Log to PostgreSQL audit trail
    ↓
[RESULT HANDLER]
    ├─ Update Neo4j (graph state)
    ├─ Update PostgreSQL (event log)
    ├─ Update Qdrant (embeddings)
    ├─ Notify user/task
    ├─ Update Obsidian (knowledge)
    └─ Trigger learning feedback
```

---

**Status:** Framework complete. Ready for Phase 2 build. All pieces exist—just need wiring.

**Next:** Create AGENT_REGISTRY.yaml (estimate 4-6 hours to tag 275 agents).

