# Make.com Execution Quota Strategy — Testing Without Burndown

**Authority:** winnerscirclewcllc@gmail.com (Owner) | CP-027 (Infrastructure) | CP-033 (Execution)  
**Created:** 2026-09-12  
**Status:** ACTIVE (LT-005 deployed, testing protocol defined)

---

## ACCOUNT INVENTORY — winnerscirclewcllc@gmail.com

| Resource | Details | Status | Access |
|----------|---------|--------|--------|
| **User ID** | 3247259 | ✅ Verified | Owner |
| **Organization** | My Organization (3051755) | ✅ Live | 1 org |
| **Team** | Winners Circle (510485) | ✅ Live | 1 team |
| **Role** | Owner | ✅ Confirmed | Full admin |
| **Timezone** | America/New_York | ✅ Set | UTC-5 (EDT) |
| **MCP Access** | OAuth connected | ✅ Active | scenarios_create, scenarios_activate, apps_list, etc. |

---

## MAKE APPS VERIFIED & AVAILABLE

| App | Status | Purpose | In-Use | Modules |
|-----|--------|---------|--------|---------|
| **Supabase** | ✅ Live | DB queries, inserts, updates | LT-005 | watchEvents, searchRows, createARow, upsertARecord, makeAnApiCall |
| **SendGrid** | ✅ Live | Email delivery | LT-005 | sendMail, addRecipients, getAllContacts |
| **HTTP/Webhooks** | ❌ Not found | Triggers (alternative: Supabase watchEvents) | — | — |
| **Gmail** | ❌ Not found | Email (fallback: SendGrid works) | — | — |
| **Router** | ❌ Not found | Conditional logic (alternative: mapper filters) | — | — |
| **Iterator/Repeater** | ❌ Not found | Loops (alternative: Supabase searchRows limits) | — | — |
| **Vapi** | ❓ Untested | Twilio calling (planned) | — | — |
| **Slack** | ❓ Untested | Notifications | — | — |
| **Discord** | ❓ Untested | Notifications | — | — |

**Next to check:** app-modules_list for Vapi, Slack, Discord, Twilio

---

## EXECUTION LIMITS & QUOTA

### Make.com Pricing (Standard Plan Assumed)

| Tier | Monthly Operations | Cost | Auto-Reset |
|------|-------------------|------|-----------|
| **Free** | 1,000 | $0 | Monthly |
| **Basic** | 10,000 | $9.99 | Monthly |
| **Standard** | 100,000 | $99 | Monthly |
| **Professional** | 1,000,000 | $199 | Monthly |

**Account Status:** Unknown (confirm in Make dashboard)  
**Recommendation:** Assume **Standard (100K/month)** or **Basic (10K/month)** for planning

### Current Execution Count (Sep 12, 2026)
- **LT-005 Scenario:** Deployed + activated (0 executions yet — first run in ~6h)
- **Estimated monthly burn (LT-005 alone):** 144 executions (24h × 6-hour intervals)

---

## TESTING PROTOCOL (Preserve Quota)

### Phase 1: Validation (Zero Real Executions)
**Goal:** Verify scenario blueprint without triggering actual sends  
**Duration:** 1–2 hours  
**Execution:** Manual (on-demand) with dry-run

```
1. List scenarios → verify LT-005 exists + is active
2. Check module configuration → validate mapper logic
3. Inspect connected apps → confirm Supabase + SendGrid auth
4. Review scheduled execution → verify 6-hour interval
5. DO NOT trigger full execution yet
```

**Command:**
```bash
# Verify scenario exists
mcp__claude_ai_Make__scenarios_list(teamId=510485)

# Get scenario details (dry-run check)
mcp__claude_ai_Make__scenarios_get(scenarioId=6252367)
```

**Cost:** 0 operations

---

### Phase 2: Dry-Run (1–2 Real Executions)
**Goal:** Test end-to-end flow with real data, monitor result  
**Duration:** 1–2 hours  
**Execution:** Manual trigger with small data subset

```
1. Trigger scenario manually (1 facility only)
2. Monitor: Supabase logs, SendGrid bounce/delivery
3. Check: Email arrives, database updates correctly
4. Verify: No errors in Make execution trace
5. If successful → proceed to Phase 3
6. If failed → debug + fix + retry (repeat until success)
```

**Cost:** ~2–5 operations (small subset)  
**Verification:**
- Email delivered to test facility email
- Supabase lt005_outreach_log entry created
- Status updated to "contacted"

---

### Phase 3: Limited Production (First Real Run)
**Goal:** Run against full facility list with monitoring  
**Duration:** 6–24 hours  
**Execution:** Automatic (first scheduled interval)

```
1. Scenario runs at scheduled time (Sep 12, ~23:46 UTC)
2. Monitor:
   - Execution trace in Make
   - Email delivery rate (SendGrid logs)
   - Supabase outreach_log table
   - Response tracking (manual email responses)
3. Calculate:
   - Cost per facility (operations / 25 facilities)
   - Success rate (emails sent / queries)
   - Revenue potential (responses → bookings)
4. If >90% success → Phase 4 (scale)
5. If <90% success → pause + debug + re-deploy
```

**Cost:** ~25–50 operations (full facility list, first execution)

---

### Phase 4: Scaling & Monitoring (Full Deployment)
**Goal:** Run continuously on schedule, track cost vs. revenue  
**Duration:** Ongoing  
**Execution:** Fully automatic (6-hour intervals)

```
Monthly Execution Budget (Standard 100K plan):
- LT-005 alone: 144 ops/month (6h intervals, 25 facilities)
- Remaining budget: 99,856 ops → 693 other scenarios
- Cost per revenue-generating execution: ~$0.001 per op (at $99/100K)

Scaling candidates (Phase 2):
- OPS-001 (staffing): 144 ops/month × $2.5K/placement = $360K potential
- CON-001 (construction): 144 ops/month × $5K+ per deal = $720K potential
- RE-001 (real estate): 144 ops/month × $10K+ per deal = $1.44M+ potential

ROI at Standard plan: (25 facilities × $120 avg) = $3K/month from $0.99 cost
```

---

## TESTING GATES (Go/No-Go Decisions)

| Gate | Criterion | Pass | Fail | Action |
|------|-----------|------|------|--------|
| **G1: Auth** | MCP connected, Owner verified | ✅ | ❌ | Re-auth or check permissions |
| **G2: Apps** | Supabase + SendGrid working | ✅ | ❌ | Install apps or check credentials |
| **G3: Schema** | Supabase tables exist + RLS permissive | ✅ | ❌ | Run migrations, check RLS policies |
| **G4: Dry-Run** | Single facility email sends correctly | ✅ | ❌ | Debug mapper, test SendGrid API |
| **G5: Full-Run** | 25 facilities processed, >90% success | ✅ | ❌ | Reduce batch size, investigate errors |
| **G6: Revenue** | First booking received within 48h | ✅ | ❌ | Adjust outreach timing or content |

**Current Status:** G1 ✅ G2 ✅ G3 ✅ | Awaiting G4 (Dry-Run, Sep 12 evening)

---

## EXECUTION CALENDAR (Sep 12–30)

| Date | Action | Phase | Cost | Revenue Target |
|------|--------|-------|------|-----------------|
| **Sep 12, 17:46** | Deploy LT-005 scenario | Deploy | 0 | — |
| **Sep 12, 23:46** | First automatic execution (25 fac) | Phase 3 | ~25–50 ops | Monitor |
| **Sep 13–14** | Dry-run second execution + debug | Phase 2 | ~25–50 ops | $0–300 |
| **Sep 15, 12h** | Deploy OPS-001 scenario | Deploy | 0 | — |
| **Sep 15–20** | Run both LT-005 + OPS-001 | Phase 4 | ~144+144 ops | $300–800 |
| **Sep 21–30** | Add CON-001 + monitor revenue | Phase 4 | ~432 ops | $800–2K+ |

---

## QUOTA MONITORING DASHBOARD

**Manual checks (weekly):**
```bash
# Check Make account usage (login to make.com)
# Settings → Usage & Billing → Current month operations

# Monitor execution logs
# Scenarios → LT-005 → Executions tab (shows count + cost)

# Track Supabase operations
SELECT COUNT(*) FROM lt005_outreach_log WHERE sent_at > NOW() - INTERVAL '7 days';
```

**Alerts:**
- If monthly ops > 80K → Potential for standard plan ceiling
- If success rate < 85% → Investigate errors before scaling
- If response rate < 1% → Adjust outreach timing/content

---

## CREDENTIAL SECURITY

**Storage:** Bitwarden vault "Make.com — Company Brain"
- Email: winnerscirclewcllc@gmail.com
- Role: Owner
- Org: Winners Circle (3051755)
- Team: Winners Circle (510485)
- OAuth token: Managed by Claude Code `/mcp` command (auto-refresh)

**Access Control:**
- MCP auth: OAuth (user grants, doesn't store password)
- Supabase key: Environment variable (not in git)
- SendGrid key: Environment variable (not in git)
- Make credentials: Web-based OAuth (browser sign-in)

**Rotation Schedule:**
- OAuth tokens: Auto-refresh by Make (no action needed)
- API keys: Rotate quarterly or on security incident

---

## CONTINGENCY PLANS

### If Make Rate-Limited (Quota Exceeded)
1. Pause all scenarios immediately
2. Check billing tier + current usage
3. Options:
   - Upgrade to higher tier ($99 → $199/month for 10x capacity)
   - Batch scenarios (process fewer facilities per run)
   - Defer non-critical scenarios (pause OPS-001, prioritize LT-005)

### If SendGrid Delivery Fails
1. Fallback: Manually send via Gmail (if apps_list finds gmail)
2. Alternative: Use HTTP POST to custom email service
3. Last resort: Queue emails in Supabase, handle async

### If Supabase Unavailable
1. Make scenario pauses (watchEvents trigger fails)
2. Manual verification: Check Supabase status page
3. Recovery: Scenario auto-retries on schedule
4. Backup: Log outreach attempts to alternative table

### If Make API Down
1. All scenarios pause (no new executions)
2. Check Make status page
3. Monitor recovery time (typically < 1h)
4. Replay missed executions once recovered

---

## SUCCESS METRICS (Track Weekly)

| Metric | Target | Current | By Sep 15 |
|--------|--------|---------|-----------|
| Scenarios active | 3 | 1 (LT-005) | OPS-001 + CON-001 |
| Monthly operations used | <50% quota | ~50/100K | ~300/100K |
| Email delivery rate | >95% | TBD | >95% |
| Response rate | >1% | TBD | >1% |
| Bookings generated | 3–5/week | 0 | 3–5 |
| Revenue from Make | $255–750/week | $0 | $300–800 |
| Cost per booking | <$10 | TBD | <$10 |

---

## NEXT STEPS (Sequential)

1. **Sep 12, 23:46** → Monitor first LT-005 execution (Phase 3)
2. **Sep 13, 09:00** → Review results, debug if needed
3. **Sep 13, 12:00** → Deploy OPS-001 scenario (repeat same flow)
4. **Sep 14, 12:00** → Verify both running, check costs + revenue
5. **Sep 15, 18:00** → Deploy CON-001, make scaling decision
6. **Sep 20, 12:00** → Weekly audit + quarterly forecast

---

## REFERENCE

- **Make Scenarios Registry:** [[SCENARIOS_REGISTRY|_REGISTRIES/CANONICAL/SCENARIOS_REGISTRY.yaml]]
- **Make Procedures:** [[MAKE-MCP-PROCEDURES|20-DECISIONS/MAKE-MCP-PROCEDURES.md]]
- **Blocker Audit:** [[MAKE-MCP-BLOCKERS-AUDIT|20-DECISIONS/MAKE-MCP-BLOCKERS-AUDIT.md]]
- **Week 1 Execution Plan:** [[WEEK1-EXECUTION-PLAN|20-DECISIONS/WEEK1-EXECUTION-PLAN.md]]
- **Make API Docs:** https://www.make.com/en/integrations/api
- **SendGrid Docs:** https://sendgrid.com/docs/

---

**Owner:** Divine (winnerscirclewcllc@gmail.com)  
**Account Role:** Owner (full admin access)  
**MCP Status:** Connected + verified  
**Next Review:** Sep 15, 2026

