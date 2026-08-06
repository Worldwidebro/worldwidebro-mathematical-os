# Repository Classification Framework (7 Layers + Vocabulary)

**System for classifying 1,400+ repositories into strategic intelligence layers**

Related: [[REPOSITORY-INTELLIGENCE-SYSTEM]] | [[repository-vocabulary]] | [[skill-execution-framework]] | [[VENTURE-MASTER]]

---

## Architecture: 7-Level Repository Intelligence Pipeline

```
Level 1: Raw Repositories (GitHub)
    ↓
Level 2: Repository Registry (Metadata extraction)
    ↓
Level 3: Repository Intelligence (AI summaries)
    ↓
Level 4: Embeddings + RAG (Searchable intelligence)
    ↓
Level 5: Knowledge Graph (Relationships + graph queries)
    ↓
Level 6: Repo-to-Venture Mapping (Strategic assignments)
    ↓
Level 7: Strategic Queries (Decision intelligence)
```

**This Classification System:** Implements Levels 2-3, outputs ready for Levels 4-5.

---

## Vocabulary Foundation

**Reference:** [[repository-vocabulary]]

All classifications use unified vocabulary from:
- Identity Vocabulary (container types)
- Capability Vocabulary (what it does)
- Technology Stack Vocabulary (how it's built)
- Business Vocabulary (commercial meaning)
- Venture Studio Vocabulary (strategic classification)
- Knowledge Graph Vocabulary (relationships)

---

## Layer 1: Repository Ingestion Classification

**Purpose:** Understand what each repo does using unified vocabulary (Level 2-3)

**Vocabulary References:** Identity | Capability | Technology Stack | Business

**Prompt Template:**

```
Analyze this GitHub repository using UNIFIED VOCABULARY:

REPO: {repo_name}
URL: {repository_url}
README: {first_500_chars}
Language: {primary_language}
Stars: {github_stars}

---

PART A: IDENTITY & PURPOSE

1. Container Type (from Identity Vocabulary)
   Choose: Repository | Project | Package | Module | Application | Service | 
   Platform | Product | Library | Framework | Toolkit | SDK | Template | 
   Boilerplate | Starter Kit

2. Primary Purpose
   What does this repo do? (one sentence)
   What problem does it solve?

3. Target Audience
   Who uses this? (developers / businesses / consumers)
   Job role / Function

---

PART B: CAPABILITIES & TECHNICAL VALUE

4. Capabilities (from Capability Vocabulary)
   List from: Authentication, Authorization, Search, Storage, Messaging, 
   Analytics, Automation, Monitoring, Logging, Reporting, Scheduling, 
   Workflows, LLM Integration, Embedding, Vector Storage, RAG, Agent Framework,
   Tool Calling, Prompting, Memory Management, Inference, Knowledge Graph

5. Technology Stack (from Technology Stack Vocabulary)
   Languages: {Python | TypeScript | Rust | Go | Java | etc}
   Frameworks: {React | FastAPI | Django | etc}
   Databases: {PostgreSQL | MongoDB | DuckDB | Chroma | etc}
   Infrastructure: {Docker | Kubernetes | AWS | Vercel | etc}
   Key dependencies: [main external tools]

6. Dependencies (from Dependency Vocabulary)
   Uses | Requires | Extends | Integrates | Depends On [list]
   Standalone: (Yes / No)
   Needed by: [what else depends on this?]

---

PART C: BUSINESS & STRATEGIC VALUE

7. Business Classification (from Business Vocabulary)
   Type: Asset | Product | Feature | Capability | Platform | Service | Solution | IP
   Commercial Potential: None | Low | Medium | High
   Monetization Path: SaaS | One-time | API | White-label | Licensing

8. Venture Studio Classification (from Venture Studio Vocabulary)
   Choose ONE: 
   - Infrastructure (foundation layer)
   - Shared Service (multi-venture tool)
   - Core Platform (backbone system)
   - Internal Tool (ops efficiency)
   - Automation (workflow engine)
   - Product (revenue generation)
   - Revenue Product (direct sales)
   - Venture (business entity)
   - Portfolio Asset (capital asset)
   - Strategic Asset (competitive advantage)

9. Essential Attributes (10 Core)
   1. Purpose: [summarize primary goal]
   2. Category: [Identity type + Venture Studio type]
   3. Capabilities: [list from Capability Vocabulary]
   4. Dependencies: [what does it need?]
   5. Tech Stack: [languages + frameworks]
   6. Reusability Score: (1-10) [across ventures]
   7. Revenue Potential: ($K/month estimate)
   8. Strategic Value: (1-10) [core to OS?]
   9. Related Ventures: (which of 712?)
   10. Related Repositories: [dependencies]

10. Final Classification
    - Identity Type: [from Container Types]
    - Venture Studio Type: [from Strategic Classification]
    - Technical Quality: Poor | Fair | Good | Excellent
    - Maintenance: Abandoned | Stale | Active | Well-maintained
    - Production Ready: Yes | No | Partial
    - Confidence Score: (1-10)
    - Reasoning: (2-3 sentences)
```

---

## Layer 2: Venture Relevance Scoring

**Purpose:** Score repository value for 712-venture portfolio

**Scoring Criteria:**

```
1. Standalone Business Potential (1-10)
   YES (8-10) | PARTIAL (4-7) | NO (1-3)

2. Powers Multiple Ventures (1-10)
   >5 ventures (8-10) | 2-4 ventures (4-7) | 1 venture (1-3)

3. Internal Productivity Value (1-10)
   >100 hours/month (8-10) | 20-50 hours (4-7) | <20 hours (1-3)

4. Revenue Potential (1-10)
   $50K+/month (8-10) | $5K-$50K/month (4-7) | <$5K/month (1-3)

5. Defensibility/Moat (1-10)
   Hard to copy (8-10) | Some barriers (4-7) | Anyone can build (1-3)

6. Maintenance Burden (1-10, inverted)
   <5 hours/month (8-10) | 5-20 hours (4-7) | >20 hours (1-3)

TIER CLASSIFICATION:
- 40-50 = TIER 1: CRITICAL (Build around)
- 30-39 = TIER 2: CORE ASSET (Integrate)
- 20-29 = TIER 3: USEFUL (Reference/fork)
- <20 = TIER 4: IGNORE
```

---

## Layer 3: Build vs Buy vs Wrap Decision

**Purpose:** Decide action for each repo

**Decision Tree:**

```
Production-ready & maintained?
├─ NO → IGNORE or LEARN
└─ YES ↓

Solves real venture problem?
├─ NO → IGNORE
└─ YES ↓

Use off-the-shelf?
├─ YES → USE
└─ NO ↓

Can extend/fork?
├─ YES → FORK + EXTEND
└─ NO ↓

Can wrap?
├─ YES → WRAP
└─ NO ↓

Commercialize directly?
├─ YES → COMMERCIALIZE
└─ NO ↓

Rebuild from scratch?
├─ YES → REBUILD
└─ NO → ARCHIVED

ACTIONS:
- USE: As-is
- FORK: Minor tweaks
- FORK+EXTEND: Significant features
- WRAP: White-label/integrate
- COMMERCIALIZE: Sell directly
- REBUILD: Use as inspiration
- LEARN: Educational only
- IGNORE: Not worth time
```

---

## Layer 4: Ecosystem Mapping

**Purpose:** Build relationship graph using Knowledge Graph vocabulary

**Node Types:** REPOSITORY | PROJECT | VENTURE | PRODUCT | CAPABILITY | SYSTEM | TOOL | AGENT | WORKFLOW | ASSET | TEAM | CUSTOMER | REVENUE_STREAM

**Relationship Types:** USES | POWERS | ENABLES | DEPENDS_ON | GENERATES | IMPLEMENTS | AUTOMATES | REPLACES | MONETIZES | CONNECTS_TO | COMPLEMENTS | COMPETES_WITH | BUILT_WITH

**Example:**
```
LangGraph (REPOSITORY)
├─ POWERS → AI Agent Platform (VENTURE)
├─ ENABLES → Multi-step Reasoning (CAPABILITY)
├─ BUILT_WITH → Python (TECHNOLOGY)
├─ DEPENDS_ON → LangChain (REPOSITORY)
└─ MONETIZES → Enterprise Licensing (REVENUE_STREAM)
```

---

## Layer 5: Operating System Mapping

**Purpose:** Assign each repo to OS layer

**OS Layers:**
- Identity, Knowledge, Memory, Agent, Automation, Communication
- Analytics, Finance, Infrastructure, Security, Data
- API, Frontend, Backend, AI/ML

**Classification:**
```
Primary OS Layer: [one layer]
Secondary Layer: [if applicable]
Integration Points: [how it connects]
```

---

## Layer 6: Technology Stack Tagging

**Purpose:** Tag with Technology Stack vocabulary

**Format:** Comma-separated
```
python,fastapi,postgresql,langchain,docker,grafana
```

---

## Layer 7: Venture Factory Analysis

**Purpose:** Identify venture candidates

**Questions:**
```
1. Could this become a business? (YES/NO)
2. Who would buy it? (persona)
3. What problem? (pain point + intensity)
4. Pricing model? (SaaS | One-time | API | White-label)
5. Competition? (1-3 competitors + defensibility)
6. Distribution? (how customers find us)
7. Time to revenue? (MVP weeks → $10K ARR)
8. Defensibility? (patents, network effects)

CLASSIFICATION:
- Internal Tool, Revenue Product, Platform
- Venture Candidate, Strategic Asset

IF VENTURE CANDIDATE:
- Estimated MRR: $[X]K
- Venture Brief: (one paragraph)
```

---

## Execution Workflow

```
Input: Repository data
  ├─ repo_name, url, description, language, stars
  
Process: 7-Layer Classification
  ├─ Layer 1: Ingestion (Identity, Capability, Tech, Business)
  ├─ Layer 2: Venture Relevance (Scoring + Tiering)
  ├─ Layer 3: Build/Buy/Wrap (Decision)
  ├─ Layer 4: Ecosystem (KG relationships)
  ├─ Layer 5: OS Mapping (Layer assignment)
  ├─ Layer 6: Tech Tagging (Stack)
  └─ Layer 7: Venture Factory (Opportunity)

Output: Repository Registry
  ├─ CSV: 10+ columns
  ├─ JSON: Full analysis
  └─ Knowledge Graph: Relationships
```

---

## Related Files

- [[repository-vocabulary]] — Complete vocabulary reference
- [[REPOSITORY-INTELLIGENCE-SYSTEM]] — Master overview + plan
- repo_classification_phase1.py — Execution script
- repository-intelligence-registry.csv — Output summary
- repository-intelligence-detailed.json — Output full
