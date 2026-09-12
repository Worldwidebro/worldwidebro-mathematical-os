#!/usr/bin/env python3
import json
import base64
import urllib.request
from pathlib import Path

auth = "Basic " + base64.b64encode(b"neo4j:changeme").decode("ascii")
url = "http://100.87.214.70:7474/db/neo4j/tx/commit"

def execute_statements(stmts):
    payload = {"statements": [{"statement": s} for s in stmts]}
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": auth, "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())

with open("14-CAPABILITIES/CAPABILITY_SOLUTION_MATRIX.json") as f:
    matrix = json.load(f)

print(f"Loaded {len(matrix)} capabilities from matrix.")

batch = []
for cid, cinfo in matrix.items():
    name = cinfo.get("name", cid).replace("'", "\\'")
    cat = cinfo.get("category", "").replace("'", "\\'")
    sec = cinfo.get("sector", "").split("-")[0]
    desc = cinfo.get("description", "").replace("'", "\\'")
    tags_json = json.dumps(cinfo.get("tags", []))
    sols_json = json.dumps(cinfo.get("solutions", []))

    cypher = f"""
    MERGE (c:Capability {{id: '{cid}'}})
    SET c.name = '{name}',
        c.category = '{cat}',
        c.description = '{desc}',
        c.tags = {tags_json},
        c.solutions = {sols_json},
        c.status = 'ACTIVE'
    WITH c
    MATCH (s:SECTOR)
    WHERE s.id = '{sec}' OR s.code = '{sec}'
    MERGE (c)-[:BELONGS_TO]->(s)
    """
    batch.append(cypher)

print(f"Executing {len(batch)} capability merges in batches of 50...")
for i in range(0, len(batch), 50):
    chunk = batch[i:i+50]
    res = execute_statements(chunk)
    if res.get("errors"):
        print("Errors in batch:", res["errors"][:1])

rel_batch = []
for cid, cinfo in matrix.items():
    for rel_id in cinfo.get("related", []):
        cypher = f"""
        MATCH (c1:Capability {{id: '{cid}'}}), (c2:Capability {{id: '{rel_id}'}})
        MERGE (c1)-[:RELATED_TO]->(c2)
        """
        rel_batch.append(cypher)

print(f"Executing {len(rel_batch)} RELATED_TO edges in batches of 100...")
for i in range(0, len(rel_batch), 100):
    chunk = rel_batch[i:i+100]
    res = execute_statements(chunk)
    if res.get("errors"):
        print("Errors in rel batch:", res["errors"][:1])

res = execute_statements([
    "MATCH (c:Capability) RETURN count(c) as cap_count",
    "MATCH ()-[r:RELATED_TO]->() RETURN count(r) as rel_count",
    "MATCH (c:Capability)-[r:BELONGS_TO]->(s) RETURN count(r) as sec_links"
])
print("\n=======================================================")
print("Neo4j Capability Graph Status:")
print("  Total Capabilities in Graph:", res["results"][0]["data"][0]["row"][0])
print("  Capability RELATED_TO Edges:", res["results"][1]["data"][0]["row"][0])
print("  Capability -> Sector Links: ", res["results"][2]["data"][0]["row"][0])
print("=======================================================")
