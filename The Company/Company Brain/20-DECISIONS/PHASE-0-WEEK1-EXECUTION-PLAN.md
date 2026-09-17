# Phase 0 Week 1: Agentic Engineering Execution Plan

**Timeline:** Sep 17-22, 2026  
**Scope:** Loop Engineering + Eval Engineering (P0/P1 repos)  
**Success Metric:** All Tier-0 ventures have working n8n workflows + deepeval evals running

---

## COMPLETION CRITERIA (Must ALL pass)

### Loop Engineering (n8n + langgraph)
- [ ] n8n running on Vercel (accessible at vercel deployment)
- [ ] Connected to Supabase (read/write ventures, tasks)
- [ ] 3 starter workflows: OPS-001 (cold call), LT-005 (dispatch), CALLCENTER (IVR)
- [ ] Langgraph L1/L2/L3 templates created (in Neo4j + code)
- [ ] Test: Run 1 complete workflow end-to-end, capture execution trace

### Eval Engineering (deepeval + LangSmith)
- [ ] Deepeval installed + imported in Python services
- [ ] LangSmith API key configured (from Bitwarden)
- [ ] 5 eval harnesses created (correctness, speed, safety, cost, reliability)
- [ ] Baseline evals run on 50-agent sample (capture pass_rate per agent)
- [ ] Test: Eval run produces JSON report with scores

### Measurement
- [ ] Neo4j has Loop + Eval repo nodes (28 repos)
- [ ] VEX Gap Solutions shows 5 Loop repos + 1 Eval repo as "installed"
- [ ] PostgreSQL eval.evaluation_runs table has 50+ baseline records

---

## TASK DECOMPOSITION (15-min unit rule)

### LOOP ENGINEERING

**Task L1: n8n Vercel Deployment** (45 min, Haiku)
- Unit 1a (15 min): Create n8n Vercel config + environment
  - Risk: Vercel auth, secrets setup
  - Done: n8n runs on Vercel, accessible via HTTPS
  
- Unit 1b (15 min): Wire n8n to Supabase
  - Risk: Row-level security, JWT auth
  - Done: n8n can read/write ventures table
  
- Unit 1c (15 min): Test connection with sample query
  - Risk: Query performance, cold start time
  - Done: Query < 500ms, returns correct data

**Task L2: Create n8n Starter Workflows** (60 min, Sonnet)
- Unit 2a (15 min): OPS-001 cold call workflow
  - Trigger: Manual (test)
  - Steps: Load prospect → Generate pitch → Log call → Update status
  - Risk: Anthropic API rate limits
  - Done: Workflow runs, produces call log
  
- Unit 2b (15 min): LT-005 dispatch workflow
  - Trigger: New delivery request (Supabase webhook)
  - Steps: Fetch shipment → Calculate route → Assign driver → Notify
  - Risk: Route calculation latency
  - Done: 3 test shipments dispatched correctly
  
- Unit 2c (15 min): CALLCENTER IVR workflow
  - Trigger: Incoming Twilio call
  - Steps: Transcribe → Classify intent → Route or transfer
  - Risk: Twilio webhook authentication
  - Done: Handles 2 test calls correctly
  
- Unit 2d (15 min): Error handling + logging
  - Risk: Silent failures, no observability
  - Done: All workflows log errors to PostgreSQL

**Task L3: Langgraph L1/L2/L3 Templates** (45 min, Sonnet)
- Unit 3a (15 min): L1 Report-Only template
  - Agent proposes action → system returns result (no execution)
  - Done: Template in code, test: agent asks → receives response
  
- Unit 3b (15 min): L2 Supervised template
  - Agent proposes → human approves → agent executes
  - Risk: Approval queue handling, timeout logic
  - Done: Can submit 1 task, await approval, execute
  
- Unit 3c (15 min): L3 Autonomous template
  - Agent executes autonomously after certification
  - Risk: Runaway execution, no circuit breaker
  - Done: Agent runs 5 tasks, respects max_retries + timeout

**Task L4: Test Loop Execution** (30 min, Haiku)
- Unit 4a (15 min): End-to-end OPS-001 workflow
  - Load prospect → n8n → log call → Supabase updated
  - Risk: State consistency, timing issues
  - Done: Full trace logged, Supabase reflects change
  
- Unit 4b (15 min): Verify L1/L2/L3 routing
  - Submit task in L1 mode → verify report-only
  - Submit task in L2 mode → verify approval gate
  - Risk: State machine transitions
  - Done: All 3 modes work correctly

---

### EVAL ENGINEERING

**Task E1: Deepeval Setup** (30 min, Haiku)
- Unit 1a (15 min): Install deepeval + dependencies
  - pip install deepeval
  - Risk: Python version (3.9+), dependency conflicts
  - Done: deepeval imports cleanly
  
- Unit 1b (15 min): Test LangSmith API connection
  - export LANGSMITH_API_KEY
  - Test: Create trace, send to LangSmith
  - Risk: API key invalid, rate limits
  - Done: Trace visible in LangSmith dashboard

**Task E2: Create 5 Eval Harnesses** (60 min, Sonnet)
- Unit 2a (15 min): Correctness evals (answer accuracy)
  - Metric: AnswerRelevancyMetric (threshold 0.7)
  - Test: 5 sample Q&As, measure F1 score
  - Done: Correctness harness in Python, < 500ms per eval
  
- Unit 2b (15 min): Speed evals (latency)
  - Metric: Response time < 5000ms threshold
  - Test: Run 5 queries, capture latencies
  - Done: Speed harness works, captures timing
  
- Unit 2c (15 min): Safety evals (no hallucinations)
  - Metric: Regex check + entailment score
  - Test: 10 prompts designed to trigger hallucinations
  - Done: Safety harness catches false claims
  
- Unit 2d (15 min): Cost evals (token efficiency)
  - Metric: tokens_used < budget per task
  - Test: Monitor 5 agent runs
  - Done: Cost harness tracks spend
  
- Unit 2e (15 min): Reliability evals (retry logic)
  - Metric: success_rate after retries
  - Test: Simulate 3 failures + retries
  - Done: Reliability harness logs recovery

**Task E3: Baseline Evals (50-Agent Sample)** (45 min, Sonnet)
- Unit 3a (15 min): Select 50-agent sample
  - Random 50 from 310 agents (stratified by layer)
  - Risk: Representativeness
  - Done: Sample in agents_baseline.yaml
  
- Unit 3b (15 min): Run evals on sample
  - For each eval harness: run on 50 agents
  - Risk: Long runtime (could be hours)
  - Done: Baseline JSON report generated
  
- Unit 3c (15 min): Store results in PostgreSQL
  - INSERT into eval.evaluation_runs
  - Risk: Data integrity, duplicates
  - Done: 250 eval records (50 agents × 5 evals) in DB

**Task E4: Test Eval Pipeline** (30 min, Haiku)
- Unit 4a (15 min): Verify report structure
  - Check: All 5 evals appear in report
  - Check: Scores are numeric, in expected range
  - Done: Report JSON valid and complete
  
- Unit 4b (15 min): Verify Neo4j wiring
  - Query: `MATCH (agent:Agent {id: "AGT-001"})-[:HAS_EVAL]->(run:EvalRun)`
  - Done: Relationships exist, scores match PostgreSQL

---

## MODEL ROUTING

| Task | Complexity | Model | Why |
|------|-----------|-------|-----|
| L1: Vercel config | Low | Haiku | Boilerplate, no reasoning needed |
| L2: Workflows | High | Sonnet | Multi-step logic, edge cases, error handling |
| L3: Langgraph templates | High | Sonnet | Architecture, state machines, testing |
| L4: E2E testing | Medium | Haiku | Verification, no new logic |
| E1: Deepeval setup | Low | Haiku | Installation, straightforward |
| E2: Eval harnesses | High | Sonnet | Design eval metrics, threshold tuning |
| E3: Baseline runs | Low | Haiku | Execution, data collection |
| E4: Verification | Medium | Haiku | Data validation checks |

**Total tokens (est.):** 12K Haiku + 18K Sonnet = 30K tokens (~$0.40)

---

## EVAL-FIRST LOOP

### Capability Eval (Before Implementation)

**Loop Engineering Capability:**
```
Question: "Can n8n orchestrate OPS-001 cold call workflow?"
Baseline: No (not implemented)
Success: Workflow runs end-to-end, produces call log
Regression: If workflow fails on 50% of inputs, implementation failed
```

**Eval Engineering Capability:**
```
Question: "Can deepeval measure agent correctness?"
Baseline: No (not set up)
Success: Eval harness runs, returns score 0-1, captures failures
Regression: If all agents score 1.0, harness is broken (no discrimination)
```

### Regression Eval (After Implementation)

**Loop Engineering (Post-impl):**
```
Test 1: OPS-001 workflow
  Input: 5 test prospects
  Expected: 5 call logs in Supabase
  Actual: [run after implementation]
  
Test 2: LT-005 workflow
  Input: 3 test shipments
  Expected: 3 dispatch records
  Actual: [run after implementation]
  
Test 3: CALLCENTER workflow
  Input: 2 test calls
  Expected: 2 transcriptions + intent classifications
  Actual: [run after implementation]
  
Test 4: L1/L2/L3 routing
  Input: 1 task in each mode
  Expected: L1 reports, L2 awaits approval, L3 executes
  Actual: [run after implementation]
```

**Eval Engineering (Post-impl):**
```
Test 1: Correctness eval
  Input: 5 Q&As (known answers)
  Expected: Scores 0.7-1.0 for correct, < 0.5 for wrong
  Regression: If all score identical, harness broken
  
Test 2: Safety eval
  Input: 10 adversarial prompts
  Expected: Flags 8+/10 as unsafe
  Regression: If all pass, harness not discriminating
  
Test 3: Baseline stats
  Input: 50-agent sample evals
  Expected: Mean pass_rate 0.5-0.8, std > 0.1
  Regression: If std < 0.05, not discriminating agents
```

---

## SUCCESS CRITERIA (Weekly Checkpoint)

**Friday Sep 22 EOD:**
- [ ] n8n deployed to Vercel, accessible
- [ ] OPS-001 cold call workflow runs (1 test call logged)
- [ ] LT-005 dispatch workflow runs (1 test shipment dispatched)
- [ ] CALLCENTER IVR workflow runs (1 test call classified)
- [ ] Langgraph L1/L2/L3 templates created + tested
- [ ] Deepeval installed, LangSmith connected
- [ ] 5 eval harnesses created + working
- [ ] Baseline evals on 50 agents complete (~250 records)
- [ ] All results in PostgreSQL + Neo4j
- [ ] VEX Gap Solutions shows "Installed" for n8n + deepeval

**If ANY fail:**
- Document failure + blockers
- Escalate to Sonnet for root-cause analysis
- Replan remaining week (if needed)

---

## PARALLEL EXECUTION (This Week)

```
Day 1-2 (Wed-Thu):
  Thread 1: n8n Vercel setup (L1, L2, L3, L4)
  Thread 2: Langgraph templates (L3)
  → Both should complete by EOD Thursday

Day 2-3 (Thu-Fri):
  Thread 1: Deepeval + LangSmith (E1)
  Thread 2: Eval harnesses (E2)
  Thread 3: Baseline evals + verification (E3, E4)
  → All should complete by EOD Friday

Test:
  Day 3 (Friday morning): Run all regression evals
  → Collect results, verify success criteria
```

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| n8n deploy fails | Medium | HIGH | Have local n8n fallback ready |
| Supabase connection fails | Low | HIGH | Test with psql first |
| Deepeval evals too slow | Medium | MEDIUM | Run in background, cache results |
| LangSmith API key invalid | Low | HIGH | Test immediately, have fallback |
| Baseline evals take > 2h | Medium | MEDIUM | Parallelize agent batches |
| State machine bugs in L2/L3 | High | HIGH | Add extensive logging, test each state |

---

## Token Budget

| Phase | Model | Est. Tokens | Cost |
|-------|-------|-------------|------|
| L1-L4 Planning + impl | Sonnet | 18,000 | $0.27 |
| E1-E4 Planning + impl | Sonnet | 12,000 | $0.18 |
| Testing + iteration | Haiku | 8,000 | $0.04 |
| **TOTAL** | — | **38,000** | **~$0.50** |

**If needed (worst case):** +50% buffer = 57K tokens

---

## Next Steps (After Week 1)

**If Phase 0 succeeds:**
→ Week 2: Graph + Tool + Context engineering (Phase 1)

**If Phase 0 partially succeeds:**
→ Fix blockers + re-test
→ Decide: continue Phase 1 or extend Week 1

**If Phase 0 fails:**
→ Escalate to Opus for architecture review
→ Replan entire rollout

