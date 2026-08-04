import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

export async function registerDeal(deal: any) {
  return supabase.from('deal_registration').insert([{ ...deal, status: 'registered' }]).select();
}

export async function markDealWon(deal_id: string) {
  await supabase.from('deal_registration').update({ status: 'won' }).eq('id', deal_id);

  const { data: deal } = await supabase
    .from('deal_registration')
    .select('partner_id, opportunity_value')
    .eq('id', deal_id)
    .single();

  const { data: partner } = await supabase
    .from('partners')
    .select('commission_pct')
    .eq('id', deal.partner_id)
    .single();

  return supabase.from('commissions').insert([{
    partner_id: deal.partner_id,
    deal_id,
    revenue: deal.opportunity_value,
    commission_pct: partner.commission_pct,
    status: 'calculated',
  }]).select();
}

export async function getPartnerDashboard(partner_id: string) {
  const { data: partner } = await supabase.from('partners').select('*').eq('id', partner_id).single();
  const { data: deals } = await supabase.from('deal_registration').select('status').eq('partner_id', partner_id);
  const { data: commissions } = await supabase.from('commissions').select('*').eq('partner_id', partner_id);

  return {
    partner,
    deals: deals || [],
    commissions: commissions || [],
  };
}

export async function getCustomerLicenses(customer_id: string) {
  const { data } = await supabase.from('customers').select('licenses, license_tier').eq('id', customer_id).single();
  return data;
}

export async function getPricingTiers() {
  const { data } = await supabase.from('pricing_tiers').select('*').eq('active', true).order('price');
  return data;
}
