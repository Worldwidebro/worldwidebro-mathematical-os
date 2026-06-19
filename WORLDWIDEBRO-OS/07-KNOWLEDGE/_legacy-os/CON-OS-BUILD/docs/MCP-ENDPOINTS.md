# MCP Server Endpoints — CON OS API Specification

**Server:** Flask + MCP Protocol  
**Port:** 8000 (main router), 8001-8005 (per-service)  
**Auth:** API key + Supabase JWT

---

## 1. /submit_referral

**Purpose:** Intake new construction deal from referral network  
**Method:** POST  
**Route:** `/mcp/tools/submit_referral`

### Input Schema

```json
{
  "contact_id": "string (required)",
  "contact_name": "string",
  "contact_phone": "string",
  "job_title": "string (required)",
  "job_description": "string",
  "budget": "number (required)",
  "timeline": "string (enum: urgent|standard|flexible)",
  "sector": "string (enum: CON-001...CON-020)",
  "contractor_ids": ["string"] (optional),
  "referrer_id": "string (optional)"
}
```

### Output Schema

```json
{
  "deal_id": "string (UUID)",
  "status": "string (enum: pending_contract|contract_sent|active|completed)",
  "estimated_profit": "number",
  "deal_score": "number (0-100)",
  "next_step": "string (description)",
  "contracts_ready": "boolean",
  "agent_assigned": "string",
  "created_at": "ISO 8601 timestamp"
}
```

### Example Request

```bash
curl -X POST http://localhost:8000/mcp/tools/submit_referral \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contact_id": "ref_charlotte_restoration",
    "contact_name": "Charlotte Restoration Team",
    "job_title": "Commercial building electrical rewire",
    "budget": 85000,
    "timeline": "urgent",
    "sector": "CON-011",
    "contractor_ids": ["contractor_elite_electrical", "contractor_licensed_subs"]
  }'
```

### Example Response

```json
{
  "deal_id": "deal_20260616_001",
  "status": "pending_contract",
  "estimated_profit": 20400,
  "deal_score": 91.4,
  "next_step": "Auto-generated contracts sent. Awaiting signature.",
  "contracts_ready": true,
  "agent_assigned": "coo_agent_1",
  "created_at": "2026-06-16T14:23:00Z"
}
```

### Business Logic

1. Validate contact exists (if not, create)
2. Classify deal (sector + urgency + budget → score)
3. Estimate profit (budget × margin% − split costs)
4. Assign COO agent for review
5. Trigger contract generation
6. Return deal record + next steps

---

## 2. /get_contractor_score

**Purpose:** Lookup contractor reputation score  
**Method:** GET  
**Route:** `/mcp/tools/get_contractor_score`

### Input Schema

```json
{
  "contractor_id": "string (required)",
  "include_metrics": "boolean (default: true)",
  "include_past_deals": "boolean (default: false)"
}
```

### Output Schema

```json
{
  "contractor_id": "string",
  "name": "string",
  "overall_score": "number (0-100)",
  "tier": "string (enum: S|A|B|C|D)",
  "metrics": {
    "quality": "number (0-100)",
    "speed": "number (0-100)",
    "compliance": "number (0-100)",
    "efficiency": "number (0-100)",
    "communication": "number (0-100)"
  },
  "deals_completed": "number",
  "total_revenue": "number",
  "past_deals": ["object"] (optional),
  "last_updated": "ISO 8601 timestamp",
  "recommendation": "string (assign to this tier of jobs)"
}
```

### Example Request

```bash
curl -X GET "http://localhost:8000/mcp/tools/get_contractor_score?contractor_id=contractor_elite_electrical&include_metrics=true"
```

### Example Response

```json
{
  "contractor_id": "contractor_elite_electrical",
  "name": "Elite Electrical Solutions",
  "overall_score": 91.4,
  "tier": "S",
  "metrics": {
    "quality": 95,
    "speed": 88,
    "compliance": 92,
    "efficiency": 89,
    "communication": 91
  },
  "deals_completed": 47,
  "total_revenue": 2340000,
  "recommendation": "Assign to all projects, especially complex work"
}
```

### Business Logic

1. Query contractor record from graph_entities
2. Calculate score: (quality×40% + speed×25% + compliance×20% + efficiency×10% + communication×5%)
3. Map score to tier (S: 90+, A: 80-89, B: 70-79, C: 60-69, D: <60)
4. Return metrics + past deals (if requested)

---

## 3. /trigger_payment_distribution

**Purpose:** Distribute payment per split model  
**Method:** POST  
**Route:** `/mcp/tools/trigger_payment_distribution`

### Input Schema

```json
{
  "deal_id": "string (required)",
  "total_payment": "number (required)",
  "invoice_id": "string",
  "invoice_date": "ISO 8601 date",
  "split_override": {
    "labor_percent": "number (default: 40)",
    "subcontractor_percent": "number (default: 20)",
    "referral_percent": "number (default: 10)",
    "platform_percent": "number (default: 12)",
    "reserve_percent": "number (default: 8)"
  }
}
```

### Output Schema

```json
{
  "payment_id": "string (UUID)",
  "deal_id": "string",
  "total_payment": "number",
  "splits": [
    {
      "recipient_type": "string (labor|subcontractor|referral|platform|reserve)",
      "recipient_id": "string",
      "recipient_name": "string",
      "amount": "number",
      "percent": "number",
      "payment_method": "string (stripe|bank|credit)",
      "status": "string (pending|processing|complete)"
    }
  ],
  "payment_status": "string (routing|processing|complete)",
  "created_at": "ISO 8601 timestamp"
}
```

### Example Request

```bash
curl -X POST http://localhost:8000/mcp/tools/trigger_payment_distribution \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "deal_id": "deal_20260616_001",
    "total_payment": 85000,
    "invoice_id": "inv_20260630_12345"
  }'
```

### Example Response

```json
{
  "payment_id": "pay_20260630_001",
  "deal_id": "deal_20260616_001",
  "total_payment": 85000,
  "splits": [
    {
      "recipient_type": "labor",
      "recipient_id": "contractor_elite_electrical",
      "recipient_name": "Elite Electrical Solutions",
      "amount": 34000,
      "percent": 40,
      "status": "routing"
    },
    {
      "recipient_type": "subcontractor",
      "recipient_id": "contractor_licensed_subs",
      "amount": 17000,
      "percent": 20,
      "status": "routing"
    },
    {
      "recipient_type": "referral",
      "recipient_id": "ref_charlotte_restoration",
      "amount": 8500,
      "percent": 10,
      "status": "routing"
    },
    {
      "recipient_type": "platform",
      "recipient_id": "worldwidebro_platform",
      "amount": 10200,
      "percent": 12,
      "status": "routing"
    },
    {
      "recipient_type": "reserve",
      "recipient_id": "reserve_fund",
      "amount": 6800,
      "percent": 8,
      "status": "pending"
    }
  ],
  "payment_status": "routing"
}
```

### Business Logic

1. Validate deal completed (work finished, invoice received)
2. Calculate splits using percentages (default or override)
3. Look up payment methods for each recipient
4. Route via Stripe API to bank accounts
5. Log ledger entries
6. Update graph: payout relationships

---

## 4. /update_graph_memory

**Purpose:** Learn from deal completion + update reputation  
**Method:** POST  
**Route:** `/mcp/tools/update_graph_memory`

### Input Schema

```json
{
  "deal_id": "string (required)",
  "completion_data": {
    "contractor_id": "string",
    "quality_rating": "number (0-100)",
    "speed_rating": "number (0-100)",
    "compliance_rating": "number (0-100)",
    "efficiency_rating": "number (0-100)",
    "communication_rating": "number (0-100)",
    "timeline_met": "boolean",
    "budget_variance": "number (percentage)"
  },
  "referrer_id": "string (optional)",
  "lessons_learned": "string (optional)"
}
```

### Output Schema

```json
{
  "graph_update_id": "string (UUID)",
  "deal_id": "string",
  "entities_updated": "number",
  "relationships_created": "number",
  "contractor_new_score": "number",
  "contractor_new_tier": "string",
  "referrer_new_score": "number",
  "similar_deals_found": "number",
  "message": "string (summary)"
}
```

### Example Request

```bash
curl -X POST http://localhost:8000/mcp/tools/update_graph_memory \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "deal_id": "deal_20260616_001",
    "completion_data": {
      "contractor_id": "contractor_elite_electrical",
      "quality_rating": 95,
      "speed_rating": 92,
      "compliance_rating": 94,
      "efficiency_rating": 89,
      "communication_rating": 90,
      "timeline_met": true,
      "budget_variance": -2
    },
    "referrer_id": "ref_charlotte_restoration"
  }'
```

### Example Response

```json
{
  "graph_update_id": "update_20260630_001",
  "deal_id": "deal_20260616_001",
  "entities_updated": 3,
  "relationships_created": 2,
  "contractor_new_score": 91.4,
  "contractor_new_tier": "S",
  "referrer_new_score": 87.3,
  "similar_deals_found": 12,
  "message": "Contractor Elite Electrical promoted to S-tier. 12 similar deals found for next referrals."
}
```

### Business Logic

1. Calculate contractor weighted score (new ratings)
2. Update contractor entity in Neo4j
3. Update referrer reputation (deal quality + conversion)
4. Create deal completion relationship
5. Generate vector embeddings for deal (for similarity matching)
6. Find similar past deals
7. Emit recommendations for future matching

---

## 5. /get_deal_forecast

**Purpose:** Predict next deals based on patterns  
**Method:** GET  
**Route:** `/mcp/tools/get_deal_forecast`

### Input Schema

```json
{
  "contractor_id": "string (optional)",
  "referrer_id": "string (optional)",
  "sector": "string (optional)",
  "days_ahead": "number (default: 30)",
  "confidence_threshold": "number (default: 0.7)"
}
```

### Output Schema

```json
{
  "forecast_id": "string (UUID)",
  "forecast_date": "ISO 8601 timestamp",
  "days_ahead": "number",
  "predicted_deals": [
    {
      "prediction_id": "string",
      "similar_deal_id": "string",
      "predicted_budget": "number",
      "predicted_timeline": "string",
      "predicted_sector": "string",
      "confidence": "number (0-1)",
      "recommended_contractors": ["string"],
      "reasoning": "string"
    }
  ],
  "total_predicted_revenue": "number",
  "recommendation": "string"
}
```

### Example Request

```bash
curl -X GET "http://localhost:8000/mcp/tools/get_deal_forecast?contractor_id=contractor_elite_electrical&days_ahead=30"
```

### Example Response

```json
{
  "forecast_id": "forecast_20260616_001",
  "forecast_date": "2026-06-16T14:30:00Z",
  "days_ahead": 30,
  "predicted_deals": [
    {
      "prediction_id": "pred_001",
      "similar_deal_id": "deal_20260510_015",
      "predicted_budget": 42000,
      "predicted_timeline": "urgent",
      "predicted_sector": "CON-011",
      "confidence": 0.89,
      "recommended_contractors": ["contractor_elite_electrical"],
      "reasoning": "Similar budget + sector pattern from past 90 days. Elite Electrical completed 4 similar jobs."
    }
  ],
  "total_predicted_revenue": 210000,
  "recommendation": "Expect 5 deals in next 30 days. Elite Electrical can handle all."
}
```

### Business Logic

1. Query contractor's past deals (vector similarity)
2. Find patterns (budget ranges, timelines, sectors)
3. Scan open leads + inbound signals
4. Score predictions (confidence = pattern match strength)
5. Recommend contractors based on past performance
6. Forecast revenue

---

## Error Handling

All endpoints return standard error format:

```json
{
  "error": "string (error type)",
  "message": "string (human readable)",
  "code": "number (HTTP status)",
  "request_id": "string (for debugging)"
}
```

### Common Errors

| Error | HTTP | Cause |
|-------|------|-------|
| INVALID_INPUT | 400 | Missing required fields |
| CONTRACTOR_NOT_FOUND | 404 | Contractor ID doesn't exist |
| DEAL_NOT_FOUND | 404 | Deal ID doesn't exist |
| INSUFFICIENT_BALANCE | 402 | Not enough funds for split |
| AUTH_FAILED | 401 | Invalid API key |
| RATE_LIMITED | 429 | Too many requests (100/min) |

---

## Rate Limits

- **Per API key:** 100 requests/min
- **Burst:** 200 requests/min (10 second window)
- **Concurrency:** 10 simultaneous requests

---

## Authentication

```bash
Authorization: Bearer $API_KEY
X-Request-ID: [auto-generated UUID]
Content-Type: application/json
```

Generate API key:
```bash
curl -X POST http://localhost:8000/auth/generate_key \
  -H "Authorization: Bearer $MASTER_KEY"
```

---

## Testing Locally

```bash
# Start all services
python services/deal_intake/service.py &
python services/contract_generator/service.py &
python services/payout_engine/service.py &
python services/orchestrator/service.py &
python services/graph_memory/service.py &

# Run integration tests
python scripts/test_endpoints.py

# Or test individually:
curl -X POST http://localhost:8001/mcp/tools/submit_referral [...]
curl -X GET http://localhost:8002/mcp/tools/get_contractor_score [...]
```
