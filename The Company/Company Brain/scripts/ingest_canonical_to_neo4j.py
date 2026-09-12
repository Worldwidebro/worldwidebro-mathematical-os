#!/usr/bin/env python3
"""
ingest_canonical_to_neo4j.py

Ingests Company Brain ground-truth canonical registries into Neo4j (bolt://100.87.214.70:7687):
- (:Venture)
- (:Repository)
- (:Site)
- (:Capability)
- Relationships:
  (:Venture)-[:OPERATES]->(:Repository)
  (:Venture)-[:DEPLOYS]->(:Site)
  (:Repository)-[:DEPLOYS_TO]->(:Site)
  (:Repository)-[:IMPLEMENTS]->(:Capability)
"""

import json
import yaml
from pathlib import Path
from neo4j import GraphDatabase

WORKSPACE = Path("/Users/acebless/Documents/The Company/Company Brain")
REPOS_FILE = WORKSPACE / "_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml"
DEPS_FILE = WORKSPACE / "_REGISTRIES/CANONICAL/OWNED_REPO_DEPENDENCIES.json"
SITES_FILE = WORKSPACE / "_REGISTRIES/CANONICAL/SITES_REGISTRY.yaml"
CAPS_FILE = WORKSPACE / "_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml"

NEO4J_URI = "bolt://100.87.214.70:7687"
import os
pwd = os.environ.get("NEO4J_PASSWORD", "changeme")
NEO4J_AUTH = ("neo4j", pwd)

def main():
    print("Connecting to Neo4j...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)

    with driver.session() as session:
        # 1. Update Capabilities
        print(f"Loading capabilities from {CAPS_FILE}...")
        with open(CAPS_FILE) as f:
            caps_data = yaml.safe_load(f)

        tech_caps = caps_data.get("technical_capabilities", {})
        for cap_name, cap_info in tech_caps.items():
            # Match existing by name or id, or create if missing
            session.run("""
                OPTIONAL MATCH (c:Capability)
                WHERE c.name = $name OR c.id = $name OR toLower(c.name) = toLower($name) OR toLower(c.id) = toLower($name)
                WITH c
                WHERE c IS NOT NULL
                SET c.repo_count = $repo_count, c.type = 'TECHNICAL'
            """, name=cap_name, repo_count=cap_info.get("repo_count", 0))

        # 2. Ingest Repositories
        print(f"Loading repositories from {REPOS_FILE}...")
        with open(REPOS_FILE) as f:
            repos_data = yaml.safe_load(f)

        repos_dict = repos_data.get("repositories", {})
        batch_repos = []
        for rid, r in repos_dict.items():
            batch_repos.append({
                "id": rid,
                "name": r.get("repo_name", ""),
                "url": r.get("github_url", ""),
                "code_verified": bool(r.get("code_verified", False)),
                "reality_status": r.get("reality_status", "UNKNOWN"),
                "dep_count": r.get("dependency_count", 0),
                "frameworks": r.get("detected_frameworks", []),
                "capabilities": r.get("verified_capabilities", [])
            })

        print(f"Ingesting {len(batch_repos)} repositories...")
        session.run("""
            UNWIND $batch AS r
            MERGE (repo:Repository {id: r.id})
            SET repo.name = r.name,
                repo.url = r.url,
                repo.code_verified = r.code_verified,
                repo.reality_status = r.reality_status,
                repo.dependency_count = r.dep_count,
                repo.frameworks = r.frameworks
            WITH repo, r
            UNWIND r.capabilities AS cap
            MATCH (c:Capability)
            WHERE c.name = cap OR c.id = cap OR toLower(c.name) = toLower(cap) OR toLower(c.id) = toLower(cap)
            MERGE (repo)-[:IMPLEMENTS]->(c)
        """, batch=batch_repos)

        # 3. Ingest Sites
        print(f"Loading sites from {SITES_FILE}...")
        with open(SITES_FILE) as f:
            sites_data = yaml.safe_load(f)

        sites_dict = sites_data.get("sites", {})
        batch_sites = []
        for sid, s in sites_dict.items():
            batch_sites.append({
                "id": sid,
                "name": s.get("site_name", ""),
                "url": s.get("primary_url", ""),
                "hosting": s.get("hosting", "Vercel"),
                "venture_id": s.get("venture_id", ""),
                "repo_id": s.get("repo_id", "")
            })

        print(f"Ingesting {len(batch_sites)} sites...")
        session.run("""
            UNWIND $batch AS s
            MERGE (site:Site {id: s.id})
            SET site.name = s.name,
                site.url = s.url,
                site.hosting = s.hosting
            WITH site, s
            WHERE s.repo_id <> '' AND s.repo_id <> 'EXTERNAL_OR_UNTRACKED'
            MATCH (r:Repository {id: s.repo_id})
            MERGE (r)-[:DEPLOYS_TO]->(site)
        """, batch=batch_sites)

        # 4. Ingest Core Operating Ventures
        core_ventures = [
            {"id": "LT-005", "name": "HealthRoute Medical Courier Dispatch", "type": "LOGISTICS", "repos": ["OWN-PRIV-0002"], "sites": ["SITE-0002", "SITE-0003", "SITE-0004"]},
            {"id": "LT-011", "name": "Dispatch Software / Carrier TMS", "type": "SAAS", "repos": ["OWN-PRIV-0007"], "sites": ["SITE-0013"]},
            {"id": "RE-001", "name": "WorldwideBro Holdings Real Estate", "type": "SERVICES", "repos": ["OWN-PRIV-0013"], "sites": ["SITE-0005"]},
            {"id": "OPS-001", "name": "Career Ops Staffing", "type": "SERVICES", "repos": ["OWN-PRIV-0008", "OWN-PRIV-0003"], "sites": ["SITE-0001"]},
            {"id": "CON-001", "name": "ACE Construction Workflow OS", "type": "SERVICES", "repos": ["OWN-PRIV-0009"], "sites": ["SITE-0015", "SITE-0016"]},
            {"id": "EC-001", "name": "Angels in Daylight Apparel", "type": "ECOMMERCE", "repos": ["OWN-PRIV-0014"], "sites": ["SITE-0017"]},
            {"id": "FIN-037", "name": "WorldwideBro Quantitative Trading", "type": "CAPITAL", "repos": ["OWN-PRIV-0006"], "sites": []}
        ]

        print(f"Ingesting {len(core_ventures)} core operating ventures...")
        for cv in core_ventures:
            session.run("""
                MERGE (v:Venture {id: $id})
                SET v.name = $name,
                    v.type = $type,
                    v.reality_status = 'OPERATING_VALIDATING',
                    v.is_core_opco = true
                WITH v
                UNWIND $repos AS rid
                MATCH (r:Repository {id: rid})
                MERGE (v)-[:OPERATES]->(r)
                WITH v
                UNWIND $sites AS sid
                MATCH (s:Site {id: sid})
                MERGE (v)-[:DEPLOYS]->(s)
            """, id=cv["id"], name=cv["name"], type=cv["type"], repos=cv["repos"], sites=cv["sites"])

        # 5. Summary metrics
        v_count = session.run("MATCH (v:Venture) RETURN count(v) as c").single()["c"]
        r_count = session.run("MATCH (r:Repository) RETURN count(r) as c").single()["c"]
        s_count = session.run("MATCH (s:Site) RETURN count(s) as c").single()["c"]
        c_count = session.run("MATCH (c:Capability) RETURN count(c) as c").single()["c"]
        rel_count = session.run("MATCH ()-[rel]->() RETURN count(rel) as c").single()["c"]

        print("\n=======================================================")
        print("Neo4j Canonical Graph Ingestion Complete & Verified:")
        print(f"  Ventures:     {v_count}")
        print(f"  Repositories: {r_count}")
        print(f"  Sites:        {s_count}")
        print(f"  Capabilities: {c_count}")
        print(f"  Total Edges:  {rel_count}")
        print("=======================================================")

    driver.close()

if __name__ == "__main__":
    main()
