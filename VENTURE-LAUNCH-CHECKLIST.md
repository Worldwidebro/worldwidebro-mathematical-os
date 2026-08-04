---
title: Venture Launch Checklist
version: 1.0
applies: Every venture launch
---

# Venture Launch Checklist

**Time**: 30 min/venture | **Status**: Ready

---

## Step 1: Venture Metadata

Required:
- VENTURE_ID (CON-001, FIN-042, etc.)
- Name, sector, owner email
- GitHub repo URL
- Stripe account ID

## Step 2: Register in Neo4j

```bash
python3 << 'EOF'
import json, base64, urllib.request
auth = base64.b64encode(b'neo4j:ventures2026').decode('ascii')

cypher = """
MERGE (v:Venture {
  id: $venture_id,
  name: $name,
  sector: $sector,
  owner: $owner,
  github_repo: $repo,
  stripe_id: $stripe,
  created_at: datetime(),
  status: "SETUP"
})
RETURN v.id
"""

payload = {"statements": [{"statement": cypher, "parameters": {
  "venture_id": "YOUR_ID",
  "name": "Your Name",
  "sector": "construction",
  "owner": "user@email.com",
  "repo": "https://github.com/...",
  "stripe": "acct_..."
}}]}

req = urllib.request.Request('http://localhost:7474/db/neo4j/tx/commit',
  data=json.dumps(payload).encode(), method='POST',
  headers={'Content-Type': 'application/json', 'Authorization': f'Basic {auth}'})
with urllib.request.urlopen(req) as r: print("✅ Registered")
EOF
```

## Step 3: Spawn Agents

```bash
python3 spawn-agents.py YOUR_VENTURE_ID
```

Creates: SalesAgent, FinanceAgent, OpsAgent (all TRAINING stage)

## Step 4: Supabase Setup

- [ ] Create project
- [ ] Run `supabase db push`
- [ ] Verify tables (agent_lifecycle, agent_metrics, venture_leads, deal_payments)

## Step 5: Payments

- [ ] Add Stripe keys to `.env`
- [ ] Register webhook: `https://YOUR_URL/api/webhooks/stripe`

## Step 6: Deploy

```bash
vercel --prod
```

## Step 7: Jotform Webhook

- [ ] Create Jotform
- [ ] Add webhook: `https://YOUR_URL/api/webhooks/jotform`
- [ ] Test submission

## Step 8: Agent Approval

Wait 1 week for eval cycle → Director approves → Autonomy increases

---

## Current Status

| Venture | Status | Agents | Revenue | Next |
|---------|--------|--------|---------|------|
| CON-001 | TRAINING | 3 | $15K/mo | Week 2: APPROVAL |

---

## Forms & Documentation

**Forms**: Use Jotform (no custom code needed, webhook handles it)  
**Docs**: Neo4j has 121 indexed documents + 200+ relationships  
**Agents**: Query live via Neo4j (no static files needed)

