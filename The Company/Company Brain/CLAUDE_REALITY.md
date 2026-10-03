---
type: truth-verification-framework
canonical: false
authority: intelligence-platform-layer
version: 1.0
updated_at: 2026-10-02T23:47:00Z
relates_to: CLAUDE_MASTER_ONTOLOGY
---

# CLAUDE_REALITY — Truth Verification Layer

**Claude claims are not truth. Truth lives in evidence, verification, and tested systems.**

**Last updated:** 2026-10-02  
**Status:** Critical operating principle  
**Framework:** Evidence-based verification

---

## Core Principle

```
CLAUDE SAYS X
    ≠
SYSTEM IS X

CLAUDE_CLAIM
    ↓
EVIDENCE
    ↓
TEST
    ↓
VERIFIED_STATE
    ↓
[[REALITY]]
```

**Key rule:** *Never trust Claude's word alone. Verify against:*
- Live system state (Docker, Neo4j, databases)
- Git commit history + blame
- Test results + CI output
- Network connectivity tests
- Actual API responses
- Audit logs + timestamps

---

## Verification Layers

### [[CLAIM]]
**What Claude asserts**

Example claims:
- "The API is running"
- "The deployment succeeded"
- "The bug is fixed"
- "The database migrated correctly"

**Status:** Unverified (L0)

### [[EVIDENCE]]
**Facts that support or contradict claim**

For "The API is running":
- HTTP 200 response ✓
- Service logs show startup ✓
- Memory usage normal ✓
- No error entries ✗

**Status:** Partially verified (L1)

### [[SOURCE]]
**Where evidence comes from**

- Docker container health status
- `curl http://localhost:3000`
- Log output from service
- Process memory from `top`
- Database query results

**Credibility hierarchy:**
1. **Direct observation** — "I just ran `curl` and got 200"
2. **System output** — "Docker ps shows container running"
3. **Logs** — "Service logs show no errors"
4. **Documentation** — "README says this should work"
5. **Assumption** — "It should be working"

### [[OBSERVATION]]
**Claude directly verifies**

```bash
# GOOD: Direct observation
$ docker ps | grep api
# Output: api-container running ✓

# BAD: Assumption
Claude: "The API is running (I assume)"
# No verification
```

**How Claude observes:**
- Run shell commands
- Make HTTP requests
- Query databases
- Read files directly
- Check git status
- Run tests

### [[VERIFICATION]]
**Test the claim**

For "The deployment succeeded":
- [ ] Service responds
- [ ] All ports open
- [ ] Health checks pass
- [ ] Logs show no errors
- [ ] Metrics normal
- [ ] Previous version still works (rollback ready)

### [[TEST]]
**Reproducible proof**

```bash
# Test: "API is running"
$ curl -s http://localhost:3000/health
# Expected: {"status":"ok"}
# Actual: {"status":"ok"}
# Result: PASS ✓
```

### [[RESULT]]
**Outcome of verification**

**Possible results:**
- ✅ **VERIFIED** — Claim matches reality
- ⚠️ **PARTIALLY_VERIFIED** — Some evidence supports, some contradicts
- ❌ **FAILED** — Evidence contradicts claim
- ❓ **UNKNOWN** — No evidence found
- ⏳ **NOT_TESTED** — Could be true, but unverified

### [[CONFIDENCE]]
**Certainty level (0.0 - 1.0)**

| Score | Status | Behavior |
|-------|--------|----------|
| 0.0 | Certainty = false | Do not rely on this |
| 0.3 | Low confidence | Seek additional verification |
| 0.6 | Moderate confidence | Accept with caution |
| 0.85 | High confidence | Reasonable to act on |
| 1.0 | Certainty = true | Safe to depend on |

### [[UNCERTAINTY]]
**Known unknowns**

Example:
```
Claude: "The database migrated correctly"
Evidence: Migration script completed
Unknown: Did all constraints pass?
Unknown: Are indexes properly built?
Unknown: Query performance affected?

Confidence: 0.65 (moderate, with gaps)
```

### [[ASSUMPTION]]
**Unverified premise**

Example:
```
Claude: "Updating that file should be safe"
Assumption: The file isn't critical infrastructure
Assumption: No other services depend on it
Assumption: Rollback is straightforward

Reality check needed before acting
```

### [[INFERENCE]]
**Logical deduction from evidence**

```
Evidence:
- Service logs show startup ✓
- No error entries ✓
- CPU/memory normal ✓

Inference:
→ Service appears healthy

Confidence: 0.8 (high, from multiple signals)
```

### [[DRIFT]]
**Discrepancy from source-of-truth**

When Claude says X but [[REALITY]] shows Y:

```
Claude says: "Feature is complete"
Reality shows:
  - Code is committed ✓
  - Tests pass ✓
  - Deployed to staging ✓
  - NOT in production ✗

Drift identified: Incomplete claim
Correction needed: "Feature in staging, not production"
```

---

## Verification Checklist

**Before accepting Claude's claim:**

- [ ] Claude ran a test (not just said it)
- [ ] Result shown (not assumed)
- [ ] Test passed (✓ not ?)
- [ ] Multiple signals align (not just one check)
- [ ] Recently verified (not from hours ago)
- [ ] Documented in audit trail
- [ ] Rollback plan clear

---

## Common False Claims (Watch For)

### "The deployment succeeded"
**Verify:** Actual HTTP response, health checks, monitoring

### "The bug is fixed"
**Verify:** Test passes, regression test added, production verified

### "No errors in logs"
**Verify:** Actually read logs (not just "should be fine")

### "The migration is complete"
**Verify:** Data integrity check, rollback tested

### "All tests pass"
**Verify:** Run tests yourself, check CI output

### "The API is available"
**Verify:** `curl` or HTTP client, not assumption

### "The feature works"
**Verify:** Use the feature end-to-end, check edge cases

---

## Reality Sources (Ranked)

1. **Live system state** — Docker, databases, services NOW
2. **Direct observation** — Claude runs test, shows result
3. **Recent logs** — Last 5 minutes, not yesterday
4. **Test results** — CI/CD pipeline output
5. **Documentation** — If updated recently
6. **Claude assertion** — Last resort, lowest trust

**DO NOT rely on:**
- "It should work"
- "According to the docs"
- "I think it's probably..."
- "This is usually..."
- Assumptions

---

## Integration with [[REALITY]] Doc

**The [[REALITY]] document is the canonical source-of-truth.**

Every claim Claude makes should be verifiable against [[REALITY]]:

```
[[CLAUDE_CLAIM]]
    ↓
[[REALITY_CHECK]]
    ↓
[Match? ✓ or ✗]
    ↓
[Update [[REALITY]] if drift found]
```

---

## Examples

### Example 1: API Status
```
Claude says: "The API is running"

Verification:
$ curl http://100.87.214.70:3004/health
→ {"status":"ok", "timestamp":"2026-10-02T23:50:00Z"}

Result: ✅ VERIFIED (0.95 confidence)
```

### Example 2: Bug Fix
```
Claude says: "Fixed the login crash"

Verification:
$ npm test -- --grep "login"
→ 15 passing (was 14 failing)
$ git log -1
→ Commit: "fix: prevent null ref in login"
$ curl http://staging/login
→ Form loads, no errors in console

Result: ✅ VERIFIED (0.85 confidence)
Note: Still needs production verification
```

### Example 3: Deployment
```
Claude says: "Deployed to production"

Verification:
$ curl https://app.example.com/api/version
→ {"version":"1.2.3", "deployed":"2026-10-02T23:30:00Z"}
$ gcloud app instances --project=prod
→ [3 instances running, traffic healthy]

Result: ✅ VERIFIED (0.92 confidence)
```

### Example 4: False Claim (Caught)
```
Claude says: "Database migration succeeded"

Verification attempt:
$ psql -c "SELECT COUNT(*) FROM users;"
→ ERROR: relation "users" does not exist

Result: ❌ FAILED (0.0 confidence)
Correction: Migration did NOT complete
```

---

## Rules for Claude in Company Brain

1. **Always verify before claiming success** — Run the test, show the result
2. **Distinguish certainty levels** — "Probably works" ≠ "Verified"
3. **Admit unknowns** — "This is uncertain because..."
4. **Check drift** — When reality differs from claim, update [[REALITY]]
5. **Audit everything** — Log to Neo4j with SHA256
6. **Test in production-like environment** — Staging ≠ production
7. **Keep [[REALITY]] current** — Update it immediately on verification

---

## When Claude Gets It Wrong

```
Claude: "The backup is complete"
Reality: Backup process crashed at 50%

Expected response:
1. Acknowledge discrepancy
2. Show evidence of failure
3. Update [[REALITY]]
4. Propose correction
5. Escalate if needed

NOT: "It should be working" or "Let me try again"
```

---

**Canonical source:** [[CLAUDE_MASTER_ONTOLOGY]]  
**Related:** [[REALITY]] [[WHERE_WE_ARE]] [[OMNIROUTE_MASTER_ONTOLOGY]]  
**Operating principle:** Verify, don't assume.

