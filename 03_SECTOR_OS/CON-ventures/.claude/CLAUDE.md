# CON.md — Construction Sector Configuration

**Scope:** Build/test/deploy + handoff rules for all CON ventures.  
**Sector:** Construction | **ID:** `CON`  
**Ventures:** 15 live (CON-001 active)  
**Status:** P1 (Speed to Lead) active  
**Updated:** 2026-07-27

---

## Build/Test/Deploy

### Build
```bash
git clone https://github.com/worldwidebro/con-ventures.git
cd con-ventures
npm install  # or: python3 -m venv .venv && pip install -r requirements.txt
cp .env.example .env  # Fill: SUPABASE_URL, STRIPE_KEY, TWILIO_KEY
npm run migrate
npm run dev
```

### Test
```bash
npm test && npm run test:integration
npm run verify:ready  # Checks Supabase, Stripe, Twilio connectivity
curl -X POST http://localhost:3000/api/leads/intake -d '{"venture_id":"CON-001","lead_name":"Test"}'
```

### Deploy (CON-001)
```bash
venture CON-001  # Activate context
git checkout -b con/con-001/feature-name
# make changes + test
git push origin con/con-001/feature-name
gh pr create --title "CON-001: ..."
# After merge: vercel deploy --prod
# Update VENTURE-READINESS-SCORECARD.csv
```

---

## Handoff Rules

**✅ Stay in CON if:** Working on CON ventures (CON-001, etc.) or P1/P7/P10/P14 features for construction.

**🔵 Cross-sector if:** CON data flows to RE (valuation), LOG (supply), or FIN (ROI):
- Post to Slack `#sector-dependencies`
- Update Supabase `venture_dependencies` table
- Notify downstream sector team

**🚨 Platform if:** Changes to n8n, Neo4j, Qdrant, or Langfuse:
- Update root `.claude/CLAUDE.md`
- Notify all 4 sectors

---

## Quick APIs

```bash
# P1 - Lead Intake
POST /api/leads/intake
{"venture_id":"CON-001","lead_name":"John","project_type":"Residential","budget":"$2.5M"}

# P7 - RFP Response  
POST /api/rfps/respond
{"venture_id":"CON-001","rfp_text":"[...RFP...]"}
```

---

## Cross-Sell Goldmine

CON-001 pays $497/mo for P1 → Unlock:
- RE: +$997/mo (Dynamic Pricing)
- LOG: +$700/mo (Receptionist)
- FIN: +$897/mo (RFP Responder)
- **Total: $2,594/mo per CON venture**

---

## Known Issues

- ⚠️ Twilio SMS not configured (needs TWILIO_API_KEY)
- ⚠️ Stripe webhook needs whitelist: con-ventures.vercel.app/api/webhooks/stripe

---

**Generated:** 2026-07-27 | **Version:** 1.0
