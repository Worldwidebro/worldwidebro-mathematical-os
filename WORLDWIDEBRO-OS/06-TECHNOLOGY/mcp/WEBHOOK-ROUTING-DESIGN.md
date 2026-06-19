# FIN-036 Webhook Routing — Design & Implementation

**Purpose:** Route scored deals to appropriate ventures  
**Triggered By:** DealScoringAgent (after scoring)  
**Delivery:** HTTP POST to venture webhook endpoints  
**Status:** Design-ready for implementation

---

## Routing Logic

```
Scored Deal (overall_score, recommended_ventures)
    ↓
Check Score Threshold
    ├─ Score < 50: DEFER (capability gap)
    ├─ Score 50-70: ROUTE with yellow flag (risky)
    └─ Score 70+: ROUTE with confidence
    ↓
Identify Venture Webhook
    (from ventures-master.csv or hardcoded map)
    ↓
Prepare Payload
    (deal data + scoring + commission info)
    ↓
Send HTTP POST
    (with retry logic + timeout)
    ↓
Log Delivery
    (in webhook_deliveries table)
    ↓
Await Venture Response
    (accepted/rejected/pending)
```

---

## Venture Webhook Endpoints

| Venture | Webhook URL | Triggers |
|---------|------------|----------|
| CON-001 | `https://con-001.local/webhooks/deals` | Construction opportunities |
| CON-002 | `https://con-002.local/webhooks/deals` | Roofing opportunities |
| ... | ... | ... |
| CON-020 | `https://con-020.local/webhooks/deals` | Specialty contracting |
| STAFF-001 | `https://staff-001.local/webhooks/leads` | Labor arbitrage |
| RE-001 | `https://re-001.local/webhooks/properties` | Real estate |

**Fallback:** If webhook unavailable, store in Supabase pending queue

---

## Webhook Payload Format

```json
{
  "event_type": "deal_routed",
  "event_id": "evt_abc123",
  "timestamp": "2026-06-12T14:30:00Z",
  
  "deal": {
    "deal_id": "crucix_construction_001",
    "title": "Excess copper wiring liquidation",
    "description": "...",
    "amount": 250000,
    "vertical": "construction_materials",
    "source_feed": "excess_inventory",
    "external_url": "https://..."
  },
  
  "fin036_scoring": {
    "viability_score": 80,
    "fit_score": 85,
    "urgency_score": 75,
    "overall_score": 81,
    "confidence": 0.87,
    "reasoning": "Clear market, CON ventures core business"
  },
  
  "fin036_routing": {
    "recommended_ventures": ["CON-001", "CON-005"],
    "primary_venture": "CON-005",
    "action": "ROUTE",
    "commission_rate": 0.10,
    "commission_on_success": 25000
  },
  
  "venture_action_required": "Review & Accept/Reject within 48 hours"
}
```

---

## Venture Response Format

Venture can respond via webhook or Supabase:

```json
{
  "deal_id": "crucix_construction_001",
  "venture_id": "CON-005",
  "status": "accepted",  // or "rejected", "pending"
  "decision_timestamp": "2026-06-12T15:45:00Z",
  "notes": "Will execute with financing. Need capital by Friday.",
  "accepted_terms": {
    "deal_amount": 250000,
    "commission_rate": 0.10,
    "fin036_commission": 25000
  }
}
```

---

## Retry Logic

**On webhook delivery failure:**

```
Attempt 1: Immediate
Attempt 2: +5 minutes (exponential backoff)
Attempt 3: +15 minutes
Attempt 4: +60 minutes
Attempt 5: +4 hours
Max 5 attempts over 5 hours

If all fail: Log to Supabase, alert via Slack
```

---

## Python Implementation

```python
import asyncio
import httpx
import json

class DealRouter:
    def __init__(self):
        self.webhook_endpoints = {
            "CON-001": "https://con-001.local/webhooks/deals",
            "CON-005": "https://con-005.local/webhooks/deals",
            "STAFF-001": "https://staff-001.local/webhooks/leads",
            "RE-001": "https://re-001.local/webhooks/properties",
        }
        self.max_retries = 5

    async def route_deal(self, deal: Dict, score: Dict, db) -> Dict:
        """Route scored deal to ventures"""
        
        # Get recommended ventures
        recommended = score.get("recommended_ventures", [])
        
        routing_results = []
        
        for venture_id in recommended:
            webhook_url = self.webhook_endpoints.get(venture_id)
            if not webhook_url:
                continue
            
            # Build payload
            payload = {
                "event_type": "deal_routed",
                "deal": deal,
                "fin036_scoring": score,
                "fin036_routing": {
                    "venture_id": venture_id,
                    "commission_rate": 0.10,
                    "commission_value": deal.get("amount", 0) * 0.10
                }
            }
            
            # Send with retries
            result = await self._send_with_retry(
                webhook_url, 
                payload, 
                venture_id, 
                deal["deal_id"]
            )
            
            # Log delivery
            db.table("webhook_deliveries").insert({
                "deal_id": deal["deal_id"],
                "venture_id": venture_id,
                "webhook_url": webhook_url,
                "payload": payload,
                "response_status": result["status"],
                "delivered_at": result["timestamp"]
            }).execute()
            
            routing_results.append(result)
        
        return routing_results

    async def _send_with_retry(self, url: str, payload: Dict, 
                                venture_id: str, deal_id: str) -> Dict:
        """Send webhook with exponential backoff retry"""
        
        async with httpx.AsyncClient(timeout=30) as client:
            for attempt in range(1, self.max_retries + 1):
                try:
                    response = await client.post(
                        url,
                        json=payload,
                        headers={"Content-Type": "application/json"}
                    )
                    
                    return {
                        "venture_id": venture_id,
                        "deal_id": deal_id,
                        "status": response.status_code,
                        "timestamp": datetime.now().isoformat(),
                        "attempt": attempt
                    }
                
                except Exception as e:
                    if attempt < self.max_retries:
                        wait_time = 5 * (2 ** (attempt - 1))  # Exponential backoff
                        await asyncio.sleep(wait_time)
                    else:
                        return {
                            "venture_id": venture_id,
                            "deal_id": deal_id,
                            "status": 0,
                            "error": str(e),
                            "timestamp": datetime.now().isoformat(),
                            "attempt": attempt
                        }
```

---

## Testing Webhook Locally

```bash
# Mock venture webhook (for testing)
python -m http.server 8000 &

# Test payload
curl -X POST http://localhost:8000/webhooks/deals \
  -H "Content-Type: application/json" \
  -d @deal-payload.json

# Expected response: 200 OK
```

---

## Monitoring & Alerts

**Log to Slack when:**
- High-score deal (>85) routed successfully
- Webhook delivery fails after 5 retries
- Venture accepts deal (create commission record)
- Venture rejects deal (log reasoning)

**Daily report:**
- Deals routed: X
- Acceptance rate: Y%
- Commission earned: $Z
