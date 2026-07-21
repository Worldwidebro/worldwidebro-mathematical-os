---
name: worldwidebro-vex-integration
description: Worldwidebro OS and vex are one unified system — internal operations + public interface
date: 2026-07-21
version: 1.0
status: ACTIVE
---

# Worldwidebro OS + vex = ONE SYSTEM

**The same organization viewed from different layers:**

---

## THE ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│                    UNIFIED SYSTEM (Worldwidebro Holdings)       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LAYER 3: PUBLIC INTERFACE (vex)                               │
│  ├─ Portfolio dashboard (712 ventures)                         │
│  ├─ Live news feed (operations ticker)                         │
│  ├─ Revenue & risk visibility                                  │
│  └─ Marketplace for customers/partners                         │
│                                                                 │
│  ───────────────── EVENT BUS BRIDGE ────────────────────        │
│  (Kafka: ventures.classified, revenue.captured, risk.flagged)  │
│                                                                 │
│  LAYER 2: OPERATIONS (Worldwidebro OS)                         │
│  ├─ Sector readiness tracker (18 OPCOs)                        │
│  ├─ 150+ autonomous bots executing tasks                       │
│  ├─ Neo4j knowledge graph (1,394 entities)                     │
│  ├─ Supabase venture records (source of truth)                 │
│  └─ n8n workflows + Slack alerts                               │
│                                                                 │
│  LAYER 1: DATA (Postgres/Neo4j/Qdrant)                         │
│  ├─ ventures table (vex_published boolean)                     │
│  ├─ ventures_events (Kafka topics)                             │
│  ├─ venture_risks (real-time flagging)                         │
│  └─ venture_revenue (MRR tracking)                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## HOW THEY CONNECT: THE NEWS FEED

**Operation Flow:**

```
1. Agent executes task
   (e.g., CON-001 invoicing bot generates invoice)
   ↓
2. Event published to Kafka
   topic: invoices.generated
   data: {invoice_id: "INV-2026-001", amount: 7455000, venture: "CON-001"}
   ↓
3. WebSocket bridge forwards to vex
   (real-time, zero latency)
   ↓
4. vex News Feed renders live
   "✅ Invoice Generated: INV-2026-001 $7.455K"
   ↓
5. User sees operations happening NOW
   (not 1 hour later via email)
```

---

## 8 KAFKA TOPICS = 8 TYPES OF NEWS

| Topic | What It Means | Shown In vex As |
|-------|--------------|-----------------|
| `ventures.classified` | Venture changed stage (MVP→Growth) | 🎯 Venture Classified: [ID] → [Stage] |
| `revenue.captured` | Payment received | 💰 Revenue Captured: [Venture] +$[Amount] |
| `invoices.generated` | Invoice created for customer | ✅ Invoice Generated: [ID] $[Amount] |
| `risk.flagged` | Venture flagged CAC too high, runway short, etc | ⚠️ Risk Flagged: [Venture] [Issue] (severity) |
| `approvals.required` | CEO/CFO needs to sign off | 🤖 Approval Required: [Venture] [Type] |
| `tasks.completed` | Bot finished a workflow | ✅ Task Completed: [Agent] [Result] |
| `errors.critical` | System alert (Neo4j timeout, payment failed) | 🔴 Critical Error: [Error] |
| `ventures.launched` | New venture went live | 🚀 Venture Launched: [ID] ($[MRR]) |

---

## VEX IS THE COMMAND CENTER DASHBOARD

**Three audiences see three things:**

| Audience | What They See | Via vex |
|----------|---------------|---------|
| **Investors** | 712 ventures portfolio + revenue growth | Ventures directory + News feed top 5 |
| **Venture teams** | Their specific venture status + approvals needed | Venture detail page + alerts in news feed |
| **Worldwidebro leadership** | Real-time ops: revenue, risks, bot execution | Operations page (news feed full screen) |

---

## THE CONNECTION IS SUPABASE

```
Supabase ventures table
├─ id (e.g., "CON-001")
├─ name
├─ stage
├─ mrr
├─ runway_months
├─ vex_published (boolean)  ← THE SWITCH
└─ created_at, updated_at

When venture reaches $5K MRR:
  → vex_published = true
  → Appears in vex Ventures directory
  → Real-time news feed shows it

Operations team in Slack:
  → "CON-001 just hit $8.2K MRR! 💰"
  → Event fires: revenue.captured
  → vex News Feed updates immediately
  → External users see: "$8.2K revenue captured this month"
```

---

## REAL-TIME EXAMPLES

**Right now, if these happened:**

```
08:00 AM — Finance bot invoices FIN-001
  vex News Feed: "✅ Invoice Generated: INV-2026-001 $7.455K"

08:05 AM — Payment received from customer
  vex News Feed: "💰 Revenue Captured: FIN-001 +$7.455K"

08:10 AM — Risk analysis flags CAC too high
  vex News Feed: "⚠️ Risk Flagged: FIN-001 CAC Too High (HIGH)"

08:15 AM — CEO approves venture launch
  vex News Feed: "🎯 Venture Launched: CON-012 ($15K/mo target)"

08:20 AM — Neo4j connection timeout (auto-recovers)
  vex News Feed: "🔴 Critical Error: Neo4j timeout (auto-recovery)"
```

**The user sees operations happening as they happen.**

---

## FOLDER STRUCTURE PROOF

```
/Documents/
├── .planning/                    ← Planning & operations docs
│   ├── SECTOR-READINESS-TRACKER.md    (internal: 18 OPCOs status)
│   ├── TOPOLOGY.md                    (internal: network topology)
│   ├── MAPS.md                        (internal: entity relationships)
│   └── [operations playbooks]
│
├── vex-hero-site/                ← PUBLIC INTERFACE
│   ├── src/pages/
│   │   ├── Ventures.tsx               (public: portfolio directory + news feed)
│   │   └── Operations.tsx             (public: live ops dashboard)
│   ├── src/components/
│   │   └── news-feed/
│   │       ├── NewsFeed.tsx           (public: operations ticker)
│   │       └── NewsFeed.module.css    (styling)
│   └── src/data/
│       └── portfolio.public.json      (synced from Supabase)
│
└── WORLDWIDEBRO-OS/
    ├── 03-PORTFOLIO/ventures/         (internal: venture folders)
    ├── 05-AGENTS/                     (internal: bot configs)
    ├── 08-DATA/
    │   └── registries/                (internal: data registry)
    └── 04-OPERATIONS/                 (internal: procedures)
```

**Summary:**
- `.planning/` + `WORLDWIDEBRO-OS/` = Internal operations (who, what, when)
- `vex-hero-site/` = External interface (what's shipped, what's earning)
- **News Feed bridges them** — real-time visibility (<100ms Kafka latency)

---

## WARP MODE IS ON

With the news feed live:

✅ **Immediate visibility** — Operations → vex in <100ms  
✅ **No manual updates** — All news generated by events  
✅ **Real accountability** — Every action timestamped and visible  
✅ **Customer trust** — Investors/partners see real activity, not marketing  

**Users know what's happening because they see it happen.**

---

**Last Updated:** 2026-07-21  
**Next Sync:** Continuous (Kafka event bus)
