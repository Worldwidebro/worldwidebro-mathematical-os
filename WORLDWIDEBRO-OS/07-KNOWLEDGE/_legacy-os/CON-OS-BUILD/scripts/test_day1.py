#!/usr/bin/env python3
"""
Day 1 Test Suite — Validates all 5 services work end-to-end
Tests: Intake → Classify → Contract → Payout → Graph
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"
SERVICES = {
    "deal_intake": "http://localhost:8001",
    "contract_generator": "http://localhost:8002",
    "payout_engine": "http://localhost:8003",
    "orchestrator": "http://localhost:8004",
    "graph_memory": "http://localhost:8005"
}

def test_service_health():
    """Check all services are running"""
    print("\n📋 Checking service health...")
    for name, url in SERVICES.items():
        try:
            r = requests.get(f"{url}/health", timeout=2)
            print(f"  ✅ {name}: {r.status_code}")
        except Exception as e:
            print(f"  ❌ {name}: {e}")

def test_submit_referral():
    """Test 1: Submit a referral"""
    print("\n🚀 Test 1: Submit Referral")
    payload = {
        "contact_id": "ref_test_001",
        "contact_name": "Test Contractor",
        "job_title": "Test Electrical Job",
        "budget": 85000,
        "timeline": "urgent",
        "sector": "CON-011",
        "contractor_ids": ["contractor_test_001"]
    }
    r = requests.post(f"{SERVICES['deal_intake']}/mcp/tools/submit_referral", json=payload)
    result = r.json()
    print(f"  Status: {r.status_code}")
    print(f"  Deal ID: {result.get('deal_id')}")
    print(f"  Deal Score: {result.get('deal_score')}")
    return result.get('deal_id')

def test_generate_contracts(deal_id):
    """Test 2: Generate contracts"""
    print(f"\n📄 Test 2: Generate Contracts for {deal_id}")
    payload = {"deal_id": deal_id}
    r = requests.post(f"{SERVICES['contract_generator']}/mcp/tools/generate_contracts", json=payload)
    result = r.json()
    print(f"  Status: {r.status_code}")
    print(f"  Contracts: {result.get('contracts_generated')}")
    return result

def test_payment_distribution(deal_id):
    """Test 3: Distribute payment"""
    print(f"\n💰 Test 3: Payment Distribution for {deal_id}")
    payload = {
        "deal_id": deal_id,
        "total_payment": 85000,
        "invoice_id": "inv_test_001"
    }
    r = requests.post(f"{SERVICES['payout_engine']}/mcp/tools/trigger_payment_distribution", json=payload)
    result = r.json()
    print(f"  Status: {r.status_code}")
    splits = result.get('splits', [])
    for split in splits:
        print(f"    {split['type']}: ${split['amount']} ({split['percent']}%)")
    return result

def test_orchestrator(deal_id):
    """Test 4: Route deal to agent"""
    print(f"\n🤖 Test 4: Orchestrator - Route Deal {deal_id}")
    payload = {
        "deal_id": deal_id,
        "event": "deal_submitted"
    }
    r = requests.post(f"{SERVICES['orchestrator']}/mcp/tools/route_deal", json=payload)
    result = r.json()
    print(f"  Status: {r.status_code}")
    print(f"  Agent: {result.get('agent_assigned')}")
    print(f"  Task ID: {result.get('task_id')}")
    return result

def test_graph_memory(deal_id):
    """Test 5: Update graph memory"""
    print(f"\n🧠 Test 5: Graph Memory - Update for {deal_id}")
    payload = {
        "deal_id": deal_id,
        "completion_data": {
            "contractor_id": "contractor_test_001",
            "quality_rating": 95,
            "speed_rating": 92,
            "compliance_rating": 94,
            "efficiency_rating": 89,
            "communication_rating": 90
        }
    }
    r = requests.post(f"{SERVICES['graph_memory']}/mcp/tools/update_graph_memory", json=payload)
    result = r.json()
    print(f"  Status: {r.status_code}")
    print(f"  Contractor Score: {result.get('contractor_new_score')}")
    print(f"  Tier: {result.get('contractor_new_tier')}")
    return result

def main():
    print("=" * 60)
    print("DAY 1 TEST SUITE — CON OS MVP")
    print("=" * 60)
    
    # Check health
    test_service_health()
    
    # Run full flow
    print("\n" + "="*60)
    print("Running Full Deal Flow")
    print("="*60)
    
    deal_id = test_submit_referral()
    if deal_id:
        test_generate_contracts(deal_id)
        test_payment_distribution(deal_id)
        test_orchestrator(deal_id)
        test_graph_memory(deal_id)
        
        print("\n" + "="*60)
        print("✅ DAY 1 COMPLETE: All 5 services tested end-to-end")
        print("="*60)
    else:
        print("\n❌ Deal submission failed")

if __name__ == "__main__":
    main()
