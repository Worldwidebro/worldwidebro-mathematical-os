import type { NextApiRequest, NextApiResponse } from 'next';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.SUPABASE_URL || 'https://rhlkjelglvurowdalrgh.supabase.co';
const supabaseKey = process.env.SUPABASE_ANON_KEY || '';

const supabase = createClient(supabaseUrl, supabaseKey);

interface DashboardMetrics {
  activeAgents: number;
  totalAgents: number;
  tasksRunning: number;
  decisionsLive: number;
  totalCost: number;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<DashboardMetrics | { error: string }>
) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    // Query active ventures (ventures with stage = 'Revenue')
    const { data: ventures, error: venturesError } = await supabase
      .from('ventures')
      .select('id, stage, status')
      .eq('status', 'active');

    if (venturesError) throw venturesError;

    // Query active leads in pipeline
    const { data: leads, error: leadsError } = await supabase
      .from('venture_leads')
      .select('id, status')
      .in('status', ['contacted', 'qualified', 'proposal']);

    if (leadsError) throw leadsError;

    // Query total revenue (30 days)
    const thirtyDaysAgo = new Date();
    thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);

    const { data: payments, error: paymentsError } = await supabase
      .from('deal_payments')
      .select('amount')
      .gte('created_at', thirtyDaysAgo.toISOString());

    if (paymentsError) throw paymentsError;

    // Calculate metrics
    const activeAgents = ventures?.filter(v => v.stage === 'Revenue').length || 0;
    const tasksRunning = leads?.length || 0;
    const decisionsLive = Math.ceil((leads?.length || 0) * 0.15);
    const totalCost = payments?.reduce((sum: number, p: any) => sum + (p.amount || 0), 0) || 0;

    const metrics: DashboardMetrics = {
      activeAgents,
      totalAgents: 31,
      tasksRunning,
      decisionsLive,
      totalCost: Math.round(totalCost),
    };

    // Cache for 10 seconds (matches dashboard poll interval)
    res.setHeader('Cache-Control', 'public, max-age=10, s-maxage=10');
    res.status(200).json(metrics);
  } catch (error) {
    console.error('Dashboard metrics error:', error);
    res.status(500).json({
      error: error instanceof Error ? error.message : 'Failed to fetch metrics',
    });
  }
}
