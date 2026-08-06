---
name: 02_PROJECTS/TECH/TECH-038/ARCHITECTURE
title: 'TECH-038: Unified Communications Platform'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# TECH-038: Unified Communications Platform

**Vision:** One platform, three customer interfaces (WhatsApp, Telegram, Voice), powers all 712 ventures.

## Architecture

```
TECH-038 Communications Platform
│
├─ Voice Infrastructure (voice/)
│  ├── Asterisk (SIP server)
│  ├── Whisper (speech-to-text)
│  ├── Coqui (text-to-speech)
│  └── VICIdial (call management)
│
├─ Channel Gateway (channel-gateway/)
│  ├── router.ts (identity/session, dispatch)
│  ├── whatsapp/ (adapter)
│  ├── telegram/ (adapter)
│  ├── voice/ (SIP → Asterisk)
│  └── adapters/ (lt-005-dispatch, con-001, ops-001)
│
├─ Data (supabase/)
│  ├── identities (unified customer/employee)
│  ├── sessions (conversation state)
│  ├── channel_messages (audit)
│  └── call_logs (voice)
│
└─ Deployment (docker-compose.yml)
```

## Faces (Customer Interfaces)

| Face | Ventures | Use |
|------|----------|-----|
| WhatsApp | LT-005, CON-001, OPS-001 | Customer requests |
| Telegram | LT-005, CON-001, OPS-001 | Internal teams |
| Voice/SIP | All | Inbound calls → agent |
| Web | Portal (existing) | Dashboard |

## One Identity Across All Channels

**Same customer identity** on WhatsApp + Telegram + Voice → unified audit trail, context switching.

## Revenue

- LT-005: $40K/mo (courier dispatch)
- CON-001: $50K/mo (construction)
- OPS-001: $25K/mo (staffing)
- EC-112: $15K/mo (ecommerce)
- RE-001: $20K/mo (real estate)
- **Total: $150K/mo** (licensed to 5 ventures @ $7K ea)

## Phases

**Week 1-2:** Infrastructure + WhatsApp (docker-compose, Asterisk, channel-gateway)
**Week 2-3:** Telegram + Voice integration
**Week 4:** Go-live (LT-005 pilot)

## Success Metrics

- [ ] Inbound voice calls → agent routing
- [ ] Customer WhatsApp → pickup request (LT-005)
- [ ] Driver Telegram → accept/complete
- [ ] Payment collected after delivery
- [ ] Scale to CON-001 ($50K/mo revenue)

## Next

1. Verify Docker Compose + Asterisk + Whisper installation
2. Wire voice adapter to Asterisk
3. Implement LT-005 agent (phone → customer service)
4. Deploy to production
