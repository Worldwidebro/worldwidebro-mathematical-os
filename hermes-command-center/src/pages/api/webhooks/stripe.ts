import { createClient } from '@supabase/supabase-js';
import Stripe from 'stripe';
import type { NextRequest } from 'next/server';

const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);
const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET!;

export const runtime = 'edge';

export async function POST(req: NextRequest) {
  const body = await req.text();
  const signature = req.headers.get('stripe-signature');

  if (!signature) {
    return Response.json({ error: 'missing signature' }, { status: 400 });
  }

  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(body, signature, webhookSecret);
  } catch (err: any) {
    console.error('[stripe-webhook] signature verification failed:', err.message);
    return Response.json({ error: 'invalid signature' }, { status: 400 });
  }

  if (event.type === 'payment_intent.succeeded') {
    const payment = event.data.object as Stripe.PaymentIntent;
    await handlePaymentSucceeded(payment);
  }

  if (event.type === 'checkout.session.completed') {
    const session = event.data.object as Stripe.Checkout.Session;
    if (session.payment_status === 'paid') {
      await handleCheckoutPaid(session);
    }
  }

  if (event.type === 'invoice.paid') {
    const invoice = event.data.object as Stripe.Invoice;
    await handleInvoicePaid(invoice);
  }

  return Response.json({ received: true });
}

export default POST;

async function handlePaymentSucceeded(payment: Stripe.PaymentIntent) {
  const email = payment.receipt_email || (payment.latest_charge as any)?.billing_details?.email || null;
  const ventureId = payment.metadata?.venture_id || 'STA-001';
  const now = new Date().toISOString();

  const { error } = await supabase.from('deal_payments').insert([{
    email,
    amount: payment.amount / 100,
    currency: payment.currency,
    venture_id: ventureId,
    stripe_payment_id: payment.id,
    status: 'succeeded',
    payment_type: 'one_time',
    description: payment.description || null,
    metadata: payment.metadata || null,
    created_at: now,
    paid_at: now,
  }]);

  if (error) {
    console.error('[stripe-webhook] deal_payments insert error:', error);
    throw error;
  }
}

async function handleCheckoutPaid(session: Stripe.Checkout.Session) {
  const email = session.customer_details?.email || session.customer_email;
  const ventureId = session.metadata?.venture_id || 'STA-001';
  const now = new Date().toISOString();

  const { error } = await supabase.from('deal_payments').insert([{
    email,
    amount: (session.amount_total || 0) / 100,
    currency: session.currency,
    venture_id: ventureId,
    stripe_payment_id: (session.payment_intent as string) || session.id,
    status: 'succeeded',
    payment_type: session.mode === 'subscription' ? 'subscription' : 'one_time',
    description: session.metadata?.description || null,
    metadata: session.metadata || null,
    created_at: now,
    paid_at: now,
  }]);

  if (error) {
    console.error('[stripe-webhook] checkout insert error:', error);
    throw error;
  }
}

async function handleInvoicePaid(invoice: Stripe.Invoice) {
  const email = typeof invoice.customer_email === 'string' ? invoice.customer_email : null;
  const ventureId = (invoice.metadata as any)?.venture_id || 'STA-001';
  const now = new Date().toISOString();
  const paymentId = typeof (invoice as any).payment_intent === 'string' ? (invoice as any).payment_intent : invoice.id;

  const { error } = await supabase.from('deal_payments').insert([{
    email,
    amount: (invoice.amount_paid || 0) / 100,
    currency: invoice.currency,
    venture_id: ventureId,
    stripe_payment_id: paymentId,
    status: 'succeeded',
    payment_type: 'subscription',
    description: invoice.description || null,
    metadata: invoice.metadata || null,
    created_at: now,
    paid_at: now,
  }]);

  if (error) {
    console.error('[stripe-webhook] invoice insert error:', error);
    throw error;
  }
}
