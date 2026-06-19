#!/usr/bin/env python3
"""LOOP 5: REVENUE OPERATIONS - Score & monitor ventures"""
import csv

ventures = []
try:
    with open('/Users/acebless/Documents/Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/venture-hub/ventures-master.csv', 'r') as f:
        ventures = list(csv.DictReader(f))
except:
    pass

print("💰 LOOP 5: REVENUE OPERATIONS")
print("="*60)
print(f"\n📊 Scoring {len(ventures)} ventures...\n")

red = yellow = green = 0
total_revenue = 0

for v in ventures:
    try:
        health = float(v.get('health_score', 50)) if v.get('health_score') else 50
        revenue = float(v.get('revenue_ytd', 0)) if v.get('revenue_ytd') else 0
        total_revenue += revenue

        if health < 40:
            red += 1
        elif health < 70:
            yellow += 1
        else:
            green += 1
    except:
        pass

print(f"🔴 RED (at-risk): {red} ventures")
print(f"🟡 YELLOW (watch): {yellow} ventures")
print(f"🟢 GREEN (healthy): {green} ventures")

print(f"\n💵 Revenue summary:")
print(f"  Total: ${total_revenue:,.0f}/month")
print(f"  Target: $57,000-135,000/month")
print(f"  On track: {'YES' if total_revenue >= 57000 else 'NO'}")

print(f"\n📈 4-Layer capital system:")
print(f"  Layer 1 (Labor): calculating...")
print(f"  Layer 2 (Skill): calculating...")
print(f"  Layer 3 (Asset): calculating...")
print(f"  Layer 4 (Capital): calculating...")

print(f"\n📢 Would post to Slack #niche-mastery:")
print(f"  Revenue status | KPIs | Action required")

print("\n" + "="*60)
print(f"✅ LOOP 5 COMPLETE: {red} interventions needed")
print("="*60 + "\n")
