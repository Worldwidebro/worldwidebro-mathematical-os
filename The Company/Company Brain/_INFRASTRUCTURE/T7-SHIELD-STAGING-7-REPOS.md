[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

---
id: INFRA-T7-SHIELD-001
title: "T7 Shield Staging: 7 Strategic Repositories Integration"
aliases: ["T7 Shield 7 Repos", "Strategic Repositories Staging"]
tags: ["t7-shield", "staging", "storage", "repositories", "architecture", "expansion"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[CLAUDE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[_INFRASTRUCTURE/REPO-ANALYSIS-STAGING-06-REPOS|6 Repos Analysis]] | [[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|Device Storage Topology]] | [[13-REPOSITORIES/README|13-REPOSITORIES Master]]

# T7 Shield Staging: 7 Strategic Repositories Integration

**Date:** 2026-09-06  
**Storage:** [[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|/Volumes/T7 Shield]] (1.8TB, 49% full, 957GB available)  
**Purpose:** Stage 7 complementary repositories for [[50-MASTER-CONTROL/50-MASTER-CONTROL|Company Brain]] architecture expansion  
**Authority:** CP-027 (Infrastructure) + CP-031/032/033/034 (New control planes)

---

## THE 7 REPOSITORIES & THEIR ROLES

### Knowledge Layer
- **awesome-harness-engineering** (REFERENCE → ADOPT PATTERNS)
  - Architectural patterns for agent execution harness
  - Token optimization, context engineering, verification, eval frameworks

### Execution Layers
- **Browser Use** (ADOPT)
  - Web automation layer (makes internet executable)
  - Can navigate, click, extract, fill forms → create entities

- **diagram-design** (ADOPT)
  - Visual reasoning + documentation skill
  - 39 diagram types for knowledge representation

### Memory & Context Layers
- **OpenViking** (TRIAL → INTEGRATE)
  - Hierarchical context database (L0/L1/L2 retrieval tiers)
  - Token optimization via tiered context delivery
  - Hierarchical retrieval trajectories

- **agentmemory** (TRIAL → COMPARE)
  - Persistent agent memory across sessions
  - Episodic, semantic, structural memory with MCP hooks
  - Lifecycle, hybrid search, automatic hooks

### Skills Layers
- **Anthropic-Cybersecurity-Skills** (ADOPT SELECTIVELY)
  - 818 skills across 34 security domains
  - Mapped to ATT&CK, NIST CSF, ATLAS, D3FEND, AI RMF, MITRE F3
  - Governable, permission-gated skill execution

- **Scientific-Agent-Skills** (ADOPT SELECTIVELY)
  - 163 research/scientific skills
  - 100+ databases/resources + research workflows
  - Evidence-oriented skill design

---

## T7 SHIELD DEPLOYMENT STRATEGY

### Storage Layout

```
[[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|/Volumes/T7 Shield]]/
│
├── 05_SOFTWARE_FACTORY/
│   └── Repositories/
│       ├── awesome-harness-engineering/     (HARNESS PATTERNS)
│       ├── browser-use/                     (WEB EXECUTION)
│       ├── diagram-design/                  (VISUAL LAYER)
│       ├── openviking/                      (CONTEXT DATABASE)
│       ├── agentmemory/                     (AGENT MEMORY)
│       ├── Anthropic-Cybersecurity-Skills/  (SECURITY SKILLS)
│       ├── scientific-agent-skills/         (RESEARCH SKILLS)
│       │
│       └── company-brain-integration/       (NEW)
│           ├── harness-ontology/
│           ├── skills-registry/
│           ├── context-layer/
│           ├── memory-layer/
│           └── integration-mappings/
│
├── company-brain-data/
│   ├── vectors/                (Qdrant snapshots)
│   ├── graphs/                 (Neo4j exports)
│   └── contexts/               (OpenViking indexed contexts)
│
└── experiments/
    ├── browser-automation/     (Browser Use test runs)
    ├── harness-tests/          (Agent harness patterns)
    ├── skill-execution/        (Skills pipeline testing)
    └── context-optimization/   (Token/latency benchmarks)
```

### Storage Allocation (957GB available)

| Use | Size | Purpose |
|-----|------|---------|
| **7 Repositories** | ~50GB | Source code + dependencies |
| **Integration Code** | ~10GB | Company Brain adapters |
| **Experiment Data** | ~20GB | Test runs, benchmarks |
| **Vector Snapshots** | ~100GB | Qdrant backups |
| **Neo4j Exports** | ~50GB | Knowledge graph backups |
| **Context Indexes** | ~50GB | OpenViking context store |
| **Agent Memory Store** | ~30GB | agentmemory persistence |
| **Research Data** | ~100GB | Scientific agent runs |
| **Buffer** | ~500GB | Growth + temporary work |
| **TOTAL USED** | ~410GB | (43% of 957GB) |

---

## PHASE 1: CLONE & STAGE (This Week)

### Task: Clone All 7 Repositories

```bash
cd /Volumes/T7\ Shield/05_SOFTWARE_FACTORY/Repositories

# Clone in parallel (or sequentially, ~30 min total)
git clone https://github.com/ai-boost/awesome-harness-engineering.git
git clone https://github.com/browser-use/browser-use.git
git clone https://github.com/cathrynlavery/diagram-design.git
git clone https://github.com/volcengine/OpenViking.git
git clone https://github.com/rohitg00/agentmemory.git
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
git clone https://github.com/K-Dense-AI/scientific-agent-skills.git

# Verify all clones
ls -la | grep -E "awesome|browser|diagram|OpenViking|agentmemory|Anthropic|scientific"
```

**Status:** Currently cloning `twentyhq/twenty` on T7 Shield

**ETA:** 30 minutes for all clones to complete

---

## PHASE 2: ANALYZE & MAP (Sep 7-8)

For each repository:

### 1. awesome-harness-engineering
```
Analysis:
├─ Extract: Agent loop patterns
├─ Extract: Context engineering best practices
├─ Extract: Planning/decomposition frameworks
├─ Extract: Verification + evals strategies
└─ Create: HARNESS_ONTOLOGY.yaml

Output:
└─ [[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|/Volumes/T7 Shield]]/company-brain-integration/harness-ontology/
   ├── patterns.yaml
   ├── frameworks.yaml
   └── control-points-mapping.yaml
```

### 2. Browser Use
```
Analysis:
├─ Understand: Browser automation API
├─ Document: Integration points with agents
├─ Plan: Web execution layer connection
├─ Test: Simple browser task (extract company info)
└─ Create: BROWSER_EXECUTION_SPEC.md

Output:
└─ /Volumes/T7 Shield/company-brain-integration/browser-layer/
   ├── api-interface.md
   ├── integration-points.md
   └── test-scripts/
```

### 3. diagram-design
```
Analysis:
├─ Catalog: 39 diagram types
├─ Map: Diagram types to Company Brain use cases
├─ Create: Visual representation ontology
└─ Test: Generate sample diagrams

Output:
└─ /Volumes/T7 Shield/company-brain-integration/visual-layer/
   ├── diagram-taxonomy.yaml
   ├── templates/
   └── generators/
```

### 4. OpenViking
```
Analysis:
├─ Understand: Hierarchical context retrieval
├─ Analyze: Token optimization vs. Qdrant
├─ Plan: Deployment alongside Neo4j + Qdrant
├─ Benchmark: Context retrieval performance
└─ Create: CONTEXT_LAYER_INTEGRATION.md

Output:
└─ /Volumes/T7 Shield/company-brain-integration/context-layer/
   ├── architecture.md
   ├── benchmarks/
   └── integration-spec.md
```

### 5. agentmemory
```
Analysis:
├─ Understand: Persistent memory architecture
├─ Compare: vs. OpenViking, vs. existing Neo4j memory
├─ Plan: Memory tier strategy
├─ Test: Simple agent session persistence
└─ Create: AGENT_MEMORY_SPEC.md

Output:
└─ /Volumes/T7 Shield/company-brain-integration/memory-layer/
   ├── architecture.md
   ├── lifecycle.md
   └── integration-spec.md
```

### 6. Anthropic-Cybersecurity-Skills
```
Analysis:
├─ Catalog: 818 skills across 34 domains
├─ Import: Skill registry into Neo4j
├─ Understand: Framework mappings (ATT&CK, NIST, etc.)
├─ Plan: Permission + governance model
└─ Create: SECURITY_SKILLS_ONTOLOGY.yaml

Output:
└─ /Volumes/T7 Shield/company-brain-integration/skills-registry/
   ├── cybersecurity.yaml
   ├── framework-mappings.yaml
   └── permissions-model.yaml
```

### 7. Scientific-Agent-Skills
```
Analysis:
├─ Catalog: 163 research skills
├─ Understand: Evidence-oriented design
├─ Import: Skill registry
├─ Plan: Research workflow automation
└─ Create: SCIENTIFIC_SKILLS_ONTOLOGY.yaml

Output:
└─ /Volumes/T7 Shield/company-brain-integration/skills-registry/
   ├── scientific.yaml
   ├── research-workflows.yaml
   └── database-integrations.yaml
```

---

## PHASE 3: CREATE INTEGRATION LAYER (Sep 9-10)

### Master Integration Specification

File: `/Volumes/T7 Shield/company-brain-integration/INTEGRATION-SPEC.md`

```yaml
company_brain_v2:
  
  harness:
    source: awesome-harness-engineering
    status: reference_patterns_extracted
    ontology: harness-ontology.yaml
    control_points:
      - agent_loop_design
      - context_engineering
      - planning_framework
      - verification_strategy
      - eval_framework
  
  context_layer:
    primary: OpenViking
    fallback: Qdrant
    status: trial_benchmarking
    features:
      - hierarchical_retrieval (L0/L1/L2)
      - token_optimization
      - retrieval_trajectories
      - hierarchical_context
  
  memory_layer:
    engines:
      - agentmemory (episodic, semantic, structural)
      - Neo4j (persistent relationships)
      - OpenViking (context store)
    status: comparative_testing
  
  skills:
    security:
      source: Anthropic-Cybersecurity-Skills
      count: 818 skills across 34 domains
      frameworks: [ATT&CK, NIST-CSF, ATLAS, D3FEND, AI-RMF, MITRE-F3]
      status: selective_adoption
    
    scientific:
      source: Scientific-Agent-Skills
      count: 163 skills
      databases: 100+
      workflows: research_pipelines
      status: selective_adoption
  
  execution:
    browser:
      source: Browser-Use
      status: ready_to_adopt
      capabilities:
        - navigate
        - click
        - type
        - extract
        - form_fill
    
    visual:
      source: diagram-design
      status: ready_to_adopt
      diagram_types: 39
      use_cases:
        - architecture_documentation
        - process_visualization
        - knowledge_representation
  
  integration_mapping:
    "awesome-harness" → harness_ontology.yaml
    "openviking" → context_layer + memory_layer
    "agentmemory" → agent_memory + persistent_sessions
    "browser-use" → web_execution_tool
    "diagram-design" → visual_communication_skill
    "cybersecurity-skills" → security_skill_domain
    "scientific-skills" → research_skill_domain
```

---

## PHASE 4: EXPANDED COMPANY BRAIN ARCHITECTURE (Sep 11-12)

```
                         COMPANY BRAIN v2
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    KNOWLEDGE              INTELLIGENCE          ACTION
        │                     │                     │
   ┌────┴────┐            ┌────┴────┐         ┌────┴────┐
   │          │            │         │         │         │
 Neo4j    OpenViking    Comp AI    Twenty    ClickUp   Buzz
   │          │       (Research)  (CRM)    (Execution) │
   │          │            │        │          │       │
   └────┬─────┘            │        │          │       │
        │                  │        │          │       │
      GRAPH             MEMORY ←────┴──────────┴───────┘
        │                  │
   Ontology          ┌─────┴─────┐
        │            │           │
   Relationships   Agent     agentmemory
        │          Session      │
        │            │          │
        └────────────┼──────────┘
                     │
                HARNESS
                     │
        ┌────────────┼────────────┐
        │            │            │
      Skills       Tools      Patterns
        │            │            │
   ┌────┴────┐   ┌───┴───┐   ┌───┴────┐
   │    │    │   │   │   │   │  Plan  │
Cyber Sci Design MCP Browser GitHub  Task
                              Decomp

        │                       │
        └───────────────────────┘
                 │
             VERIFICATION
                 │
             FEEDBACK
                 │
           NEO4J (closes loop)
```

---

## NEW ONTOLOGY: AGENT HARNESS

```yaml
# Add to Neo4j as first-class ontology

agent_harness:
  components:
    agent_loop:
      - observation
      - planning
      - action
      - verification
      - feedback
    
    context_engineering:
      - retrieval_strategy
      - context_tier (L0, L1, L2)
      - token_budget
      - compaction
    
    planning:
      - goal_decomposition
      - task_generation
      - dependency_analysis
      - priority_ranking
    
    tool_interface:
      - tool_discovery
      - tool_selection
      - capability_matching
      - execution_contract
    
    skills_management:
      - skill_registry
      - skill_prerequisites
      - skill_permissions
      - skill_verification
    
    memory_management:
      - episodic_memory (sessions)
      - semantic_memory (facts)
      - structural_memory (relationships)
      - experience_replay
    
    verification:
      - output_validation
      - constraint_checking
      - human_review (optional)
      - quality_scoring
    
    evals:
      - correctness
      - efficiency
      - safety
      - alignment
    
    observability:
      - execution_tracing
      - token_tracking
      - latency_monitoring
      - cost_tracking
    
    debugging:
      - step_inspection
      - state_replay
      - error_analysis
      - performance_profiling
    
    human_in_loop:
      - approval_gates
      - override_capability
      - feedback_collection
      - fine_tuning

  relationships:
    Agent -[:USES]-> AgentHarness
    AgentHarness -[:IMPLEMENTS]-> Component
    Component -[:REQUIRES]-> Tool
    Tool -[:PROVIDES]-> Capability
    Skill -[:ENABLES]-> Capability
    Memory -[:STORES]-> Experience
    Context -[:OPTIMIZES]-> TokenUsage
```

---

## STORAGE OPTIMIZATION

### T7 Shield becomes tiered cache:

```
FAST PATH (Local SSD on Mac):
└── Working directories
    ├── Active agents
    └── Current experiments

TIER 1 (T7 Shield, local):
└── Repositories (7 repos + integration code)
└── Experiment results
└── Vector indexes (hot set)
└── Agent memory (recent sessions)

TIER 2 (LaCie, when mounted):
└── Vector snapshots (full set)
└── Neo4j backups
└── Historical data
└── Archive
```

---

## QUICK START: T7 SHIELD STAGING

```bash
# 1. Create directory structure
mkdir -p /Volumes/T7\ Shield/company-brain-integration/{harness-ontology,skills-registry,context-layer,memory-layer,integration-mappings}

# 2. Clone all 7 repos (in parallel)
cd /Volumes/T7\ Shield/05_SOFTWARE_FACTORY/Repositories
for repo in awesome-harness-engineering browser-use diagram-design openviking agentmemory Anthropic-Cybersecurity-Skills scientific-agent-skills; do
  git clone https://github.com/<owner>/$repo.git &
done
wait

# 3. Verify all clones
ls -lh | grep -E "awesome|browser|diagram|OpenViking|agentmemory|Anthropic|scientific"

# 4. Generate analysis
cd /Volumes/T7\ Shield/company-brain-integration
echo "Phase 2: Repository analysis and mapping (starting Sep 7)"

# 5. Create integration spec
touch /Volumes/T7\ Shield/company-brain-integration/INTEGRATION-SPEC.md
```

---

## SUCCESS CRITERIA

✅ **By Sep 12:**
- [ ] All 7 repos cloned to T7 Shield
- [ ] Analysis complete for each repo
- [ ] Integration specification drafted
- [ ] Master ontology updated with Harness + Skills
- [ ] Neo4j schema extended (Agent, Skill, Memory, Context nodes)
- [ ] Phase 1 Buzz deployment complete
- [ ] Ready to begin Phase 2 (Intelligence layer) integration

---

## THIS WEEK'S TIMELINE

| Day | Task | Owner | Storage |
|-----|------|-------|---------|
| **Sep 6 (Now)** | Clone CRM repos | Complete | T7 Shield |
| **Sep 7** | Analyze 7 repos | TBD | T7 Shield |
| **Sep 8** | Create ontology mappings | TBD | T7 Shield |
| **Sep 9** | Integration specification | TBD | T7 Shield |
| **Sep 10** | Neo4j schema extensions | TBD | Mac Studio |
| **Sep 11-12** | Phase 1 Buzz deployment | TBD | LaCie (when mounted) |
| **Sep 13+** | Phase 2 integration begins | TBD | Both drives |

---

## WHAT THIS ENABLES

### Immediate (Sep 12)
- Agent Harness ontology in Neo4j
- Composable skills (security + scientific)
- Hierarchical context retrieval (OpenViking)
- Persistent agent memory (agentmemory)
- Web automation capability (Browser Use)
- Visual reasoning (Diagram Design)

### Phase 2 (Oct 1-31)
- Comp AI CRM feeds skills + context layer
- Twenty creates tasks that auto-generate Buzz rooms
- ClickUp tasks route to appropriate skill domain
- Browser Use agents extract research from web
- Scientific agents run research workflows

### Phase 3 (Nov 1-30)
- Full harness integration
- Multi-layer memory (episodic/semantic/structural)
- Agents operating at token-optimized context tiers
- Complete verification + eval pipeline

### Phase 4 (Dec 1-31)
- Genuine agentic operating system
- 904-repo adoption + monitoring
- Closed-loop knowledge generation
- Full governance + safety controls

---

## DECISION: T7 SHIELD AS STAGING GROUND

**Status:** ✅ YES

T7 Shield becomes the **integration hub** for these 7 repositories:

1. **Storage Ready:** 957GB available (43% allocated)
2. **Location Ready:** `/Volumes/T7 Shield/company-brain-integration/`
3. **Access Ready:** Local + Tailscale accessible
4. **Isolation Ready:** Separate from LaCie (production)

This keeps experiments + integration work off the critical LaCie path while Phase 1 Buzz deployment happens in parallel.

---

**Authority:** CP-027 (Infrastructure) + Strategic Architecture Review  
**Next Action:** Begin cloning 7 repos to T7 Shield (in progress)  
**Follow-up:** Sep 7 - Repository analysis and mapping begins  

