import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.38.4';

const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
);

const HUBSPOT_API_KEY = Deno.env.get('HUBSPOT_API_KEY');
const HUBSPOT_BASE_URL = 'https://api.hubapi.com';

interface HubSpotDeal {
  id: string;
  properties: {
    dealname?: string;
    dealstage?: string;
    amount?: string;
    closedate?: string;
    dealowner?: string;
    [key: string]: any;
  };
}

interface DealRecord {
  hubspot_id: string;
  dealname: string | null;
  dealstage: string | null;
  amount: number;
  closedate: string | null;
  dealowner: string | null;
  synced_at: string;
}

export async function syncHubSpotDeals(): Promise<Response> {
  try {
    let allDeals: HubSpotDeal[] = [];
    let after: string | undefined;

    while (true) {
      const url = new URL(`${HUBSPOT_BASE_URL}/crm/v3/objects/deals`);
      url.searchParams.append('limit', '100');
      url.searchParams.append(
        'properties',
        'dealname,dealstage,amount,closedate,dealowner'
      );

      if (after) {
        url.searchParams.append('after', after);
      }

      const response = await fetch(url.toString(), {
        headers: {
          Authorization: `Bearer ${HUBSPOT_API_KEY}`,
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HubSpot API error: ${response.statusText}`);
      }

      const data = await response.json();
      allDeals = allDeals.concat(data.results || []);

      if (!data.paging?.next?.after) {
        break;
      }
      after = data.paging.next.after;
    }

    const deals: DealRecord[] = allDeals.map((deal: HubSpotDeal) => ({
      hubspot_id: deal.id,
      dealname: deal.properties.dealname || null,
      dealstage: deal.properties.dealstage || null,
      amount: deal.properties.amount ? parseFloat(deal.properties.amount) : 0,
      closedate: deal.properties.closedate || null,
      dealowner: deal.properties.dealowner || null,
      synced_at: new Date().toISOString(),
    }));

    const { error: upsertError } = await supabase
      .from('hubspot_deals')
      .upsert(deals, { onConflict: 'hubspot_id' });

    if (upsertError) throw upsertError;

    console.log(`✅ Synced ${deals.length} deals from HubSpot`);

    return new Response(
      JSON.stringify({
        success: true,
        synced_count: deals.length,
        total_deal_value: deals.reduce((sum, d) => sum + d.amount, 0),
        timestamp: new Date().toISOString(),
      }),
      {
        headers: { 'Content-Type': 'application/json' },
        status: 200,
      }
    );
  } catch (error) {
    console.error('HubSpot deal sync error:', error);
    return new Response(
      JSON.stringify({
        error: error instanceof Error ? error.message : 'Unknown error',
      }),
      { headers: { 'Content-Type': 'application/json' }, status: 500 }
    );
  }
}

Deno.serve(syncHubSpotDeals);
