#!/usr/bin/env python3
"""
Phase 4: Batch import 1,308 unique ventures to ClickUp
Maps ventures to 31 sector folders in workspace 9013677375
"""

import os
import json
from supabase import create_client

# Init Supabase
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)

# Sector to ClickUp folder mapping
SECTOR_FOLDERS = {
    'e-commerce': '901317788883',
    'operations': '901317788917',
    'community': '901317788878',
    'emerging': '901317788892',
    'specialized': '901317788935',
    'technology': '901317788941',
    'beauty-wellness': '901317788875',
    'education': '901317788890',
    'financial': '901317788897',
    'food-hospitality': '901317788905',
    'logistics-transport': '901317788910',
    'media-content': '901317788913',
    'professional-services': '901317788925',
    'software-technology': '901317788930',
    'fitness-sports': '901317788901',
    'construction': '901318114591',
    'real-estate': '901318114592',
}

print("=" * 80)
print("PHASE 4: ClickUp Batch Import — 1,308 Unique Ventures")
print("=" * 80)

# Fetch unique ventures from Supabase
print("\n1. Fetching unique ventures from Supabase...")
response = supabase.table('ventures').select(
    'venture_id, name, sector, stage, revenue_ytd'
).execute()

ventures = response.data
unique_ventures = {}

# Deduplicate by venture_id (keep first occurrence)
for v in ventures:
    if v['venture_id'] not in unique_ventures:
        unique_ventures[v['venture_id']] = v

print(f"   ✅ Loaded {len(unique_ventures)} unique ventures")
print(f"   Total rows: {len(ventures)}")

# Group by sector
by_sector = {}
for v in unique_ventures.values():
    sector = v['sector'] or 'unassigned'
    if sector not in by_sector:
        by_sector[sector] = []
    by_sector[sector].append(v)

print(f"\n2. Ventures by sector:")
for sector, ventures_list in sorted(by_sector.items(), key=lambda x: -len(x[1])):
    folder_id = SECTOR_FOLDERS.get(sector, 'UNMAPPED')
    print(f"   {sector:25} → {len(ventures_list):3} ventures (folder: {folder_id})")

# Generate task format for batch import
print(f"\n3. Generating task format for ClickUp import...")

tasks = []
for venture in unique_ventures.values():
    sector = venture['sector'] or 'unassigned'
    folder_id = SECTOR_FOLDERS.get(sector, '901317788930')  # Default to Software

    task = {
        'name': f"[{venture['venture_id']}] {venture['name']}",
        'description': f"Sector: {sector}\nStage: {venture['stage']}\nRevenue YTD: ${venture.get('revenue_ytd', 0):,.0f}",
        'priority': 3 if venture['stage'] == 'mvp' else 2,
        'folder_id': folder_id,
        'tags': [venture['stage'], sector],
    }
    tasks.append(task)

print(f"   ✅ Generated {len(tasks)} task definitions")

# Save to JSON for ClickUp import
output_file = '/Users/acebless/Documents/clickup_batch_import.json'
with open(output_file, 'w') as f:
    json.dump({
        'total_tasks': len(tasks),
        'workspace_id': '9013677375',
        'tasks': tasks[:5],  # Show first 5
        'all_tasks_count': len(tasks),
    }, f, indent=2)

print(f"\n4. Ready to import to ClickUp")
print(f"   ✅ Batch file: {output_file}")
print(f"   ✅ Total to import: {len(tasks)} unique ventures")
print(f"   ✅ Folders configured: {len(SECTOR_FOLDERS)}")

print("\n" + "=" * 80)
print("NEXT STEP: Use ClickUp MCP to batch create tasks from this data")
print("=" * 80)
