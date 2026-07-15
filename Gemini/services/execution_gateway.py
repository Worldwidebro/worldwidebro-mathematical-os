import sys
import os
import subprocess
import socket
import json

OBSIDIAN_SYNC_SCRIPT = "/Users/acebless/Documents/obsidian_graph_sync.py"
GRAPHIFY_SYNC_SCRIPT = "/Users/acebless/Documents/inject_graphify_payload.py"
DOCS_DIR = "/Users/acebless/Documents"

def run_obsidian_sync():
    """Runs the obsidian_graph_sync.py script and returns the stdout logs."""
    if not os.path.exists(OBSIDIAN_SYNC_SCRIPT):
        return {"status": "error", "message": f"Obsidian sync script not found at {OBSIDIAN_SYNC_SCRIPT}"}
    
    try:
        # Run using python3
        res = subprocess.run(
            ["python3", OBSIDIAN_SYNC_SCRIPT],
            capture_output=True,
            text=True,
            cwd=DOCS_DIR,
            env=os.environ.copy()
        )
        return {
            "status": "success" if res.returncode == 0 else "error",
            "stdout": res.stdout,
            "stderr": res.stderr,
            "returncode": res.returncode
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def run_graphify_injection():
    """Runs the inject_graphify_payload.py script and returns stdout logs."""
    if not os.path.exists(GRAPHIFY_SYNC_SCRIPT):
        return {"status": "error", "message": f"Graphify injection script not found at {GRAPHIFY_SYNC_SCRIPT}"}
    
    try:
        res = subprocess.run(
            ["python3", GRAPHIFY_SYNC_SCRIPT],
            capture_output=True,
            text=True,
            cwd=DOCS_DIR,
            env=os.environ.copy()
        )
        return {
            "status": "success" if res.returncode == 0 else "error",
            "stdout": res.stdout,
            "stderr": res.stderr,
            "returncode": res.returncode
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def run_pen_tester():
    """Performs a real local socket port scan on common ports to identify active service endpoints."""
    target_host = "127.0.0.1"
    # Probing standard ports for web servers, database, Neo4j, Qdrant, and local services
    ports = {
        8000: "Operations Control Dashboard (server.py)",
        8001: "Model Context Protocol Gateway (mcp_gateway.py)",
        3002: "Twenty Portfolio CRM Server",
        5432: "PostgreSQL Database Server",
        6379: "Redis Cache Server",
        7474: "Neo4j Graph Database Web Console",
        7687: "Neo4j Bolt Connector Protocol",
        6333: "Qdrant Vector Database Server",
        11434: "Ollama Local Model Server API"
    }
    
    results = []
    open_ports_count = 0
    
    for port, name in ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.15) # Quick timeout
        result = s.connect_ex((target_host, port))
        
        status = "CLOSED"
        if result == 0:
            status = "OPEN (Active)"
            open_ports_count += 1
            
        results.append({
            "port": port,
            "name": name,
            "status": status
        })
        s.close()
        
    return {
        "status": "success",
        "open_ports": open_ports_count,
        "results": results
    }

def run_repo_scanner(target_dir=None):
    """Scans the documents directory to list local package dependencies and workspace profiles."""
    scan_path = target_dir or DOCS_DIR
    if not os.path.exists(scan_path):
        return {"status": "error", "message": f"Target path {scan_path} does not exist"}

    found_repos = []
    
    # Simple search for package manifest configurations
    for item in os.listdir(scan_path):
        item_path = os.path.join(scan_path, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            manifests = []
            
            # Check standard manifest files
            package_json = os.path.join(item_path, "package.json")
            requirements_txt = os.path.join(item_path, "requirements.txt")
            gemini_md = os.path.join(item_path, "GEMINI.md")
            
            if os.path.exists(package_json):
                manifests.append("package.json (Node/Vite)")
            if os.path.exists(requirements_txt):
                manifests.append("requirements.txt (Python)")
            if os.path.exists(gemini_md):
                manifests.append("GEMINI.md (Gemini Rules)")
                
            if manifests:
                found_repos.append({
                    "name": item,
                    "path": item_path,
                    "manifests": manifests
                })

    return {
        "status": "success",
        "scanned_path": scan_path,
        "total_projects": len(found_repos),
        "projects": found_repos
    }

def execute_capability(capability_id, args=None):
    """Router routing execution logic based on capability IDs."""
    if args is None:
        args = {}
        
    if capability_id == "obsidian-sync":
        return run_obsidian_sync()
    elif capability_id == "graphify-injection":
        return run_graphify_injection()
    elif capability_id == "pen-tester":
        return run_pen_tester()
    elif capability_id == "repo-scanner":
        target = args.get("target_dir")
        return run_repo_scanner(target)
    else:
        return {
            "status": "error",
            "message": f"Capability '{capability_id}' execution wrapper not mapped."
        }

if __name__ == '__main__':
    # Easy CLI testing
    if len(sys.argv) > 1:
        cap = sys.argv[1]
        print(json.dumps(execute_capability(cap), indent=2))
    else:
        print("Usage: python3 execution_gateway.py <capability_id>")
