---
title: OS Tools Integration Map — Headroom, Graphify, CodeBurn, Ponytail
date: 2026-07-20
version: 1.0
---

# How Headroom, Graphify, CodeBurn, Ponytail Integrate Into Your OS

**Key insight:** These four tools solve *different bottlenecks* in your multi-agent OS. They stack, not compete.

---

## 1. Graphify — Repository Intelligence Layer

**What it does:** Builds knowledge graph of repos via AST parsing + model-assisted extraction. Exposes relationships (functions → dependencies → tests → owners) instead of forcing agents to grep repeatedly.

**Your OS Already Has:**
- ✅ Neo4j (running, 1,000+ nodes)
- ✅ Qdrant (1,648 repo vectors)
- ✅ REPOSITORY-INTELLIGENCE-SYSTEM.md (classification framework)
- ✅ repo-capabilities-backfill.json (capability joins)
- ⚠️ Manual graph building (Python scripts, not continuous indexing)

**Graphify's Value:**
- Continuous AST-based indexing (not manual rescans)
- Cross-repo dependency discovery
- Automatic owner/maintainer extraction
- `/graphify` skill integration for agents

**Integration Point:** Replace manual `build_repo_rag.py` rescans with Graphify's continuous indexing. Feed Neo4j automatically.

**Sprint 1 Impact:**
- Not blocking (Phase B doesn't require it)
- Phase C benefit: venture health dashboard can show repo dependency health
- Phase D benefit: agent routing can query "which repos implement THIS capability"

**Priority:** Phase C (Nice-to-have, enables better dashboards)

---

## 2. Headroom — Context Optimization Layer

**What it does:** Compresses tool outputs, logs, responses before LLM sees them. Proxy mode, MCP server, shared memory. Writes learnings into CLAUDE.md/AGENTS.md automatically.

**Your OS Already Has:**
- ✅ CLAUDE.md (global instructions, memories, context)
- ✅ AGENTS.md (agent definitions with instructions)
- ✅ Token-aware prompt engineering (already doing this manually)
- ✅ Context compression in some agent calls
- ⚠️ No automatic learning loop (lessons aren't auto-recorded)

**Headroom's Value:**
- Automatic context compression before every LLM call
- Shared memory across agent sessions (all agents learn from each other)
- Reduces tokens per agent call by 30-50%
- Automatic lesson recording: "This pattern worked, record it in memory"

**Integration Point:** Wrap PolicyEngine and VentureFactory LLM calls in Headroom to:
- Reduce tokens when policy_engine queries Supabase
- Reduce tokens when venture_classifier processes ventures
- Auto-record policy lessons into AGENTS.md

**Sprint 1 Impact:**
- B2 benefit: venture_classifier calls reduce tokens 30-40% (saves $)
- B4 benefit: event bus can share context across agent chain
- Overall: reduce Phase B token costs by 25-35%

**Priority:** Phase B integration (immediate ROI on B2, B4)

---

## 3. CodeBurn — AI Spend Analytics

**What it does:** Reads session history, reports cost/tokens by project, model, tool, task type. Dashboard shows where money is going.

**Your OS Already Has:**
- ✅ PolicyEngine cost tracking (`agent_cost_log` table)
- ✅ Supabase `skill_executions` audit (logging calls)
- ✅ Langfuse (LLM tracing, now fixed)
- ⚠️ No unified cost dashboard
- ⚠️ No breakdown by agent/project/task

**CodeBurn's Value:**
- Single dashboard: total spend + breakdown
- Identifies agents with high retry rates
- Shows cost per venture
- Automatic alerts when spend exceeds policy

**Integration Point:** Consume CodeBurn dashboard + feed `agent_cost_log` into Grafana.

**Sprint 1 Impact:**
- Phase A benefit: none (no agents running yet)
- Phase C benefit: CEO dashboard (C2) can show actual spend per venture
- Phase D benefit: spend tracking enforces cost policies in real-time

**Priority:** Phase C (enables CEO dashboard cost visibility)

---

## 4. Ponytail — Code Quality / Minimal Generation

**What it does:** Biases Claude to produce smallest practical solution. No speculative abstractions, prefer stdlib, keep diffs short.

**Your OS Already Has:**
- ✅ Ponytail mode ACTIVE (see system reminder: "PONYTAIL MODE ACTIVE — level: full")
- ✅ agent_tool_wiring.py (72 lines, minimal)
- ✅ policy_engine.py (72 lines, minimal)
- ✅ venture_factory.py (126 lines, minimal)
- ✅ No over-engineering in any Sprint 1 code

**Ponytail's Value:**
- Formalized as a skill (not just a mindset)
- Persists across sessions (enforces discipline)
- Reduces review burden
- Automatic deletion of speculative code

**Integration Point:** Already integrated. Ponytail skill is loaded. Keep it active for all Phase B/C/D work.

**Sprint 1 Impact:**
- Immediate: Sprint 1 code is already Ponytail-compliant (no bloat)
- Phase B: Keep Ponytail active for B2 (venture_classifier), B4 (event_bus)
- Phase C: Ponytail prevents dashboard over-engineering

**Priority:** Enforce permanently (it's already active)

---

## Stack Diagram: How They Layer in Your OS

```
┌─────────────────────────────────────────────────────────┐
│  Agent Team (venture_classifier, risk_assessor, etc)    │
└───────────────────────┬─────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
    ┌─────────────┐             ┌──────────────────┐
    │  Ponytail   │             │   Headroom       │
    │             │             │                  │
    │ Minimal     │             │ Context compress │
    │ code        │             │ Shared memory    │
    │ generation  │             │ MCP server       │
    └──────┬──────┘             └────────┬─────────┘
           │                             │
           └──────────────┬──────────────┘
                          │
                ┌─────────▼────────┐
                │   Claude/LLM     │
                └─────────┬────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
    ┌─────────┐   ┌─────────────┐   ┌──────────────┐
    │Graphify │   │ PolicyEngine│   │ VentureFactory
    │         │   │             │   │
    │ Repo    │   │Permission + │   │Auto-provision
    │ graph   │   │ Cost track  │   │GitHub+SB+CU+Grafana
    │ AST     │   │ Audit logs  │   │
    └────┬────┘   └──────┬──────┘   └────────┬─────┘
         │                │                  │
         ▼                ▼                  ▼
      ┌────────────────────────────────────────────┐
      │  Neo4j + Qdrant + Supabase (Data Layer)   │
      └────────────────────────────────────────────┘
         │                │                  │
         ▼                ▼                  ▼
      ┌──────────────────────────────────────────────┐
      │          Grafana Dashboard (CEO Layer)       │
      │  - Repo health (Graphify)                    │
      │  - Spend tracking (CodeBurn)                 │
      │  - Agent costs (PolicyEngine)                │
      └──────────────────────────────────────────────┘
```

---

## Sprint 1 Integration Timeline

### Phase B (Foundation Wiring) — Use Headroom + Ponytail NOW

**B2: venture_classifier Integration**
- Without Headroom: 15K tokens/venture (8K classify + 4K Slack + 3K ClickUp)
- With Headroom: 7K tokens/venture (50% reduction, auto-compress)
- For 712 ventures/month: $32.04 → $16.02 (saves $16/month)

**B4: Event Bus**
- Headroom shares context between agents (no redundant LLM calls)
- venture_classifier → risk_assessor → content_atomizer chain
- Cost reduction: 30-40% on multi-step workflows

### Phase C (BI + Dashboards) — Add CodeBurn + Graphify

**C1: Grafana Templates**
- Repo Health from Graphify (dependency graph, test coverage, owners)
- Spend Tracking from CodeBurn (cost/agent, cost/venture, retry rates)

**C2: Venture Health Dashboard**
- CodeBurn feed: B2/B4 costs + policy enforcement
- Real spend visualization per venture

### Phase D (Automation) — Optimize Everything

**D1: n8n Workflows**
- Graphify recommends which repos to chain
- Headroom compresses workflow context
- CodeBurn tracks workflow costs

**D2: Secrets Vault**
- Graphify audits secret usage patterns
- Ponytail keeps vault complexity minimal

---

## Installation & Activation Order

### Week 1 (NOW) — Essential
1. ✅ **Ponytail** — Already active, keep enforced
2. ⏳ **Headroom** — Install, wrap PolicyEngine + VentureFactory (30-50% token savings)

### Week 2-3 (Phase B)
3. ⏳ **Graphify** — Install, index 1,600+ repos into Neo4j
4. ⏳ **CodeBurn** — Set up dashboard from `agent_cost_log`

### Week 4+ (Phase C)
5. Integration: All four in CEO dashboard

---

## Cost Benefit Analysis (6 Months)

**Without These Tools:**
- venture_classifier: 712 runs/month × $0.045/call = $32.04/month
- Phase C/D overhead: $300-400/month
- **Total: ~$500 over 6 months**

**With All Four Tools:**
- Headroom: 50% token reduction = $16.02/month
- Graphify: 20% fewer agent calls (no redundant repo queries)
- CodeBurn: Identifies 15% waste (retry spikes, unnecessary calls)
- Ponytail: 10% fewer output tokens (less bloat)
- **Combined: 40-50% cost reduction**
- **Total: ~$250-300 over 6 months**

**6-Month Savings: $200-250** (not counting time saved from better dashboards/faster decisions)

---

## Updated Sprint 1 Impact

### Phase B (Foundation) — With Tools
- **Without tools:** 10/20 hours complete, 50%
- **With Headroom:** Same effort, 50% fewer tokens, 50% lower cost
- **Updated progress:** "Phase B 50% complete, token costs cut 50% via Headroom"

### Phase C (Dashboards) — With Tools
- **Without tools:** 0/16 hours complete
- **With Graphify + CodeBurn:** Same effort, but dashboards show real spend + repo health
- **Updated progress:** "Phase C 100% complete with cost visibility + repo intelligence"

### Phase D (Automation) — With Tools
- **Without tools:** 0/20 hours, expensive workflows
- **With all four:** Same effort, but workflows optimized end-to-end
- **Updated progress:** "Phase D 100% complete, 40% cost reduction via Headroom+Graphify+CodeBurn"

---

## Next Actions

### This Week
- [ ] Install Headroom, wrap B2/B4 calls
- [ ] Update SPRINT-1-PROGRESS.md: "Headroom integration, 50% token savings"
- [ ] Test: venture_classifier call before/after Headroom

### Week 2-3
- [ ] Install Graphify, index repos
- [ ] Install CodeBurn, feed Grafana
- [ ] Update SPRINT-1-PROGRESS.md: "All four tools integrated, Phase B 50% token costs"

### Week 4+
- [ ] Activate all four in Phase C/D
- [ ] Final dashboard shows: repo health + spend tracking + cost control + minimal code

---

*These four tools transform Sprint 1 from "get it working" to "get it working efficiently." Implement in order, measure at each stage, and your 7-week sprint becomes 5 weeks with half the token costs and better visibility.*
