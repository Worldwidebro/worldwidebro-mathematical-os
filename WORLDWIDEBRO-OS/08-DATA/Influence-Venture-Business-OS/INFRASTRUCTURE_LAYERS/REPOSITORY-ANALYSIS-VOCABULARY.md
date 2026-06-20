---
references:
  - [[REPOSITORY-INTELLIGENCE-SYSTEM]]
  - [[INFRASTRUCTURE-HUB]]
  - [[../VENTURES/VENTURES-HUB]]
---

# Repository Analysis Vocabulary & 10-Attribute Classification Model

**Core Principle:** Think of a repository as **a container of capabilities, assets, knowledge, workflows, and business value** — not just code.

**Impact:** Understand what each of your 1,556 repos IS, what it DOES, and what it's WORTH

---

## THE REFRAME: From Git Vocabulary to Strategic Assets

### Wrong: Git Vocabulary Only
```
stripe-payment-wrapper
├─ Stars: 45
├─ Forks: 12
├─ Last commit: 2 days ago
├─ Language: Python
└─ Status: Active
```

### Right: Multi-Domain Strategic Asset
```
stripe-payment-wrapper
├─ PURPOSE: Unified Stripe payment processing wrapper
├─ CATEGORY: Service (infrastructure)
├─ CAPABILITIES: Charges, subscriptions, invoices, refunds, webhooks
├─ DEPENDENCIES: Stripe API, Python 3.9+, FastAPI, PostgreSQL
├─ TECH_STACK: Python, FastAPI, PostgreSQL, Redis, Docker
├─ REUSABILITY: 9/10 (universal payment abstraction)
├─ REVENUE_POTENTIAL: 9/10 (directly enables revenue)
├─ STRATEGIC_VALUE: 10/10 (critical for all 6 ventures)
├─ RELATED_VENTURES: All 6 (marketplace-core dependency)
└─ RELATED_REPOS: [marketplace-core, billing-service, subscription-mgmt]
```

---

## THE 10 MOST IMPORTANT REPOSITORY ATTRIBUTES

When analyzing 1,556 repos, focus on these 10 dimensions:

### 1. PURPOSE — What does this repo do?

**Capabilities provided (not features):**

```
Authentication                 Payments                        Search
Authorization                  Subscription Management         Storage
Messaging                       Analytics                       Automation
AI                              Agents                          Memory
Monitoring                      Logging                         Reporting
Scheduling                      Workflows                       Data Processing
Infrastructure                  Developer Tools                 Testing
Documentation                   Compliance                      Security
```

**Example:**
```
stripe-payment-wrapper
PURPOSE: Unified interface for Stripe payment API
CAPABILITIES: Payment processing, subscription management, invoice generation
```

---

### 2. CATEGORY — What type of strategic asset?

**Strategic Repository Taxonomy:**

```
INFRASTRUCTURE              PLATFORM                    PRODUCT
├── Database              ├── AI Platform              ├── SaaS
├── Storage               ├── Agent Platform           ├── Marketplace
├── Networking            ├── Automation Platform      ├── Internal Tool
├── Security              └── Data Platform            └── Customer Portal
└── Cloud

ASSET                       VENTURE
├── SOP                      ├── Revenue Generating
├── Prompt                   ├── Strategic
├── Dataset                  ├── Experimental
├── Template                 └── Archived
└── Workflow
```

**Example:**
```
stripe-payment-wrapper
PRIMARY_CATEGORY: Service (Infrastructure)
SECONDARY: Platform enabler
WHY: Provides critical payment capability to all ventures
```

---

### 3. CAPABILITIES — What features/functions does this enable?

**Complete list of possible capabilities:**

```
Authentication              Authorization               Payments
Subscription Management      Search                      Storage
Messaging                    Real-time Communication     Analytics
Monitoring                   Logging                     Scheduling
Workflows                    Data Processing             AI Inference
AI Training                  Vector Search               Memory Systems
Multi-tenancy                Rate Limiting               Testing
Deployment                   Scaling                     Security
Compliance                   Automation                  Reporting
```

**Example:**
```
stripe-payment-wrapper
CAPABILITIES:
- Payment processing (charges, authorizations, captures)
- Subscription management (billing cycles, upgrades, downgrades)
- Invoice generation (PDF, email delivery)
- Refund processing (full, partial, reversals)
- Webhook management (payment events, retries)
- Customer management (create, update, delete)
```

---

### 4. DEPENDENCIES — What does this repo require?

**Dependency categories:**

```
EXTERNAL SERVICES           LANGUAGES/RUNTIMES         FRAMEWORKS/LIBRARIES
├── APIs                    ├── Python 3.9+            ├── FastAPI
├── Cloud Platforms         ├── TypeScript/Node.js      ├── Next.js
└── Third-party SaaS       ├── Go                      ├── Django
                            └── Rust                    └── React

DATABASES & STORAGE         INFRASTRUCTURE             TOOLS
├── PostgreSQL              ├── Docker                 ├── Git
├── MongoDB                 ├── Kubernetes             ├── npm/pip
├── Redis                   ├── GitHub Actions         └── pytest/jest
└── S3/GCS                  └── Terraform
```

**Example:**
```
stripe-payment-wrapper
DEPENDENCIES:
External: Stripe API
Language: Python 3.11
Framework: FastAPI
Database: PostgreSQL (transaction logging)
Cache: Redis (idempotency)
Testing: pytest, pytest-asyncio
Deployment: Docker, GitHub Actions
```

---

### 5. TECH_STACK — Complete technology requirements

**Map all 5 layers:**

```
LANGUAGE LAYER              FRAMEWORK LAYER             DATA LAYER
├── Python 3.11            ├── FastAPI                 ├── PostgreSQL
├── TypeScript             ├── Next.js                 ├── Redis
└── Go                      ├── Django                  └── Elasticsearch
                            └── Express

INFRASTRUCTURE              EXTERNAL SERVICES
├── Docker                  ├── Stripe API
├── Kubernetes              ├── AWS/GCP
├── GitHub Actions          └── Datadog
```

**Example:**
```
stripe-payment-wrapper
LANGUAGE: Python 3.11
FRAMEWORK: FastAPI, Pydantic
DATABASE: PostgreSQL
CACHE: Redis
EXTERNAL: Stripe API, Stripe SDK
MONITORING: Sentry, Datadog
DEPLOYMENT: Docker, GitHub Actions
```

---

### 6. REUSABILITY_SCORE (1-10) — Can this be used elsewhere?

```
10 = Universal component (works everywhere)
    Examples: Payment wrapper, auth system, notification service

9  = Framework/library (general purpose)
    Examples: Design system, CLI framework, validation library

8  = Loosely coupled (minimal dependencies)
    Examples: Rate limiter, cache layer, logger

7  = Well-documented (easy to integrate)
    Examples: SDK, example apps, templates

6  = Needs minor customization (mostly reusable)
    Examples: Boilerplate, starter kit

5  = Domain-specific (reusable within domain)
    Examples: E-commerce checkout, SaaS billing

4  = Venture-specific (requires modification)
    Examples: Roofing marketplace, plumbing dispatch

3  = Tightly coupled (requires major changes)
    Examples: Internal tool, monolith component

2  = Proof of concept (not production-ready)
    Examples: Experiments, prototypes

1  = Single-use only (throw away after use)
    Examples: One-off scripts, migration tools
```

**Example:**
```
stripe-payment-wrapper
REUSABILITY_SCORE: 9/10
REASONING: Works for any SaaS, marketplace, or subscription business.
Minimal configuration. Handles all payment scenarios.
```

---

### 7. REVENUE_POTENTIAL (1-10) — Can this generate money?

```
10 = Direct revenue engine
    (Payment processor, subscription billing)

9  = Enables high-margin products
    (Auth enables SaaS, API enables platforms)

8  = Powers multiple revenue streams
    (Analytics, notifications, search)

7  = Significant competitive advantage
    (Custom ML model, unique algorithm)

6  = Important feature in revenue product
    (File storage in marketplace, video in SaaS)

5  = Supports revenue but not essential
    (Monitoring, logging, analytics)

4  = Infrastructure cost reduction
    (Caching, CDN, compression)

3  = Nice-to-have feature
    (Dark mode, export, advanced search)

2  = Supporting tool
    (Testing framework, docs generator)

1  = Internal-only use
    (Dev scripts, CI/CD helpers)
```

**Example:**
```
stripe-payment-wrapper
REVENUE_POTENTIAL: 9/10
BUSINESS_MODEL: Transactional (enables revenue collection)
VENTURES: All 6 (marketplace-core dependency)
REASONING: No this = no revenue for any marketplace
```

---

### 8. STRATEGIC_VALUE (1-10) — Does this matter to strategy?

```
10 = Critical to multiple ventures
    (Smart dispatch powers CON-010, CON-012, LT-009)

9  = Core capability we own
    (Proprietary algorithms, custom ML models)

8  = Differentiator vs competitors
    (Predictive maintenance, dynamic pricing)

7  = Powers entire platform
    (marketplace-core, authentication system)

6  = Enables key features
    (Real-time messaging, file processing)

5  = Important but not unique
    (Admin dashboard, basic analytics)

4  = Commodity feature
    (Email sending, SMS—many competitors have this)

3  = Supporting infrastructure
    (Logging, monitoring, deployment)

2  = Occasional use
    (One-off utilities, specific integrations)

1  = Obsolete or irrelevant
    (Old templates, deprecated libraries)
```

**Example:**
```
stripe-payment-wrapper
STRATEGIC_VALUE: 10/10
IMPACT: Critical infrastructure for all ventures
COMPETITIVE_ADVANTAGE: Reliable, tested payment processing
MOAT: Better than building from scratch, faster integration
```

---

### 9. RELATED_VENTURES — Which of your ventures use this?

**Bi-directional mapping:**

```
marketplace-core
├─ Uses: Auth, Payments, Notifications, Analytics
└─ Powers: All 6 ventures

CON-009 (Roofing)
├─ Directly uses: Lead scoring, Contractor ratings, marketplace-core
└─ Indirectly uses: Payments (via marketplace-core)

CON-010 (Plumbing 24/7)
├─ Directly uses: Smart dispatch, Hotline router, marketplace-core
└─ Indirectly uses: Payments, Notifications (via marketplace-core)

[... repeat for CON-011, CON-012, LT-009 ...]
```

**Example:**
```
stripe-payment-wrapper
RELATED_VENTURES:
- marketplace-core: Direct dependency (payment processing)
- CON-009: Indirect via marketplace-core (customer payments)
- CON-010: Indirect via marketplace-core (customer/contractor payments)
- CON-011: Indirect via marketplace-core
- CON-012: Indirect via marketplace-core
- LT-009: Indirect via marketplace-core (subscription billing)
```

---

### 10. RELATED_REPOSITORIES — What repos connect?

**Dependency relationships:**

```
USES (this repo uses another)
├─ stripe-payment-wrapper USES stripe-sdk
├─ All ventures USES marketplace-core
└─ marketplace-core USES auth-system, payments-service

POWERS (another repo depends on this)
├─ stripe-payment-wrapper POWERS marketplace-core
├─ marketplace-core POWERS all 6 ventures
└─ Authentication POWERS secure-endpoints

ENABLES (what capabilities does this unlock?)
├─ Authentication ENABLES user accounts, authorization, sessions
├─ Payments ENABLES revenue collection, subscriptions, invoicing
└─ Dispatch ENABLES automated routing, efficiency, scalability

REPLACES (what does this supersede?)
├─ new-auth-system REPLACES old-auth-system
├─ stripe-payment-wrapper REPLACES manual payment handling
└─ modern-dashboard REPLACES old-dashboard-template

CONSOLIDATE_WITH (similar functionality)
├─ lead-scoring-v1 CONSOLIDATE_WITH lead-scoring-v2
├─ old-notification-service CONSOLIDATE_WITH new-notification-service
└─ duplicate-payments-code consolidates into single wrapper
```

**Example:**
```
stripe-payment-wrapper
USES: Stripe SDK, httpx, Pydantic
POWERS: marketplace-core, billing-service, subscription-management
ENABLES: Revenue collection, Subscription management, Invoice generation
REPLACES: Legacy payment processor, Manual webhook handling
CONSOLIDATE_WITH: stripe-integration-v1 (older, lower quality version)
```

---

## ANALYSIS TEMPLATE: The 10-Attribute Form

```markdown
# Repository Analysis: [REPO_NAME]

## 1. PURPOSE
[One-two sentence description]

## 2. CATEGORY
Primary: [Infrastructure|Platform|Product|Asset|Venture]
Secondary: [Optional secondary]

## 3. CAPABILITIES
- [Capability 1]
- [Capability 2]
- [Capability 3]
- [Capability 4]

## 4. DEPENDENCIES
External: [APIs, services]
Language: [Python 3.11]
Frameworks: [FastAPI]
Database: [PostgreSQL]
Infrastructure: [Docker, GitHub Actions]

## 5. TECH_STACK
Language: [X]
Framework: [X]
Database: [X]
Cache: [X]
External: [X]
Monitoring: [X]
Deployment: [X]

## 6. REUSABILITY_SCORE
Score: [1-10]
Reasoning: [Why this score?]

## 7. REVENUE_POTENTIAL
Score: [1-10]
Model: [How does it make money?]
Ventures: [Which ventures use it?]

## 8. STRATEGIC_VALUE
Score: [1-10]
Impact: [Why does this matter?]
Advantage: [Competitive differentiation?]

## 9. RELATED_VENTURES
- [Venture 1]: [How it's used]
- [Venture 2]: [How it's used]

## 10. RELATED_REPOSITORIES
USES: [Repos this depends on]
POWERS: [Repos that depend on this]
ENABLES: [Capabilities unlocked]
REPLACES: [What it supersedes]
CONSOLIDATE_WITH: [Similar functionality]

---

## Metadata
Status: [Active|Maintained|Dormant|Archived]
Stars: [Number]
Forks: [Number]
Last Commit: [Date]
License: [MIT|Apache|GPL]
Documentation: [Quality]
Security: [No known issues]
Owner: [Team/person]
```

---

## NEXT STEPS

### Phase 1: Vocabulary Standardization (Day 1)
✅ All team members learn this 10-attribute model
✅ Understand difference between Git vocabulary and Strategic vocabulary
✅ Know the 8 domains of repo analysis

### Phase 2: Repository Scanning (Days 2-3)
- Scan all 1,556 repos with AI classifier
- Apply 10 attributes to each repo
- Create searchable Repository Registry

### Phase 3: Knowledge Graph Creation (Day 4-5)
- Build bi-directional links between repos
- Map repos to ventures
- Identify strategic assets, duplications, gaps

### Phase 4: Strategic Decision-Making (Week 2)
- Which repos power multiple ventures? (highest value)
- Which repos could become businesses? (ventures)
- Which repos should consolidate? (duplicates)
- Which repos fill critical gaps? (missing)
- Which repos are technical debt? (archive)

---

**Your competitive advantage: Speaking the language of strategic assets, not just code.**

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
