#!/usr/bin/env python3
import csv
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load .env
load_dotenv()

# Initialize Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# Read contacts from CSV
contacts = []
with open('contacts-extracted.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['name']:  # Skip empty rows
            contacts.append(row)

print(f"Loaded {len(contacts)} contacts")

# Segmentation logic
def get_tier(warmth_score, industry, name):
    """Determine HOT/WARM/COLD tier"""
    warmth = int(warmth_score)

    # HOT: warmth 8+ OR professional industries OR family
    hot_industries = ['Legal/Law', 'Insurance/Finance', 'Beauty/Wellness']
    family_names = ['Dad', 'Mom', 'Mommy iphone']

    if warmth >= 8:
        return 'HOT'
    if any(industry.startswith(x) for x in hot_industries if x in industry):
        return 'HOT'
    if name in family_names:
        return 'HOT'  # Family gets priority for personal referral

    # WARM: warmth 6-7 OR music/entertainment
    if warmth >= 6:
        return 'WARM'
    if 'Music' in industry or 'Entertainment' in industry:
        return 'WARM'

    # COLD: warmth 5 or lower, unknown industry, distant location
    return 'COLD'

def get_outreach_method(tier):
    """Determine outreach method by tier"""
    if tier == 'HOT':
        return 'call'
    elif tier == 'WARM':
        return 'whatsapp'
    else:
        return 'email'

# Segment and prepare for insert
segmented = []
tier_counts = {'HOT': 0, 'WARM': 0, 'COLD': 0}

for contact in contacts:
    tier = get_tier(contact['warmth_score'], contact['industry_guess'], contact['name'])
    tier_counts[tier] += 1

    segmented.append({
        'contact_name': contact['name'],
        'contact_phone': contact['phone'],
        'contact_email': contact['email'] or None,
        'company': contact['company'] or None,
        'location': contact['location'],
        'industry_guess': contact['industry_guess'],
        'warmth_score': int(contact['warmth_score']),
        'tier': tier,
        'outreach_method': get_outreach_method(tier),
        'outreach_status': 'pending'
    })

print(f"\nTier Breakdown:")
print(f"  HOT:  {tier_counts['HOT']} contacts (direct calls)")
print(f"  WARM: {tier_counts['WARM']} contacts (WhatsApp)")
print(f"  COLD: {tier_counts['COLD']} contacts (email)")

# Insert into Supabase in batches
batch_size = 10
for i in range(0, len(segmented), batch_size):
    batch = segmented[i:i+batch_size]
    result = supabase.table('contact_tiers').insert(batch).execute()
    print(f"Inserted batch {i//batch_size + 1} ({len(batch)} contacts)")

print(f"\n✅ All {len(segmented)} contacts segmented and inserted")
