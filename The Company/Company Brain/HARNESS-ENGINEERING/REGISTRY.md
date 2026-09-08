# Agent Harness Engineering Registry

**Version:** 1.0  
**Generated:** 2026-09-08  
**Domain:** Agent Infrastructure  
**Authority:** ai-boost/awesome-harness-engineering + Anthropic/OpenAI/Microsoft canonical sources  
**Status:** Foundation template | Full registry incoming

---

## Sources

| ID | Name | Owner | Stars | Priority | Coverage |
|----|------|-------|-------|----------|----------|
| **harness-1** | Awesome Harness Engineering | ai-boost | 4200 | primary | Context delivery, tool design, permissions, verification, observability, safety, debugging |
| **harness-2** | RUCAIBox Agent Harness Survey | RUCAIBox | 2100 | primary | Academic: agent workflows, memory systems, skills, orchestration (500+ refs) |
| **harness-3** | lopopolo/harness-engineering | lopopolo | 1800 | secondary | Organizational synthesis: AGENTS.md, CLAUDE.md, playbooks, evals, domain modeling |

---

## Design Primitives (Harness Architecture)

```yaml
Agent Harness Layers:

1. Context Delivery & Compaction
   - What agent knows (evidence ledger, curation)
   - Token budgets (context limits per agent)
   - Freshness & coherence across sessions

2. Agent Loop Architecture
   - Plan → Act → Verify cycles
   - Checkpoint & resume mechanics
   - Long-horizon task decomposition

3. Tool Interface Design
   - Schema design (input/output enforcement)
   - Error surfaces (rich diagnostics)
   - MCP tool registration & composition

4. Skills & Capabilities Registry
   - Composable procedures
   - Skill → tool routing
   - Capability discovery

5. Permissions & Authorization
   - Structured permission systems (not natural language)
   - Resource access gating (who calls what)
   - Risk-based tool filtering
   - Approval workflows

6. Memory & State Management
   - Cross-session persistence
   - Evidence ledger (audit trail)
   - Transactional guarantees

7. Task Orchestration
   - Multi-agent coordination
   - Subagent topology (manager vs. decentralized)
   - Handoff contracts & dependencies

8. Verification & Evals
   - Eval harnesses (behavioral, not unit tests)
   - Regression detection
   - Quality gates before production

9. Observability & Tracing
   - Execution tracing (Langfuse model)
   - Decision tracking & audit
   - Error classification for learning
   - Telemetry for debugging

10. Safety & Guardrails (Defense-in-Depth)
    - Input validation
    - Output filtering
    - Resource limits (CPU, memory, API calls)
    - Kill switches (max daily loss, position size, etc.)
    - Approval gates for high-risk operations

11. Debugging & Developer Experience
    - Agent reasoning visibility
    - Tool call inspection
    - Context replay & step-through

12. Human-in-the-Loop Collaboration
    - Approval gates for critical decisions
    - Override mechanisms
    - Feedback integration
```

---

## Canonical Foundations (Organizational Essays)

| Source | Title | Key Insight | Year |
|--------|-------|------------|------|
| **OpenAI** | Harness Engineering | Model + Harness = Agent; harness is the lever | 2023 |
| **Anthropic** | Building Effective Agents | When to use workflows vs agents; compose primitives | 2024 |
| **Anthropic** | Harness Design for Long-Running Apps | Assumptions expire as models improve | 2024 |
| **Anthropic** | Writing Effective Tools for Agents | Tool design is agent UX | 2024 |
| **Anthropic** | Beyond Permission Prompts | Structured permissions beat natural language | 2024 |
| **Anthropic** | Demystifying Evals for AI Agents | Unit tests fail for agents; need behavioral evals | 2024 |
| **Google** | Agent Development Kit | Multi-agent topology + tool registration | 2024 |
| **Martin Fowler** | Harness Engineering | Three systems: context, constraints, entropy mgmt | 2024 |
| **LangChain** | Anatomy of an Agent Harness | Five primitives: filesystem, execution, sandbox, memory, context | 2024 |
| **Microsoft** | Azure SRE Agent Harness | 35K incidents, 40.5h→3m TTM, filesystem-based context | 2026 |
| **Anthropic** | Claude Code Quality Postmortem | Harness changes (prompt, cache, defaults) caused regression | 2026 |

---

## Critical for Company Brain

Your system needs all 12 harness layers:

| Layer | Why Critical | Implementation Status |
|-------|---|---|
| **Context Delivery** | Agents can't reason without rich context | 🟡 Partial (Neo4j has data, not yet exposed to agents) |
| **Tool Interface Design** | Wrong schema = unreliable execution | 🟡 MCP tools exist, schema audit needed |
| **Permissions & Authorization** | "Please don't trade capital" fails; schema wins | 🔴 Missing (critical for L2/L3) |
| **Verification & Evals** | Before agents deploy, tests must pass | 🔴 Missing (eval harnesses not built) |
| **Safety & Guardrails** | Kill switches prevent catastrophic failures | 🔴 Missing (critical for capital operations) |
| **Observability & Tracing** | No audit trail = no learning | 🟡 Langfuse exists, not wired to agents |
| **Human-in-the-Loop** | Approval gates for high-risk decisions | 🟡 Buzz exists, not integrated to agent flow |

---

## Scoring Model (Harness-Specific)

Harness engineering tools scored on 12 dimensions:

```yaml
dimensions:
  - completeness: coverage of all 12 layers
  - maturity: production-ready vs. experimental
  - integration_readiness: plugs into Neo4j/Qdrant/MCP
  - documentation: how clear is the pattern
  - production_evidence: case studies (Azure SRE, etc.)
  - adoption: stars, contributors, activity
  - active_maintenance: commits per month
  - learning_curve: easy to grok vs. steep
  - composability: plays with other tools
  - cost: licensing, infrastructure overhead
  - observability_score: how much insight it gives
  - reliability_score: proven in production

composite_formula: "weighted_avg(completeness×0.20 + production_evidence×0.20 + maturity×0.15 + integration_readiness×0.15 + adoption×0.10 + documentation×0.10 + learning_curve×0.10)"
```

---

## Sample High-Confidence Frameworks

### Canonical Pattern: Microsoft Azure SRE Agent

**What worked:** Filesystem-based context (code + runbooks + schemas as files) + generic tools (read_file, grep, shell)

**What didn't:** 100+ bespoke tools per task, natural-language permissions, silent failures

**Result:** 35,000+ incidents handled autonomously, 40.5h → 3m TTM, <1% escalation

**Lesson:** Better harness > better model. Harness-only changes moved evals 20+ positions.

---

## Integration with Company Brain

```
AGENT HARNESS ENGINEERING
    ↓
Supplies: Context delivery, tool design, permissions, verification
    ↓
Feeds: CP-006 (Agent Control Plane)
    ↓
Enables: L2/L3 autonomous operations (16 routing + 26 sub-agents)
    ↓
Secures: Capital deployment (trading, venture funding)
    ↓
Produces: Observable, auditable, reversible agent decisions
```

---

## Implementation Roadmap

| Phase | Timeline | Deliverable |
|-------|----------|---|
| **Phase 1** | Week 1-2 | Context delivery layer (evidence ledger, curator) |
| **Phase 2** | Week 2-3 | Tool interface audit + schema enforcement |
| **Phase 3** | Week 3-4 | Permissions & authorization (structured gates) |
| **Phase 4** | Week 4-5 | Verification & eval harnesses |
| **Phase 5** | Week 5-6 | Safety guardrails + kill switches |
| **Phase 6** | Week 6-7 | Observability wiring (Langfuse → agents) |
| **Phase 7** | Week 7-8 | Human-in-the-loop approval workflows |

---

## Status

- ✅ Foundational research complete (3 authoritative sources)
- ✅ 12-layer architecture defined
- 🟡 Registry template created (this file)
- 🔴 Full framework tools mapping pending (60+ tools to classify)
- 🔴 Neo4j integration pending

**Next:** Populate framework/tool registry using ai-boost/awesome-harness-engineering categories.

---

**Authority:** Domain 11.5 (Agent Harness Engineering) — Part of 18-domain Company Brain taxonomy  
**Control Plane:** CP-006 (Agent Control Plane), CP-027 (Infrastructure Control Plane)  
**Related:** [[INTEGRATED-SYSTEM-ARCHITECTURE]], [[TRADING-OS]], [[Agent OS]]
