#!/usr/bin/env python3
"""
904 Starred Repositories Capability Audit Engine
Grounded in Rule #2 of AGENTS.md / ANTIGRAVITY.md:
"Reuse First & Starred Repos: Never write custom code without first querying the 904 Starred Repositories"

Classifies the 904 Starred Repositories across 4 Canonical Action Tiers:
- ADOPT: Directly deployed to eliminate SaaS costs or accelerate Tier-0 (< 48h to cash).
- ADAPT: High-value tools/frameworks needing vertical re-skinning for Logistics, Staffing, Construction, or Health.
- REFERENCE: Architectural specs, prompt repos, skill sets, system design patterns.
- IGNORE: Coding interview prep, algorithmic puzzles, consumer toys, non-enterprise lists.
"""

import json
import re
import os
import yaml

INVENTORY_PATH = "_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md"
OUTPUT_JSON = "_REGISTRIES/CANONICAL/STARRED_REPOS_CAPABILITY_AUDIT.json"
OUTPUT_YAML = "_REGISTRIES/CANONICAL/STARRED_REPOS_CAPABILITY_AUDIT.yaml"
VEX_DATA_TARGET = "../../Worldwidebro-Vex/src/data/starred-audit.json"

# High-priority manual overrides for known key repositories in the company ecosystem
EXPLICIT_OVERRIDES = {
    "openobserve/openobserve": {
        "classification": "ADOPT",
        "category": "OBSERVABILITY & TELEMETRY",
        "target_ventures": ["OMNIROUTE", "VEX", "LT-011"],
        "target_layer": "INFRASTRUCTURE CORE",
        "distance_to_cash": "Infrastructure Core",
        "commercial_use": "Single-binary Rust observability on Mac Studio; captures all OmniRoute inference spans, latency, and token costs at 140x lower cost than Datadog/Elastic.",
        "impact_use": "Enables zero-cost open telemetry for community non-profit software deployments."
    },
    "n8n-io/n8n": {
        "classification": "ADOPT",
        "category": "WORKFLOW AUTOMATION",
        "target_ventures": ["OPS-001", "LT-005", "CALLCENTER"],
        "target_layer": "4. OPERATING COMPANY LAYER",
        "distance_to_cash": "Immediate (< 24h)",
        "commercial_use": "Automates applicant intake, clinic STAT courier triggers, and Twilio voice webhooks with visual drag-and-drop workflows.",
        "impact_use": "Provides automated workflow pipelines for community training programs and non-profit grant reporting."
    },
    "firecrawl/firecrawl": {
        "classification": "ADOPT",
        "category": "WEB DATA EXTRACTION",
        "target_ventures": ["OPS-001", "LT-005", "RE-001"],
        "target_layer": "4. OPERATING COMPANY LAYER",
        "distance_to_cash": "Immediate (< 24h)",
        "commercial_use": "Extracts hiring manager contacts from warehouse job boards and clinic directory listings in Charlotte Metro.",
        "impact_use": "Scrapes public grant postings and minority-owned business opportunity portals."
    },
    "garrytan/gstack": {
        "classification": "ADOPT",
        "category": "DOCUMENT & REPORT GENERATION",
        "target_ventures": ["VEX", "RE-001", "CON-001"],
        "target_layer": "2. HOLDING COMPANY LAYER",
        "distance_to_cash": "Direct (< 48h)",
        "commercial_use": "Generates publication-grade vector PDF due diligence packets, investor prospectuses, and loan packages via Playwright.",
        "impact_use": "Formats professional 501(c)(3) annual impact reports and grant submittal decks."
    },
    "DietrichGebert/ponytail": {
        "classification": "ADOPT",
        "category": "CODE INTEGRITY & GOVERNANCE",
        "target_ventures": ["BRAIN", "VEX"],
        "target_layer": "INFRASTRUCTURE CORE",
        "distance_to_cash": "Infrastructure Core",
        "commercial_use": "Enforces 'the best code is the code you never wrote' anti-bloat guardrails, preventing unnecessary dependencies.",
        "impact_use": "Audits open-source educational code for minimal technical debt."
    },
    "msitarzewski/agency-agents": {
        "classification": "ADOPT",
        "category": "MULTI-AGENT WORKFORCE",
        "target_ventures": ["BRAIN", "OPS-001", "LT-005", "CALLCENTER"],
        "target_layer": "4. OPERATING COMPANY LAYER",
        "distance_to_cash": "Immediate (< 24h)",
        "commercial_use": "Provides specialized subagent skill definitions (@sales-coach, @reality-checker, @qa, @dispatcher) executing in Company Brain.",
        "impact_use": "Supplies mentoring and interview preparation agents for vocational trainees."
    },
    "browser-use/browser-use": {
        "classification": "ADOPT",
        "category": "BROWSER AUTOMATION",
        "target_ventures": ["LT-005", "OPS-001", "RE-001"],
        "target_layer": "4. OPERATING COMPANY LAYER",
        "distance_to_cash": "Direct (< 48h)",
        "commercial_use": "Automates booking requests on third-party freight portals, municipal parcel registry queries, and clinical EHR portals.",
        "impact_use": "Assists non-technical community users with automated utility assistance and state benefit form submission."
    },
    "twentyhq/twenty": {
        "classification": "ADAPT",
        "category": "CRM & CLIENT ENGAGEMENT",
        "target_ventures": ["OPS-001", "LT-005", "RE-001"],
        "target_layer": "4. OPERATING COMPANY LAYER",
        "distance_to_cash": "Direct (< 48h)",
        "commercial_use": "Open-source enterprise CRM adapted for tracking medical clinic specimen accounts and warehouse hiring manager relationships.",
        "impact_use": "Community partner relationship manager tracking foundation grants and apprentices."
    },
    "chatwoot/chatwoot": {
        "classification": "ADOPT",
        "category": "OMNICHANNEL CUSTOMER ENGAGEMENT",
        "target_ventures": ["CALLCENTER", "LT-005", "LT-011"],
        "target_layer": "4. OPERATING COMPANY LAYER",
        "distance_to_cash": "Immediate (< 24h)",
        "commercial_use": "Self-hosted customer communication hub integrating WhatsApp, SMS, web chat, and email for 24/7 delivery tracking.",
        "impact_use": "Multi-lingual community support desk for local assistance inquiries."
    },
    "exo-explore/exo": {
        "classification": "ADOPT",
        "category": "DISTRIBUTED LOCAL COMPUTE",
        "target_ventures": ["BRAIN", "OMNIROUTE"],
        "target_layer": "INFRASTRUCTURE CORE",
        "distance_to_cash": "Infrastructure Core",
        "commercial_use": "Clusters Mac Studio M4 Max and MacBook Air via MLX peer-to-peer interconnect for 70B+ model inference with zero cloud fees.",
        "impact_use": "Permits zero-cost offline AI reasoning for community centers without broadband."
    },
    "deeplethe/utopia": {
        "classification": "ADAPT",
        "category": "KNOWLEDGE & ONTOLOGY CORE",
        "target_ventures": ["BRAIN", "VEX"],
        "target_layer": "1. GOVERNANCE & FAMILY OFFICE",
        "distance_to_cash": "Medium (72h+)",
        "commercial_use": "Bitemporal enterprise world model and ontology-to-SQL mapping for tracking 150-Node entity evolutions.",
        "impact_use": "Maps philanthropic endowment allocations across non-profit trust structures."
    },
    "codecrafters-io/build-your-own-x": {
        "classification": "IGNORE",
        "category": "EDUCATIONAL / STUDY",
        "target_ventures": ["NONE"],
        "target_layer": "NONE",
        "distance_to_cash": "N/A",
        "commercial_use": "Rebuilding git, docker, or sqlite from scratch is educational but violates the reuse-first production mandate.",
        "impact_use": "Self-study material for students."
    },
    "jwasham/coding-interview-university": {
        "classification": "IGNORE",
        "category": "INTERVIEW PREP",
        "target_ventures": ["NONE"],
        "target_layer": "NONE",
        "distance_to_cash": "N/A",
        "commercial_use": "Academic Big Tech interview preparation guide with zero enterprise application.",
        "impact_use": "Reference for jobseekers."
    },
    "TheAlgorithms/Python": {
        "classification": "REFERENCE",
        "category": "ALGORITHMS & DATA STRUCTURES",
        "target_ventures": ["BRAIN"],
        "target_layer": "ENGINEERING CORE",
        "distance_to_cash": "N/A",
        "commercial_use": "Reference implementations for sorting, graph traversal, and spatial pathfinding in dispatch algorithms.",
        "impact_use": "Open educational algorithm implementations."
    },
    "donnemartin/system-design-primer": {
        "classification": "REFERENCE",
        "category": "ARCHITECTURE & SYSTEM DESIGN",
        "target_ventures": ["BRAIN", "LT-011", "VEX"],
        "target_layer": "ENGINEERING CORE",
        "distance_to_cash": "N/A",
        "commercial_use": "Standard patterns for designing large-scale high-concurrency architectures and fault-tolerant queues.",
        "impact_use": "Curriculum for junior engineering apprentices."
    },
    "github/spec-kit": {
        "classification": "ADOPT",
        "category": "SPEC-DRIVEN DEVELOPMENT",
        "target_ventures": ["BRAIN", "VEX"],
        "target_layer": "ENGINEERING CORE",
        "distance_to_cash": "Infrastructure Core",
        "commercial_use": "Enforces spec-first contracts before writing code, preventing placeholder architectures.",
        "impact_use": "Standardized requirements templates for civic technology projects."
    },
    "anthropics/skills": {
        "classification": "ADOPT",
        "category": "AGENT SKILLS STANDARD",
        "target_ventures": ["BRAIN", "OMNIROUTE"],
        "target_layer": "ENGINEERING CORE",
        "distance_to_cash": "Infrastructure Core",
        "commercial_use": "Official Anthropic agent skills framework, standardized across Company Brain .agents/skills/ directory.",
        "impact_use": "Open skill library for civic automation."
    },
    "f/prompts.chat": {
        "classification": "REFERENCE",
        "category": "PROMPT ENGINEERING",
        "target_ventures": ["CALLCENTER", "OPS-001"],
        "target_layer": "4. OPERATING COMPANY LAYER",
        "distance_to_cash": "Direct (< 48h)",
        "commercial_use": "Curated system prompts adaptable for customer intake and recruiter phone screening.",
        "impact_use": "Community prompt library for non-technical users."
    }
}

def classify_repo(index, repo_name, url, stars, lang, category, desc):
    full_str = f"{repo_name} {desc} {cat_override(category)}".lower()
    
    # Check explicit overrides
    for key, override in EXPLICIT_OVERRIDES.items():
        if key.lower() in repo_name.lower():
            return {
                "id": f"EXT-STAR-{int(index):03d}",
                "repo_name": repo_name,
                "url": url,
                "stars": stars,
                "language": lang,
                **override
            }

    # Heuristic Classification Rules
    # 1. IGNORE criteria: interview prep, pure book lists, leetcode, cheat sheets with no code
    if any(k in full_str for k in [
        "interview", "coding interview", "interview-prep", "leetcode", "book-of-secret", 
        "free-programming-books", "awesome-", "cheat-sheet", "cheatsheet", "roadmap",
        "curated list of", "awesome list", "tips and tricks", "flashcards"
    ]) and not any(k in full_str for k in ["engine", "agent", "crawler", "mcp", "workflow", "server"]):
        return {
            "id": f"EXT-STAR-{int(index):03d}",
            "repo_name": repo_name,
            "url": url,
            "stars": stars,
            "language": lang,
            "classification": "IGNORE",
            "category": "LIST / RESOURCE / STUDY",
            "target_ventures": ["NONE"],
            "target_layer": "NONE",
            "distance_to_cash": "N/A",
            "commercial_use": "Curated list or interview resource without deployable enterprise code.",
            "impact_use": "Self-study reading resource for community learners."
        }

    # 2. ADOPT criteria: agent harnesses, scrapers, workflow engines, OCR, PDF, phone, DBs, telemetry
    is_adopt = any(k in full_str for k in [
        "automation", "scraper", "crawler", "browser", "telemetry", "observability", 
        "pdf", "ocr", "workflow", "sip", "voip", "fastmcp", "mcp server", "vector", 
        "database", "redis", "postgres", "neo4j", "dispatch", "queue", "billing", 
        "stripe", "agent harness", "agentic", "cli tool", "search engine", "ollama", "inference"
    ])

    # 3. Target Ventures mapping
    target_ventures = []
    target_layer = "4. OPERATING COMPANY LAYER"
    distance = "Medium (72h+)"

    if any(k in full_str for k in ["courier", "medical", "dispatch", "route", "logistics", "gps", "fleet", "transport"]):
        target_ventures.extend(["LT-005", "LT-011"])
        target_layer = "7. SPECIALIZED LOGISTICS & FLEET"
        distance = "Immediate (< 24h)"
    elif any(k in full_str for k in ["staffing", "resume", "recruiter", "job", "applicant", "workforce", "hiring"]):
        target_ventures.append("OPS-001")
        distance = "Direct (< 48h)"
    elif any(k in full_str for k in ["voice", "call", "phone", "telephony", "audio", "speech", "whisper", "tts", "stt"]):
        target_ventures.append("CALLCENTER")
        distance = "Immediate (< 24h)"
    elif any(k in full_str for k in ["construction", "cad", "bim", "jobsite", "building", "field"]):
        target_ventures.append("CON-001")
        distance = "Direct (< 48h)"
    elif any(k in full_str for k in ["real estate", "property", "parcel", "gis", "map", "underwriting"]):
        target_ventures.append("RE-001")
        distance = "Direct (< 48h)"
    elif any(k in full_str for k in ["inference", "llm", "agent", "prompt", "rag", "eval", "mcp", "memory"]):
        target_ventures.extend(["BRAIN", "OMNIROUTE"])
        target_layer = "INFRASTRUCTURE CORE"
        distance = "Infrastructure Core"
    else:
        target_ventures.append("VEX")

    # 4. Determine Classification (ADOPT vs ADAPT vs REFERENCE)
    if any(k in full_str for k in ["benchmark", "spec", "primer", "template", "framework", "guidelines", "collection of prompts"]):
        classification = "REFERENCE"
        category_label = "ARCHITECTURE / SPEC / PATTERN"
    elif is_adopt and stars > 10000:
        classification = "ADOPT"
        category_label = "PRODUCTION AUTOMATION / INFRASTRUCTURE"
    elif any(k in full_str for k in ["crm", "erp", "e-commerce", "dashboard", "portal", "admin", "platform"]):
        classification = "ADAPT"
        category_label = "VERTICAL PLATFORM (NEEDS RESKIN)"
    elif is_adopt:
        classification = "ADAPT"
        category_label = "INTEGRATION UTILITY"
    else:
        classification = "REFERENCE"
        category_label = "CODE PATTERN / ALGORITHM"

    # Summarize commercial and impact use
    commercial_use = f"Provides open-source {category_label.lower()} for accelerating {', '.join(target_ventures[:2])} operations without proprietary SaaS fees."
    impact_use = f"Can be repurposed to supply free tooling or technical literacy resources to foundation programs."

    return {
        "id": f"EXT-STAR-{int(index):03d}",
        "repo_name": repo_name,
        "url": url,
        "stars": stars,
        "language": lang if lang != "-" else "Multi-Language",
        "classification": classification,
        "category": category_label,
        "target_ventures": list(set(target_ventures)),
        "target_layer": target_layer,
        "distance_to_cash": distance,
        "commercial_use": commercial_use,
        "impact_use": impact_use
    }

def cat_override(c):
    return "" if c == "External Capability" else c

def main():
    if not os.path.exists(INVENTORY_PATH):
        print(f"Error: {INVENTORY_PATH} not found.")
        return

    with open(INVENTORY_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    audited_repos = []
    for line in lines:
        if line.strip().startswith("|") and not line.strip().startswith("| #") and not line.strip().startswith("| :---"):
            parts = [p.strip() for p in line.strip().split("|")[1:-1]]
            if len(parts) >= 6:
                index = parts[0]
                match = re.search(r'\[(.*?)\]\((.*?)\)', parts[1])
                repo_name = match.group(1) if match else parts[1]
                url = match.group(2) if match else f"https://github.com/{repo_name}"
                stars_str = parts[2].replace(",", "")
                stars = int(stars_str) if stars_str.isdigit() else 0
                lang = parts[3]
                category = parts[4]
                desc = parts[5]

                audit_item = classify_repo(index, repo_name, url, stars, lang, category, desc)
                audited_repos.append(audit_item)

    # Calculate summary metrics
    summary = {
        "ADOPT": sum(1 for r in audited_repos if r["classification"] == "ADOPT"),
        "ADAPT": sum(1 for r in audited_repos if r["classification"] == "ADAPT"),
        "REFERENCE": sum(1 for r in audited_repos if r["classification"] == "REFERENCE"),
        "IGNORE": sum(1 for r in audited_repos if r["classification"] == "IGNORE"),
    }
    total_stars = sum(r["stars"] for r in audited_repos)

    payload = {
        "metadata": {
            "title": "904 Starred Repositories Capability & Supply Chain Audit",
            "version": "1.0.0",
            "authority": "System Architecture & Reuse-First Mandate (CP-027 / CP-032)",
            "source_inventory": INVENTORY_PATH,
            "total_repositories_audited": len(audited_repos),
            "total_github_stars": total_stars,
            "classification_summary": summary,
            "governing_rules": [
                "Rule 2: Reuse First & Query 904 Starred Repositories",
                "Rule 9: Revenue Gate & Tier-0 Prioritization (< 48h to cash)",
                "Rule 4: Zero Placeholder Architecture"
            ]
        },
        "repositories": audited_repos
    }

    # Write output JSON
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"Wrote {OUTPUT_JSON} ({len(audited_repos)} repositories)")

    # Write output YAML
    with open(OUTPUT_YAML, "w", encoding="utf-8") as f:
        yaml.dump(payload, f, default_flow_style=False, sort_keys=False)
    print(f"Wrote {OUTPUT_YAML}")

    # Mirror to Worldwidebro-Vex data
    os.makedirs(os.path.dirname(VEX_DATA_TARGET), exist_ok=True)
    with open(VEX_DATA_TARGET, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"Mirrored to {VEX_DATA_TARGET}")

    print("\nAUDIT SUMMARY:")
    print(f"Total Repositories: {len(audited_repos)}")
    print(f"Total Stars: {total_stars:,}")
    print(f"ADOPT (Tier-0 Ready / Infrastructure): {summary['ADOPT']}")
    print(f"ADAPT (Vertical Re-skinning Needed): {summary['ADAPT']}")
    print(f"REFERENCE (Architectures & Prompts): {summary['REFERENCE']}")
    print(f"IGNORE (Educational / Non-Enterprise): {summary['IGNORE']}")

if __name__ == "__main__":
    main()
