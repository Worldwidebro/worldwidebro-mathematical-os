import os
import sys
import json
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# Add current path to import execution_gateway
GEMINI_DIR = "/Users/acebless/Documents/Gemini"
sys.path.append(os.path.join(GEMINI_DIR, "services"))
import execution_gateway

def load_fcc_env():
    env_vars = {}
    fcc_env_path = os.path.expanduser('~/.fcc/.env')
    if os.path.exists(fcc_env_path):
        try:
            with open(fcc_env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line_strip = line.strip()
                    if line_strip and not line_strip.startswith('#') and '=' in line_strip:
                        k, v = line_strip.split('=', 1)
                        env_vars[k.strip()] = v.strip().strip('"').strip("'")
        except Exception as e:
            print(f"Error loading ~/.fcc/.env: {e}")
    return env_vars

# Define the agent tools
@tool
def sync_obsidian_graph() -> str:
    """Trigger the sync pipeline mapping Obsidian notes to Neo4j Supabase graph."""
    res = execution_gateway.run_obsidian_sync()
    return json.dumps(res, indent=2)

@tool
def repository_scanner(target_dir: str = None) -> str:
    """Scrapes dependencies and manifest imports across directories (GitNexus).
    Optionally specify a 'target_dir' directory path to scan. Defaults to the main documents directory.
    """
    res = execution_gateway.run_repo_scanner(target_dir)
    return json.dumps(res, indent=2)

@tool
def run_pen_tester() -> str:
    """Performs a real local socket port scan on common ports to identify active service endpoints (METATRON)."""
    res = execution_gateway.run_pen_tester()
    return json.dumps(res, indent=2)

@tool
def ad_compliance_audit(campaign_id: str) -> str:
    """Audits campaign scripts manifest against regulatory criteria checklist for a given campaign_id."""
    campaign_dir = os.path.join(GEMINI_DIR, "campaigns", campaign_id)
    manifest_path = os.path.join(campaign_dir, "manifest.json")
    rules_path = os.path.join(GEMINI_DIR, "tools/claude-ads/rules.md")

    # Create dummy template files if none exist to allow testing
    if not os.path.exists(manifest_path):
        os.makedirs(campaign_dir, exist_ok=True)
        dummy_manifest = {
            "campaign_id": campaign_id,
            "script": "Our product is guaranteed to cure baldness in 2 hours! Free trials for everyone.",
            "claims": ["baldness cure", "2 hours timeline"]
        }
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(dummy_manifest, f, indent=2)

    if not os.path.exists(rules_path):
        os.makedirs(os.path.dirname(rules_path), exist_ok=True)
        dummy_rules = (
            "# Ad Campaign Regulations\n\n"
            "- Rule 1: No health guarantees or absolute cures.\n"
            "- Rule 2: Claims regarding timelines (e.g. 'X hours') must be backfilled with clinical evidence.\n"
        )
        with open(rules_path, 'w', encoding='utf-8') as f:
            f.write(dummy_rules)

    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        
        with open(rules_path, 'r', encoding='utf-8') as f:
            rules = f.read()

        script = manifest.get("script", "")
        violations = []

        if "cure" in script.lower() or "guarantee" in script.lower():
            violations.append("Violation of Rule 1: Medical claim or guarantee of cure detected in script.")
        if "hour" in script.lower() or "minute" in script.lower():
            violations.append("Violation of Rule 2: Timeline-related claims must possess supporting evidence.")

        status = "fail" if violations else "pass"
        res = {
            "status": status,
            "violations": violations,
            "campaign": campaign_id,
            "script": script
        }
        return json.dumps(res, indent=2)
    except Exception as e:
        return json.dumps({"error": f"Campaign audit runner failed: {str(e)}"})

ALL_TOOLS = [sync_obsidian_graph, repository_scanner, run_pen_tester, ad_compliance_audit]

def run_agent(agent_name: str, prompt: str):
    logs = []
    logs.append(f"🤖 [Initializing Live LangGraph Agent: {agent_name}]...")

    # Load environment variables
    env_vars = load_fcc_env()
    
    # Enable LangSmith tracing if configured
    langsmith_key = env_vars.get("LANGSMITH_API_KEY")
    if langsmith_key:
        logs.append("📡 LangSmith tracing key detected. Initializing automatic tracing...")
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGSMITH_API_KEY"] = langsmith_key
        os.environ["LANGSMITH_PROJECT"] = env_vars.get("LANGSMITH_PROJECT", "Worldwidebro-OS")
    else:
        logs.append("ℹ️ LangSmith tracing key not set. Skipping tracing.")

    # Choose model based on environment
    nim_key = env_vars.get("NVIDIA_NIM_API_KEY")
    if nim_key:
        logs.append("⚡ NVIDIA NIM API key detected. Connecting to meta/llama-3.1-70b-instruct...")
        model = ChatOpenAI(
            model="meta/llama-3.1-70b-instruct",
            openai_api_key=nim_key,
            openai_api_base="https://integrate.api.nvidia.com/v1",
            temperature=0.1
        )
    else:
        logs.append("🔌 Falling back to local Ollama on http://localhost:11434 (model: qwen3:8b)...")
        model = ChatOpenAI(
            model="qwen3:8b",
            openai_api_key="ollama",
            openai_api_base="http://localhost:11434/v1",
            temperature=0.1
        )

    # Load agent details to define system prompt focus
    agents_file = os.path.join(GEMINI_DIR, "registry", "agents.yaml")
    system_prompt = f"You are the {agent_name} of WORLDWIDEBRO-OS.\n"
    if os.path.exists(agents_file):
        try:
            with open(agents_file, 'r', encoding='utf-8') as f:
                content = f.read()
            entries = []
            current = {}
            for line in content.split('\n'):
                line_strip = line.strip()
                if not line_strip:
                    continue
                if line_strip.startswith('-'):
                    if current:
                        entries.append(current)
                        current = {}
                    line_strip = line_strip.lstrip('-').strip()
                if ':' in line_strip:
                    parts = line_strip.split(':', 1)
                    k = parts[0].strip().replace('"', '').replace("'", "")
                    v = parts[1].strip().replace('"', '').replace("'", "")
                    current[k] = v
            if current:
                entries.append(current)

            agent_details = next((a for a in entries if a.get("name", "").lower() == agent_name.lower()), None)
            if agent_details:
                system_prompt += f"Role: {agent_details.get('role', '')}\nFocus: {agent_details.get('focus', '')}\n"
        except Exception as e:
            logs.append(f"⚠️ Warning loading agent description: {e}")

    system_prompt += (
        "\nProvide helpful, structured output to satisfy the user request. "
        "Use your tools when appropriate to fetch real-world data from the system."
    )

    logs.append("🧠 Compiling ReAct agent graph...")
    agent_graph = create_react_agent(model, tools=ALL_TOOLS, state_modifier=system_prompt)

    logs.append("🚀 Executing agentic cognitive loop...")
    final_response = ""
    try:
        inputs = {"messages": [("user", prompt)]}
        seen_messages = set()
        # Run agent stream to extract logs and tool calls
        for event in agent_graph.stream(inputs, stream_mode="values"):
            if "messages" in event:
                for msg in event["messages"]:
                    msg_id = getattr(msg, "id", None) or f"{msg.type}_{msg.content[:20]}"
                    if msg_id in seen_messages:
                        continue
                    seen_messages.add(msg_id)
                    
                    # Check for tool calls in assistant message
                    if msg.type == "ai" and hasattr(msg, "tool_calls") and msg.tool_calls:
                        for tc in msg.tool_calls:
                            logs.append(f"  🔧 [Tool Invocation] calling '{tc['name']}' with arguments: {json.dumps(tc['args'])}")
                    
                    # If it's a tool message
                    elif msg.type == "tool":
                        logs.append(f"  📥 [Tool Return] '{msg.name}' completed execution.")
                    
                    # If it's the final assistant completion
                    elif msg.type == "ai" and not (hasattr(msg, "tool_calls") and msg.tool_calls):
                        final_response = msg.content

        if not final_response:
            # Fallback if stream values didn't end with ai content
            res = agent_graph.invoke(inputs)
            final_response = res["messages"][-1].content

    except Exception as e:
        logs.append(f"❌ Error during execution: {str(e)}")
        final_response = f"An error occurred while running the agent: {str(e)}"

    return {
        "logs": logs,
        "response": final_response
    }
