---
references:
  - [[VENTURE-MASTER]]
  - REPOSITORY-INTELLIGENCE-SYSTEM-2026-06-11
---

# REPOSITORY INTELLIGENCE VOCABULARY
**Purpose:** Rich vocabulary for analyzing repos as business assets, not just code containers.

**Core principle:** A repository is **a container of capabilities, assets, knowledge, workflows, and business value.**

---

## THE 10 CORE ATTRIBUTES

If you only tracked 10 fields per repository, these are the 10:

```
1. PURPOSE
   What does this repository exist to do? (One sentence)
   Example: "Chroma stores vector embeddings for semantic search"

2. CATEGORY
   Venture Studio classification
   (Infrastructure, Shared Service, Core Platform, Internal Tool, 
    Automation, Product, Revenue Product, Venture, Portfolio Asset, 
    Strategic Asset)
   Example: "Infrastructure (Database)"

3. CAPABILITIES
   What can it do? (3-5 primary capabilities)
   Example: ["Vector storage", "Semantic search", "Embedding management"]

4. DEPENDENCIES
   What does it need to work? (Other repos/services)
   Example: ["PostgreSQL", "OpenAI API", "Python 3.8+"]

5. TECH STACK
   What is it built with? (Languages, frameworks)
   Example: ["Python", "FastAPI", "Pydantic"]

6. REUSABILITY
   How many ventures use this? (1-10 score)
   Example: 9 (used by 700+ ventures)

7. REVENUE_POTENTIAL
   Could this be commercialized? (Annual revenue if spun out)
   Example: "$500K-2M/year"

8. STRATEGIC_VALUE
   Does this enable other ventures? (What it unlocks)
   Example: "Powers memory layer for AI ventures, enables RAG"

9. RELATED_VENTURES
   Which ventures use this? (Venture IDs)
   Example: ["EDU-013", "CON-011", "FIN-001", ...]

10. RELATED_REPOS
    What other repos does it connect to? (Dependencies/integrations)
    Example: ["LangChain", "OpenAI-SDK", "LangGraph"]
```

---

## VENTURE STUDIO VOCABULARY (Most Important)

How does this repository serve your ventures?

```
INFRASTRUCTURE
├── Database (PostgreSQL, Supabase, Redis)
├── Storage (S3, file systems)
├── Networking (DNS, CDN, firewalls)
├── Security (auth, encryption)
├── Cloud (hosting, deployment)
└── DevOps (CI/CD, containers)

SHARED SERVICE
├── Authentication (Supabase Auth)
├── Payments (Stripe)
├── Email (Resend)
├── Analytics (DuckDB, Grafana)
└── Logging (Sentry, LogRocket)

CORE PLATFORM
├── AI Platform (LLM, embeddings)
├── Agent Platform (LangGraph, decision)
├── Automation Platform (n8n, Temporal)
├── Data Platform (Chroma, LightRAG)
└── Workflow Platform (orchestration)

INTERNAL TOOL
├── Build tools (CLI, utility)
├── Admin tools (management, config)
├── Testing tools (QA, benchmarks)
└── Development tools (DevX, debugging)

AUTOMATION
├── Workflow automation (n8n)
├── Data pipeline (ETL)
├── Process automation (scheduling)
└── Integration automation (API bridges)

PRODUCT
├── SaaS (subscription revenue)
├── Marketplace (transaction fees)
├── API (consumption-based)
└── Software (one-time purchase)

REVENUE PRODUCT
├── Direct customer revenue (paid users)
├── Affiliate revenue (commissions)
├── Commission revenue (take rate)
└── Licensing revenue (IP)

VENTURE
├── Portfolio business (standalone)
├── Revenue generating (profitable)
├── Strategic (enables ventures)
├── Experimental (proof-of-concept)
└── Archived (retired)

PORTFOLIO ASSET
├── Strategic asset (critical)
├── Intellectual asset (IP)
├── Reusable asset (multi-venture)
└── Knowledge asset (documentation)

STRATEGIC ASSET
├── Competitive moat (hard to replicate)
├── Irreplaceable (can't buy)
├── Core to business (revenue driver)
└── Foundation for growth (scales ventures)
```

---

## CAPABILITY VOCABULARY

What can this repository DO?

```
AUTHENTICATION
├── Login/signup
├── OAuth/social auth
├── Multi-factor auth
├── Session management
└── Password reset

AUTHORIZATION
├── Role-based access (RBAC)
├── Permission management
├── API keys
└── Scope-based access

STORAGE & DATA
├── Database operations (CRUD)
├── File storage
├── Object storage
├── Cache layer
├── Data versioning
└── Backup/recovery

SEARCH & DISCOVERY
├── Full-text search
├── Semantic search
├── Vector search
├── Filtering/faceting
└── Ranking/scoring

AI & REASONING
├── LLM integration
├── Embedding generation
├── Vector storage
├── RAG (retrieval-augmented)
├── Agent orchestration
├── Tool calling
├── Prompt engineering
├── Memory/context
└── Decision making

AUTOMATION & WORKFLOWS
├── Workflow definition
├── Job scheduling
├── Task execution
├── Event-driven actions
├── Integration bridges
└── API orchestration

PAYMENTS & BILLING
├── Payment processing
├── Subscription management
├── Invoice generation
├── Revenue recognition
├── Refunds/disputes
└── Analytics

COMMUNICATION
├── Email sending
├── SMS
├── Push notifications
├── Webhooks
├── Message queuing
└── Real-time sync

ANALYTICS & REPORTING
├── Event tracking
├── User analytics
├── Business metrics
├── Dashboard/visualization
├── Data export
└── Report generation

MONITORING & OBSERVABILITY
├── Application logging
├── Error tracking
├── Performance monitoring
├── Alerting
├── Distributed tracing
└── Health checks

CONTENT MANAGEMENT
├── Document storage
├── Version control
├── Publishing workflow
├── Content preview
├── SEO optimization
└── Multi-language support
```

---

## AI VOCABULARY (LLM-Specific)

Specialized capabilities for AI systems:

```
LLM
├── Model (GPT-4, Claude, Llama)
├── API (inference endpoint)
├── Fine-tuning (custom model)
└── Prompt engineering

EMBEDDING
├── Embedding generation (text → vector)
├── Embedding model (semantic)
├── Dimension (vector size)
└── Similarity search

VECTOR STORE
├── Storage (Chroma, Pinecone)
├── Indexing (fast lookup)
├── Retrieval (semantic search)
└── Scaling (millions of vectors)

RAG (RETRIEVAL-AUGMENTED GENERATION)
├── Knowledge base (documents)
├── Retrieval (find context)
├── Augmentation (inject into prompt)
└── Generation (LLM response)

AGENT
├── Agent framework (LangGraph)
├── Tool calling (function calls)
├── Planning (multi-step reasoning)
├── Execution (taking actions)
└── Feedback loop (learning)

MEMORY
├── Short-term (conversation history)
├── Long-term (vector store, graph)
├── Context window (token limits)
└── Retention (important info)

EVALUATION
├── Benchmark (test suite)
├── Metric (accuracy, latency)
├── Human evaluation (quality)
└── Automated evaluation (scoring)

MCP (MODEL CONTEXT PROTOCOL)
├── Server (tool provider)
├── Resource (documents, APIs)
├── Tool (callable function)
└── Integration (connect to Claude)

KNOWLEDGE GRAPH
├── Entities (people, places, things)
├── Relationships (connections)
├── Inference (reasoning)
└── Semantic understanding (meaning)
```

---

## BUSINESS VOCABULARY

Commercial/financial perspective:

```
ASSET
├── Intellectual property
├── Proprietary code
├── Trade secrets
├── Customer data
└── Market position

PRODUCT
├── MVP (minimum viable)
├── Growth stage (scaling)
├── Mature (stable revenue)
├── Declining (sunset)
└── Experimental (proof of concept)

FEATURE
├── Core feature (required)
├── Advanced feature (premium)
├── Nice-to-have (optional)
└── Deprecated (being removed)

SERVICE
├── SaaS (recurring subscription)
├── API (consumption-based)
├── Professional services (labor)
├── Managed service (hands-off)
└── Consulting (expertise)

OFFERING
├── Freemium (free + paid)
├── Premium (paid only)
├── Enterprise (custom pricing)
├── Open source (free)
└── Hybrid (multiple models)

IP (INTELLECTUAL PROPERTY)
├── Patent (legal protection)
├── Copyright (automatic)
├── Trade secret (confidential)
├── Trademark (brand)
└── License (permission to use)

REVENUE STREAM
├── Subscription (recurring)
├── Transaction fee (per use)
├── Commission (affiliate)
├── Advertising (attention)
├── Licensing (IP rental)
└── Markup (resale)

DISTRIBUTION CHANNEL
├── Direct sales (customer relationship)
├── Self-serve (online, no sales)
├── Marketplace (third-party)
├── Partnership (OEM, reseller)
├── Community (open source)
└── API (developer integration)

COMPETITIVE ADVANTAGE
├── Cost advantage (cheaper)
├── Speed advantage (faster)
├── Quality advantage (better)
├── Brand advantage (reputation)
├── Network advantage (users attract users)
└── Data advantage (proprietary insights)

MOAT (DEFENSIBILITY)
├── Technical moat (hard to replicate)
├── Network effect (more valuable with users)
├── Switching costs (expensive to leave)
├── Brand moat (customer loyalty)
├── Data moat (proprietary dataset)
└── Regulatory moat (compliance barrier)
```

---

## KNOWLEDGE GRAPH VOCABULARY

How repos connect to ventures:

```
NODE TYPES
├── REPOSITORY (code)
├── PROJECT (initiative)
├── VENTURE (business)
├── PRODUCT (customer-facing)
├── FEATURE (capability)
├── SYSTEM (integrated)
├── TOOL (utility)
├── AGENT (autonomous)
├── WORKFLOW (automation)
├── ASSET (knowledge/data)
└── CUSTOMER (user)

RELATIONSHIP TYPES
├── USES (A uses B)
├── POWERS (A powers B)
├── ENABLES (A enables B)
├── DEPENDS_ON (A needs B)
├── GENERATES (A creates B)
├── IMPLEMENTS (A realizes B)
├── AUTOMATES (A removes manual steps from B)
├── REPLACES (A supersedes B)
├── SUPPORTS (A enables using B)
├── MONETIZES (A generates revenue from B)
└── CONNECTS_TO (A integrates with B)

EXAMPLE GRAPH
├── LangGraph POWERS → AI-Agent-Stack
├── Chroma POWERS → Memory-Layer
├── n8n AUTOMATES → Customer-Onboarding
├── Supabase POWERS → All-712-Ventures
└── CON-011 USES → Supabase, Resend, Vercel
```

---

## BUILD VS BUY VOCABULARY

Decision framework for each repo:

```
BUILD
├── Build from scratch
├── Build custom integration
└── Build wrapper/extension

FORK
├── Clone and customize heavily
├── Maintain separately
└── Diverge from upstream

REUSE
├── Use as-is
├── Integrate directly
└── Minimal customization

WRAP
├── Add management layer
├── White-label it
├── Host as managed service

EXTEND
├── Add features
├── Enhance capability
└── Customize for ventures

INTEGRATE
├── Connect as service
├── API integration
└── Plug into system

WHITE_LABEL
├── Rebrand for customers
├── Sell as own product
└── Managed service offering

HOST
├── Run internally
├── SaaS wrapper
└── Internal service

LICENSE
├── Buy commercial license
├── Vendor relationship
└── Paid subscription

COMMERCIALIZE
├── Spin out as product
├── Sell to market
├── Create business

ARCHIVE
├── Decommission
├── Retire
└── Historical reference only
```

---

## QUICK DECISION TREE

For each repo:

```
Is this primarily DATA (not code)?
├─ YES → DATASET
└─ NO → Continue

Is this educational/tutorial?
├─ YES → LEARNING
└─ NO → Continue

Is this no longer used?
├─ YES → ARCHIVE
└─ NO → Continue

Is this Infrastructure/Platform?
├─ YES → INFRASTRUCTURE or PLATFORM
└─ NO → Continue

Is this something customers pay for?
├─ YES → PRODUCT
└─ NO → Continue

Is this autonomous/AI decision-making?
├─ YES → AGENT
└─ NO → Continue

Is this a backend service/API?
├─ YES → SERVICE
└─ NO → Continue

Is this automation/orchestration?
├─ YES → WORKFLOW
└─ NO → Continue

Is this a developer tool/framework?
├─ YES → FRAMEWORK or TOOL
└─ NO → PLATFORM or something else
```

---

## ANALYSIS QUESTIONS

Key questions for each repo:

```
IDENTITY
- What is this repository?
- What is its primary purpose?
- Who maintains it?

BUSINESS
- Could this be a product?
- What problem does it solve?
- Who would buy it?

TECHNICAL
- What does it depend on?
- How reusable is it?
- How well-maintained is it?

STRATEGIC
- Does it power other ventures?
- Is it critical infrastructure?
- Can we commercialize it?

OPERATIONAL
- Who uses it?
- How often is it updated?
- What's the maintenance burden?

INTEGRATION
- What other repos does it connect to?
- How does it fit in our OS?
- What ventures use it?

FUTURE
- Is this a 3-year asset?
- Should we invest in it?
- Should we decommission it?
```

---

**This is your complete vocabulary for Repository Intelligence.**

Use it to rebuild Layer 1 with venture/business language instead of git language.

