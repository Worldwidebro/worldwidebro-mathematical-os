#!/usr/bin/env python3
"""
Export graph_entities and graph_relationships from Supabase to Obsidian JSON + dashboard.
Run SECOND (after populate_venture_knowledge_graph.py).
Exports: .obsidian-sync/graph-data.json and .obsidian-sync/venture-hub-alignment.json
Creates: KNOWLEDGE-GRAPH-DASHBOARD.md with Dataview blocks
"""

import os
import sys
import json
from datetime import datetime
from typing import List, Dict, Any
from dotenv import load_dotenv

try:
    from supabase import create_client
except ImportError:
    print("ERROR: supabase-py not installed. Run: pip install supabase-py")
    sys.exit(1)

load_dotenv()


class ObsidianGraphSync:
    def __init__(self):
        self.url = os.getenv('SUPABASE_URL')
        self.key = os.getenv('SUPABASE_KEY')
        if not self.url or not self.key:
            print("ERROR: No credentials. Set SUPABASE_URL and SUPABASE_KEY in .env")
            sys.exit(1)

        self.supabase = create_client(self.url, self.key)
        self.entities = []
        self.relationships = []

    def fetch_entities(self) -> List[Dict[str, Any]]:
        """Fetch all entities from graph_entities with pagination"""
        all_entities = []
        page_size = 1000
        offset = 0
        try:
            while True:
                response = self.supabase.table('graph_entities').select('*').range(offset, offset + page_size - 1).execute()
                if not response.data:
                    break
                all_entities.extend(response.data)
                if len(response.data) < page_size:
                    break
                offset += page_size
            return all_entities
        except Exception as e:
            print(f"ERROR fetching entities: {e}")
            return []

    def fetch_relationships(self) -> List[Dict[str, Any]]:
        """Fetch all relationships from graph_relationships with pagination"""
        all_relationships = []
        page_size = 1000
        offset = 0
        try:
            while True:
                response = self.supabase.table('graph_relationships').select('*').range(offset, offset + page_size - 1).execute()
                if not response.data:
                    break
                all_relationships.extend(response.data)
                if len(response.data) < page_size:
                    break
                offset += page_size
            return all_relationships
        except Exception as e:
            print(f"ERROR fetching relationships: {e}")
            return []

    def build_alignment_report(self) -> Dict[str, Any]:
        """Build venture alignment report"""
        ventures = [e for e in self.entities if e.get('entity_type') == 'VENTURE']
        repos = [e for e in self.entities if e.get('entity_type') == 'REPO']
        contacts = [e for e in self.entities if e.get('entity_type') == 'PERSON']

        # Count relationship types
        rel_types = {}
        for rel in self.relationships:
            rel_type = rel.get('relation_type', 'UNKNOWN')
            rel_types[rel_type] = rel_types.get(rel_type, 0) + 1

        return {
            "timestamp": datetime.now().isoformat(),
            "entity_summary": {
                "total_entities": len(self.entities),
                "ventures": len(ventures),
                "repos": len(repos),
                "contacts": len(contacts),
                "other": len(self.entities) - len(ventures) - len(repos) - len(contacts)
            },
            "relationship_summary": {
                "total_relationships": len(self.relationships),
                "by_type": rel_types
            },
            "repo_coverage": {
                "repos_with_connections": len([r for r in repos if any(
                    rel['target_id'] == r['entity_id'] or rel['source_id'] == r['entity_id']
                    for rel in self.relationships
                )])
            },
            "connection_status": "live" if len(self.relationships) > 0 else "pending"
        }

    def export_to_json(self):
        """Export graph data to .obsidian-sync/graph-data.json"""
        os.makedirs('.obsidian-sync', exist_ok=True)

        graph_data = {
            "entities": self.entities,
            "relationships": self.relationships,
            "exported_at": datetime.now().isoformat()
        }

        with open('.obsidian-sync/graph-data.json', 'w') as f:
            json.dump(graph_data, f, indent=2)

        print(f"✅ Exported graph data: .obsidian-sync/graph-data.json ({len(self.entities)} entities, {len(self.relationships)} relationships)")

    def export_alignment_report(self):
        """Export alignment report to .obsidian-sync/venture-hub-alignment.json"""
        alignment = self.build_alignment_report()

        with open('.obsidian-sync/venture-hub-alignment.json', 'w') as f:
            json.dump(alignment, f, indent=2)

        print(f"✅ Exported alignment report: .obsidian-sync/venture-hub-alignment.json")

    def create_dashboard(self, alignment: Dict[str, Any]):
        """Create KNOWLEDGE-GRAPH-DASHBOARD.md with Dataview blocks"""
        dashboard = f"""---
tags: knowledge-graph, dashboard, obsidian
created: {datetime.now().isoformat()}
---

# Knowledge Graph Dashboard

**Last Sync:** {alignment['timestamp']}
**Status:** {alignment['connection_status'].upper()}

---

## System Health

| Metric | Value |
|--------|-------|
| **Total Entities** | {alignment['entity_summary']['total_entities']} |
| **Ventures** | {alignment['entity_summary']['ventures']} |
| **Repos** | {alignment['entity_summary']['repos']} |
| **Contacts** | {alignment['entity_summary']['contacts']} |
| **Total Relationships** | {alignment['relationship_summary']['total_relationships']} |
| **Repos w/ Connections** | {alignment['repo_coverage']['repos_with_connections']} |

---

## Entity Types

```dataview
TABLE WITHOUT ID
    entity_type AS "Type",
    count(rows) AS "Count"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
GROUP BY entity_type
SORT Count DESC
```

---

## Relationship Types

```dataview
TABLE WITHOUT ID
    relation_type AS "Type",
    count(rows) AS "Count"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
GROUP BY relation_type
SORT Count DESC
```

---

## Ventures (Top 20)

```dataview
TABLE WITHOUT ID
    entity_name AS "Venture",
    entity_type AS "Type"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
WHERE entity_type = "VENTURE"
LIMIT 20
```

---

## Repos (Top 20)

```dataview
TABLE WITHOUT ID
    entity_name AS "Repo",
    entity_type AS "Type"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
WHERE entity_type = "REPO"
LIMIT 20
```

---

## Contacts (Top 20)

```dataview
TABLE WITHOUT ID
    entity_name AS "Contact",
    entity_type AS "Type"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
WHERE entity_type = "PERSON"
LIMIT 20
```

---

## Data Source

- **Source:** Supabase (graph_entities, graph_relationships)
- **Export:** .obsidian-sync/graph-data.json
- **Alignment:** .obsidian-sync/venture-hub-alignment.json

---

## Sync Status

✅ **Entities imported:** {alignment['entity_summary']['total_entities']}
✅ **Relationships established:** {alignment['relationship_summary']['total_relationships']}
✅ **Dashboard rendered:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

**Next Steps:**
1. Open this file in Obsidian
2. Verify 8 Dataview blocks render above
3. If blocks show data, graph is connected
4. If blocks are empty, check Supabase connection

---

## Repository Map / Venture Index / Knowledge Graph — Master Index
_Source of truth = CSVs + Supabase, not the GitHub API._

### Venture Index
| File | Rows | What |
|------|------|------|
| `.../INFRASTRUCTURE_LAYERS/venture-hub/ventures-master.csv` | 712 | Canonical ventures (id, name, sector, stage, status, repo_id) |
| `.../venture-hub/ventures_with_capabilities.csv` | 618 | + required_capabilities + top_repo_1/2/3 |
| `08-DATA/registries/ventures.csv` / `venture_capability_map.csv` | — | Registry snapshot + venture->capability |

### Repository Map
| File | Size/Rows | What |
|------|-----------|------|
| `.../REFERENCE/REPOSITORY-REGISTRY.json` | 908K | ~1,592 repos, 10 attributes |
| `.../venture-hub/MASTER-REPO-REGISTRY.csv` | 985 | Repos -> ventures + agents + health_score |
| `08-DATA/registries/repositories.csv` / `venture_repo_map.csv` | 37K / 137K | Flat repo list + venture<->repo edges |

### Knowledge Graph
| File / Store | Size | What |
|--------------|------|------|
| `.obsidian-sync/graph-data.json` | 7.5M | Full entity+relationship export |
| `.obsidian-sync/venture-hub-alignment.json` | 221K | Processed alignment |
| Supabase graph_entities / graph_relationships | — | Source of truth |
| Neo4j 08-DATA/venture-hub-data/neo4j | — | Graph DB |

### Regenerate
- python3 populate_venture_knowledge_graph.py   -> graph_entities + relationships
- python3 obsidian_graph_sync.py                -> .obsidian-sync/*.json + this dashboard
- python3 scan_repositories.py                  -> REPOSITORY-REGISTRY.json
- python3 WORLDWIDEBRO-OS/08-DATA/build_registries.py  -> 08-DATA/registries/*.csv
"""

        with open('KNOWLEDGE-GRAPH-DASHBOARD.md', 'w') as f:
            f.write(dashboard)

        print(f"✅ Created dashboard: KNOWLEDGE-GRAPH-DASHBOARD.md")

    def run(self):
        """Execute full sync pipeline"""
        print("\n📊 Obsidian Graph Sync Starting...\n")

        # Fetch from Supabase
        print("📥 Fetching entities...")
        self.entities = self.fetch_entities()
        print(f"   Found {len(self.entities)} entities")

        print("📥 Fetching relationships...")
        self.relationships = self.fetch_relationships()
        print(f"   Found {len(self.relationships)} relationships")

        if not self.entities:
            print("\n⚠️  WARNING: No entities found. Did you run populate_venture_knowledge_graph.py?")
            return False

        # Export
        self.export_to_json()
        alignment = self.build_alignment_report()
        self.export_alignment_report()
        self.create_dashboard(alignment)

        print("\n✅ Sync Complete!\n")
        print("📋 Summary:")
        print(f"   Entities: {alignment['entity_summary']['total_entities']}")
        print(f"   Relationships: {alignment['relationship_summary']['total_relationships']}")
        print(f"   Connection Status: {alignment['connection_status'].upper()}")
        print(f"\n🎯 Next Step: Open KNOWLEDGE-GRAPH-DASHBOARD.md in Obsidian to verify rendering")

        return True


if __name__ == '__main__':
    sync = ObsidianGraphSync()
    success = sync.run()
    sys.exit(0 if success else 1)
