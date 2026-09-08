---
id: INFRA-REPO-ANALYSIS-001
title: "Repository Analysis — 6 Strategic Repositories Staged on [[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|T7 Shield]]"
aliases: ["Repo Analysis 6 Repos", "T7 Staging Repos Analysis"]
tags: ["repositories", "staging", "t7-shield", "harness-engineering", "browser-use", "openviking"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[CLAUDE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[_INFRASTRUCTURE/T7-SHIELD-STAGING-7-REPOS|[[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|T7 Shield]] 7 Repos Integration]] | [[13-REPOSITORIES/README|13-REPOSITORIES Master]] | [[15-SKILLS/README|15-SKILLS Master]]

# Repository Analysis — 6 Strategic Repositories Staged on [[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|T7 Shield]]

**Date:** 2026-09-06  
**Status:** Clones complete, ready for Phase 1C analysis (Sep 7-10)  
**Location:** /Volumes/T7 Shield/company-brain-integration/

---

## REPOSITORY MANIFEST

| Repo | Purpose | Size | Cloned | Status |
|------|---------|------|--------|--------|
| **awesome-harness-engineering** | Agent orchestration patterns | 500MB | ✅ | Analyzing... |
| **browser-use** | Web automation & navigation | 300MB | ✅ | Analyzing... |
| **diagram-design** | Visual reasoning (D2 graphs) | 100MB | ✅ | Analyzing... |
| **openviking** | Hierarchical context retrieval | 400MB | ✅ | Analyzing... |
| **scientific-skills** | Research skills registry (163 items) | 50MB | ✅ | Analyzing... |
| **anthropic-cybersecurity-skills** | Security skills registry (818 items) | 50MB | ✅ | Analyzing... |

---

## ARCHITECTURE QUICK-SCAN (Preliminary)

### 1. awesome-harness-engineering (MetaGPT)

**What it is:**  
- Multi-agent orchestration framework with role-based teams
- Structured workflows for complex reasoning tasks
- State management and memory persistence

**[[50-MASTER-CONTROL/50-MASTER-CONTROL|Company Brain]] Integration Points:**
- [[55-LOOP-ENGINEERING/README|Layer 11: Loop Engineering]] (autonomy patterns)
- [[14-CAPABILITIES/README|Layer 9: Capability Router]] (team composition)
- Agent pool for Phase 1 reposit intelligence

**Quick Facts:**
```
Language: Python 3.9+
Main module: metagpt/
Core: Agent, Role, Team, Memory abstractions
State: Persistent workflow checkpoints
Use case: Multi-agent collaboration chains
```

**Phase 1C Analysis Needed:**
- [ ] Extract 15-component AgentHarness ontology
- [ ] Map to Neo4j schema (Agent, Role, Team nodes)
- [ ] Define Capability Router interface
- [ ] Evaluate for Company Brain agent orchestration

---

### 2. browser-use (Browser Use)

**What it is:**
- Agentic web navigation and automation SDK
- Handles JS-rendered SPAs and complex forms
- Error recovery and click-based interaction

**[[50-MASTER-CONTROL/50-MASTER-CONTROL|Company Brain]] Integration Points:**
- Layer 10: Execution (web-based work)
- Research agents reading web content
- Repository Intelligence Phase 8 (web discovery)

**Quick Facts:**
```
Language: Python 3.11+
Async: Full async/await support
Browser: Playwright-based (with Selenium option)
Spec: Fine-grained DOM element querying
Reliability: Built-in retry and fallback
```

**Phase 1C Analysis Needed:**
- [ ] Extract web-action primitives (click, fill, read, navigate)
- [ ] Create MCP bridge (browser_action tool)
- [ ] Benchmark against Playwright/Puppeteer
- [ ] Define reliability guardrails

---

### 3. diagram-design (D2)

**What it is:**
- Declarative diagram language and renderer
- Text-to-diagram compilation (ASCII art equivalent)
- Automatic layout and styling

**[[50-MASTER-CONTROL/50-MASTER-CONTROL|Company Brain]] Integration Points:**
- Layer 14: Visualization (reasoning artifacts)
- Agent output formatting (visual reasoning)
- Architecture diagrams and knowledge graph visualization

**Quick Facts:**
```
Language: Go + TypeScript
Syntax: Markdown-like diagram declarations
Output: SVG, PNG, PDF
Styling: Built-in themes + custom CSS
Use case: System architecture, flowcharts, entity relationships
```

**Phase 1C Analysis Needed:**
- [ ] Create D2 schema for Neo4j graph visualization
- [ ] Build visual reasoning skill (agent → D2 → image)
- [ ] Benchmark rendering speed
- [ ] Define CI/CD integration points

---

### 4. openviking (llama_index)

**What it is:**
- Vector store abstraction + semantic retrieval
- Hierarchical context assembly (L0/L1/L2)
- Query routing and fallback strategies

**Company Brain Integration Points:**
- Layer 13: Retrieval (Qdrant + semantic search)
- Token-optimized context (L0/L1/L2 hierarchy)
- Context compiler (Neo4j → ranked context)

**Quick Facts:**
```
Language: Python 3.8+
Vector stores: Qdrant, Pinecone, Weaviate, Chroma
Hierarchical retrieval: Tree summarization + RAG
Query routing: LLM-guided context selection
Token budgeting: Compressed + full context modes
```

**Phase 1C Analysis Needed:**
- [ ] Extract hierarchical context architecture (L0/L1/L2)
- [ ] Benchmark token efficiency vs flat retrieval
- [ ] Integrate with existing Qdrant setup
- [ ] Define context compiler specification

---

### 5. scientific-skills (Scientific Agent Skills)

**What it is:**
- 163-item research and data science skill registry
- Task-specific research workflows
- Evidence validation and citation management

**Company Brain Integration Points:**
- Layer 12: Skills (research domain)
- Comp AI research agent skill pool
- Repository Intelligence Phase 4-6 evaluation

**Quick Facts:**
```
Registry size: 163 skills
Categories: Research, Analysis, Validation, Synthesis
Composable: Multi-step research workflows
Validation: Evidence-based reasoning required
Storage: YAML registry + structured metadata
```

**Phase 1C Analysis Needed:**
- [ ] Parse skill registry into Neo4j Skill nodes
- [ ] Map to Company Brain capability taxonomy
- [ ] Create skill composition rules
- [ ] Build research workflow templates

---

### 6. anthropic-cybersecurity-skills (Cybersecurity Skills)

**What it is:**
- 818-item security and compliance skill registry
- Defense, audit, and threat modeling workflows
- Governance and policy automation

**Company Brain Integration Points:**
- Layer 15: Security (policy enforcement)
- Repository Intelligence Phase 7 (security review)
- Threat modeling for venture assessment

**Quick Facts:**
```
Registry size: 818 skills
Categories: Defense, Detection, Investigation, Governance
Composable: Multi-phase security assessments
Standards: NIST, OWASP, CIS Benchmarks
Storage: YAML registry + dependency graph
```

**Phase 1C Analysis Needed:**
- [ ] Parse skill registry into Neo4j Skill nodes
- [ ] Create vulnerability assessment workflow
- [ ] Build security review skill chains
- [ ] Integrate with repo-disposition decision logic

---

## PHASE 1C INTEGRATION TIMELINE (Sep 7-10)

### Sep 7 (Monday) — Architecture Extraction
- [ ] Extract AgentHarness ontology (awesome-harness-engineering)
- [ ] Define Agent, Role, Team Neo4j nodes
- [ ] Scope capability router interface
- [ ] Map 163 + 818 skills to Neo4j Skill nodes

### Sep 8 (Tuesday) — Web & Context Layer
- [ ] Document browser-use action primitives
- [ ] Design web-action MCP bridge
- [ ] Extract hierarchical context architecture (L0/L1/L2)
- [ ] Benchmark context token efficiency

### Sep 9 (Wednesday) — Visualization & Workflow
- [ ] Design D2 schema for Neo4j visualization
- [ ] Create visual reasoning skill (agent → D2 → SVG)
- [ ] Build research workflow templates
- [ ] Create security assessment skill chains

### Sep 10 (Thursday) — Integration Specification
- [ ] Write INTEGRATION-SPEC.md (master document)
- [ ] Define Neo4j schema additions (40+ relationships)
- [ ] Create MCP tool interfaces (6 new tools)
- [ ] Document implementation order (Phase 1-4)

---

## NEO4J SCHEMA EXTENSIONS (Preview)

**New Node Types:**
```cypher
(:Agent {name, framework, role})
(:Skill {name, domain, composable, requires[]})
(:Task {name, workflow_id, dependencies[]})
(:Memory {type, scope, ttl})
(:Context {level, tokens, compressed})
(:Workflow {name, phase, domain})
```

**New Relationship Types:**
```cypher
ORCHESTRATES (Agent → Skill)
REQUIRES (Skill → Skill)
DEPENDS_ON (Task → Task)
RETRIEVES (Agent → Context)
USES (Agent → Memory)
OUTPUTS (Workflow → Task)
```

**Example Query (Hybrid Search):**
```cypher
MATCH (agent:Agent)-[:ORCHESTRATES]->
  (skill:Skill)-[:REQUIRES]->(dep:Skill)
WHERE agent.framework = "awesome-harness"
WITH skill, count(dep) as complexity
ORDER BY complexity DESC
LIMIT 10
RETURN skill.name, complexity
```

---

## DEPENDENCY SEQUENCE

```
awesome-harness-engineering
    ↓ (agent patterns)
    ├─→ browser-use (agent actions)
    ├─→ scientific-skills (agent skills)
    └─→ anthropic-cybersecurity-skills (agent skills)

openviking
    ↓ (context retrieval)
    └─→ Neo4j (context assembly)

diagram-design
    ↓ (visualization)
    └─→ Agent output (reasoning artifacts)
```

---

## SUCCESS CRITERIA (Sep 12)

- [ ] ✅ 6 repos analyzed and documented
- [ ] ✅ AgentHarness ontology extracted (15 components)
- [ ] ✅ 981 skills (163 + 818) mapped to Neo4j
- [ ] ✅ Web-action and context architectures specified
- [ ] ✅ INTEGRATION-SPEC.md complete (Phase 1-4 implementation plan)
- [ ] ✅ Neo4j schema ready for loading
- [ ] ✅ MCP tools specified (6 new tools)

---

## BLOCKER WATCHING (Sep 7-10)

| Item | Status | Action Required |
|------|--------|-----------------|
| LaCie mount | 🔴 Still pending | User connects USB-C + mounts |
| Buzz Phase 1 | ⏸️ Blocked | Starts once LaCie mounted |
| CRM eval | ⏳ In progress | trycompai-crm + twenty cloning now |
| 6 repo analysis | 🟢 Ready | Start Sep 7 AM |

---

## NEXT HANDOFF

**From:** Infrastructure Team (Task C complete)  
**To:** Architecture Team (Phase 1C analysis begins Sep 7)  
**Deliverable:** INTEGRATION-SPEC.md (Sep 10 delivery)  
**Unblocks:** Phase 2 CRM deployment (Oct 1)

---

**Created:** 2026-09-06 20:50  
**Authority:** CP-027 (Infrastructure Control Plane)
