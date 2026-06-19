import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.38.4';

const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
);

interface TransactionRow {
  amount: number;
}

interface MetricsRow {
  week_of: string;
  revenue_mrr: number;
  revenue_growth_pct: number | null;
}

export async function calculateMRR(): Promise<Response> {
  try {
    // Get all active subscriptions
    const { data: transactions, error: selectError } = await supabase
      .from('spending_transaction')
      .select('amount')
      .eq('type', 'subscription')
      .eq('status', 'active') as { data: TransactionRow[] | null; error: any };

    if (selectError) throw selectError;

    const currentMRR = (transactions || []).reduce((sum, t) => sum + t.amount, 0);

    // Get previous week's MRR for growth calculation
    const lastWeek = new Date();
    lastWeek.setDate(lastWeek.getDate() - 7);

    const { data: lastMetrics } = await supabase
      .from('metrics_weekly')
      .select('revenue_mrr')
      .gte('week_of', lastWeek.toISOString())
      .order('week_of', { ascending: false })
      .limit(1) as { data: MetricsRow[] | null };

    const previousMRR = lastMetrics?.[0]?.revenue_mrr || 0;
    const growthPct = previousMRR > 0
      ? ((currentMRR - previousMRR) / previousMRR) * 100
      : 0;

    // Insert into metrics_weekly
    const { error: insertError } = await supabase
      .from('metrics_weekly')
      .insert({
        week_of: new Date().toISOString(),
        revenue_mrr: currentMRR,
        revenue_growth_pct: growthPct,
        followers: 0,
        community_members: 0,
        deals_sourced: 0,
        deals_closed: 0,
        sops_created: 0,
        content_pieces: 0,
        agents_deployed: 0,
      });

    if (insertError) throw insertError;

    console.log(
      `✅ MRR calculated: $${currentMRR.toFixed(2)} (${growthPct > 0 ? '+' : ''}${growthPct.toFixed(1)}% growth)`
    );

    return new Response(
      JSON.stringify({
        success: true,
        mrr: currentMRR,
        growth_pct: growthPct,
        timestamp: new Date().toISOString(),
      }),
      {
        headers: { 'Content-Type': 'application/json' },
        status: 200,
      }
    );
  } catch (error) {
    console.error('MRR calculation error:', error);
    return new Response(
      JSON.stringify({
        error: error instanceof Error ? error.message : 'Unknown error',
      }),
      { headers: { 'Content-Type': 'application/json' }, status: 500 }
    );
  }
}

// Run on schedule: 6 AM daily
Deno.serve(calculateMRR);
