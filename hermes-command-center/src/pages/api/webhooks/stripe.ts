import Stripe from 'stripe';
import { createClient } from '@supabase/supabase-js';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || '', { apiVersion: '2024-06-20' });
const supabase = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL || '', process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '');

export const config = { api: { bodyParser: { raw: true } } };

export default async function handler(req: any, res: any) {
  if (req.method !== 'POST') return res.status(405).end();

  const sig = req.headers['stripe-signature'];
  const now = new Date().toISOString();

  try {
    const event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET || '');

    if (event.type === 'checkout.session.completed') {
      const session = event.data.object as any;
      const email = session.customer_email;
      const amount = Math.round((session.amount_total || 0) / 100);
      const ventureId = session.metadata?.venture_id || 'STA-001';
      const stripePaymentId = session.payment_intent;

      console.log(`[${now}] ✅ Payment confirmed: ${email} | $${amount} | ${ventureId}`);

      const { error } = await supabase.from('payments').insert([{
        email, amount, venture_id: ventureId, stripe_payment_id: stripePaymentId,
        status: 'succeeded', created_at: now, paid_at: now,
      }]);

      if (error) {
        console.error(`[${now}] ❌ Supabase error: ${error.message}`);
        return res.status(500).json({ error: error.message });
      }

      res.status(200).json({ received: true });
    } else if (event.type === 'charge.refunded') {
      console.log(`[${now}] 🔄 Refund: ${event.data.object.id}`);
      res.status(200).json({ received: true });
    } else {
      res.status(200).json({ received: true });
    }
  } catch (err: any) {
    console.error(`[${now}] ❌ Webhook error: ${err.message}`);
    res.status(400).json({ error: err.message });
  }
}
