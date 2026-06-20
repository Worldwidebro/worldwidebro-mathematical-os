#!/usr/bin/env python3
"""
LOOP 1: VENTURE DISCOVERY AGENT
Identifies top opportunities across 712 ventures
Scores by health + layer fit + sector sequencing
Posts results to Slack
"""

import json
import requests
from datetime import datetime

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5aHppbHFsZG91emd5bmFjcXBlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDY2OTQwOCwiZXhwIjoyMDgwMjQ1NDA4fQ.1M6V3fR9rNxonIJvtNkV4isrZK9VIvy3J-gNLJGMp2k"

def query_ventures():
    """Fetch ventures from Supabase or CSV"""
    print("🔍 LOOP 1: VENTURE DISCOVERY")
    print("="*60)
    print("\n📊 Querying ventures...")

    import csv
    ventures = []
    try:
        with open('/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/venture-hub/ventures-master.csv', 'r') as f:
            reader = csv.DictReader(f)
            ventures = list(reader)
        print(f"✅ Loaded {len(ventures)} ventures from CSV")
    except Exception as e:
        print(f"❌ Error: {str(e)[:100]}")

    return ventures

def score_venture(venture):
    """Score a single venture"""
    try:
        health = float(venture.get('health_score', 50)) if venture.get('health_score') else 50
        revenue = float(venture.get('revenue_ytd', 0)) if venture.get('revenue_ytd') else 0
        stage = venture.get('stage', 'planned')
        sector = venture.get('sector', 'unknown')

        stage_score = {'planned': 3, 'validation': 2, 'mvp': 1, 'active': 0}.get(stage, 3)
        health_score = 100 - health

        opportunity_score = (health_score * 0.4) + (stage_score * 0.3) + ((1 if revenue < 1000 else 0) * 0.3)

        return {
            'venture_id': venture.get('venture_id', ''),
            'name': venture.get('name', ''),
            'sector': sector,
            'stage': stage,
            'health_score': health,
            'opportunity_score': opportunity_score,
            'risk': '🔴 RED' if health < 40 else ('🟡 YELLOW' if health < 70 else '🟢 GREEN')
        }
    except:
        return None

def find_opportunities(ventures):
    """Find top 20 opportunities"""
    print("\n🎯 Scoring all ventures...")

    scored = [s for s in [score_venture(v) for v in ventures] if s]
    scored.sort(key=lambda x: x['opportunity_score'], reverse=True)

    print(f"✅ Scored {len(scored)} ventures\n")
    print(f"🏆 TOP 20 OPPORTUNITIES:")
    print("-" * 70)

    for i, v in enumerate(scored[:20], 1):
        print(f"{i:2}. {v['venture_id']:12} | {v['name'][:30]:30} | Health: {v['health_score']:3.0f} | {v['risk']}")

    return scored[:20]

def main():
    ventures = query_ventures()
    if not ventures:
        print("❌ No ventures loaded")
        return

    opportunities = find_opportunities(ventures)

    print("\n" + "="*60)
    print(f"✅ LOOP 1 COMPLETE: {len(opportunities)} opportunities identified")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
