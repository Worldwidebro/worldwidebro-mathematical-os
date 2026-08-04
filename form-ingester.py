#!/usr/bin/env python3
"""Ingest P0 form schemas into Neo4j. Usage: python form-ingester.py"""

import json
import base64
import urllib.request
import os
from pathlib import Path

def ingest_forms():
    """Load all form schemas from /forms/ and create Form nodes in Neo4j"""

    auth = base64.b64encode(b'neo4j:ventures2026').decode('ascii')
    forms_dir = Path('/Users/acebless/Documents/forms')

    if not forms_dir.exists():
        print(f"❌ {forms_dir} not found")
        return

    form_files = sorted(forms_dir.glob('*.json'))
    print(f"📋 Found {len(form_files)} form schemas\n")

    for form_file in form_files:
        with open(form_file) as f:
            form = json.load(f)

        form_id = form.get('form_id')
        form_name = form.get('name')
        ventures = form.get('required_for', [])

        # Create Form node
        cypher = """
        MERGE (f:Form {form_id: $form_id, name: $name})
        SET f.description = $description, f.status = $status, f.agent_can_fill = $agent, f.version = $version
        RETURN f.form_id
        """

        payload = {
            "statements": [{
                "statement": cypher,
                "parameters": {
                    "form_id": form_id,
                    "name": form_name,
                    "description": form.get('description'),
                    "status": form.get('status'),
                    "agent": form.get('agent_can_fill'),
                    "version": form.get('version')
                }
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
                if result.get('results'):
                    print(f"✅ {form_name}: {form_id}")
        except Exception as e:
            print(f"❌ {form_name}: {e}")

        # Create REQUIRES_FORM relationships
        for venture_id in ventures:
            cypher = """
            MATCH (v:Venture {id: $venture_id})
            MATCH (f:Form {form_id: $form_id})
            MERGE (v)-[:REQUIRES_FORM]->(f)
            RETURN v.id, f.form_id
            """

            payload = {
                "statements": [{
                    "statement": cypher,
                    "parameters": {"venture_id": venture_id, "form_id": form_id}
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
                    if result.get('results'):
                        print(f"   └─ {venture_id} requires {form_id}")
            except Exception as e:
                print(f"   └─ {venture_id}: {e}")

    print(f"\n📊 Form ingestion complete")

if __name__ == '__main__':
    ingest_forms()
