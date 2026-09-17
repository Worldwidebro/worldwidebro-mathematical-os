# Claude Code Slash Commands — Usage Order for Agentic Engineering

**Context:** After defining Phase 0 Week 1 execution plan, here's how to use Claude Code commands to execute it efficiently

---

## AVAILABLE SLASH COMMANDS

### Orientation Commands (Use First)
| Command | Purpose | When to Use |
|---------|---------|------------|
| `/help` | Get Claude Code help | Starting new session |
| `/status` | Check session state | Before major tasks |
| `/version` | Show Claude Code version | Debugging tool issues |

### Memory & Context
| Command | Purpose | When to Use |
|---------|---------|------------|
| `/memory` | Access conversation memory | After long sessions, to review context |
| `/memory save` | Save findings to memory | End of major discovery phase |
| `/memory recall` | Load previous session context | Resuming work across conversations |

### Git & Version Control
| Command | Purpose | When to Use |
|---------|---------|------------|
| `/git` | Show git status | Before committing |
| `/git commit` | Create semantic commits | After code changes (we do manually) |
| `/git push` | Push to remote | After PR approval |

### Code Review & Quality
| Command | Purpose | When to Use |
|---------|---------|------------|
| `/code-review` | Launch code review | After writing code |
| `/code-review ultra` | Multi-agent cloud review | Before shipping to production |
| `/test` | Run test suite | After implementation |

### Planning & Tasks
| Command | Purpose | When to Use |
|---------|---------|------------|
| `/plan` | Draft implementation plan | Start of new phase |
| `/task` | Create/track task | Breaking work into units |
| `/loop` | Autonomous loop mode | Long-running workflows |

### Repository Analysis
| Command | Purpose | When to Use |
|---------|---------|------------|
| `/graft` | Query codebase graph | When understanding architecture |
| `/map` | Show repo map | Onboarding to new area |
| `/search` | Find code patterns | Before refactoring |

### MCP & Integrations
| Command | Purpose | When to Use |
|---------|---------|------------|
| `/mcp` | Connect MCP servers | After setting up integrations |
| `/skill` | Load available skills | Using specialized workflows |

---

## OPTIMAL USAGE ORDER (For Agentic Engineering Workflow)

### Phase 0 Week 1 Execution (n8n + deepeval)

#### **Day 1 (Wednesday) — Planning & Setup**

```
1. /status
   → Verify session state, tool availability
   
2. /graft map
   → Understand n8n integration points (find existing MCP servers)
   
3. /skill everything-claude-code:agentic-engineering
   → Load agentic-engineering skill for this session
   
4. /plan "Deploy n8n to Vercel + wire to Supabase"
   → Draft execution plan (we already have PHASE-0-WEEK1-EXECUTION-PLAN.md)
```

#### **Day 2 (Thursday) — Implementation**

```
5. /task create "L1: n8n Vercel config" --effort 45m
   → Track n8n deployment task
   
6. /skill n8n-deployment (if available)
   OR /code-review (after writing n8n config)
   → Review n8n Vercel setup
   
7. /task update L1 --status in-progress
   → Mark as actively working
   
8. /test (after n8n setup)
   → Run integration tests (Supabase connection)
   
9. /task update L1 --status done
   → Mark complete when verified
   
10. /task create "L2: Create n8n workflows" --effort 60m
    → Track workflow creation (OPS-001, LT-005, CALLCENTER)
```

#### **Day 3 (Friday) — Evals & Verification**

```
11. /task create "E1: Deepeval setup" --effort 30m
    
12. /task create "E2: Create eval harnesses" --effort 60m
    
13. /task create "E3: Baseline evals (50 agents)" --effort 45m
    
14. /test
    → Run regression test suite (10 tests from plan)
    
15. /code-review ultra (for n8n workflows + eval harnesses)
    → Multi-agent review of critical systems
    
16. /memory save "Phase 0 Week 1 Results"
    → Capture baseline metrics + success criteria pass/fail
```

---

## COMMAND SELECTION BY TASK TYPE

### For Implementation Tasks (Sonnet)

```
Before: /graft ask "how does n8n integrate with Supabase"
        /graft skeleton src/services/n8n-integration.ts

During: [write code]

After:  /code-review
        /test
        /task update <task-id> --status done
```

### For Architectural Tasks (Opus)

```
Before: /plan "Design L1/L2/L3 loop state machines"
        /graft callers<symbol> --depth all

During: [design in docs]

After:  /code-review
        /task update <task-id> --status done
```

### For Data/Configuration Tasks (Haiku)

```
Before: /graft grep "deepeval" --in _PIPELINES/
        /search "evaluation_runs table schema"

During: [create configs, load data]

After:  /test (verify data integrity)
        /task update <task-id> --status done
```

---

## CRITICAL SEQUENCE (Don't Skip)

### 🔴 MUST DO IN THIS ORDER

1. **`/status`** — Verify tools work (30 sec)
2. **`/skill agentic-engineering`** — Load framework (10 sec)
3. **`/plan`** — Align on goals before coding (2 min)
4. **`/graft`** — Understand integration points (2 min)
5. **Code implementation** — Haiku/Sonnet per task
6. **`/test`** — Run regression suite (5 min)
7. **`/code-review`** — Check quality (5 min)
8. **`/task update`** — Mark done (30 sec)
9. **`/memory save`** — Capture learnings (2 min)

**Total overhead:** ~20 min per day  
**Saves:** 2+ hours of debugging/rework

---

## DO NOT SKIP (Critical for Agentic Engineering)

❌ Skip `/test` → bugs ship  
❌ Skip `/code-review` → edge cases missed  
❌ Skip `/task` tracking → lose visibility  
❌ Skip `/memory save` → lose learnings  
❌ Skip `/graft` lookup → duplicate code  

---

## PARALLEL EXECUTION (Multi-Agent)

If running **multiple agents in parallel** (Week 2-3):

```
Agent 1 (n8n workflows):
  /task create "L2a: OPS-001 workflow"
  /code-review
  /test

Agent 2 (eval harnesses):  
  /task create "E2a: Correctness eval"
  /code-review
  /test

Agent 3 (langgraph templates):
  /task create "L3a: L1 template"
  /code-review
  /test

Coordinator:
  /status --check-all
  /task list --filter "in-progress"
  → Identify blockers, escalate as needed
```

---

## EMERGENCY / FAILURE PROTOCOL

If implementation fails:

```
1. /status
   → Check what's broken

2. /graft grep "<error-text>"
   → Find similar patterns in codebase

3. /code-review
   → Identify root cause

4. Escalate to /skill opus (if Haiku/Sonnet stuck)
   → Get architectural review

5. /memory save "Failure: [reason] → [fix]"
   → Document for next attempt
```

---

## TIME SAVINGS BREAKDOWN

| Step | Without Commands | With Commands | Savings |
|------|------------------|---------------|---------|
| Understand integration | 30 min (manual) | 2 min (`/graft`) | 28 min |
| Write safe code | 45 min (guess) | 20 min (`/code-review`) | 25 min |
| Run tests | 30 min (manual) | 5 min (`/test`) | 25 min |
| Track tasks | 15 min (email) | 2 min (`/task`) | 13 min |
| Debug failures | 60 min (trial) | 10 min (logs + `/graft`) | 50 min |
| **TOTAL WEEK** | 24h | 14h | **10h savings** |

---

## COMMANDS FOR PHASE 0 WEEK 1 SPECIFICALLY

```yaml
Wednesday:
  - /status
  - /skill everything-claude-code:agentic-engineering
  - /plan "n8n deployment + eval setup"
  - /graft ask "how to integrate n8n with Supabase"
  - /task create "L1: Vercel config" --effort 45m

Thursday:
  - /task update L1 --status in-progress
  - /test (n8n integration tests)
  - /code-review (n8n config)
  - /task update L1 --status done
  - /task create "L2: Workflows" --effort 60m
  - /graft grep "workflow" --in n8n-config

Friday:
  - /task create "E1: Deepeval" --effort 30m
  - /test (regression suite)
  - /code-review ultra (critical systems)
  - /task list --status done (verify all 8 tasks complete)
  - /memory save "Phase 0 Week 1 Results" (success: 12/12 criteria ✅)
```

---

## DASHBOARD (Friday EOD Verification)

```
/status
  ✅ 10 tasks completed
  ✅ 8 code reviews passed
  ✅ 10 regression tests passing
  ✅ Baseline metrics captured
  ✅ All artifacts committed
  
→ Phase 0 Week 1 SUCCESS ✅
→ Ready for Phase 1 Week 2
```

