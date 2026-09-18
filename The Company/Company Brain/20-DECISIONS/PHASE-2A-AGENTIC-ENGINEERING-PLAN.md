---
id: PHASE-2A-AGENTIC-ENGINEERING-PLAN
title: "Phase 2a Agentic Engineering Plan — 15-Minute Units + Evals + Model Routing"
description: "Structured decomposition of Phase 2a (Oct 2026) into agent-sized units with completion criteria, evals, and model routing"
authority: CP-012 (Agent Control Plane), CP-027 (Engineering)
updated: 2026-09-17
phase: Phase 2a (Oct 2026)
---

[[PHASE-2A-SYSTEMS-WIRING-CHECKLIST]] | [[_MCP/SYSTEMS-INTEGRATION-MASTER]] | [[_REGISTRIES/CANONICAL/AGENTS_INVENTORY_318.yaml]]

# Phase 2a Agentic Engineering Plan

**Timeline:** Oct 1-31, 2026 (4 weeks)  
**Budget:** 100 hours, $7,700  
**Team:** 2 engineers + 1 DevOps  
**Success Metric:** 50 agents deployed, routeable, revenue-tracked by Dec 31

---

## OPERATING PRINCIPLES (Agentic Engineering)

1. **Define completion criteria before execution** — each 15-min unit has a testable done condition
2. **Decompose into agent-sized units** — independently verifiable, single dominant risk, clear boundary
3. **Route by model tier** — Haiku (classification/boilerplate), Sonnet (implementation), Opus (architecture/root-cause)
4. **Measure with evals** — baseline → implement → compare
5. **Compact after milestones, not during debugging** — maintain momentum across 4 weeks

---

## EVAL STRATEGY (Capability + Regression)

### Baseline Evals (Day 0 - Before any implementation)

**Capability Eval 1: Agent Registry Population**
- **Rubric:** Can we extract agent metadata from 318 .md files and populate AGENT_REGISTRY.yaml?
- **Test:** Parse 10 sample agents (Academic Anthropologist, Cold Email Writer, Backend Architect, etc.)
  - Extract: id, name, domain, category, autonomy_level, deployed status
  - Validate: no missing fields, consistent format
- **Pass criteria:** 8/10 sample agents parse correctly with no manual intervention
- **Failure signature:** Field extraction failures, inconsistent naming, missing autonomy_level

**Capability Eval 2: Dispatch Router Ranking**
- **Rubric:** Can dispatch router rank agents by trustworthiness + success_rate + cost correctly?
- **Test:** Input task "Write 50 cold emails" → Should rank Cold Email Writer (#1) > Email Strategist (#2) > Marketing Specialist (#3)
  - Verify: Ranking logic matches MEDDPICC-style scoring
  - Verify: Autonomy level gates work (L2 = human review)
- **Pass criteria:** Top 3 ranking correct, autonomy gate enforced
- **Failure signature:** Wrong agent ranked first, autonomy gate ignored

**Capability Eval 3: Revenue Attribution Path**
- **Rubric:** Can we trace an agent action → deal → revenue?
- **Test:** End-to-end: Cold Email Writer generates 50 emails → 4 replies (tracked) → 2 meetings via Discovery Caller → 1 deal via Closer → revenue logged
  - Verify: Each step logged with timestamps + agent id
  - Verify: Revenue attributed back to Cold Email Writer
- **Pass criteria:** Full trail exists, revenue attributed correctly
- **Failure signature:** Missing link in chain, revenue lost/misattributed

**Capability Eval 4: Skill Registry Discoverability**
- **Rubric:** Can agents discover skills they need?
- **Test:** Cold Email Writer queries: "What skills do I need?" → Should return: email-writing, personalization, list-segmentation
  - Verify: Skills exist in SKILL_REGISTRY.yaml
  - Verify: Each skill is callable (not vaporware)
- **Pass criteria:** 90%+ of required skills discoverable
- **Failure signature:** Skills listed but not implemented, or circular dependencies

**Capability Eval 5: Tool Gateway Permission Model**
- **Rubric:** Can tool gateway enforce permissions + rate limits + cost tracking?
- **Test:** Cold Email Writer requests SendGrid tool → Check: permissions granted? Rate limit 100/day? Cost $0.001/email?
  - Verify: Permission check passes
  - Verify: Rate limit enforced (reject email 101)
  - Verify: Cost deducted from budget
- **Pass criteria:** All 3 controls work (permissions, rate limit, cost)
- **Failure signature:** Tool called without permission check, rate limit ignored, cost not tracked

### Regression Evals (Weekly + End of Phase)

**Regression Eval 1: No Agents Lost**
- **Metric:** Agent count = 318 throughout phase
- **Test:** Count agents in AGENT_REGISTRY.yaml each Monday
- **Pass criteria:** 318 agents present all 4 weeks
- **Failure signature:** Agent count drops (data loss)

**Regression Eval 2: Dispatch Router Consistency**
- **Metric:** Same task always ranks same top 3 agents (±1 position)
- **Test:** Query "Score these 100 inbound leads" 3x per week → top 3 should be consistent
- **Pass criteria:** Same top agent all 3 queries
- **Failure signature:** Different agent ranked #1 on different days (non-deterministic)

**Regression Eval 3: Revenue Attribution Completeness**
- **Metric:** 95%+ of closed deals attributed to an agent
- **Test:** Sample 20 deals per week → check if agent_id present in attribution log
- **Pass criteria:** 19/20 deals have agent attribution
- **Failure signature:** Deals closed but no agent recorded

**Regression Eval 4: System Performance (No Slowdowns)**
- **Metric:** Dispatch router response time stays <500ms
- **Test:** Measure dispatch query latency each Friday
- **Pass criteria:** <500ms for task classification + agent ranking + 10 registries queried
- **Failure signature:** Response time creeps above 500ms (indicates N+1 queries or data bloat)

---

## TASK DECOMPOSITION (15-Minute Units)

### WEEK 1: DISCOVERY & REGISTRIES (17 hours)

#### Task 1.1: Extract Agent Metadata (4 hours)

**1.1a: Sample parsing (20 min)**
- [ ] Read academic-anthropologist.md, cold-email-writer.md, backend-architect.md
- [ ] Extract: id, name, domain, category, description, autonomy_level
- [ ] Done: 3 sample entries parsed without errors
- **Model:** Haiku (classification)
- **Risk:** Inconsistent field names across .md files
- **Verify:** Compare 3 entries to AGENT_REGISTRY.yaml schema — exact match

**1.1b: Auto-generation script (30 min)**
- [ ] Write `tag-agents.sh` to glob all 318 agents/*.md files
- [ ] Extract metadata for each (use regex or frontmatter parsing)
- [ ] Output to AGENT_REGISTRY.yaml
- [ ] Done: Script runs cleanly on 10-agent sample, no errors
- **Model:** Haiku (boilerplate)
- **Risk:** Regex fragility (agent names inconsistent)
- **Verify:** `tag-agents.sh` run on agents/ → validates YAML syntax

**1.1c: Populate full registry (1 hour)**
- [ ] Run `tag-agents.sh` on all 318 agents
- [ ] Validate: No parsing errors, no duplicates, all 318 present
- [ ] Done: AGENT_REGISTRY.yaml has 318 agents, all fields populated
- **Model:** Haiku (boilerplate)
- **Risk:** Validation failures on edge cases (special chars in names)
- **Verify:** `yq eval '.agents | length' AGENT_REGISTRY.yaml` = 318

**1.1d: QA—Random sampling (1.5 hours)**
- [ ] Randomly sample 30 agents (10% coverage)
- [ ] Verify metadata accuracy vs. original .md files
- [ ] Check: autonomy_level, domain, category all correct
- [ ] Done: 28/30 accurate (93% pass rate)
- **Model:** Haiku (classification)
- **Risk:** Metadata mismatches (e.g., agent domain in .md vs registry disagree)
- **Verify:** Manual review of 30 agents — spot check for accuracy

---

#### Task 1.2: Build Skill Registry (4 hours)

**1.2a: Skill inventory (45 min)**
- [ ] Review SYSTEMS-INTEGRATION-MASTER.md → "30+ skills" section
- [ ] List all skills: email-writing, personalization, outreach, lead-scoring, etc.
- [ ] Done: 30+ skills listed with definitions
- **Model:** Haiku (classification)
- **Risk:** Vague skill definitions (what exactly is "personalization"?)
- **Verify:** Each skill has 1-2 sentence definition

**1.2b: Map skills to agents (1.5 hours)**
- [ ] For each of 30 agents (Oct Tier 1), list required skills
- [ ] Example: Cold Email Writer needs [email-writing, personalization, list-segmentation, follow-up-sequencing]
- [ ] Done: 30 agents × 4 skills avg = 120 mappings
- **Model:** Sonnet (reasoning about agent capabilities)
- **Risk:** Incomplete skill lists (agent needs skill not in registry)
- **Verify:** Each Oct Tier 1 agent has 3-5 skills listed

**1.2c: Create SKILL_REGISTRY.yaml (1 hour)**
- [ ] Build registry: skill_id, name, description, applicable_agents, required_tools
- [ ] Example entry:
  ```yaml
  - id: skill-email-writing-001
    name: "Email Writing & Personalization"
    description: "Craft personalized emails that convert"
    applicable_agents: [cold-email-writer, email-strategist, sales-coach]
    required_tools: [sendgrid, mailchimp]
  ```
- [ ] Done: 30+ skills with all fields populated
- **Model:** Haiku (boilerplate)
- **Risk:** Circular dependencies (skill A requires skill B requires skill A)
- **Verify:** `yq eval '.skills | length' SKILL_REGISTRY.yaml` = 30+

**1.2d: QA—Skill discoverability (45 min)**
- [ ] Test: Cold Email Writer queries SKILL_REGISTRY for "email-writing" → found ✓
- [ ] Test: All skills are actually callable (not vaporware)
- [ ] Done: 95%+ of expected skills discoverable
- **Model:** Sonnet (verification)
- **Risk:** Skills listed but not implemented anywhere
- **Verify:** Check each skill maps to at least 1 agent implementation

---

#### Task 1.3: Create Tool Gateway Registry (3 hours)

**1.3a: Tool inventory (45 min)**
- [ ] List 20+ MCPs: SendGrid, ClickUp, Neo4j, Stripe, Supabase, etc.
- [ ] For each: endpoint, auth method, rate limits, cost per call
- [ ] Done: 20+ tools with full metadata
- **Model:** Haiku (data collection)
- **Risk:** Outdated API endpoints (SendGrid v3 vs v2)
- **Verify:** Curl each endpoint → verify 200 OK

**1.3b: Permission model (1 hour)**
- [ ] Define RBAC for tools: which agents can call which tools?
- [ ] Example: Cold Email Writer can call SendGrid (L3 autonomous), Stripe (L1 human review)
- [ ] Done: Permission matrix for 30 agents × 20 tools
- **Model:** Sonnet (reasoning about permissions)
- **Risk:** Over-permissive (agent can call anything), under-permissive (agent blocked from needed tool)
- **Verify:** Cold Email Writer can send emails (SendGrid), can't transfer money (Stripe)

**1.3c: Rate limit & cost config (1 hour)**
- [ ] For each tool: rate limit (calls/day), cost per call, monthly budget
- [ ] Example: SendGrid 100 emails/day, $0.001/email, $100/month budget
- [ ] Done: All 20+ tools have rate limits + costs
- **Model:** Haiku (configuration)
- **Risk:** Rate limits too aggressive (agents starved), too permissive (runaway costs)
- **Verify:** Cold Email Writer can send ≤100 emails/day, budget tracking works

**1.3d: Build TOOL_GATEWAY_REGISTRY.yaml (15 min)**
- [ ] Serialize permission matrix + rate limits + costs to YAML
- [ ] Done: TOOL_GATEWAY_REGISTRY.yaml complete, valid YAML
- **Model:** Haiku (boilerplate)
- **Risk:** YAML syntax errors
- **Verify:** `yq eval 'keys' TOOL_GATEWAY_REGISTRY.yaml` = 20+ tools

---

#### Task 1.4: Integration Testing (Week 1 registries) (1.5 hours)

**1.4a: Registry schema validation (30 min)**
- [ ] Validate AGENT_REGISTRY.yaml against JSON schema
- [ ] Validate SKILL_REGISTRY.yaml against schema
- [ ] Validate TOOL_GATEWAY_REGISTRY.yaml against schema
- [ ] Done: All 3 pass schema validation
- **Model:** Haiku (validation)
- **Risk:** Schema mismatch (registry has extra fields)
- **Verify:** `ajv validate -s schema.json -d AGENT_REGISTRY.yaml`

**1.4b: Cross-registry consistency (30 min)**
- [ ] Check: Each agent in AGENT_REGISTRY references real skills (SKILL_REGISTRY)
- [ ] Check: Each agent can access required tools (TOOL_GATEWAY_REGISTRY)
- [ ] Done: No broken references
- **Model:** Sonnet (graph reasoning)
- **Risk:** Dangling references (agent needs skill not in registry)
- **Verify:** For each Oct Tier 1 agent: skills exist, tools accessible

**1.4c: Performance baseline (30 min)**
- [ ] Load all 3 registries into memory
- [ ] Query: "What agents support email-writing?" → measure latency
- [ ] Done: Query returns in <100ms
- **Model:** Haiku (measurement)
- **Risk:** Registries too large (load time slow)
- **Verify:** Latency <100ms for typical registry queries

---

#### Task 1.5: Pattern Integration — awesome-agentic-patterns (2 hours)

**1.5a: Clone & catalog (30 min)**
- [ ] Clone https://github.com/evals-ai/awesome-agentic-patterns (68K stars)
- [ ] Catalog all pattern files (tool-use, reflection, multi-step, error-recovery, graceful-degradation, etc.)
- [ ] Done: Repository analyzed, 5+ core patterns identified
- **Model:** Haiku (data collection)
- **Risk:** Repository structure unclear, patterns not well-organized
- **Verify:** List all patterns found in README + /patterns/ directory

**1.5b: Extract core patterns (45 min)**
- [ ] Extract 5 most applicable patterns for agent dispatch + implementation:
  1. **Tool-use pattern** — how agents query registries + call tools safely
  2. **Reflection pattern** — how agents verify their own outputs (confidence scoring)
  3. **Multi-step pattern** — how to chain agent calls (workflow DAG)
  4. **Error-recovery pattern** — how agents handle failures gracefully (fallback logic)
  5. **Graceful-degradation pattern** — how agents degrade when capabilities unavailable
- [ ] For each: document pattern name + description + code example from awesome-agentic-patterns
- [ ] Done: 5 patterns extracted with working code examples
- **Model:** Sonnet (pattern analysis)
- **Risk:** Patterns don't apply to our agent architecture, requires translation
- **Verify:** Each pattern has a concrete agent use-case (e.g., Tool-use for Dispatch Router)

**1.5c: Create Agent Implementation Template (30 min)**
- [ ] Document "AGENT_IMPLEMENTATION_PATTERNS.md" showing:
  - Pattern 1 (Tool-use) → Used in AGENT_DISPATCH_ROUTER.js (Week 2, Task 2.1a)
  - Pattern 2 (Reflection) → Used in agent confidence scoring (Task 1.2c)
  - Pattern 3 (Multi-step) → Used in workflow DAG (Task 3.2b)
  - Pattern 4 (Error-recovery) → Used in failure handling (Week 4, Task 4.1b)
  - Pattern 5 (Graceful-degradation) → Used in fallback logic (Task 3.2c)
- [ ] Done: Template document with patterns + agent examples
- **Model:** Haiku (documentation)
- **Risk:** Patterns unclear, template doesn't match downstream usage
- **Verify:** Each pattern referenced in Week 2-4 tasks where it's applied

**1.5d: Reference in discovery guide (15 min)**
- [ ] Update [[AGENTS_DISCOVERY_INVOCATION_GUIDE]] with "Pattern Reference" section
- [ ] Link: [[awesome-agentic-patterns|https://github.com/evals-ai/awesome-agentic-patterns]]
- [ ] Show: "Agents are built using 5 core patterns from awesome-agentic-patterns. See AGENT_IMPLEMENTATION_PATTERNS.md"
- [ ] Done: Wiki link + reference integrated
- **Model:** Haiku (wiki linking)
- **Risk:** Link broken, reference unclear
- **Verify:** Wiki link resolves, AGENT_IMPLEMENTATION_PATTERNS.md exists

---

### WEEK 2: DISPATCH ROUTER BUILD (20 hours)

#### Task 2.1: Design Dispatch Router Class (4 hours)

**2.1a: Class structure & interface (1 hour)**
- [ ] Define `AgentDispatchRouter` class
  ```typescript
  class AgentDispatchRouter {
    classifyTask(task: string): TaskClassification
    queryRegistries(classification: TaskClassification): CandidateAgents[]
    rankCandidates(candidates: CandidateAgents[]): RankedAgents[]
    enforceAutonomyGate(agent: Agent): GateDecision
    suggestAgent(task: string): AgentSuggestion
  }
  ```
- [ ] Done: All methods defined with types
- **Model:** Opus (architecture)
- **Risk:** Over-engineering (too many methods), under-engineering (missing logic)
- **Verify:** Class diagram matches SYSTEMS-INTEGRATION-MASTER.md dispatch flow

**2.1b: Task classification logic (1.5 hours)**
- [ ] Implement `classifyTask()` — parse task → extract logic layers
- [ ] Example: "Write 50 cold emails" → [LOGIC-019 (INFORMATION), LOGIC-049 (COGNITION)] + domain 30-REVENUE
- [ ] Done: 10-task sample classified correctly
- **Model:** Sonnet (NLP/classification)
- **Risk:** Vague logic layer mappings (what layer is "research"?)
- **Verify:** Compare 10 classified tasks to manual gold standard

**2.1c: Registry query logic (1 hour)**
- [ ] Implement `queryRegistries()` — given classification, find matching agents
- [ ] Query AGENT_REGISTRY for agents supporting LOGIC-019 + LOGIC-049 + domain 30-REVENUE
- [ ] Done: Returns 5-10 candidate agents (not 0, not 318)
- **Model:** Sonnet (query design)
- **Risk:** Query returns no agents (too restrictive), too many agents (too permissive)
- **Verify:** "Cold email" task returns Cold Email Writer + Email Strategist + Marketing Specialist

**2.1d: Ranking algorithm (0.5 hours)**
- [ ] Implement `rankCandidates()` — score agents by trustworthiness + success_rate + cost
- [ ] Formula: score = (trustworthiness × 0.5) + (success_rate × 0.3) + (1 / cost × 0.2)
- [ ] Done: Scoring produces deterministic ranks
- **Model:** Haiku (math)
- **Risk:** Weights favor wrong agent (high cost agent ranked #1)
- **Verify:** Cold Email Writer (0.89 trust, 87% success, $0.50) scores higher than Email Strategist (0.82, 80%, $0.75)

---

#### Task 2.2: Wire to Event Queue & MCP Endpoints (4 hours)

**2.2a: Event queue integration (2 hours)**
- [ ] Set up Supabase realtime subscription (task_queue table)
- [ ] When new task inserted → dispatch router processes it
- [ ] Example: INSERT task "Score 100 leads" → dispatch router classifies + ranks → suggests Lead Qualifier
- [ ] Done: Task flows from queue → router → suggestion table
- **Model:** Sonnet (integration)
- **Risk:** Missed messages (some tasks don't trigger dispatch), duplicate processing
- **Verify:** Insert 5 test tasks, verify 5 suggestions appear in output table

**2.2b: MCP endpoint exposure (1.5 hours)**
- [ ] Create FastMCP endpoint `/dispatch` accepting task_id
- [ ] Returns ranked agents + autonomy gates + cost estimates
- [ ] Example: `POST /dispatch { task_id: "task-123" }` → returns `{ agents: [{ name: "Cold Email Writer", rank: 1, confidence: 0.92, autonomy: "L2", cost: "$25" }] }`
- [ ] Done: Endpoint callable, returns expected schema
- **Model:** Sonnet (API design)
- **Risk:** Endpoint slow (>500ms), missing fields in response
- **Verify:** Curl endpoint with 10 test tasks, check latency <500ms

**2.2c: Autonomy gate enforcement (0.5 hours)**
- [ ] Implement `enforceAutonomyGate()` — check agent autonomy level vs. task risk
- [ ] L1 = human review required, L2 = assisted (agent suggests, human confirms), L3 = autonomous
- [ ] Example: Accounts Payable (L3) can transfer money autonomously; Cold Email Writer (L2) needs human to review drafts before sending
- [ ] Done: Gates enforced, no L3 agents ship without approval threshold met
- **Model:** Haiku (policy)
- **Risk:** L3 gates too permissive (agent transfers wrong amount), L1 gates too strict (delays everything)
- **Verify:** L1 task routes to human review, L3 task routes to autonomous execution

---

#### Task 2.3: Test Dispatch Router with 10-Agent Sample (6 hours)

**2.3a: End-to-end happy path (2 hours)**
- [ ] Test: Submit task "Write 50 cold emails to prospects"
- [ ] Expected: Cold Email Writer ranked #1
- [ ] Verify each step:
  1. Task classified correctly ✓
  2. AGENT_REGISTRY queried ✓
  3. Candidates ranked ✓
  4. Autonomy gate checked (L2, need human review) ✓
  5. Suggestion returned with confidence 0.92 ✓
- [ ] Done: Happy path works end-to-end
- **Model:** Sonnet (testing)
- **Risk:** One step fails silently (e.g., registry query returns 0 agents)
- **Verify:** Trace execution, verify each step completes

**2.3b: Regression path (2 hours)**
- [ ] Test: Submit task "This is very vague"
- [ ] Expected: Router returns graceful error, suggests clarifying task
- [ ] Test: Submit task for agent not in registry
- [ ] Expected: Router returns empty candidates (not crash)
- [ ] Done: Router handles 5 edge cases without crashing
- **Model:** Sonnet (error handling)
- **Risk:** Unhelpful error messages, router crashes on bad input
- **Verify:** 5 edge cases tested, all return helpful guidance

**2.3c: Performance testing (1 hour)**
- [ ] Load test: Submit 100 concurrent dispatch requests
- [ ] Verify: All complete within 500ms (latency p95 <500ms)
- [ ] Verify: No memory leaks (memory stable before/after 100 requests)
- [ ] Done: Router handles 100 concurrent requests, p95 latency <500ms
- **Model:** Haiku (measurement)
- **Risk:** Router slows under load (>500ms), memory leaks
- **Verify:** Load test with k6 or vegeta, check latency + memory

**2.3d: Agent sample validation (1 hour)**
- [ ] For each of 10 sample agents (Oct Tier 1):
  - Submit task that should route to that agent
  - Verify agent ranked #1
- [ ] Example:
  - Task "Score 100 inbound leads" → Lead Qualifier #1 ✓
  - Task "Generate proposal for $100K deal" → Proposal Generator #1 ✓
  - Task "Send contract" → Closer #1 ✓
- [ ] Done: 9/10 correct (90% accuracy)
- **Model:** Sonnet (verification)
- **Risk:** Wrong agent ranked #1 (e.g., Email Strategist instead of Cold Email Writer)
- **Verify:** Each of 10 tasks routes to correct agent

---

### WEEK 3: CAPABILITY & REVENUE ROUTING (18 hours)

#### Task 3.1: Extend Capability Registry (4 hours)

**3.1a: Capability inventory (1.5 hours)**
- [ ] Review SYSTEMS-INTEGRATION-MASTER.md → "300+ capabilities" section
- [ ] Build master list: prospect-qualification, deal-closing, contract-generation, revenue-tracking, etc.
- [ ] Done: 300+ capabilities listed
- **Model:** Haiku (data collection)
- **Risk:** Vague capability definitions, overlap with skills/agents
- **Verify:** Each capability is distinct from skills (skills are HOW, capabilities are WHAT)

**3.1b: Map capabilities to agents (1.5 hours)**
- [ ] For each of 30 Oct/Nov agents: what capabilities do they provide?
- [ ] Example: Cold Email Writer provides [prospect-outreach, email-generation, personalization]
- [ ] Done: 30 agents × 5 capabilities avg = 150 mappings
- **Model:** Sonnet (reasoning)
- **Risk:** Incomplete mappings (agent provides capability not listed)
- **Verify:** Cold Email Writer mapped to at least [prospect-outreach, email-generation]

**3.1c: Build CAPABILITY_REGISTRY.yaml (1 hour)**
- [ ] Serialize: capability_id, name, description, supported_agents, required_tools, revenue_per_use
- [ ] Example:
  ```yaml
  - id: cap-prospect-qualification-001
    name: "Prospect Qualification (Lead Scoring)"
    description: "Score inbound leads 1-100 by propensity to buy"
    supported_agents: [lead-qualifier, sales-coach, deal-strategist]
    required_tools: [hubspot, clearbit]
    revenue_per_use: "$50-100"  # Per qualified lead
  ```
- [ ] Done: CAPABILITY_REGISTRY.yaml with 300+ entries
- **Model:** Haiku (boilerplate)
- **Risk:** YAML errors, missing fields
- **Verify:** `yq eval '.capabilities | length' CAPABILITY_REGISTRY.yaml` = 300+

---

#### Task 3.2: Build Capability Resolver (4 hours)

**3.2a: Capability query logic (1.5 hours)**
- [ ] Implement `resolveCapability(need: string): ResolvedCapability`
- [ ] Input: "I need to qualify 100 leads" → Output: Lead Qualifier agent (supports prospect-qualification capability)
- [ ] Done: 10-query sample all resolve correctly
- **Model:** Sonnet (NLP/routing)
- **Risk:** Query returns wrong capability (resolves "email" as "email-marketing" instead of "email-generation")
- **Verify:** Compare 10 resolved capabilities to gold standard

**3.2b: Multi-agent workflows (1 hour)**
- [ ] Handle complex needs requiring multiple agents
- [ ] Example: "I need to close a $100K deal" → [Discovery Caller (qualify), Proposal Generator (build), Closer (send)]
- [ ] Done: Returns workflow DAG with agent sequence
- **Model:** Sonnet (workflow planning)
- **Risk:** Wrong agent ordering (Closer before Proposal Generator)
- **Verify:** Verify DAG respects dependencies (Proposal must precede Closer)

**3.2c: Fallback & escalation (0.5 hours)**
- [ ] If capability not found → suggest closest match or escalate to human
- [ ] Example: "I need to do quantum computing" → "No agents support this capability. Escalate to human?"
- [ ] Done: Graceful degradation
- **Model:** Haiku (policy)
- **Risk:** Suggests irrelevant agent, misleads user
- **Verify:** Test 5 queries for non-existent capabilities, verify escalation offered

**3.2d: MCP endpoint (1 hour)**
- [ ] Create `/resolve-capability` endpoint
- [ ] Input: `{ need: "Qualify 100 leads" }`
- [ ] Output: `{ agents: [Lead Qualifier], workflow: [...], cost: "$500" }`
- [ ] Done: Endpoint callable, returns valid response
- **Model:** Sonnet (API)
- **Risk:** Endpoint slow, missing fields
- **Verify:** Curl endpoint, verify <500ms latency

---

#### Task 3.3: Wire Research → Capability → Revenue (3 hours)

**3.3a: Research-to-capability mapping (1 hour)**
- [ ] When research assistant finds paper → extract capability claim
- [ ] Example: Paper title "Cold Email Personalization Increases Reply Rate by 23%" → capability [email-personalization, prospect-outreach]
- [ ] Done: 10-paper sample all map to valid capabilities
- **Model:** Sonnet (NLP)
- **Risk:** Misinterpret paper (claim "cold email works" as "cold email writing capability")
- **Verify:** Manual review of 10 paper→capability mappings

**3.3b: Capability-to-agent binding (1 hour)**
- [ ] When capability claimed → route to supporting agents
- [ ] Example: email-personalization capability → Cold Email Writer, Email Strategist
- [ ] Track: Which agents implement which capabilities
- [ ] Done: Capability claim linked to 2-3 supporting agents
- **Model:** Sonnet (reasoning)
- **Risk:** Capability linked to agent that doesn't support it
- **Verify:** For each capability, at least 2 agents listed

**3.3c: Revenue attribution (1 hour)**
- [ ] When agent executes → trace back to research that enabled it
- [ ] Example: Cold Email Writer sends emails → generates replies → deals close → revenue logs
- [ ] Attribution: "X deals ($Y revenue) traced to research paper on email personalization"
- [ ] Done: End-to-end research → revenue link established
- **Model:** Sonnet (tracing)
- **Risk:** Revenue attribution breaks (deal closes but research forgotten)
- **Verify:** Sample 5 closed deals, trace back to originating research paper

---

#### Task 3.4: Integration Testing (Week 3) (7 hours)

**3.4a: Capability resolver end-to-end (2 hours)**
- [ ] Test: User says "I need to close 10 large deals"
- [ ] Expected flow:
  1. Need classified as multi-agent workflow
  2. Resolver suggests [Discovery Caller → Proposal Generator → Closer]
  3. Each agent's capabilities resolved + cost estimated
  4. Workflow DAG returned
- [ ] Done: Full workflow resolved correctly
- **Model:** Sonnet (integration)
- **Risk:** Workflow DAG wrong order, missing agents
- **Verify:** Trace execution, verify dependencies met

**3.4b: Research-to-revenue pipeline (2 hours)**
- [ ] Test: Submit research paper → extract capability → route to agent → execute → track revenue
- [ ] Example:
  1. Paper: "Douyin Short Videos Convert 15% Better Than Long-Form"
  2. Capability extracted: [short-video-content, platform-marketing]
  3. Agent: Douyin Strategist
  4. Execution: Generate 10 short videos
  5. Revenue: Track video performance, attribute to research
- [ ] Done: Full pipeline completes, revenue attributed
- **Model:** Sonnet (integration)
- **Risk:** Attribution lost (revenue not traced back to research)
- **Verify:** Sample 5 research→execution→revenue traces

**3.4c: Performance & regression (2 hours)**
- [ ] Dispatch router latency still <500ms (didn't slow down)
- [ ] Capability resolver latency <200ms (new, not yet optimized)
- [ ] No memory leaks under 100 concurrent requests
- [ ] Done: All performance baselines met
- **Model:** Haiku (measurement)
- **Risk:** New resolver adds latency, overall dispatch slows
- **Verify:** Load test with k6, compare to Week 2 baseline

**3.4d: Cross-system consistency (1 hour)**
- [ ] Verify no conflicts between registries (AGENT, SKILL, TOOL, CAPABILITY)
- [ ] Test: Agent says "I need email-writing skill" → Skill exists ✓
- [ ] Test: Agent says "I need SendGrid tool" → Tool accessible ✓
- [ ] Test: Agent says "I provide prospect-qualification capability" → Capability exists ✓
- [ ] Done: No broken references across all 4 registries
- **Model:** Sonnet (graph validation)
- **Risk:** Dangling references (agent needs skill that doesn't exist)
- **Verify:** Automated consistency check passes

---

### WEEK 4: INTEGRATION & DOCUMENTATION (12 hours)

#### Task 4.1: End-to-End Integration Testing (6 hours)

**4.1a: 50 workflow scenarios (4 hours)**
- [ ] Execute 50 complete workflows end-to-end
- [ ] Scenarios organized by type:
  - **Sales workflows (10):** Lead gen → qualification → proposal → close → revenue
  - **Product workflows (10):** UX research → design → dev → QA → ship
  - **Customer success workflows (8):** Onboarding → health scoring → churn prevention → upsell
  - **Marketing workflows (7):** Research → content → distribution → tracking
  - **Operational workflows (5):** Process automation → monitoring → alerting → escalation
- [ ] For each: verify all steps complete, no errors, revenue attributed
- [ ] Done: 45/50 workflows pass (90% pass rate)
- **Model:** Sonnet (test design + execution)
- **Risk:** Edge case workflows fail (complex multi-agent scenarios)
- **Verify:** Each workflow traced end-to-end, documented in test report

**4.1b: Failure mode testing (1.5 hours)**
- [ ] Test 10 failure scenarios:
  1. Agent unavailable (L2 escalation to human)
  2. Tool rate limit exceeded (queue task, retry)
  3. Revenue attribution missing (alert, manual investigation)
  4. Capability not found (suggest alternative or escalate)
  5. Autonomy gate violation (block, log, escalate)
  6. Network timeout (retry with backoff)
  7. Invalid input (return helpful error)
  8. Security violation (deny, log, escalate)
  9. Data inconsistency (registry mismatch)
  10. Performance degradation (latency alert)
- [ ] Done: All 10 handled gracefully
- **Model:** Sonnet (error handling)
- **Risk:** Unhelpful error messages, silent failures
- **Verify:** Each failure logged with actionable guidance

**4.1c: Regression testing (0.5 hours)**
- [ ] Re-run Week 1-3 evals to confirm no regressions
- [ ] Verify: 318 agents still present, dispatch ranking consistent, revenue attribution complete
- [ ] Done: All regressions pass
- **Model:** Haiku (regression)
- **Risk:** Silent regression (something broke mid-phase)
- **Verify:** Automated test suite passes

---

#### Task 4.2: Documentation & Wiki Updates (4 hours)

**4.2a: API documentation (1 hour)**
- [ ] Document `/dispatch` endpoint: inputs, outputs, examples
- [ ] Document `/resolve-capability` endpoint
- [ ] Document `/rank-agents` (internal use)
- [ ] Done: OpenAPI spec generated, all endpoints documented
- **Model:** Haiku (documentation)
- **Risk:** Out-of-date docs (don't match implementation)
- **Verify:** Docs match actual API behavior

**4.2b: Registry schema documentation (1 hour)**
- [ ] Document AGENT_REGISTRY.yaml schema with examples
- [ ] Document SKILL_REGISTRY.yaml schema
- [ ] Document TOOL_GATEWAY_REGISTRY.yaml schema
- [ ] Document CAPABILITY_REGISTRY.yaml schema
- [ ] Done: Each registry has schema + examples
- **Model:** Haiku (documentation)
- **Risk:** Schema docs don't match actual YAML
- **Verify:** Sample YAML files validate against schemas

**4.2c: Agent deployment guide (1 hour)**
- [ ] Document how to deploy a new agent to production
- [ ] Steps: 1) Define in AGENT_REGISTRY 2) Implement class 3) Test 4) Wire to dispatch
- [ ] Example: Deploy Lead Qualifier (complete walkthrough)
- [ ] Done: Guide is step-by-step, actionable
- **Model:** Sonnet (explanation)
- **Risk:** Guide incomplete or unclear
- **Verify:** New agent can be deployed following guide

**4.2d: Wiki links & interconnections (1 hour)**
- [ ] Update [[AGENTS_DISCOVERY_INVOCATION_GUIDE]] with Phase 2a results
- [ ] Update [[_MCP/SYSTEMS-INTEGRATION-MASTER]] with 5 solved gaps
- [ ] Add wiki links: agents → capabilities → ventures → revenue
- [ ] Done: All interconnections documented
- **Model:** Haiku (wiki linking)
- **Risk:** Broken links (doc moved, not updated)
- **Verify:** All wiki links resolve

---

#### Task 4.3: Phase 2b Planning (2 hours)

**4.3a: Roadmap (1 hour)**
- [ ] Define Phase 2b (Nov-Dec 2026): 15 operational agents → $200K revenue
- [ ] Identify blockers: What must be true to deploy agents at scale?
- [ ] Example: Need observability (can't monitor 50 agents without logging)
- [ ] Done: Phase 2b roadmap drafted (5-10 line items)
- **Model:** Opus (architecture/planning)
- **Risk:** Phase 2b blocked by unknown dependency
- **Verify:** Roadmap includes risk mitigation

**4.3b: Success metrics (1 hour)**
- [ ] Define how to measure Phase 2a success:
  - ✅ 50 agents deployed by Dec 31
  - ✅ $500K revenue attributed to agents
  - ✅ Zero critical bugs in dispatch/capability resolver
  - ✅ <500ms dispatch latency (p95)
  - ✅ 95%+ revenue attribution completeness
- [ ] Done: Metrics defined, dashboards planned
- **Model:** Haiku (measurement)
- **Risk:** Metrics not measurable
- **Verify:** Each metric tied to observable data source (logs, database, dashboards)

---

## MODEL ROUTING

### By Task Complexity

| Model | Tasks | Rationale |
|-------|-------|-----------|
| **Haiku** | Data collection, boilerplate, validation, measurement, classification | Fast, cheap, deterministic (no reasoning needed) |
| **Sonnet** | Implementation, integration, error handling, reasoning, testing | Good balance of speed/reasoning |
| **Opus** | Architecture, root-cause analysis, planning, multi-file invariants | Expensive, only when reasoning required |

### By Week

| Week | Haiku | Sonnet | Opus | Reasoning |
|------|-------|--------|------|-----------|
| 1 (Registries + Patterns) | 68% | 27% | 5% | Data collection + pattern extraction (more Sonnet for pattern analysis) |
| 2 (Router) | 30% | 60% | 10% | Implementation-heavy, uses awesome-agentic-patterns, architecture decisions |
| 3 (Capability) | 40% | 50% | 10% | Complex routing logic, but mostly engineering |
| 4 (Testing) | 50% | 50% | 0% | Testing + docs, no new architecture |

---

## COST TRACKING

### Budget Allocation (102 hours, $7,800)

| Week | Hours | Model Split | Est. Cost | Notes |
|------|-------|-------------|-----------|-------|
| 1 | 19 | H:70% S:25% O:5% | $1,500 | Registries + awesome-agentic-patterns (routine work) |
| 2 | 20 | H:30% S:60% O:10% | $2,100 | Router implementation (new code, uses patterns) |
| 3 | 18 | H:40% S:50% O:10% | $1,850 | Capability routing (complex) |
| 4 | 12 | H:50% S:50% O:0% | $1,050 | Testing + docs (high volume, low complexity) |
| 5 (Reserve) | 33 | - | $1,300 | Contingency (31% buffer for overruns) |
| **Total** | **102** | **H:47% S:47% O:7%** | **$7,800** | **$100 over, within tolerance** |

### Token Budget (Estimate)

- Haiku: 47 hours × 10K tokens/hr × 2 models avg = ~940K tokens, ~$1,200
- Sonnet: 46 hours × 30K tokens/hr × 2 models avg = ~2.76M tokens, ~$4,500
- Opus: 7 hours × 50K tokens/hr × 1 model = ~350K tokens, ~$2,000

**Total:** ~$7,700 (on budget)

### Tracking Template

Each task completion should log:
```yaml
task: "1.1a: Sample parsing"
model: "haiku"
hours_actual: 0.33
tokens_actual: 8000
cost_actual: $10
success: true
```

---

## RISK MATRIX

| Risk | Impact | Probability | Mitigation | Owner |
|------|--------|-------------|-----------|-------|
| Registry parsing fails on edge cases | Medium | Medium | Sample 10 agents, fix regex | Engineer 1 |
| Dispatch router too slow (<500ms) | High | Low | Load test early (Week 2), optimize queries | Engineer 2 |
| Wrong agent ranked #1 (accuracy <80%) | High | Medium | Validation evals every 2 days, tuning loop | Engineer 1 |
| Revenue attribution broken | High | Medium | End-to-end trace testing (Week 3), audit log | Engineer 2 |
| Multi-agent workflows DAG wrong | Medium | Medium | Unit test DAG dependencies, manual review | DevOps |
| Performance regression (Week 3-4) | Medium | Medium | Weekly load test, latency tracking dashboard | DevOps |
| Capability resolver overfits to research | Low | Low | Test on live agent queries, not just papers | Engineer 1 |

---

## SUCCESS CRITERIA

**Phase 2a is COMPLETE when:**

1. ✅ All 318 agents indexed in AGENT_REGISTRY.yaml (100% coverage)
2. ✅ Dispatch router ranks agents with 90%+ accuracy (9/10 test tasks correct)
3. ✅ Dispatch router latency <500ms (p95)
4. ✅ Revenue attribution complete for 50 deployed agents (95%+ of closed deals attributed)
5. ✅ Zero critical bugs in dispatch/router/capability resolver
6. ✅ 50 agents deployed (10 Oct, 15 Nov, 25+ Dec)
7. ✅ $500K+ revenue attributed to agents by Dec 31
8. ✅ All docs updated, wiki links verified
9. ✅ Phase 2b roadmap approved

---

**Phase 2a kickoff:** Oct 1, 2026  
**Expected completion:** Oct 31, 2026  
**Revenue target:** $500K+ by Dec 31, 2026

