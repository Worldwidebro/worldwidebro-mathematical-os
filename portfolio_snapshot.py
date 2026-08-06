#!/usr/bin/env python3
"""Generate portfolio snapshot: 7 core ventures + synergies + blockers."""

import json
from datetime import datetime

# 7 Core Ventures with KPI targets from the portfolio architecture
CORE_VENTURES = {
    "RE-001": {
        "name": "Real Estate Holdings",
        "role": "Asset Backbone",
        "sector": "real_estate",
        "readiness": 3.5,
        "kpis": {
            "cap_rate": {"target": ">=7%", "current": "TBD"},
            "occupancy": {"target": ">=95%", "current": "TBD"},
            "tenant_retention": {"target": ">=80%", "current": "TBD"},
            "internal_leasing_savings": {"target": "15-20%", "current": "0%"}
        },
        "synergies": ["LT-005", "LT-011", "EC-001", "EC-112"],
        "repos": ["re-001-property-holdings"],
        "blockers": ["Repo archived", "Vercel deployment pending"]
    },
    "LT-005": {
        "name": "Medical Courier Dispatch",
        "role": "Specialized Last-Mile + Healthcare Compliance",
        "sector": "logistics",
        "readiness": 68.0,
        "kpis": {
            "delivery_sla": {"target": "<2hr", "current": "TBD"},
            "damage_rate": {"target": "<1%", "current": "TBD"},
            "discreet_packaging": {"target": "100%", "current": "TBD"},
            "order_upgrade_frequency": {"target": ">5%", "current": "0%"}
        },
        "synergies": ["RE-001", "EC-112", "LT-011"],
        "repos": ["lt-005-medical-courier-dispatch"],
        "blockers": ["Repo archived", "Integration with LT-011 pending"]
    },
    "LT-011": {
        "name": "Dispatch Software (Techwolf)",
        "role": "Exclusive Logistics Platform + Order Management",
        "sector": "logistics",
        "readiness": 45.0,
        "kpis": {
            "platform_uptime": {"target": "99.9%", "current": "TBD"},
            "order_processing_time": {"target": "<30s", "current": "TBD"},
            "customer_adoption": {"target": ">80%", "current": "TBD"},
            "api_integration_rate": {"target": ">90%", "current": "0%"}
        },
        "synergies": ["LT-005", "RE-001", "CON-001", "EC-001"],
        "repos": ["lt-011-dispatch-software"],
        "blockers": ["Backend REST APIs partially wired", "Customer portal MVP incomplete"]
    },
    "OPS-001": {
        "name": "Staffing & HR Operations",
        "role": "Internal Staffing + Payroll + Talent Marketplace",
        "sector": "operations",
        "readiness": 25.0,
        "kpis": {
            "hiring_cost_reduction": {"target": "30%", "current": "0%"},
            "internal_placement_rate": {"target": ">70%", "current": "0%"},
            "payroll_accuracy": {"target": "100%", "current": "TBD"},
            "call_list_conversion": {"target": ">15%", "current": "0% (74 prospects identified)"}
        },
        "synergies": ["ALL"],
        "repos": ["ops-staff-001-staffing"],
        "blockers": ["12 HIGH-priority call scripts written but not executed", "Career ops portal needs live sync"]
    },
    "CON-001": {
        "name": "Construction OS (Ace Construction)",
        "role": "Builder + Real Estate Verticals + Supplier Control",
        "sector": "construction",
        "readiness": 10.0,
        "kpis": {
            "cost_advantage": {"target": "15% cheaper", "current": "TBD"},
            "project_margin": {"target": ">25%", "current": "TBD"},
            "supplier_financing": {"target": "Internal only", "current": "0%"},
            "re_001_integration": {"target": "100%", "current": "0%"}
        },
        "synergies": ["RE-001", "FIN-001"],
        "repos": ["con-001-ace-construction"],
        "blockers": ["Supabase project setup incomplete", "Instagram funnel not deployed"]
    },
    "FIN-001": {
        "name": "GenixBank Lite + Treasury",
        "role": "Central Financial Infrastructure + Processing + Internal Lending",
        "sector": "financial",
        "readiness": 41.0,
        "kpis": {
            "internal_processing_rate": {"target": "1% cheaper", "current": "TBD"},
            "ec_processing_capture": {"target": "100%", "current": "0%"},
            "internal_loan_rate": {"target": "Favorable", "current": "N/A"},
            "cash_sweep_rate": {"target": ">=70%", "current": "0%"}
        },
        "synergies": ["EC-112", "EC-001", "CON-001", "LT-005"],
        "repos": ["fin-001-genixbank-lite"],
        "blockers": ["Trading MCP integration pending", "Supabase webhook setup incomplete"]
    },
    "EC-112": {
        "name": "Cosmic Kitty (Adult E-Commerce)",
        "role": "Cash Flow Generator + Funnel Testbed",
        "sector": "e_commerce",
        "readiness": 55.0,
        "kpis": {
            "ltv_cac_ratio": {"target": ">5x", "current": "TBD"},
            "aov": {"target": ">$85", "current": "TBD"},
            "return_rate": {"target": "<8%", "current": "TBD"},
            "internal_checkout": {"target": "100%", "current": "0%"}
        },
        "synergies": ["FIN-001", "LT-005", "LT-011", "RE-001"],
        "repos": ["ec-112-cosmic-kitty"],
        "blockers": ["Medusa backend wired but storefront pending", "Stripe integration incomplete", "Railway deploy blocked"]
    }
}

# Top synergy opportunities
SYNERGY_MATRIX = {
    "RE-001 → LT-005/LT-011": {
        "type": "Space Lease",
        "description": "RE-001 warehouse/space to LT-005 & LT-011",
        "savings": "15-20% lease cost reduction",
        "status": "Blocked: RE-001 archived"
    },
    "FIN-001 → EC-112/EC-001": {
        "type": "Payment Processing",
        "description": "FIN-001 processes all EC transactions, captures fees",
        "savings": "$50-200K annual processing fees",
        "status": "Blocked: Stripe webhook missing"
    },
    "OPS-001 → ALL": {
        "type": "Staffing",
        "description": "OPS-001 fills all ventures' hiring needs, reduces external recruiter spend",
        "savings": "30% hiring cost reduction",
        "status": "Blocked: 74 prospects, 12 scripts, 0 calls placed"
    },
    "CON-001 → RE-001": {
        "type": "Construction",
        "description": "CON-001 builds/renovates RE-001 properties, supplies tenants",
        "savings": "15% construction cost + 10% supply cost",
        "status": "Blocked: CON-001 not wired to RE-001"
    },
    "LT-011 → EC-112/EC-001": {
        "type": "Fulfillment",
        "description": "LT-011 provides order routing + dispatch for EC stores",
        "savings": "$50-100K annual logistics consolidation",
        "status": "Blocked: API integration 0%"
    },
    "FIN-001 → CON-001": {
        "type": "Supply Financing",
        "description": "FIN-001 finances supplier relationships, improves CON-001 margins",
        "savings": "2-5% cost of capital advantage",
        "status": "Not started"
    }
}

# Top blockers preventing synergy activation
BLOCKERS = [
    {
        "id": "B001",
        "type": "Archive Debt",
        "ventures": ["RE-001", "LT-005"],
        "description": "RE-001 and LT-005 repos archived July 29; cannot deploy or integrate",
        "impact": "15-20% savings frozen",
        "action": "Restore RE-001 from archive"
    },
    {
        "id": "B002",
        "type": "API Integration",
        "ventures": ["LT-011", "EC-112", "EC-001"],
        "description": "LT-011 dispatch APIs not wired to EC checkout; orders not routing",
        "impact": "$50-100K logistics savings",
        "action": "Complete LT-011 REST API wiring (3 endpoints: orders, tracking, invoicing)"
    },
    {
        "id": "B003",
        "type": "Payment Processing",
        "ventures": ["FIN-001", "EC-112"],
        "description": "EC-112 Stripe webhooks not connected to FIN-001 treasury; no payment capture",
        "impact": "$50-200K annual processing fee capture",
        "action": "Wire Supabase webhook → FIN-001 payment collection"
    },
    {
        "id": "B004",
        "type": "Staffing Execution",
        "ventures": ["OPS-001"],
        "description": "74 HIGH-priority prospects identified, 12 call scripts written, 0 calls placed",
        "impact": "$150K-300K initial revenue",
        "action": "Execute call list immediately (5 calls/day × 74 prospects = Week 3 completion)"
    },
    {
        "id": "B005",
        "type": "Construction Integration",
        "ventures": ["CON-001", "RE-001"],
        "description": "CON-001 not linked to RE-001; no property management integration",
        "impact": "15% construction cost + 10% supply cost savings",
        "action": "Map CON-001 projects to RE-001 properties; wire Supabase"
    }
]

print("=" * 80)
print("WORLDWIDEBRO PORTFOLIO SNAPSHOT")
print("=" * 80)
print(f"Generated: {datetime.now().isoformat()}")
print(f"Core Ventures: 7")
print(f"Total Readiness (Avg): {sum(v['readiness'] for v in CORE_VENTURES.values()) / len(CORE_VENTURES):.1f}%")
print()

print("7 CORE VENTURES:")
print("-" * 80)
for vid, v in CORE_VENTURES.items():
    print(f"\n{vid}: {v['name']}")
    print(f"  Role: {v['role']}")
    print(f"  Readiness: {v['readiness']}%")
    print(f"  Synergies: {', '.join(v['synergies'])}")
    print(f"  Blockers: {len(v['blockers'])} (see details below)")

print("\n" + "=" * 80)
print("TOP SYNERGY OPPORTUNITIES:")
print("=" * 80)
for syn, details in SYNERGY_MATRIX.items():
    print(f"\n{syn}")
    print(f"  Type: {details['type']}")
    print(f"  Savings: {details['savings']}")
    print(f"  Status: {details['status']}")

print("\n" + "=" * 80)
print("TOP 5 BLOCKERS (Preventing $400K-800K Synergy Activation):")
print("=" * 80)
for blocker in BLOCKERS:
    print(f"\n{blocker['id']}: {blocker['type']}")
    print(f"  Ventures: {', '.join(blocker['ventures'])}")
    print(f"  Impact: {blocker['impact']}")
    print(f"  Action: {blocker['action']}")

