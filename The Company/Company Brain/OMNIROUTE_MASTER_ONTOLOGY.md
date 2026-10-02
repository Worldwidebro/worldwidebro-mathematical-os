---
type: infrastructure-control-ontology
canonical: true
authority: ai-connectivity-plane
updated_at: 2026-10-02T22:00:00Z
source_of_truth: true
---

# OMNIROUTE_MASTER_ONTOLOGY — AI Infrastructure Control Plane

**OmniRoute is not just an "AI proxy." It is a complete AI connectivity, routing, resilience, optimization, protocol, observability, and agent infrastructure layer.**

This ontology models OmniRoute as a **first-class system node** with explicit governance, routing policies, quota management, resilience strategies, and deep integration with the Company Brain's knowledge graph and decision-making.

---

## [OMNIROUTE_IDENTITY] — System Architecture

```
[OMNIROUTE]
│
├── [AI_GATEWAY]             — Unified API for all AI clients
├── [MODEL_GATEWAY]          — Model abstraction + routing
├── [UNIFIED_API]            — Single endpoint, 359+ providers
├── [AI_ROUTER]              — Intelligent routing engine
├── [PROVIDER_ORCHESTRATOR]  — Provider/account management
├── [QUOTA_ORCHESTRATOR]     — Quota + headroom management
├── [FAILOVER_ENGINE]        — Automatic fallback + retry
├── [RESILIENCE_ENGINE]      — Circuit breaker + cooldown
├── [COMPRESSION_ENGINE]     — RTK + Caveman + stacked transforms
├── [PROTOCOL_GATEWAY]       — OpenAI-compatible API layer
├── [MCP_SERVER]             — Model Context Protocol interface
├── [A2A_SERVER]             — Agent-to-Agent execution
├── [CLI]                    — Command-line control
├── [DASHBOARD]              — Web observability interface
├── [DESKTOP_APPLICATION]    — Electron app (macOS/Windows/Linux)
├── [PWA]                    — Progressive web app
├── [ANDROID_RUNTIME]        — Termux support
└── [AGENT_CONTROL_PLANE]    — Integration with Company Brain agents
```

---

## [REQUEST_LIFECYCLE] — The Complete Flow

**This is the single most important operational ontology.**

```
[REQUEST]
    ↓
[AUTHENTICATION]            — Verify client identity
    ↓
[REQUEST_VALIDATION]        — Schema + format check
    ↓
[CAPABILITY_DETECTION]      — What does this request need?
    ↓
[MODEL_RESOLUTION]          — Resolve model alias/name
    ↓
[ALIAS_RESOLUTION]          — smart → AUTO_COMBO, cheap → AUTO_CHEAP
    ↓
[COMBO_RESOLUTION]          — Map to combo/routing strategy
    ↓
[PROVIDER_SELECTION]        — Which providers can handle this?
    ↓
[ACCOUNT_SELECTION]         — Which accounts have quota?
    ↓
[QUOTA_CHECK]               — Verify headroom before request
    ↓
[HEALTH_CHECK]              — Provider/model healthy?
    ↓
[COMPRESSION]               — Apply RTK/Caveman/stacked
    ↓
[TRANSLATION]               — Convert to provider protocol
    ↓
[UPSTREAM_REQUEST]          — Send to AI provider
    ↓
[MODEL_EXECUTION]           — Provider processes request
    ↓
[STREAMING]                 — Stream response (if enabled)
    ↓
[RESPONSE_TRANSLATION]      — Convert back to client format
    ↓
[RESPONSE]                  — Return to client
    ↓
[USAGE_CAPTURE]             — Record tokens + metrics
    ↓
[COST_CAPTURE]              — Calculate cost
    ↓
[QUOTA_UPDATE]              — Update account quota used
    ↓
[TELEMETRY]                 — Send metrics
    ↓
[LOGGING]                   — Log request/response
    ↓
[CACHE]                     — Cache response for future hits
    ↓
[LEARNING]                  — Update routing scores
    ↓
[OBSERVABILITY_UPDATE]      — Update dashboard metrics
```

**Failure branch:**

```
[ERROR]
    ↓
[CLASSIFY_ERROR]            — What type of failure?
    ↓
[RETRY?]
    ├── YES → [RETRY] → [BACKOFF] → [UPSTREAM_REQUEST]
    └── NO
         ↓
[FALLBACK?]
    ├── YES → [NEXT_TARGET] → [PROVIDER_SELECTION]
    └── NO
         ↓
[ESCALATE?]
    ├── YES → [HIGHER_AUTHORITY]
    └── NO
         ↓
[FAIL]
```

---

## [OMNIROUTE_CONTROL_LOOP] — Cybernetic Feedback

OmniRoute operates as a **continuous learning system**:

```
[OBSERVE]               ← What happened?
    ↓
[MEASURE]               ← Latency, cost, errors, success
    ↓
[CLASSIFY]              ← Categorize performance
    ↓
[SCORE]                 ← Rate provider/model/combo
    ↓
[SELECT]                ← Choose best option for next request
    ↓
[EXECUTE]               ← Send request
    ↓
[VERIFY]                ← Check result quality
    ↓
[RECORD]                ← Log metrics + evidence
    ↓
[LEARN]                 ← Update scoring models
    ↓
[RECONFIGURE]           ← Adjust routing weights
    ↓
[OBSERVE] ↺             ← Feed back to top
```

---

## [CLIENT_CONNECTIVITY] — Who Connects

```
[CLIENTS]
│
├── [[CLAUDE_CODE]]          — Code assistant
├── [[CODEX_CLI]]            — Command-line interface
├── [[CURSOR]]               — IDE integration
├── [[CLINE]]                — AI shell
├── [[COPILOT]]              — Microsoft Copilot
├── [[ANTIGRAVITY]]          — Company Brain agent
├── [[OPENCLAW]]             — Custom framework
├── [[KILO_CODE]]            — Development environment
├── [[CONTINUE]]             — IDE plugin
├── [[FACTORY_DROID]]        — Automation agent
├── [[AIDER]]                — Git-aware AI
├── [[GOOSE]]                — Agent framework
├── [[DEVIN_CLI]]            — Autonomous coding
├── [[KIMI_CODING]]          — Chinese AI coding
├── [[COMMAND_CODE]]         — Command-line AI
├── [[CUSTOM_CLI]]           — Custom applications
├── [[CUSTOM_APPLICATION]]   — Internal tools
├── [[WEB_APPLICATION]]      — Browser-based
├── [[MOBILE_APPLICATION]]   — Mobile apps
└── [[AGENT]]                — Company Brain agents
```

**Connection model:**

```
[CLIENT]
    ↓
[BASE_URL] (http://100.87.214.70:3004 or https://remote)
    ↓
[/v1]
    ↓
[AUTHENTICATION]
    ↓
[MODEL]
    ↓
[[OMNIROUTE]]
```

---

## [PROVIDER_REGISTRY] — Dynamic Catalog

OmniRoute maintains a **live, evolving provider registry** with 359+ providers:

```
[PROVIDER]
│
├── [PROVIDER_ID]
├── [PROVIDER_NAME]
├── [PROVIDER_TYPE]          — API_KEY, OAUTH, FREE, COOKIE, LOCAL
├── [PROVIDER_PROTOCOL]      — OpenAI-compatible? gRPC? Custom?
├── [PROVIDER_ENDPOINT]      — Base URL
├── [PROVIDER_MODELS]        — List of available models
├── [PROVIDER_CAPABILITIES]  — Chat, vision, image, audio, embedding
├── [PROVIDER_LIMITS]        — Rate limits, max tokens
├── [PROVIDER_QUOTA]         — Free tier quota, monthly limits
├── [PROVIDER_COST]          — $ per token (input/output)
├── [PROVIDER_HEALTH]        — Current status, uptime
├── [PROVIDER_REGION]        — Geographic location
├── [PROVIDER_TERMS]         — Usage terms, restrictions
├── [PROVIDER_AUTH]          — API key, OAuth, session cookie
├── [PROVIDER_PROXY]         — Proxy server (if needed)
├── [PROVIDER_MANIFEST]      — Metadata + documentation
├── [PROVIDER_TIER]          — Free, paid, premium
├── [PROVIDER_STATUS]        — Active, deprecated, experimental
└── [PROVIDER_METADATA]      — Last updated, verified date
```

---

## [MODEL_REGISTRY] — 1,200+ Models

Each provider offers multiple models:

```
[MODEL]
│
├── [MODEL_ID]               — "claude-opus-5", "gpt-4-turbo"
├── [MODEL_NAME]             — Human-readable name
├── [MODEL_PROVIDER]         — [[ANTHROPIC]], [[OPENAI]], etc.
├── [MODEL_FAMILY]           — Claude, GPT, Gemini, etc.
├── [MODEL_VERSION]          — Latest version + aliases
├── [MODEL_MODALITY]         — Text, vision, audio, video, image
├── [MODEL_CONTEXT]          — 8K, 32K, 200K, 1M tokens
├── [MODEL_OUTPUT_LIMIT]     — Max output tokens
├── [MODEL_REASONING]        — Extended thinking? o1-style?
├── [MODEL_TOOLS]            — Function calling? Tool use?
├── [MODEL_STREAMING]        — Server-sent events? WebSocket?
├── [MODEL_COST]             — $/1M input, $/1M output
├── [MODEL_QUOTA]            — Rate limit per account
├── [MODEL_HEALTH]           — Current availability
├── [MODEL_VISIBILITY]       — Public? Private? Limited beta?
├── [MODEL_ALIAS]            — smart → claude-opus, cheap → gpt-3.5
└── [MODEL_CAPABILITIES]     — List of features
```

---

## [ROUTING_ENGINE] — The Decision System

```
[ROUTING_ENGINE]
│
├── [ROUTE_SELECTION]        — Which combo/strategy to use?
├── [TARGET_SELECTION]       — Which targets in the combo?
├── [MODEL_SELECTION]        — Which model best fits request?
├── [PROVIDER_SELECTION]     — Which providers have the model?
├── [ACCOUNT_SELECTION]      — Which accounts have quota?
├── [QUOTA_SELECTION]        — Which account has most headroom?
├── [COST_SELECTION]         — Cheapest provider available?
├── [HEALTH_SELECTION]       — Healthiest provider?
├── [CONTEXT_SELECTION]      — Preserve session/context?
├── [CACHE_SELECTION]        — Use cached response?
├── [FAILOVER_SELECTION]     — What's the backup?
└── [POLICY_SELECTION]       — What policies apply?
```

---

## [ROUTING_STRATEGIES] — Current Modes

OmniRoute documents these routing strategies (list evolves):

```
[ROUTING_STRATEGIES]
│
├── [PRIORITY]               — Fixed priority order
├── [WEIGHTED]               — Probabilistic distribution
├── [ROUND_ROBIN]            — Rotate through targets
├── [CONTEXT_RELAY]          — Preserve context across rotations
├── [FILL_FIRST]             — Use cheapest until quota hit
├── [P2C]                     — Power of two choices
├── [RANDOM]                 — Random selection
├── [LEAST_USED]             — Pick underutilized account
├── [COST_OPTIMIZED]         — Minimize $ spend
├── [RESET_AWARE]            — Track quota reset times
├── [RESET_WINDOW]           — Plan around reset windows
├── [HEADROOM]               — Preserve headroom buffer
├── [STRICT_RANDOM]          — No optimization
├── [AUTO]                   — Automatic best choice
├── [LKGP]                   — Last Known Good Provider
├── [CONTEXT_OPTIMIZED]      — Preserve session integrity
├── [CACHE_OPTIMIZED]        — Maximize cache hits
├── [FUSION]                 — Multi-model voting
├── [PIPELINE]               — Sequential multi-step execution
└── [AUTO_COMBO]             — Intelligent multi-factor scoring
```

---

## [AUTO_COMBO] — Intelligent Selection

OmniRoute's **self-configuring routing mode** analyzes requests and selects optimal paths:

```
[AUTO_COMBO]
│
├── [AUTO_CODING]            — For code generation/analysis
├── [AUTO_FAST]              — Minimize latency
├── [AUTO_CHEAP]             — Minimize cost
├── [AUTO_OFFLINE]           — Local-only models
├── [AUTO_SMART]             — Best quality regardless of cost
├── [AUTO_LKGP]              — Use last successful provider
└── [AUTO_CHAOS]             — Multi-model panel + judge
```

**Underlying selection logic:**

```
[REQUEST]
    ↓
[REQUEST_CLASSIFICATION]    — Is this code? Chat? Analysis?
    ↓
[CAPABILITY_REQUIREMENTS]   — What does it need?
    ↓
[MODEL_CANDIDATES]          — Which models can do this?
    ↓
[PROVIDER_CANDIDATES]       — Which providers have them?
    ↓
[ACCOUNT_CANDIDATES]        — Which accounts are available?
    ↓
[HEALTH_CHECK]              — Are they healthy?
    ↓
[QUOTA_CHECK]               — Do they have quota?
    ↓
[COST_ANALYSIS]             — How expensive?
    ↓
[CONTEXT_ANALYSIS]          — Can they handle the context?
    ↓
[CAPABILITY_ANALYSIS]       — Do they have required features?
    ↓
[POLICY_CHECK]              — Do they comply with policies?
    ↓
[SCORE]                     — Rate each option
    ↓
[SELECT]                    — Pick winner
    ↓
[EXECUTE]
```

---

## [QUOTA_ENGINE] — Headroom Management

```
[QUOTA]
│
├── [ACCOUNT_QUOTA]          — Quota for specific account
├── [PROVIDER_QUOTA]         — Provider's published limits
├── [MODEL_QUOTA]            — Per-model rate limits
├── [DAILY_QUOTA]            — Daily reset quota
├── [MONTHLY_QUOTA]          — Monthly billing cycle
├── [REQUEST_LIMIT]          — Requests per minute/hour
├── [TOKEN_LIMIT]            — Tokens per period
├── [CREDIT_LIMIT]           — $ credit limit
├── [RESET_TIME]             — When does quota reset?
├── [HEADROOM]               — Buffer before exhaustion
├── [USAGE]                  — Tokens consumed so far
├── [REMAINING]              — Tokens left
├── [LIMIT]                  — Hard limit
└── [QUOTA_HEALTH]           — Status (healthy, low, exhausted)
```

**Quota lifecycle:**

```
[AVAILABLE]
    ↓
[CONSUMING]                 ← Each request uses tokens
    ↓
[LOW]                       ← Below headroom threshold
    ↓
[ROTATION_TRIGGERED]        ← Switch to next account
    ↓
[EXHAUSTED]                 ← Account at limit
    ↓
[RESET_PENDING]             ← Waiting for reset time
    ↓
[RESET]                     ← Quota resets
    ↓
[AVAILABLE] ↺
```

---

## [ACCOUNT_ROTATION] — Quota-Aware Switching

When an account's quota gets low, OmniRoute rotates to another:

```
[ACTIVE_ACCOUNT]
    ↓ [QUOTA_CHECK]
    ↓
[LOW_HEADROOM?]
    ├── YES
    │   ↓
    │ [GENERATE_CONTEXT_RELAY]  ← Summarize session
    │   ↓
    │ [NEXT_ACCOUNT]            ← Switch to Account B
    │   ↓
    │ [INJECT_CONTEXT]          ← Resume session
    │   ↓
    │ [CONTINUE] ← Request continues transparently
    │
    └── NO
        ↓
    [CONTINUE]
```

---

## [RESILIENCE_ENGINE] — Failure Recovery

```
[RESILIENCE]
│
├── [RETRY]                  — Exponential backoff
├── [BACKOFF]                — Jitter to avoid thundering herd
├── [CIRCUIT_BREAKER]        — Trip on repeated failures
├── [COOLDOWN]               — Temporary provider blacklist
├── [QUEUE]                  — Buffer requests during outage
├── [ANTI_THUNDERING_HERD]   — Distributed retry with jitter
├── [429_CLASSIFICATION]     — Rate limit vs. quota exhaustion
├── [UPSTREAM_HINTS]         — Use provider's Retry-After headers
├── [TIMEOUT_CONTROL]        — Adaptive timeout tuning
├── [PROVIDER_EXPIRATION]    — Disable failed providers
├── [ACCOUNT_DISABLE]        — Temporarily skip bad accounts
├── [MODEL_COOLDOWN]         — Cooldown broken models
└── [SELF_HEALING]           — Automatic recovery + retry
```

---

## [COMPRESSION_ENGINE] — Token Reduction

OmniRoute reduces tokens **15-95%** via compression:

```
[COMPRESSION]
│
├── [RTK]                    — Domain-specific reduction rules
│   ├── [SHELL]              — Bash/shell command compression
│   ├── [GIT]                — Git output compression
│   ├── [TEST]               — Test output compression
│   ├── [BUILD]              — Build log compression
│   ├── [PACKAGE]            — Package manager compression
│   ├── [DOCKER]             — Docker command compression
│   ├── [INFRASTRUCTURE]     — Infrastructure output compression
│   ├── [JSON]               — JSON formatting compression
│   └── [STACK_TRACE]        — Stack trace compression
│
├── [CAVEMAN]                — Aggressive shorthand reduction
├── [STACKED]                — Multiple transformation passes
├── [LANGUAGE_RULES]         — Grammar-based reduction
├── [RULE_PACKS]             — Bundled rule sets
├── [COMMAND_FILTERS]        — Command-specific filters
├── [CONTEXT_REDUCTION]      — Trim context windows
├── [TOKEN_REDUCTION]        — Minimize output tokens
├── [CACHE_OPTIMIZATION]     — Cache compressed versions
├── [RAW_OUTPUT_RECOVERY]    — Decompress when needed
├── [COMPRESSION_PREVIEW]    — Show what will be compressed
├── [COMPRESSION_ANALYTICS]  — Track savings
└── [COMPRESSION_COMBOS]     — Pre-tuned compression modes
```

**Compression pipeline:**

```
[INPUT]
    ↓
[CLASSIFY_CONTENT]          ← Is this shell? JSON? Stack trace?
    ↓
[APPLY_RTK]                 ← Domain-specific rules
    ↓
[APPLY_CAVEMAN]             ← Aggressive shorthand
    ↓
[APPLY_STACKED]             ← Multiple passes
    ↓
[VERIFY_INTEGRITY]          ← Can we decompress this?
    ↓
[OUTPUT]                    ← Compressed, token-efficient
```

---

## [MCP_SERVER] — Model Context Protocol

```
[MCP_SERVER]
│
├── [MCP_STDIO]              — Standard input/output transport
├── [MCP_HTTP]               — HTTP/REST transport
├── [MCP_SSE]                — Server-Sent Events transport
├── [MCP_STREAMABLE_HTTP]    ← Efficient streaming
│
├── [MCP_TOOL]               — Function calling interface
├── [MCP_SCOPE]              — Permission scoping
├── [MCP_AUTH]               — Authentication/authorization
├── [MCP_AUDIT]              — Request logging + tracing
└── [MCP_CLIENT]             — Integrated with Claude, etc.
```

**Architecture:**

```
[[CLAUDE]]
    ↓
[MCP]
    ↓
[[OMNIROUTE]]
    ↓
[110+ TOOLS]
    ├── Provider management
    ├── Combo configuration
    ├── Quota monitoring
    ├── Health checks
    ├── Analytics
    ├── Security
    └── ... (see GitHub for complete list)
```

---

## [A2A_SERVER] — Agent-to-Agent Execution

```
[A2A_SERVER]
│
├── [AGENT_CARD]             — Agent metadata + capabilities
├── [AGENT_DISCOVERY]        ← Find available agents
├── [JSON_RPC]               — Standard RPC protocol
├── [TASK]                   — Work unit
├── [TASK_MANAGER]           ← Track execution
├── [SKILL]                  ← Individual capability
├── [SKILL_HANDLER]          ← Execute skill
├── [STREAMING]              ← Stream responses
├── [SSE]                    ← Server-Sent Events
├── [AUTHENTICATION]         ← Agent identity verification
├── [TASK_STATUS]            ← In-progress tracking
├── [TASK_CANCEL]            ← Abort execution
└── [AGENT_TO_AGENT]         ← Direct agent communication
```

**Canonical execution path:**

```
[AGENT]
    ↓
[AGENT_DISCOVERY]           ← Find target agent
    ↓
[[OMNIROUTE_AGENT_CARD]]    ← Get capabilities
    ↓
[A2A_REQUEST]               ← Prepare request
    ↓
[TASK]                      ← Create task
    ↓
[SKILL]                     ← Select capability
    ↓
[ROUTING]                   ← Route to provider
    ↓
[MODEL]                     ← Select model
    ↓
[RESULT]                    ← Return output
```

---

## [TRANSLATOR] — Protocol Compatibility

```
[TRANSLATOR]
│
├── [REQUEST_TRANSLATION]    ← Client format → provider format
├── [RESPONSE_TRANSLATION]   ← Provider format → client format
├── [OPENAI_FORMAT]          ← Translate from OpenAI schema
├── [CLAUDE_FORMAT]          ← Translate from Claude schema
├── [GEMINI_FORMAT]          ← Translate from Gemini schema
├── [PROVIDER_FORMAT]        ← Translate to provider-specific
├── [PLAYGROUND]             ← Test translation
├── [CHAT_TESTER]            ← Interactive testing
├── [TEST_BENCH]             ← Automated testing
└── [LIVE_MONITOR]           ← Real-time monitoring
```

---

## [SECURITY_LAYER] — Protection & Compliance

```
[SECURITY]
│
├── [API_AUTH]               ← API key authentication
├── [API_KEYS]               ← Key generation + rotation
├── [BEARER_AUTH]            ← Bearer token support
├── [MANAGEMENT_AUTH]        ← Admin authentication
├── [SCOPED_TOKENS]          ← Limited-scope tokens
├── [IP_FILTERING]           ← Allow/block IP ranges
├── [PROVIDER_BLOCKING]      ← Block specific providers
├── [SESSION_SECURITY]       ← Session isolation
├── [SECRET_STORAGE]         ← Encrypted credential storage
├── [AUDIT_LOG]              ← Immutable request log
├── [COMPLIANCE]             ← Regulatory requirements
├── [SSRF_PROTECTION]        ← Server-side request forgery prevention
├── [OUTBOUND_URL_GUARD]     ← Safe URL checking
├── [SAFE_FETCH]             ← Secure HTTP fetching
├── [TLS]                    ← HTTPS + encryption
├── [CERTIFICATE_DETECTION]  ← Certificate pinning
└── [PRIVACY]                ← PII protection + redaction
```

---

## [OBSERVABILITY_LAYER] — Visibility & Metrics

```
[OBSERVABILITY]
│
├── [LOGGING]                ← Request/response logging
├── [METRICS]                ← Prometheus-compatible metrics
├── [TRACING]                ← Distributed traces
├── [TELEMETRY]              ← System telemetry
├── [REQUEST_LOG]            ← Every request recorded
├── [ERROR_LOG]              ← Errors + stack traces
├── [AUDIT_LOG]              ← Action audit trail
├── [HEALTH]                 ← System health status
├── [LATENCY]                ← Response time tracking
├── [P50/P95/P99]            ← Percentile latencies
├── [UPTIME]                 ← Availability percentage
├── [MEMORY]                 ← Resource usage
├── [CACHE_STATS]            ← Cache hit rate
├── [PROVIDER_HEALTH]        ← Provider status tracking
├── [MODEL_HEALTH]           ← Model availability
├── [COMBO_HEALTH]           ← Routing combo performance
└── [QUOTA_TELEMETRY]        ← Quota consumption tracking
```

---

## [ANALYTICS_LAYER] — Usage Intelligence

```
[ANALYTICS]
│
├── [REQUEST_COUNT]          ← Total requests
├── [TOKEN_USAGE]            ← Total tokens consumed
├── [INPUT_TOKENS]           ← Prompt tokens
├── [OUTPUT_TOKENS]          ← Completion tokens
├── [COST]                   ← $ spent by provider/model
├── [LATENCY]                ← Response time statistics
├── [PROVIDER_USAGE]         ← Requests per provider
├── [MODEL_USAGE]            ← Requests per model
├── [ACCOUNT_USAGE]          ← Usage per account
├── [COMBO_USAGE]            ← Routing effectiveness
├── [CACHE_HITS]             ← Cache hit percentage
├── [COMPRESSION_SAVINGS]    ← Tokens saved
├── [QUOTA_USAGE]            ← Quota consumption rate
├── [ERROR_RATE]             ← Failure percentage
└── [ACTIVITY_HEATMAP]       ← Usage patterns over time
```

---

## [COST_ENGINE] — Financial Tracking

```
[COST]
│
├── [PROVIDER_COST]          ← Cost per provider
├── [MODEL_COST]             ← Cost per model
├── [ACCOUNT_COST]           ← Cost per account
├── [REQUEST_COST]           ← Cost per request
├── [TOKEN_COST]             ← $/1M tokens
├── [ESTIMATED_COST]         ← Predicted cost
├── [ACTUAL_COST]            ← Invoiced cost
├── [FREE_TIER_VALUE]        ← Value of free quota used
├── [COST_OPTIMIZATION]      ← Recommendations
└── [COST_ANALYTICS]         ← Spending patterns
```

---

## [FREE_TIER_ENGINE] — Zero-Cost Optimization

```
[FREE_TIER_ENGINE]
│
├── [FREE_PROVIDER]          ← No-cost providers
├── [FREE_MODEL]             ← No-cost models
├── [FREE_ACCOUNT]           ← Accounts with free tier
├── [FREE_POOL]              ← Pool of free accounts
├── [POOL_DEDUPLICATION]     ← Avoid double-counting quotas
├── [FREE_CREDITS]           ← Promotional credits
├── [MONTHLY_BUDGET]         ← Budget reset schedule
├── [TOKEN_BUDGET]           ← Token limit per period
├── [RESET]                  ← Reset schedule
├── [TERMS]                  ← Usage restrictions
├── [RISK]                   ← Account ban risk
├── [REGIONAL_REQUIREMENT]   ← Geographic restrictions
├── [SIGNUP_CREDIT]          ← New user bonuses
└── [FREE_TIER_RANKING]      ← Quality ranking
```

---

## [COMPANY_BRAIN_INTEGRATION]

```
[[COMPANY_BRAIN]]
    │
    ├── [[CLAUDE_CODE]]
    ├── [[ANTIGRAVITY]]
    ├── [[CODEX]]
    ├── [[OPENCLAW]]
    │
    └── [[OMNIROUTE]]
         │
         ├── [ROUTING_ENGINE]
         ├── [QUOTA_ENGINE]
         ├── [RESILIENCE_ENGINE]
         ├── [COMPRESSION_ENGINE]
         ├── [MCP_INTERFACE]
         ├── [A2A_INTERFACE]
         ├── [SECURITY_LAYER]
         ├── [OBSERVABILITY_LAYER]
         ├── [ANALYTICS_LAYER]
         └── [COST_ENGINE]
              │
              ↓
         [[PROVIDER_REGISTRY]]
         [[MODEL_REGISTRY]]
         [[ACCOUNT_REGISTRY]]
         [[QUOTA_ENGINE]]
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
         [[NEXT_DECISION]]
```

---

## [OBSIDIAN_VAULT_STRUCTURE]

Your Obsidian vault should represent OmniRoute as:

```
[[OMNIROUTE]]
│
├── [[OMNIROUTE_ARCHITECTURE]]
├── [[OMNIROUTE_PROVIDERS]]
├── [[OMNIROUTE_MODELS]]
├── [[OMNIROUTE_CONNECTIONS]]
├── [[OMNIROUTE_ROUTING]]
├── [[OMNIROUTE_COMBOS]]
├── [[OMNIROUTE_AUTO_COMBO]]
├── [[OMNIROUTE_FALLBACK]]
├── [[OMNIROUTE_RESILIENCE]]
├── [[OMNIROUTE_QUOTA]]
├── [[OMNIROUTE_ACCOUNTS]]
├── [[OMNIROUTE_CONTEXT_RELAY]]
├── [[OMNIROUTE_COMPRESSION]]
├── [[OMNIROUTE_CACHE]]
├── [[OMNIROUTE_MCP]]
├── [[OMNIROUTE_A2A]]
├── [[OMNIROUTE_API]]
├── [[OMNIROUTE_CLI]]
├── [[OMNIROUTE_DASHBOARD]]
├── [[OMNIROUTE_SECURITY]]
├── [[OMNIROUTE_OBSERVABILITY]]
├── [[OMNIROUTE_ANALYTICS]]
├── [[OMNIROUTE_COST]]
├── [[OMNIROUTE_FREE_TIERS]]
├── [[OMNIROUTE_PROXY]]
├── [[OMNIROUTE_TRANSLATOR]]
├── [[OMNIROUTE_MEMORY]]
├── [[OMNIROUTE_SKILLS]]
├── [[OMNIROUTE_EVAL]]
├── [[OMNIROUTE_DEPLOYMENT]]
├── [[OMNIROUTE_DOCKER]]
├── [[OMNIROUTE_TAILSCALE]]
├── [[OMNIROUTE_CLAUDE_CODE]]
├── [[OMNIROUTE_CODEX]]
├── [[OMNIROUTE_ANTIGRAVITY]]
├── [[OMNIROUTE_CONNECTIVITY_TESTS]]
├── [[OMNIROUTE_HEALTH]]
└── [[OMNIROUTE_REALITY]]
```

---

## [BRACKET_VOCABULARY]

```
[OMNIROUTE]
[AI_GATEWAY]
[MODEL_GATEWAY]
[UNIFIED_API]
[PROVIDER]
[MODEL]
[ACCOUNT]
[CONNECTION]
[CREDENTIAL]
[OAUTH]
[API_KEY]
[FREE_TIER]

[ROUTER]
[ROUTING]
[ROUTING_STRATEGY]
[COMBO]
[AUTO_COMBO]
[TARGET]
[FALLBACK]
[FAILOVER]
[FAILURE]
[RETRY]
[BACKOFF]
[CIRCUIT_BREAKER]
[COOLDOWN]
[RESILIENCE]

[QUOTA]
[HEADROOM]
[RESET]
[ACCOUNT_ROTATION]
[STICKY_SESSION]
[CONTEXT_RELAY]

[COMPRESSION]
[RTK]
[CAVEMAN]
[STACKED_COMPRESSION]
[TOKEN_SAVINGS]
[CACHE]
[REASONING_REPLAY]

[FUSION]
[PIPELINE]
[CHAOS]
[PARALLEL_EXECUTION]
[JUDGE]
[SYNTHESIS]

[MCP]
[MCP_TOOL]
[MCP_TRANSPORT]
[MCP_SCOPE]

[A2A]
[AGENT_CARD]
[A2A_TASK]
[A2A_SKILL]
[JSON_RPC]
[AGENT_DISCOVERY]

[TRANSLATOR]
[OPENAI_FORMAT]
[CLAUDE_FORMAT]
[PROVIDER_FORMAT]

[CLI]
[DASHBOARD]
[ELECTRON]
[PWA]
[TERMUX]

[PROXY]
[TUNNEL]
[TAILSCALE]
[CLOUDFLARE]
[NGROK]

[SECURITY]
[AUTH]
[SSRF_GUARD]
[SAFE_FETCH]
[AUDIT]
[POLICY]

[OBSERVABILITY]
[LOGGING]
[TELEMETRY]
[METRICS]
[HEALTH]
[LATENCY]
[UPTIME]

[ANALYTICS]
[COST]
[USAGE]
[QUOTA_TELEMETRY]
[FREE_TIER_ANALYTICS]

[MEMORY]
[SKILL]
[EVALUATION]
[PLAYGROUND]

[BACKUP]
[SYNC]
[CONFIG_BUNDLE]

[DEPLOYMENT]
[DOCKER]
[CONTAINER]
[VOLUME]
[NETWORK]
```

---

## [THE_MOST_IMPORTANT_CONNECTION]

```
[[CLAUDE_CODE]]
    ↓ [OPENAI_COMPATIBLE_REQUEST]
[[OMNIROUTE]]
    ↓ [ROUTING_ENGINE]
[[AUTO_COMBO]]
    ↓ [SCORING_ALGORITHM]
[[PROVIDER_REGISTRY]]
    ↓ [ACCOUNT_POOL]
[[QUOTA_ENGINE]]
    ↓ [ACCOUNT_SELECTION]
[[MODEL_SELECTION]]
    ↓ [PROVIDER_SELECTION]
[[COMPRESSION_ENGINE]]
    ↓ [TOKEN_REDUCTION]
[[UPSTREAM_AI_PROVIDER]]
    ↓ [RESPONSE]
[[OBSERVABILITY_LAYER]]
    ↓ [METRICS_CAPTURE]
[[KNOWLEDGE_GRAPH]]
    ↓ [ROUTING_FEEDBACK]
[[COMPANY_BRAIN]]
    ↓ [NEXT_DECISION]
```

---

**OmniRoute is the AI infrastructure control plane for the Company Brain. Not just a tool, but a system.**

---

**Related:** [[WHOAMI.md]] · [[WHERE_WE_ARE.md]] · [[DATA_FLOW.md]] · [[INFRASTRUCTURE.md]] · [[CROSS_LINK_MASTER_ONTOLOGY.md]] · [[TASK_EXECUTION_MASTER_ONTOLOGY.md]] · [[OBSIDIAN_MASTER_ONTOLOGY.md]]

**AI infrastructure control plane: 68 subsystems, cybernetic feedback, intelligent routing.**
