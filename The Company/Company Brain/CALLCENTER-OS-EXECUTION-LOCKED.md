[[STARTHERE]] | [[REALITY]] | [[09-OPERATIONS|Call Center OS]] | [[INDEX]]

# Call Center OS — Execution Locked (Sep 9, 2026)

**Authority:** Infrastructure Control Plane (CP-027) + Execution Control Plane (CP-033)  
**Status:** ✅ EXECUTION PLAN LOCKED — Ready to start Phase 1  
**Timeline:** 8 weeks MVP (Phases 1-3) + 4 weeks extended (Phases 4-5)  
**Full plan:** [github.com/Worldwidebro/callcenter/EXECUTION-PLAN.md](https://github.com/Worldwidebro/callcenter)

---

## Goals from Chat (Sep 9)

### Strategic Intent
- Build **Customer Operations OS** that beats Vapi on AI Supervisor + Business KG + Dispatch
- Use LiveKit for voice (self-hosted, 80% cost savings vs Vapi)
- Launch revenue from 7 Tier-1 ventures within 8 weeks

### Execution Goals
1. **Phase 1 (Week 1-2):** Inbound/outbound calls via LiveKit SIP + AI receptionist ✅ Locked
2. **Phase 2 (Week 3-4):** Multi-agent orchestrator (Reception, Sales, Support, Scheduling) ✅ Locked
3. **Phase 3 (Week 5-8):** CRM sync + dispatch integration → first revenue ✅ Locked
4. **Phase 4 (Week 9-12):** AI Supervisor (autonomous SLA monitoring) ⏳ Deferred
5. **Phase 5 (Week 13-16):** Evaluation center (regression gates) ⏳ Deferred

---

## Tech Stack (Locked)

**Core infrastructure (already live in Company Brain):**
- ✅ Neo4j (20,363 edges)
- ✅ Qdrant (17,236 vectors)
- ✅ PostgreSQL + Redis + MinIO
- ✅ OmniRoute/LiteLLM (model gateway)
- ✅ Langfuse (observability, deployed but not wired)

**New deployments (Phases 1-3):**
- 🟡 **LiveKit Server** (realtime voice transport)
- 🟡 **LiveKit Agents** (STT→LLM→TTS pipeline)
- 🟡 **LiveKit SIP** (phone integration)
- 🟡 **LangGraph** (agent orchestrator)
- ✅ **n8n** (automation, planned Phase 2)
- ✅ **Twenty CRM** (catalogued, integrate Phase 3)
- ✅ **Chatwoot** (omnichannel, Phase 4+)
- ✅ **Cal.com** (scheduling, Phase 3)
- ✅ **Keycloak** (identity, Phase 3+)

**Deferred (Phase 4+):**
- ⏳ Promptfoo (test harness)
- ⏳ DeepEval (agent evals)
- ⏳ OpenFGA (fine-grained authz)
- ⏳ Pipecat (voice alternative, if LiveKit needs fallback)

---

## Existing OSS Catalogued

**Already in external-capabilities-by-sector.yaml:**
| Project | Status | Reference |
|---------|--------|-----------|
| LangGraph | ✅ Catalogued | langchain-ai/langgraph |
| Chatwoot | ✅ Catalogued | chatwoot/chatwoot |
| Twenty | ✅ Catalogued | twentyhq/twenty |
| n8n | ✅ Catalogued | SEC-028 (Order Routing) |
| Langfuse | ✅ Catalogued | langfuse/langfuse |
| Keycloak | ✅ Catalogued | keycloak/keycloak |
| NATS | ✅ Catalogued | nats-io/nats-server |

**NOT in registry (to add):**
| Project | Gap | Priority |
|---------|-----|----------|
| LiveKit | Voice transport | 🔴 P0 |
| LiveKit Agents | Voice agents | 🔴 P0 |
| Pipecat | Voice alternative | 🟡 P1 |
| Promptfoo | Test harness | 🟡 P1 |
| OpenFGA | Fine-grained authz | 🟡 P2 |

---

## Scope Decision (MVP vs Full)

**Why MVP (Phases 1-3 only)?**
- Ship revenue in 8 weeks (vs 16 weeks for all phases)
- Validate voice + agent + business model ASAP
- Add AI Supervisor + Evaluation when revenue-proven
- Risk mitigation: only 8 weeks invested if model fails

**What's in MVP:**
- ✅ Voice runtime (LiveKit)
- ✅ Multi-agent orchestration (LangGraph)
- ✅ Business integration (Neo4j, n8n, CRM)
- ✅ First revenue attribution

**What's deferred to Month 2-3:**
- ⏳ AI Supervisor (autonomous interventions)
- ⏳ Evaluation center (regression gates + safety)

---

## Week 1 Action Items (Phase 1 Kickoff)

**Owner:** DevOps + Engineering  
**Timeline:** Sep 9-15 (Week 1)  
**Deliverable:** Inbound call working with AI response

- [ ] **Day 1-2:** Deploy LiveKit server (Docker on Mac Studio)
- [ ] **Day 3:** Evaluate LiveKit Agents vs Pipecat (recommend LiveKit Agents)
- [ ] **Day 4:** Wire OmniRoute/LiteLLM as backend
- [ ] **Day 5:** Test inbound call end-to-end (phone → SIP → LiveKit → AI → phone)

---

## Revenue Milestones

| Milestone | Timeline | Owner | Ventures |
|-----------|----------|-------|----------|
| **AI handles first call** | Week 2 (Sep 16) | DevOps | Any |
| **Call → CRM sync** | Week 6 (Oct 1) | Engineering | Any |
| **First revenue attributed** | Week 8 (Oct 13) | Sales | OPS-001, LT-005, CON-001 |
| **Supervisor autonomous** | Week 12 (Nov 10) | Engineering | All 7 |
| **Production safety gates** | Week 16 (Dec 8) | QA | All 7 |

---

## Cross-Repo References

**Primary execution repo:** [github.com/Worldwidebro/callcenter](https://github.com/Worldwidebro/callcenter)  
**Plan location:** callcenter/EXECUTION-PLAN.md  
**Folder structure:** callcenter/VOICE-OS/ (livekit, agents, configs)

**Related Company Brain docs:**
- [[CLAUDE.md]] — Infrastructure status
- [[oss-integration-candidates-2026-09-05.md]] — OSS evaluation history
- [_REGISTRIES/external-capabilities-by-sector.yaml] — External OSS catalog

---

## Locked Decisions

**Architecture:** ✅ LiveKit + LangGraph + Business integration
**Scope:** ✅ MVP (Phases 1-3) + Extended (Phases 4-5)
**Timeline:** ✅ 8 weeks MVP, +4 weeks extended
**Execution:** ✅ Starting Sep 9 (Week 1)
**First revenue:** ✅ Target end of Week 8 (Oct 13)

---

**Generated:** 2026-09-09  
**Status:** Plan locked, execution ready  
**Next:** Phase 1 kickoff (this week)
