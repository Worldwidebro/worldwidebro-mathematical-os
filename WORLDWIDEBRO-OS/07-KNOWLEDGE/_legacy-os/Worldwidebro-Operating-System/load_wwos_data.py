#!/usr/bin/env python3
"""
Worldwidebro Operating System - Data Loader
Loads WWOS data into Supabase tables
"""

import json
import csv
import os
from supabase import create_client, Client

# Initialize Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ ERROR: SUPABASE_URL and SUPABASE_KEY not set in .env")
    exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def load_cash_flow_calendar():
    """Load cash flow calendar from JSON"""
    try:
        with open('financial/CASH-FLOW-CALENDAR-2026.json', 'r') as f:
            data = json.load(f)

        for month_data in data['monthly_layers']:
            supabase.table('cash_flow_calendar').insert({
                'month': month_data['month'],
                'layer_1_services': month_data['layer_1_services'],
                'layer_2_products': month_data['layer_2_products'],
                'layer_3_acquisitions': month_data['layer_3_acquisitions'],
                'layer_4_capital': month_data['layer_4_capital'],
                'total_cash_in': month_data['total_cash_in'],
                'notes': month_data['notes']
            }).execute()

        print("✅ Cash flow calendar loaded (12 months)")
    except Exception as e:
        print(f"❌ Error loading cash flow: {e}")

def load_unit_economics():
    """Load unit economics from CSV"""
    try:
        with open('registries/UNIT-ECONOMICS-BY-VENTURE-TYPE.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                supabase.table('unit_economics').insert({
                    'venture_type': row['Venture_Type'],
                    'layer': int(row['Layer'].split('_')[1]) if '_' in row['Layer'] else None,
                    'revenue_model': row['Revenue_Model'],
                    'avg_monthly_revenue': row['Avg_Monthly_Revenue'],
                    'cogs_percent': int(row['COGS_Percent']) if row['COGS_Percent'].isdigit() else 0,
                    'operating_costs': int(row['Operating_Costs']) if row['Operating_Costs'].isdigit() else 0,
                    'monthly_profit': row['Monthly_Profit'],
                    'profit_margin_percent': row['Profit_Margin_Percent'],
                    'examples': row['Examples'],
                    'notes': row['Notes']
                }).execute()

        print("✅ Unit economics loaded (14 venture types)")
    except Exception as e:
        print(f"❌ Error loading unit economics: {e}")

def load_ventures_asset_classification():
    """Load ventures asset classification from CSV"""
    try:
        with open('portfolio/VENTURES-ASSET-CLASSIFICATION.csv', 'r') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                supabase.table('ventures_asset_classification').insert({
                    'venture_name': row['Venture_Name'],
                    'sector': row['Sector'],
                    'venture_type': row['Type'],
                    'asset_classification': row['Asset_Classification'],
                    'revenue_potential_1_5': int(row['Revenue_Potential_1_5']),
                    'strategic_value_1_5': int(row['Strategic_Value_1_5']),
                    'automation_potential_1_5': int(row['Automation_Potential_1_5']),
                    'competitive_advantage_1_5': int(row['Competitive_Advantage_1_5']),
                    'scalability_1_5': int(row['Scalability_1_5']),
                    'capital_efficiency_1_5': int(row['Capital_Efficiency_1_5']),
                    'asset_score_0_30': int(row['Asset_Score_0_30']),
                    'classification_rationale': row['Classification_Rationale'],
                    'monthly_profit_projection': row['Monthly_Profit_Projection'],
                    'status': row['Status']
                }).execute()
                count += 1

        print(f"✅ Ventures asset classification loaded ({count} ventures)")
    except Exception as e:
        print(f"❌ Error loading ventures: {e}")

def load_phases_completion():
    """Load 12-phase completion data"""
    phases = [
        (1, "Vision & Ecosystem Design", 60, 28, "✅ REFERENCE"),
        (2, "Industry & Money Flow Mapping", 70, 35, "✅ REFERENCE"),
        (3, "Company Formation", 50, 16, "✅ PARTIAL"),
        (4, "Contract Library", 40, 54, "❌ NOT STARTED"),
        (5, "Organization Design", 35, 44, "❌ NOT STARTED"),
        (6, "Compensation & Incentives", 85, 22, "✅ DONE"),
        (7, "Financial Architecture", 95, 35, "✅ DONE"),
        (8, "Venture Portfolio Management", 90, 196, "✅ DONE"),
        (9, "Operations System", 45, 44, "❌ NOT STARTED"),
        (10, "Communication System", 60, 17, "⚠️ PARTIAL"),
        (11, "Technology Stack", 65, 378, "⚠️ PARTIAL"),
        (12, "Scaling Roadmap", 70, 28, "✅ PARTIAL")
    ]

    try:
        for phase_num, phase_name, completion, repos, status in phases:
            supabase.table('phases_completion').insert({
                'phase_number': phase_num,
                'phase_name': phase_name,
                'completion_percent': completion,
                'repos_available': repos,
                'status': status
            }).execute()

        print("✅ 12-phase completion tracking loaded")
    except Exception as e:
        print(f"❌ Error loading phases: {e}")

def main():
    print("\n" + "="*80)
    print("WORLDWIDEBRO OPERATING SYSTEM - DATA LOADER")
    print("="*80)
    print("\nLoading data into Supabase...\n")

    load_cash_flow_calendar()
    load_unit_economics()
    load_ventures_asset_classification()
    load_phases_completion()

    print("\n" + "="*80)
    print("✅ WWOS DATA LOAD COMPLETE")
    print("="*80)
    print("\nNext: Run obsidian_graph_sync.py to sync to Obsidian dashboard\n")

if __name__ == "__main__":
    main()
