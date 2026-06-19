#!/usr/bin/env python3
"""MCP Contract Engine — Referral → Contract → Splits Automation"""
import json, os
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client

load_dotenv("/Users/acebless/Documents/.env")
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def submit_referral(referrer_name: str, deal_title: str, deal_value: float, deal_type: str = "service"):
    """Submit referral → auto-generates contract + calculates splits"""
    print(f"\n📋 MCP: {referrer_name} → {deal_title} (${deal_value:,.0f})")
    
    # Get/create referrer
    ref = supabase.table('referrers').select('*').eq('name', referrer_name).execute()
    if not ref.data:
        nr = supabase.table('referrers').insert({'name': referrer_name, 'email': f"{referrer_name.lower().replace(' ', '.')}@ref.io", 'tier': 'tier_3', 'commission_rate': 10}).execute()
        ref_id = nr.data[0]['id']
    else:
        ref_id = ref.data[0]['id']
    
    # Create deal with split
    split = {'costs': 40, 'referrer': ref.data[0]['commission_rate'] if ref.data else 10, 'operator': 35, 'platform': 10}
    deal = supabase.table('deals').insert({'deal_type': deal_type, 'amount': deal_value, 'status': 'intake', 'metadata': {'title': deal_title, 'referrer_id': ref_id, 'split_model': split}}).execute()
    deal_id = deal.data[0]['id']
    
    # Auto-generate contract
    contract = supabase.table('contracts').insert({'deal_id': deal_id, 'contract_type': 'referral_agreement', 'parties': {'referrer_id': ref_id}, 'terms': {'referrer_pct': split['referrer'], 'operator_pct': split['operator'], 'platform_pct': split['platform']}}).execute()
    
    # Calculate splits
    ref_payout = deal_value * split['referrer'] / 100
    op_payout = deal_value * split['operator'] / 100
    plat_payout = deal_value * split['platform'] / 100
    
    # Update referrer score
    supabase.table('referrers').update({'total_deals_referred': (ref.data[0]['total_deals_referred'] if ref.data else 0) + 1, 'total_revenue_sourced': (ref.data[0]['total_revenue_sourced'] if ref.data else 0) + deal_value, 'trust_score': min(1.0, (ref.data[0]['trust_score'] if ref.data else 0.5) + 0.05)}).eq('id', ref_id).execute()
    
    return {'status': 'success', 'deal_id': str(deal_id), 'contract_id': str(contract.data[0]['id']), 'splits': {'referrer': f"${ref_payout:,.0f}", 'operator': f"${op_payout:,.0f}", 'platform': f"${plat_payout:,.0f}"}}

# Run example
result = submit_referral('Sarah Chen', 'Construction Site SaaS', 150000, 'saas_mvp')
print(f"✅ Result: {json.dumps(result, indent=2)}")
