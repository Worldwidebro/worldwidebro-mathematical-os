# Gaps & Blockers

## Critical (Blocks Revenue)

| Gap | Fix Time | Status |
|-----|----------|--------|
| Real Supabase data ingestion | 1 day | ⏳ supabase_loader.py written, not tested |
| Real Neo4j carrier graph | 4 hours | ⏳ seed_carriers.cypher written, needs load |
| Stripe payment integration | 1 day | ❌ missing |
| VAPI voice inbound | 2 days | ❌ missing |
| SMS notifications | 4 hours | ❌ missing |

## Major (Blocks Operations)

| Gap | Fix Time | Status |
|-----|----------|--------|
| ClickUp task creation | 1 day | ❌ API stub only |
| Slack alerts | 2 hours | ❌ missing |
| Driver app (mobile job board) | 3 days | ❌ missing |
| Client portal (real-time tracking) | 1 day | ⏳ WebSocket skeleton |
| Admin dashboard | 1 day | ⏳ health_check.py, no UI |

## Medium (Blocks Scale)

| Gap | Fix Time | Status |
|-----|----------|--------|
| Multi-tenant principal | 1 day | ⏳ scheduler.py, needs config |
| Load balancing / HA | 1 day | ❌ single instance only |
| Rate limiting | 4 hours | ❌ missing |
| Audit logging | 1 day | ⏳ Langfuse connected, incomplete |
| CI/CD pipeline | 2 days | ❌ missing |

## Working ✅

- Dispatch workflow engine (7 phases)
- Principal enforcer (goal checking)
- API skeleton (FastAPI routes)
- Scheduler framework (5 jobs)
- Call center portal UI
- Update flows skeleton

---

## Build to First $1K Revenue

1. **Seed Real Carriers** (4 hrs) — add 5 NC carriers to Neo4j
2. **Wire Supabase** (1 day) — fetch loads, mark COMPLETED
3. **Stripe Invoicing** (1 day) — create invoice, webhook on payment
4. **SMS Notifications** (4 hrs) — Twilio alerts to carrier + shipper
5. **First Load** (1 day) — end-to-end test with real shipper

**Total: 3-4 days → revenue**

---

## Run Full Stack Now

```bash
# Terminal 1: Scheduler (principal checks every 5 min)
python scheduler.py

# Terminal 2: API server
python api_routes.py

# Terminal 3: VEX frontend
cd vex-hero-site && npm run dev

# Terminal 4: Wire Supabase (fetch real loads)
python main_wired.py
```

Verify: Supabase load → engine → billing → call center.
