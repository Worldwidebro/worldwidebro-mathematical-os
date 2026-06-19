#!/usr/bin/env python3
"""
Extraction Agent — JSON → Structured Ideas with Venture Routing

Takes output from ocr_vision_processor.py
Adds venture type tagging, deal flow classification, routing recommendations

Usage:
    python extraction_agent.py --input extracted_ideas.json --output ideas_classified.json
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
from anthropic import Anthropic

client = Anthropic()

VENTURE_ROUTING_PROMPT = """Given this extracted idea, classify it for our venture portfolio.

Idea: {idea_text}
Category: {category}
Tools: {tools}
Monetization: {monetization}

Return valid JSON ONLY:

{
  "venture_types": ["HRMS", "ConstructionOps", "RealEstate", "Logistics", "AI_Services"],
  "venture_type_primary": "best fit from above",
  "next_action": "research|validate|build|pass",
  "routable_agents": ["hrms_agent", "ops_agent"],
  "risk_level": "low|medium|high",
  "deal_flow_stage": "idea|lead|opportunity|pitch|deal",
  "confidence_in_routing": 0.0-1.0,
  "recommended_next_step": "what happens next"
}

Strategic routing to operating companies.
"""

def classify_idea(idea: Dict[str, Any]) -> Dict[str, Any]:
    """Classify idea for venture routing using Claude."""
    if idea.get("error"):
        return idea

    try:
        prompt = VENTURE_ROUTING_PROMPT.format(
            idea_text=idea.get("idea_text", ""),
            category=idea.get("category", ""),
            tools=", ".join(idea.get("tools_mentioned", [])),
            monetization=idea.get("monetization_angle", "Unknown"),
        )

        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )

        response_text = message.content[0].text.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]

        classification = json.loads(response_text.strip())
        idea.update(classification)
        idea["classified_at"] = datetime.utcnow().isoformat()

        return idea

    except Exception as e:
        idea["classification_error"] = str(e)
        return idea

def process_ideas(ideas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process list of extracted ideas."""
    classified_ideas = []

    for idx, idea in enumerate(ideas):
        print(f"Classifying idea {idx + 1}/{len(ideas)}...", file=sys.stderr)
        classified = classify_idea(idea)
        classified_ideas.append(classified)

    return classified_ideas

def main():
    parser = argparse.ArgumentParser(description="Classify and route extracted ideas")
    parser.add_argument("--input", type=str, required=True, help="Input JSON from ocr_vision_processor")
    parser.add_argument("--output", type=str, help="Output JSON (default: stdout)")

    args = parser.parse_args()

    try:
        with open(args.input, "r") as f:
            ideas = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    classified = process_ideas(ideas if isinstance(ideas, list) else [ideas])

    if args.output:
        with open(args.output, "w") as f:
            json.dump(classified, f, indent=2)
        print(f"Saved to: {args.output}", file=sys.stderr)
    else:
        print(json.dumps(classified, indent=2))

if __name__ == "__main__":
    main()
