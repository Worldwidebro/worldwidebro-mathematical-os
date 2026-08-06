---
name: services/channel-gateway/EXAMPLE
title: 'Channel Gateway Example: LT-005 Medical Courier'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Channel Gateway Example: LT-005 Medical Courier

## Flow

```
Customer (WhatsApp)
  ↓ "STAT pickup at hospital"
whatsapp/webhook.ts
  ↓ POST /webhooks/whatsapp
router.ts :: routeMessage()
  ↓ resolveIdentity(whatsapp, +15551234567, LT-005)
  ↓ getOrCreateSession(user_123, whatsapp, LT-005)
dispatchToAgent() → lt-005-dispatch.ts
  ↓ parseIntent("STAT pickup...") → STAT_PICKUP
  ↓ handleStatPickup() 
  ↓ response: "STAT pickup received. Driver in 3-7 minutes."
sendWhatsAppMessage(+15551234567, response)
  ↓ queue via WhatsApp Business Platform API
  
[ Dispatcher agent runs in background ]
  ↓ Create pickup_request in Supabase
  ↓ Query available drivers (Qdrant: location + status)
  ↓ Assign closest driver
  ↓ Send Telegram to driver: "New pickup: Hospital → 123 Main St"

Driver (Telegram)
  ↓ "I accept this delivery"
telegram/webhook.ts
  ↓ POST /webhooks/telegram
router.ts :: routeMessage()
  ↓ resolveIdentity(telegram, 987654321, LT-005)
  ↓ getOrCreateSession(driver_456, telegram, LT-005)
dispatchToAgent() → lt-005-dispatch.ts
  ↓ handleDriverAccept()
  ↓ response: "Pickup accepted. Route loaded. Head to location now."
sendTelegramMessage(987654321, response)
```

## Key Points

- **Same identity/session layer** for customer (WhatsApp) + driver (Telegram)
- **Same router** handles all channels
- **Venture-specific adapters** customize agent behavior (LT-005 dispatch vs CON-001 construction vs OPS-001 staffing)
- **Supabase** tables (identities, sessions, channel_messages) provide persistence + audit trail
- **Qdrant** used by dispatcher agent for semantic search (driver location/status/skills)

## Next

1. Wire `dispatchToAgent()` in router.ts to call `lt-005-dispatch.ts`
2. Implement Supabase pickups + driver assignment tables
3. Build dispatcher background agent (runs on schedule or event-driven)
4. Deploy to Vercel (shared service) + integrate with LT-005 Vercel frontend
