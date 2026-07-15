---
references:
  - [[VENTURE-MASTER]]
  - [[ORB-MASTER-CONNECTOR-2026-06-11]]
---

# Deal Contracts, Responsibilities & Intake (Middleman Layer)

**Purpose:** Map the paperwork that lets you **capture a spread** as a middleman. You already have a 10-contract library (`CONTRACTS/CONTRACT-INDEX.md`) — this doc points to it, fills the **3 missing middleman agreements**, and adds the deal **intake form**.

> ⚠️ Operational starting points, not legal advice. Have a NC attorney review the new Subcontractor + Teaming agreements once; reuse after.

---

## 1) WHAT YOU ALREADY HAVE (reuse these)

From `CONTRACTS/` — covers the supply side + partnerships:

| Existing contract | Middleman use |
|-------------------|---------------|
| MSA (4) + SOW (5) | RETAINER deals — agency/B2B client terms + per-project scope |
| NDA (3) | Protects client lists + pricing (your moat) — sign first, always |
| IP Assignment (2) | Worker-side IP on dev/creative deals |
| Revenue Share (6) | REFERRAL / finder's-fee splits (adapt for flat finder's fee) |
| Decision Rights Matrix (9) | The responsibilities/RACI baseline |
| Vendor Agreement (8) | When you're the buyer of tools/subs' services |
| Joint Venture (7) | Co-*owned* ventures (NOT the same as teaming — see gap below) |

---

## 2) THE 3 GAPS TO ADD (middleman-specific, not in the 10)

| New file → `CONTRACTS/` | Model | Why it's needed | Priority |
|-------------------------|-------|-----------------|----------|
| **11-SUBCONTRACTOR-AGREEMENT** | NET — construction/field | You hire the crew *under* you: scope, pay, insurance/COI, indemnity, no-poach. **Needed for the first deal.** | 🔴 NOW |
| **12-BROKER-DISPATCH-AGREEMENT** | BROKER — logistics dispatch | Your % per load, who bills the shipper, carrier duties, non-circumvention | 🟡 when courier/dispatch deal appears |
| **13-TEAMING-AGREEMENT** | BROKER — gov primes | You + prime bid *together* (not co-owned): work split, exclusivity for that bid, what happens on award | 🟡 when priming/teaming |

> JV (7) ≠ Teaming. JV = shared ownership of a new entity. Teaming = two independent firms agree to pursue one specific contract. Gov subbing uses **teaming**, not JV.

---

## 3) RESPONSIBILITIES (RACI) — construction sub-broker

Builds on Decision Rights Matrix (9). For a sub deal:

| Function | You (middleman) | Crew/Sub | Prime |
|----------|:---:|:---:|:---:|
| Win work / get on sub list | **R** | — | A |
| Scope & price | **R** | C | A |
| Sign prime's subcontract (obligation up) | **R** | — | A |
| Sign your subcontractor agreement (obligation down) | **R** | A | — |
| Perform the work | A | **R** | — |
| Supervision / QA | **R** | R | C |
| Insurance / COI | **R** | C | I |
| Invoice prime / pay crew | **R** | I | — |
| **Keep the spread** | **R** | — | — |

**Your value = you own the relationship, both contracts, and the money flow.** Crew owns labor. The gap between the two contracts is your spread.

---

## 4) THE SPREAD

```
Prime pays you (contract price)
  → you pay crew (labor cost via Subcontractor Agreement #11)
  → you keep MARGIN + coordination fee
```
Construction: crew at $X, bill prime $X +15–30%. Dispatch: keep 5–10%/load. Agency: bill−pay. Referral: flat fee, no delivery risk.

---

## 5) DEAL INTAKE FORM (JotForm)

**Form:** `Winners Circle — Deal Intake` · routes to ClickUp/Notion via existing Zapier Form→Task zap. **One form, all sectors** (sector field routes).

| Field | Type |
|-------|------|
| Date | date |
| Source / prime / client | short text |
| Sector (Construction / Logistics / Services / Other) | dropdown |
| Scope of work | long text |
| Location | short text |
| Estimated value ($) | number |
| Timeline / deadline | date |
| Crew/sub needed? | yes/no |
| Status (Lead / Quoted / Won / Lost) | dropdown |
| Notes | long text |

*(JotForm MCP is connected — this can be created live on request.)*

---

## HONEST SEQUENCE

You need exactly **one** new doc to start: **#11 Subcontractor Agreement**, because the first deal is a construction sub. Everything else (Broker, Teaming, the JotForm) gets built when that deal type actually appears.

> Draft #11, make the SYNCON call, let real deals pull #12/#13 + the form into existence. Don't build all three + the form before the first call.
