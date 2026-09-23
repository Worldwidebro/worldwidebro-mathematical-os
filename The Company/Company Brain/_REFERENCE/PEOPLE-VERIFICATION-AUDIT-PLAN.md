# PEOPLE VERIFICATION AUDIT PLAN

**Date:** 2026-09-23  
**Owner:** CP-027 (Infrastructure)  
**Timeline:** Sep 23–30 (parallel with BASE-009/012/014 instantiation)  
**Goal:** Verify all [TO_VERIFY] entries in PEOPLE-REGISTRY + fill gaps

---

## PHASE 1A: 3 REVENUE-READY VENTURES (4 hours)

### OPS-001 (Staffing) — URGENT

**What to find:**
- [ ] Founder/CEO name
- [ ] Founder/CEO email
- [ ] Founder/CEO phone
- [ ] Operations manager (if different from founder)
- [ ] Finance contact

**Where to look:**
- `Worldwidebro/ops-001-ace-construction/README.md` (or similar)
- `CLAUDE.md` in venture directory
- `.github/CODEOWNERS`
- Vercel deployment settings

**Update:**
- PERSON-019 → Update with real name
- PEOPLE-REGISTRY.yaml → status = PENDING_VERIFICATION
- RESPONSIBILITY-MATRIX.csv → Link to OpCo-014 (Staffing OpCo)

**Evidence to collect:**
- [ ] Screenshot of README founder line
- [ ] GitHub commit history (who owns the repo)
- [ ] Deployment project settings

---

### LT-005 (Medical Courier) — URGENT

**What to find:**
- [ ] Founder/CEO name
- [ ] Founder/CEO email
- [ ] Operations manager
- [ ] Finance contact

**Hint:** Likely "Ace Bless" based on email patterns (winnerscirclewcllc@gmail.com)

**Where to look:**
- `Worldwidebro/lt-005-medical-courier-dispatch/README.md`
- `CLAUDE.md`
- git commit author info
- Make.com scenario (if wired)

**Update:**
- PERSON-020 → Update with real name
- PEOPLE-REGISTRY.yaml → status = PENDING_VERIFICATION
- RESPONSIBILITY-MATRIX.csv → Link to OpCo-009 (Logistics)

**Evidence to collect:**
- [ ] GitHub contributor list
- [ ] Make.com scenario ownership
- [ ] Supabase project settings

---

### CALLCENTER — URGENT

**What to find:**
- [ ] Founder/CEO name
- [ ] Founder/CEO email
- [ ] CTO (if Twilio setup requires one)

**Where to look:**
- `Worldwidebro/callcenter-*/README.md`
- Vercel project settings
- Twilio account (who owns the workspace)

**Update:**
- PERSON-021 → Update with real name
- PEOPLE-REGISTRY.yaml → status = PENDING_VERIFICATION

---

## PHASE 1B: 50 VENTURE REPOS (8 hours)

### Sampling Strategy

**Tier 1 (Quick wins — ~15 ventures, 2 min each):**
- Search for obvious founder names in README
- Extract: name, GitHub handle
- [Search Pattern](Command line):
  ```
  grep -i "founder\|creator\|ceo\|built by" README.md
  ```

**Tier 2 (Moderate effort — ~20 ventures, 5 min each):**
- Read full README + CLAUDE.md
- Check `.github/CODEOWNERS`
- Extract from git history: `git log --all --format=%an | sort | uniq -c | sort -rn`

**Tier 3 (Detailed investigation — ~15 ventures, 10 min each):**
- No obvious information in README
- Check Vercel project settings
- Check GitHub org membership
- Infer from commit patterns

---

### Repository Audit Template

```bash
# For each repo:
cd /path/to/venture/repo

# 1. Check README for founder
grep -i "founder\|creator\|ceo" README.md | head -5

# 2. Check CLAUDE.md for person names
grep -i "founder\|ceo\|name\|author" CLAUDE.md | head -5

# 3. Check CODEOWNERS
cat .github/CODEOWNERS 2>/dev/null || echo "No CODEOWNERS"

# 4. Check top contributors
git log --all --format=%an | sort | uniq -c | sort -rn | head -5

# 5. Check most recent commits
git log --oneline -20 | head -5
```

---

## PHASE 1C: FAMILY OFFICE CORE (2 hours)

**What to find:**
- [ ] Actual Family Office CEO name
- [ ] Actual CFO name
- [ ] Actual COO name
- [ ] Actual CIO name
- [ ] Actual Trustee name
- [ ] Actual Trust Protector name

**Where to look:**
- Family office organizational chart (if exists)
- Personal contacts
- Legal documents (trust agreement, appointment letters)
- Email signature blocks (if forwarded)

**Update:**
- PERSON-003 through PERSON-009 → Fill with real names
- PEOPLE-REGISTRY.yaml → status = PENDING_VERIFICATION
- Request formal confirmation via email

---

## PHASE 1D: EXTERNAL ADVISORS (2 hours)

**What to find:**
- [ ] Estate planning attorney name + firm
- [ ] Corporate attorney name + firm
- [ ] CPA/tax advisor name + firm
- [ ] Banker name + bank
- [ ] Insurance broker name + firm

**Where to look:**
- Personal records
- Email footers (forwarded emails)
- Legal document headers
- Bank statements
- Insurance policy declarations

**Update:**
- PERSON-010 through PERSON-018 → Fill with real names
- PEOPLE-REGISTRY.yaml → status = PENDING_VERIFICATION
- Mark as ADVISORY roles (may need consent to list)

---

## DATA STRUCTURE FOR AUDIT

### Spreadsheet to track progress:

```
person_id,current_name,new_name,source,confidence,status,notes
PERSON-001,[FOUNDER NAME],TBD,TO_VERIFY,0%,UNKNOWN,
PERSON-019,[OPS-001 FOUNDER],TBD,GitHub repo README,95%,PENDING_VERIFICATION,Likely Ace Bless
PERSON-020,[LT-005 FOUNDER],TBD,Make.com scenario,90%,PENDING_VERIFICATION,Email pattern suggests Ace
...
```

### Update workflow:

```
1. Find data → Add to tracking sheet
2. Collect evidence (screenshot/link)
3. Validate confidence (>80% to proceed)
4. Send verification email to person (if external)
5. Update PEOPLE-REGISTRY.yaml
6. Update RESPONSIBILITY-MATRIX.csv
7. Mark status: PENDING_VERIFICATION → (VERIFIED or NEEDS_FOLLOW_UP)
```

---

## GAPS TO IDENTIFY

### Use RESPONSIBILITY-MATRIX to find unfilled roles:

```
entity_id,role_id,status
OpCo-001,ROLE-GENERAL-MANAGER,[EMPTY] ← GAP
OpCo-002,ROLE-GENERAL-MANAGER,PERSON-005
OpCo-003,ROLE-GENERAL-MANAGER,[EMPTY] ← GAP
```

**For each gap:**
1. Document which entity + which role is missing
2. Classify: UNFILLED vs UNKNOWN (we don't know who but someone must exist)
3. If UNFILLED: Assign task "Hire/appoint [role] for [entity]"
4. If UNKNOWN: Mark for follow-up "Who is actually the [role] for [entity]?"

---

## OUTPUT: VERIFICATION REPORT

**By Oct 1:**

```yaml
verification_status:
  people_verified: "18 / 50" (36%)
  people_pending_verification: "32 / 50" (64%)
  people_unfilled: "5 / 50" (10%)
  
  ventures_audited: "45 / 789" (6%)
  founders_identified: "38 / 45" (84%)
  
  gaps_identified:
    missing_people: 8
    missing_roles: 12
    missing_evidence: 15
  
  next_actions:
    - Follow up with 32 pending people
    - Complete 744 venture audits (parallel effort)
    - Assign missing roles
    - Collect evidence documents

  timeline:
    - Oct 1-6: Priority verification (revenue ventures + core team)
    - Oct 7-31: Scaling (remaining 744 ventures + roles)
    - Nov 1-30: Evidence collection + legal verification
```

---

## CRITICAL: DON'T RUSH

**Guidelines:**
- ✅ Do publish findings (even partial) → Agents can use partial data
- ✅ Do mark status clearly (UNKNOWN / PENDING / VERIFIED)
- ❌ Don't guess (if uncertain, mark [TO_VERIFY])
- ❌ Don't publish without consent (for external advisors, ask first)
- ✅ Do track evidence (screenshot/link to proof)

---

## TOOLS FOR THIS WORK

### Command-line audit tools:
```bash
# Find repos
find ~/Documents/The\ Company -type d -name "*ops-001*" -o -name "*lt-005*"

# Search for names in files
grep -r "founder\|ceo\|created by" ~/path/to/ventures --include="*.md" --include="*.yaml"

# Extract from git
cd /path/to/repo && git log --all --format=%an | sort | uniq -c | sort -rn

# Quick PEOPLE-REGISTRY check
grep "TO_VERIFY" _REGISTRIES/CANONICAL/PEOPLE-REGISTRY.yaml | wc -l
```

### CSV tools:
```bash
# Sort RESPONSIBILITY-MATRIX by status (gaps first)
sort -t',' -k9 _REGISTRIES/CANONICAL/RESPONSIBILITY-MATRIX.csv | grep -i empty

# Count gaps
grep -i "empty\|\[to_verify\]" _REGISTRIES/CANONICAL/RESPONSIBILITY-MATRIX.csv | wc -l
```

---

## SUCCESS CRITERIA

### By Sep 27:
- [ ] 3 revenue ventures fully verified (PERSON-019, PERSON-020, PERSON-021)
- [ ] 50 venture repos sampled
- [ ] Family office core team identified (PERSON-001 through PERSON-009)
- [ ] At least 5 external advisors named

### By Oct 1:
- [ ] 18+ people moved to PENDING_VERIFICATION status
- [ ] 25+ gaps documented in RESPONSIBILITY-MATRIX
- [ ] Verification report drafted

### By Oct 6:
- [ ] 18+ people moved to VERIFIED status
- [ ] Gap resolution plan created
- [ ] Agent routing tests passing

---

## WHO DOES THIS?

**Option A:** You (manually audit repos + send verification emails)  
**Option B:** Agent to assist (provide repo list + do automated search + compile results)  
**Option C:** Hybrid (Agent finds candidates, you verify + send emails)

**Recommended:** Hybrid approach
- Agent searches 789 repos for "founder" keyword
- Compiles top candidates with confidence scores
- You verify top 50 + send confirmation emails
- Updates feed back into PEOPLE-REGISTRY

---

**Start:** Now (Sep 23)  
**Completion:** Oct 6 (Phase 1A complete)  
**Ongoing:** Oct 7+ (continuous verification as agents discover new people)

Commit: 5af7f6e4
