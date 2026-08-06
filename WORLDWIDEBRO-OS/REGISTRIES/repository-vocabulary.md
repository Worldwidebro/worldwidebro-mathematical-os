---
name: WORLDWIDEBRO-OS/REGISTRIES/repository-vocabulary
title: Repository Classification Vocabulary
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Repository Classification Vocabulary

**Unified semantic vocabulary for classifying 1,400+ repositories**

Used by: `repo-classification-prompts.md` | `repo_classification_phase1.py`

---

## Identity Vocabulary

How we name and categorize repository types.

```
REPOSITORY CONTAINER TYPES:
- Repository (raw code)
- Project (organized repos)
- Codebase (single system)
- Package (distributable)
- Module (functional unit)
- Component (UI/system piece)
- Application (standalone)
- Service (API/microservice)
- System (collection of services)
- Platform (multi-service backbone)
- Product (commercial offering)
- Library (reusable code)
- Framework (development framework)
- Toolkit (tool collection)
- SDK (software development kit)
- Template (starter code)
- Boilerplate (code skeleton)
- Starter Kit (pre-configured project)
```

---

## Capability Vocabulary

What the repository actually does (functional capabilities).

```
CORE CAPABILITIES:
- Authentication (user identity verification)
- Authorization (permission control)
- Payments (transaction processing)
- Search (information retrieval)
- Storage (data persistence)
- Messaging (inter-process communication)
- Analytics (data analysis & insights)
- Automation (workflow execution)
- Monitoring (system observability)
- Logging (event tracking)
- Reporting (data visualization)
- Scheduling (task timing)
- Workflows (process orchestration)

AI CAPABILITIES:
- LLM Integration (language model usage)
- Embedding Generation (vector creation)
- Vector Storage (embedding persistence)
- RAG (retrieval-augmented generation)
- Agent Framework (autonomous systems)
- Tool Calling (function invocation)
- Prompting (instruction engineering)
- Memory Management (context storage)
- Reasoning (multi-step logic)
- Inference (prediction execution)
- Fine Tuning (model customization)
- Evaluation (quality assessment)
- MCP (Model Context Protocol)
- Knowledge Graph (relationship mapping)
```

---

## Technology Stack Vocabulary

What technologies this repo uses.

```
LANGUAGES:
- Python
- TypeScript / JavaScript
- Rust
- Go
- Java
- C++
- Kotlin
- Swift
- Dart

FRONTEND:
- React, Vue, Angular, Svelte
- Next.js, Nuxt, Remix
- Tailwind, Material UI, shadcn/ui
- Electron, Tauri

BACKEND:
- Node.js, Express, NestJS
- FastAPI, Django, Flask
- Go (chi, gin, fiber)
- Rust (Actix, Axum)
- Spring Boot, Quarkus

DATABASE:
- PostgreSQL, MySQL
- MongoDB, CouchDB
- DuckDB (analytics)
- Redis (cache)
- Supabase (backend-as-service)

VECTOR & AI:
- Chroma (vector DB)
- Pinecone (vector DB)
- Weaviate (vector DB)
- LangChain (LLM orchestration)
- LangGraph (agent framework)
- Ollama (local LLM)

INFRASTRUCTURE:
- Docker, Kubernetes
- AWS, GCP, Azure
- Vercel, Netlify, Railway
- Cloudflare, Digital Ocean

AUTOMATION:
- n8n (low-code automation)
- Zapier (cloud automation)
- Apache Airflow (workflow)
- Prefect (workflow orchestration)
- GitHub Actions (CI/CD)
- Bull (job queue)
- Temporal (workflow engine)

ANALYTICS & MONITORING:
- Grafana (visualization)
- Metabase (BI)
- Datadog (monitoring)
- Sentry (error tracking)
- PostHog (product analytics)
```

---

## Dependency Vocabulary

How repositories relate to each other.

```
DEPENDENCY RELATIONSHIPS:
- Depends On (requires to function)
- Uses (calls or imports)
- Requires (must be installed)
- Imports (code dependency)
- Extends (builds on top of)
- Implements (conforms to standard)
- Wraps (adds abstraction)
- Integrates (works alongside)
- Embeds (contains inside)
- Calls (function invocation)
- Connects To (network/API call)
```

---

## Ownership & Community Vocabulary

Who maintains and uses the repo.

```
OWNERSHIP:
- Owner (original creator)
- Maintainer (active development)
- Contributor (code additions)
- Author (creator/credit)
- Team (group ownership)
- Organization (company/entity)

CODE FLOW:
- Fork (independent copy)
- Upstream (original repo)
- Downstream (derivative)
- Sponsor (financial support)
- Community (user base)
```

---

## Business Vocabulary

Commercial and strategic meaning.

```
COMMERCIAL CLASSIFICATION:
- Asset (IP or capability)
- Product (sellable offering)
- Feature (component of product)
- Capability (what it enables)
- Platform (multi-use backbone)
- Service (recurring offering)
- Offering (solution package)
- Solution (problem answer)
- IP (intellectual property)

VALUE DRIVERS:
- Revenue Stream (money flow)
- Competitive Advantage (vs competitors)
- Moat (defensible advantage)
- Distribution (customer access)
- Market (target audience)
- Customer (end user)
- Unit Economics (cost per customer)
- CAC (customer acquisition cost)
- LTV (lifetime value)
```

---

## Venture Studio Vocabulary

Strategic classification for 712-venture portfolio.

```
STRATEGIC CLASSIFICATION:
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
```

**Examples:**
```
Supabase → Infrastructure (database + auth backend)
n8n → Automation (workflow orchestration)
LangGraph → Agent Framework (AI capability)
Custom SaaS → Product (revenue generation)
Customer Portal → Revenue Product (direct user interaction)
```

---

## Knowledge Graph Vocabulary

How repositories interconnect in a graph structure.

```
NODE TYPES:
- REPOSITORY (code container)
- PROJECT (repo collection)
- VENTURE (business entity)
- PRODUCT (commercial offering)
- FEATURE (capability unit)
- SYSTEM (collection of services)
- TOOL (utility)
- AGENT (autonomous entity)
- WORKFLOW (process)
- ASSET (capital/IP)
- CAPABILITY (functional ability)
- TEAM (people)
- CUSTOMER (user/buyer)
- REVENUE_STREAM (money flow)

RELATIONSHIP TYPES:
- USES (depends on)
- POWERS (enables)
- ENABLES (makes possible)
- DEPENDS_ON (requires)
- GENERATES (creates)
- IMPLEMENTS (provides)
- AUTOMATES (streamlines)
- REPLACES (obsoletes)
- SUPPORTS (aids)
- MONETIZES (captures value)
- CONNECTS_TO (interfaces)
- COMPLEMENTS (works with)
- COMPETES_WITH (alternative to)
- BUILT_WITH (uses technology)
```

**Example Graph:**
```
LangGraph (REPOSITORY)
├─ POWERS → AI Agent Platform (VENTURE)
├─ ENABLES → Multi-step Reasoning (CAPABILITY)
├─ BUILT_WITH → Python (TECHNOLOGY)
├─ DEPENDS_ON → LangChain (REPOSITORY)
└─ MONETIZES → Enterprise Licensing (REVENUE_STREAM)
```

---

## Repository Analysis Vocabulary

Questions every repo classification should answer.

```
CORE ATTRIBUTES (10 ESSENTIAL):

1. Purpose
   - What is the primary goal?
   - What problem does it solve?

2. Category
   - Identity type (Library, Framework, Product, etc)
   - Venture Studio classification (Infrastructure, Product, etc)

3. Capabilities
   - What can it do? (functional capabilities)
   - What does it enable?

4. Dependencies
   - What does it require?
   - What else needs this?

5. Tech Stack
   - Languages & frameworks
   - Infrastructure requirements

6. Reusability Score
   - Can other projects use this? (1-10)
   - Across how many ventures?

7. Revenue Potential
   - Could this be a product? ($K/month estimate)
   - What's the monetization path?

8. Strategic Value
   - Core to operating system? (1-10)
   - Competitive advantage?

9. Related Ventures
   - Which of 712 ventures use this?
   - Which would benefit?

10. Related Repositories
    - What other repos depend on this?
    - What does this build on?
```

---

## Build vs Buy Vocabulary

Decision framework for repository action.

```
BUILD OPTIONS:
- Build (create from scratch)
- Fork (copy + customize)
- Clone (exact duplicate)
- Reuse (use as-is)
- Extend (add features)
- Integrate (combine with others)
- Wrap (add abstraction layer)
- White Label (rebrand & resell)
- Host (run on our infra)
- License (pay for usage)
- Commercialize (sell directly)
- Archive (stop maintaining)
- Replace (discontinue + remove)
- Retire (sunset)
```

---

## Quality Metrics Vocabulary

How to measure repository health.

```
POPULARITY:
- Stars (GitHub stars count)
- Forks (community copies)
- Watchers (attention)
- Downloads (package usage)
- Traffic (page views)

HEALTH:
- Contributors (team size)
- Open Issues (work backlog)
- Closed Issues (resolved)
- PR Merges (release velocity)
- Commit Frequency (activity level)
- Last Commit (recency)
- Maintenance Status (active/stale/abandoned)

QUALITY:
- Test Coverage (code coverage %)
- Code Quality (lint scores)
- Security Vulnerabilities (CVE count)
- Dependency Health (outdated deps)
- Documentation (completeness)
- Performance (speed/efficiency)

MATURITY:
- Releases (version history)
- Stability (breaking changes)
- Production Ready (yes/no)
- License (legal status)
```

---

## Strategic Repository Taxonomy

Top-level classification for all 1,400 repos.

```
INFRASTRUCTURE (Foundation Layer)
├─ Database (PostgreSQL, MongoDB)
├─ Storage (S3, file systems)
├─ Networking (CDN, DNS, reverse proxy)
├─ Security (encryption, auth, compliance)
└─ Cloud (AWS, GCP, Vercel)

PLATFORM (Multi-Service Backbone)
├─ AI Platform (LLM orchestration, agents)
├─ Agent Platform (autonomous systems)
├─ Automation Platform (workflow engine)
├─ Data Platform (analytics, warehousing)
└─ API Platform (gateway, orchestration)

PRODUCT (Commercial Offering)
├─ SaaS (subscription software)
├─ Marketplace (two-sided)
├─ Internal Tool (ops efficiency)
└─ Customer Portal (user interface)

ASSET (Capital or IP)
├─ SOP (standard operating procedure)
├─ Prompt (AI instruction)
├─ Dataset (training data)
├─ Template (code skeleton)
└─ Workflow (process automation)

VENTURE (Business Entity)
├─ Revenue Generating (active monetization)
├─ Strategic (competitive advantage)
├─ Experimental (testing)
└─ Archived (sunset)
```

---

## Usage in Classification

**Layer 1:** Use Identity, Capability, Tech Stack vocabulary
```
Type: Framework (Identity)
Capabilities: LLM Integration, Agent Framework, Prompting (Capability)
Tech Stack: Python, TypeScript (Tech Stack)
```

**Layer 2:** Use Business, Venture Studio vocabulary
```
Classification: Core Platform (Venture Studio)
Revenue Potential: $50K/month SaaS (Business)
Competitive Advantage: Specialized AI workflows (Business)
```

**Layer 3:** Use Build vs Buy vocabulary
```
Action: FORK + EXTEND (Build vs Buy)
Decision: Fork this repo + add custom capabilities (Action)
```

**Layer 4:** Use Knowledge Graph vocabulary
```
Relationships:
- POWERS → AI Agent Platform (VENTURE)
- DEPENDS_ON → LangChain (REPOSITORY)
- MONETIZES → Enterprise Licensing (REVENUE_STREAM)
```

**Layer 5:** Use Venture Studio, Strategic Taxonomy vocabulary
```
OS Layer: Agent Layer, Memory Layer (Venture Studio)
Strategic Category: Core Platform (Strategic Taxonomy)
```

**Layer 6:** Use Technology Stack vocabulary
```
Tags: Python, FastAPI, PostgreSQL, LangChain, Docker (Tech Stack)
```

**Layer 7:** Use Business, Venture Studio vocabulary + 10 Essential Attributes
```
Venture Candidate: YES
Category: Revenue Product (Strategic)
Revenue Potential: $75K/month (Business)
Reusability: 8/10 (Essential Attribute)
```

---

## Reference

Use this vocabulary when:
- Writing classification prompts
- Parsing classification results
- Building knowledge graphs
- Creating dashboards
- Making venture decisions
- Assigning repositories to ventures
- Identifying new business opportunities

All 1,400 repos should map to this vocabulary for semantic consistency.
