import { createClient } from '@supabase/supabase-js';
import type { NextRequest } from 'next/server';

const supabase = createClient(
  process.env.SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
);

export const runtime = 'edge';

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { email, budget, venture_id, name, company, message, source } = body;

    if (!email || typeof email !== 'string') {
      return Response.json({ error: 'email is required' }, { status: 400 });
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return Response.json({ error: 'invalid email format' }, { status: 400 });
    }

    const now = new Date().toISOString();
    const { data, error } = await supabase
      .from('venture_leads')
      .insert([{
        email: email.toLowerCase().trim(),
        budget: budget ?? null,
        venture_id: venture_id || 'STA-001',
        status: 'new',
        name: name ?? null,
        company: company ?? null,
        message: message ?? null,
        source: source ?? 'hermes-api',
        created_at: now,
        updated_at: now,
      }])
      .select()
      .single();

    if (error) {
      console.error('[leads] insert error:', error);
      return Response.json({ error: 'failed to create lead', details: error.message }, { status: 500 });
    }

    return Response.json({ success: true, lead_id: data.id, message: 'Lead captured successfully' }, { status: 201 });
  } catch (err) {
    console.error('[leads] unexpected error:', err);
    return Response.json({ error: 'internal server error' }, { status: 500 });
  }
}

async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const venture_id = searchParams.get('venture_id');
  const status = searchParams.get('status');
  const limit = parseInt(searchParams.get('limit') || '50', 10);

  let query = supabase.from('venture_leads').select('*').order('created_at', { ascending: false }).limit(limit);

  if (venture_id) query = query.eq('venture_id', venture_id);
  if (status) query = query.eq('status', status);

  const { data, error } = await query;

  if (error) {
    return Response.json({ error: error.message }, { status: 500 });
  }

  return Response.json({ leads: data, count: data?.length ?? 0 });
}

export default POST;
