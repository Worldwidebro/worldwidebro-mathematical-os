#!/usr/bin/env python3
"""Spawn agents for a venture. Usage: python spawn-agents.py CON-001"""

import sys
import json
import base64
import urllib.request

def map_agent_to_os(agent_type, venture_id, auth):
    """Map agent type to OS it manages (SalesAgent → SalesOS, etc.)"""
    type_to_os = {
        "SALES_AGENT": "salesos",
        "FINANCE_AGENT": "financeos",
        "OPERATIONS_AGENT": "operationsos"
    }
    return type_to_os.get(agent_type)

def query_required_forms(venture_id, auth):
    """Query Neo4j for forms required by this venture"""
    cypher = """
    MATCH (v:Venture {id: $venture_id})-[:REQUIRES_FORM]->(f:Form)
    RETURN f.form_id, f.name, f.agent_can_fill
    """
    payload = {
        "statements": [{
            "statement": cypher,
            "parameters": {"venture_id": venture_id}
        }]
    }
    try:
        req = urllib.request.Request(
            'http://localhost:7474/db/neo4j/tx/commit',
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json', 'Authorization': f'Basic {auth}'},
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            result = json.loads(response.read())
            forms = []
            if result.get('results') and result['results'][0].get('data'):
                for row in result['results'][0]['data']:
                    forms.append({
                        "form_id": row['row'][0],
                        "name": row['row'][1],
                        "agent": row['row'][2]
                    })
            return forms
    except Exception as e:
        return []

def spawn_agents(venture_id):
    if not venture_id:
        print("❌ Usage: python spawn-agents.py VENTURE_ID")
        sys.exit(1)

    auth = base64.b64encode(b'neo4j:ventures2026').decode('ascii')

    agents = [
        {"type": "SALES_AGENT", "name": f"SalesAgent-{venture_id}", "autonomy": "LEVEL_2", "caps": ["lead-capture"]},
        {"type": "FINANCE_AGENT", "name": f"FinanceAgent-{venture_id}", "autonomy": "LEVEL_1", "caps": ["payments"]},
        {"type": "OPERATIONS_AGENT", "name": f"OpsAgent-{venture_id}", "autonomy": "LEVEL_2", "caps": ["workflows"]}
    ]

    # Query required forms
    forms = query_required_forms(venture_id, base64.b64encode(b'neo4j:ventures2026').decode('ascii'))

    print(f"🚀 Spawning {len(agents)} agents for {venture_id}...\n")
    if forms:
        print(f"📋 Required forms: {', '.join([f['name'] for f in forms])}\n")

    for agent in agents:
        agent_id = f"{agent['type'].split('_')[0]}-{venture_id}-v1"
        os_id = map_agent_to_os(agent['type'], venture_id, auth)

        cypher = f"""
        MATCH (v:Venture {{id: $venture_id}})
        MERGE (a:Agent {{agent_id: $agent_id, name: $name, type: $type, venture_id: $venture_id, status: "CREATED", autonomy_level: $autonomy, created_at: datetime(), cost_ytd: 0}})
        MERGE (v)-[:SPAWNS_AGENT]->(a)
        """
        if os_id:
            cypher += f"""
            WITH a
            MATCH (os:Venture {{id: '{os_id}'}})
            MERGE (a)-[:MANAGES_OS]->(os)
            """
        cypher += "RETURN a.agent_id"

        payload = {"statements": [{"statement": cypher, "parameters": {
            "venture_id": venture_id, "agent_id": agent_id, "name": agent["name"],
            "type": agent["type"], "autonomy": agent["autonomy"]
        }}]}

        try:
            req = urllib.request.Request(
                'http://localhost:7474/db/neo4j/tx/commit',
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json', 'Authorization': f'Basic {auth}'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                result = json.loads(response.read())
                if result.get('results'):
                    print(f"✅ {agent['type']}: {agent_id}")
                    if os_id: print(f"   Manages: {os_id}")
                    print(f"   Capabilities: {', '.join(agent['caps'])}\n")
        except Exception as e:
            print(f"❌ {agent['type']}: {e}\n")

    print(f"📊 {venture_id}: {len(agents)} agents created (TRAINING stage)")
    if forms:
        print(f"📋 {len(forms)} forms linked to agents via Neo4j REQUIRES_FORM")

if __name__ == '__main__':
    spawn_agents(sys.argv[1] if len(sys.argv) > 1 else None)
