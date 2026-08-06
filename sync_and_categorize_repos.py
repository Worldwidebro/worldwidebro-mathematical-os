#!/usr/bin/env python3
"""
Sync and Categorize Repositories
Loads 886 owned and 831 starred repositories, applies multi-dimensional 
classification (Category, Phase, Department, Tool Type, Capabilities),
generates a comprehensive markdown map, and syncs them to Supabase.
"""

import os
import json
import re
import urllib.request
import urllib.error
from datetime import datetime

# Load environment variables manually from .env
def load_env():
    env = {}
    env_path = "/Users/acebless/Documents/.env"
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    k, v = line.strip().split('=', 1)
                    env[k] = v
    return env

ENV = load_env()
SUPABASE_URL = ENV.get("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = ENV.get("SUPABASE_KEY", "")

# Rules for categories
CATEGORIES = {
    "AI / RAG Systems": r"(rag|llama_index|embedding|llm|vector|search|retrieval|openai|deepsearch|claude|qwen|fastgpt|ollama|agenticseek|context|searcher)",
    "Agentic Orchestration": r"(agent|langgraph|orchestrat|fabric|agency|crew|autogen|orchestrator|openhands|aider|goose|stagehand|hermes|openagents)",
    "OSINT & Enrichment": r"(osint|maigret|sherlock|instagram|scraper|crawl|social|searcher|background|analyzer|profile|enrich)",
    "Knowledge Graphs": r"(graphify|graph|neo4j|relationship|networkx|graphiti|drawdb|visual)",
    "Monitoring & Observability": r"(prometheus|grafana|loki|sentry|opentelemetry|monitor|alert|observability|tracy|telemetry|log)",
    "DevOps & Infrastructure": r"(kustomize|argo|cd|cilium|k6|pi-hole|docker|kubernetes|terraform|caddy|nginx|cloud|proxy|dns|headscale|syncthing|netbird|server|deploy|backup|tunnel)",
    "Video & Media Generation": r"(ppt|video|whisper|media|audio|speech|tts|voice|ffmpeg|image|comfy|live-cam|transcribe|draw)",
    "Content & Document Processing": r"(doc|pdf|markdown|extract|parse|contract|sign|ocr|text|content-management|cms|document)",
    "Finance & Trading": r"(credit|risk|finance|trading|market|stock|quant|portfolio|ledger|actual|billing|invoice|payment|stripe|ccxt|bloomberg|hedge-fund|tax|investment|arbitrage)",
    "CRM & Pipeline": r"(crm|clickup|contact|hubspot|pipeline|sales|lead|volo|customer)",
    "Development Tools": r"(template|boilerplate|starter|cli|sdk|builder|git|coder|tips|cheat|compiler|parser|mcp|github)",
    "Learning & Training": r"(course|tutorial|learn|guide|skills|education|academy|training|roadmap|interview)"
}

# Mapping Categories to Departments & Lifecycle Phases
CAT_METADATA = {
    "AI / RAG Systems": {"dept": "Product & R&D", "phase": "Discovery"},
    "Agentic Orchestration": {"dept": "Product & R&D", "phase": "Engineering"},
    "OSINT & Enrichment": {"dept": "Operations", "phase": "Discovery"},
    "Knowledge Graphs": {"dept": "Product & R&D", "phase": "Engineering"},
    "Monitoring & Observability": {"dept": "Engineering", "phase": "Learning"},
    "DevOps & Infrastructure": {"dept": "Engineering", "phase": "Engineering"},
    "Video & Media Generation": {"dept": "Product & R&D", "phase": "Revenue"},
    "Content & Document Processing": {"dept": "Legal & Admin", "phase": "Engineering"},
    "Finance & Trading": {"dept": "Finance & HR", "phase": "Revenue"},
    "CRM & Pipeline": {"dept": "Sales & Marketing", "phase": "Revenue"},
    "Development Tools": {"dept": "Engineering", "phase": "Engineering"},
    "Learning & Training": {"dept": "Finance & HR", "phase": "Learning"}
}

# Tool Type classification rules
TOOL_TYPES = {
    "Framework": r"(framework|orchestrat|graph|crew|autogen|langchain|next)",
    "Platform": r"(server|host|db|docker|kubernetes|cloud|caddy|nginx|prometheus|grafana|pocketbase|supabase)",
    "Library": r"(sdk|client|py|js|ts|go-sdk|api|helper|lib)",
    "CLI / Tool": r"(cli|tool|aider|claude-code|git|scanner|cmd)",
    "Boilerplate / Template": r"(template|boilerplate|starter|scaffold|example|sample)"
}

def classify_repo(repo_name, description, topics, language):
    desc = (description or "").lower()
    name_lower = repo_name.lower()
    topics_lower = [t.lower() for t in (topics or [])]
    lang_lower = (language or "").lower()
    combined = f"{name_lower} {desc} {' '.join(topics_lower)} {lang_lower}"

    # 1. Determine Category
    category = "Specialized Utilities"
    for cat, pattern in CATEGORIES.items():
        if re.search(pattern, combined):
            category = cat
            break

    # 2. Determine Department & Phase
    meta = CAT_METADATA.get(category, {"dept": "Operations", "phase": "Engineering"})
    dept = meta["dept"]
    phase = meta["phase"]

    # 3. Determine Tool Type
    tool_type = "Application"
    for t_type, pattern in TOOL_TYPES.items():
        if re.search(pattern, combined):
            tool_type = t_type
            break

    # 4. Extract specific technical capabilities
    capabilities = []
    
    # Core technical keywords
    tech_keywords = {
        "vector search": r"(vector|embedding|cosine|similarity)",
        "speech-to-text": r"(whisper|transcribe|speech-to-text|voice)",
        "text-to-speech": r"(tts|speech-synthesis|fish-speech)",
        "web scraping": r"(scrape|crawl|spider|beautifulsoup|scrapy|firecrawl)",
        "workflow automation": r"(n8n|temporal|kestra|workflow|activepieces)",
        "visual analytics": r"(grafana|dashboard|visualize|chart|plot)",
        "e-signature": r"(docuseal|sign|signature)",
        "order dispatch": r"(dispatch|courier|routing)",
        "credit scoring": r"(credit|risk|loan|score)",
        "multi-agent logic": r"(multi-agent|swarm|orchestration|agentic)",
        "container orchestration": r"(kubernetes|k8s|docker-compose|swarm)",
        "secrets management": r"(vault|infisical|secrets)",
        "database storage": r"(postgres|mysql|sqlite|nosql|neo4j|qdrant|chroma)",
        "ci/cd pipelines": r"(github-actions|argo|jenkins|pipeline)"
    }
    
    for cap, pattern in tech_keywords.items():
        if re.search(pattern, combined):
            capabilities.append(cap)
            
    return category, phase, dept, tool_type, capabilities

def sync_repos():
    print("🚀 Starting Repository Categorization and Sync...")
    
    # Load files
    owned_path = "/Users/acebless/Documents/scratch_owned_repos.json"
    starred_path = "/Users/acebless/Documents/scratch_starred_repos.json"
    
    if not os.path.exists(owned_path) or not os.path.exists(starred_path):
        print("❌ Error: JSON source files not found. Run fetching commands first.")
        return

    with open(owned_path) as f:
        owned_data = json.load(f)
    with open(starred_path) as f:
        starred_data = json.load(f)

    print(f"📊 Loaded {len(owned_data)} owned and {len(starred_data)} starred repos.")

    all_records = []
    categorized_by_cat = {}

    # Process Owned
    for r in owned_data:
        name = r["name"]
        desc = r.get("description", "")
        lang = r.get("primaryLanguage", {}).get("name", "") if r.get("primaryLanguage") else ""
        topics = r.get("repositoryTopics", []) or []
        url = r.get("url", f"https://github.com/Worldwidebro/{name}")
        stars = r.get("stargazerCount", 0)
        
        category, phase, dept, tool_type, capabilities = classify_repo(name, desc, topics, lang)
        
        # Format tags to append to capabilities
        db_capabilities = list(capabilities)
        db_capabilities.append(f"category:{category}")
        db_capabilities.append(f"phase:{phase}")
        db_capabilities.append(f"dept:{dept}")
        db_capabilities.append(f"tool:{tool_type}")

        # Heuristic maturity
        maturity = "production" if name in ['LightRAG', 'langgraph', 'prometheus', 'grafana'] else "beta"

        # Heuristic integration days
        effort_map = {"low": 3, "medium": 7, "high": 14}
        effort = "medium"
        if len(capabilities) <= 1: effort = "low"
        elif len(capabilities) >= 4: effort = "high"
        
        record = {
            "repo_id": name,
            "name": name,
            "github_url": url,
            "owner": "Worldwidebro",
            "purpose": desc or f"Venture software for {name}",
            "description": desc or f"Venture repository for {name}",
            "maturity": maturity,
            "language": lang or "unknown",
            "capabilities": db_capabilities,
            "stack": [lang.lower()] if lang else ["unknown"],
            "business_use_cases": [f"{category} business functionality"],
            "integration_effort": effort,
            "estimated_integration_days": effort_map[effort],
            "github_stars": stars,
            "repo_type": "owned",
            "verification_status": "verified"
        }
        all_records.append(record)
        
        # Organize for markdown report
        if category not in categorized_by_cat:
            categorized_by_cat[category] = []
        categorized_by_cat[category].append((name, "owned", desc, phase, dept, tool_type, capabilities))

    # Process Starred
    for r in starred_data:
        full_name = r["full_name"]
        name = r["name"]
        desc = r.get("description", "")
        lang = r.get("language", "")
        topics = r.get("topics", []) or []
        url = r.get("html_url", "")
        stars = r.get("stargazers_count", 0)
        owner = r.get("owner", {}).get("login", "") if r.get("owner") else ""
        
        category, phase, dept, tool_type, capabilities = classify_repo(name, desc, topics, lang)
        
        db_capabilities = list(capabilities)
        db_capabilities.append(f"category:{category}")
        db_capabilities.append(f"phase:{phase}")
        db_capabilities.append(f"dept:{dept}")
        db_capabilities.append(f"tool:{tool_type}")

        maturity = "mature" if stars >= 5000 else ("production" if stars >= 1000 else "beta")
        
        effort_map = {"low": 3, "medium": 7, "high": 14}
        effort = "medium"
        if len(capabilities) <= 1: effort = "low"
        elif len(capabilities) >= 4: effort = "high"

        record = {
            "repo_id": full_name,  # Avoid conflicts with owner prefix
            "name": name,
            "github_url": url,
            "owner": owner,
            "purpose": desc or f"Reference software: {name}",
            "description": desc or f"Starred repository: {full_name}",
            "maturity": maturity,
            "language": lang or "unknown",
            "capabilities": db_capabilities,
            "stack": [lang.lower()] if lang else ["unknown"],
            "business_use_cases": [f"{category} utility"],
            "integration_effort": effort,
            "estimated_integration_days": effort_map[effort],
            "github_stars": stars,
            "repo_type": "starred",
            "verification_status": "verified"
        }
        all_records.append(record)

        if category not in categorized_by_cat:
            categorized_by_cat[category] = []
        categorized_by_cat[category].append((full_name, "starred", desc, phase, dept, tool_type, capabilities))

    # 3. Generate Markdown Catalog REPOS-ORGANIZATION-MAP.md
    print("📝 Generating REPOS-ORGANIZATION-MAP.md...")
    md_content = []
    md_content.append("# 🗺️ REPOSITORY ORGANIZATION & CAPABILITY MAP")
    md_content.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}  ")
    md_content.append(f"**Total Tracked Repositories:** {len(all_records)} ({len(owned_data)} Owned, {len(starred_data)} Starred)  ")
    md_content.append("This document indexes all available capabilities across the business departments, venture lifecycle phases, and tool classifications to prevent custom file creation and enable drag-and-drop system wiring.")
    md_content.append("\n---")
    
    # Department Summary Table
    md_content.append("\n## 🏢 CLASSIFICATION BY BUSINESS DEPARTMENT")
    md_content.append("| Department | Core Phase | Representative Repositories | Key Capabilities |")
    md_content.append("|---|---|---|---|")
    depts_repos = {}
    for r in all_records:
        dept = [c.split(":")[1] for c in r["capabilities"] if c.startswith("dept:")][0]
        phase = [c.split(":")[1] for c in r["capabilities"] if c.startswith("phase:")][0]
        if dept not in depts_repos:
            depts_repos[dept] = {"phase": phase, "repos": [], "caps": set()}
        depts_repos[dept]["repos"].append(r["name"])
        for cap in r["capabilities"]:
            if not cap.startswith(("category:", "phase:", "dept:", "tool:")):
                depts_repos[dept]["caps"].add(cap)

    for dept, data in sorted(depts_repos.items()):
        repos_sample = ", ".join(sorted(list(set(data["repos"])))[:4]) + "..."
        caps_sample = ", ".join(sorted(list(data["caps"]))[:3]) or "general utilities"
        md_content.append(f"| **{dept}** | {data['phase']} | {repos_sample} | {caps_sample} |")

    # Lifecycle Phase breakdown
    md_content.append("\n## 🔄 CLASSIFICATION BY VENTURE LIFECYCLE PHASE")
    md_content.append("| Lifecycle Phase | Description | Key Categories | Repos Count |")
    md_content.append("|---|---|---|---|")
    phases_counts = {}
    phases_cats = {}
    for r in all_records:
        phase = [c.split(":")[1] for c in r["capabilities"] if c.startswith("phase:")][0]
        cat = [c.split(":")[1] for c in r["capabilities"] if c.startswith("category:")][0]
        phases_counts[phase] = phases_counts.get(phase, 0) + 1
        if phase not in phases_cats:
            phases_cats[phase] = set()
        phases_cats[phase].add(cat)

    phase_descriptions = {
        "Discovery": "Market validation, intelligence gathering, OSINT research, and lead sourcing.",
        "Engineering": "Platform coding, database structuring, orchestration, infrastructure deployment.",
        "Revenue": "Monetization, financial trading, invoicing/billing, video/media marketing.",
        "Learning": "System monitoring, metrics collection, telemetry analytics, and training loops."
    }

    for phase in ["Discovery", "Engineering", "Revenue", "Learning"]:
        desc = phase_descriptions.get(phase, "")
        cats = ", ".join(sorted(list(phases_cats.get(phase, []))))
        count = phases_counts.get(phase, 0)
        md_content.append(f"| **{phase}** | {desc} | {cats} | {count} |")

    # Detailed Categories
    md_content.append("\n## 📚 DETAILED CATEGORY INDEX")
    for cat, repos in sorted(categorized_by_cat.items()):
        md_content.append(f"\n### {cat} ({len(repos)} Repositories)")
        md_content.append("| Repository / Path | Type | Department | Phase | Tool Type | Key Capabilities |")
        md_content.append("|---|---|---|---|---|---|")
        
        # Sort so owned come first, then starred, and limited to showing top 15 in details to avoid bloating markdown
        repos_sorted = sorted(repos, key=lambda x: (x[1] != 'owned', x[0]))
        for r_name, r_type, desc, phase, dept, tool_type, caps in repos_sorted[:15]:
            type_tag = "🔵 Owned" if r_type == "owned" else "⭐ Starred"
            caps_str = ", ".join(caps) if caps else "utility"
            md_content.append(f"| `{r_name}` | {type_tag} | {dept} | {phase} | {tool_type} | {caps_str} |")
        if len(repos) > 15:
            md_content.append(f"| *... and {len(repos) - 15} more repositories* | | | | | |")

    # Write Map
    with open("/Users/acebless/Documents/REPOS-ORGANIZATION-MAP.md", "w") as f:
        f.write("\n".join(md_content))
    print("✅ Created /Users/acebless/Documents/REPOS-ORGANIZATION-MAP.md")

    # 4. Sync/Upload to Supabase
    if not SUPABASE_KEY:
        print("⚠️ SUPABASE_KEY not set. Skipping database sync.")
        return

    print(f"📤 Syncing {len(all_records)} repositories to Supabase in batches...")
    batch_size = 100
    success_count = 0
    
    for i in range(0, len(all_records), batch_size):
        batch = all_records[i:i + batch_size]
        url = f"{SUPABASE_URL}/rest/v1/repos"
        
        # Prepare PostgREST bulk upsert with on_conflict query param
        req = urllib.request.Request(
            f"{url}?on_conflict=repo_id",
            data=json.dumps(batch).encode(),
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
                "Prefer": "resolution=merge-duplicates"
            },
            method="POST"
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                if response.status in [200, 201, 204]:
                    success_count += len(batch)
                    print(f"   ✓ Synced batch {i//batch_size + 1}: {success_count}/{len(all_records)} repos...")
        except urllib.error.HTTPError as e:
            print(f"   ❌ Batch {i//batch_size + 1} failed: {e.code} {e.reason}")
            print(f"      Response: {e.read().decode()[:300]}")
        except Exception as e:
            print(f"   ❌ Batch {i//batch_size + 1} failed: {e}")

    print(f"✅ Sync complete. Successfully loaded {success_count}/{len(all_records)} records into Supabase.")

if __name__ == "__main__":
    sync_repos()
