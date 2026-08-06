---
name: WORLDWIDEBRO-OS/06-PARTNERS/SERVICENOW-INTEGRATION
title: ServiceNow Integration Spec
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# ServiceNow Integration Spec

## Architecture

Partner logs in → ServiceNow auto-provisioned → Lead captured in VEX → Webhook fires → ServiceNow incident created → Deal progresses → Payment received → Auto-close ticket + commission recorded

## API Specification

### 1. Incident Creation (Lead Capture)

```
POST /servicenow/incidents
{
  "partner_id": "partner-123",
  "venture_id": "CON-001",
  "customer_email": "prospect@company.com",
  "deal_value": 15000
}

Response: incident_id (e.g., "INC0012345")
```

### 2. Deal Stage Updates

```
PATCH /servicenow/incidents/{id}
{
  "stage": "consultation_booked|quote_sent|won|lost"
}
```

### 3. Partner Dashboard (Read)

```
GET /servicenow/incidents?partner_id={id}

Response: [incident list with deal value, stage, commission]
Summary: total_deals, won_deals, pipeline_value, earned_commission
```

### 4. Stripe Payment Webhook

Trigger: Payment received → Mark incident closed → Record commission → Email partner → Update dashboard

## Setup Instructions

**For Partner:**
1. OAuth login → ServiceNow auto-provisioned
2. Generate API key → Copy to settings
3. Test: curl POST to /servicenow/incidents

**For Engineering:**
1. Create ServiceNow API wrapper
2. Wire Stripe webhook → incident close
3. Add partner auth middleware (API key validation)
4. Audit logging (all API calls)

## Security

- Rate limit: 1000 req/day per partner
- Log all incident changes (audit trail)
- Encrypt API keys at rest
- Annual key rotation

**UPDATED: 2026-08-05**
