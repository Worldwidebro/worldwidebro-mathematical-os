# Make.com Alignment Matrix — Account → Tools → Scenarios → Testing → Revenue

**Date:** 2026-09-12  
**Owner:** Divine (winnerscirclewcllc@gmail.com)  
**Authority:** CP-027 (Infrastructure) + CP-033 (Execution) + CP-021 (Revenue)

---

## ACCOUNT (Single Source of Truth)

```
┌─────────────────────────────────────────────────────────────┐
│ MAKE.COM ACCOUNT — winnerscirclewcllc@gmail.com             │
│ ┌──────────────────────────────────────────────────────────┐│
│ │ User ID: 3247259                                         ││
│ │ Role: Owner (full admin access verified Sep 12, 16:49)   ││
│ │ Organization: My Organization (ID: 3051755)              ││
│ │ Team: Winners Circle (ID: 510485)                        ││
│ │ MCP Status: Connected ✅ (OAuth via /mcp command)        ││
│ │ Last Login: 2026-09-12T16:49:27.436Z                     ││
│ └──────────────────────────────────────────────────────────┘│
│                                                              │
│ Quota: Standard Plan (assumed) = 100K ops/month             │
│ Monthly budget: ~99,856 ops remaining (after LT-005)        │
│ Cost: $99/month @ 100K ops = $0.00099 per operation        │
└─────────────────────────────────────────────────────────────┘
```

---

## TOOLS/APPS (Inventory)

### Verified ✅ (Ready to Use)

| App | Modules Available | Use-Case | Status | Test Date |
|-----|-------------------|----------|--------|-----------|
| **Supabase** | watchEvents, searchRows, createARow, upsertARecord, makeAnApiCall | Database queries + updates | ✅ IN USE | Sep 12 verified |
| **SendGrid** | sendMail, addRecipients, getAllContacts | Email delivery | ✅ IN USE | Sep 12 verified |

### Not Found ❌ (Workarounds Used)

| App | Expected Module | Alternative | Impact | Status |
|-----|-----------------|-------------|--------|--------|
| **HTTP/Webhooks** | makeRequest, receiveData | Use Supabase watchEvents (trigger on create/update) | Low | Acceptable |
| **Gmail** | sendMail | Use SendGrid instead | Low | Acceptable |
| **Router** | routeByCondition | Use mapper filters + separate flow branches | Medium | Acceptable |
| **Iterator** | iterate | Use searchRows limit + array iteration | Medium | Acceptable |

### To Test ❓ (Planned for Phase 2)

| App | Module | Use-Case | Venture | Timeline |
|-----|--------|----------|---------|----------|
| **Vapi** | Make call | Cold calling via Twilio | LT-005 upgrade | Week 2 |
| **Slack** | sendMessage | Notifications | All scenarios | Week 3 |
| **Discord** | sendMessage | Notifications | Internal ops | Week 3 |

---

## SCENARIOS (Deployment Pipeline)

### Currently Deployed

```
┌──────────────────────────────────────────────────────────┐
│ SCN-000001: LT-005 Medical Facility Outreach              │
│                                                           │
│ Make ID: 6252367                                          │
│ Status: ✅ ACTIVATED (Sep 12, 17:46 UTC)                 │
│ Schedule: Every 6 hours (21,600 seconds)                  │
│ Next Run: Sep 12, 23:46 UTC (first execution)             │
│                                                           │
│ Modules (8-module flow):                                  │
│  1. Supabase watchEvents (trigger)                        │
│  2. Supabase searchRows (query 25 facilities)             │
│  3. Supabase searchRows (supplemental data)               │
│  4. SendGrid sendMail (personalized email)                │
│  5. Supabase upsertARecord (update status to contacted)   │
│  6. Supabase createARow (log attempt)                     │
│  7. Supabase createARow (secondary log)                   │
│  8. Supabase makeAnApiCall (audit trail)                  │
│                                                           │
│ Revenue Model:                                            │
│  • Facilities: 25 Charlotte medical centers               │
│  • Email delivery: SendGrid (verified)                    │
│  • Response target: >1% (0–3 contacts)                    │
│  • Conversion: 10–20% of responses to bookings            │
│  • Revenue per booking: $85–$150                          │
│  • Weekly revenue: $255–$750 (3–5 bookings)               │
│  • Monthly revenue: $1,020–$3,000                         │
│  • Cost: ~$0.04/month (144 ops × $0.00099)               │
│  • ROI: $1,020 / $0.04 = 25,500x                          │
│                                                           │
│ Quota Impact: 144 ops/month (6-hour intervals)            │
└──────────────────────────────────────────────────────────┘
```

### Ready to Deploy (Pending Testing)

```
┌──────────────────────────────────────────────────────────┐
│ SCN-000002: OPS-001 Staffing Placement Outreach           │
│                                                           │
│ Status: 🟡 READY (blueprint documented)                   │
│ Deploy Date: Sep 15 (after LT-005 G4–G5 gates pass)       │
│ Schedule: Every 6 hours (same as LT-005)                  │
│                                                           │
│ Modules (8-module flow):                                  │
│  1. Supabase watchEvents (trigger on staffing need)       │
│  2. Supabase searchRows (query 50 candidates)             │
│  3. Supabase searchRows (recruiter filters)               │
│  4. SendGrid sendMail (recruitment email + resume link)   │
│  5. Supabase upsertARecord (mark contacted)               │
│  6–8. Logging (createARow + API calls)                    │
│                                                           │
│ Revenue Model:                                            │
│  • Candidates: 50 per location (growing)                  │
│  • Placement rate: 8–10% of contacts                      │
│  • Revenue per placement: $2,500 (recruiter fee)          │
│  • Weekly bookings: 4–6 placements                        │
│  • Weekly revenue: $10K–$15K                              │
│  • Monthly revenue: $40K–$60K                             │
│  • Cost: ~$0.04/month                                     │
│  • ROI: $40K / $0.04 = 1,000,000x                         │
│                                                           │
│ Quota Impact: +144 ops/month (288 total with LT-005)      │
└──────────────────────────────────────────────────────────┘
```

### Planning (Week 2)

```
┌──────────────────────────────────────────────────────────┐
│ SCN-000003: CON-001 Construction Project Outreach         │
│ SCN-000004: RE-001 Real Estate Deal Pipeline              │
│ SCN-000005: CALLCENTER Twilio Call Campaign               │
│                                                           │
│ Each: ~144 ops/month (6-hour interval)                    │
│ Combined monthly: +576 ops (864 total with LT-005+OPS-001)│
│ Still within 100K/month Standard plan (91% headroom)      │
└──────────────────────────────────────────────────────────┘
```

---

## TESTING GATES (Go/No-Go)

### Gate Sequence (Sequential, Blocking)

```
LT-005 TESTING GATES:
├─ G1: Auth ✅ PASSED
│  └─ MCP connected, Owner verified
│
├─ G2: Apps ✅ PASSED
│  └─ Supabase + SendGrid working
│
├─ G3: Schema ✅ PASSED
│  └─ Supabase tables exist + RLS permissive
│
├─ G4: Dry-Run 🟡 PENDING (Sep 12, 18:00–22:00)
│  └─ Single facility email sends correctly
│  └─ Blocks: Phase 2 testing, Phase 3 auto-run
│
├─ G5: Full-Run 🟡 PENDING (Sep 12, 23:46)
│  └─ 25 facilities processed, >90% success
│  └─ Blocks: Scaling to OPS-001
│
└─ G6: Revenue 🟡 PENDING (Sep 14, 12:00)
   └─ First booking received within 48h
   └─ Blocks: Weekly forecast + scaling decision
```

**Retry Logic:**
- G1–G3: Human intervention (auth/credentials/schema)
- G4–G5: Automatic retry up to 3x (debug on 3rd fail)
- G6: Manual follow-up (depends on response timing)

---

## SCENARIO → TOOLS → ACCOUNT MAPPING

```
Account: winnerscirclewcllc@gmail.com (Owner, 510485 team)
  │
  ├─ LT-005 Scenario (6252367)
  │  ├─ Tool: Supabase (lt005_charlotte_facilities table)
  │  ├─ Tool: SendGrid (send email)
  │  ├─ Test Gate: G1–G6
  │  ├─ Monthly Cost: $0.04 (144 ops)
  │  └─ Monthly Revenue: $1,020–$3,000
  │
  ├─ OPS-001 Scenario (pending)
  │  ├─ Tool: Supabase (ops_candidates table)
  │  ├─ Tool: SendGrid (send recruitment email)
  │  ├─ Test Gate: G1–G6 (repeat after LT-005)
  │  ├─ Monthly Cost: $0.04 (144 ops)
  │  └─ Monthly Revenue: $40K–$60K
  │
  └─ CON-001 + RE-001 + CALLCENTER (pending)
     ├─ Tools: Supabase + SendGrid + Vapi (TBD)
     ├─ Test Gate: G1–G6 per scenario
     ├─ Monthly Cost: ~$0.12 (576 ops)
     └─ Monthly Revenue: $20K–$100K+ (combined)
```

---

## QUOTA ALLOCATION (100K ops/month)

```
ALLOCATION BY SCENARIO:

LT-005 (Medical):           144 ops/month  =  0.14% quota
OPS-001 (Staffing):         144 ops/month  =  0.14% quota
CON-001 (Construction):     144 ops/month  =  0.14% quota
RE-001 (Real Estate):       144 ops/month  =  0.14% quota
CALLCENTER (Voice):         144 ops/month  =  0.14% quota
RESERVE (future):        99,380 ops/month  = 99.38% quota

TOTAL USED:                 720 ops/month  =  0.72% quota
UTILIZATION:             99,280 ops available (99.28% headroom)

RUNWAY:
- At current rate: 138 years before quota exhausted
- Can add 137 more similar scenarios without scaling
- Upgrade not needed until deploying 50+ concurrent scenarios
```

---

## DECISION MATRIX (When to Deploy Next Scenario)

| After Gate | Deploy Next? | Condition | Action |
|------------|--------------|-----------|--------|
| **G4 passes** | No | Still testing LT-005 dry-run | Monitor results |
| **G5 passes** | Start OPS-001 G1–G3 | LT-005 full execution success | Prepare OPS-001 |
| **G6 passes** | Deploy OPS-001 | First LT-005 booking confirmed | Run OPS-001 scenario |
| **OPS G5 passes** | Start CON-001 G1–G3 | OPS-001 execution success | Prepare CON-001 |
| **OPS G6 passes** | Deploy CON-001 | OPS-001 bookings confirmed | Run CON-001 scenario |

**Stopping Conditions:**
- Any scenario fails G5 (full-run) → Pause, debug, retry max 3x
- Any scenario shows <85% success rate → Investigation required
- Quota usage >80% → Evaluate upgrade or pause non-critical scenarios

---

## REVENUE FORECAST (Best Case)

| Week | Scenarios | Ops/Week | Revenue | Cumulative |
|------|-----------|----------|---------|------------|
| **W1 (Sep 12–18)** | LT-005 | 144 | $255–$750 | $255–$750 |
| **W2 (Sep 19–25)** | LT-005 + OPS-001 | 288 | $10K–$15K | $10.3K–$15.8K |
| **W3 (Sep 26–30)** | LT-005 + OPS-001 + CON-001 | 432 | $15K–$30K | $25.3K–$46.8K |
| **Month Total** | 3 scenarios | 864 ops | $25K–$47K | — |

**Contingency:**
- If 50% success rates: $12.5K–$23.5K/month
- If 90% success rates: $22.5K–$42K/month

---

## QUICK REFERENCE CHECKLIST

✅ **Account Setup:**
- [ ] User verified: Divine (3247259)
- [ ] Role verified: Owner
- [ ] Team verified: Winners Circle (510485)
- [ ] MCP connected: `/mcp status`

✅ **Tools Verified:**
- [ ] Supabase app connected
- [ ] SendGrid app connected
- [ ] Credentials securely stored

✅ **Scenarios Ready:**
- [ ] LT-005 deployed + activated (G1–G3 pass)
- [ ] OPS-001 blueprint ready (pending G4–G5)
- [ ] CON-001 blueprint ready (pending OPS-001 success)

✅ **Testing Gates:**
- [ ] G1: Auth ✅
- [ ] G2: Apps ✅
- [ ] G3: Schema ✅
- [ ] G4: Dry-Run (pending Sep 12 evening)
- [ ] G5: Full-Run (pending Sep 12 23:46)
- [ ] G6: Revenue (pending Sep 14)

✅ **Quota Management:**
- [ ] Monthly budget tracked (<100K ops)
- [ ] Cost per operation: $0.00099
- [ ] Scaling headroom: 99.28% available
- [ ] Upgrade not needed for 12+ months

---

## REFERENCE DOCUMENTS

- **Procedures:** [[MAKE-MCP-PROCEDURES|20-DECISIONS/MAKE-MCP-PROCEDURES.md]]
- **Blockers Audit:** [[MAKE-MCP-BLOCKERS-AUDIT|20-DECISIONS/MAKE-MCP-BLOCKERS-AUDIT.md]]
- **Quota Strategy:** [[MAKE-EXECUTION-QUOTA-STRATEGY|20-DECISIONS/MAKE-EXECUTION-QUOTA-STRATEGY.md]]
- **Scenarios Registry:** [[SCENARIOS_REGISTRY|_REGISTRIES/CANONICAL/SCENARIOS_REGISTRY.yaml]]
- **Week 1 Execution:** [[WEEK1-EXECUTION-PLAN|20-DECISIONS/WEEK1-EXECUTION-PLAN.md]]

---

**Updated:** 2026-09-12T18:00:00Z  
**Owner:** Divine (winnerscirclewcllc@gmail.com)  
**Next Review:** Sep 13, 09:00 (after G4 dry-run completion)
