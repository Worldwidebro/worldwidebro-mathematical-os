#!/usr/bin/env python3
"""
Repository Classification System - Phase 1 (LLM enrichment)

For deterministic Level 2+3 pilot (no API), use:
  python3 WORLDWIDEBRO-OS/REGISTRIES/repo_classification_pilot.py --pilot 100

This script enriches Tier 1-2 rows with Claude multi-turn summaries.
Requires ANTHROPIC_API_KEY and repos from pilot CSV or full inventory.
"""

import os
import json
import csv
import sys
import subprocess
from pathlib import Path
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

# Configuration
PILOT_SCRIPT = "/Users/acebless/Documents/WORLDWIDEBRO-OS/REGISTRIES/repo_classification_pilot.py"
PILOT_CSV = "/Users/acebless/Documents/WORLDWIDEBRO-OS/REGISTRIES/repository_registry_pilot.csv"
REPOS_INPUT_FILE = "/Users/acebless/Documents/repos-owned-inventory.json"
OUTPUT_REGISTRY = "/Users/acebless/Documents/WORLDWIDEBRO-OS/REGISTRIES/repository-intelligence-registry.csv"
OUTPUT_DETAILED = "/Users/acebless/Documents/WORLDWIDEBRO-OS/REGISTRIES/repository-intelligence-detailed.json"
BATCH_SIZE = 10


def run_pilot_if_needed(pilot_size: int = 100) -> None:
    """Run deterministic pilot classifier before LLM enrichment."""
    if not os.path.exists(PILOT_CSV):
        print(f"Running pilot classifier ({pilot_size} repos)...")
        subprocess.run(
            [sys.executable, PILOT_SCRIPT, "--pilot", str(pilot_size)],
            check=True,
        )

def load_repos():
    """Load repository data from JSON"""
    if not os.path.exists(REPOS_INPUT_FILE):
        print(f"Error: {REPOS_INPUT_FILE} not found")
        return []

    with open(REPOS_INPUT_FILE, 'r') as f:
        data = json.load(f)

    # Handle both dict and list formats
    if isinstance(data, dict):
        if 'repos' in data:
            return data['repos']
        elif 'repositories' in data:
            return data['repositories']
        else:
            return list(data.values())
    return data

def classify_repo(repo_data):
    """Use Claude to classify a single repository using multi-turn conversation"""

    repo_name = repo_data.get('name', 'Unknown')
    repo_url = repo_data.get('html_url', '')
    description = repo_data.get('description', '')
    language = repo_data.get('language', 'Unknown')
    stars = repo_data.get('stargazers_count', 0)

    print(f"\n📦 Classifying: {repo_name}")
    print(f"   URL: {repo_url}")
    print(f"   Language: {language} | Stars: {stars}")

    # Start multi-turn conversation
    conversation_history = []

    # Turn 1: Layer 1 Classification
    layer1_prompt = f"""
Analyze this GitHub repository and provide a classification:

REPO: {repo_name}
URL: {repo_url}
DESCRIPTION: {description}
LANGUAGE: {language}
STARS: {stars}

Determine:
1. Primary Purpose (what does it do)
2. Problem Solved (who needs this)
3. Target User (job role/function)
4. Technology Stack
5. Dependencies (standalone or requires others)
6. Inputs & Outputs
7. Business Value (could this be a product?)
8. Technical Value (production-ready? code quality? maintenance status?)
9. Strategic Value (reusability 1-10)
10. Classification Type (Infrastructure/Platform/Product/Agent/Tool/Service/Framework/Library/Dataset/Template/Workflow/Learning/Archive)

Provide confidence score (1-10) and reasoning.
"""

    conversation_history.append({"role": "user", "content": layer1_prompt})

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1500,
        system="You are a repository intelligence analyst. Classify GitHub repositories systematically using provided frameworks.",
        messages=conversation_history
    )

    layer1_response = response.content[0].text
    conversation_history.append({"role": "assistant", "content": layer1_response})

    print(f"✓ Layer 1 Classification complete")

    # Turn 2: Layer 2 Venture Relevance (if applicable)
    layer2_prompt = """
Based on your analysis, now score the venture relevance using this rubric:

1. Can it become a standalone business? (1-10)
2. Can it power multiple businesses? (1-10)
3. Internal productivity value (1-10)
4. Revenue potential if commercialized (1-10)
5. Defensibility/competitive moat (1-10)
6. Maintenance burden (1-10, inverted)

Total score of 6 dimensions:
- 40-50 = TIER 1: CRITICAL
- 30-39 = TIER 2: CORE ASSET
- 20-29 = TIER 3: USEFUL COMPONENT
- <20 = TIER 4: IGNORE

Provide scores, total, and tier classification.
"""

    conversation_history.append({"role": "user", "content": layer2_prompt})

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1000,
        system="You are a repository intelligence analyst. Classify GitHub repositories systematically using provided frameworks.",
        messages=conversation_history
    )

    layer2_response = response.content[0].text
    conversation_history.append({"role": "assistant", "content": layer2_response})

    print(f"✓ Layer 2 Venture Relevance complete")

    # Turn 3: Layer 3 Decision Matrix
    layer3_prompt = """
Provide a concise BUILD/BUY/WRAP decision:

Use this decision tree:
1. Production-ready & maintained actively?
2. Solves real problem in ventures?
3. Can use off-the-shelf?
4. Can extend/fork for our needs?
5. Can wrap with our logic?
6. Can commercialize directly?
7. Rebuild from scratch?

Choose ONE ACTION: [USE / FORK / FORK+EXTEND / WRAP / COMMERCIALIZE / REBUILD / LEARN / IGNORE]

Provide action, reasoning (one sentence), timeline, and owner recommendation.
"""

    conversation_history.append({"role": "user", "content": layer3_prompt})

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=800,
        system="You are a repository intelligence analyst. Classify GitHub repositories systematically using provided frameworks.",
        messages=conversation_history
    )

    layer3_response = response.content[0].text
    conversation_history.append({"role": "assistant", "content": layer3_response})

    print(f"✓ Layer 3 Build/Buy/Wrap decision complete")

    # Turn 4: Layer 5 & 6 - OS Layer + Technology Tags
    layer45_prompt = """
Finally, provide:

OS LAYER ASSIGNMENT (primary & secondary):
Choose from: Identity, Knowledge, Memory, Agent, Automation, Communication, Analytics, Finance, Infrastructure, Security, Data, API, Frontend, Backend, AI/ML

TECHNOLOGY TAGS (comma-separated):
From: React, Vue, Node.js, Python, PostgreSQL, MongoDB, Docker, Kubernetes, Supabase, AWS, TensorFlow, LangChain, etc.

And for VENTURE FACTORY potential:
Is this a Venture Candidate? (YES/NO)
If YES: Estimated monthly revenue potential: $[X]K
Brief venture pitch (one paragraph if applicable)

Provide OS layers, tech tags, venture candidate status, and revenue estimate.
"""

    conversation_history.append({"role": "user", "content": layer45_prompt})

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1000,
        system="You are a repository intelligence analyst. Classify GitHub repositories systematically using provided frameworks.",
        messages=conversation_history
    )

    layer45_response = response.content[0].text

    print(f"✓ Layer 5 & 6 complete")

    # Parse and structure results
    result = {
        "repo_name": repo_name,
        "repository_url": repo_url,
        "description": description,
        "language": language,
        "stars": stars,
        "layer1_classification": layer1_response,
        "layer2_venture_relevance": layer2_response,
        "layer3_decision": layer3_response,
        "layer45_os_and_tech": layer45_response,
        "full_conversation": conversation_history
    }

    return result

def parse_classification_result(result):
    """Extract key fields from classification result for CSV"""

    # Extract primary type from layer1 response
    layer1_text = result['layer1_classification'].lower()
    primary_type = "Unknown"

    type_keywords = {
        "infrastructure": "Infrastructure",
        "platform": "Platform",
        "product": "Product",
        "agent": "Agent",
        "tool": "Tool",
        "service": "Service",
        "framework": "Framework",
        "library": "Library",
        "dataset": "Dataset",
        "template": "Template",
        "workflow": "Workflow",
        "learning": "Learning",
        "archive": "Archive"
    }

    for keyword, type_name in type_keywords.items():
        if keyword in layer1_text:
            primary_type = type_name
            break

    # Extract venture tier from layer2
    tier = "TIER 4"
    for tier_name in ["TIER 1", "TIER 2", "TIER 3", "TIER 4"]:
        if tier_name in result['layer2_venture_relevance']:
            tier = tier_name
            break

    # Extract action from layer3
    action = "UNKNOWN"
    actions = ["USE", "FORK", "FORK+EXTEND", "WRAP", "COMMERCIALIZE", "REBUILD", "LEARN", "IGNORE"]
    for act in actions:
        if act in result['layer3_decision']:
            action = act
            break

    return {
        "repo_name": result['repo_name'],
        "primary_type": primary_type,
        "venture_tier": tier,
        "decision_action": action,
        "stars": result['stars'],
        "language": result['language']
    }

def main():
    """Main execution"""
    print("🚀 Repository Classification System - Phase 1")
    print("=" * 60)

    # Load repositories
    repos = load_repos()
    print(f"\n📚 Loaded {len(repos)} repositories")

    if not repos:
        print("No repositories found. Exiting.")
        return

    # For demo: classify first 5 repos
    demo_count = min(5, len(repos))
    print(f"\n🔄 Classifying first {demo_count} repos (demo mode)")

    classified_repos = []
    csv_rows = []

    for i, repo in enumerate(repos[:demo_count]):
        try:
            result = classify_repo(repo)
            classified_repos.append(result)

            # Extract CSV row
            csv_row = parse_classification_result(result)
            csv_rows.append(csv_row)

            print(f"✅ {i+1}/{demo_count} complete")

        except Exception as e:
            print(f"❌ Error classifying {repo.get('name', 'Unknown')}: {str(e)}")
            continue

    # Write detailed results to JSON
    print(f"\n💾 Writing detailed results to {OUTPUT_DETAILED}")
    os.makedirs(os.path.dirname(OUTPUT_DETAILED), exist_ok=True)

    with open(OUTPUT_DETAILED, 'w') as f:
        json.dump(classified_repos, f, indent=2)

    # Write CSV summary
    print(f"💾 Writing CSV registry to {OUTPUT_REGISTRY}")
    os.makedirs(os.path.dirname(OUTPUT_REGISTRY), exist_ok=True)

    if csv_rows:
        with open(OUTPUT_REGISTRY, 'w', newline='') as f:
            fieldnames = csv_rows[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(csv_rows)

    print(f"\n✅ Classification complete!")
    print(f"   Classified: {len(classified_repos)} repos")
    print(f"   Detailed: {OUTPUT_DETAILED}")
    print(f"   Registry: {OUTPUT_REGISTRY}")

    # Summary statistics
    tier_counts = {}
    action_counts = {}

    for row in csv_rows:
        tier = row['venture_tier']
        action = row['decision_action']
        tier_counts[tier] = tier_counts.get(tier, 0) + 1
        action_counts[action] = action_counts.get(action, 0) + 1

    print(f"\n📊 Summary:")
    print(f"   By Tier: {tier_counts}")
    print(f"   By Action: {action_counts}")

if __name__ == "__main__":
    main()
