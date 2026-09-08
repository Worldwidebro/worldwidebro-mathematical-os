---
name: official-stripe-integration
description: Official Stripe payment integration skill covering PaymentIntents, idempotent webhook processing, Checkout Sessions, Customer Portal, subscription lifecycle, SCA/3D Secure compliance, and financial reconciliation.
source: VoltAgent/awesome-agent-skills
origin: Stripe Official Engineering Standards
---

[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# 💳 Official Stripe Integration Skill

> Authoritative payment engineering patterns based on Stripe official documentation, idempotent webhook processing, and SCA/3DS compliance.

## 🧠 Core Principles

1. **Idempotency Everywhere**: All mutating Stripe API requests (charges, transfers, refunds) must supply an `Idempotency-Key` header (`uuidv4` or deterministic event hash).
2. **Server-Side Truth**: Never trust client-submitted amounts, prices, or currency parameters. Look up canonical product/price IDs in the database or Stripe Catalog.
3. **Webhook Verification**: Always verify raw webhook request signatures using `stripe.webhooks.constructEvent()` before inspecting event payloads.
4. **Resilient Webhook Handlers**: Return HTTP 200 immediately after verifying the signature and enqueueing the task to an asynchronous worker or durable queue.

---

## 🛠️ Implementation Patterns

### 1. PaymentIntent Creation with Idempotency

```typescript
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2024-06-20',
});

export async function createCheckoutPaymentIntent({
  customerId,
  amountInCents,
  currency = 'usd',
  orderId,
}: {
  customerId: string;
  amountInCents: number;
  currency: string;
  orderId: string;
}) {
  return await stripe.paymentIntents.create(
    {
      amount: amountInCents,
      currency,
      customer: customerId,
      automatic_payment_methods: { enabled: true },
      metadata: {
        orderId,
        ventureId: process.env.VENTURE_ID || 'CORE',
      },
    },
    {
      idempotencyKey: `pi_${orderId}_${amountInCents}`,
    }
  );
}
```

### 2. Verified Webhook Dispatcher

```typescript
import { NextRequest, NextResponse } from 'next/server';
import Stripe from 'stripe';

export async function POST(req: NextRequest) {
  const body = await req.text();
  const signature = req.headers.get('stripe-signature');

  if (!signature) {
    return NextResponse.json({ error: 'Missing stripe-signature' }, { status: 400 });
  }

  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    );
  } catch (err: any) {
    return NextResponse.json({ error: `Webhook signature verification failed: ${err.message}` }, { status: 400 });
  }

  // Handle essential subscription & payment events
  switch (event.type) {
    case 'payment_intent.succeeded': {
      const paymentIntent = event.data.object as Stripe.PaymentIntent;
      await handlePaymentSuccess(paymentIntent);
      break;
    }
    case 'customer.subscription.updated':
    case 'customer.subscription.deleted': {
      const subscription = event.data.object as Stripe.Subscription;
      await syncSubscriptionStatus(subscription);
      break;
    }
    default:
      console.log(`[Stripe Webhook] Unhandled event type: ${event.type}`);
  }

  return NextResponse.json({ received: true }, { status: 200 });
}
```

---

## 🔒 Security & PCI Compliance Checklist

- [ ] Secret API keys (`sk_live_*`) are never exposed to browser bundles or client code.
- [ ] Raw request bodies are passed to `constructEvent` without JSON parsing interference.
- [ ] Webhook replay attacks are mitigated by checking timestamp freshness within tolerance (default: 300 seconds).
- [ ] Customer payment details use Stripe Elements / Checkout to maintain SAQ-A PCI compliance.
