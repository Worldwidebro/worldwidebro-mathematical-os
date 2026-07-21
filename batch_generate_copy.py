#!/usr/bin/env python3
"""
Batch Copy Generator using Ollama (Local LLM)
Generates landing page copy using qwen2.5:32b on Mac Studio
"""

import os
import json
import subprocess
from pathlib import Path
import csv

OLLAMA_HOST = "http://100.87.214.70:11434"  # Mac Studio (tailscale IP)
OLLAMA_MODEL = "qwen2.5:32b"

DOCS_ROOT = Path("/Users/acebless/Documents")
OUTPUT_DIR = DOCS_ROOT / "WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/WRITING-ENGINE/09-ARCHIVE/generated-copy"
VENTURES_CSV = DOCS_ROOT / "WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv"

def read_ventures(limit=10):
    """Read ventures from CSV."""
    ventures = []
    with open(VENTURES_CSV, "r") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= limit:
                break
            ventures.append(row)
    return ventures

def generate_copy(venture_name, description):
    """Call Ollama to generate landing page copy."""

    prompt = f"""Write landing page copy for: {venture_name}

Description: {description}

Format:
Headline: [benefit-driven]
Subheading: [clarification]
Problem: [customer pain]
Solution: [your fix]
CTA: [button text]

Be specific. Use metrics if possible."""

    try:
        result = subprocess.run(
            ["curl", "-s", f"{OLLAMA_HOST}/api/generate",
             "-d", json.dumps({"model": OLLAMA_MODEL, "prompt": prompt, "stream": False})],
            capture_output=True, text=True, timeout=30
        )

        if result.returncode == 0:
            response = json.loads(result.stdout)
            return response.get("response", "")
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def batch_generate(batch_type="landing_pages", count=10):
    """Generate copy for multiple ventures."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ventures = read_ventures(limit=count)

    print(f"🚀 Generating {batch_type} for {len(ventures)} ventures...\n")

    generated = []
    for i, v in enumerate(ventures, 1):
        v_id = v.get("venture_id", "UNKNOWN")
        v_name = v.get("name", "Unknown")
        desc = v.get("description", "")

        print(f"[{i}/{len(ventures)}] {v_name}...", end=" ", flush=True)

        copy = generate_copy(v_name, desc)
        if copy:
            generated.append({"venture_id": v_id, "venture_name": v_name, "copy": copy})
            print("✅")
        else:
            print("❌")

    # Save output
    output_file = OUTPUT_DIR / f"{batch_type}-{len(ventures)}.json"
    with open(output_file, "w") as f:
        json.dump(generated, f, indent=2)

    print(f"\n✅ Generated {len(generated)}/{len(ventures)}")
    print(f"📁 {output_file}")

if __name__ == "__main__":
    import sys

    batch_type = "landing_pages"
    count = 10

    if "--count" in sys.argv:
        count = int(sys.argv[sys.argv.index("--count") + 1])

    print(f"🔗 Testing Ollama at {OLLAMA_HOST}...")
    try:
        r = subprocess.run(["curl", "-s", f"{OLLAMA_HOST}/api/tags"],
                          capture_output=True, timeout=5)
        if r.returncode == 0:
            print("✅ Ollama online\n")
            batch_generate(batch_type, count)
        else:
            print("❌ Ollama not responding")
    except Exception as e:
        print(f"❌ Cannot reach Ollama: {e}")
        print(f"   ssh macstudio && ollama serve")
