---
type: intelligence-platform-ontology
canonical: true
authority: intelligence-platform-layer
version: 1.0
updated_at: 2026-10-02T23:30:00Z
source_of_truth: true
core_nodes: 55
---

# CLAUDE_MASTER_ONTOLOGY v1.0 — Multi-Surface Intelligence Platform

**Claude is not just an "API" or "chatbot." It is a complete multi-surface intelligence platform spanning models, interfaces, tools, agents, context management, memory, artifacts, connectors, code execution, research, autonomy, and enterprise governance.**

This ontology models Claude as a **first-class platform node** in the Company Brain's knowledge architecture, occupying the **Intelligence + Execution Layer** alongside OMNIROUTE (routing), MCP (protocol), OBSIDIAN (knowledge capture), NEO4J (relationships), and DOCKER (runtime).

---

## [[CLAUDE_COMPLETE_ARCHITECTURE]] — 55 Core Nodes

```
[[CLAUDE]]
│
├─ [[CLAUDE_IDENTITY]]
│  ├── [[ANTHROPIC]]                    — Creator organization
│  ├── [[CLAUDE_MODELS]]                — Model family versions
│  ├── [[ASSISTANT]]                    — Interactive assistant
│  ├── [[AGENT]]                        — Agentic executor
│  ├── [[REASONING_SYSTEM]]             — Extended thinking capability
│  ├── [[KNOWLEDGE_SYSTEM]]             — Context + memory
│  ├── [[EXECUTION_SYSTEM]]             — Tool use + workflow
│  ├── [[TOOL_USING_SYSTEM]]            — MCP/connector integration
│  ├── [[MULTIMODAL_SYSTEM]]            — Text/image/vision
│  └── [[INTELLIGENCE_PLATFORM]]        — Unified platform
│
├─ [[CLAUDE_MODELS]]
│  ├── [[MODEL_FAMILY]]                 — Claude 3, 5 lineages
│  ├── [[MODEL_VERSION]]                — Opus, Sonnet, Haiku, Fable
│  ├── [[MODEL_RELEASE]]                — Versioning + deprecation
│  ├── [[MODEL_CAPABILITY]]             — Reasoning, code, vision, tool-use
│  ├── [[MODEL_CONTEXT]]                — 200K, 4M token windows
│  ├── [[MODEL_OUTPUT]]                 — Max token generation limits
│  ├── [[MODEL_COST]]                   — Input/output pricing + cache
│  ├── [[MODEL_LATENCY]]                — P50, P95, P99 timing
│  ├── [[MODEL_AVAILABILITY]]           — Regional + quota limits
│  └── [[MODEL_ROUTING]]                — Selection via OmniRoute
│
├─ [[CLAUDE_INTELLIGENCE]]
│  ├── [[PERCEPTION]]                   — Parse input + context
│  ├── [[UNDERSTANDING]]                — Comprehension + analysis
│  ├── [[REASONING]]                    — Logic + inference
│  ├── [[PLANNING]]                     — Goal decomposition
│  ├── [[SYNTHESIS]]                    — Combine + create
│  ├── [[GENERATION]]                   — Text/code/artifact output
│  ├── [[ANALYSIS]]                     — Comparative evaluation
│  ├── [[CLASSIFICATION]]               — Categorization
│  ├── [[EXTRACTION]]                   — Data + entity discovery
│  ├── [[TRANSFORMATION]]               — Convert format/representation
│  ├── [[VERIFICATION]]                 — Fact-checking + validation
│  └── [[ITERATION]]                    — Refinement + feedback loops
│
├─ [[EXTENDED_THINKING]]
│  ├── [[THINKING_MODE]]                — Enable extended reasoning
│  ├── [[REASONING_BUDGET]]             — Token allocation to thinking
│  ├── [[COMPLEX_REASONING]]            — Multi-step problem decomposition
│  ├── [[PROBLEM_DECOMPOSITION]]        — Break into subproblems
│  ├── [[TOOL_REASONING]]               — Plan tool sequences
│  └── [[REASONING_OUTPUT]]             — Expose thinking chain
│
├─ [[CLAUDE_CONTEXT]]
│  ├── [[SYSTEM_PROMPT]]                — Company Brain instructions (CLAUDE.md)
│  ├── [[USER_PROMPT]]                  — Current request
│  ├── [[CONVERSATION]]                 — Chat history
│  ├── [[PROJECT_CONTEXT]]              — Project knowledge base
│  ├── [[TOOL_CONTEXT]]                 — MCP tool descriptions
│  ├── [[FILE_CONTEXT]]                 — Uploaded/referenced files
│  ├── [[CODEBASE_CONTEXT]]             — Repository intelligence
│  ├── [[WEB_CONTEXT]]                  — Search results + web research
│  ├── [[AGENT_CONTEXT]]                — Subagent state + results
│  ├── [[MEMORY_CONTEXT]]               — Persistent user memory
│  └── [[SESSION_CONTEXT]]              — Conversation session state
│
├─ [[CONTEXT_ENGINEERING]]
│  ├── [[CONTEXT_SELECTION]]            — Curate relevant context
│  ├── [[CONTEXT_RETRIEVAL]]            — Fetch from registries/graph
│  ├── [[CONTEXT_RANKING]]              — Prioritize by relevance
│  ├── [[CONTEXT_COMPRESSION]]          — Reduce token footprint
│  ├── [[CONTEXT_INJECTION]]            — Weave into prompt
│  ├── [[CONTEXT_WINDOW]]               — Manage token budget
│  ├── [[CONTEXT_PERSISTENCE]]          — Store across sessions
│  └── [[CONTEXT_HANDOFF]]              — Pass to subagents
│
├─ [[CLAUDE_MEMORY]]
│  ├── [[MEMORY]]                       — Persistent user memory store
│  ├── [[MEMORY_WRITE]]                 — Record observations
│  ├── [[MEMORY_SEARCH]]                — Retrieve stored facts
│  ├── [[MEMORY_RETRIEVAL]]             — Context recall
│  ├── [[MEMORY_SCOPE]]                 — User/project/session levels
│  ├── [[MEMORY_RETENTION]]             — TTL + deletion policy
│  ├── [[USER_MEMORY]]                  — Cross-session user facts
│  ├── [[PROJECT_MEMORY]]               — Project-scoped knowledge
│  └── [[SESSION_MEMORY]]               — Conversation-scoped state
│
├─ [[PROJECTS]]
│  ├── [[PROJECT]]                      — Named workspace
│  ├── [[PROJECT_OWNER]]                — Access control
│  ├── [[PROJECT_MEMBERS]]              — Collaboration
│  ├── [[PROJECT_INSTRUCTIONS]]         — Custom system prompt
│  ├── [[PROJECT_KNOWLEDGE]]            — Uploaded files + context
│  ├── [[PROJECT_FILES]]                — Scoped file access
│  ├── [[PROJECT_CHATS]]                — Conversation history
│  ├── [[PROJECT_MEMORY]]               — Project-specific memory
│  ├── [[PROJECT_CONNECTORS]]           — Integrated services
│  └── [[PROJECT_PERMISSIONS]]          — Role-based access
│
├─ [[CLAUDE_ARTIFACTS]]
│  ├── [[ARTIFACT]]                     — Standalone output
│  ├── [[DOCUMENT]]                     — Living document
│  ├── [[CODE]]                         — Executable code
│  ├── [[WEBSITE]]                      — HTML/CSS/JS site
│  ├── [[DASHBOARD]]                    — Interactive dashboard
│  ├── [[DIAGRAM]]                      — Visual structure
│  ├── [[DESIGN]]                       — Figma-style design
│  ├── [[SLIDE_DECK]]                   — Presentation deck
│  ├── [[INTERACTIVE_TOOL]]             — Custom web app
│  ├── [[ARTIFACT_EDIT]]                — In-place editing
│  ├── [[ARTIFACT_SHARE]]               — Collaboration links
│  ├── [[ARTIFACT_EXPORT]]              — Download formats
│  └── [[ARTIFACT_RUNTIME]]             — Live execution context
│
├─ [[CLAUDE_CODE]]
│  ├── [[CLI]]                          — claude command-line tool
│  ├── [[TERMINAL]]                     — Terminal session integration
│  ├── [[CODEBASE]]                     — Repository context awareness
│  ├── [[SHELL]]                        — Bash/zsh command execution
│  ├── [[GIT]]                          — Version control + branches
│  ├── [[FILE_SYSTEM]]                  — Read/write/edit files
│  ├── [[BUILD_SYSTEM]]                 — Compile + test execution
│  ├── [[DEBUG]]                        — Debugging workflows
│  ├── [[REFACTOR]]                     — Code transformation
│  ├── [[REPOSITORY_INTELLIGENCE]]      — Code navigation + analysis
│  ├── [[MCP]]                          — MCP server/tool integration
│  ├── [[SKILLS]]                       — Claude Code skills
│  ├── [[PLUGINS]]                      — Plugin ecosystem
│  ├── [[SUBAGENTS]]                    — Delegated agents
│  ├── [[HOOKS]]                        — Automation event triggers
│  ├── [[PERMISSIONS]]                  — Sandbox + access control
│  ├── [[CLAUDE_MD]]                    — Repository instructions file
│  └── [[SESSION]]                      — Session state management
│
├─ [[COWORK]]
│  ├── [[AGENTIC_TASK]]                 — Long-running autonomous task
│  ├── [[TASK_PLANNING]]                — Decompose + estimate
│  ├── [[TASK_EXECUTION]]               — Execute steps autonomously
│  ├── [[TASK_REVIEW]]                  — Human review + approval
│  ├── [[TASK_RESUME]]                  — Continue after interruption
│  ├── [[LOCAL_FILES]]                  — Local file system access
│  ├── [[BROWSER]]                      — Web browsing + interaction
│  ├── [[COMPUTER_USE]]                 — Desktop automation
│  ├── [[CONNECTORS]]                   — Service integrations
│  ├── [[SCHEDULED_TASKS]]              — Cloud-scheduled execution
│  └── [[CLOUD_EXECUTION]]              — Run without keeping device awake
│
├─ [[CLAUDE_SURFACES]]
│  ├── [[CLAUDE_WEB]]                   — claude.ai web interface
│  ├── [[CLAUDE_DESKTOP]]               — macOS/Windows/Linux desktop app
│  ├── [[CLAUDE_MOBILE]]                — iOS/Android mobile apps
│  ├── [[CLAUDE_CODE]]                  — Code IDE integration
│  ├── [[CLAUDE_COWORK]]                — Knowledge work interface
│  ├── [[CLAUDE_API]]                   — Programmatic API
│  └── [[CLAUDE_ARTIFACTS]]             — Published artifact pages
│
├─ [[CONNECTORS_AND_INTEGRATIONS]]
│  ├── [[CONNECTORS]]                   — External service integrations
│  ├── [[REMOTE_CONNECTORS]]            — Cloud-hosted integrations
│  ├── [[LOCAL_CONNECTORS]]             — Desktop connectors
│  ├── [[MCP_CONNECTOR]]                — Model Context Protocol bridge
│  ├── [[INTERACTIVE_CONNECTORS]]       — Live UI in chat
│  ├── [[TOOL_DISCOVERY]]               — Auto-detect available tools
│  ├── [[TOOL_ACCESS]]                  — Execute with permissions
│  ├── [[CONNECTOR_LIFECYCLE]]          — Install/enable/disable
│  └── [[CONNECTOR_PERMISSIONS]]        — OAuth + API key auth
│
├─ [[MCP]]
│  ├── [[MODEL_CONTEXT_PROTOCOL]]       — Tool + resource protocol
│  ├── [[MCP_SERVER]]                   — Local/remote MCP servers
│  ├── [[MCP_TOOL]]                     — Exposed tool definitions
│  ├── [[MCP_RESOURCE]]                 — Accessible resources
│  ├── [[MCP_PROMPT]]                   — Template prompts
│  ├── [[TOOL_DISCOVERY]]               — List available tools
│  ├── [[TOOL_EXECUTION]]               — Invoke with args
│  ├── [[TOOL_RESULT]]                  — Parse + integrate output
│  ├── [[MCP_PERMISSIONS]]              — Tool access control
│  └── [[MCP_GOVERNANCE]]               — Security + rate limits
│
├─ [[SKILLS_AND_PLUGINS]]
│  ├── [[SKILL]]                        — Reusable procedure
│  ├── [[SKILL_INSTRUCTIONS]]           — Task definition
│  ├── [[SKILL_TOOLS]]                  — Integrated tools
│  ├── [[SKILL_REGISTRY]]               — Central skill catalog
│  ├── [[SKILL_DISCOVERY]]              — Find + list skills
│  ├── [[SKILL_INSTALL]]                — Enable skill
│  ├── [[PLUGIN]]                       — Extensible module
│  ├── [[PLUGIN_MARKETPLACE]]           — Plugin directory
│  ├── [[PLUGIN_PERMISSIONS]]           — Scope-based access
│  └── [[PLUGIN_LIFECYCLE]]             — Install/update/remove
│
├─ [[CAPABILITIES]]
│  ├── [[VISION]]                       — Image understanding
│  ├── [[PDF_VISION]]                   — Document understanding
│  ├── [[CODE_UNDERSTANDING]]           — Programming language knowledge
│  ├── [[MULTIMODAL]]                   — Text + image synthesis
│  ├── [[STRUCTURED_OUTPUT]]            — JSON/XML generation
│  ├── [[WEB_SEARCH]]                   — Live internet search
│  ├── [[RESEARCH]]                     — Deep investigation mode
│  ├── [[BROWSER_CONTROL]]              — Automated web interaction
│  ├── [[COMPUTER_VISION]]              — Screen reading + automation
│  ├── [[FILE_HANDLING]]                — Upload/download/parse files
│  ├── [[PROMPT_CACHING]]               — Reuse cached context
│  └── [[VOICE_INPUT_OUTPUT]]           — Audio interaction
│
├─ [[AUTONOMY_LEVELS]]
│  ├── [[L0]]                           — Respond only (no action)
│  ├── [[L1]]                           — Assist (read/suggest/plan)
│  ├── [[L2]]                           — Execute (tool-use + verify)
│  ├── [[L3]]                           — Autonomous (multi-step + recovery)
│  ├── [[HUMAN_APPROVAL_GATE]]          — Require confirmation
│  ├── [[ESCALATION]]                   — Defer to human
│  └── [[AUTONOMY_VERIFICATION]]        — Laya ML confidence scoring
│
├─ [[SECURITY_AND_GOVERNANCE]]
│  ├── [[AUTHENTICATION]]               — API keys + OAuth
│  ├── [[AUTHORIZATION]]                — Permission scope enforcement
│  ├── [[PERMISSIONS]]                  — Tool/file/network access control
│  ├── [[AUDIT_LOG]]                    — Immutable request audit trail
│  ├── [[DATA_PROTECTION]]              — Encryption at rest + transit
│  ├── [[COMPLIANCE]]                   — Regulatory requirement gates
│  ├── [[GUARDRAILS]]                   — Safety + alignment boundaries
│  ├── [[SECRET_REDACTION]]             — Sanitize sensitive data
│  └── [[HUMAN_IN_THE_LOOP]]            — Approval workflows
│
├─ [[OBSERVABILITY_AND_ANALYTICS]]
│  ├── [[SESSION_LOG]]                  — Conversation audit trail
│  ├── [[MESSAGE_LOG]]                  — All messages logged
│  ├── [[TOOL_LOG]]                     — Tool invocation + results
│  ├── [[ERROR_LOG]]                    — Errors + failures
│  ├── [[AUDIT_LOG]]                    — Security + compliance events
│  ├── [[TOKEN_USAGE]]                  — Input/output/cache tokens
│  ├── [[LATENCY_TRACKING]]             — Response time metrics
│  ├── [[COST_TRACKING]]                — Token cost per request
│  ├── [[SUCCESS_METRICS]]              — Task completion rate
│  └── [[TELEMETRY]]                    — System health signals
│
├─ [[CLAUDE_API]]
│  ├── [[MESSAGES_API]]                 — Chat completion endpoint
│  ├── [[BATCH_API]]                    — Async batch jobs
│  ├── [[FILES_API]]                    — File upload/download
│  ├── [[MODELS_API]]                   — List available models
│  ├── [[TOKEN_COUNTING]]               — Pre-calculate token cost
│  ├── [[PROMPT_CACHING]]               — Cache control headers
│  ├── [[STREAMING]]                    — Server-sent events
│  ├── [[TOOLS]]                        — Tool use definitions
│  ├── [[VISION]]                       — Image + document input
│  ├── [[STRUCTURED_OUTPUT]]            — JSON schema generation
│  ├── [[WEB_SEARCH]]                   — Search integration
│  ├── [[COMPUTER_USE]]                 — Browser + OS control
│  └── [[ADMIN_API]]                    — Organization management
│
├─ [[COST_OPTIMIZATION]]
│  ├── [[MODEL_ROUTING]]                — Select cheapest capable model
│  ├── [[PROMPT_CACHING]]               — Reuse cached context
│  ├── [[CONTEXT_COMPRESSION]]          — Reduce input tokens
│  ├── [[BATCH_PROCESSING]]             — Off-peak cost reduction
│  ├── [[TASK_DELEGATION]]              — Delegate to smaller models
│  └── [[BUDGET_ENFORCEMENT]]           — Hard spend limits
│
├─ [[CLAUDE_EXECUTION_LOOP]]
│  ├── [[INTENT]]                       — User objective
│  ├── [[CONTEXT_ASSEMBLY]]             — Gather relevant knowledge
│  ├── [[PLANNING]]                     — Decompose into steps
│  ├── [[TOOL_SELECTION]]               — Choose appropriate tools
│  ├── [[EXECUTION]]                    — Invoke tools/APIs
│  ├── [[OBSERVATION]]                  — Parse + analyze results
│  ├── [[VALIDATION]]                   — Verify correctness
│  ├── [[STATE_UPDATE]]                 — Record progress
│  ├── [[ITERATION]]                    — Refine + retry
│  ├── [[HANDOFF]]                      — Delegate or escalate
│  └── [[COMPLETION]]                   — Deliver output
│
├─ [[CLAUDE_REALITY_LAYER]]
│  ├── [[CLAIM]]                        — Statement + assertion
│  ├── [[EVIDENCE]]                     — Supporting facts + sources
│  ├── [[OBSERVATION]]                  — Direct verification
│  ├── [[TEST]]                         — Experimental validation
│  ├── [[VERIFICATION]]                 — Proof of correctness
│  ├── [[CONFIDENCE]]                   — Certainty level (0.0-1.0)
│  ├── [[UNCERTAINTY]]                  — Known unknowns
│  ├── [[ASSUMPTION]]                   — Unverified premise
│  ├── [[INFERENCE]]                    — Logical deduction
│  └── [[DRIFT]]                        — Discrepancy from source-of-truth
│
└─ [[CLAUDE_COMPANY_BRAIN_INTEGRATION]]
   ├── [[CLAUDE]]                       — Intelligence + execution
   ├── [[OMNIROUTE]]                    — Model routing + resilience
   ├── [[MCP]]                          — Tool protocol
   ├── [[OBSIDIAN]]                     — Knowledge capture
   ├── [[NEO4J]]                        — Relationship graph
   ├── [[QDRANT]]                       — Vector retrieval
   ├── [[DOCKER]]                       — Runtime infrastructure
   ├── [[TAILSCALE]]                    — Network fabric
   ├── [[GITHUB]]                       — Repository intelligence
   ├── [[ANTIGRAVITY]]                  — Agent orchestration
   └── [[REALITY]]                      — Source-of-truth verification
```

---

## Integration Pattern

```
                    ┌──────────────────────┐
                    │    [[COMPANY_BRAIN]] │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              ↓                ↓                ↓
       [[KNOWLEDGE]]     [[ORCHESTRATION]]   [[REALITY]]
              │                │                │
          [[OBSIDIAN]]      [[CLAUDE]]       [[EVIDENCE]]
              │                │                │
          [[NEO4J]]      [[CLAUDE_CODE]]  [[VERIFICATION]]
          [[QDRANT]]       [[COWORK]]
                              │
                             [[MCP]]
                              │
                         [[OMNIROUTE]]
                              │
                  ┌───────────┼───────────┐
                  ↓           ↓           ↓
             [[MODELS]]  [[PROVIDERS]] [[ROUTING]]
                              │
                         [[EXECUTION]]
                              │
                         [[TASK]]
                              ↓
                         [[ACTION]]
                              ↓
                         [[OUTCOME]]
                              ↓
                         [[EVIDENCE]]
                              ↓
                         [[LEARNING]]
                              ↺
```

---

## Key Architectural Distinctions

| Component | Role | Note |
|-----------|------|------|
| **[[CLAUDE]]** | Intelligence + Reasoning | The cognitive system |
| **[[OMNIROUTE]]** | Model Selection + Routing | The connection fabric |
| **[[MCP]]** | Tool + Context Protocol | The integration standard |
| **[[OBSIDIAN]]** | Knowledge Capture | Human-readable semantic layer |
| **[[NEO4J]]** | Relationship Graph | Machine-readable knowledge structure |
| **[[QDRANT]]** | Vector Retrieval | Semantic + embedding search |
| **[[DOCKER]]** | Runtime Container | Execution environment |
| **[[COMPANY_BRAIN]]** | Orchestration | Master control plane |

**Critical:** [[CLAUDE]] should NOT be treated as the ultimate source of truth. It is an **intelligence tool**. Verify all claims against [[REALITY]].

---

## Bracket Vocabulary (Wiki-Link Aliases)

See `NAVIGATION_ALIASES.yaml` for complete cross-reference and bracket notation definitions.

**Common references:**
- `[[CLAUDE]]` — Master Claude platform
- `[[CLAUDE_CODE]]` — Claude Code CLI/IDE integration
- `[[CLAUDE_MODELS]]` — Model family + versions
- `[[CLAUDE_API]]` — Programmatic API
- `[[CLAUDE_COWORK]]` — Knowledge-work agentic interface
- `[[CLAUDE_CONTEXT]]` — Context management
- `[[CLAUDE_MEMORY]]` — Persistent memory
- `[[CLAUDE_PROJECTS]]` — Workspace + collaboration
- `[[CLAUDE_ARTIFACTS]]` — Generated/published outputs
- `[[CLAUDE_AUTONOMY]]` — L0-L3 autonomous execution
- `[[CLAUDE_REALITY]]` — Truth verification layer
- `[[CLAUDE_EXECUTION_LOOP]]` — Task decomposition + execution
- `[[OMNIROUTE]]` — Model routing + resilience layer
- `[[MCP]]` — Model Context Protocol
- `[[OBSIDIAN]]` — Knowledge graph capture
- `[[NEO4J]]` — Relationship database
- `[[COMPANY_BRAIN]]` — Master orchestration

---

**Version:** 1.0  
**Updated:** 2026-10-02  
**Authority:** Intelligence Platform Layer  
**Status:** Canonical ✅



---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
