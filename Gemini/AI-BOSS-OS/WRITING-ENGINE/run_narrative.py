#!/usr/bin/env python3
import os
import sys
import argparse

GEMINI_DIR = "/Users/acebless/Documents/Gemini"
sys.path.append(os.path.join(GEMINI_DIR, "services"))

try:
    from knowledge_engine import LLMAdapter
except ImportError:
    class LLMAdapter:
        def generate(self, prompt, model="qwen3:8b"):
            import requests
            body = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False
            }
            r = requests.post("http://localhost:11434/v1/chat/completions", json=body, timeout=15)
            return r.json()["choices"][0]["message"]["content"]

def load_file_content(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def run_narrative_engine(text, voice="visionary", role="copywriter", framework="direct", venture=""):
    engine_dir = os.path.join(GEMINI_DIR, "AI-BOSS-OS", "WRITING-ENGINE")
    
    # Load rules and structures
    brand_voice = load_file_content(os.path.join(engine_dir, "01-FOUNDATION", "BRAND-VOICE.md"))
    style_guide = load_file_content(os.path.join(engine_dir, "01-FOUNDATION", "STYLE-GUIDE.md"))
    persuasion = load_file_content(os.path.join(engine_dir, "01-FOUNDATION", "PERSUASION-PSYCHOLOGY.md"))
    copy_frameworks = load_file_content(os.path.join(engine_dir, "02-COPYWRITING", "EMAIL-SEQUENCES.md"))
    
    # Venture overrides
    venture_override = ""
    if venture:
        # Check active venture writing path
        venture_path = os.path.join(GEMINI_DIR, "AI-BOSS-OS", "VENTURES", venture, "WRITING", "Brand-Voice.md")
        if not os.path.exists(venture_path):
            # Check secondary documents path if active
            venture_path = os.path.join("/Users/acebless/Documents/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active", venture, "writing", "Brand-Voice.md")
        if os.path.exists(venture_path):
            venture_override = load_file_content(venture_path)
            
    # Load agent role rules
    agent_prompt = ""
    if role == "copywriter":
        agent_prompt = load_file_content(os.path.join(engine_dir, "07-AI-WRITER-AGENTS", "COPYWRITER-AGENT.md"))
    else:
        agent_prompt = load_file_content(os.path.join(engine_dir, "07-AI-WRITER-AGENTS", "EDITOR-AGENT.md"))

    prompt = f"""
You are the {role.upper()} AGENT of the WORLDWIDEBRO-OS Writing Engine.
Process the following raw input text.

=== INPUT TEXT ===
{text}
==================

Here is our global brand voice and tone guidelines:
{brand_voice}

{"Here is the specific brand voice override for venture " + venture + ":\n" + venture_override if venture_override else ""}

Here is our editorial style guide:
{style_guide}

Here is the copywriting frameworks reference:
{copy_frameworks}

Here is our persuasion psychology reference:
{persuasion}

Here are your specific agent directives:
{agent_prompt}

TASK:
Rewrite and polish the INPUT TEXT.
- Use the '{voice}' tone option.
- Apply the '{framework}' copywriting framework (structure it accordingly if applicable, otherwise keep it formatted neatly).
- Ensure the output strictly adheres to the style guide (active voice, serial commas, bold metrics).
- Output ONLY the polished and complete text without any surrounding commentary or meta-notes.
"""

    adapter = LLMAdapter()
    return adapter.generate(prompt)

def main():
    parser = argparse.ArgumentParser(description="Narrative Engine Runner")
    parser.add_argument("--input", type=str, required=True, help="Raw draft text or generation prompt")
    parser.add_argument("--voice", type=str, default="visionary", help="Tone variant to use")
    parser.add_argument("--role", type=str, default="copywriter", choices=["copywriter", "editor"], help="Agent role")
    parser.add_argument("--framework", type=str, default="direct", choices=["AIDA", "PAS", "direct"], help="Framework")
    parser.add_argument("--venture", type=str, default="", help="Venture ID")
    args = parser.parse_args()

    try:
        output = run_narrative_engine(args.input, args.voice, args.role, args.framework, args.venture)
        print(output.strip())
    except Exception as e:
        print(f"Error running narrative engine: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
