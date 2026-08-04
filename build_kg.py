#!/usr/bin/env python3
import json
import csv
from pathlib import Path
from neo4j import GraphDatabase

# Database config
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "ventures2026"

# File paths
WORKSPACE_DIR = Path("/Users/acebless/Documents")
REGISTRIES_DIR = WORKSPACE_DIR / "WORLDWIDEBRO-OS" / "REGISTRIES"
DATA_DIR = WORKSPACE_DIR / "WORLDWIDEBRO-OS" / "08-DATA"

VENTURES_FILE = WORKSPACE_DIR / "ventures_index.csv"
REPOS_FILE = REGISTRIES_DIR / "repository_registry_pilot.json"
EDGES_FILE = REGISTRIES_DIR / "repository_graph_edges_pilot.csv"
CORE_MAP_FILE = WORKSPACE_DIR / "IZA-OS-CORE-VENTURE-MAP.json"

def get_session():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    return driver.session(), driver

def setup_constraints(session):
    print("Setting up Neo4j constraints...")
    constraints = [
        "CREATE CONSTRAINT IF NOT EXISTS FOR (o:Organization) REQUIRE o.id IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (a:Agent) REQUIRE a.id IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (c:Capability) REQUIRE c.name IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (t:Tool) REQUIRE t.name IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (v:Venture) REQUIRE v.id IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (f:Founder) REQUIRE f.id IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (r:Repository) REQUIRE r.id IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (s:Sector) REQUIRE s.name IS UNIQUE"
    ]
    for c in constraints:
        try:
            session.run(c)
        except Exception as e:
            print(f"  Warning setting constraint: {e}")
    print("Constraints set.")

def populate_organizations(session):
    print("Populating Organizations (Holding & OpCos)...")
    
    # 1. Create Holding Company
    session.run("""
        MERGE (o:Organization {id: 'worldwidebro'})
        SET o.name = 'Worldwidebro Holdings', o.type = 'HOLDING', o.updated_at = datetime()
    """)
    
    # 2. Read IZA-OS-CORE-VENTURE-MAP.json
    if CORE_MAP_FILE.exists():
        with open(CORE_MAP_FILE) as f:
            core_data = json.load(f)
            
        for core in core_data.get("cores", []):
            opco = core["opco"]
            # Create OpCo Organization
            session.run("""
                MERGE (o:Organization {id: $id})
                SET o.name = $name, o.type = 'OPCO', o.updated_at = datetime()
                WITH o
                MATCH (p:Organization {id: 'worldwidebro'})
                MERGE (o)-[:BELONGS_TO]->(p)
            """, {
                "id": opco + "-OS",
                "name": opco + " Operating System"
            })
            
            # Create Core Venture node (e.g. CON-001)
            session.run("""
                MERGE (v:Venture {id: $venture_id})
                SET v.name = $name, v.sector = $sector, v.stage = 'active', v.updated_at = datetime()
                WITH v
                MATCH (o:Organization {id: $opco_id})
                MERGE (o)-[:OPERATES]->(v)
            """, {
                "venture_id": core["venture_id"],
                "name": core["name"],
                "sector": core["vex_sector"],
                "opco_id": opco + "-OS"
            })
            
            # Create Repository node for the core
            session.run("""
                MERGE (r:Repository {id: $id})
                SET r.name = $name, r.full_name = $full_name, r.url = $url, r.purpose = $purpose, r.updated_at = datetime()
                WITH r
                MATCH (v:Venture {id: $venture_id})
                MERGE (r)-[:POWERS]->(v)
            """, {
                "id": core["id"],
                "name": core["name"],
                "full_name": core["repo"],
                "url": core["github_url"],
                "purpose": core["purpose"],
                "venture_id": core["venture_id"]
            })
            
    print("Organizations populated.")

def populate_ventures(session):
    print("Populating Ventures from CSV...")
    if not VENTURES_FILE.exists():
        print(f"❌ {VENTURES_FILE} not found!")
        return
        
    with open(VENTURES_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            # Clean up MRR
            try:
                mrr = int(row.get("revenue_usd_monthly") or 0)
            except ValueError:
                mrr = 0
                
            session.run("""
                MERGE (v:Venture {id: $id})
                SET v.name = $name,
                    v.sector = $sector,
                    v.stage = $stage,
                    v.revenue_monthly = $mrr,
                    v.status = $status,
                    v.created_at = $created_date,
                    v.updated_at = datetime()
            """, {
                "id": row["id"],
                "name": row["name"],
                "sector": row["sector"],
                "stage": row["stage"],
                "mrr": mrr,
                "status": row["status"],
                "created_date": row["created_date"]
            })
            
            # Map sectors
            sector_name = row["sector"]
            if sector_name:
                session.run("""
                    MERGE (s:Sector {name: $sector_name})
                    WITH s
                    MATCH (v:Venture {id: $v_id})
                    MERGE (v)-[:BELONGS_TO_SECTOR]->(s)
                """, {
                    "sector_name": sector_name,
                    "v_id": row["id"]
                })
                
                # Determine OpCo link based on sector
                opco_id = None
                sec_lower = sector_name.lower()
                if "construction" in sec_lower:
                    opco_id = "CON-OS"
                elif "staffing" in sec_lower or "labor" in sec_lower:
                    opco_id = "STA-OS"
                elif "real" in sec_lower or "estate" in sec_lower or "beauty" in sec_lower or "wellness" in sec_lower:
                    opco_id = "RE-OS"
                elif "education" in sec_lower:
                    opco_id = "EDU-OS"
                elif "financial" in sec_lower or "finance" in sec_lower:
                    opco_id = "FIN-OS"
                elif "transportation" in sec_lower or "logistics" in sec_lower or "shipping" in sec_lower:
                    opco_id = "LOG-OS"
                elif "marketing" in sec_lower or "marketplace" in sec_lower:
                    opco_id = "MKT-OS"
                
                if opco_id:
                    session.run("""
                        MATCH (s:Sector {name: $sector_name})
                        MATCH (o:Organization {id: $opco_id})
                        MERGE (s)-[:BELONGS_TO_OPCO]->(o)
                    """, {
                        "sector_name": sector_name,
                        "opco_id": opco_id
                    })
                    
            count += 1
            
    print(f"Populated {count} ventures.")

def populate_repositories(session):
    print("Populating Repositories from JSON...")
    if not REPOS_FILE.exists():
        print(f"❌ {REPOS_FILE} not found!")
        return
        
    with open(REPOS_FILE) as f:
        repos_data = json.load(f)
        
    count = 0
    for repo in repos_data:
        try:
            stars = int(repo.get("stars") or 0)
        except ValueError:
            stars = 0
            
        try:
            reusability = int(repo.get("reusability_score") or 0)
        except ValueError:
            reusability = 0
            
        try:
            revenue_potential = int(repo.get("revenue_potential") or 0)
        except ValueError:
            revenue_potential = 0
            
        try:
            strategic_value = int(repo.get("strategic_value") or 0)
        except ValueError:
            strategic_value = 0
            
        session.run("""
            MERGE (r:Repository {id: $id})
            SET r.name = $name,
                r.full_name = $full_name,
                r.url = $url,
                r.language = $language,
                r.stars = $stars,
                r.purpose = $purpose,
                r.category = $category,
                r.reusability_score = $reusability,
                r.revenue_potential = $revenue_potential,
                r.strategic_value = $strategic_value,
                r.updated_at = datetime()
        """, {
            "id": repo["repo_name"],
            "name": repo["repo_name"],
            "full_name": repo["full_name"],
            "url": repo["url"],
            "language": repo.get("language") or "unknown",
            "stars": stars,
            "purpose": repo.get("purpose") or "",
            "category": repo.get("category") or "Unclassified",
            "reusability": reusability,
            "revenue_potential": revenue_potential,
            "strategic_value": strategic_value
        })
        count += 1
        
    print(f"Populated {count} repositories.")

def populate_relationships(session):
    print("Populating Relationships from edges CSV...")
    if not EDGES_FILE.exists():
        print(f"❌ {EDGES_FILE} not found!")
        return
        
    with open(EDGES_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        powers_count = 0
        enables_count = 0
        
        for row in reader:
            source = row["source_repo"]
            rel = row["relationship"]
            target = row["target"]
            
            if rel == "POWERS":
                # Repo -> Venture link
                res = session.run("""
                    MATCH (r:Repository {id: $source})
                    MATCH (v:Venture {id: $target})
                    MERGE (r)-[p:POWERS]->(v)
                    SET p.updated_at = datetime()
                    RETURN r.id, v.id
                """, {
                    "source": source,
                    "target": target
                })
                if res.peek():
                    powers_count += 1
                    
            elif rel == "ENABLES":
                # Repo -> Capability link. First merge capability node
                # Set dynamic category & keywords
                keywords = [target.lower()]
                session.run("""
                    MERGE (c:Capability {name: $name})
                    ON CREATE SET c.description = 'Dynamic capability for ' + $name,
                                  c.keywords = $keywords,
                                  c.category = 'technology',
                                  c.created_at = datetime()
                    SET c.updated_at = datetime()
                """, {
                    "name": target,
                    "keywords": keywords
                })
                
                res = session.run("""
                    MATCH (r:Repository {id: $source})
                    MATCH (c:Capability {name: $target})
                    MERGE (r)-[e:ENABLES]->(c)
                    SET e.updated_at = datetime()
                    RETURN r.id, c.name
                """, {
                    "source": source,
                    "target": target
                })
                if res.peek():
                    enables_count += 1
                    
    print(f"Relationships populated: {powers_count} POWERS links, {enables_count} ENABLES links.")

def verify_graph(session):
    print("\nVerifying final Graph State in Neo4j...")
    
    nodes = session.run("MATCH (n) RETURN labels(n)[0] as label, count(*) as count ORDER BY count DESC")
    print("Nodes in Graph:")
    for record in nodes:
        print(f"  - {record['label']}: {record['count']}")
        
    rels = session.run("MATCH ()-[r]->() RETURN type(r) as type, count(*) as count ORDER BY count DESC")
    print("Relationships in Graph:")
    for record in rels:
        print(f"  - {record['type']}: {record['count']}")

def main():
    print("="*60)
    print("STARTING PROGRAMMATIC KNOWLEDGE GRAPH INGESTION")
    print("="*60)
    
    session, driver = get_session()
    try:
        setup_constraints(session)
        populate_organizations(session)
        populate_ventures(session)
        populate_repositories(session)
        populate_relationships(session)
        verify_graph(session)
    except Exception as e:
        print(f"\n❌ Ingestion failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        session.close()
        driver.close()
        
    print("\n"+"="*60)
    print("INGESTION PROCESS COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()
