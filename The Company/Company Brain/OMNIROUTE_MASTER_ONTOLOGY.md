---
type: infrastructure-control-ontology
canonical: true
authority: ai-connectivity-plane
version: 2.0
updated_at: 2026-10-02T23:00:00Z
source_of_truth: true
subsystems: 38
---

# OMNIROUTE_MASTER_ONTOLOGY v2.0 — AI Infrastructure Control Plane

**OmniRoute is not just an "AI proxy." It is a complete AI connectivity, routing, resilience, optimization, protocol, observability, agent, and integrated subsystems layer.**

This comprehensive ontology models OmniRoute as a **first-class system node** with 38 documented subsystems, explicit governance, and deep integration with the Company Brain's knowledge graph.

---

## [OMNIROUTE_COMPLETE_ARCHITECTURE] — 38 Subsystems

```
[OMNIROUTE]
│
├─ [CORE_GATEWAY]
│  ├── [AI_GATEWAY]                — Unified API for all clients
│  ├── [MODEL_GATEWAY]             — Model abstraction + routing
│  ├── [UNIFIED_API]               — Single endpoint, 359+ providers
│  ├── [OPENAI_COMPATIBILITY]      — OpenAI-compatible protocol
│  ├── [PROTOCOL_TRANSLATION]      — Provider format conversion
│  └── [PROTOCOL_LAYER]            — REST, MCP, A2A, Batch, Files
│
├─ [ROUTING_SYSTEM]
│  ├── [AI_ROUTER]                 — Intelligent routing engine
│  ├── [ROUTING_STRATEGIES]        — 20+ routing modes
│  ├── [AUTO_COMBO]                — Multi-factor intelligent selection
│  ├── [COMBOS]                    — Pre-tuned routing combinations
│  ├── [FUSION]                    — Multi-model voting + judge
│  ├── [PIPELINE]                  — Sequential multi-step execution
│  ├── [ROUTING_TRANSPARENCY]      — Expose routing decisions via headers
│  └── [CACHE_AFFINITY]            — Cache-aware routing decisions
│
├─ [QUOTA_SYSTEM]
│  ├── [QUOTA_ENGINE]              — Quota + headroom tracking
│  ├── [QUOTA_SHARE]               — Shared accounts, pooled keys, quota slices
│  ├── [ACCOUNT_ROTATION]          — Quota-aware account switching
│  ├── [CONTEXT_RELAY]             — Transparent session transfer
│  ├── [HEADROOM_MANAGEMENT]       — Buffer before exhaustion
│  ├── [RESET_WINDOWS]             — Reset schedule tracking
│  └── [COST_HEADERS]              — Per-request cost telemetry
│
├─ [RESILIENCE_SYSTEM]
│  ├── [ADMISSION_CONTROL]         — Overload protection + request queue
│  ├── [BACKPRESSURE]              — Load shedding + concurrency control
│  ├── [REQUEST_QUEUE]             — Heavy request queueing
│  ├── [RETRY_ENGINE]              — Exponential backoff + jitter
│  ├── [CIRCUIT_BREAKER]           — Trip on repeated failures
│  ├── [COOLDOWN]                  — Temporary provider blacklist
│  ├── [FAILOVER_ENGINE]           — Automatic fallback chain
│  ├── [HEALTH_CHECK]              — Provider + model availability
│  └── [SELF_HEALING]              — Automatic recovery loops
│
├─ [COMPRESSION_SYSTEM]
│  ├── [COMPRESSION_ENGINE]        — Core compression orchestration
│  ├── [RTK]                       — Domain-specific reduction rules
│  ├── [CAVEMAN]                   — Aggressive shorthand reduction
│  ├── [LLMLINGUA]                 — Token pruning via LLMlingua
│  ├── [ULTRA]                     — Additional compression engine
│  ├── [OMNIGLYPH]                 — Token symbolization
│  ├── [GCF]                       — Graph compression filter
│  ├── [MCP_ACCESSIBILITY_FILTER]  — Accessibility-aware compression
│  ├── [COMPRESSION_STUDIO]        — Visual composition + reordering
│  ├── [COMPRESSION_LEARNING]      — Self-improving filter discovery
│  ├── [FIDELITY_GATE]             — Preserve semantic meaning
│  └── [INFLATION_GUARD]           — Prevent decompression explosion
│
├─ [CACHE_SYSTEM]
│  ├── [CACHE]                     — Response caching
│  ├── [PREFIX_CACHE]              — Semantic prefix caching
│  ├── [SEMANTIC_CACHE]            — Vector-based cache matching
│  ├── [CACHE_AFFINITY]            — Route to cache holders
│  └── [CACHE_HIT_OPTIMIZATION]    — Maximize cache effectiveness
│
├─ [AGENT_SYSTEM]
│  ├── [OMNICONDUCTOR]             — Inbound A2A delegation fleet
│  ├── [MCP_SERVER]                — Model Context Protocol interface
│  ├── [A2A_SERVER]                — Agent-to-Agent execution layer
│  ├── [ACP_AGENT_DISCOVERY]       — Agent capability provider discovery
│  ├── [AGENT_FLEET]               — Multi-agent orchestration
│  ├── [AGENT_CARD]                — Agent metadata + capabilities
│  ├── [SKILL_EXECUTION]           — Skill invocation + routing
│  └── [AGENT_COORDINATION]        — Multi-agent workflow
│
├─ [SKILLS_AND_PLUGINS]
│  ├── [SKILL_REGISTRY]            — Central skill catalog
│  ├── [SKILL_MARKETPLACE]         — Skill discovery + installation
│  ├── [GITHUB_SKILL_DISCOVERY]    — Auto-import from GitHub repos
│  ├── [PLUGIN_SYSTEM]             — Extensible plugin framework
│  ├── [PLUGIN_MARKETPLACE]        — Plugin discovery + installation
│  ├── [PLUGIN_PERMISSIONS]        — Scope-based access control
│  └── [PLUGIN_LIFECYCLE]          — Install, enable, disable, remove
│
├─ [API_LAYER]
│  ├── [INFERENCE_API]             — Chat completions endpoint
│  ├── [RESPONSES_API]             — OpenAI Responses protocol
│  ├── [BATCH_API]                 — Batch processing jobs
│  ├── [FILES_API]                 — File upload/download
│  ├── [EMBEDDINGS_API]            — Vector embeddings
│  ├── [IMAGE_GENERATION_API]      — Image generation
│  ├── [VISION_API]                — Image understanding
│  ├── [AUDIO_API]                 — Audio processing
│  ├── [TTS_API]                   — Text-to-speech
│  ├── [STT_API]                   — Speech-to-text
│  └── [OCR_API]                   — Optical character recognition
│
├─ [PROVIDER_SYSTEM]
│  ├── [PROVIDER_REGISTRY]         — Core provider catalog
│  ├── [PROVIDER_ORCHESTRATOR]     — Provider lifecycle management
│  ├── [MODEL_REGISTRY]            — 1,200+ model catalog
│  ├── [RADAR]                     — Live free-tier catalog overlay
│  ├── [FREE_TIER_ENGINE]          — Zero-cost optimization
│  ├── [PROVIDER_HEALTH]           — Availability + performance
│  ├── [PROVIDER_RANKING]          — Quality/cost/latency scoring
│  └── [CONNECTION_REGISTRY]       — API keys, OAuth, credentials
│
├─ [NETWORK_AND_PROXY]
│  ├── [TAILSCALE]                 — VPN-based access
│  ├── [TUNNELS]                   — Tunnel endpoints
│  ├── [CLOUD_RELAY]               — Edge deployment layer
│  ├── [CLOUDFLARE_WORKERS]        — Cloudflare edge relays
│  ├── [DENO_DEPLOY]               — Deno Deploy edge relays
│  ├── [MITM_TPROXY]               — Transparent proxy + MITM decryption
│  ├── [TRANSPARENT_PROXY]         — Intercept CLI traffic
│  ├── [PROXY_POOL]                — Managed proxy set
│  └── [PROXY_ROTATION]            — Rotate proxies per request
│
├─ [SECURITY_AND_COMPLIANCE]
│  ├── [AUTHORIZATION]             — API key + bearer token auth
│  ├── [GUARDRAILS]                — Comprehensive security gates
│  ├── [ROUTE_GUARDS]              — Route-level access control
│  ├── [SCOPE_GUARDS]              — Permission scope enforcement
│  ├── [SSRF_PROTECTION]           — Server-side request forgery prevention
│  ├── [ERROR_SANITIZATION]        — Safe error message generation
│  ├── [SECRET_REDACTION]          — Redact sensitive data from errors
│  ├── [STEALTH]                   — Fingerprint normalization
│  ├── [PUBLIC_CREDENTIALS]        — Handle public API keys safely
│  ├── [COMPLIANCE]                — Regulatory requirement enforcement
│  ├── [AUDIT_LOG]                 — Immutable request audit trail
│  ├── [BUDGET_GUARD]              — USD spend limits + enforcement
│  └── [SPEND_QUOTAS]              — Per-key USD budget limits
│
├─ [OBSERVABILITY_AND_ANALYTICS]
│  ├── [LOGGING]                   — Request/response logging
│  ├── [METRICS]                   — Prometheus-compatible metrics
│  ├── [TRACING]                   — Distributed trace collection
│  ├── [TELEMETRY]                 — System telemetry
│  ├── [BIGQUERY_EXPORT]           — Log export to BigQuery
│  ├── [HEALTH_DASHBOARD]          — Live health status
│  ├── [ANALYTICS_ENGINE]          — Usage + cost analytics
│  ├── [LATENCY_ANALYSIS]          — P50, P95, P99 tracking
│  ├── [UPTIME_TRACKING]           — Availability percentage
│  └── [ACTIVITY_HEATMAP]          — Usage pattern visualization
│
├─ [INFRASTRUCTURE]
│  ├── [EMBEDDED_SERVICES]         — Redis, 9Router, Bifrost, Mux
│  ├── [REDIS]                     — In-process cache store
│  ├── [9ROUTER]                   — Internal routing service
│  ├── [CLIPROXYAPI]               — CLI proxy API layer
│  ├── [BIFROST]                   — Bridge service
│  ├── [DATABASE]                  — SQLite + Qdrant persistence
│  ├── [VERSION_MANAGER]           — Service versioning + lifecycle
│  ├── [BACKUP]                    — Configuration backup/restore
│  ├── [SYNC]                      — Cross-device configuration sync
│  ├── [DOCKER]                    — Container deployment
│  ├── [ELECTRON]                  — Desktop app (macOS/Windows/Linux)
│  ├── [PWA]                       — Progressive web app
│  └── [TERMUX]                    — Android CLI support
│
├─ [INTEGRATIONS]
│  ├── [CLAUDE_CODE]               — Claude Code IDE integration
│  ├── [CODEX]                     — Codex CLI integration
│  ├── [CURSOR]                    — Cursor IDE integration
│  ├── [CLINE]                     — Cline AI shell
│  ├── [COPILOT]                   — Microsoft Copilot integration
│  ├── [ANTIGRAVITY]               — Company Brain agent integration
│  ├── [OPENCLAW]                  — OpenClaw framework
│  ├── [OBSIDIAN]                  — Obsidian vault sync + MCP tools
│  ├── [GITHUB]                    — GitHub skill discovery + sync
│  └── [TELEGRAM]                  — Telegram bot bridge
│
├─ [INTERFACE_LAYER]
│  ├── [CLI]                       — Command-line control
│  ├── [DASHBOARD]                 — Web observability interface
│  ├── [DESKTOP_APP]               — Electron desktop application
│  ├── [PWA_APP]                   — Browser-based PWA
│  ├── [TERMINAL_UI]               — Terminal-based UI
│  └── [MOBILE_APP]                — Termux/Android support
│
├─ [EVALUATION_AND_TESTING]
│  ├── [EVALUATION]                — Model + routing evaluation
│  ├── [BENCHMARKS]                — Performance benchmarking
│  ├── [PLAYGROUND]                — Interactive testing
│  ├── [TEST_BENCH]                — Automated test framework
│  └── [REGRESSION_TEST]           — Regression detection
│
└─ [OPERATIONS]
   ├── [GAMIFICATION]              — Leaderboards, achievements
   ├── [RELEASE_ENGINEERING]       — Release checklist + gating
   ├── [DOCUMENTATION]             — API docs, guides, tutorials
   └── [COMMUNITY]                 — Support, contributions, feedback
```

---

## [REQUEST_LIFECYCLE] — Complete Flow with 30+ Stages

```
[REQUEST]
    ↓
[AUTHENTICATION]                    — Verify client identity
    ↓
[AUTHORIZATION_CHECK]               — Verify permissions + scopes
    ↓
[ROUTE_GUARD_CHECK]                 — Apply route-level guards
    ↓
[BUDGET_GUARD_CHECK]                — Check USD spend limits
    ↓
[REQUEST_VALIDATION]                — Schema + format check
    ↓
[CAPABILITY_DETECTION]              — What does this request need?
    ↓
[MODEL_RESOLUTION]                  — Resolve model alias/name
    ↓
[ALIAS_RESOLUTION]                  — smart → AUTO_COMBO, cheap → AUTO_CHEAP
    ↓
[COMBO_RESOLUTION]                  — Map to routing strategy
    ↓
[ADMISSION_CONTROL_CHECK]           — Check queue + concurrency limits
    ↓
[PROVIDER_SELECTION]                — Which providers can handle this?
    ↓
[ACCOUNT_SELECTION]                 — Which accounts have quota?
    ↓
[QUOTA_CHECK]                       — Verify headroom before request
    ↓
[CACHE_AFFINITY_ROUTING]            — Route to cache holder if hit likely
    ↓
[CACHE_LOOKUP]                      — Check semantic/prefix cache
    ├── HIT → [CACHE_RESPONSE] → [COST_ESTIMATE] → [RESPONSE]
    └── MISS ↓
    ↓
[HEALTH_CHECK]                      — Provider/model healthy?
    ↓
[COMPRESSION_CLASSIFICATION]        — What content type is this?
    ↓
[COMPRESSION_ENGINE_SELECTION]      — Which engines to apply?
    ↓
[COMPRESSION_APPLY]                 — Apply RTK/Caveman/Stacked/etc
    ↓
[PROTOCOL_TRANSLATION]              — Convert to provider protocol
    ↓
[ROUTING_DECISION_LOGGING]          — Log routing choice + candidates
    ↓
[COST_ESTIMATION]                   — Estimate request cost
    ↓
[UPSTREAM_REQUEST]                  — Send to AI provider
    ↓
[STREAMING]                         — Stream response chunks (if enabled)
    ↓
[PROTOCOL_REVERSE_TRANSLATION]      — Convert back to client format
    ↓
[RESPONSE]                          — Return to client
    ├── [X-OMNIROUTE-DECISION]      — Include routing metadata header
    ├── [X-OMNIROUTE-COST]          — Include actual cost header
    ├── [X-OMNIROUTE-CACHED]        — Note if cache hit
    └── [X-OMNIROUTE-COMPRESSION]   — Note compression applied
    ↓
[USAGE_CAPTURE]                     — Record tokens + latency
    ↓
[COST_CAPTURE]                      — Calculate actual cost
    ↓
[QUOTA_UPDATE]                      — Deduct from account quota
    ↓
[CACHE_STORAGE]                     — Store in semantic/prefix cache
    ↓
[TELEMETRY]                         — Send metrics to observability
    ↓
[LOGGING]                           — Log to audit trail
    ↓
[LEARNING]                          — Update routing scores
    ↓
[OBSERVABILITY_UPDATE]              — Update dashboard
    ↓
[COMPLETE]
```

**Failure branch:**

```
[ERROR]
    ↓
[ERROR_CLASSIFICATION]              — What type of failure?
    ↓
[ERROR_SANITIZATION]                — Remove secrets from error
    ↓
[RETRY?]
    ├── YES → [BACKOFF] → [RETRY_COUNT_CHECK]
    │         ├── LIMIT_OK → [UPSTREAM_REQUEST]
    │         └── LIMIT_HIT ↓
    └── NO ↓
         ↓
[FALLBACK?]
    ├── YES → [NEXT_TARGET] → [PROVIDER_SELECTION]
    └── NO ↓
         ↓
[CIRCUIT_BREAKER?]
    ├── YES → [COOLDOWN_PROVIDER]
    └── NO ↓
         ↓
[ESCALATE?]
    ├── YES → [HIGHER_AUTHORITY]
    └── NO ↓
         ↓
[FAIL] → [CLIENT_SAFE_ERROR] → [RESPONSE]
```

---

## [OMNICONDUCTOR] — Agent Fleet Delegation

```
[OMNICONDUCTOR]
│
├── [INBOUND_A2A_DELEGATION]     ← Agent requests work
├── [AGENT_FLEET]                ← Pool of available agents
├── [CONDUCTOR_SKILLS]           ← Orchestration capabilities
├── [AGENT_CARD_REGISTRY]        ← Agent metadata
├── [TASK_QUEUE]                 ← Pending task queue
├── [FARO_VOICE]                 ← Voice command interface
├── [PUSH_TO_TALK]               ← PTT activation
├── [AGENT_DELEGATION]           ← Route to agent
└── [MULTI_AGENT_CONTROL]        ← Manage fleet execution
```

---

## [QUOTA_SHARE] — Shared Account Pooling

```
[QUOTA_SHARE]
│
├── [SHARED_ACCOUNT]             ← Multiple clients share quota
├── [POOLED_KEYS]                ← Key pool management
├── [QUOTA_SLICES]               ← Allocate quota to users
├── [WORK_CONSERVING]            ← Use idle quota
├── [IDLE_LENDING]               ← Lend to high-need users
├── [FAIRNESS]                   ← Prevent starvation
├── [QUOTA_LEASE]                ← Temporary allocations
├── [QUOTA_ALLOCATION]           ← Dynamic rebalancing
└── [QUOTA_REBALANCING]          ← Optimize distribution
```

---

## [ROUTING_TRANSPARENCY] — Expose Decisions

```
[ROUTING_TRANSPARENCY]
│
├── [ROUTING_DECISION]           ← What was selected?
├── [DECISION_HEADER]            ← X-OMNIROUTE-DECISION
├── [STRATEGY]                   ← Which strategy used?
├── [SELECTED_PROVIDER]          ← Provider chosen
├── [SELECTED_CONNECTION]        ← Connection used
├── [LATENCY]                    ← Expected latency
├── [CANDIDATE_POOL]             ← All considered options
├── [AUTO_COMBO_CANDIDATES]      ← Auto-Combo scoring
└── [ROUTE_EXPLANATION]          ← Rationale (human-readable)
```

---

## [ADMISSION_CONTROL] — Overload Protection

```
[ADMISSION_CONTROL]
│
├── [OVERLOAD_PROTECTION]        ← Prevent cascade failures
├── [REQUEST_QUEUE]              ← Buffer surge requests
├── [HEAVY_REQUEST_QUEUEING]     ← Long-context prioritization
├── [RPM_ROLLING_LEASE]          ← RPM fairness distribution
├── [CONNECTION_CAPACITY]        ← Track available connections
├── [BACKPRESSURE]               ← Slow down if overloaded
├── [CONCURRENCY_CONTROL]        ← Limit parallel requests
├── [QUEUE_TIMEOUT]              ← Discard if waited too long
└── [LOAD_SHEDDING]              ← Drop low-priority requests
```

---

## [COMPRESSION_STUDIO] — Visual Engine Composition

```
[COMPRESSION_STUDIO]
│
├── [ENGINE_REGISTRY]            ← 12 available engines
├── [ENGINE_PIPELINE]            ← Composable sequence
├── [DRAG_REORDER]               ← Visual reordering
├── [ENGINE_ENABLE_DISABLE]      ← Toggle engines on/off
├── [ENGINE_CONFIGURATION]       ← Tune each engine
├── [FIDELITY_GATE]              ← Preserve semantic meaning
├── [INFLATION_GUARD]            ← Prevent expansion
└── [PREVIEW]                    ← See compression effect
```

---

## [COMPRESSION_LEARNING] — Self-Improving Filters

```
[COMPRESSION_LEARNING]
│
├── [RAW_TOOL_OUTPUT]            ← Captured output
├── [NOISE_DETECTION]            ← Find repetitive patterns
├── [REPEATED_NOISE]             ← Identify common noise
├── [FILTER_DISCOVERY]           ← Generate RTK filters
├── [FILTER_SUGGESTION]          ← Suggest improvements
├── [COMMAND_SAMPLE]             ← Example command
├── [FILTER_REGISTRY]            ← Store learned filters
├── [LEARN]                      ← Update from observations
└── [AUDIT]                      ← Verify filter safety
```

---

## [EMBEDDED_SERVICES] — Internal Infrastructure

```
[EMBEDDED_SERVICES]
│
├── [REDIS]                      ← In-process cache
├── [9ROUTER]                    ← Internal routing
├── [CLIPROXYAPI]                ← CLI proxy layer
├── [BIFROST]                    ← Bridge service
├── [MUX]                        ← Request multiplexing
├── [SERVICE_LIFECYCLE]          ← Start/stop/health
├── [AUTO_START]                 ← Start on boot
├── [SERVICE_HEALTH]             ← Health checks
├── [SERVICE_LOGS]               ← Per-service logging
└── [SUPERVISED_SERVICE]         ← Restart on failure
```

---

## [VERSION_MANAGER] — Service Versioning

```
[VERSION_MANAGER]
│
├── [VERSION]                    ← Current version
├── [INSTALL]                    ← Install specific version
├── [UPDATE]                     ← Update to new version
├── [ROLLBACK]                   ← Revert to previous
├── [START]                      ← Start service
├── [STOP]                       ← Stop service
├── [RESTART]                    ← Restart service
├── [AUTO_START]                 ← Enable/disable auto-start
├── [SERVICE_VERSION]            ← Track versions
├── [COMPATIBILITY]              ← Check compatibility
└── [RELEASE_STATE]              ← Stable/beta/alpha
```

---

## [PLUGIN_SYSTEM] — Extensibility

```
[PLUGIN_SYSTEM]
│
├── [PLUGIN_REGISTRY]            ← Available plugins
├── [PLUGIN_MANIFEST]            ← Plugin metadata
├── [PLUGIN_INSTALL]             ← Install plugin
├── [PLUGIN_ENABLE]              ← Enable plugin
├── [PLUGIN_DISABLE]             ← Disable plugin
├── [PLUGIN_PERMISSIONS]         ← Scope-based access
├── [PLUGIN_API]                 ← Extension interface
├── [PLUGIN_LIFECYCLE]           ← Initialize/cleanup
└── [PLUGIN_MARKETPLACE]         ← Discover plugins
```

---

## [OBSIDIAN_INTEGRATION] — Knowledge Vault Sync

```
[OBSIDIAN_INTEGRATION]
│
├── [VAULT]                      ← Obsidian vault path
├── [VAULT_SYNC]                 ← Bidirectional sync
├── [NOTE]                       ← Markdown files
├── [WIKI_LINK]                  ← [[ENTITY]] references
├── [BACKLINK]                   ← Reverse references
├── [TAG]                        ← #topic organization
├── [FRONTMATTER]                ← YAML metadata
├── [GRAPH]                      ← Relationship visualization
├── [MCP_TOOLS]                  ← Expose as MCP tools
├── [NOTE_READ]                  ← Read from vault
├── [NOTE_WRITE]                 ← Write to vault
├── [NOTE_SEARCH]                ← Full-text search
├── [REGISTRY_SYNC]              ← Sync registries ↔ vault
└── [KNOWLEDGE_GRAPH_SYNC]       ← Update Neo4j from vault
```

---

## [CLOUD_RELAY] — Edge Deployment

```
[CLOUD_RELAY]
│
├── [CLOUDFLARE_WORKERS]         ← Edge compute
├── [DENO_DEPLOY]                ← Deno edge platform
├── [EDGE_RELAY]                 ← Relay at edge
├── [UPSTREAM]                   ← Backend connection
├── [DOWNSTREAM]                 ← Client connection
├── [AUTH]                       ← Token verification
├── [FORWARDING]                 ← Request relay
├── [EDGE_POLICY]                ← Geographic routing
└── [FAILOVER]                   ← Edge fallback
```

---

## [BIGQUERY_EXPORT] — Log Analytics

```
[BIGQUERY_EXPORT]
│
├── [SCHEDULE]                   ← Export frequency
├── [BIGQUERY]                   ← Destination project
├── [EXPORT_JOB]                 ← BigQuery job management
├── [LOG_BATCH]                  ← Batched logs
├── [SCHEMA]                     ← BigQuery schema
├── [DELIVERY]                   ← Ensure delivery
├── [FAILURE_RETRY]              ← Retry on failure
└── [RETENTION]                  ← Data retention policy
```

---

## [REALITY_VS_CAPABILITY] — Critical Distinction

**Important:** Do NOT model as existing:

```
[OMNIROUTE] → [ARBITRARY_EXTERNAL_MCP_SERVERS] → [AGGREGATED_TOOLS]
```

This feature does **not yet exist**. The repo explicitly distinguishes:

```
[OMNIROUTE_MCP_SERVER]          [EXTERNAL_MCP_SERVERS]
    ↓                                ↓
[OMNIROUTE_TOOLS]              [SEPARATE_ECOSYSTEM]
```

**This is the [[REALITY]] vs [[DESIRED_CAPABILITY]] separation you maintain in [[WHERE_WE_ARE]].**

---

## [COMPANY_BRAIN_INTEGRATION] — Complete Connection

```
[[COMPANY_BRAIN]]
    │
    ├── [[CLAUDE_CODE]]
    ├── [[ANTIGRAVITY]]
    ├── [[CODEX]]
    ├── [[OPENCLAW]]
    │
    └── [[OMNIROUTE]] (v2.0)
         │
         ├── [ROUTING_ENGINE] + [AUTO_COMBO] + [CACHE_AFFINITY]
         ├── [QUOTA_ENGINE] + [QUOTA_SHARE] + [ACCOUNT_ROTATION]
         ├── [RESILIENCE_ENGINE] + [ADMISSION_CONTROL] + [CIRCUIT_BREAKER]
         ├── [COMPRESSION_ENGINE] + [COMPRESSION_STUDIO] + [COMPRESSION_LEARNING]
         ├── [OMNICONDUCTOR] + [MCP] + [A2A] + [ACP]
         ├── [SKILLS_MARKETPLACE] + [GITHUB_SKILL_DISCOVERY]
         ├── [OBSIDIAN_INTEGRATION]
         ├── [CLOUD_RELAY]
         ├── [BIGQUERY_EXPORT]
         ├── [BUDGET_GUARD] + [COST_HEADERS]
         ├── [GUARDRAILS] + [ERROR_SANITIZATION] + [STEALTH]
         └── [RADAR] + [PROVIDER_REGISTRY] + [MODEL_REGISTRY]
              │
              ↓
         [[PROVIDER_REGISTRY]]
         [[MODEL_REGISTRY]]
         [[ACCOUNT_REGISTRY]]
              │
              ↓
         [[AI_PROVIDER]]
              │
              ↓
         [MODEL_RESPONSE]
              │
              ↓
         [[KNOWLEDGE_GRAPH]]
              │
              ↓
         [[WHERE_WE_ARE]]
              │
              ↓
         [[NEXT_DECISION]] ↺
```

---

**OmniRoute v2.0: 38 subsystems, cybernetic feedback, complete AI infrastructure control plane.**

---

**Related:** [[WHOAMI.md]] · [[WHERE_WE_ARE.md]] · [[DATA_FLOW.md]] · [[INFRASTRUCTURE.md]] · [[CROSS_LINK_MASTER_ONTOLOGY.md]] · [[TASK_EXECUTION_MASTER_ONTOLOGY.md]] · [[OBSIDIAN_MASTER_ONTOLOGY.md]]

**AI infrastructure control plane v2.0: Enhanced with 30 missing subsystems for complete coverage.**
