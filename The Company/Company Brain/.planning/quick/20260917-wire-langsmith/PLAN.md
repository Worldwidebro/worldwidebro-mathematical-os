---
objective: Wire LangSmith API integration
status: planning
effort: 30 min
---

# Wire LangSmith (Quick Task)

## Objective
Configure LangSmith API key from Bitwarden and wire it into the evaluation pipeline so deepeval evals can send traces to LangSmith.

## Success Criteria
- [ ] LangSmith API key retrieved from Bitwarden
- [ ] Environment variable configured (LANGSMITH_API_KEY)
- [ ] Test trace created + sent to LangSmith
- [ ] Trace visible in LangSmith dashboard
- [ ] Documented in eval-harness setup scripts

## Tasks
1. Get API key from Bitwarden
2. Configure in environment (.env or export)
3. Create test trace via deepeval
4. Send to LangSmith API
5. Verify in dashboard
6. Update PHASE-0-WEEK1-EXECUTION-PLAN.md with actual credentials scope

## Dependencies
- deepeval installed (from eval-harness-registry-schema.sql)
- LangSmith project created (aipehhzlsmfxxzwceppd)
- Bitwarden access

## Blockers
None identified

## Notes
- Should take 20-30 min end-to-end
- Critical for eval pipeline (unblocks deepeval harnesses)
- Part of Phase 0 Week 1 execution
