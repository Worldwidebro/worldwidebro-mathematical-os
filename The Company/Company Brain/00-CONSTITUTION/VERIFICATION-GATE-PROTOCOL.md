# Verification Gate Protocol — Anti-Hallucination Mandate

**Authority:** CLAUDE.md Rule #1 + REALITY.md live truth ledger  
**Scope:** All claims of completion, deployment, or working code  
**Updated:** 2026-09-10  
**Enforcement:** Non-negotiable before commit, deployment, or status update

---

## The Core Rule

> **NEVER claim a capability exists or works without producing evidence from one of these:**
> 1. **Live CLI output** (docker ps, curl response, git log)
> 2. **Database query result** (SELECT from Supabase, Neo4j MATCH, Redis GET)
> 3. **Test output** (passing test suite, E2E trace, browser screenshot)
> 4. **Production verification** (HTTP 200 response, actual data returned, no error logs)

**If you cannot produce evidence, say "NOT VERIFIED" and stop.**

---

## Three Verification Gates

### Gate 1: Build Verification
**Claim:** "Code compiles and tests pass"
**Required:** `npm test` output showing ✅ PASS, zero errors
**Reject if:** Skipped tests, warnings, or "should pass"

### Gate 2: Integration Verification  
**Claim:** "API endpoint is deployed and working"
**Required:** 
```bash
curl -X POST https://app.vercel.app/api/endpoint -d '{}' | jq .
# Returns: HTTP 200 + actual JSON (not 404, not HTML error)
```
**Reject if:** Returns 404, 500, error page, or mocked data

### Gate 3: End-to-End Verification
**Claim:** "Full feature works (API + database + external service)"
**Required:**
1. curl returns data
2. SELECT from database confirms row exists
3. External service (Stripe/OSRM/etc.) confirms call was made
**Reject if:** Any one of these fails

---

## Red Flags (STOP if You See These)

🛑 "Tests passed" (no output shown)  
🛑 "API is deployed" (never curled production)  
🛑 "It works" (no E2E proof)  
🛑 "Should be wired" (should ≠ verified)  
🛑 "Commits made" (commits ≠ working)  

**When you see these → Ask: "Show me the actual output"**

---

## Current Status: Week 1 Reality

| Venture | Claimed | Gate 1 | Gate 2 | Gate 3 | Verified |
|---------|---------|--------|--------|--------|----------|
| OPS-001 | "Live" | ? | ❌ | ? | ❌ |
| LT-005 | "Live" | ? | ❌ | ? | ❌ |
| CALLCENTER | "Live" | ? | ❌ | ? | ❌ |
| CON-001 | "Complete" | ❌ | ❌ (404) | ❌ | ❌ |
| RE-001 | "Complete" | ❌ | ❌ (500) | ❌ | ❌ |
| LT-011 | "Complete" | ❌ | ❌ | ❌ | ❌ |

**Next step:** Actually verify each one. Production endpoints must return HTTP 200 before any revenue execution.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
