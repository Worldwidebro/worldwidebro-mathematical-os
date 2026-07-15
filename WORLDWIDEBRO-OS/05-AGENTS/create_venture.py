#!/usr/bin/env python3
"""
IZA OS Venture Factory CLI Spawner
Fully automates the Stage 2 creation pipeline: seeder + Neo4j mapping + Postgres logging + VEX sync.
"""
import os
import sys
import yaml
import json
import argparse
import csv
import subprocess
from datetime import datetime
from neo4j import GraphDatabase
import psycopg2

DOCS = "/Users/acebless/Documents"
WORLDWIDEBRO_OS = os.path.join(DOCS, "WORLDWIDEBRO-OS")
REGISTRIES = os.path.join(WORLDWIDEBRO_OS, "08-DATA/registries")
SECTOR_REGISTRY = os.path.join(REGISTRIES, "sector_registry.yaml")
AGENT_REGISTRY = os.path.join(WORLDWIDEBRO_OS, "05-AGENTS/agent_registry.yaml")
VENTURES_CSV = os.path.join(REGISTRIES, "ventures.csv")
VEX_DIR = os.path.join(DOCS, "vex-hero-site")

# Import service endpoints from local os_env helper
sys.path.append(DOCS)
try:
    from os_env import NEO4J_URI, NEO4J_AUTH
except ImportError:
    NEO4J_URI = "bolt://localhost:7687"
    NEO4J_AUTH = ("neo4j", "ventures2026")

POSTGRES_URL = os.environ.get("PG_URL", "postgresql://divinejohns@100.87.214.70:5432/iza_os_ventures")

class VentureFactory:
    def __init__(self, name, sector, location, target, revenue_goal):
        self.name = name
        self.sector = sector.lower()
        self.location = location or "United States"
        self.target = target or "General Market"
        self.revenue_goal = float(revenue_goal) if revenue_goal else 0.0
        
        # Standardized prefix and folder path
        self.venture_prefix = self.sector[:3].upper()
        # Find next index from CSV
        next_idx = self.get_next_index()
        self.venture_id = f"{self.venture_prefix}-{next_idx:03d}"
        
        self.folder_name = f"{self.sector}-000-{self.name.replace(' ', '-').lower()}"
        self.venture_dir = os.path.join(DOCS, self.folder_name)

    def get_next_index(self):
        try:
            with open(VENTURES_CSV, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                indices = []
                for row in reader:
                    v_id = row.get("venture_id", "")
                    if v_id.startswith(self.venture_prefix):
                        try:
                            indices.append(int(v_id.split("-")[1]))
                        except (ValueError, IndexError):
                            pass
                return max(indices) + 1 if indices else 1
        except Exception:
            return 1

    def load_yaml(self, path):
        if not os.path.exists(path):
            print(f"Error: Config not found at {path}")
            return None
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def query_neo4j_repos(self, caps):
        if not caps:
            return []
        try:
            driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
            with driver.session() as session:
                query = """
                MATCH (c:Capability)<-[:IMPLEMENTS]-(r:Repo)
                WHERE c.name IN $caps
                RETURN DISTINCT r.name as name
                """
                res = session.run(query, caps=caps)
                repos = [row["name"] for row in res]
                driver.close()
                return repos
        except Exception as e:
            print(f"⚠️ Neo4j Repo query failed ({e}). Defaulting to local catalog.")
            return ["medusa", "stripe", "keycloak", "twenty-crm"]

    def write_to_neo4j(self, caps):
        try:
            driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
            with driver.session() as session:
                # Merge Sector
                session.run("MERGE (s:Sector {name: $sector})", sector=self.sector)
                # Merge Venture
                session.run("""
                MERGE (v:Venture {id: $vid})
                SET v.name = $name, v.stage = 'Planned', v.status = 'active'
                """, vid=self.venture_id, name=self.name)
                # Link Venture to Sector
                session.run("""
                MATCH (v:Venture {id: $vid}), (s:Sector {name: $sector})
                MERGE (v)-[:MAPPED_TO]->(s)
                """, vid=self.venture_id, sector=self.sector)
                # Link Venture to required capabilities
                for cap in caps:
                    session.run("""
                    MERGE (c:Capability {name: $cap})
                    WITH c
                    MATCH (v:Venture {id: $vid})
                    MERGE (v)-[:USES]->(c)
                    """, cap=cap, vid=self.venture_id)
            driver.close()
            print("🌐 Neo4j: Venture and capability nodes merged successfully.")
        except Exception as e:
            print(f"⚠️ Neo4j write failed: {e}")

    def write_to_postgres(self):
        try:
            conn = psycopg2.connect(POSTGRES_URL)
            cur = conn.cursor()
            query = """
            INSERT INTO ventures (venture_name, category, status, revenue_estimate, completion_percentage)
            VALUES (%s, %s, 'Planned', %s, 0);
            """
            cur.execute(query, (self.name, self.sector, self.revenue_goal))
            conn.commit()
            cur.close()
            conn.close()
            print("🐘 PostgreSQL: Registered venture in postgres database.")
        except Exception as e:
            print(f"⚠️ PostgreSQL write failed: {e}")

    def append_to_csv(self):
        try:
            fieldnames = []
            with open(VENTURES_CSV, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                headers = next(reader)
                fieldnames = headers
                
            with open(VENTURES_CSV, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                row = {
                    "venture_id": self.venture_id,
                    "name": self.name,
                    "sector": self.sector,
                    "stage": "planned",
                    "status": "planned",
                    "revenue_ytd": "0",
                    "revenue_target": str(self.revenue_goal),
                    "costs_mom": "0",
                    "opco": self.sector.upper()
                }
                # Fill missing columns with empty string
                row = {k: row.get(k, "") for k in fieldnames}
                writer.writerow(row)
            print("📝 CSV: Appended venture entry to registries/ventures.csv.")
        except Exception as e:
            print(f"⚠️ CSV update failed: {e}")

    def spawn(self):
        print(f"\n🏭 VENTURE FACTORY: Seeding new Venture ID '{self.venture_id}' under {self.folder_name}...")
        
        # Load registry configs
        sectors_cfg = self.load_yaml(SECTOR_REGISTRY)
        agents_cfg = self.load_yaml(AGENT_REGISTRY)
        
        if not sectors_cfg or not agents_cfg:
            return False
            
        sector_info = next((s for s in sectors_cfg.get("sectors", []) if s["name"] == self.sector), None)
        if not sector_info:
            print(f"Warning: Sector '{self.sector}' not configured in registry. Using fallback defaults.")
            sector_info = {
                "name": self.sector,
                "label": self.sector.capitalize(),
                "required_capabilities": ["api", "database", "authentication"],
                "agents": [{"role": "CEO", "name": f"{self.sector.capitalize()} CEO Agent"}]
            }
            
        # Create directories
        subdirs = [
            "00_IDENTITY", "01_STRATEGY", "02_PRODUCT", "03_CUSTOMERS",
            "05_SALES", "06_FINANCE", "07_OPERATIONS", "08_TECHNOLOGY",
            "09_AI_AGENTS", "10_DATA", "14_ANALYTICS"
        ]
        os.makedirs(self.venture_dir, exist_ok=True)
        for s in subdirs:
            os.makedirs(os.path.join(self.venture_dir, s), exist_ok=True)
            
        # 1. Write identity
        identity = f"""# Venture Profile: {self.name}
Venture ID: {self.venture_id}
Sector: {self.sector}
Location: {self.location}
Target Audience: {self.target}
"""
        with open(os.path.join(self.venture_dir, "00_IDENTITY/venture_profile.md"), "w") as f:
            f.write(identity)
            
        # 2. Write strategy
        strategy = f"""# Strategy: {self.name}
Revenue Goal: ${self.revenue_goal:,.2f}/year
Monetization: Subscription SaaS / Professional Service
"""
        with open(os.path.join(self.venture_dir, "01_STRATEGY/business_model.md"), "w") as f:
            f.write(strategy)
            
        # 3. Query Neo4j to map implementing repos
        caps = sector_info.get("required_capabilities", [])
        mapped_repos = self.query_neo4j_repos(caps)
        tech_map = f"""# Technology Map: {self.name}
Required Capabilities: {', '.join(caps)}

## Mapped Implementing Repositories (from Capability Graph)
{chr(10).join(f'- {r}' for r in mapped_repos)}
"""
        with open(os.path.join(self.venture_dir, "08_TECHNOLOGY/repository_map.md"), "w") as f:
            f.write(tech_map)
            
        # 3b. Symlink real local repositories if present in workspace
        self.link_local_repositories(mapped_repos)
            
        # 4. Generate AI workforce config
        mapped_agents = []
        for role_entry in sector_info.get("agents", []):
            agent_details = next((a for a in agents_cfg.get("agents", []) if a["role"].lower() == role_entry["role"].lower() or a["name"].lower() == role_entry["name"].lower()), None)
            if agent_details:
                mapped_agents.append(agent_details)
            else:
                mapped_agents.append({
                    "name": role_entry["name"],
                    "role": role_entry["role"],
                    "mission": "Operate sector workflows dynamically.",
                    "authority": ["read_local_database"],
                    "limits": ["cannot_alter_production"],
                    "brain": {"reasoning": "qwen2.5:7b", "coding": "deepseek-coder:6.7b", "embeddings": "nomic-embed-text"}
                })
        agent_config = {
            "venture": self.name,
            "id": self.venture_id,
            "agents": mapped_agents
        }
        with open(os.path.join(self.venture_dir, "09_AI_AGENTS/agent_registry.yaml"), "w") as f:
            yaml.safe_dump(agent_config, f, sort_keys=False)
            
        # 5. Write venture state database file
        state = {
            "id": self.venture_id,
            "name": self.name,
            "sector": self.sector,
            "stage": "planned",
            "revenue": 0.0,
            "customers": 0,
            "agents_active": len(mapped_agents),
            "health_score": 100,
            "next_actions": [
                "run repo lint",
                "create landing page waitlist",
                "link to twenty CRM"
            ]
        }
        with open(os.path.join(self.venture_dir, "venture.json"), "w") as f:
            json.dump(state, f, indent=2)
            
        # Write to databases & registries
        self.write_to_neo4j(caps)
        self.write_to_postgres()
        self.append_to_csv()
        
        # 5b. Compile and execute operational & technical blueprints (Venture SOP + Product PRD)
        self.compile_and_deploy_blueprints()
        
        # 6. Trigger VEX site rebuild
        self.rebuild_vex()
        
        print("🎉 VENTURE CREATION PIPELINE COMPLETED.")
        return True

    def rebuild_vex(self):
        try:
            print("🔄 VEX: Running VEX public data generator...")
            res_gen = subprocess.run(
                ["node", "scripts/generate-public-data.mjs"],
                capture_output=True,
                text=True,
                cwd=VEX_DIR
            )
            if res_gen.returncode == 0:
                print("   Data generated: portfolio.public.json updated.")
                print("🔄 VEX: Building production site bundles...")
                res_build = subprocess.run(
                    ["npm", "run", "build"],
                    capture_output=True,
                    text=True,
                    cwd=VEX_DIR
                )
                if res_build.returncode == 0:
                    print("   Site built successfully: ready for staging deploy.")
                else:
                    print(f"⚠️ VEX Build failed: {res_build.stderr}")
            else:
                print(f"⚠️ VEX Data Generation failed: {res_gen.stderr}")
        except Exception as e:
            print(f"⚠️ VEX Update failed: {e}")

    def execute_sql_schema(self, sql_content):
        try:
            conn = psycopg2.connect(POSTGRES_URL)
            cur = conn.cursor()
            cur.execute(sql_content)
            conn.commit()
            cur.close()
            conn.close()
            print("   PostgreSQL: Executed compiled database schemas successfully.")
        except Exception as e:
            print(f"   ⚠️ PostgreSQL Schema execution failed: {e}")

    def compile_and_deploy_blueprints(self):
        print("🛠️ Knowledge Compiler: Generating operational SOPs and technical schemas...")
        
        # Define 4 core operational departments / system modules
        departments = [
            ("Operations & Logistics", "Core State Engine"),
            ("Marketing & Growth Hooks", "REST API Gateway"),
            ("Sales Pipelines & CRM", "Database Schema & Models"),
            ("HR & Hiring Playbook", "Client Web Frontend")
        ]
        
        # 1. Compile SOPs into 07_OPERATIONS/
        ops_dir = os.path.join(self.venture_dir, "07_OPERATIONS")
        manual_content = f"# Venture Operations Manual: {self.name}\n\n**Sector:** {self.sector}\n**Departments:**\n"
        for idx, (dept, comp) in enumerate(departments, 1):
            manual_content += f"## Department {idx}: {dept}\n*Standard Operating Procedures and drills.*\n\n"
            dept_dir = os.path.join(ops_dir, f"dept_{idx}_{dept.lower().replace(' ', '_').replace('&', 'and')}")
            os.makedirs(dept_dir, exist_ok=True)
            
            # Write SOP files
            with open(os.path.join(dept_dir, "standard_operating_procedure.md"), "w") as f:
                f.write(f"# Standard Operating Procedure: {dept}\n\n1. Define operational bounds for {self.name}.\n2. Trigger department workflows.\n")
            with open(os.path.join(dept_dir, "training_playbook.md"), "w") as f:
                f.write(f"# Training Playbook: {dept}\n\nOnboarding instructions for staff and operators in {self.name}.\n")
            with open(os.path.join(dept_dir, "competency_quiz.md"), "w") as f:
                f.write(f"# Competency Assessment: {dept}\n\n1. Operational checklist verification quiz items.\n")
            with open(os.path.join(dept_dir, "weekly_drill_checklist.md"), "w") as f:
                f.write(f"# Weekly Checklist: {dept}\n\nOperational checks for {self.name}.\n")
        
        with open(os.path.join(ops_dir, "operations_manual.md"), "w") as f:
            f.write(manual_content)
        print("   SOPs written to 07_OPERATIONS/ successfully.")
        
        # 2. Compile PRDs into 08_TECHNOLOGY/
        tech_dir = os.path.join(self.venture_dir, "08_TECHNOLOGY")
        prd_content = f"# Product Requirements Document (PRD): {self.name}\n\n**Sector/Platform:** {self.sector}\n**Technical Modules:**\n"
        full_sql_content = ""
        
        for idx, (dept, comp) in enumerate(departments, 1):
            prd_content += f"## Module {idx}: {comp}\n*Technical specs and schema definitions.*\n\n"
            comp_dir = os.path.join(tech_dir, f"module_{idx}_{comp.lower().replace(' ', '_').replace('&', 'and')}")
            os.makedirs(comp_dir, exist_ok=True)
            
            # Generate deliverables
            with open(os.path.join(comp_dir, "feature_specification.md"), "w") as f:
                f.write(f"# Feature Specification: {comp}\n\nUser stories and technical requirements for {self.name}.\n")
            with open(os.path.join(comp_dir, "api_spec_openapi.yaml"), "w") as f:
                f.write(f"openapi: 3.0.0\ninfo:\n  title: {comp} API\n  version: 1.0.0\npaths:\n  /api/execute:\n    post:\n      summary: Trigger {comp} logic\n")
            
            # Generate SQL Schema table name specific to this venture and component
            table_name = f"{self.venture_prefix.lower()}_{self.venture_id.split('-')[1]}_{comp.lower().replace(' ', '_').replace('&', 'and')}"
            sql = f"-- Database Schema: {comp}\nCREATE TABLE IF NOT EXISTS {table_name} (\n  id SERIAL PRIMARY KEY,\n  venture_id VARCHAR(50) DEFAULT '{self.venture_id}',\n  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);\n"
            full_sql_content += sql
            with open(os.path.join(comp_dir, "database_schema.sql"), "w") as f:
                f.write(sql)
                
            tool_def = {
                "name": f"{self.venture_prefix.lower()}_{comp.lower().replace(' ', '_').replace('&', 'and')}",
                "description": f"Orchestrates technical commands for {comp} in venture {self.name}",
                "parameters": {"type": "object", "properties": {}}
            }
            with open(os.path.join(comp_dir, "agentic_tool_definitions.json"), "w") as f:
                json.dump(tool_def, f, indent=2)
                
        with open(os.path.join(tech_dir, "prd_architecture.md"), "w") as f:
            f.write(prd_content)
        print("   PRD assets and schemas written to 08_TECHNOLOGY/ successfully.")
        
        # 3. Automatically deploy SQL schemas to postgres database
        if full_sql_content:
            self.execute_sql_schema(full_sql_content)

    def link_local_repositories(self, mapped_repos):
        repos_dir = os.path.join(self.venture_dir, "08_TECHNOLOGY/repos")
        os.makedirs(repos_dir, exist_ok=True)
        print("🔗 Repository Linker: Linking local code repositories to 08_TECHNOLOGY/repos...")
        
        for r in mapped_repos:
            local_repo_path = os.path.join(DOCS, r)
            if os.path.exists(local_repo_path):
                symlink_path = os.path.join(repos_dir, r)
                # Remove if it exists (e.g. from previous run)
                if os.path.islink(symlink_path) or os.path.exists(symlink_path):
                    try:
                        os.unlink(symlink_path)
                    except:
                        pass
                try:
                    os.symlink(local_repo_path, symlink_path)
                    print(f"   Linked local repo: {r} -> {local_repo_path}")
                except Exception as e:
                    print(f"   ⚠️ Symlink failed for {r}: {e}")
            else:
                print(f"   (Reference only: local repository {r} not found under {DOCS})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IZA OS Venture Spawner CLI")
    parser.add_argument("--name", required=True, help="Name of the venture")
    parser.add_argument("--sector", required=True, help="OpCo sector key (e.g. construction, ecommerce, financial)")
    parser.add_argument("--location", help="Target geographic location")
    parser.add_argument("--target", help="Ideal Customer Profile target")
    parser.add_argument("--revenue", help="Target annual revenue goal")
    args = parser.parse_args()
    
    factory = VentureFactory(args.name, args.sector, args.location, args.target, args.revenue)
    factory.spawn()
