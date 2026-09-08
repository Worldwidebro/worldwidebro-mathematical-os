#!/usr/bin/env python3
"""
execute_neo4j_activation.py
Executes Neo4j activation queries to wire REP-001 (worldwidebro-venture-portal),
REP-002, REP-003, AGT-001..009, CAP-001..212, and TOL tools into Neo4j.
"""

import json
import base64
import urllib.request
import urllib.error
import sys

NEO4J_URL = "http://100.87.214.70:7474/db/neo4j/tx/commit"
AUTH_HEADER = "Basic " + base64.b64encode(b"neo4j:ventures2026").decode("ascii")

STATEMENTS = [
    # Agents
    "MERGE (agt1:Agent {id: 'AGT-001'}) ON CREATE SET agt1.name = 'Venture PM', agt1.type = 'orchestration'",
    "MERGE (agt2:Agent {id: 'AGT-002'}) ON CREATE SET agt2.name = 'Financial Analyst', agt2.type = 'finance'",
    "MERGE (agt3:Agent {id: 'AGT-003'}) ON CREATE SET agt3.name = 'System Architect', agt3.type = 'architecture'",
    "MERGE (agt4:Agent {id: 'AGT-004'}) ON CREATE SET agt4.name = 'QA Specialist', agt4.type = 'testing'",
    "MERGE (agt5:Agent {id: 'AGT-005'}) ON CREATE SET agt5.name = 'Infrastructure Engineer', agt5.type = 'infrastructure'",
    "MERGE (agt6:Agent {id: 'AGT-006'}) SET agt6.name = 'Education Teacher', agt6.routing_key = 'education-teacher', agt6.type = 'routing'",
    "MERGE (agt7:Agent {id: 'AGT-007'}) SET agt7.name = 'Education Peer', agt7.routing_key = 'education-peer', agt7.type = 'routing'",
    "MERGE (agt8:Agent {id: 'AGT-008'}) SET agt8.name = 'Education Content', agt8.routing_key = 'education-content', agt8.type = 'routing'",
    "MERGE (agt9:Agent {id: 'AGT-009'}) SET agt9.name = 'Education Eval', agt9.routing_key = 'education-eval', agt9.type = 'routing'",

    # Sector & Control Plane
    "MERGE (sec37:Sector {id: 'SEC-037'}) SET sec37.name = 'Education & Learning'",
    "MERGE (cp31:ControlPlane {id: 'CP-031'}) SET cp31.name = 'Education Control Plane', cp31.sector = 'SEC-037'",

    # Repositories
    "MERGE (rep1:Repository {id: 'REP-001'}) SET rep1.name = 'worldwidebro-venture-portal', rep1.type = 'core-platform', rep1.url = 'https://github.com/Worldwidebro/worldwidebro-venture-portal', rep1.code_verified = true, rep1.reality_status = 'OPERATING'",
    "MERGE (rep2:Repository {id: 'REP-002'}) SET rep2.name = 'vex-hero-site', rep2.type = 'hero-site', rep2.url = 'https://github.com/Worldwidebro/vex-hero', rep2.code_verified = true, rep2.reality_status = 'SPECULATIVE'",
    "MERGE (rep3:Repository {id: 'REP-003'}) SET rep3.name = 'claude-home', rep3.type = 'vex-core', rep3.url = 'https://github.com/Worldwidebro/claude-home', rep3.code_verified = true, rep3.reality_status = 'OPERATING'",

    # Capabilities
    "MERGE (cap1:Capability {id: 'CAP-001'}) SET cap1.name = 'Venture management'",
    "MERGE (cap12:Capability {id: 'CAP-012'}) SET cap12.name = 'Dashboard UI'",
    "MERGE (cap50:Capability {id: 'CAP-050'}) SET cap50.name = 'Sector visualization'",
    "MERGE (cap100:Capability {id: 'CAP-100'}) SET cap100.name = 'Agent routing'",
    "MERGE (cap101:Capability {id: 'CAP-101'}) SET cap101.name = 'Task discovery'",
    "MERGE (cap150:Capability {id: 'CAP-150'}) SET cap150.name = 'Knowledge graph'",
    "MERGE (cap200:Capability {id: 'CAP-200'}) SET cap200.name = 'Curriculum planning'",
    "MERGE (cap201:Capability {id: 'CAP-201'}) SET cap201.name = 'Slide generation'",
    "MERGE (cap202:Capability {id: 'CAP-202'}) SET cap202.name = 'Interactive simulations'",
    "MERGE (cap203:Capability {id: 'CAP-203'}) SET cap203.name = 'PBL design'",
    "MERGE (cap204:Capability {id: 'CAP-204'}) SET cap204.name = 'TTS rendering'",
    "MERGE (cap205:Capability {id: 'CAP-205'}) SET cap205.name = 'PPTX export'",
    "MERGE (cap206:Capability {id: 'CAP-206'}) SET cap206.name = 'Diagram creation'",
    "MERGE (cap207:Capability {id: 'CAP-207'}) SET cap207.name = 'Discussion prompts'",
    "MERGE (cap208:Capability {id: 'CAP-208'}) SET cap208.name = 'Q&A handling'",
    "MERGE (cap209:Capability {id: 'CAP-209'}) SET cap209.name = 'Content structuring'",
    "MERGE (cap210:Capability {id: 'CAP-210'}) SET cap210.name = 'Peer feedback'",
    "MERGE (cap211:Capability {id: 'CAP-211'}) SET cap211.name = 'Progress tracking'",
    "MERGE (cap212:Capability {id: 'CAP-212'}) SET cap212.name = 'Performance reporting'",

    # Tools
    "MERGE (t1:Tool {id: 'TOL-clickup'}) SET t1.name = 'ClickUp API', t1.type = 'task-management'",
    "MERGE (t2:Tool {id: 'TOL-supabase'}) SET t2.name = 'Supabase Client', t2.type = 'database'",
    "MERGE (t3:Tool {id: 'TOL-stripe'}) SET t3.name = 'Stripe API', t3.type = 'payments'",
    "MERGE (t4:Tool {id: 'TOL-neo4j'}) SET t4.name = 'Neo4j', t4.type = 'graph-database'",
    "MERGE (t5:Tool {id: 'TOL-qdrant'}) SET t5.name = 'Qdrant', t5.type = 'vector-search'",
    "MERGE (t6:Tool {id: 'TOL-anthropic'}) SET t6.name = 'Anthropic Claude', t6.type = 'llm'",
    "MERGE (t7:Tool {id: 'TOL-vercel'}) SET t7.name = 'Vercel Deployment API', t7.type = 'hosting'",

    # Relationships: Agents to Sector & Control Plane
    "MATCH (a:Agent), (s:Sector) WHERE a.id IN ['AGT-006', 'AGT-007', 'AGT-008', 'AGT-009'] AND s.id = 'SEC-037' MERGE (a)-[:SERVES]->(s)",
    "MATCH (a:Agent), (cp:ControlPlane) WHERE a.id IN ['AGT-006', 'AGT-007', 'AGT-008', 'AGT-009'] AND cp.id = 'CP-031' MERGE (a)-[:EXECUTES]->(cp)",

    # Relationships: Agents to Capabilities
    "MATCH (a:Agent {id: 'AGT-006'}), (c:Capability) WHERE c.id IN ['CAP-200', 'CAP-201', 'CAP-206', 'CAP-209'] MERGE (a)-[:IMPLEMENTS]->(c)",
    "MATCH (a:Agent {id: 'AGT-007'}), (c:Capability) WHERE c.id IN ['CAP-207', 'CAP-208', 'CAP-210'] MERGE (a)-[:IMPLEMENTS]->(c)",
    "MATCH (a:Agent {id: 'AGT-008'}), (c:Capability) WHERE c.id IN ['CAP-201', 'CAP-202', 'CAP-203', 'CAP-205'] MERGE (a)-[:IMPLEMENTS]->(c)",
    "MATCH (a:Agent {id: 'AGT-009'}), (c:Capability) WHERE c.id IN ['CAP-208', 'CAP-211', 'CAP-212'] MERGE (a)-[:IMPLEMENTS]->(c)",

    # Relationships: Repositories to Agents
    "MATCH (r:Repository {id: 'REP-001'}), (a:Agent) WHERE a.id IN ['AGT-001', 'AGT-002', 'AGT-006'] MERGE (r)-[:USED_BY]->(a)",
    "MATCH (r:Repository {id: 'REP-002'}), (a:Agent {id: 'AGT-002'}) MERGE (r)-[:USED_BY]->(a)",
    "MATCH (r:Repository {id: 'REP-003'}), (a:Agent) WHERE a.id IN ['AGT-001', 'AGT-002', 'AGT-003', 'AGT-004', 'AGT-005'] MERGE (r)-[:USED_BY]->(a)",

    # Relationships: Repositories to Capabilities
    "MATCH (r:Repository {id: 'REP-001'}), (c:Capability) WHERE c.id IN ['CAP-001', 'CAP-012', 'CAP-050'] MERGE (r)-[:IMPLEMENTS]->(c)",
    "MATCH (r:Repository {id: 'REP-003'}), (c:Capability) WHERE c.id IN ['CAP-100', 'CAP-101', 'CAP-150'] MERGE (r)-[:IMPLEMENTS]->(c)",

    # Relationships: Agents & Repositories to Tools
    "MATCH (a:Agent), (t:Tool {id: 'TOL-anthropic'}) WHERE a.id IN ['AGT-006', 'AGT-007', 'AGT-008', 'AGT-009'] MERGE (a)-[:CAN_USE]->(t)",
    "MATCH (a:Agent), (t:Tool {id: 'TOL-clickup'}) WHERE a.id IN ['AGT-001', 'AGT-002', 'AGT-006'] MERGE (a)-[:CAN_USE]->(t)",
    "MATCH (r:Repository {id: 'REP-001'}), (t:Tool) WHERE t.id IN ['TOL-clickup', 'TOL-supabase', 'TOL-stripe'] MERGE (r)-[:USES_TOOL]->(t)",
    "MATCH (r:Repository {id: 'REP-002'}), (t:Tool) WHERE t.id IN ['TOL-vercel', 'TOL-supabase'] MERGE (r)-[:USES_TOOL]->(t)",
    "MATCH (r:Repository {id: 'REP-003'}), (t:Tool) WHERE t.id IN ['TOL-neo4j', 'TOL-qdrant', 'TOL-anthropic'] MERGE (r)-[:USES_TOOL]->(t)"
]

VERIFICATION_QUERIES = [
    ("REP-001 Node", "MATCH (r:Repository {id: 'REP-001'}) RETURN r.id, r.name, r.url, r.code_verified"),
    ("REP-001 Capabilities", "MATCH (r:Repository {id: 'REP-001'})-[:IMPLEMENTS]->(c:Capability) RETURN c.id, c.name"),
    ("REP-001 Agents", "MATCH (r:Repository {id: 'REP-001'})-[:USED_BY]->(a:Agent) RETURN a.id, a.name"),
    ("REP-001 Tools", "MATCH (r:Repository {id: 'REP-001'})-[:USES_TOOL]->(t:Tool) RETURN t.id, t.name"),
    ("Education Agents Linked", "MATCH (a:Agent)-[:SERVES]->(s:Sector {id: 'SEC-037'}) RETURN a.id, a.name"),
    ("Total Repositories in Graph", "MATCH (r:Repository) RETURN count(r) as total_repos"),
    ("Total Agents in Graph", "MATCH (a:Agent) RETURN count(a) as total_agents")
]

def run_statements(statements):
    payload = {"statements": [{"statement": s} for s in statements]}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        NEO4J_URL,
        data=data,
        headers={
            "Authorization": AUTH_HEADER,
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = resp.read().decode("utf-8")
        res = json.loads(body)
        errors = res.get("errors", [])
        if errors:
            print("❌ Neo4j Error:", errors)
            sys.exit(1)
        return res

def main():
    print("🚀 Executing Neo4j Activation queries...")
    run_statements(STATEMENTS)
    print("✅ All statements executed successfully.")

    print("\n🔍 Verifying Graph State:")
    for label, query in VERIFICATION_QUERIES:
        res = run_statements([query])
        results = res.get("results", [{}])[0]
        data = results.get("data", [])
        rows = [d.get("row") for d in data]
        print(f"  • {label}: {rows}")

if __name__ == "__main__":
    main()
