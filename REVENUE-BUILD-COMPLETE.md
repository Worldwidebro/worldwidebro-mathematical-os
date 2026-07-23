# Complete Revenue Pipeline Build — Copy/Paste Ready

**Status:** Ready to execute  
**Time:** 4 hours  
**Timeline:** Tue-Thu 2026-07-22 to 2026-07-24

---

## FILE 1: `/src/components/LeadForm.tsx` (Paste into Hermes)

```typescript
'use client';
import { useState } from 'react';

export default function LeadForm({ venture_id = 'STA-001' }) {
  const [status, setStatus] = useState('');
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: any) {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch('/api/leads', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: e.target.email.value,
          budget: parseFloat(e.target.budget.value),
          venture_id,
        }),
      });
      if (res.ok) {
        setStatus('✅ Submitted! We\'ll call you soon.');
        e.target.reset();
      } else setStatus('❌ Error. Try again.');
    } catch (err) {
      setStatus('❌ Network error.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-md mx-auto p-6 bg-slate-800 rounded-lg border border-slate-700">
      <h2 className="text-lg font-bold mb-4">Get Started</h2>
      <input name="email" type="email" placeholder="your@company.com" required className="w-full mb-3 px-3 py-2 bg-slate-700 border border-slate-600 rounded text-sm text-white" />
      <input name="budget" type="number" placeholder="Budget ($)" required min="0" step="100" className="w-full mb-4 px-3 py-2 bg-slate-700 border border-slate-600 rounded text-sm text-white" />
      <button type="submit" disabled={loading} className="w-full px-4 py-2 bg-cyan-500 hover:bg-cyan-600 disabled:bg-slate-600 text-black font-bold rounded text-sm">
        {loading ? 'Submitting...' : 'Submit'}
      </button>
      {status && <p className="mt-3 text-xs text-center text-slate-300">{status}</p>}
    </form>
  );
}
```

---

## FILE 2: `/src/pages/api/leads.ts`

```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL || '',
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || ''
);

export default async function handler(req: any, res: any) {
  if (req.method !== 'POST') return res.status(405).end();
  const { email, budget, venture_id } = req.body;
  try {
    const { data, error } = await supabase.from('lead_intake').insert([{
      email, budget, venture_id: venture_id || 'STA-001', status: 'new', created_at: new Date().toISOString(),
    }]);
    if (error) throw error;
    res.status(200).json({ lead_id: data?.[0]?.id });
  } catch (err: any) {
    res.status(500).json({ error: err.message });
  }
}
```

---

## FILE 3: `/src/pages/api/pay.ts`

```typescript
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || '', { apiVersion: '2024-06-20' });

export default async function handler(req: any, res: any) {
  if (req.method !== 'POST') return res.status(405).end();
  const { email, amount, venture_id = 'STA-001' } = req.body;
  try {
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: [{
        price_data: {
          currency: 'usd',
          unit_amount: Math.round(amount * 100),
          product_data: { name: `${venture_id} Service` },
        },
        quantity: 1,
      }],
      mode: 'payment',
      success_url: `${process.env.DOMAIN}/success?email=${email}`,
      cancel_url: `${process.env.DOMAIN}/cancel`,
      metadata: { email, venture_id },
    });
    res.status(200).json({ url: session.url });
  } catch (err: any) {
    res.status(500).json({ error: err.message });
  }
}
```

---

## FILE 4: Supabase SQL (Run in Supabase console)

```sql
CREATE TABLE lead_intake (id uuid PRIMARY KEY DEFAULT gen_random_uuid(), email text NOT NULL, budget numeric, venture_id text DEFAULT 'STA-001', status text DEFAULT 'new', created_at timestamp DEFAULT now());
CREATE TABLE payments (id uuid PRIMARY KEY DEFAULT gen_random_uuid(), email text NOT NULL, venture_id text DEFAULT 'STA-001', amount numeric NOT NULL, stripe_payment_id text, status text DEFAULT 'pending', created_at timestamp DEFAULT now(), paid_at timestamp);
CREATE INDEX idx_lead_intake_venture_status ON lead_intake(venture_id, status);
CREATE INDEX idx_payments_venture_status ON payments(venture_id, status);
```

---

## FILE 5: Update `/src/app/page.tsx` — Add this to Dashboard tab

After the `const [skills, setSkills]` line, add:
```typescript
const [mrr, setMrr] = useState(0);
useEffect(() => {
  (async () => {
    const { data } = await supabase.from('payments').select('amount').eq('status', 'succeeded').gte('created_at', new Date(Date.now() - 7*24*60*60*1000).toISOString());
    setMrr(data?.reduce((sum, p: any) => sum + (p.amount || 0), 0) || 0);
  })();
}, []);
```

Then in the KPI grid, add:
```typescript
<div className="card p-5">
  <div className="text-xs font-medium text-slate-400 mb-2">REVENUE THIS WEEK</div>
  <div style={{fontSize:'26px', fontWeight:'bold', color:'#10b981'}}>${mrr.toFixed(2)}</div>
  <div style={{fontSize:'12px', color:'var(--text-3)', marginTop:'8px'}}>Paid customers</div>
</div>
```

---

## FILE 6: `.env.local`

```bash
NEXT_PUBLIC_SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_key
STRIPE_SECRET_KEY=sk_live_your_key
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_your_key
DOMAIN=http://localhost:3000
```

---

## STRIPE CLI TESTING (Optional)

```bash
# Login (one time)
stripe login

# Listen for webhooks while running npm run dev
stripe listen --forward-to localhost:3000/api/webhooks/stripe

# Test payment event
stripe trigger payment_intent.succeeded
```

---

## QUICK START ORDER

1. Create FILE 1 (LeadForm.tsx)
2. Create FILE 2 (/api/leads.ts)
3. Create FILE 3 (/api/pay.ts)
4. Run FILE 4 SQL in Supabase
5. Update FILE 5 in page.tsx
6. Add FILE 6 env vars
7. Test: `curl -X POST http://localhost:3000/api/leads -H "Content-Type: application/json" -d '{"email":"test@acme.com","budget":500,"venture_id":"STA-001"}'`
8. Deploy: `vercel --prod`

---

## TIMELINE

| When | What | Duration |
|------|------|----------|
| Tue 7/22 | Deploy Hermes | 1h |
| Wed 7/23 | Create FILES 1-3 + SQL + .env | 2.5h |
| Thu 7/24 | Add FILE 5 + test | 30min |
| Fri 7/25 | Validate + launch | 1h |
| Mon 7/29 | First customer | **$500-$1K** |

**Total: 4 hours of actual build time. Start now.**
