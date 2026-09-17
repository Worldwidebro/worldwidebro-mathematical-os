# Research Intelligence Base

**Domain:** 42-RESEARCH-INTELLIGENCE  
**Purpose:** Transform global research into Company Brain capabilities, experiments, and revenue opportunities  
**Authority:** CP-065 (Knowledge Logic)  
**Updated:** 2026-09-17

---

## Overview

The Research Intelligence Base turns **academic and technical research into business advantages** by:

1. **Discovering** new techniques, models, datasets, benchmarks
2. **Extracting** claims, evidence, code, implementations
3. **Verifying** findings through replication and internal testing
4. **Connecting** research to Company Brain capabilities and ventures
5. **Adopting** validated research into production workflows

This is not "a place to search papers."

This is **research → capability → venture → revenue**.

---

## Architecture

```
GLOBAL RESEARCH ECOSYSTEM
├── arXiv (preprints)
├── Semantic Scholar (citations + embeddings)
├── OpenAlex (scholarly graph)
├── Papers With Code (paper ↔ code mapping)
├── Hugging Face (models + implementations)
├── GitHub (open-source baselines)
└── Industry blogs (state-of-the-art)
    │
    ▼
RESEARCH AGENT
    │
    ├─ DISCOVER: New papers, methods, models
    ├─ EXTRACT: Claims, evidence, code
    ├─ VERIFY: Replicate, validate locally
    └─ LINK: Map to Company Brain
    │
    ▼
COMPANY BRAIN GRAPH
    │
    ├─ NEW CAPABILITY: (method/model/technique)
    ├─ NEW REPOSITORY: (code implementation)
    ├─ NEW AGENT TASK: (workflow integration)
    └─ NEW OPPORTUNITY: (venture application)
    │
    ▼
EXPERIMENT SYSTEM
    │
    ├─ Sandbox testing
    ├─ Benchmark evaluation
    ├─ Replication verification
    └─ Adoption decision
    │
    ▼
ADOPTION DECISION
    │
    ├─ WATCH: Monitor for maturation
    ├─ EXPERIMENT: Pilot in sandbox
    ├─ PILOT: Limited venture deployment
    ├─ ADOPTED: Full integration
    ├─ REJECTED: Not applicable
    └─ SUPERSEDED: Replaced by better approach
    │
    ▼
REVENUE IMPACT
    │
    └─ Capability → Venture → Customer → Revenue
```

---

## 20 Sections

### 01-SOURCES
Research sources (arXiv, Semantic Scholar, OpenAlex, Papers With Code, etc.)  
[[RESEARCH-SOURCE-REGISTRY.yaml|_REGISTRIES/CANONICAL/RESEARCH-SOURCE-REGISTRY.yaml]]

### 02-PAPERS
Tracked academic papers, organized by topic/status

### 03-AUTHORS
Researchers whose work is relevant to Company Brain

### 04-INSTITUTIONS
Universities and labs producing research in Company Brain domains

### 05-TOPICS
Research topic taxonomy (LLMs, RAG, Vision, Robotics, etc.)

### 06-METHODS
Techniques and algorithms discovered through research

### 07-MODELS
Machine learning models introduced in research (architectures, weights)

### 08-DATASETS
Training and evaluation datasets discovered through research

### 09-BENCHMARKS
Evaluation metrics, leaderboards, test suites for research assessment

### 10-REPOSITORIES
Code repositories implementing research (from GitHub, Hugging Face, Papers With Code)

### 11-CLAIMS
Assertions made by researchers (requires evidence to validate)

### 12-EVIDENCE
Empirical data and experiments supporting or refuting claims

### 13-EXPERIMENTS
Controlled tests run on Company Brain infrastructure to validate research

### 14-RESULTS
Outcomes of internal experiments and replication attempts

### 15-HYPOTHESES
Testable predictions about what research could enable

### 16-OPPORTUNITIES
Business or capability opportunities identified from research

### 17-RESEARCH-AGENTS
Agents responsible for discovery, extraction, verification, adoption

### 18-RESEARCH-WORKFLOWS
Processes for moving research from discovery → adoption

### 19-RESEARCH-EVALUATIONS
Assessment of research quality, applicability, and business value

### 20-ADOPTION-DECISIONS
Record of whether/how Company Brain adopts research

---

## The Evidence Hierarchy

```
OBSERVATION
    ↓
SOURCE (arXiv, journal, conference)
    ↓
PAPER (published research)
    ↓
CLAIM (assertion, finding)
    ↓
EVIDENCE (data supporting claim)
    ↓
EXPERIMENT (controlled test)
    ↓
REPLICATION (independent verification)
    ↓
VALIDATED_RESULT (verified, trustworthy)
    ↓
ADOPTED_CAPABILITY (integrated into Company Brain)
    ↓
BUSINESS_OUTCOME (revenue impact)
```

**Key principle:** Don't confuse "paper says this works" with "we tested it and it works for us."

---

## Typed Wikilinks for Research

```markdown
# Research Paper Example

cites::[[Prior Work Paper]]
proposes::[[New Routing Method]]
introduced::[[Graph Attention Network]]
uses-dataset::[[Common Crawl]]
evaluated-on::[[MMLU Benchmark]]
implemented-by-repository::[[GitHub Repo: attention-routing]]
similar-to::[[Connected Paper: Earlier Routing Study]]
enables-capability::[[Capability: Semantic Routing]]
creates-opportunity::[[Opportunity: AI-Native Dispatch System]]

## Adoption Status
adoption-status::[[WATCH - Monitoring for maturation]]
```

---

## Research Agent Responsibilities

### Discovery Agent
- Monitor arXiv for new papers in AI/ML
- Track top research institutions
- Identify breakthrough research
- Alert when papers match Company Brain interests

### Extraction Agent
- Extract claims, methods, models from papers
- Find code implementations (Papers With Code, GitHub)
- Catalog datasets and benchmarks
- Create structured knowledge entries

### Verification Agent
- Download and read papers
- Pull open-source code
- Run benchmark evaluations
- Replicate key findings on local infrastructure

### Connection Agent
- Map research to existing capabilities
- Identify capability gaps
- Link papers to relevant ventures
- Propose business opportunities

### Adoption Agent
- Run pilot experiments in sandboxes
- Measure applicability to Company Brain domains
- Make adoption decisions (watch/pilot/adopted/rejected)
- Integrate adopted research into workflows

### Learning Agent
- Track adoption outcomes
- Measure capability improvements
- Record business impact
- Feed learnings back to research selection

---

## Example: From Research to Revenue

### 1. Discovery
**Paper:** "Retrieval-Augmented Generation Improves LLM Accuracy" (arXiv:2305.xxxxx)

```markdown
proposes::[[Retrieval-Augmented Generation]]
evaluated-on::[[MMLU, TriviaQA Benchmarks]]
implemented-by-repository::[[GitHub: facebook/contriever]]
```

### 2. Extraction
- **Method:** RAG (retriever + generator pipeline)
- **Model:** Contriever (dense retriever)
- **Dataset:** Wikipedia, Common Crawl
- **Benchmark:** MMLU +5.2%, TriviaQA +8.1%
- **Code:** https://github.com/facebook/contriever

### 3. Verification
- Set up local RAG system using Contriever
- Test on Company Brain internal datasets
- Compare against baseline LLM performance
- Measure latency, cost, accuracy tradeoffs

### 4. Connection
```
Research (RAG) 
    ↓
Capability (Knowledge Augmentation)
    ↓
Agent (AI Assistant Agent)
    ↓
Workflow (Customer Question Answering)
    ↓
Venture (LT-005: Medical Courier → Patient Q&A)
    ↓
Revenue ($X per interaction)
```

### 5. Adoption Decision
**Status:** ADOPTED

```markdown
adoption-status::[[ADOPTED - Integrated into AI Assistant]]
deployment-date::2026-10-15
venture-applied-to::[[LT-005: Medical Courier]]
capability-enabled::[[Capability: Patient Knowledge Augmentation]]
business-impact::[[Revenue: +$2K/month from enhanced Q&A]]
improvement-over-baseline::[[+12% customer satisfaction]]
```

### 6. Revenue
- RAG-powered patient Q&A increases customer retention
- Reduces support costs
- Enables upsell to premium support tier
- Net revenue impact: +$24K/year per venture

---

## Research Status Types

- **WATCH:** Interesting but not yet validated (papers, early research)
- **EXPERIMENT:** Testing in sandbox environment
- **PILOT:** Limited deployment in one venture
- **ADOPTED:** Integrated into standard capabilities
- **REJECTED:** Evaluated but determined not applicable
- **SUPERSEDED:** Replaced by newer/better approach

---

## Connected Domains

- **01-IDENTITY:** Company Brain identity informed by research capabilities
- **30-REVENUE:** Research-to-revenue pathways
- **34-PRODUCT:** New product capabilities from research
- **16-AGENTS:** Research agents and workflows
- **_EVAL:** Evaluation framework for research validation
- **_MEMORY:** Research learning and memory systems
- **_REGISTRIES:** [[RESEARCH-SOURCE-REGISTRY.yaml]] (sources), RESEARCH-REGISTRY.yaml (papers)

---

## Research Control Plane

**Authority:** [[CP-065: Knowledge Logic]]

**Responsibilities:**
- Approve research source additions
- Validate research adoption decisions
- Oversee experiment execution
- Track research-to-revenue impact
- Manage research budget allocation

---

## Quick Start

1. **Check research sources:** [[RESEARCH-SOURCE-REGISTRY.yaml|_REGISTRIES/CANONICAL/RESEARCH-SOURCE-REGISTRY.yaml]]
2. **Read latest papers:** See 02-PAPERS folder
3. **Review adoption pipeline:** See 18-RESEARCH-WORKFLOWS
4. **Check opportunities:** See 16-OPPORTUNITIES (highest-value research applications)
5. **Track impact:** See 20-ADOPTION-DECISIONS and business outcomes

---

## References

- Master Ontology (with research types): [[_ONTOLOGY/RESEARCH-INTELLIGENCE-LAYER.xml]]
- Source Registry: [[_REGISTRIES/CANONICAL/RESEARCH-SOURCE-REGISTRY.yaml]]
- Logic Framework: [[_DOCS/LOGIC-ARCHITECTURE-FRAMEWORK.md]] (Logic-065: Knowledge Logic)
- Integration Guide: [[_DOCS/TYPED-WIKILINKS-GUIDE.md]]

---

**Principle:** Every paper, model, benchmark, and dataset in the research ecosystem has potential to become a Company Brain capability. Our job is to systematically identify, verify, and convert that potential into measurable business value.

