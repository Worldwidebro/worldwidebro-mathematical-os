#!/usr/bin/env python3
"""Wire OS relationships in Neo4j. Usage: python os-wire-relationships.py"""

import json
import base64
import urllib.request

def wire_os_relationships():
    auth = base64.b64encode(b'neo4j:ventures2026').decode('ascii')
    print("🔗 Wiring OS relationships...\n")

    # Wire all OS → BUILT_ON_IZA → iza-os-api
    cypher = """
    MATCH (os:Venture {type: 'OS'})
    MATCH (iza:Venture {id: 'iza-os-api'})
    MERGE (os)-[:BUILT_ON_IZA]->(iza)
    RETURN COUNT(*) as count
    """
    payload = {"statements": [{"statement": cypher}]}
    try:
        req = urllib.request.Request('http://localhost:7474/db/neo4j/tx/commit',
            data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json', 'Authorization': f'Basic {auth}'}, method='POST')
        with urllib.request.urlopen(req, timeout=5) as r:
            count = json.loads(r.read())['results'][0]['data'][0]['row'][0]
            print(f"✅ Created {count} BUILT_ON_IZA edges")
    except Exception as e:
        print(f"❌ BUILT_ON_IZA failed: {e}")

    # Wire focus ventures → OS (INHERITS_OS)
    focus_os_map = {
        "con-001": ["constructionos", "financeos", "payrollos", "projectos", "crmos"],
        "lt-005": ["courieros", "financeos", "complianceos", "privacyos"],
        "lt-011": ["dispatchos", "financeos", "integrationos"],
        "sta-001": ["staffingos", "financeos", "recruitingos", "peopleos"],
        "ops-001": ["operationsos", "financeos", "workflowos"],
        "ec-001": ["ecommerceos", "financeos", "crmos", "marketingos"],
        "ec-112": ["ecommerceos", "financeos", "crmos", "marketingos"],
        "re-001": ["realestateos", "financeos", "projectos"]
    }

    for venture_id, os_list in focus_os_map.items():
        for os_id in os_list:
            cypher = """
            MATCH (v:Venture {id: $v_id})
            MATCH (os:Venture {id: $os_id})
            MERGE (v)-[:INHERITS_OS]->(os)
            RETURN v.id
            """
            payload = {"statements": [{"statement": cypher, "parameters": {"v_id": venture_id, "os_id": os_id}}]}
            try:
                req = urllib.request.Request('http://localhost:7474/db/neo4j/tx/commit',
                    data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json', 'Authorization': f'Basic {auth}'}, method='POST')
                with urllib.request.urlopen(req, timeout=5) as r:
                    if json.loads(r.read()).get('results'): print(f"✅ {venture_id} → {os_id}")
            except Exception as e:
                print(f"❌ {venture_id} → {os_id}: {e}")

    print(f"\n✅ Wiring complete")

if __name__ == '__main__':
    wire_os_relationships()
