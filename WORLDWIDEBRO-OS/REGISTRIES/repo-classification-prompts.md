# Repository Classification Framework (7 Layers)

**System for classifying 1,400+ repositories into strategic intelligence layers**

Related: [[skill-execution-framework]] | [[VENTURE-MASTER]]

---

## Layer 1: Repository Ingestion Classification

**Purpose:** Understand what each repo does, what problem it solves, technical value, business value.

**Prompt Template:**

```
Analyze this GitHub repository:

REPO: {repo_name}
URL: {repository_url}
README: {first_500_chars_of_readme}
Language: {primary_language}
Stars: {github_stars}

Determine:

1. Primary Purpose
   - What does this repo do in one sentence?

2. Problem Solved
   - What user problem does it address?
   - Who has this problem? (developers, businesses, consumers)

3. Target User
   - Who would benefit most from this tool/library/framework?
   - Job title / Role / Function

4. Technology Stack
   - Primary language(s)
   - Key frameworks/dependencies
   - Infrastructure requirements

5. Dependencies
   - Does this repo require other specific tools/services?
   - Can it run standalone?

6. Inputs & Outputs
   - What data/files does it accept?
   - What does it produce?

7. Business Value
   - Could this be packaged as a product?
   - What's the commercial potential?
   - Revenue model if commercialized: (SaaS, one-time license, open-source with paid support, API service, etc)

8. Technical Value
   - Is this production-ready?
   - Code quality assessment: (Poor / Fair / Good / Excellent)
   - Maintenance status: (Abandoned / Stale / Active / Well-maintained)
   - Is it a learning resource or production asset?

9. Strategic Value
   - Could this become core to our operating system?
   - Does it fill a gap in our infrastructure?
   - Reusability score: (1-10) — can we use this across multiple ventures?

10. Classification
   - Choose ONE primary type:
     * Infrastructure (foundation layer)
     * Platform (multi-venture backbone)
     * Product (standalone commercial)
     * Agent (AI/automation agent)
     * Tool (utility/CLI)
     * Service (API/microservice)
     * Framework (development framework)
     * Library (code library)
     * Dataset (data resource)
     * Template (starter/boilerplate)
     * Workflow (automation pipeline)
     * Learning (educational resource)
     * Archive (deprecated/obsolete)

Provide confidence score (1-10) for this classification.

Explain reasoning in 2-3 sentences.
```

---

## Layer 2: Venture Relevance Scoring

**Purpose:** Score how useful each repo is for our portfolio of 712 ventures.

**Prompt Template:**

```
Given these ventures in sector: {sector}

And this repository: {repo_name}

Score the relevance using this rubric:

SCORING CRITERIA:

1. Can it become a standalone business?
   - YES (8-10 points): This could be a venture on its own
   - PARTIAL (4-7 points): Could work as part of a larger venture
   - NO (1-3 points): Too specialized or not commercial

2. Can it power multiple businesses?
   - YES (8-10 points): >5 of our ventures could use this
   - PARTIAL (4-7 points): 2-4 ventures could use this
   - NO (1-3 points): Only 1 venture might use it

3. Internal productivity value
   - HIGH (8-10 points): Saves us 100+ hours/month
   - MEDIUM (4-7 points): Saves us 20-50 hours/month
   - LOW (1-3 points): Saves us <20 hours/month

4. Revenue potential (if commercialized)
   - HIGH (8-10 points): $50K+/month SaaS potential
   - MEDIUM (4-7 points): $5K-$50K/month potential
   - LOW (1-3 points): <$5K/month or no commercial potential

5. Defensibility (competitive moat)
   - HIGH (8-10 points): Hard to copy, unique IP
   - MEDIUM (4-7 points): Some barriers to entry
   - LOW (1-3 points): Anyone can build this

6. Maintenance burden (cost to maintain)
   - LOW (8-10 points): <5 hours/month to maintain
   - MEDIUM (4-7 points): 5-20 hours/month to maintain
   - HIGH (1-3 points): >20 hours/month or declining health

FINAL TIER CLASSIFICATION:

Total Score:
- 40-50 points = **TIER 1: CRITICAL** (Build around this)
- 30-39 points = **TIER 2: CORE ASSET** (Integrate into system)
- 20-29 points = **TIER 3: USEFUL COMPONENT** (Reference/fork as needed)
- <20 points = **TIER 4: IGNORE** (Not worth our time)
```

---

## Layer 3: Build vs Buy vs Wrap Decision Matrix

**Purpose:** Decide the right action for each repo: Build, Fork, Extend, Wrap, Commercialize, or Ignore.

**Decision Tree:**

```
For repository: {repo_name}

1. Is it production-ready AND maintained actively?
   NO → Archive or learn from it → IGNORE or LEARN
   YES → Continue

2. Does it solve a real problem in our ventures?
   NO → IGNORE
   YES → Continue

3. Can we use it off-the-shelf?
   YES → Use it as-is → USE
   NO → Continue

4. Can we extend it for our needs?
   YES → Fork + extend → FORK + EXTEND
   NO → Continue

5. Can we wrap it with our logic?
   YES → White-label or integrate → WRAP
   NO → Continue

6. Can we commercialize it directly?
   YES → Sell as product or API → COMMERCIALIZE
   NO → Continue

7. Should we rebuild from scratch?
   YES → Use as inspiration only → REBUILD
   NO → ARCHIVED

RECOMMENDATION FORMAT:

ACTION: [USE / FORK / FORK+EXTEND / WRAP / COMMERCIALIZE / REBUILD / LEARN / IGNORE]

REASONING: [Cost analysis, timeline, risk, strategic leverage]

TIMELINE: [If action, when do we implement?]

OWNER: [Who implements this?]
```

---

## Layer 4: Ecosystem Mapping (Relationships)

**Purpose:** Build a knowledge graph showing how repos relate to ventures, capabilities, and each other.

**Node Types:**

```
Repository (this repo)
Project (collection of repos)
Venture (business using this)
Capability (what this enables)
Revenue Stream (how it monetizes)
Technology (what it depends on)
Team (who maintains it)
```

**Relationship Types:**

```
POWERS — This repo powers a venture
ENABLES — This capability is enabled by repo
USES — This repo uses another repo
DEPENDS_ON — This repo depends on another
REPLACES — This obsoletes another approach
GENERATES — This creates revenue stream
AUTOMATES — This automates workflow
MONETIZES — This captures value from...
COMPLEMENTS — Works well with...
CONFLICTS — Incompatible with...
```

**Example Mapping:**

```
LangGraph
  ├─ POWERS → AI Agent Platform (venture)
  ├─ ENABLES → Multi-step reasoning (capability)
  ├─ USES → Python (technology)
  ├─ DEPENDS_ON → LangChain (repo)
  └─ MONETIZES → AI automation revenue (stream)

Chroma
  ├─ POWERS → Memory System (venture)
  ├─ ENABLES → Semantic search (capability)
  ├─ USES → Python (technology)
  ├─ COMPLEMENTS → LangGraph
  └─ MONETIZES → Enterprise licensing (stream)
```

---

## Layer 5: Operating System Mapping

**Purpose:** Determine where each repo belongs in the 15-layer OS architecture.

**OS Categories:**

```
Identity Layer
├─ Authentication
├─ Authorization
└─ User profiles

Knowledge Layer
├─ Information management
├─ Learning resources
└─ Documentation

Memory Layer
├─ State storage
├─ Context management
└─ History tracking

Agent Layer
├─ Agent frameworks
├─ LLM integrations
└─ Autonomous systems

Automation Layer
├─ Workflow engines
├─ Task scheduling
└─ Integration platforms

Communication Layer
├─ Messaging
├─ Real-time updates
└─ Notifications

Analytics Layer
├─ Data aggregation
├─ Metrics calculation
└─ Reporting

Finance Layer
├─ Billing
├─ Revenue tracking
└─ Cost management

Infrastructure Layer
├─ Hosting
├─ Databases
└─ DevOps

Security Layer
├─ Encryption
├─ Compliance
└─ Threat protection

Data Layer
├─ Pipelines
├─ Warehousing
└─ Processing

API Layer
├─ REST/GraphQL
├─ WebSockets
└─ Integration points

Frontend Layer
├─ UI components
├─ Design systems
└─ Web applications

Backend Layer
├─ Business logic
├─ Services
└─ Core systems

AI/ML Layer
├─ Models
├─ Training pipelines
└─ Inference systems
```

**Prompt:**

```
Determine where this repository belongs in the operating system.

REPO: {repo_name}

Choose primary layer(s):
- Could this be part of multiple layers?
- How does it interact with other layers?

LAYER ASSIGNMENT:
- Primary: [Layer]
- Secondary: [Layer] (if applicable)

INTEGRATION POINTS:
- What does this layer depend on?
- What depends on this layer?
```

---

## Layer 6: Technology Stack Tagging

**Purpose:** Tag each repo with its technology to understand our stack composition.

**Tag Categories:**

```
FRONTEND
- React, Vue, Svelte, Angular
- Next.js, Nuxt, Remix
- Tailwind, Material UI
- Electron, Tauri

BACKEND
- Node.js, Python, Go, Rust
- Django, FastAPI, Express
- GraphQL, REST APIs
- Redis, message queues

DATABASE
- PostgreSQL, MongoDB, DuckDB
- Vector databases (Chroma, Pinecone)
- Search (Elasticsearch, MeiliSearch)
- Time-series (InfluxDB, TimescaleDB)

AI/ML
- LangChain, LangGraph
- TensorFlow, PyTorch
- Hugging Face, Anthropic
- OpenAI, Google AI

INFRASTRUCTURE
- Docker, Kubernetes
- AWS, GCP, Vercel
- Supabase, Firebase
- Terraform, Pulumi

AUTOMATION
- n8n, Make, Zapier
- Apache Airflow, Prefect
- GitHub Actions, GitLab CI
- Temporal, Bull

ANALYTICS
- DuckDB, BigQuery
- Grafana, Metabase
- Mixpanel, Amplitude
- PostHog, Plausible
```

---

## Layer 7: Venture Factory Analysis

**Purpose:** Identify which repos can become standalone businesses.

**Prompt:**

```
Assume this repository is an asset to commercialize.

REPO: {repo_name}

Determine:

1. Could it become a business?
   - YES/NO with reasoning

2. Who would buy it?
   - Target customer persona(s)
   - Job title / Industry

3. What problem does it solve?
   - Pain point it addresses
   - Intensity of pain (1-10)

4. Pricing model
   - SaaS subscription? One-time? API-based? White-label?
   - Estimated price point per customer

5. Competition
   - Direct competitors (1-3)
   - Competitive advantages vs them
   - Defensibility score (1-10)

6. Distribution channels
   - How would customers find us?
   - Sales model (direct sales, self-serve, marketplace, etc)

7. Time to revenue
   - How long from today to first paying customer?
   - Milestones: MVP (weeks), Beta (months), Launch (months), $10K ARR (months)

8. Defensibility
   - Patents, trade secrets, network effects?
   - Can competitors copy easily?
   - Switching cost once customer uses it?

CLASSIFICATION:

- **Internal Tool** — Use internally, not for sale
- **Revenue Product** — Standalone product, sell directly
- **Platform** — Multi-sided platform (sellers + buyers)
- **Venture Candidate** — Could be a venture in portfolio
- **Strategic Asset** — Keep as competitive advantage, don't sell

VENTURE BRIEF:

If "Venture Candidate," create 1-paragraph description of how this becomes a venture:
- Problem solved
- Target customer
- Revenue model
- Defensibility
- Potential MRR at scale
```

---

## Master Classification Workflow

**Input:** Repository data
- repo_name, repository_url, description, stars, language, last_commit

**Process:**
1. Run Layer 1 (Classification) for each repo
2. Run Layer 2 (Venture Relevance) for relevant ventures
3. Run Layer 3 (Decision matrix) for top 20%
4. Map Layer 4 (Ecosystem relationships)
5. Assign Layer 5 (OS layer)
6. Tag Layer 6 (Technology)
7. Analyze Layer 7 (Venture candidates)

**Output:** Repository Registry
```csv
repo_name,
primary_type,
classification_confidence,
venture_tier,
decision_action,
os_layer_primary,
os_layer_secondary,
technology_tags,
is_venture_candidate,
venture_potential_mrr,
related_ventures,
ecosystem_relationships,
recommendation,
priority_score
```

---

## Execution Path

**Phase 1A:** Ingest + classify 50 repos manually (calibrate prompts)
**Phase 1B:** Ingest + classify remaining 1,350 repos (automated with Claude)
**Phase 2:** Score venture relevance per sector
**Phase 3:** Build ecosystem graph (Neo4j)
**Phase 4:** Dashboard (which repos power which ventures?)
**Phase 5:** Venture factory pipeline (identify 10-20 new ventures from repos)
