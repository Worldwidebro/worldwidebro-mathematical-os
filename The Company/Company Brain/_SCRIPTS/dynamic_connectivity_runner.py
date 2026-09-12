#!/usr/bin/env python3
import json
import os
import datetime
import subprocess
import socket

REGISTRY_PATH = '../_REGISTRIES/CONNECTIVITY/CONNECTIVITY-TESTS.json'
REPORT_PATH = '../_TESTS/CONNECTIVITY/STRICT_REALITY_AUDIT.md'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Hardware Nodes (Tailscale Mesh)
NODES = {
    "Localhost": "127.0.0.1",
    "Mac Studio": "100.87.214.70",
    "MacBook Air": "100.121.17.63"
}

def ping_http(url):
    try:
        result = subprocess.run(["curl", "-sI", url], capture_output=True, text=True, timeout=5)
        return "200 OK" in result.stdout
    except Exception:
        return False

def check_tcp_across_nodes(port):
    for node_name, ip in NODES.items():
        try:
            with socket.create_connection((ip, port), timeout=1):
                return True, f"Active on {node_name} ({ip}:{port})"
        except Exception:
            continue
    return False, f"Offline across mesh (Port {port})"

def execute_physical_test(test_id, description):
    """
    STRICT REALITY CHECKS ONLY.
    No file existence checks. No "static" mapping. 
    If it's not a live socket, API, or executing code, it fails.
    """
    desc_lower = description.lower()
    
    # 1. Venture Deployment (Production URLs)
    if "deployment" in desc_lower or "release" in desc_lower or "production" in desc_lower or test_id in ["CONN-489", "CONN-490"]:
        sites = [
            "https://ops-staff-001-staffing.vercel.app/",
            "https://healthroute-courier.vercel.app/",
            "https://callcenter-eosin.vercel.app/",
            "https://con-001-ace-construction.vercel.app/",
            "https://re-001-worldwidebro-holdings.vercel.app/",
            "https://lt-011-dispatch-software.vercel.app/"
        ]
        up_count = sum(1 for site in sites if ping_http(site))
        if up_count > 0:
            return True, True, f"HTTP 200 OK from {up_count}/6 Production Ventures"
        return True, False, "Production deployments unreachable"

    # 2. VEX Dashboard / Revenue Engine
    if "revenue" in desc_lower or "finance" in desc_lower or "dashboard" in desc_lower or test_id in ["CONN-375", "CONN-406"]:
        if ping_http("https://vex-hero-site-sigma.vercel.app/"):
            return True, True, "HTTP 200 OK from VEX Command Center"
        return True, False, "VEX Revenue Dashboard unreachable"

    # 3. Neo4j Knowledge Graph (Port 7474 / 7687)
    if "connects to" in desc_lower or "graph" in desc_lower or "node" in desc_lower:
        up, msg = check_tcp_across_nodes(7474)
        if up:
            return True, True, f"Neo4j: {msg}"
        return True, False, f"Neo4j: {msg}"

    # 4. OmniRoute / Agent Gateway (Port 20128)
    if "agent" in desc_lower or "workflow" in desc_lower or "mcp" in desc_lower:
        up, msg = check_tcp_across_nodes(20128)
        if up:
            return True, True, f"OmniRoute: {msg}"
        return True, False, f"OmniRoute: {msg}"
        
    # 5. Qdrant / Vector Memory (Port 6333)
    if "memory" in desc_lower or "search" in desc_lower or "semantic" in desc_lower:
        up, msg = check_tcp_across_nodes(6333)
        if up:
            return True, True, f"Qdrant: {msg}"
        return True, False, f"Qdrant: {msg}"
        
    # 6. LiteLLM / Model Runtime (Port 4000)
    if "model" in desc_lower or "ai" in desc_lower or "inference" in desc_lower:
        up, msg = check_tcp_across_nodes(4000)
        if up:
            return True, True, f"LiteLLM: {msg}"
        return True, False, f"LiteLLM: {msg}"

    # If there is no specific hardware/network test mapped, it inherently fails in reality.
    return False, False, "No physical integration test wired yet"

def run_tests():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    registry_file = os.path.join(script_dir, REGISTRY_PATH)
    report_file = os.path.join(script_dir, REPORT_PATH)

    with open(registry_file, 'r') as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for test in tests:
        has_test, success, msg = execute_physical_test(test["TEST_ID"], test["DESCRIPTION"])
        
        if has_test and success:
            test["STATUS"] = "PASS"
            test["ACTUAL_BEHAVIOR"] = f"[PHYSICAL] {msg}"
            passed += 1
        elif has_test and not success:
            test["STATUS"] = "FAIL"
            test["ACTUAL_BEHAVIOR"] = f"[OFFLINE] {msg}"
            failed += 1
        else:
            test["STATUS"] = "FAIL"
            test["ACTUAL_BEHAVIOR"] = "[UNWIRED] " + msg
            failed += 1
        
        test["LAST_RUN"] = datetime.datetime.now().isoformat()

    with open(registry_file, 'w') as f:
        json.dump(tests, f, indent=2)

    total = len(tests)

    markdown_content = f"""# Strict Reality Connectivity Audit

**Last Run:** {datetime.datetime.now().isoformat()}

**Rule:** NO HALLUCINATIONS. NO MOCKS. NO STATIC FILE CHECKS.
If a connection cannot be proven via a live API, active Database, or physical network socket, it **FAILS**.

## Audit Summary

- **Total Tests:** {total}
- **Passing (Physical):** {passed}
- **Failing (Offline/Unwired):** {failed}

> **{passed}/{total} reality tests passing.**

## Test Matrix

| Test ID | Description | Status | Reality Evidence |
|---|---|---|---|
"""
    for t in tests:
        status_icon = "✅" if t["STATUS"] == "PASS" else "❌"
        markdown_content += f"| {t['TEST_ID']} | {t['DESCRIPTION']} | {status_icon} {t['STATUS']} | {t.get('ACTUAL_BEHAVIOR', '')} |\n"

    with open(report_file, 'w') as f:
        f.write(markdown_content)
    
    print(f"Brutal Reality Audit Complete: {passed}/{total} passing. Report saved.")

if __name__ == "__main__":
    run_tests()
