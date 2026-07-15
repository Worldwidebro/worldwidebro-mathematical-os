#!/usr/bin/env python3
"""
IZA OS Agent Factory
Generates standardized venture folders with agent, strategy, tech, database, and KPI files.
"""
import os
import sys
import yaml
import json

DOCS = "/Users/acebless/Documents"
WORLDWIDEBRO_OS = os.path.join(DOCS, "WORLDWIDEBRO-OS")
REGISTRIES = os.path.join(WORLDWIDEBRO_OS, "08-DATA/registries")
SECTOR_REGISTRY = os.path.join(REGISTRIES, "sector_registry.yaml")
AGENT_REGISTRY = os.path.join(WORLDWIDEBRO_OS, "05-AGENTS/agent_registry.yaml")

class AgentFactory:
    def __init__(self, name, sector):
        self.name = name
        self.sector = sector.lower()
        self.folder_name = f"{self.sector}-000-{self.name.replace(' ', '-').lower()}"
        self.venture_dir = os.path.join(DOCS, self.folder_name)
        
    def load_yaml(self, path):
        if not os.path.exists(path):
            print(f"Error: Registry file not found at {path}")
            return None
        with open(path, "r") as f:
            return yaml.safe_load(f)
            
    def build_venture(self):
        print(f"\n🚀 AGENT FACTORY: Spawning venture '{self.name}' (Sector: {self.sector})...")
        
        # Load configurations
        sectors_cfg = self.load_yaml(SECTOR_REGISTRY)
        agents_cfg = self.load_yaml(AGENT_REGISTRY)
        
        if not sectors_cfg or not agents_cfg:
            return False
            
        # Find sector configurations
        sector_info = next((s for s in sectors_cfg.get("sectors", []) if s["name"] == self.sector), None)
        if not sector_info:
            print(f"Warning: Sector '{self.sector}' not found in registry. Using default settings.")
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
        for sub in subdirs:
            os.makedirs(os.path.join(self.venture_dir, sub), exist_ok=True)
            
        # 1. Write identity
        profile_content = f"""# Venture Profile: {self.name}
Identity: {sector_info['label']} Venture
Sector: {self.sector}
Stage: Idea / Planned
Status: Planned
"""
        with open(os.path.join(self.venture_dir, "00_IDENTITY/venture_profile.md"), "w") as f:
            f.write(profile_content)
            
        # 2. Write strategy
        strategy_content = f"""# Business Model: {self.name}
Venture Type: B2B SaaS / Portal
Target Customers: {sector_info['label']} Operators
Revenue Stream: Subscription Billing (Stripe)
"""
        with open(os.path.join(self.venture_dir, "01_STRATEGY/business_model.md"), "w") as f:
            f.write(strategy_content)
            
        # 3. Write active capabilities to tech stack
        tech_content = f"""# Technology Map: {self.name}
Required Capabilities: {', '.join(sector_info['required_capabilities'])}
Deployment: Vercel (Frontend) + Supabase/PostgreSQL (Backend)
"""
        with open(os.path.join(self.venture_dir, "08_TECHNOLOGY/repository_map.md"), "w") as f:
            f.write(tech_content)
            
        # 4. Generate AI workforce configs
        mapped_agents = []
        for role_entry in sector_info.get("agents", []):
            agent_details = next((a for a in agents_cfg.get("agents", []) if a["role"].lower() == role_entry["role"].lower() or a["name"].lower() == role_entry["name"].lower()), None)
            if agent_details:
                mapped_agents.append(agent_details)
            else:
                mapped_agents.append({
                    "name": role_entry["name"],
                    "role": role_entry["role"],
                    "mission": "Operate domain tasks dynamically.",
                    "authority": ["read_local_database"],
                    "limits": ["cannot_alter_production"],
                    "brain": {"reasoning": "qwen2.5:7b", "coding": "deepseek-coder:6.7b", "embeddings": "nomic-embed-text"}
                })
                
        agent_registry_content = {
            "venture": self.name,
            "sector": self.sector,
            "agents": mapped_agents
        }
        with open(os.path.join(self.venture_dir, "09_AI_AGENTS/agent_registry.yaml"), "w") as f:
            yaml.safe_dump(agent_registry_content, f, sort_keys=False)
            
        # 5. Write venture state tracking
        state_content = {
            "name": self.name,
            "sector": self.sector,
            "stage": "Idea / Planned",
            "revenue": 0,
            "customers": 0,
            "agents_active": len(mapped_agents),
            "health_score": 100,
            "next_actions": [
                "run repo scan on capabilities",
                "generate database schema",
                "compile initial dashboard"
            ]
        }
        with open(os.path.join(self.venture_dir, "venture.json"), "w") as f:
            json.dump(state_content, f, indent=2)
            
        # 6. Write KPI dashboard
        kpi_content = {
            "venture": self.name,
            "active_metrics": {
                "visitors": 0,
                "leads": 0,
                "subscribers": 0,
                "api_latency_ms": 0,
                "agent_success_rate": 1.0
            }
        }
        with open(os.path.join(self.venture_dir, "14_ANALYTICS/KPI_dashboard.json"), "w") as f:
            json.dump(kpi_content, f, indent=2)
            
        print(f"✅ Spawned successfully!")
        print(f"   Directory: {self.venture_dir}")
        print(f"   Agent config: 09_AI_AGENTS/agent_registry.yaml ({len(mapped_agents)} agents active)")
        print(f"   Venture tracking: venture.json")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 agent_factory.py <VentureName> <Sector>")
        sys.exit(1)
    name_arg = sys.argv[1]
    sector_arg = sys.argv[2]
    factory = AgentFactory(name_arg, sector_arg)
    factory.build_venture()
