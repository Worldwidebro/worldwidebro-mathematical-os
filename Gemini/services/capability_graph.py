import os
import re

REGISTRY_DIR = "/Users/acebless/Documents/Gemini/registry"
OUTPUT_DIR = "/Users/acebless/Documents/Gemini/reports"

def parse_yaml_simple(filepath):
    """
    Very simple YAML parser for flat structures, avoiding extra dependencies.
    Matches basic key-value lists and maps.
    """
    if not os.path.exists(filepath):
        return []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into entries starting with -
    entries = []
    current = {}
    
    for line in content.split('\n'):
        line_strip = line.strip()
        if not line_strip:
            continue
        
        # New list item
        if line_strip.startswith('-'):
            if current:
                entries.append(current)
                current = {}
            line_strip = line_strip.lstrip('-').strip()
            
        if ':' in line_strip:
            parts = line_strip.split(':', 1)
            key = parts[0].strip().replace('"', '').replace("'", "")
            val = parts[1].strip().replace('"', '').replace("'", "")
            
            # Basic list values
            if val.startswith('[') and val.endswith(']'):
                val = [item.strip() for item in val[1:-1].split(',')]
            current[key] = val
            
    if current:
        entries.append(current)
        
    return entries

def build_graph():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    repos = parse_yaml_simple(os.path.join(REGISTRY_DIR, "repositories.yaml"))
    caps = parse_yaml_simple(os.path.join(REGISTRY_DIR, "capabilities.yaml"))
    integrations = parse_yaml_simple(os.path.join(REGISTRY_DIR, "integrations.yaml"))
    
    cypher_statements = []
    cypher_statements.append("// WORLDWIDEBRO-OS Capability Graph Initialization")
    cypher_statements.append("MATCH (n) DETACH DELETE n;\n")
    
    # 1. Create Repository nodes
    cypher_statements.append("// 1. Create Repository Nodes")
    for r in repos:
        name = r.get("name", "unknown")
        url = r.get("url", "")
        category = r.get("category", "")
        purpose = r.get("purpose", "")
        status = r.get("status", "planned")
        cypher_statements.append(
            f"CREATE (:Repository {{name: '{name}', url: '{url}', category: '{category}', purpose: '{purpose}', status: '{status}'}});"
        )
    cypher_statements.append("")

    # 2. Create Capability nodes
    cypher_statements.append("// 2. Create Capability Nodes")
    for c in caps:
        cap_id = c.get("id", "unknown")
        name = c.get("name", "unknown")
        category = c.get("category", "")
        desc = c.get("description", "")
        cypher_statements.append(
            f"CREATE (:Capability {{id: '{cap_id}', name: '{name}', category: '{category}', description: '{desc}'}});"
        )
    cypher_statements.append("")

    # 3. Create Agent nodes
    cypher_statements.append("// 3. Create Agent Nodes")
    # Fetch unique agents from integrations list
    agents = set()
    for integration in integrations:
        agent_name = integration.get("used_by_agent")
        if agent_name:
            agents.add(agent_name)
            
    for agent in agents:
        cypher_statements.append(f"CREATE (:Agent {{name: '{agent}'}});")
    cypher_statements.append("")

    # 4. Link relationships
    cypher_statements.append("// 4. Create Graph Relationships")
    for integration in integrations:
        repo = integration.get("repository", "")
        cap = integration.get("provides_capability", "")
        agent = integration.get("used_by_agent", "")
        
        # Link Repository to Capability
        cypher_statements.append(
            f"MATCH (r:Repository {{name: '{repo}'}}), (c:Capability {{id: '{cap}'}}) "
            f"CREATE (r)-[:PROVIDES]->(c);"
        )
        
        # Link Capability to Agent
        if agent:
            cypher_statements.append(
                f"MATCH (c:Capability {{id: '{cap}'}}), (a:Agent {{name: '{agent}'}}) "
                f"CREATE (a)-[:USES]->(c);"
            )
            
    output_path = os.path.join(OUTPUT_DIR, "capability_graph_build.cypher")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(cypher_statements))
        
    print(f"Capability graph compiled. Saved Cypher script to: {output_path}")

if __name__ == '__main__':
    build_graph()
