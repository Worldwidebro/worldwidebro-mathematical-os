import Stripe from 'stripe';
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || '', { apiVersion: '2024-06-20' });
export default async function handler(req: any, res: any) {
  if (req.method !== 'POST') return res.status(405).end();
  const { email, amount, venture_id = 'STA-001' } = req.body;
  const now = new Date().toISOString();
  try {
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: [{
        price_data: { currency: 'usd', unit_amount: Math.round(amount * 100), product_data: { name: `${venture_id} Service` } },
        quantity: 1,
      }],
      mode: 'payment',
      success_url: `${process.env.DOMAIN}/success?email=${email}`,
      cancel_url: `${process.env.DOMAIN}/cancel`,
      customer_email: email,
      metadata: { email, venture_id, created_at: now },
    });
    console.log(`[${now}] ✅ Payment: ${email} | $${amount} | ${venture_id}`);
    res.status(200).json({ url: session.url, session_id: session.id, created_at: now });
  } catch (err: any) {
    res.status(500).json({ error: err.message });
  }
}
