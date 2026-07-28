#!/usr/bin/env python3
"""
simulate_deal_flow.py - Simulates the AI Deal Team pipeline for DEAL-001 (Worldwidebro Deal Flow Agency)
focusing on high-value B2B deals in Charlotte, NC.
"""

import sys
import sqlite3
import json
import datetime as dt

# Emojis for beautiful visualization
INFO = "ℹ️"
SUCCESS = "✅"
DISCOVERY = "🔍"
QUALIFY = "⚖️"
MATCH = "🤝"
OUTREACH = "📧"
FINANCE = "💰"
CLOSING = "✍️"

def load_simple_yaml(path):
    """
    A lightweight custom parser to read basic yaml structures in the registries
    without external dependencies like PyYAML.
    """
    data = {}
    current_list_name = None
    current_item = None
    
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            # Strip comments and whitespace
            line = line.split('#')[0].strip()
            if not line:
                continue
            
            # Check for root list definition like 'agents:' or 'ventures:'
            if line.endswith(':'):
                current_list_name = line[:-1].strip()
                data[current_list_name] = []
                continue
                
            # Check for list item '- key: val' or new list element '-'
            if line.startswith('-'):
                # Extract key value from the list element line
                line_content = line[1:].strip()
                current_item = {}
                if current_list_name:
                    data[current_list_name].append(current_item)
                
                if not line_content:
                    continue
                line = line_content
                
            if ':' in line and current_item is not None:
                k, v = line.split(':', 1)
                k = k.strip()
                v = v.strip()
                # Clean up array notation like [x, y, z]
                if v.startswith('[') and v.endswith(']'):
                    v = [x.strip().strip("'\"") for x in v[1:-1].split(',') if x.strip()]
                # Clean up quotes
                elif (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                    v = v[1:-1]
                current_item[k] = v
    return data

def log_step(agent, step_name, msg, emoji="🚀"):
    print(f"\n{emoji} [{agent}] {step_name}")
    print(f"   ↳ {msg}")

def main():
    print("=" * 70)
    print("      WORLDWIDEBRO HOLDINGS: B2B DEAL FLOW AGENCY SIMULATION (DEAL-001)      ")
    print("=" * 70)

    # 1. Registry Vetting
    print(f"{INFO} Loading and validating registries...")
    try:
        agents = load_simple_yaml("registry/agents.yaml")
        ventures = load_simple_yaml("registry/ventures.yaml")
        print(f"{SUCCESS} Loaded {len(agents.get('agents', []))} registered agents.")
        print(f"{SUCCESS} Loaded {len(ventures.get('ventures', []))} registered ventures (DEAL-001 verified).")
    except Exception as e:
        print(f"❌ Error loading registries: {e}")
        sys.exit(1)

    # 2. Database Schema setup (SQLite memory DB representing Supabase)
    print(f"\n{INFO} Setting up in-memory transaction database (Staging)...")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Create the tables
    cursor.execute("""
    CREATE TABLE companies (
      company_id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      industry TEXT NOT NULL,
      location TEXT NOT NULL,
      company_size TEXT,
      estimated_revenue DECIMAL(12,2)
    )""")
    
    cursor.execute("""
    CREATE TABLE assets (
      asset_id TEXT PRIMARY KEY,
      asset_type TEXT NOT NULL,
      owner_company_id TEXT REFERENCES companies(company_id),
      estimated_value DECIMAL(12,2),
      location TEXT NOT NULL,
      availability_status TEXT
    )""")

    cursor.execute("""
    CREATE TABLE needs (
      need_id TEXT PRIMARY KEY,
      buyer_company_id TEXT REFERENCES companies(company_id),
      requirement_type TEXT NOT NULL,
      budget DECIMAL(12,2),
      deadline TEXT
    )""")

    cursor.execute("""
    CREATE TABLE deals (
      deal_id TEXT PRIMARY KEY,
      seller_company_id TEXT REFERENCES companies(company_id),
      buyer_company_id TEXT REFERENCES companies(company_id),
      asset_id TEXT REFERENCES assets(asset_id),
      need_id TEXT REFERENCES needs(need_id),
      contract_value DECIMAL(12,2) NOT NULL,
      commission_pct DECIMAL(5,4),
      commission_fee DECIMAL(12,2),
      status TEXT,
      created_at TEXT,
      closed_at TEXT
    )""")
    print(f"{SUCCESS} PostgreSQL/Supabase tables emulated successfully.")

    # 3. Simulate Pipeline
    # Step A: Opportunity Discovery
    log_step(
        "Opportunity Discovery Agent",
        "Scraping Charlotte B2B registries & liquidation files",
        "Discovered raw asset AST-201 (Caterpillar Excavator, $200K) at 'Queen City Excavation'\n"
        "   Discovered raw requirement NED-301 (Site grading machinery, $250K budget) at 'Metrolina Logistics Hub'",
        DISCOVERY
    )
    
    # Insert companies into db
    cursor.executemany("INSERT INTO companies VALUES (?, ?, ?, ?, ?, ?)", [
        ('COM-101', 'Queen City Excavation', 'Construction', 'Charlotte, NC', 'Medium', 4500000.00),
        ('COM-102', 'Metrolina Logistics Hub', 'Transportation', 'Charlotte, NC', 'Large', 28000000.00)
    ])
    
    # Insert asset & need
    cursor.execute("INSERT INTO assets VALUES (?, ?, ?, ?, ?, ?)", 
                   ('AST-201', 'equipment', 'COM-101', 200000.00, 'Charlotte, NC', 'immediate'))
    cursor.execute("INSERT INTO needs VALUES (?, ?, ?, ?, ?)", 
                   ('NED-301', 'COM-102', 'materials_procurement', 250000.00, '2026-09-01'))
    
    # Step B: Lead Qualification
    log_step(
        "Lead Qualification Agent",
        "Validating asset ownership and financial liquidity",
        "Verified: 'Queen City Excavation' owns title to AST-201. 'Metrolina Logistics Hub' has active capital reservation.\n"
        "   Match quality score: 0.94/1.00 (Highly compatible). Lead status changed to: QUALIFIED.",
        QUALIFY
    )

    # Step C: Buyer Matching
    log_step(
        "Buyer Matching Agent",
        "Running Neo4j Graph Traversal & Matching Logic",
        "Successfully mapped relation: (:Company {name: 'Queen City Excavation'})-[:OWNS]->(:Asset {type: 'equipment'})"
        "-[:MATCHES {score: 0.94}]->(:Need {requirement: 'site_grading'})<-[:HAS_NEED]-(:Company {name: 'Metrolina Logistics Hub'}).",
        MATCH
    )

    # Step D: Outreach Agent
    outreach_email = """
    Subject: Commission Opportunity / Machinery Procurement Match - Charlotte Douglas Hub
    To: operations@metrolinalogistics.com
    
    Dear Operations Lead,
    We have identified a qualified, immediately available Caterpillar 320 Excavator located in Charlotte, NC, 
    matching your active site grading infrastructure expansion request (Ref: NED-301). 
    We can arrange an introduction and facilitate transfer terms within 48 hours. 
    
    Best regards,
    Worldwidebro Deal Flow Agency
    """
    log_step(
        "Outreach Agent",
        "Initiating target buyer outbound engagement",
        f"Drafted cold proposal to Metrolina Logistics Hub operations team:\n{outreach_email}",
        OUTREACH
    )

    # Step E: Negotiation & Transaction Structuring
    log_step(
        "Negotiation Agent",
        "Structuring commission terms & pricing margins",
        "Calculated broker referral parameters:\n"
        "   - Asset value: $200,000.00\n"
        "   - Proposed commission: 5% flat fee\n"
        "   - Potential commission payout: $10,000.00",
        FINANCE
    )

    # Step F: Contract Agent
    log_step(
        "Contract Agent",
        "Issuing B2B Referral & Finder Fee Contract",
        "Generated standard B2B Finder Agreement between 'Worldwidebro Deal Flow Agency', "
        "'Queen City Excavation', and 'Metrolina Logistics Hub'. Escrow contract signed electronically.",
        CLOSING
    )

    # Post Deal completion to Database
    cursor.execute("""
    INSERT INTO deals (deal_id, seller_company_id, buyer_company_id, asset_id, need_id, contract_value, commission_pct, commission_fee, status, created_at, closed_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        'DL-501', 'COM-101', 'COM-102', 'AST-201', 'NED-301', 
        200000.00, 0.05, 10000.00, 'closed_won', 
        dt.datetime.now().isoformat(), dt.datetime.now().isoformat()
    ))
    conn.commit()

    # 4. REPORT REVENUE & METRICS
    print("\n" + "=" * 70)
    print("                DEAL FLOW PIPELINE STATUS & METRICS REPORT               ")
    print("=" * 70)
    
    cursor.execute("""
    SELECT d.deal_id, c1.name as seller, c2.name as buyer, d.contract_value, d.commission_fee, d.status 
    FROM deals d
    JOIN companies c1 ON d.seller_company_id = c1.company_id
    JOIN companies c2 ON d.buyer_company_id = c2.company_id
    """)
    res = cursor.fetchone()
    
    print(f"📈 Active Venture:       Worldwidebro Deal Flow Agency (DEAL-001)")
    print(f"🔑 Deal Reference:       {res[0]}")
    print(f"🏢 Seller Company:       {res[1]}")
    print(f"🏢 Buyer Company:        {res[2]}")
    print(f"💰 Contract Value:       ${res[3]:,.2f}")
    print(f"💵 Commission Fee (5%):  ${res[4]:,.2f}")
    print(f"📊 Transaction Status:   {res[5].upper()}")
    print("-" * 70)
    print(f"🎯 Target Monthly Goal:  $10,000.00")
    print(f"🏆 Simulated Payout:     ${res[4]:,.2f} (100% of Monthly Target Hit)")
    print("=" * 70)
    
    conn.close()

if __name__ == "__main__":
    main()
