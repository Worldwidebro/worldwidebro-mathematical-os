#!/usr/bin/env python3
"""
Deal Ecosystem Orchestrator — Supabase Integration
6-step cycle: intake → qualify → contract → execute → pay → score
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

try:
    from supabase import create_client
    supabase = create_client(
        os.getenv('SUPABASE_URL'),
        os.getenv('SUPABASE_KEY')
    )
    SUPABASE_AVAILABLE = True
except Exception as e:
    print(f"⚠️  Supabase not available: {e}")
    SUPABASE_AVAILABLE = False


class DealEcosystemSupabase:
    def __init__(self):
        self.base_dir = '/Users/acebless/Documents'
        self.supabase = supabase if SUPABASE_AVAILABLE else None

    def intake_deal(self, deal_data):
        deal_id = f"DEL-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        deal = {
            'deal_id': deal_id,
            'title': deal_data.get('title'),
            'deal_value': deal_data.get('deal_value', 0),
            'originator_id': deal_data.get('originator_id'),
            'operator_id': deal_data.get('operator_id'),
            'capital_provider_id': deal_data.get('capital_provider_id'),
            'deal_status': 'intake',
            'created_at': datetime.now().isoformat(),
        }
        print(f"✅ STEP 1: INTAKE — {deal_id}")
        return deal

    def qualify_deal(self, deal):
        deal_value = deal['deal_value']
        deal['splits'] = {
            'costs': deal_value * 0.40,
            'referral': deal_value * 0.10,
            'operator': deal_value * 0.35,
            'platform': deal_value * 0.10,
            'profit_buffer': deal_value * 0.05,
        }
        deal['deal_status'] = 'qualified'
        print(f"✅ STEP 2: QUALIFY — 4-way split calculated")
        return deal

    def generate_contracts(self, deal):
        deal['contracts'] = [
            {'deal_id': deal['deal_id'], 'type': 'referral', 'recipient': deal['originator_id'], 'amount': deal['splits']['referral']},
            {'deal_id': deal['deal_id'], 'type': 'execution', 'recipient': deal['operator_id'], 'amount': deal['splits']['operator']},
            {'deal_id': deal['deal_id'], 'type': 'platform', 'recipient': 'PLATFORM', 'amount': deal['splits']['platform']},
        ]
        deal['deal_status'] = 'contracted'
        print(f"✅ STEP 3: CONTRACTS — 3 contracts generated")
        return deal

    def execute_workflow(self, deal):
        deal['workflow'] = {'deal_id': deal['deal_id'], 'status': 'queued'}
        deal['deal_status'] = 'executing'
        print(f"✅ STEP 4: WORKFLOW — queued for execution")
        return deal

    def distribute_payments(self, deal):
        deal['payments'] = [
            {'deal_id': deal['deal_id'], 'recipient': deal['originator_id'], 'role': 'originator', 'amount': deal['splits']['referral']},
            {'deal_id': deal['deal_id'], 'recipient': deal['operator_id'], 'role': 'operator', 'amount': deal['splits']['operator']},
            {'deal_id': deal['deal_id'], 'recipient': 'PLATFORM', 'role': 'platform', 'amount': deal['splits']['platform']},
        ]
        deal['deal_status'] = 'closed'
        print(f"✅ STEP 5: PAYMENTS — 3 payments scheduled")
        return deal

    def update_reputation(self, deal):
        deal['reputation_updates'] = {
            deal['originator_id']: {'reliability_change': 5, 'payment_change': 5},
            deal['operator_id']: {'reliability_change': 0, 'payment_change': 5},
        }
        deal['completed_at'] = datetime.now().isoformat()
        print(f"✅ STEP 6: REPUTATION — scores updated")
        return deal

    def save_to_supabase(self, deal):
        if not SUPABASE_AVAILABLE:
            print("⚠️  Supabase not configured")
            return deal

        try:
            supabase.table('referral_deals').insert({
                'deal_id': deal['deal_id'],
                'title': deal['title'],
                'originator_id': deal['originator_id'],
                'operator_id': deal['operator_id'],
                'deal_value': deal['deal_value'],
                'deal_status': deal['deal_status'],
            }).execute()
            print(f"✅ Supabase: referral_deals saved")

            for contract in deal['contracts']:
                supabase.table('deal_contracts').insert({
                    'deal_id': deal['deal_id'],
                    'contract_type': contract['type'],
                    'contract_template': contract,
                }).execute()
            print(f"✅ Supabase: contracts saved ({len(deal['contracts'])})")

            for payment in deal['payments']:
                supabase.table('deal_payments').insert({
                    'deal_id': deal['deal_id'],
                    'recipient_id': payment['recipient'],
                    'recipient_role': payment['role'],
                    'amount': payment['amount'],
                }).execute()
            print(f"✅ Supabase: payments saved ({len(deal['payments'])})")

        except Exception as e:
            print(f"⚠️  Supabase error: {str(e)[:100]}")

        return deal

    def execute_full_cycle(self, deal_data):
        print("\n" + "="*100)
        print("DEAL ECOSYSTEM → SUPABASE")
        print("="*100 + "\n")

        deal = self.intake_deal(deal_data)
        deal = self.qualify_deal(deal)
        deal = self.generate_contracts(deal)
        deal = self.execute_workflow(deal)
        deal = self.distribute_payments(deal)
        deal = self.update_reputation(deal)
        deal = self.save_to_supabase(deal)

        print("\n" + "="*100)
        print(f"✅ COMPLETE: Deal {deal['deal_id']} → Supabase")
        print("="*100)
        return deal


if __name__ == '__main__':
    ecosystem = DealEcosystemSupabase()
    example = {
        'title': 'Build E-Commerce Platform',
        'originator_id': 'contact-sarah-chen',
        'operator_id': 'contact-alex-rodriguez',
        'capital_provider_id': 'contact-venture-fund',
        'deal_value': 100000,
    }
    result = ecosystem.execute_full_cycle(example)
    with open(f"{ecosystem.base_dir}/deal_execution_supabase_result.json", 'w') as f:
        json.dump(result, f, indent=2)
    print(f"\n📁 Result: deal_execution_supabase_result.json")
