#!/usr/bin/env python3
"""
Writing Engine Initialization Script
Creates base templates and initialization status.
"""

import os
import json
from pathlib import Path
from datetime import datetime

DOCS_ROOT = Path("/Users/acebless/Documents")
WRITING_ENGINE_ROOT = DOCS_ROOT / "WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/WRITING-ENGINE"

def create_base_files():
    """Create foundational markdown files."""

    files = {
        "00-README.md": """# Writing Engine

Automated narrative system for 712 ventures.

## Folders

- 01-FOUNDATION/ — Brand voice, style guide
- 02-COPYWRITING/ — Landing pages, emails, ads
- 03-CONTENT/ — Social media, blogs
- 04-BUSINESS-WRITING/ — PRDs, proposals
- 05-VENTURE-WRITING/ — Per-venture overrides
- 06-KNOWLEDGE-BASE/ — Case studies, lessons
- 07-AI-WRITER-AGENTS/ — Agent docs
- 08-TEMPLATES/ — Reusable templates
- 10-AUDIO-VISUAL/ — Video scripts, thumbnails
- 11-STRATEGY-DOCS/ — Content calendar, keywords
- 12-APPROVAL-WORKFLOWS/ — Compliance checklist
- 13-METRICS-ANALYTICS/ — Performance tracking

## Status

Created: {date}
Supabase Tables: 4 (content_drafts, brand_voices, compliance_log, content_metrics)
Ventures: 712
""".format(date=datetime.now().strftime("%Y-%m-%d")),

        "01-FOUNDATION/BRAND-VOICE.md": """# Global Brand Voice

## Personality
- Tone: Confident, human-centric, visionary
- Audience: Founders, operators, builders
- Message: "Build once. Scale to 712."

## Principles
1. Clarity first
2. Active voice
3. Benefit-driven
4. Evidence-based

## Forbidden
- synergy, leverage, paradigm shift, disruptive

## Examples
✗ "leverage cutting-edge AI to optimize"
✓ "Cut admin time by 12 hours/week"
""",

        "02-COPYWRITING/LANDING-PAGES.md": """# Landing Page Templates

## PAS Framework
- Problem: [Pain + cost]
- Agitate: [Why it matters]
- Solve: [Your solution]
- Proof: [3-4 results]
- CTA: [One action]

## Example
Problem: Managing payroll takes 8 hrs/week
Agitate: While you're drowning, team's waiting
Solve: HRMS: Payroll in 10 minutes
Proof: 50 contractors/week, zero errors
CTA: Start Free Trial
""",

        "11-STRATEGY-DOCS/CONTENT-CALENDAR-TEMPLATE.md": """# Weekly Content Calendar

Week of: [DATE]

| Day | Platform | Topic | Status |
|-----|----------|-------|--------|
| Mon | LinkedIn | Case Study | ❌ |
| Tue | TikTok | BTS Video | ❌ |
| Wed | Email | Newsletter | ❌ |
| Thu | Twitter | Insights | ❌ |
| Fri | Blog | [Keyword] | ❌ |

## Metrics
| Platform | CTR | Conversions | Revenue |
|----------|-----|-------------|---------|
| Email | 3.2% | 5 | $2,450 |
| LinkedIn | 1.8% | 2 | $450 |
| TikTok | 2.1% | 8 | $1,200 |
""",
    }

    for filepath, content in files.items():
        full_path = WRITING_ENGINE_ROOT / filepath
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
        print(f"✅ {filepath}")

def create_status():
    """Create initialization status."""
    status = {
        "initialized_at": datetime.now().isoformat(),
        "folders_created": 13,
        "supabase_tables": ["content_drafts", "brand_voices", "compliance_log", "content_metrics"],
        "next_steps": [
            "Execute SUPABASE-SCHEMA.sql in Supabase",
            "Run: python3 batch_generate_copy.py",
            "Wire n8n webhook",
        ],
    }

    with open(WRITING_ENGINE_ROOT / "INIT-STATUS.json", "w") as f:
        json.dump(status, f, indent=2)
    print(f"✅ INIT-STATUS.json")

if __name__ == "__main__":
    print("🚀 Initializing Writing Engine...\n")
    create_base_files()
    create_status()
    print("\n✅ DONE\n📋 Next: Execute SUPABASE-SCHEMA.sql then run batch_generate_copy.py")
