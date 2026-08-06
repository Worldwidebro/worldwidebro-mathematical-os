# Portfolio Operating System — GSD Roadmap

**Milestone**: v1 (4-week sprint)  
**Target**: 2026-08-12 (Week 4 completion)  
**Status**: Ready to plan

---

## Phase Breakdown

| Phase | Title | Duration | Goal | Week | Status |
|-------|-------|----------|------|------|--------|
| **1** | Launch Campaigns + Unblock B001-B004 | 5 days | Deploy OPS-001 + EC-112/CON-001 ads; resolve property/payment/envvar blockers | 1 | `ready-to-plan` |
| **2** | Activate Synergies S1+S3, Resolve B005 | 7 days | LT-005 lease + RE-001 valuations; construction tracking | 2 | not-started |
| **3** | EC-112 + CON-001 Full Deployment | 7 days | Checkout to revenue; invoice to payment; retargeting | 3 | not-started |
| **4** | Synergy Scaling + Portfolio Optimization | 7 days | S2/S4/S5 live; readiness 80%; all 7 revenue-generating | 4 | not-started |

---

## Phase 1: Launch Campaigns + Unblock B001-B004
**Duration**: Week 1 (Aug 5-9)  
**Deliverables**: 
- OPS-001 staffing system live + call script
- EC-112 paid ad campaign launched
- CON-001 paid ad campaign launched
- Blocker B001 (property/tenant model) resolved
- Blocker B003 (Stripe webhooks + RLS) resolved
- Blocker B004 (Vercel env vars) resolved
- Blocker B002 (SMS dispatch) started or resolved

**Success Criteria**:
- $50K revenue activated
- 4 blockers unblocked
- 3 ventures deployed to Vercel
- Readiness: 27.7% → 35%

**Dependencies**: PORTFOLIO-CONTEXT.md, venture specs (RE-001.md, LT-005.md, etc.)

---

## Phase 2: Activate Synergies S1+S3, Resolve B005
**Duration**: Week 2 (Aug 12-16)  
**Deliverables**:
- S1 (B001 + RE-001 → LT-005 warehouse lease) live
- S3 (CON-001 → RE-001 property valuations) live
- B005 (construction project tracking) resolved
- OPS-001 call volume scaled

**Success Criteria**:
- $150K cumulative revenue
- 2 synergies activated ($180K + $100K annual value)
- 5/7 ventures deployed
- Readiness: 35% → 50%

**Dependencies**: Phase 1 completion

---

## Phase 3: EC-112 + CON-001 Full Deployment
**Duration**: Week 3 (Aug 19-23)  
**Deliverables**:
- EC-112 checkout to payment flow live
- CON-001 invoicing to payment flow live
- Paid ad retargeting campaigns (Phase 2 audience)
- All 5 blockers (B001-B005) resolved

**Success Criteria**:
- $200K cumulative revenue
- EC-112 + CON-001 full revenue paths live
- 6/7 ventures deployed
- Readiness: 50% → 65%

**Dependencies**: Phase 2 completion

---

## Phase 4: Synergy Scaling + Portfolio Optimization
**Duration**: Week 4 (Aug 26-30)  
**Deliverables**:
- S2 (B003 + EC-112 → FIN-001 subscriptions) live
- S4 (OPS-001 staffing → LT-005 dispatch) live
- S5 (LT-011 platform serving all ventures) live
- Portfolio readiness audit: verify 80% baseline
- All 7 ventures generating revenue

**Success Criteria**:
- $300K cumulative revenue ($700K for 4-week total)
- 5/6 synergies activated ($540K+ annual value)
- 7/7 ventures deployed + generating
- Readiness: 65% → 80%+

**Dependencies**: Phase 3 completion

---

## Venture Dependencies Matrix

```
RE-001 (Real Estate)
├─ Blocked by: B001 (property/tenant model)
├─ Enables: LT-005 (warehouse space lease)
├─ Synergy: S3 (CON-001 valuations)
└─ Revenue potential: $900K/yr

LT-005 (Medical Courier)
├─ Blocked by: B002 (SMS dispatch)
├─ Enabled by: RE-001 (B001 resolved)
├─ Synergy: S1 (warehouse lease)
└─ Revenue potential: $400K/yr

LT-011 (Logistics Platform)
├─ Blocked by: B004 (Vercel env vars)
├─ Enables: All ventures (S5)
├─ Synergy: S5 (ops platform)
└─ Revenue potential: $600K/yr

OPS-001 (Staffing)
├─ Blocked by: B004 (Vercel env vars)
├─ Enables: LT-005 (dispatch staff)
├─ Synergy: S4 (staffing cross-venture)
└─ Revenue potential: $200K/yr

CON-001 (Construction)
├─ Blocked by: B003 (Stripe), B005 (project model)
├─ Enables: RE-001 (valuations)
├─ Synergy: S3 (property valuations)
└─ Revenue potential: $1.2M/yr

FIN-001 (Finance)
├─ Blocked by: B003 (Stripe)
├─ Enabled by: EC-112 (payment processing)
├─ Synergy: S2 (subscriptions)
└─ Revenue potential: $80K/yr

EC-112 (E-commerce)
├─ Blocked by: B003 (Stripe webhooks)
├─ Enables: FIN-001 (subscriptions)
├─ Synergy: S2 (payment processing)
└─ Revenue potential: $280K/yr
```

---

## Critical Blockers Timeline

| Blocker | Phase | Week | Duration | Value | Vendor/Task |
|---------|-------|------|----------|-------|-------------|
| **B001** | 1 | 1 | 3 days | $900K | Supabase property/tenant model |
| **B002** | 1 | 1 | 2 days | $200K | VAPI/Twilio SMS dispatch |
| **B003** | 1 | 1 | 2 days | $150K | Stripe webhooks + RLS |
| **B004** | 1 | 1 | 1 day | $0 | Vercel env vars (all ventures) |
| **B005** | 2 | 2 | 2 days | $500K | Supabase project tracking |

---

## Execution Model

**Parallel tracks** (simultaneous within each phase):
1. **Revenue campaigns** — OPS-001 calls, EC-112/CON-001 ads
2. **Blocker resolution** — B001-B005 unblocking
3. **Deployment** — Vercel + Supabase wiring per venture
4. **Synergy activation** — Cross-venture integrations as blockers clear

**Weekly revenue targets**:
- Week 1: $50K (OPS + early ads)
- Week 2: $150K (cumulative; S1+S3 synergies)
- Week 3: $200K (cumulative; EC-112+CON-001 live)
- Week 4: $300K+ (cumulative; S2+S4+S5 scaling)

---

## Requirements Traceability

| Requirement | Phase | Type | Owner |
|-------------|-------|------|-------|
| OPS-001 staffing live w/ call script | 1 | Revenue | OPS-001 PM |
| EC-112 paid ads launched | 1 | Revenue | Marketing |
| CON-001 paid ads launched | 1 | Revenue | Marketing |
| B001: Property/tenant model | 1 | Blocker | Engineering |
| B002: SMS dispatch | 1 | Blocker | Engineering |
| B003: Stripe webhooks | 1 | Blocker | Engineering |
| B004: Vercel env vars | 1 | Blocker | DevOps |
| B005: Project tracking | 2 | Blocker | Engineering |
| S1: LT-005 lease integration | 2 | Synergy | RE-001/LT-005 |
| S2: FIN-001 subscriptions | 4 | Synergy | EC-112/FIN-001 |
| S3: RE-001 valuations | 2 | Synergy | CON-001/RE-001 |
| S4: Cross-venture staffing | 4 | Synergy | OPS-001/LT-005 |
| S5: LT-011 platform ops | 4 | Synergy | LT-011/all |
| EC-112 checkout live | 3 | Revenue | EC-112 |
| CON-001 invoicing live | 3 | Revenue | CON-001 |
| Readiness 80%+ | 4 | Portfolio | PM |

