# LAYER 1: REPOSITORY INGESTION PROMPT
**Purpose:** Analyze any repository and classify it using 12 types + extract 10 key attributes.

**Usage:** Apply this prompt to each repository. Can be automated with API or run manually.

---

## THE 10 CORE ATTRIBUTES (LAYER 1 COMPLETE)

For every repository, fill in these 10 fields:

```
REPOSITORY ANALYSIS

Repository: [repo-name]
GitHub URL: [url]

EXTRACT THESE 10 ATTRIBUTES:

1. PURPOSE
   What does this repository exist to do?
   (One sentence max)
   Example: "Chroma stores vector embeddings for semantic search"

2. CATEGORY
   Which Venture Studio classification?
   Choose ONE: Infrastructure | Shared Service | Core Platform | Internal Tool | 
              Automation | Product | Revenue Product | Venture | Portfolio Asset | 
              Strategic Asset
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

6. REUSABILITY_SCORE
   How many of your 712 ventures use this? (1-10 scale)
   Example: 9 (used by 700+ ventures)

7. REVENUE_POTENTIAL
   Could this be commercialized? (Annual revenue if spun out)
   Example: "$500K-2M/year"

8. STRATEGIC_VALUE
   Does this enable other ventures? (What ventures, what it unlocks)
   Example: "Powers memory layer for AI ventures, enables RAG"

9. RELATED_VENTURES
   Which ventures use this? (Venture IDs)
   Example: ["EDU-013", "CON-011", "FIN-001", ...]

10. RELATED_REPOS
    What other repos does it connect to? (Dependencies/integrations)
    Example: ["LangChain", "OpenAI-SDK", "LangGraph"]

---

OUTPUT FORMAT:

NAME: [repo-name]
CATEGORY: [Infrastructure | Shared Service | Core Platform | Internal Tool | Automation | Product | Revenue Product | Venture | Portfolio Asset | Strategic Asset]
PURPOSE: [one sentence]
CAPABILITIES: [3-5 capabilities as bullet list]
DEPENDENCIES: [list of required repos/services]
TECH_STACK: [languages and frameworks]
REUSABILITY_SCORE: [1-10]
REVENUE_POTENTIAL: [estimated annual revenue or "$0"]
STRATEGIC_VALUE: [what ventures it enables, what it unlocks]
RELATED_VENTURES: [list of venture IDs or "none"]
RELATED_REPOS: [list of connected repos]

EXAMPLE (Chroma):

NAME: chromadb
CATEGORY: Infrastructure (Database)
PURPOSE: Vector database for embeddings storage and semantic search
CAPABILITIES: ["Vector storage", "Semantic search", "Embedding indexing"]
DEPENDENCIES: ["PostgreSQL", "OpenAI API", "Python 3.8+"]
TECH_STACK: ["Python", "FastAPI", "Pydantic"]
REUSABILITY_SCORE: 9
REVENUE_POTENTIAL: "$500K-2M/year (white-label vector SaaS)"
STRATEGIC_VALUE: Powers memory layer for all AI ventures, enables RAG
RELATED_VENTURES: ["EDU-013", "CON-011", "FIN-001", "FIN-002", "FIN-003"]
RELATED_REPOS: ["LangChain", "OpenAI-Python-SDK", "LangGraph", "Pinecone", "Weaviate"]

EXAMPLE (CON-011 Electrical Website):

NAME: con-011-electrical-services
CATEGORY: Product
PURPOSE: Lead generation website for electrical contracting services
CAPABILITIES: ["Contact form", "Service portfolio", "Project gallery", "Lead capture"]
DEPENDENCIES: ["Supabase", "Resend", "Vercel", "Cloudflare"]
TECH_STACK: ["HTML", "CSS", "JavaScript"]
REUSABILITY_SCORE: 5
REVENUE_POTENTIAL: "$42K-84K/month (direct revenue)"
STRATEGIC_VALUE: Launches construction ecosystem, proves template for 14 more trades
RELATED_VENTURES: ["CON-001", "CON-009", "CON-010", "CON-012", "CON-013"]
RELATED_REPOS: ["rebrand-con-trade.js", "Supabase", "Vercel", "Resend"]
```

---

## CLASSIFICATION GUIDE (Help Choosing)

### INFRASTRUCTURE
**Signs:** Enables other services | No end-user interface | Powers multiple products | DevOps/deployment focus

**Examples:** Supabase, Vercel, Cloudflare, Redis

**Question:** Would ventures break if this disappeared?

---

### PLATFORM
**Signs:** Multi-tenant | Marketplace features | Foundation for other products | OS-like

**Examples:** n8n, LangGraph, Supabase

**Question:** Can multiple ventures use this simultaneously?

---

### PRODUCT
**Signs:** Complete | Revenue-ready | Customer-facing | Solves problem end-to-end

**Examples:** CON-011 website, SaaS app, mobile app

**Question:** Is this something customers would pay for?

---

### AGENT
**Signs:** Autonomous decisions | LLM-based | Actions without intervention | Has reasoning

**Examples:** LangGraph, AI trading bot

**Question:** Does this make autonomous decisions?

---

### TOOL
**Signs:** Utility | CLI | Automation | Internal productivity | Not customer-facing

**Examples:** Build script, data migration, rebrand-con-trade.js

**Question:** Is this internal team use?

---

### SERVICE
**Signs:** API or microservice | Specific capability | Backend only | Integration point

**Examples:** Resend (email), Stripe (payments)

**Question:** Is this an API others call?

---

### FRAMEWORK
**Signs:** Abstraction layer | Pattern library | Provides structure | For developers

**Examples:** LangGraph, Next.js, Django, design system

**Question:** Does this help developers build things?

---

### LIBRARY
**Signs:** Code library | SDK | Reusable component | Imported by other code

**Examples:** React, OpenAI SDK, pandas, lodash

**Question:** Is this something other code imports?

---

### DATASET
**Signs:** Data collection | Training data | Knowledge base | Not executable code

**Examples:** construction-content-topics.csv, training dataset

**Question:** Is this primarily data vs code?

---

### TEMPLATE
**Signs:** Boilerplate | Starter kit | Scaffold | Starting point for new projects

**Examples:** Next.js starter, React boilerplate

**Question:** Is this a starting point?

---

### WORKFLOW
**Signs:** Automation | Orchestration | Job scheduling | Event-driven

**Examples:** n8n workflow, GitHub Actions, scheduled task

**Question:** Does this automate a process?

---

### LEARNING
**Signs:** Tutorial | Guide | Documentation | Examples | Educational

**Examples:** README, tutorial repo, code examples, blog

**Question:** Is this for learning/reference?

---

### ARCHIVE
**Signs:** No longer used | Deprecated | Superseded | Historical

**Examples:** Old implementation, deprecated library

**Question:** Is this still actively used?

---

## EXAMPLES (Fully Worked)

### Example 1: Chroma
```
NAME: chromadb
TYPE: Infrastructure
PURPOSE: Vector database for embeddings storage and semantic search
BUSINESS_VALUE: Could white-label as SaaS ($20/venture/mo = $14.4K MRR)
TECHNICAL_VALUE: 9/10
STRATEGIC_VALUE: Powers memory layer for all 712 ventures
CONFIDENCE: 10/10
REASONING: Core infrastructure used by all ventures for vector search and embeddings. Reusable across ventures.
```

### Example 2: CON-011 (Electrical Website)
```
NAME: con-011-electrical-services
TYPE: Product
PURPOSE: Lead generation and service marketing website for electrical contracting
BUSINESS_VALUE: $42K-84K MRR (month 1-2)
TECHNICAL_VALUE: 5/10
STRATEGIC_VALUE: Launches construction ecosystem, proves template
CONFIDENCE: 10/10
REASONING: Complete, revenue-generating product. Not a framework. Ready for production. Repeatable template for 14 other trades.
```

### Example 3: LangGraph
```
NAME: langraph
TYPE: Framework + Platform
PURPOSE: Framework for building autonomous agents with LLMs
BUSINESS_VALUE: Could be standalone AI agent SaaS product
TECHNICAL_VALUE: 9/10
STRATEGIC_VALUE: Powers decision-making layer for all ventures
CONFIDENCE: 9/10
REASONING: Both a framework developers build with AND platform for commercialization. Strategically critical.
```

### Example 4: Old Custom Auth
```
NAME: custom-auth-system-v1
TYPE: Archive
PURPOSE: Custom authentication from 2 years ago
BUSINESS_VALUE: Low (maintenance cost $2K/year, no revenue)
TECHNICAL_VALUE: 2/10
STRATEGIC_VALUE: Replaced by Supabase; should be decommissioned
CONFIDENCE: 10/10
REASONING: Legacy system. Supabase Auth is superior. Should consolidate and decommission.
```

---

## TEST REPOS (50 to classify)

**Infrastructure (10):**
Supabase, Vercel, Cloudflare, Redis, PostgreSQL, Docker, Kubernetes, Prometheus, Grafana, DuckDB

**AI/ML (10):**
LangGraph, Chroma, Claude API, LightRAG, OpenAI, HF transformers, PyTorch, LlamaIndex, LangChain, LiteLLM

**Data (10):**
construction-content-topics.csv, ventures-master.csv, DuckDB, pandas, Arrow, Parquet, TensorFlow Datasets, HF Datasets, Wikipedia, Wikidata

**Tools/Utilities (10):**
n8n, rebrand-con-trade.js, populate_venture_knowledge_graph.py, obsidian_graph_sync.py, GitHub Actions, Temporal, Bull, Celery, Airflow, Make.com

**Other (10):**
Next.js, React, Tailwind, MDN Web Docs, template-repo, deprecated-payment-system, YouTube-scripts-repo, marketplace-platform, payment-api-wrapper, autonomous-agent-example

---

## NEXT STEPS

1. ✅ Save this prompt to `/Users/acebless/Documents/repo-ingestion-prompt.md`
2. Apply to 50 test repos (classify each)
3. Build scoring spreadsheet (Task #2)
4. Batch process all 1,400 repos (Task #4)

