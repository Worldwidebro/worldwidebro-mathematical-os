#!/usr/bin/env python3
"""Process captured Instagram data"""
import json
from pathlib import Path

INTAKE_DIR = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/00_INTAKE_LAYER/Instagram_Raw")

def process_captures():
    """Find and process all captured Instagram posts"""
    captures = list(INTAKE_DIR.glob("*.json"))

    if not captures:
        print("⚠️  No captures found in", INTAKE_DIR)
        return

    print(f"📊 Found {len(captures)} captures")

    for capture_file in captures:
        with open(capture_file, 'r') as f:
            data = json.load(f)

        print(f"\n📸 {data.get('source_url', 'unknown')}")
        print(f"   Caption: {data.get('caption', '')[:60]}...")

if __name__ == "__main__":
    process_captures()
