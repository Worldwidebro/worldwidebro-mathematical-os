---
type: data-ontology
canonical: true
authority: company-brain-circulatory-system
updated_at: 2026-10-02T18:45:00Z
verification_required: true
source_of_truth: true
---

# DATA_FLOW — Company Brain Circulatory System

**Complete data lifecycle ontology. Describes how reality becomes knowledge becomes decision becomes action becomes outcome.**

Every object has a data-flow story: Where did it come from? What is it? Who transformed it? Where is it stored? What does it connect to? Who uses it? What decision does it inform? What action does it cause? What outcome results? What feedback returns?

The fundamental recursive loop:

```
[[REALITY]] → [[DATA]] → [[KNOWLEDGE]] → [[DECISION]] → [[ACTION]] → [[OUTCOME]] → [[FEEDBACK]] → [[REALITY]] ↺
```

---

## [[DATA_FLOW]] Root Ontology

```
[[DATA_FLOW]]
├── [[DATA_SOURCES]]
├── [[DATA_CAPTURE]]
├── [[DATA_TRANSPORT]]
├── [[DATA_TRANSFORMATION]]
├── [[DATA_VALIDATION]]
├── [[DATA_IDENTITY]]
├── [[DATA_STORAGE]]
├── [[KNOWLEDGE]]
├── [[COMPUTATION]]
├── [[DECISION]]
├── [[ACTION]]
├── [[OUTCOMES]]
├── [[FEEDBACK]]
├── [[OBSERVABILITY]]
├── [[SECURITY]]
├── [[GOVERNANCE]]
└── [[DATA_LIFECYCLE]]
```

---

## [[DATA_SOURCES]] — Where Reality Enters

```yaml
sources:
  
  human_input:
    channel: Claude Code, Obsidian, Terminal
    frequency: Real-time
    format: Text, markdown, commands
    volume: Variable
    quality: High (authenticated)
  
  agent_output:
    channel: OmniRoute, MCP servers, Agents
    frequency: Event-driven
    format: JSON, structured
    volume: High
    quality: Validated
  
  external_apis:
    channel: GitHub, Make.com, Supabase, HubSpot
    frequency: Polling + webhooks
    format: JSON, REST
    volume: High
    quality: Vendor-dependent
  
  repositories:
    channel: Git repos (1,740)
    frequency: Push events
    format: Code, markdown, YAML
    volume: Continuous
    quality: High (code review gated)
  
  devices:
    channel: Mac Studio, Mac Air, iPhone
    frequency: Continuous
    format: System logs, metrics
    volume: Medium
    quality: System-generated
  
  applications:
    channel: Claude, Antigravity, Codex
    frequency: Event-driven
    format: Action traces, decisions, reasoning
    volume: High
    quality: Structured
  
  knowledge_base:
    channel: Obsidian vault, wiki links
    frequency: Manual + agent-updated
    format: Markdown, [[links]]
    volume: Growing
    quality: Human-curated + AI-validated
```

---

## [[DATA_CAPTURE]] — Extraction & Ingestion

```yaml
capture:
  
  webhook_ingestion:
    protocol: HTTP POST
    sources: GitHub, Make.com, Supabase
    format: JSON
    validation: Schema + signature verification
    queue: Redis message queue
    processing: Async, event-driven
  
  api_polling:
    frequency: Configurable (15m-24h)
    sources: HubSpot, external APIs
    format: REST JSON
    retry: Exponential backoff
    storage: PostgreSQL raw_imports table
  
  file_parsing:
    formats: .md, .yaml, .json, .csv, .py
    sources: Git repos, local files
    extraction: LLM-powered + regex
    output: Structured data
  
  ocr_transcription:
    image_input: Screenshots, documents
    model: Claude Vision
    output: Text + structured fields
  
  git_ingestion:
    source: 1,740 repositories
    extraction: Commits, PRs, issues, code
    frequency: Real-time webhooks
    parser: GitHub API + git log
    storage: Neo4j graph + PostgreSQL
```

---

## [[DATA_TRANSPORT]] — Movement & Routing

```yaml
transport:
  
  http:
    protocol: REST + JSON
    endpoints: [[INFRASTRUCTURE#Services]]
    routers: OmniRoute (port 3004)
    middleware: Authentication, validation, rate limiting
    reliability: Retries + circuit breaker
  
  message_queue:
    platform: Redis
    topics: events.*, tasks.*, webhooks.*
    consumers: Agents, pipelines, workers
    durability: Persistence enabled
    latency: <100ms P99
  
  mcp:
    protocol: Stdio + SSE
    servers: omniroute, company-brain, + custom
    clients: Claude Code, agents, applications
    reliability: Connection pooling
  
  database_sync:
    from: PostgreSQL ↔ Neo4j ↔ Qdrant
    protocol: Custom ETL pipeline
    frequency: Real-time + batch
    consistency: Eventual (configurable)
  
  file_sync:
    platform: Syncthing (planned)
    from: Mac Studio ↔ Mac Air
    folders: ~/.claude/projects, ~/Documents/Company\ Brain
    frequency: Real-time
    consistency: Bidirectional
```

---

## [[DATA_TRANSFORMATION]] — Normalization & Enrichment

```yaml
transformation:
  
  normalization:
    input: Raw data (multiple formats)
    steps:
      - Extract fields from source format
      - Map to canonical schema
      - Apply type casting
      - Standardize units/formats
    output: Normalized record
  
  deduplication:
    method: Entity resolution + canonical IDs
    tools: Neo4j entity matching
    scope: Ventures, repositories, agents, capabilities
    confidence: Threshold-based
  
  enrichment:
    techniques:
      - LLM entity extraction
      - Semantic embedding (Qdrant)
      - Graph relationship inference
      - Historical data lookup
    sources: Neo4j, Qdrant, external knowledge
  
  classification:
    dimensions:
      - Sector (SEC-001 to SEC-035)
      - Venture type (startup, spv, opco)
      - Capability category
      - Risk level
      - Priority tier
    method: Rules + LLM classification
  
  embedding:
    model: nomic-embed-text (local)
    dimensions: 768
    output: Qdrant vectors
    use: Semantic search, similarity matching
  
  aggregation:
    level: Venture, sector, portfolio
    dimensions: Revenue, metrics, health
    frequency: Daily + on-demand
    output: Materialized views (PostgreSQL)
  
  derivation:
    rules_engine: Company Brain rules
    examples:
      - Calculate venture health score
      - Infer capability gaps
      - Detect anomalies
      - Predict outcomes
```

---

## [[DATA_VALIDATION]] — Quality Gates

```yaml
validation:
  
  schema_validation:
    tool: JSON Schema (defined per type)
    enforcement: Reject invalid before storage
    examples:
      - Venture schema: name, sector, status, revenue
      - Agent schema: name, capabilities, skills, model
      - Repository schema: url, language, stars, status
  
  type_validation:
    strict: true
    coercion: Attempt numeric strings → numbers
    rejection: Invalid types fail fast
  
  quality_checks:
    completeness: Required fields present
    accuracy: Values match known domain
    freshness: Not stale (time-based)
    consistency: Cross-reference checks
  
  provenance:
    tracking: Source of every record
    chain: Data lineage from source to storage
    audit: Immutable log of transformations
    evidence: [[INFRASTRUCTURE#CONNECTIVITY_TESTING]]
  
  reconciliation:
    frequency: Daily
    method: Cross-system comparison
    tolerance: <0.1% discrepancy
    resolution: Automated merge or alert
```

---

## [[DATA_IDENTITY]] — Entity Resolution

```yaml
identity:
  
  canonical_id:
    format: TYPE-000001 (e.g., VEN-000147, CAP-000392)
    generation: Sequence generator (PostgreSQL)
    immutable: true
    scope: Global across Company Brain
  
  entity_types:
    - VEN (Venture, 789)
    - CAP (Capability, 300+)
    - REP (Repository, 1,740)
    - AGT (Agent, 309)
    - SKL (Skill, 300+)
    - SEC (Sector, 35)
    - MOD (Model, 10+)
    - OPC (Operating Company, 36)
    - SPV (Special Purpose Vehicle, 15+)
  
  relationships:
    venture_operates_in_sector: VEN → SEC
    agent_has_capability: AGT → CAP
    repository_implements_capability: REP → CAP
    sector_managed_by_opco: SEC → OPC
    model_provides_inference: MOD → outputs
  
  resolution_method:
    primary: Canonical ID
    fallback_1: External ID (GitHub, HubSpot, etc.)
    fallback_2: Semantic similarity (Qdrant vectors)
    fallback_3: Human curation (last resort)
  
  multi_reference:
    tracking: [machine_id (ULID), ref_id (TYPE-000001), slug (url-safe)]
    mapping: ID registry in Neo4j + PostgreSQL
```

---

## [[DATA_STORAGE]] — Persistence Layer

```yaml
storage:
  
  neo4j:
    purpose: Relationship graph
    entities: All canonical objects
    edges: 20,363+ (Oct 2 verified)
    access: bolt://100.87.214.70:7687
    queries: Cypher (path finding, pattern matching)
    source_of_truth: Relationships, ontology
  
  qdrant:
    purpose: Semantic vector store
    vectors: 17,236+ (Oct 2 verified)
    dimensions: 768 (nomic-embed-text)
    access: http://100.87.214.70:6333
    queries: Vector similarity, hybrid search
  
  postgresql:
    purpose: Relational structure + transactions
    tables:
      - ventures (789 + details)
      - repositories (1,740 + metadata)
      - capabilities (300+ features)
      - agents (309 + config)
      - metrics (revenue, health, execution)
    access: localhost:5433 (SSH tunnel)
    transactions: ACID guaranteed
  
  redis:
    purpose: Cache + sessions
    ttl: Configurable per key
    access: localhost:6379 (SSH tunnel)
    use: Real-time counters, temporary state
  
  file_storage:
    location: /Volumes/T7\ Shield (922 GB available)
    types: Models, repos, backups, raw data
    access: Bind mounts to Docker containers
  
  markdown_vault:
    location: ~/Documents/Company\ Brain
    format: .md with [[wiki links]]
    version: Git-tracked
    ontology: Bracket notation [[SECTION]] hierarchy
  
  object_storage:
    planned: S3-compatible (future)
    use: Large files, archives, backups
```

---

## [[KNOWLEDGE]] — Semantic Understanding

```yaml
knowledge:
  
  documents:
    where: Obsidian vault + [[INFRASTRUCTURE.md]]
    format: Markdown + [[links]]
    ontology: Bracket notation [[LAYER]] hierarchy
    
  facts:
    where: Neo4j nodes + relationships
    format: Property graph
    examples:
      - Venture LT-005 has revenue $2.1K/month
      - Sector SEC-027 owns 89 repositories
      - Agent discovery-engine requires Neo4j capability
  
  observations:
    where: Audit logs + [[REALITY.md]]
    format: Timestamped evidence
    immutable: true
    example: "OmniRoute port verified 3004 on 2026-10-02 18:15 UTC"
  
  insights:
    where: Reports, analysis, derived data
    format: Structured + narrative
    example: "Portfolio readiness 27.7% avg, trending +2.3%"
  
  context:
    where: [[WHERE_WE_ARE.md]] + agent memory
    format: Status + relationships
    freshness: Real-time updated
  
  memory:
    short_term: Redis cache (seconds-hours)
    medium_term: PostgreSQL sessions (days)
    long_term: Neo4j + markdown vault (permanent)
  
  graph:
    engine: Neo4j
    nodes: 3000+ entities
    edges: 20,363+ relationships
    queries: Path finding, recommendation, impact analysis
  
  source_of_truth:
    hierarchy:
      1. [[REALITY.md]] (audit-verified facts)
      2. [[WHERE_WE_ARE.md]] (current state)
      3. Neo4j (relationships)
      4. Qdrant (semantic similarity)
      5. PostgreSQL (transactional data)
      6. Markdown vault (documented knowledge)
```

---

## [[COMPUTATION]] — Reasoning & Inference

```yaml
computation:
  
  rules:
    engine: Company Brain rules language
    examples:
      - IF venture.revenue > threshold THEN priority = HIGH
      - IF capability.missing in agent THEN flag_gap = true
      - IF risk > threshold THEN escalate_to_human = true
  
  functions:
    platform: OmniRoute
    count: 110+ tools
    categories: Data, text, analysis, integration
    invocation: Agent → OmniRoute → tool
  
  models:
    llm:
      - Claude Haiku (local via OmniRoute)
      - Claude Sonnet (remote)
      - qwen3.6:35b-a3b (local Ollama)
      - hermes3, llama3.1 (local Ollama)
    
    embedding:
      - nomic-embed-text (local)
      - Purpose: Document similarity, semantic search
    
    routing:
      platform: OmniRoute (LiteLLM)
      selection: Cost + capability matching
      fallback: Local models if cloud unavailable
  
  agents:
    count: 309 registered
    discovery: Neo4j query → capability match
    invocation: Task router → OmniRoute → agent
    feedback: Outcome → learning loop
  
  workflows:
    platform: Make.com + OmniRoute
    examples:
      - Lead gen → CRM → revenue tracking
      - Repository → capability extraction → agent routing
      - Decision event → agent action → outcome logging
  
  pipelines:
    ingestion: Data sources → capture → validation → storage
    enrichment: Raw data → transformation → knowledge
    reasoning: Knowledge → computation → insight
    execution: Decision → action → outcome
```

---

## [[DECISION]] — Choice-Making

```yaml
decision:
  
  signal:
    sources:
      - Agent observations (what did you see?)
      - System metrics (is something wrong?)
      - User input (what do you want?)
      - External events (what changed?)
  
  context:
    assembly: Where_WE_ARE.md + Neo4j + memory
    relevance: Entity resolution → related context
    freshness: <5min (real-time refreshed)
  
  evaluation:
    method: Rule engine + LLM + agent judgment
    criteria: Risk, priority, impact, cost, compliance
    scoring: Confidence threshold (0.60-0.85 for L2 autonomy)
  
  decision:
    options: Multiple paths evaluated
    choice: Selected based on evaluation
    owner: Human (L0), Agent (L1/L2/L3), Automated (L3)
    trace: Logged to Neo4j KG-007 with SHA256 provenance
  
  approval:
    threshold: L1 (human confirm), L2 (audit trail), L3 (auto)
    escalation: Risk → human, normal → auto
  
  policy:
    constraint: Company Brain rules
    example: "Ventures with <10% readiness cannot enter L3 autonomy"
    enforcement: Hard gate before action
```

---

## [[ACTION]] — Execution

```yaml
action:
  
  create:
    examples: Venture, agent, capability, task
    triggers: Decision + approval
    format: API call + logging
    consistency: Transactional
  
  update:
    examples: Revenue, status, relationships
    triggers: Data flow + agent actions
    format: Database write + event emit
    atomicity: Single write, no partial updates
  
  send:
    examples: Notification, email, message
    platform: Webhook + MCP
    triggers: Decision → action
    tracking: Delivery log + retry
  
  call:
    examples: External API, LLM inference
    platform: OmniRoute
    format: JSON request/response
    resilience: Retry + fallback
  
  execute:
    examples: Workflow, agent loop, pipeline
    platform: Make.com + OmniRoute
    triggers: Event or schedule
    observability: Execution logs + metrics
  
  delegate:
    examples: Complex task → agent
    platform: OmniRoute agent router
    method: Capability matching + cost optimization
    accountability: Outcome tracking
  
  automate:
    examples: Recurring tasks, workflows
    platform: Make.com scenarios + n8n
    triggers: Time or event-based
    feedback: Learning loop
```

---

## [[OUTCOMES]] — Results & Impact

```yaml
outcomes:
  
  revenue:
    tracking: Venture → deal → revenue
    unit: $ per month
    aggregation: Portfolio + sector level
    attribution: Agent action → revenue impact
  
  velocity:
    metrics:
      - Time from discovery → agent assignment
      - Agent execution time
      - Outcome delivery time
    target: <24h for most workflows
  
  quality:
    dimensions:
      - Accuracy: Did the agent get it right?
      - Completeness: Did it handle all cases?
      - Timeliness: Was it fast enough?
      - Cost: Did it use resources efficiently?
  
  learning:
    capture: Every outcome → feedback
    analysis: Did we meet objectives?
    improvement: Update rules, models, agents
    loop: Knowledge → decision → action → outcome ↺
  
  business_impact:
    examples:
      - Ventures moved to higher autonomy level
      - Revenue increased via agent actions
      - Capabilities discovered + reused
      - Agents improved via learning loops
```

---

## [[FEEDBACK]] — Continuous Improvement

```yaml
feedback:
  
  user_feedback:
    source: Claude Code, agents, manual review
    format: Structured (rating, comment, category)
    storage: Neo4j + PostgreSQL
    use: Agent improvement, capability refinement
  
  system_feedback:
    metrics: Latency, error rate, throughput
    source: [[INFRASTRUCTURE#Observability]]
    trigger: Alert on degradation
    action: Escalate or auto-remediate
  
  agent_feedback:
    source: Task outcome vs. expected
    analysis: Did agent succeed?
    storage: Agent performance logs
    use: Routing logic + model selection
  
  error_feedback:
    source: Failed transactions, validation errors
    logging: [[INFRASTRUCTURE#Logging]]
    analysis: Root cause → fix
    prevention: Update rules + validation
  
  correction:
    trigger: Wrong outcome
    action: Undo + retry or manual intervention
    learning: Why did it fail?
    prevention: Update decision criteria
  
  model_improvement:
    loop: Feedback → analysis → model update
    method: Fine-tuning, prompt optimization, reranking
    frequency: Daily + on-demand
    validation: A/B test before deployment
  
  learning_loop:
    cycle:
      1. Outcome measured
      2. Feedback analyzed
      3. Learning extracted
      4. Rules/models updated
      5. Next decision improved
    duration: Hours to days
    evidence: Improvement metrics tracked
```

---

## [[OBSERVABILITY]] — Monitoring & Transparency

```yaml
observability:
  
  logging:
    platform: OpenObserve
    levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    retention: 30 days (configurable)
    queries: Full-text search + analytics
  
  metrics:
    platform: Prometheus + Grafana
    collection: [[INFRASTRUCTURE#Services]]
    dimensions: By service, by agent, by workflow
    SLOs: Latency <50ms P99, error rate <0.1%
  
  tracing:
    format: Distributed traces (request → hops)
    tool: Jaeger or similar
    span: Each API call, agent action, decision
    parent: Track causality through system
  
  health_checks:
    frequency: Every 30s
    targets: [[INFRASTRUCTURE#Services]]
    status: [[WHERE_WE_ARE.md#Connectivity_Tests]]
    alert: Page on-call if critical
  
  audit_log:
    immutable: true
    events: Every data write, decision, action
    retention: Permanent
    query: By entity, by time, by actor
    compliance: SOC 2, GDPR audit trail
  
  dashboards:
    executive: Revenue, velocity, health
    operational: System metrics, alerts
    technical: Database queries, error rates
    real_time: Push updates as data flows
```

---

## [[SECURITY]] — Data Protection

```yaml
security:
  
  authentication:
    method: OAuth (Tailscale, SSH key)
    enforcement: Every external API call
    tokens: Short-lived (<1h), rotated regularly
  
  authorization:
    model: Role-based (admin, user, viewer)
    granularity: By entity type + operation
    enforcement: Every data access
  
  encryption:
    transport: TLS (HTTPS everywhere)
    at_rest: Evaluated (PostgreSQL encryption)
    secrets: Bitwarden (not code)
  
  pii:
    classification: Marked in schema
    access: Restricted to authorized roles
    deletion: Right to be forgotten (GDPR)
    masking: In logs + reports
  
  data_classification:
    public: Repositories, documentation
    internal: Venture details, metrics
    confidential: Financial, customer data
    restricted: Credentials, API keys
  
  retention:
    policy: By data type + jurisdiction
    audit_log: Permanent
    raw_data: 90 days unless archived
    purge: Automated + logged
```

---

## [[GOVERNANCE]] — Ownership & Accountability

```yaml
governance:
  
  ownership:
    entity_type: Each has a primary owner
    examples:
      - Venture → Founder or manager
      - Agent → Technical owner
      - Capability → Maintainer
    accountability: Owner ensures data quality
  
  stewardship:
    responsibility: Keep data current
    update_frequency: By data type
    escalation: If data becomes stale
  
  policy:
    rule_set: Company Brain rules + regulatory
    enforcement: Hard gates + soft alerts
    audit: Monthly review
  
  compliance:
    frameworks: SOC 2, GDPR, etc. (TODO)
    evidence: [[INFRASTRUCTURE#Security]]
    gap_analysis: Pending
  
  lineage:
    tracking: Source → transformations → storage
    purpose: Audit trail + impact analysis
    query: "Where did this data come from?"
  
  provenance:
    recording: Every fact has origin + timestamp
    immutable: Cannot be changed (only appended)
    evidence: Neo4j KG-007 + audit log
  
  version:
    strategy: Immutable IDs + timestamped changes
    history: Full audit trail
    rollback: Can restore to point-in-time
  
  source_of_truth:
    hierarchy: [[WHERE_WE_ARE.md#Source_of_Truth_Hierarchy]]
    enforcement: Single source for each data type
    conflicts: Resolution process documented
```

---

## [[DATA_LIFECYCLE]] — Complete Arc

```
[[REALITY]]
    ↓
[[CREATE]] — Entity born (venture created, agent discovered)
    ↓
[[INGEST]] — Data enters system (via API, file, human input)
    ↓
[[PROCESS]] — Validation, transformation, enrichment
    ↓
[[STORE]] — Persisted to Neo4j, PostgreSQL, Qdrant, markdown
    ↓
[[ENRICH]] — AI analysis, embedding, classification, derivation
    ↓
[[USE]] — Agent queries, decisions, reasoning
    ↓
[[SHARE]] — Exposed via API, reports, dashboards
    ↓
[[ARCHIVE]] — Moved to cold storage if historical
    ↓
[[DESTROY]] — Deletion on retention policy (GDPR compliance)
    ↓
[[FEEDBACK]] ↺ LOOP BACK TO REALITY
```

---

## [[NEXT_ACTIONS]]

```
NOW:
  [ ] Document specific data flows for each venture type
  [ ] Map data dependencies (if X changes, what updates?)
  [ ] Create data quality SLOs
  
THIS_WEEK:
  [ ] Set up data lineage tracking in Neo4j
  [ ] Implement provenance logging for all writes
  [ ] Publish data governance policy
  
NEXT_MONTH:
  [ ] Automated data quality monitoring
  [ ] Data catalog + discovery UI
  [ ] Compliance audit (SOC 2, GDPR)
```

---

**Related:** [[WHERE_WE_ARE.md]] · [[INFRASTRUCTURE.md]] · [[WHOAMI.md]] · [[REALITY.md]]

**This is the circulatory system. Every object in Company Brain flows through it.**
