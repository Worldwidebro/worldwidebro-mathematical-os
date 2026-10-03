---
type: capability-registry
canonical: false
authority: intelligence-platform-layer
version: 1.0
updated_at: 2026-10-02T23:35:00Z
relates_to: CLAUDE_MASTER_ONTOLOGY
---

# CLAUDE_CAPABILITIES — Core Platform Capabilities

**Last updated:** 2026-10-02  
**Status:** Operative  
**Source:** [[CLAUDE_MASTER_ONTOLOGY]]

---

## Foundation Capabilities

### [[VISION]]
- Image understanding + analysis
- Multi-image comparison
- PDF + document processing
- Screenshot interpretation
- Visual reasoning

### [[CODE]]
- 50+ programming languages
- Code generation + explanation
- Debugging + optimization
- Architecture analysis
- Test generation

### [[REASONING]]
- Logic chains
- Multi-step decomposition
- Constraint satisfaction
- Comparative analysis
- Extended thinking (with thinking token budget)

### [[TOOL_USE]]
- MCP tool integration
- Shell command execution
- File operations (read/write/navigate)
- API integration
- Multi-tool orchestration

### [[STRUCTURED_OUTPUT]]
- JSON schema generation
- Deterministic response format
- Validated data extraction
- Type-safe generation

---

## Platform-Specific Capabilities

### [[CLAUDE_CODE]]
- **Repository intelligence:** Navigate codebases, understand dependencies
- **Shell execution:** Run bash/zsh commands
- **Git integration:** Commit, branch, PR workflows
- **File editing:** Read/edit/create files with precise diffs
- **Build systems:** Invoke compilers, test runners
- **MCP tools:** Full access to local + remote tools
- **Subagents:** Delegate to specialist agents
- **Hooks:** Automation via shell scripts
- **Permissions:** Sandbox enforcement

### [[CLAUDE_COWORK]]
- **Agentic tasks:** Long-running autonomous workflows
- **Task planning:** Decompose goals into steps
- **Task execution:** Execute with verification
- **Local files:** Desktop file system access
- **Browser:** Automated web interaction
- **Computer use:** Screen + keyboard automation
- **Scheduled tasks:** Cloud-based task scheduling
- **Cloud execution:** Run without device awake

### [[CLAUDE_WEB]]
- Chat interface
- Project management
- File upload/download
- Artifact publishing
- Memory management
- Search capabilities

### [[CLAUDE_API]]
- **Messages API:** Chat completion
- **Batch API:** Async processing
- **Files API:** Attachment handling
- **Vision:** Image input
- **Structured output:** JSON schema
- **Tool use:** MCP + custom tools
- **Streaming:** Real-time response
- **Token counting:** Pre-calculate costs

---

## Integration Capabilities

### [[CONNECTORS]]
- 100+ service integrations
- OAuth authentication
- API key management
- Interactive connector UIs
- Real-time data sync

### [[MCP]]
- Model Context Protocol
- Tool discovery + execution
- Resource access
- Prompt templates
- Full governance + permissions

### [[ARTIFACTS]]
- Generate + edit live documents
- Code + design artifacts
- Interactive tools
- Sharing + collaboration
- Export (DOCX, PDF, PPTX)

### [[MEMORY]]
- Persistent user memory
- Cross-session recall
- Searchable knowledge base
- Memory scope (user/project/session)

### [[PROJECTS]]
- Workspace organization
- Custom instructions
- Knowledge base upload
- Collaboration + sharing
- File access scoping

---

## Advanced Capabilities

### [[EXTENDED_THINKING]]
- Allocate tokens to reasoning
- Multi-step problem decomposition
- Expose thinking chains
- Cost visible in token usage

### [[RESEARCH_MODE]]
- Deep multi-source investigation
- Citation + evidence collection
- Cross-check + contradiction detection
- Structured research reports

### [[WEB_SEARCH]]
- Live internet search
- Recency + freshness
- Citation generation
- Search refinement

### [[PROMPT_CACHING]]
- Reuse cached context
- Reduced token cost
- Cache-affinity routing (via [[OMNIROUTE]])
- TTL management

---

## Model-Specific Capabilities

| Model | Context | Reasoning | Cost | Best For |
|-------|---------|-----------|------|----------|
| **Claude 5 Opus** | 200K | Excellent | High | Complex reasoning + code |
| **Claude 5 Sonnet** | 200K | Good | Medium | Balanced + general-purpose |
| **Claude 5 Haiku** | 200K | Good | Low | Speed + cost |
| **Claude Fable** | 8K | Good | Very low | Classification + fast inference |

---

## Security + Compliance

### [[PERMISSIONS]]
- Tool-level access control
- File path whitelisting
- Network + API restrictions
- MCP tool scoping

### [[AUDIT_LOG]]
- All interactions logged
- Immutable records
- Searchable history
- Compliance retention

### [[GUARDRAILS]]
- Safety alignment
- Jailbreak resistance
- Regulatory compliance
- Custom policy gates

---

## Limitations

- **No persistent learning:** Changes to Claude's weights don't persist
- **No autonomy without MCP:** Needs tools for external action
- **Rate limits:** Model quota + concurrency constraints
- **Token budgets:** Context window + output limits
- **No real-time data:** Search via web search; graph queries via MCP

---

## How to Check Current Capabilities

```bash
# Via Claude API
curl https://api.anthropic.com/v1/models \
  -H "Authorization: Bearer $ANTHROPIC_API_KEY"

# Via OmniRoute (Company Brain)
curl http://100.87.214.70:3004/api/models
```

---

**Canonical source:** [[CLAUDE_MASTER_ONTOLOGY]]



---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
