import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL || '',
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || ''
);

export default async function handler(req: any, res: any) {
  if (req.method !== 'POST') return res.status(405).end();
  const { email, budget, venture_id } = req.body;
  const now = new Date().toISOString();
  try {
    const { data, error } = await supabase.from('lead_intake').insert([{
      email, budget, venture_id: venture_id || 'STA-001', status: 'new', created_at: now,
    }]);
    if (error) throw error;
    console.log(`[${now}] ✅ Lead: ${email} | $${budget} | ${venture_id}`);
    res.status(200).json({ lead_id: (data as any)?.[0]?.id || 'pending', created_at: now });
  } catch (err: any) {
    res.status(500).json({ error: err.message });
  }
}
