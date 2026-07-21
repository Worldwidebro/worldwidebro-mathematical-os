#!/usr/bin/env python3
"""
align_sales_engines.py
Automates the alignment of Sales Scripts, Capability Statements, Formation Trackers,
Agent Communication Maps, and Ecosystem blueprints across all 100+ active portfolio ventures.
"""
import os
import sys
import re
import argparse

DOCS_DIR = "/Users/acebless/Documents"
WORLDWIDEBRO_OS = os.path.join(DOCS_DIR, "WORLDWIDEBRO-OS")
OPERATIONS_DIR = os.path.join(WORLDWIDEBRO_OS, "04-OPERATIONS")
ACTIVE_VENTURES_DIR = os.path.join(WORLDWIDEBRO_OS, "03-PORTFOLIO/ventures/active")
PROPOSED_VENTURES_DIR = os.path.join(WORLDWIDEBRO_OS, "03-PORTFOLIO/ventures/proposed")

# Mapping directory prefixes to sector keys
SECTOR_MAP = {
    "CON": "CON",
    "EC": "ECO",
    "ECO": "ECO",
    "LT": "LOG",
    "LOG": "LOG",
    "FIN": "FIN",
    "TEC": "TEC",
    "TECH": "TEC",
    "RE": "REA",
    "REA": "REA"
}

def parse_venture_meta(dir_name, dir_path):
    """
    Extracts Venture ID and Name from directory name or internal config files.
    """
    v_id = "TBD"
    v_name = dir_name
    
    # Try parsing venture.json
    json_path = os.path.join(dir_path, "venture.json")
    if os.path.exists(json_path):
        import json
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("id", "TBD"), data.get("name", dir_name), data.get("stage", "development")
        except:
            pass
            
    # Try parsing VENTURE.md
    md_path = os.path.join(dir_path, "VENTURE.md")
    if os.path.exists(md_path):
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()
                id_match = re.search(r"Venture ID\s*(?::|\|)\s*([A-Za-z0-9\-]+)", content)
                name_match = re.search(r"^#\s*(.+)$", content, re.MULTILINE)
                if id_match:
                    v_id = id_match.group(1).strip()
                if name_match:
                    v_name = name_match.group(1).strip()
                return v_id, v_name, "development"
        except:
            pass
            
    # Fallback to directory name parsing
    # E.g. "CON-001-Ace-Construction" or "003-Logistics-Dispatch-Service"
    parts = dir_name.split("-")
    if parts[0].upper() in SECTOR_MAP:
        sector_prefix = SECTOR_MAP[parts[0].upper()]
        try:
            index = int(parts[1])
            v_id = f"{sector_prefix}-{index:03d}"
            v_name = " ".join(parts[2:])
        except ValueError:
            v_id = f"{sector_prefix}-TBD"
            v_name = " ".join(parts[1:])
    elif re.match(r"^\d+$", parts[0]):
        # E.g. "003-Logistics-Dispatch-Service"
        try:
            index = int(parts[0])
            # Determine sector based on suffix/name search
            lower_name = dir_name.lower()
            sector_prefix = "LOG"
            if "construct" in lower_name:
                sector_prefix = "CON"
            elif "commerce" in lower_name or "shop" in lower_name or "store" in lower_name:
                sector_prefix = "ECO"
            elif "finance" in lower_name or "bank" in lower_name or "portfolio" in lower_name:
                sector_prefix = "FIN"
            elif "tech" in lower_name or "editor" in lower_name:
                sector_prefix = "TEC"
            elif "estate" in lower_name or "rent" in lower_name:
                sector_prefix = "REA"
                
            v_id = f"{sector_prefix}-{index:03d}"
            v_name = " ".join(parts[1:])
        except ValueError:
            pass
            
    # Clean up name
    v_name = v_name.replace("-", " ").title()
    return v_id, v_name, "development"

def get_sector_from_id(v_id):
    if "-" in v_id:
        prefix = v_id.split("-")[0].upper()
        return SECTOR_MAP.get(prefix, None)
    return None

def align_venture(dir_name, dir_path, dry_run=True, force=False):
    v_id, v_name, v_status = parse_venture_meta(dir_name, dir_path)
    sector_prefix = get_sector_from_id(v_id)
    
    if not sector_prefix:
        return False
        
    print(f"⚙️ Aligning {v_id} | {v_name} under sector {sector_prefix}...")
    
    # 1. Read master templates from 04-OPERATIONS
    master_cap = os.path.join(OPERATIONS_DIR, f"{sector_prefix}-CAPABILITY-STATEMENT.md")
    master_sales = os.path.join(OPERATIONS_DIR, f"{sector_prefix}-SALES-SCRIPTS.md")
    master_tracker = os.path.join(OPERATIONS_DIR, f"{sector_prefix}-FORMATION-CREDENTIAL-TRACKER.md")
    master_agent = os.path.join(OPERATIONS_DIR, "AGENT-COMMUNICATION-PROTOCOLS.md")
    
    if not os.path.exists(master_cap) or not os.path.exists(master_sales):
        # Fallback to CON templates if sector files are missing
        print(f"   ⚠️ Master templates missing for {sector_prefix}. Skipping.")
        return False
        
    with open(master_cap, "r", encoding="utf-8") as f:
        cap_content = f.read()
    with open(master_sales, "r", encoding="utf-8") as f:
        sales_content = f.read()
    with open(master_tracker, "r", encoding="utf-8") as f:
        tracker_content = f.read()
    with open(master_agent, "r", encoding="utf-8") as f:
        agent_content = f.read()
        
    # Replace placeholders
    def replace_placeholders(text):
        text = text.replace("[Venture Name]", v_name)
        text = text.replace("[Venture ID]", v_id)
        text = text.replace("[Status]", v_status)
        return text
        
    # Generate execution metadata headers
    from datetime import datetime
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Map raw agent names to their unified ID prefixes
    agent_id_map = {
        "CEO Agent": "AG-CEO",
        "Operations Agent": "AG-CAO",
        "Finance Agent": "AG-CFO",
        "Developer Agent": "AG-CTO"
    }
    
    # Determine layout skeleton
    is_new_skeleton = os.path.exists(os.path.join(dir_path, "00_IDENTITY"))

    # Determine base wikilink names based on skeleton structure
    if is_new_skeleton:
        links_map = {
            "cap": ["sales_scripts", "formation_credential_tracker", "departments_and_ecosystem", "VENTURE-MASTER"],
            "sales": ["capability_statement", "formation_credential_tracker", "agent_communication", "LOOP-FRAMEWORK"],
            "track": ["capability_statement", "departments_and_ecosystem", "HOLDINGS-PLAYBOOK"],
            "agent": ["departments_and_ecosystem", "capability_statement", "AGENT-COMMUNICATION-PROTOCOLS"],
            "eco": ["agent_communication", "formation_credential_tracker", "SECTOR-REGISTRY"]
        }
    else:
        links_map = {
            "cap": ["SALES-SCRIPTS", "FORMATION-CREDENTIAL-TRACKER", "DEPARTMENTS-AND-ECOSYSTEM", "VENTURE-MASTER"],
            "sales": ["CAPABILITY-STATEMENT", "FORMATION-CREDENTIAL-TRACKER", "AGENT-COMMUNICATION", "LOOP-FRAMEWORK"],
            "track": ["CAPABILITY-STATEMENT", "DEPARTMENTS-AND-ECOSYSTEM", "HOLDINGS-PLAYBOOK"],
            "agent": ["DEPARTMENTS-AND-ECOSYSTEM", "CAPABILITY-STATEMENT", "AGENT-COMMUNICATION-PROTOCOLS"],
            "eco": ["AGENT-COMMUNICATION", "FORMATION-CREDENTIAL-TRACKER", "SECTOR-REGISTRY"]
        }

    def get_header(agent, dept, schedule, wikilinks):
        # Format links to be venture-prefixed when referencing other venture docs
        formatted_links = []
        for link in wikilinks:
            if link in ["VENTURE-MASTER", "LOOP-FRAMEWORK", "HOLDINGS-PLAYBOOK", "AGENT-COMMUNICATION-PROTOCOLS", "SECTOR-REGISTRY"]:
                formatted_links.append(f"  - [[{link}]]")
            else:
                formatted_links.append(f"  - [[{v_id}-{link}]]")
        links_str = "\n".join(formatted_links)
        
        agent_id = agent_id_map.get(agent, agent)
        return f"""---
execution_metadata:
  venture_id: "{v_id}"
  agent_completed: "{agent_id}"
  department: "{dept}"
  node: "HW-AIR-01"
  database_link: "DB-POSTGRES:PT-5433"
references:
{links_str}
---

"""

    cap_content = get_header("CEO Agent", "Sales & Billing", "on-demand", links_map["cap"]) + replace_placeholders(cap_content)
    sales_content = get_header("Operations Agent", "Sales & Billing", "on-demand", links_map["sales"]) + replace_placeholders(sales_content)
    tracker_content = get_header("Finance Agent", "Operations & Logistics", "weekly", links_map["track"]) + replace_placeholders(tracker_content)
    agent_content = get_header("Developer Agent", "Operations & Logistics", "on-demand", links_map["agent"]) + replace_placeholders(agent_content)
    
    # Build venture specific AGENT-COMMUNICATION.md
    agent_flow_content = f"""# Agent Workforces & Communication — {v_name}

Venture ID: {v_id}
Sector: {sector_prefix}

{agent_content}
"""

    # Build venture specific DEPARTMENTS-AND-ECOSYSTEM.md
    ecosystem_content = get_header("CEO Agent", "Operations & Logistics", "on-demand", links_map["eco"]) + f"""# Departments & System Ecosystem — {v_name}

This document outlines the department boundary configurations and integration points to the central holding ecosystem.

---

## 1. THE 4 CORE DEPARTMENTS

### Department 1: Operations & Logistics
*   **Responsible Agent:** Operations Agent / CAO
*   **System Boundaries:** Coordinates the core execution loops (e.g. dispatch tracking, storefront catalog checks).

### Department 2: Marketing & Growth
*   **Responsible Agent:** Operations Agent (CRM automations) / Marketing Agent
*   **System Boundaries:** Runs landing page intakes, email lists, and conversion funnel scans.

### Department 3: Sales & Billing
*   **Responsible Agent:** Finance Agent / CFO
*   **System Boundaries:** Integrates Stripe billing nodes, manages client database pipelines, and reconciles invoicing ledgers.

### Department 4: HR & Onboarding
*   **Responsible Agent:** Operations Agent
*   **System Boundaries:** Subcontractor background check logs and internal workforce onboarding.

---

## 2. CENTRAL OS ECOSYSTEM INTEGRATION

Every active venture is interconnected with the centralized control plane:
- **Shared Memory (Qdrant Vector DB)**: Syncs planning notes and repository symbol graphs.
- **Ontology (Neo4j Graph)**: Joins `(Venture: {v_id})` to implementing code repositories.
- **State Database (PostgreSQL)**: Reconciles transactional customer objects.
- **Portals (VEX site)**: Automatically publishes metadata to the public portfolio directory.
"""

    # Determine layout skeleton
    is_new_skeleton = os.path.exists(os.path.join(dir_path, "00_IDENTITY"))
    
    targets = {}
    if is_new_skeleton:
        targets = {
            "capability": os.path.join(dir_path, "00_IDENTITY/capability_statement.md"),
            "sales": os.path.join(dir_path, "05_SALES/sales_scripts.md"),
            "tracker": os.path.join(dir_path, "06_FINANCE/formation_credential_tracker.md"),
            "agent": os.path.join(dir_path, "09_AI_AGENTS/agent_communication.md"),
            "ecosystem": os.path.join(dir_path, "07_OPERATIONS/departments_and_ecosystem.md")
        }
    else:
        # Old skeleton - write inside docs/
        docs_folder = os.path.join(dir_path, "docs")
        if not dry_run:
            os.makedirs(docs_folder, exist_ok=True)
        targets = {
            "capability": os.path.join(docs_folder, "CAPABILITY-STATEMENT.md"),
            "sales": os.path.join(docs_folder, "SALES-SCRIPTS.md"),
            "tracker": os.path.join(docs_folder, "FORMATION-CREDENTIAL-TRACKER.md"),
            "agent": os.path.join(docs_folder, "AGENT-COMMUNICATION.md"),
            "ecosystem": os.path.join(docs_folder, "DEPARTMENTS-AND-ECOSYSTEM.md")
        }
        
    # Write files if not dry run + protect customized files
    for key, target_path in targets.items():
        content_map = {
            "capability": cap_content,
            "sales": sales_content,
            "tracker": tracker_content,
            "agent": agent_flow_content,
            "ecosystem": ecosystem_content
        }
        content = content_map[key]
        
        # Check if file exists and has customized data
        should_write = True
        if os.path.exists(target_path) and not force:
            with open(target_path, "r", encoding="utf-8") as f:
                existing_text = f.read()
                # If the file does not have placeholders ("TBD" or "[Venture") and contains custom names, protect it
                if "TBD" not in existing_text and "[Venture" not in existing_text and len(existing_text) > 100:
                    print(f"   🛡️ Protected custom file: {os.path.basename(target_path)}")
                    should_write = False
                    
        if should_write:
            if dry_run:
                print(f"   [DRY RUN] Would write to {os.path.relpath(target_path, DOCS_DIR)}")
            else:
                try:
                    # Make parent dirs if needed
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    with open(target_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"   ✅ Wrote: {os.path.relpath(target_path, DOCS_DIR)}")
                except Exception as e:
                    print(f"   ❌ Failed to write {target_path}: {e}")
                    
    return True

def main():
    parser = argparse.ArgumentParser(description="Portfolio Sales Engines and Agent Alignment")
    parser.add_argument("--execute", action="store_true", help="Commit changes (runs dry-run by default)")
    parser.add_argument("--force", action="store_true", help="Overwrite protected custom files")
    args = parser.parse_args()
    
    dry_run = not args.execute
    if dry_run:
        print("🔍 DRY RUN MODE (use --execute to apply changes)\n")
        
    aligned_count = 0
    
    # Process Active Ventures
    if os.path.exists(ACTIVE_VENTURES_DIR):
        print(f"📂 Processing active ventures in {ACTIVE_VENTURES_DIR}...")
        for item in os.listdir(ACTIVE_VENTURES_DIR):
            item_path = os.path.join(ACTIVE_VENTURES_DIR, item)
            if os.path.isdir(item_path) and not item.startswith("."):
                if align_venture(item, item_path, dry_run, args.force):
                    aligned_count += 1
                    
    # Process Proposed Ventures
    if os.path.exists(PROPOSED_VENTURES_DIR):
        print(f"\n📂 Processing proposed ventures in {PROPOSED_VENTURES_DIR}...")
        for item in os.listdir(PROPOSED_VENTURES_DIR):
            item_path = os.path.join(PROPOSED_VENTURES_DIR, item)
            if os.path.isdir(item_path) and not item.startswith("."):
                if align_venture(item, item_path, dry_run, args.force):
                    aligned_count += 1

    print(f"\n🎉 Alignment complete. Processed {aligned_count} ventures.")

if __name__ == "__main__":
    main()
