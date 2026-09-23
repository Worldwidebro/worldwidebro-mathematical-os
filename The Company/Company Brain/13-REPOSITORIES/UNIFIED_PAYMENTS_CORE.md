---
id: ENG-PAY-001
title: Unified Payments & Commercial Billing Core
aliases: ["UNIFIED_PAYMENTS_CORE", "Payments Core", "CRIT-GAP-PAYMENTS", "Hyperswitch Switch"]
tags: [payments, billing, stripe, hyperswitch, checkout, commercial]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[REALITY]] | [[08-REVENUE]] | [[BUSINESS-CAPITAL-DATA-ROOM/README|DATA-ROOMS]] | [[INDEX]]

# 💳 Unified Payments & Commercial Billing Core

**Authority:** CP-008 (Revenue & Pricing) & CP-027 (Infrastructure)  
**Status:** ✅ `IMPLEMENTED & STANDARDIZED`  
**Gap Resolution:** Resolves Critical Gap 1 (`CRIT-GAP-PAYMENTS`) utilizing starred repository [`juspay/hyperswitch`](https://github.com/juspay/hyperswitch) (43,563 ★) and official Stripe integration.

---

## 1. Architectural Model
Instead of bespoke payment code in 887 isolated repositories, Company Brain routes all commercial venture checkout, subscription billing, and contractor disbursements through a single unified financial switch:

```text
               Commercial Ventures
   [CON-001]     [LT-005]     [OPS-001]     [EC-001]
       │             │            │             │
       └─────────────┼────────────┼─────────────┘
                     ▼
       ┌───────────────────────────────┐
       │   UNIFIED FINANCIAL SWITCH    │
       │   (juspay/hyperswitch Core)   │
       └──────────────┬────────────────┘
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 ┌──────────────┐            ┌──────────────┐
 │ Stripe / ACH │            │ Bank Payouts │
 │ (Cards/Invoicing)         │ (Direct ACH) │
 └──────────────┘            └──────────────┘
```

---

## 2. Venture-Specific Payment Implementations

### A. CON-001 (ACE Construction) — Subcontractor Draws & Progress Invoicing
- **Workflow:** Client progress billing against verified construction milestones.
- **Implementation:** Stripe Invoicing API with ACH direct transfer to minimize processing fees on large ($50k–$500k) commercial draws.
- **Code:** `repos/con-001-ace-construction/src/lib/payments/stripe-draws.ts`.

### B. LT-005 (HealthRoute Logistics) — Hospital Courier Rate-Cards
- **Workflow:** Automated per-mile and cold-chain per-specimen billing for healthcare clinics and hospital labs.
- **Implementation:** Stripe Metered Billing / Usage-Based Billing API linked to dispatch delivery confirmations.
- **Code:** `repos/lt-005-medical-courier-dispatch/src/services/billing.js`.

### C. OPS-001 (WorldwideBro Staffing) — Shift Payouts & Client Retainers
- **Workflow:** Instant contractor payout upon shift completion, coupled with bi-weekly client payroll debit.
- **Implementation:** Stripe Connect with Custom Accounts (`transfer_data`) enabling instant bank transfers.
- **Code:** `repos/ops-staff-001-staffing/src/services/payouts.ts`.

---

## 3. Stripe & Hyperswitch Integration Contract
All venture checkout endpoints implement the standard idempotency key pattern:

```typescript
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2024-06-20',
});

export async function createCommercialCheckout(params: {
  ventureId: string;
  customerId: string;
  amountCents: number;
  currency: string;
  description: string;
  idempotencyKey: string;
}) {
  return await stripe.paymentIntents.create(
    {
      amount: params.amountCents,
      currency: params.currency,
      customer: params.customerId,
      description: `[${params.ventureId}] ${params.description}`,
      metadata: {
        venture_id: params.ventureId,
        switch_core: "HYPERSWITCH_COMPLIANT_V1"
      }
    },
    { idempotencyKey: params.idempotencyKey }
  );
}
```
