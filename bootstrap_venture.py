#!/usr/bin/env python3
import os
import sys
import json
import argparse
from datetime import datetime
from supabase import create_client
from neo4j import GraphDatabase

# Database connection details
SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
NEO4J_URI = "bolt://localhost:7687"
NEO4J_AUTH = ("neo4j", "ventures2026")

def load_env():
    """Load env vars from .env files."""
    for env_path in ["/Users/acebless/Documents/.env", "/Users/acebless/.env"]:
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if "=" in line and not line.strip().startswith("#"):
                        k, v = line.strip().split("=", 1)
                        os.environ[k.strip()] = v.strip()

def setup_directory(venture_id, name, sector, opco, capabilities, synergies_list):
    """Create directory structure and fill out templates."""
    base_dir = f"/Users/acebless/Documents/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/{venture_id}"
    docs_dir = os.path.join(base_dir, "docs")
    financials_dir = os.path.join(base_dir, "financials")
    
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(financials_dir, exist_ok=True)
    
    # 1. Write venture.json
    venture_metadata = {
        "venture_id": venture_id,
        "name": name,
        "sector": sector,
        "parent_opco": opco,
        "capabilities": capabilities,
        "synergies": synergies_list,
        "created_at": datetime.now().isoformat(),
        "status": "active"
    }
    with open(os.path.join(base_dir, "venture.json"), "w") as f:
        json.dump(venture_metadata, f, indent=2)
        
    # 2. Initialize financials
    with open(os.path.join(financials_dir, "deployments.csv"), "w") as f:
        f.write("date,amount,predicted_roi_pct,actual_roi_pct,status,error_msg\n")
        
    with open(os.path.join(financials_dir, "unit_economics.csv"), "w") as f:
        f.write("metric,value\ncac,500\nltv,3000\ngross_margin_pct,85\n")
        
    # 3. Populate template docs
    template_dir = "/Users/acebless/Documents/templates/venture/docs"
    replacements = {
        "{{VENTURE_NAME}}": name,
        "{{VENTURE_ID}}": venture_id,
        "{{SECTOR}}": sector,
        "{{PARENT_OPCO}}": opco,
        "{{DATE}}": datetime.now().strftime("%Y-%m-%d"),
        "{{GITHUB_URL}}": f"https://github.com/Worldwidebro/{venture_id.lower()}-{name.replace(' ', '-').lower()}",
        "{{CAPABILITIES}}": "\n".join([f"- {c}" for c in capabilities]),
        "{{SYNERGIES}}": "\n".join([f"- {s['type']} with {s['other_id']}" for s in synergies_list]) if synergies_list else "None defined."
    }
    
    for doc_name in ["pitch.md", "onboarding_checklist.md", "MUTUAL-SYNERGY-AGREEMENT.md", "VENTURE-COMPLIANCE-FORM.md"]:
        src = os.path.join(template_dir, doc_name)
        dst = os.path.join(docs_dir, doc_name)
        if os.path.exists(src):
            with open(src, "r") as sf:
                content = sf.read()
            for placeholder, val in replacements.items():
                content = content.replace(placeholder, val)
            with open(dst, "w") as df:
                df.write(content)
                
    print(f"✓ Created folder structure & files at: {base_dir}")
    return base_dir

def sync_to_neo4j(venture_id, name, sector, opco, capabilities, synergies_list):
    """Register venture and synergies in local Neo4j graph database."""
    driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
    with driver.session() as session:
        # Merge Venture Node and link to Sector & OPCO
        session.run("""
            MERGE (v:Venture {id: $id})
            ON CREATE SET v.name = $name, v.sector = $sector, v.stage = 'growth', v.status = 'active'
            ON MATCH SET v.name = $name, v.status = 'active'
            
            MERGE (o:Organization {id: $opco, type: 'OPCO'})
            MERGE (v)-[:BELONGS_TO]->(o)
            
            MERGE (s:Sector {name: $sector})
            MERGE (v)-[:BELONGS_TO_SECTOR]->(s)
        """, id=venture_id, name=name, sector=sector, opco=opco)
        
        # Link Capabilities
        for cap in capabilities:
            session.run("""
                MATCH (v:Venture {id: $venture_id})
                MERGE (c:Capability {name: $cap})
                MERGE (v)-[:NEEDS]->(c)
            """, venture_id=venture_id, cap=cap.strip())
            
        # Link Synergies
        for syn in synergies_list:
            other_id = syn.get("other_id")
            syn_type = syn.get("type", "PARTNERS_WITH")
            session.run(f"""
                MATCH (v:Venture {{id: $venture_id}})
                MERGE (other:Venture {{id: $other_id}})
                MERGE (v)-[:{syn_type}]->(other)
            """, venture_id=venture_id, other_id=other_id)
            
    driver.close()
    print(f"✓ Registered '{venture_id}' in Neo4j graph with {len(capabilities)} capabilities & {len(synergies_list)} synergies.")

def sync_to_supabase(venture_id, name, sector, opco):
    """Upsert venture metadata in Supabase 'ventures' and 'agent_credentials' tables."""
    supabase_key = os.getenv("SUPABASE_KEY")
    if not supabase_key:
        print("⚠️ Warning: SUPABASE_KEY not found. Skipping Supabase write.")
        return
        
    client = create_client(SUPABASE_URL, supabase_key)
    
    # Upsert Ventures Table
    venture_row = {
        "venture_id": venture_id,
        "name": name,
        "slug": venture_id.lower(),
        "sector": sector,
        "status": "active",
        "parent_opco": opco,
        "monthly_revenue": 0,
        "github_url": f"https://github.com/Worldwidebro/{venture_id.lower()}-{name.replace(' ', '-').lower()}"
    }
    client.table("ventures").upsert(venture_row, on_conflict="venture_id").execute()
    
    # Write initial credentials placeholder
    credential_row = {
        "agent_id": venture_id,
        "status": "active"
    }
    client.table("agent_credentials").upsert(credential_row, on_conflict="agent_id").execute()
    
    print(f"✓ Synced '{venture_id}' to Supabase operational registry.")

def main():
    load_env()
    
    parser = argparse.ArgumentParser(description="Bootstrap new Venture under AI Boss OS V1")
    parser.add_argument("--id", required=True, help="Venture ID (e.g. CON-011)")
    parser.add_argument("--name", required=True, help="Venture Name")
    parser.add_argument("--sector", required=True, help="Sector name")
    parser.add_argument("--opco", required=True, help="Parent OPCO (e.g. CON-OS)")
    parser.add_argument("--capabilities", required=True, help="Comma-separated list of capabilities")
    parser.add_argument("--synergies", help="JSON string listing synergies with other ventures")
    
    args = parser.parse_args()
    
    capabilities_list = [c.strip() for c in args.capabilities.split(",") if c.strip()]
    
    synergies_list = []
    if args.synergies:
        try:
            synergies_list = json.loads(args.synergies)
        except json.JSONDecodeError as e:
            print(f"Error parsing synergies JSON: {e}")
            sys.exit(1)
            
    print(f"\n🚀 Bootstrapping Venture '{args.name}' ({args.id})...")
    
    # 1. Setup local files
    setup_directory(args.id, args.name, args.sector, args.opco, capabilities_list, synergies_list)
    
    # 2. Sync to Neo4j Graph
    sync_to_neo4j(args.id, args.name, args.sector, args.opco, capabilities_list, synergies_list)
    
    # 3. Sync to Supabase Registry
    sync_to_supabase(args.id, args.name, args.sector, args.opco)
    
    print(f"✨ Venture '{args.id}' is successfully bootstrapped and ready for autonomous routine operations!\n")

if __name__ == "__main__":
    main()
