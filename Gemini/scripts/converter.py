#!/usr/bin/env python3
import os
import sys
import re
import argparse
from concurrent.futures import ThreadPoolExecutor

# Simple YAML parser since pyyaml might not be installed
def parse_simple_yaml(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    result = {}
    current_top_key = None
    current_sec_key = None
    current_third_key = None
    current_item = None
    
    def clean_val(v):
        v = v.strip().strip('"').strip("'")
        if v.lower() == 'true': return True
        if v.lower() == 'false': return False
        if v.isdigit(): return int(v)
        return v

    for idx, line in enumerate(lines):
        stripped = line.rstrip()
        if not stripped.strip() or stripped.strip().startswith('#'):
            continue
            
        indent = len(stripped) - len(stripped.lstrip())
        stripped = stripped.strip()
        
        if indent == 0:
            current_top_key = stripped.split(':', 1)[0].strip().strip('"').strip("'")
            is_list = False
            for next_line in lines[idx + 1:]:
                next_stripped = next_line.strip()
                if not next_stripped or next_stripped.startswith('#'):
                    continue
                next_indent = len(next_line) - len(next_line.lstrip())
                if next_indent > 0:
                    if next_stripped.startswith('-'):
                        is_list = True
                    break
                else:
                    break
            if is_list:
                result[current_top_key] = []
            else:
                result[current_top_key] = {}
            current_sec_key = None
            current_third_key = None
            current_item = None
            
        elif indent == 2:
            if stripped.startswith('-'):
                val = stripped[1:].strip()
                if ':' in val:
                    k, v = val.split(':', 1)
                    k = k.strip().strip('"').strip("'")
                    v = clean_val(v)
                    current_item = {k: v}
                    result[current_top_key].append(current_item)
                else:
                    result[current_top_key].append(clean_val(val))
            else:
                if ':' in stripped:
                    k, v = stripped.split(':', 1)
                    k = k.strip().strip('"').strip("'")
                    v = v.strip()
                    current_sec_key = k
                    if v == '':
                        is_list = False
                        for next_line in lines[idx + 1:]:
                            next_stripped = next_line.strip()
                            if not next_stripped or next_stripped.startswith('#'):
                                continue
                            next_indent = len(next_line) - len(next_line.lstrip())
                            if next_indent > 2:
                                if next_stripped.startswith('-'):
                                    is_list = True
                                break
                            else:
                                break
                        if is_list:
                            result[current_top_key][k] = []
                        else:
                            result[current_top_key][k] = {}
                    else:
                        result[current_top_key][k] = clean_val(v)
                        
        elif indent == 4:
            if stripped.startswith('-'):
                val = stripped[1:].strip()
                val = clean_val(val)
                if not isinstance(result[current_top_key][current_sec_key], list):
                    result[current_top_key][current_sec_key] = []
                result[current_top_key][current_sec_key].append(val)
            else:
                if ':' in stripped:
                    k, v = stripped.split(':', 1)
                    k = k.strip().strip('"').strip("'")
                    v = v.strip()
                    
                    if current_item is not None:
                        current_item[k] = clean_val(v)
                    else:
                        current_third_key = k
                        if v == '':
                            is_list = False
                            for next_line in lines[idx + 1:]:
                                next_stripped = next_line.strip()
                                if not next_stripped or next_stripped.startswith('#'):
                                    continue
                                next_indent = len(next_line) - len(next_line.lstrip())
                                if next_indent > 4:
                                    if next_stripped.startswith('-'):
                                        is_list = True
                                    break
                                else:
                                    break
                            if is_list:
                                result[current_top_key][current_sec_key][k] = []
                            else:
                                result[current_top_key][current_sec_key][k] = {}
                        else:
                            result[current_top_key][current_sec_key][k] = clean_val(v)
                            
        elif indent == 6:
            if stripped.startswith('-'):
                val = clean_val(stripped[1:].strip())
                target = result[current_top_key][current_sec_key][current_third_key]
                if not isinstance(target, list):
                    result[current_top_key][current_sec_key][current_third_key] = []
                    target = result[current_top_key][current_sec_key][current_third_key]
                target.append(val)
                
    return result



# Generate the instructions markdown text
def build_rules_markdown(models_data, agents_data, councils_data, routing_data, catalog_data):
    md = []
    md.append("# AI-BOSS-OS Workspace Instructions & Capabilities Registry\n")
    md.append("This file defines the system architecture, model policies, and available agent blueprints for this workspace.\n")
    
    md.append("## 1. System Map & Core Ports")
    md.append("- **OmniRoute Gateway**: `http://localhost:20128/v1`")
    md.append("- **Ollama**: Port `11434` (models mapped from external storage)")
    md.append("- **Neo4j Graph Database**: Ports `7474` (HTTP) / `7687` (Bolt)")
    md.append("- **Qdrant Vector DB**: Port `6333` (Docker container: `civos_qdrant`)")
    md.append("- **Langfuse Tracing Dashboard**: Port `3003` (Docker container: `civos_langfuse`)\n")
    
    md.append("## 2. Model Routing Table (`auto/*`)")
    md.append("| Logical Tag | Primary Target | Fallback Target | Description |")
    md.append("| :--- | :--- | :--- | :--- |")
    
    policies = routing_data.get('routing_policies', {})
    for tag, targets in policies.items():
        if isinstance(targets, list):
            primary = targets[0] if len(targets) > 0 else 'N/A'
            fallback = targets[1] if len(targets) > 1 else 'Local Fallback'
        else:
            primary = targets
            fallback = 'N/A'
        md.append(f"| `{tag}` | {primary} | {fallback} | Centralized route tag |")
    md.append("")
    
    md.append("## 3. Registered Agents")
    agents = agents_data.get('agent', {})
    for name, config in agents.items():
        tools_list = ", ".join(config.get('tools', [])) if isinstance(config.get('tools'), list) else config.get('tools', 'None')
        md.append(f"### {name}")
        md.append(f"- **Default Routing Model**: `{config.get('model', 'auto')}`")
        md.append(f"- **Tools**: `{tools_list}`")
        md.append(f"- **Escalation Target**: `{config.get('escalation', 'none')}`\n")
        
    md.append("## 4. LLM Councils (Governance)")
    councils = councils_data.get('councils', {})
    for name, config in councils.items():
        members = ", ".join(config.get('members', [])) if isinstance(config.get('members'), list) else config.get('members', 'None')
        md.append(f"### {name.capitalize()} Council")
        md.append(f"- **Members**: {members}")
        md.append(f"- **Chairman**: `{config.get('chairman', 'claude')}`")
        md.append(f"- **Consensus Threshold**: `{config.get('threshold', '80%')}`\n")
        
    md.append("## 5. Agent Blueprints Catalog")
    
    # Custom Agents
    custom_agents = catalog_data.get('agents', [])
    if custom_agents:
        md.append("### Custom Enterprise Agents")
        md.append("| Agent Name | Industry | Role / Description | Source |")
        md.append("| :--- | :--- | :--- | :--- |")
        for ag in custom_agents:
            md.append(f"| {ag.get('name')} | {ag.get('industry')} | {ag.get('description')} | {ag.get('repo')} |")
        md.append("")
        
    # CrewAI
    crew_use_cases = catalog_data.get('crewai_use_cases', [])
    if crew_use_cases:
        md.append("### CrewAI Framework Blueprints")
        md.append("| Use Case | Industry | Description | Source |")
        md.append("| :--- | :--- | :--- | :--- |")
        for uc in crew_use_cases:
            md.append(f"| {uc.get('name')} | {uc.get('industry')} | {uc.get('description')} | {uc.get('repo')} |")
        md.append("")
        
    # AutoGen
    autogen_use_cases = catalog_data.get('autogen_use_cases', [])
    if autogen_use_cases:
        md.append("### AutoGen Multi-Agent Collaboration Blueprints")
        md.append("| Use Case | Industry | Description | Source |")
        md.append("| :--- | :--- | :--- | :--- |")
        for uc in autogen_use_cases:
            md.append(f"| {uc.get('name')} | {uc.get('industry')} | {uc.get('description')} | {uc.get('link')} |")
        md.append("")

    # Agno
    agno_use_cases = catalog_data.get('agno_use_cases', [])
    if agno_use_cases:
        md.append("### Agno Lightweight Blueprints")
        md.append("| Agent Name | Industry | Description | Language |")
        md.append("| :--- | :--- | :--- | :--- |")
        for uc in agno_use_cases:
            md.append(f"| {uc.get('name')} | {uc.get('industry')} | {uc.get('description')} | {uc.get('code')} |")
        md.append("")

    # LangGraph
    langgraph_use_cases = catalog_data.get('langgraph_use_cases', [])
    if langgraph_use_cases:
        md.append("### LangGraph State-Machine Workflows")
        md.append("| Use Case | Industry | Description | Language |")
        md.append("| :--- | :--- | :--- | :--- |")
        for uc in langgraph_use_cases:
            md.append(f"| {uc.get('name')} | {uc.get('industry')} | {uc.get('description')} | {uc.get('code')} |")
        md.append("")
        
    return "\n".join(md)

def convert_tool(tool, md_content, dist_dir):
    os.makedirs(dist_dir, exist_ok=True)
    
    # Custom headers/wrapper formatting depending on tool requirements
    if tool == 'cursor':
        target_file = os.path.join(dist_dir, 'cursorrules')
        content = md_content
    elif tool == 'aider':
        target_file = os.path.join(dist_dir, 'CONVENTIONS.md')
        content = md_content
    elif tool == 'windsurf':
        target_file = os.path.join(dist_dir, 'windsurfrules')
        content = md_content
    elif tool == 'copilot':
        target_file = os.path.join(dist_dir, 'copilot-instructions.md')
        content = md_content
    elif tool == 'antigravity':
        target_file = os.path.join(dist_dir, 'GEMINI.md')
        content = md_content
    else:
        # Standard format
        target_file = os.path.join(dist_dir, f'{tool}-instructions.md')
        content = md_content
        
    with open(target_file, 'w') as f:
        f.write(content)
        
    print(f"Generated integration file for tool: {tool} -> {target_file}")
    return tool, target_file

def main():
    parser = argparse.ArgumentParser(description="Compile rules files for multi-agent frameworks.")
    parser.add_argument('--parallel', action='store_true', help='Convert tools in parallel')
    parser.add_argument('--jobs', type=int, default=4, help='Number of parallel jobs')
    parser.add_argument('--tool', type=str, default='all', help='Specify one tool to convert (or all)')
    args = parser.parse_args()
    
    workspace = '/Users/acebless/Documents/Gemini'
    core_dir = os.path.join(workspace, 'AI-BOSS-OS/AI-CORE')
    dist_dir = os.path.join(workspace, 'scripts/dist')
    
    # Read registries
    models = parse_simple_yaml(os.path.join(core_dir, 'model-registry/model_registry.yaml'))
    agents = parse_simple_yaml(os.path.join(core_dir, 'agent-registry/agent_registry.yaml'))
    councils = parse_simple_yaml(os.path.join(core_dir, 'council-registry/council_registry.yaml'))
    routing = parse_simple_yaml(os.path.join(core_dir, 'policies/routing_policies.yaml'))
    catalog = parse_simple_yaml(os.path.join(core_dir, 'agent-registry/agent_catalog.yaml'))
    
    md_content = build_rules_markdown(models, agents, councils, routing, catalog)
    
    tools = [
        'claudecode', 'copilot', 'antigravity', 'gemini-cli', 'opencode',
        'openclaw', 'cursor', 'aider', 'windsurf', 'qwen-code',
        'kimi-code', 'codex', 'osaurus', 'hermes'
    ]
    
    if args.tool != 'all':
        if args.tool not in tools:
            print(f"Error: Unknown tool: {args.tool}")
            sys.exit(1)
        tools = [args.tool]
        
    if args.parallel and len(tools) > 1:
        with ThreadPoolExecutor(max_workers=args.jobs) as executor:
            futures = [executor.submit(convert_tool, t, md_content, dist_dir) for t in tools]
            for fut in futures:
                fut.result()
    else:
        for t in tools:
            convert_tool(t, md_content, dist_dir)

if __name__ == '__main__':
    main()
