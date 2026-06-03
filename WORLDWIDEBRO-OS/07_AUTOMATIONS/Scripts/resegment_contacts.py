#!/usr/bin/env python3
import csv
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

# Read original CSV
contacts = []
with open('contacts-extracted.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['name']:
            contacts.append(row)

def get_tier_v2(warmth_score, industry, name, location):
    """Recalibrated tier logic"""
    warmth = int(warmth_score)
    
    # HOT: high warmth OR professional OR family OR Charlotte-based with known industry
    hot_industries = ['Legal/Law', 'Insurance/Finance', 'Beauty/Wellness']
    family_names = ['Dad', 'Mom', 'Mommy iphone']
    
    if warmth >= 8:
        return 'HOT'
    if any(industry.startswith(x) for x in hot_industries if x in industry):
        return 'HOT'
    if name in family_names:
        return 'HOT'
    
    # WARM: warmth 6+ OR Charlotte-based OR any known industry
    if warmth >= 6:
        return 'WARM'
    if 'Charlotte' in location or 'Charlotte' in (location or ''):
        return 'WARM'
    if industry != 'unknown':
        return 'WARM'
    
    # COLD: warmth 5, unknown industry, non-Charlotte
    return 'COLD'

# Clear existing and re-insert
supabase.table('contact_tiers').delete().neq('id', 0).execute()

segmented = []
tier_counts = {'HOT': 0, 'WARM': 0, 'COLD': 0}

for contact in contacts:
    tier = get_tier_v2(
        contact['warmth_score'],
        contact['industry_guess'],
        contact['name'],
        contact['location']
    )
    tier_counts[tier] += 1
    
    outreach = 'call' if tier == 'HOT' else ('whatsapp' if tier == 'WARM' else 'email')
    
    segmented.append({
        'contact_name': contact['name'],
        'contact_phone': contact['phone'],
        'contact_email': contact['email'] or None,
        'company': contact['company'] or None,
        'location': contact['location'],
        'industry_guess': contact['industry_guess'],
        'warmth_score': int(contact['warmth_score']),
        'tier': tier,
        'outreach_method': outreach,
        'outreach_status': 'pending'
    })

print(f"Revised Tier Breakdown:")
print(f"  HOT:  {tier_counts['HOT']:2d} contacts (direct calls)")
print(f"  WARM: {tier_counts['WARM']:2d} contacts (WhatsApp)")
print(f"  COLD: {tier_counts['COLD']:2d} contacts (email)")

# Insert in batches
batch_size = 10
for i in range(0, len(segmented), batch_size):
    batch = segmented[i:i+batch_size]
    supabase.table('contact_tiers').insert(batch).execute()
    print(f"  ✓ Batch {i//batch_size + 1}")

print(f"\n✅ Re-segmented and inserted {len(segmented)} contacts")
