import json
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv("/Users/acebless/Documents/.env")
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

with open("/Users/acebless/Documents/graphify-repo-injection.json", "r") as f:
    payload = json.load(f)

# Build capability name-to-id mapping
cap_name_to_id = {}
for cap in payload.get('entities', {}).get('capabilities', []):
    cap_name_to_id[cap['name'].lower()] = cap['id']

print(f"🔄 Injecting: {payload['metadata']['total_repos']} repos + {payload['metadata']['total_capabilities']} caps + {payload['metadata']['total_relationships']} rels\n")
print(f"Loaded {len(cap_name_to_id)} capabilities mappings from JSON.\n")

print("🔄 Inserting relationships...")
rels_inserted = 0
rels_failed = 0
rels_skipped = 0

for rel in payload['relationships']:
    target_name = rel.get('target_name', '').lower()
    target_id = cap_name_to_id.get(target_name)
    
    if not target_id:
        # Fallback to query DB directly for match just in case
        try:
            db_res = supabase.table('graph_entities').select('id').eq('entity_type', 'CAPABILITY').eq('name', rel.get('target_name')).execute()
            if db_res.data:
                target_id = db_res.data[0]['id']
        except Exception:
            pass
            
    if not target_id:
        rels_skipped += 1
        continue

    try:
        supabase.table('graph_relationships').insert({
            'id': rel['id'],
            'source_id': rel['source_id'],
            'target_id': target_id,
            'relation_type': rel.get('relationship_type', 'PROVIDES_CAPABILITY'),
            'weight': rel.get('strength', 1.0),
            'context': f"Repo provides {rel['target_name']} capability"
        }).execute()
        rels_inserted += 1
    except Exception as e:
        if "duplicate" in str(e).lower():
            # If it's already there, count it as inserted or skip
            pass
        else:
            rels_failed += 1
            if rels_failed <= 5:
                print(f"  ⚠️  Error: {str(e)[:120]}")

print(f"  ✅ {rels_inserted} relationships inserted successfully")
print(f"  ℹ️  {rels_skipped} relationships skipped due to missing target_id mapping")
print(f"  ❌ {rels_failed} relationships failed")

# Verify final stats
entities = supabase.table('graph_entities').select('count', count='exact').execute()
relationships = supabase.table('graph_relationships').select('count', count='exact').execute()

print(f"\n📊 Final Graph State:")
print(f"  - Entities: {entities.count}")
print(f"  - Relationships: {relationships.count}")

# Count by type
entity_types = supabase.table('graph_entities').select('entity_type').execute()
type_counts = {}
for e in entity_types.data:
    t = e.get('entity_type')
    type_counts[t] = type_counts.get(t, 0) + 1

print(f"\n  Entity Types:")
for typ, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"    - {typ}: {count}")

print(f"\n✅ Phase 4A: Graph Injection Complete")
