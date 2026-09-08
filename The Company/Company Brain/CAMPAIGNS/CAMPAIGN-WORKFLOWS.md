# CAMPAIGN-WORKFLOWS — Multi-Step Autonomous Workflows

> **Canonical Document ID:** `DOC-WFL-CAM-001`  
> **Authority:** Operations & Orchestration (CP-019 / CP-022)  
> **Status:** ACTIVE SPECIFICATION  
> **Canonical Alias:** [[CAMPAIGNS/WORKFLOWS.md]]

---

## 1. Canonical Outbound Workflow (`WFL-OUT-001`)

```text
STEP 1: Prospect Ingestion (Apollo API query for 50 target CTOs)
   │
   ▼
STEP 2: Data Verification (NeverBounce email deliverability check)
   │
   ▼
STEP 3: Codebase Intelligence Pre-Flight (GitHub API query for repo languages & agent imports)
   │
   ▼
STEP 4: Personalization Synthesis (Copy Agent populates technical hook and languages)
   │
   ▼
STEP 5: Compliance Audit (Compliance Agent verifies CAN-SPAM footer & claim citations)
   │
   ▼
STEP 6: Scheduled Dispatch (Outbound mailer sends at 09:30 prospect local time)
   │
   ▼
STEP 7: Telemetry Ingest (Webhook records open/click/reply to Grafana & Neo4j)
```

---

## 2. Master Links

- Automation: [[CAMPAIGNS/CAMPAIGN-AUTOMATION]]
- Orchestration: [[CAMPAIGNS/CAMPAIGN-ORCHESTRATION]]
