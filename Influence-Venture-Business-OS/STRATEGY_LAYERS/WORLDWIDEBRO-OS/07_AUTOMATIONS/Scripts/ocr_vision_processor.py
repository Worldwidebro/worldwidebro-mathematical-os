#!/usr/bin/env python3
"""
OCR Vision Processor — Instagram Screenshot → Structured JSON

Reads images from 00_INTAKE_LAYER/Instagram_Screenshots/
Uses Claude Vision API to extract caption + metadata
Outputs structured JSON with idea_text, people, tools, monetization_angle, confidence

Usage:
    python ocr_vision_processor.py --image-path path/to/screenshot.png
    python ocr_vision_processor.py --batch-dir /WORLDWIDEBRO-OS/00_INTAKE_LAYER/Instagram_Screenshots/
"""

import json
import sys
import argparse
import base64
from pathlib import Path
from datetime import datetime
from anthropic import Anthropic

client = Anthropic()

EXTRACTION_PROMPT = """You are an Instagram intelligence extractor. Analyze this Instagram post/screenshot and extract structured insights.

RETURN VALID JSON ONLY (no markdown, no preamble):

{
  "idea_text": "The core idea or insight from this post (1-2 sentences)",
  "category": "AI|Marketing|Sales|Automation|Ventures|Operations",
  "people_mentioned": ["Name 1", "Name 2"],
  "tools_mentioned": ["Tool 1", "Tool 2"],
  "monetization_angle": "How could this make money? null if not clear",
  "frameworks": ["Framework 1"],
  "is_opportunity": true|false,
  "confidence": 0.0-1.0,
  "source_type": "post|story|reel|caption|comment"
}

Be concise. Confidence = how certain you are this is a real business opportunity (not just content).
"""

def encode_image_to_base64(image_path: str) -> str:
    """Convert image file to base64 for Claude Vision API."""
    with open(image_path, "rb") as image_file:
        return base64.standard_b64encode(image_file.read()).decode("utf-8")

def get_image_media_type(image_path: str) -> str:
    """Determine image media type from file extension."""
    ext = Path(image_path).suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    return media_types.get(ext, "image/jpeg")

def process_image(image_path: str) -> dict:
    """Process a single image using Claude Vision API. Returns structured JSON extraction."""
    image_path = Path(image_path)
    if not image_path.exists():
        return {"error": f"Image not found: {image_path}"}

    image_data = encode_image_to_base64(str(image_path))
    media_type = get_image_media_type(str(image_path))

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": image_data,
                            },
                        },
                        {"type": "text", "text": EXTRACTION_PROMPT},
                    ],
                }
            ],
        )

        response_text = message.content[0].text.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]

        extraction = json.loads(response_text.strip())
        extraction["source_file"] = str(image_path)
        extraction["processed_at"] = datetime.utcnow().isoformat()
        extraction["extracted_by"] = "ocr_vision_processor v1.0"

        return extraction

    except json.JSONDecodeError as e:
        return {"error": f"JSON parse failed: {e}"}
    except Exception as e:
        return {"error": f"API error: {str(e)}"}

def process_batch(directory: str) -> list:
    """Process all images in a directory."""
    dir_path = Path(directory)
    if not dir_path.is_dir():
        print(f"Directory not found: {directory}")
        return []

    results = []
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

    for image_file in sorted(dir_path.iterdir()):
        if image_file.suffix.lower() in image_extensions:
            print(f"Processing: {image_file.name}...", file=sys.stderr)
            result = process_image(str(image_file))
            results.append(result)

    return results

def main():
    parser = argparse.ArgumentParser(description="Extract insights from Instagram screenshots")
    parser.add_argument("--image-path", type=str, help="Path to single image")
    parser.add_argument("--batch-dir", type=str, help="Path to directory of images")
    parser.add_argument("--output", type=str, help="Output JSON file (default: stdout)")

    args = parser.parse_args()

    if args.image_path:
        results = [process_image(args.image_path)]
    elif args.batch_dir:
        results = process_batch(args.batch_dir)
    else:
        parser.print_help()
        sys.exit(1)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Saved to: {args.output}", file=sys.stderr)
    else:
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
