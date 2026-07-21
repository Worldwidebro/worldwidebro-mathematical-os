#!/usr/bin/env python3
import os
import sys
import json
import subprocess
from typing import Dict, Any, List

# Add parent path to allow importing os_env
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from os_env import OLLAMA_CHAT, CHAT_MODEL
except ImportError:
    OLLAMA_CHAT = "http://100.87.214.70:11434/v1/chat/completions"
    CHAT_MODEL = "qwen3:8b"

CREATE_VENTURE_SCRIPT = "/Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/create_venture.py"

try:
    from knowledge_engine import LLMAdapter
except ImportError:
    from services.knowledge_engine import LLMAdapter

class VentureFactoryEngine:
    def __init__(self):
        self.llm = LLMAdapter()

    def ideate(self, sector: str, gap_description: str, num_ideas=3) -> List[Dict[str, Any]]:
        """Generates venture concepts solving a given sector gap."""
        prompt = (
            f"Given a market gap in the {sector} sector: \"{gap_description}\".\n"
            f"Generate {num_ideas} venture ideas that address this gap.\n"
            f"Provide the output strictly as a JSON list of objects containing 'name', 'tagline', and 'revenue_model'.\n"
            f"Do not write conversational explanations, write valid JSON only."
        )
        try:
            content = self.llm.generate(prompt)
            clean_content = content.replace("```json", "").replace("```", "").strip()
            ideas = json.loads(clean_content)
        except Exception as e:
            ideas = [
                {
                    "name": f"AI {sector.capitalize()} Analyzer",
                    "tagline": f"Solving: {gap_description}",
                    "revenue_model": "SaaS Subscription"
                }
            ]
        return ideas

    def spawn_venture(self, name: str, sector: str, location: str = None, target: str = None, revenue_goal: float = None) -> Dict[str, Any]:
        """Runs the create_venture.py script as a subprocess to spawn a venture directory."""
        if not os.path.exists(CREATE_VENTURE_SCRIPT):
            return {
                "status": "error",
                "message": f"Create Venture CLI spawner script not found at {CREATE_VENTURE_SCRIPT}"
            }
        
        args = [
            "python3",
            CREATE_VENTURE_SCRIPT,
            "--name", name,
            "--sector", sector
        ]
        if location:
            args.extend(["--location", location])
        if target:
            args.extend(["--target", target])
        if revenue_goal:
            args.extend(["--revenue", str(revenue_goal)])
            
        try:
            res = subprocess.run(
                args,
                capture_output=True,
                text=True,
                cwd="/Users/acebless/Documents",
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

if __name__ == '__main__':
    v_factory = VentureFactoryEngine()
    import sys
    if len(sys.argv) > 2:
        action = sys.argv[1]
        if action == "ideate":
            print(json.dumps(v_factory.ideate("beauty", "skincare tracking"), indent=2))
        elif action == "spawn":
            print(json.dumps(v_factory.spawn_venture("Miami glow", "beauty"), indent=2))
