#!/usr/bin/env python3
"""
run_agent_team.py
Autonomous task executor that maps corporate agent profiles (AG-CEO, AG-CTO, etc.)
and sector teams to their registered skills and tools. Runs local executions with 0 tokens.
"""
import os
import sys
import yaml
import json
import subprocess
from datetime import datetime

DOCS = "/Users/acebless/Documents"
WORLDWIDEBRO_OS = os.path.join(DOCS, "WORLDWIDEBRO-OS")
REGISTRIES = os.path.join(WORLDWIDEBRO_OS, "08-DATA/registries")
AGENT_MD = os.path.join(WORLDWIDEBRO_OS, "05-AGENTS/agent.md")
TOOLS_REGISTRY = os.path.join(REGISTRIES, "agent_tools_registry.yaml")

class AgentTeamOrchestrator:
    def __init__(self, venture_dir):
        self.venture_dir = os.path.normpath(venture_dir)
        self.venture_name = os.path.basename(self.venture_dir)
        self.agent_cfg_path = os.path.join(self.venture_dir, "09_AI_AGENTS/agent_registry.yaml")
        
    def load_yaml(self, path):
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def log_execution(self, agent_id, tool_name, status, log_msg):
        log_dir = os.path.join(self.venture_dir, "10_DATA")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "agent_execution_logs.jsonl")
        
        entry = {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "agent_id": agent_id,
            "tool": tool_name,
            "status": status,
            "log": log_msg
        }
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"📝 [{agent_id}] Logged execution: {tool_name} ({status})")

    def run_task(self, agent_id, task_type):
        print(f"\n⚡ [{agent_id}] Initiating local task: {task_type} for venture {self.venture_name}...")
        
        # Load tools registry to find the mapped tool for this agent/task
        tools_cfg = self.load_yaml(TOOLS_REGISTRY)
        if not tools_cfg:
            print("Error: Could not load agent_tools_registry.yaml")
            return False
            
        # Map task types to local CLI executions (0 tokens)
        if task_type == "compile-outreach":
            # Map to compile_outreach.py
            script_path = "/Users/acebless/Documents/WORLDWIDEBRO-OS/04-OPERATIONS/compile_outreach.py"
            try:
                result = subprocess.run(
                    ["python3", script_path],
                    capture_output=True,
                    text=True,
                    check=True
                )
                self.log_execution(agent_id, "compile_outreach.py", "SUCCESS", "Outreach templates compiled locally with 0 tokens.")
                return True
            except Exception as e:
                self.log_execution(agent_id, "compile_outreach.py", "FAILED", str(e))
                return False
                
        elif task_type == "db-dedupe" and agent_id == "AG-CAO":
            # Map to dedupe_twenty_companies.py
            script_path = "/Users/acebless/Documents/dedupe_twenty_companies.py"
            try:
                # Run dry run first to see status
                result = subprocess.run(
                    ["python3", script_path],
                    capture_output=True,
                    text=True,
                    check=True
                )
                self.log_execution(agent_id, "dedupe_twenty_companies.py", "SUCCESS", f"CRM Deduplication ran. Output: {result.stdout[:200]}")
                return True
            except Exception as e:
                self.log_execution(agent_id, "dedupe_twenty_companies.py", "FAILED", str(e))
                return False
                
        elif task_type == "repo-scan" and agent_id == "AG-CTO":
            # Map to scan_repositories.py
            script_path = "/Users/acebless/Documents/scan_repositories.py"
            if os.path.exists(script_path):
                try:
                    result = subprocess.run(
                        ["python3", script_path],
                        capture_output=True,
                        text=True,
                        check=True
                    )
                    self.log_execution(agent_id, "scan_repositories.py", "SUCCESS", "Repository scan and capability mapping complete.")
                    return True
                except Exception as e:
                    self.log_execution(agent_id, "scan_repositories.py", "FAILED", str(e))
                    return False
            else:
                self.log_execution(agent_id, "scan_repositories.py", "FAILED", "scan_repositories.py script not found.")
                return False
        else:
            self.log_execution(agent_id, "unknown_tool", "FAILED", f"No local zero-token route configured for task: {task_type}")
            return False

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 run_agent_team.py <VenturePath> <AgentID> <TaskType>")
        print("Example: python3 run_agent_team.py /Users/acebless/Documents/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/003-Logistics-Dispatch-Service AG-CEO compile-outreach")
        sys.exit(1)
        
    v_path = sys.argv[1]
    agent_id = sys.argv[2]
    task_type = sys.argv[3]
    
    orchestrator = AgentTeamOrchestrator(v_path)
    orchestrator.run_task(agent_id, task_type)

if __name__ == "__main__":
    main()
