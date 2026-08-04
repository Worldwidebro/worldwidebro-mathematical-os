#!/usr/bin/env python3
"""Ingest OS platforms into Neo4j as Venture nodes. Usage: python os-ingester.py"""

import json
import base64
import urllib.request
from pathlib import Path

def ingest_os_platforms():
    auth = base64.b64encode(b'neo4j:ventures2026').decode('ascii')
    registry_file = Path('/Users/acebless/Documents/os-registry.json')

    if not registry_file.exists():
        print(f"❌ {registry_file} not found"); return

    with open(registry_file) as f:
        registry = json.load(f)

    os_platforms = registry.get('os_platforms', [])
    iza_infra = registry.get('iza_os_infrastructure', [])

    print(f"📊 Ingesting {len(os_platforms)} OS + {len(iza_infra)} IZA-OS nodes\n")

    # Create OS Venture nodes
    for os_config in os_platforms:
        os_name = os_config['name']
        cypher = """
        MERGE (v:Venture {id: $os_id, name: $os_name})
        SET v.type = 'OS', v.os_type = $os_type, v.category = $category, v.status = 'CREATED'
        RETURN v.id
        """
        payload = {"statements": [{"statement": cypher, "parameters": {
            "os_id": os_name.lower(), "os_name": os_name,
            "os_type": os_config['type'], "category": os_config['category']
        }}]}
        try:
            req = urllib.request.Request('http://localhost:7474/db/neo4j/tx/commit',
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json', 'Authorization': f'Basic {auth}'},
                method='POST')
            with urllib.request.urlopen(req, timeout=5) as r:
                if json.loads(r.read()).get('results'): print(f"✅ {os_name}")
        except Exception as e: print(f"❌ {os_name}: {e}")

    # Create IZA-OS nodes
    print(f"\n🔧 IZA-OS infrastructure\n")
    for infra in iza_infra:
        cypher = """
        MERGE (v:Venture {id: $id, name: $name})
        SET v.type = 'INFRASTRUCTURE', v.parent = 'IZA-OS', v.status = 'CREATED'
        RETURN v.id
        """
        payload = {"statements": [{"statement": cypher, "parameters": {
            "id": infra['name'].lower(), "name": infra['name']
        }}]}
        try:
            req = urllib.request.Request('http://localhost:7474/db/neo4j/tx/commit',
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json', 'Authorization': f'Basic {auth}'},
                method='POST')
            with urllib.request.urlopen(req, timeout=5) as r:
                if json.loads(r.read()).get('results'): print(f"✅ {infra['name']}")
        except Exception as e: print(f"❌ {infra['name']}: {e}")

    print(f"\n✅ Complete: {len(os_platforms)} OS + {len(iza_infra)} infrastructure")

if __name__ == '__main__':
    ingest_os_platforms()
