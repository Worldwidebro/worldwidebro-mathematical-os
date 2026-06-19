# 🧪 REAL DEAL SIMULATION — Charlotte Water Damage Restoration

**Scenario:** Water damage in Charlotte, NC | Insurance-backed | $28,500 scope  
**Timeline:** Complete flow from lead → payment → reputation update  
**System:** CON-022 (Insurance Restoration) | 11-day execution | 100% automated

---

## STEP 1: DEAL INTAKE (Hour 0:00)

Insurance claim comes in. System classifies as CON-022.

```bash
curl -X POST http://localhost:8001/mcp/tools/submit_referral \
  -d '{"contact_id":"insurer_allstate_charlotte","job_title":"Water Damage","budget":28500,"timeline":"urgent","sector":"CON-022"}'
```

**Response:** Deal CON-022-10491 created. Score: 82/100. Profit: $6,840.

---

## STEP 2: CONTRACT GENERATION (Hour 0:15)

System auto-generates 4 contracts:
- Client Authorization (insurance assignment)
- Contractor Agreement ($19,800 labor)
- Referral Agreement (10% = $2,850)
- Platform Terms (12% = $3,420)

All contracts ready for signing.

---

## STEP 3: SIGNATURES + FUNDING (Hour 1:00)

- Allstate signs: 6 min ✅
- Contractor signs: 18 min ✅
- Referral confirms: 4 min ✅
- 30% released: $8,550 ✅

---

## STEP 4: CONTRACTOR ASSIGNMENT (Hour 1:30)

System selects:
- Charlotte Elite Drywall (Score: 91/100, S-tier)
- Charlotte Flooring Pros (Score: 88/100, A-tier)
- Licensed Electric (Score: 84/100, A-tier)

All auto-assigned. Notifications sent.

---

## STEP 5: DISPATCH + SCHEDULE (Hour 2:00)

n8n creates 11-day execution plan:
- Day 1: Inspection
- Days 2-4: Demolition
- Days 5-10: Rebuild
- Day 11: Final inspection + closeout

---

## STEP 6: EXECUTION TRACKING (Days 1-11)

Field crews update via CompanyCam/Fieldwire:
- Day 1: 5% complete (inspection done)
- Days 2-4: 30% complete (demolition on track)
- Days 5-10: 72% complete (rebuild in progress)
- Day 11: 100% COMPLETE ✅

---

## STEP 7: PAYMENT DISTRIBUTION (Day 11, Hour 14:00)

```json
{
  "splits": [
    {"contractor": 19800},
    {"materials": 3200},
    {"referral": 2850},
    {"platform": 3420}
  ]
}
```

All payments routed automatically via Stripe/ACH.

---

## STEP 8: REPUTATION UPDATE (Day 11, Hour 15:00)

Charlotte Elite performance:
- Quality: 94/100
- Speed: 96/100
- Compliance: 100/100
- **New Score: 95.5/100 → S-TIER** ✅

Promoted from A-tier. Flagged for premium projects.

---

## STEP 9: FINAL STATE

- Total Revenue: $28,500
- Platform Profit: $3,420
- Cycle Time: 11 days
- Quality: 95.5/100
- Next Deal Forecast: 8 similar deals in 30 days

**System: 100% automated. Zero manual steps.**

