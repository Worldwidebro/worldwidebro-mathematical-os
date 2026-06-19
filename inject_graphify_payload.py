import json
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv("/Users/acebless/Documents/.env")
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

with open("/Users/acebless/Documents/graphify-repo-injection.json", "r") as f:
    payload = json.load(f)

print(f"🔄 Injecting: {payload['metadata']['total_repos']} repos + {payload['metadata']['total_capabilities']} caps + {payload['metadata']['total_relationships']} rels\n")

# Relationships only (repos/caps already exist from previous session)
print("🔄 Inserting relationships...")
rels_inserted = 0
rels_failed = 0

for rel in payload['relationships']:
    try:
        supabase.table('graph_relationships').insert({
            'id': rel['id'],
            'source_id': rel['source_id'],
            'target_id': rel.get('target_id', ''),
            'relation_type': rel.get('relationship_type', 'PROVIDES_CAPABILITY'),
            'weight': rel.get('strength', 1.0),
            'context': f"Repo provides {rel['target_name']} capability"
        }).execute()
        rels_inserted += 1
    except Exception as e:
        if "duplicate" not in str(e).lower():
            rels_failed += 1
            if rels_failed <= 3:
                print(f"  ⚠️  {str(e)[:60]}")

print(f"  ✅ {rels_inserted} relationships inserted")

# Verify
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
