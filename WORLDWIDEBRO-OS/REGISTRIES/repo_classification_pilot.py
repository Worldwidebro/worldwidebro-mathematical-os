#!/usr/bin/env python3
"""
Repository Intelligence — Level 2 (Registry) + Level 3 (Intelligence) pilot.

Deterministic classification using repo_vocabulary.json.
No API required for pilot pass; optional --llm for enrichment later.

Usage:
  python3 repo_classification_pilot.py --pilot 100
  python3 repo_classification_pilot.py --all
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any

REGISTRY_DIR = Path(__file__).resolve().parent
DOCUMENTS = REGISTRY_DIR.parent.parent  # ~/Documents

VOCAB_PATH = REGISTRY_DIR / "repo_vocabulary.json"
OWNED_PATH = DOCUMENTS / "WORLDWIDEBRO-OS/04-OPERATIONS/The office/repos.json"
STARRED_PATH = DOCUMENTS / "repos-index.json"

OUTPUT_CSV = REGISTRY_DIR / "repository_registry_pilot.csv"
OUTPUT_JSON = REGISTRY_DIR / "repository_registry_pilot.json"
OUTPUT_EDGES = REGISTRY_DIR / "repository_graph_edges_pilot.csv"

# Map raw topic/capability tokens → controlled vocabulary capabilities
RAW_CAP_MAP: dict[str, str] = {
    "ai": "AI",
    "ai-agents": "Agents",
    "agents": "Agents",
    "apis": "API",
    "api": "API",
    "automation": "Automation",
    "auth": "Authentication",
    "billing": "Payments",
    "payments": "Payments",
    "storage": "Storage",
    "database": "Storage",
    "messaging": "Messaging",
    "notifications": "Notifications",
    "analytics": "Analytics",
    "monitoring": "Monitoring",
    "deployment": "Deployment",
    "docker": "Deployment",
    "kubernetes": "Deployment",
    "security": "Security",
    "crm": "CRM",
    "marketplace": "Marketplace",
    "rag": "RAG",
    "vector": "RAG",
    "search": "Search",
    "scheduling": "Scheduling",
    "dispatch": "Dispatch",
    "routing": "Routing",
    "workflows": "Workflows",
    "data-flow": "Automation",
    "deepagents": "Agents",
    "chatgpt": "AI",
    "cli": "API",
}

CAPABILITY_SIGNALS: list[tuple[str, str]] = [
    (r"auth|oauth|jwt|login|identity", "Authentication"),
    (r"payment|stripe|billing|invoice|subscription", "Payments"),
    (r"search|elasticsearch|algolia|vector", "Search"),
    (r"storage|s3|blob|file-system|minio", "Storage"),
    (r"messag|slack|email|sms|twilio|notification", "Messaging"),
    (r"analytics|metric|dashboard|grafana|observability", "Analytics"),
    (r"automation|workflow|n8n|zapier|trigger", "Automation"),
    (r"agent|mcp|langgraph|crew|autogen", "Agents"),
    (r"rag|embedding|vector|chromadb|qdrant|weaviate|llamaindex", "RAG"),
    (r"llm|openai|anthropic|inference|gpt", "AI"),
    (r"monitor|logging|sentry|datadog|apm", "Monitoring"),
    (r"schedul|cron|calendar|dispatch", "Scheduling"),
    (r"deploy|docker|kubernetes|k8s|ci/cd|terraform|coolify", "Deployment"),
    (r"security|encrypt|vault|compliance|hipaa", "Security"),
    (r"crm|hubspot|salesforce|pipeline", "CRM"),
    (r"marketplace|commerce|ecommerce|shop", "Marketplace"),
    (r"route|vrp|tsp|gps|maps|geocod", "Routing"),
    (r"dispatch|field-service", "Dispatch"),
    (r"sign|docusign|esign|document-sign", "Digital Signature"),
    (r"video|ffmpeg|stream|media", "Video"),
    (r"knowledge-graph|neo4j|graph", "Knowledge Graph"),
    (r"hrms|staffing|payroll|workforce", "Workflows"),
    (r"test|pytest|jest|e2e", "Testing"),
    (r"api|rest|graphql|grpc", "API"),
    (r"database|postgres|supabase|mysql|mongo|redis", "Storage"),
    (r"content|blog|cms|headless", "Content Generation"),
]

ROLE_SIGNALS: list[tuple[str, str]] = [
    (r"n8n|zapier|airflow|temporal", "Automation"),
    (r"langgraph|crewai|autogen|agent", "Agent"),
    (r"supabase|postgres|prisma|drizzle", "Backend"),
    (r"next\.js|react|vue|svelte|frontend", "Frontend"),
    (r"openbb|financial|trading|arbitrage", "Infrastructure"),
    (r"chromadb|qdrant|weaviate|pgvector|lightrag", "Data"),
    (r"sentry|grafana|datadog|langfuse", "Analytics"),
    (r"stripe|payment|billing", "Revenue Product"),
    (r"venture|marketplace|saas", "Revenue Product"),
    (r"template|boilerplate|starter|cursorrules|skill", "Internal Tool"),
    (r"docker|k8s|terraform|coolify", "Infrastructure"),
]

IDENTITY_SIGNALS: list[tuple[str, str]] = [
    (r"framework|langchain|django|rails", "Framework"),
    (r"sdk|client-lib", "SDK"),
    (r"template|boilerplate|starter", "Template"),
    (r"skill|mcp-server", "Agent Skill"),
    (r"platform|studio|hub", "Platform"),
    (r"marketplace|saas", "Product"),
    (r"lib|library", "Library"),
    (r"api|service", "Service"),
]

CATEGORY_SIGNALS: list[tuple[str, str]] = [
    (r"database|postgres|redis|storage|docker|k8s|terraform|cloud|supabase", "INFRASTRUCTURE"),
    (r"agent|mcp|langgraph|llama|rag|embedding|ai-platform", "PLATFORM"),
    (r"saas|marketplace|portal|app", "PRODUCT"),
    (r"template|prompt|workflow|sop|dataset|skill", "ASSET"),
    (r"venture|revenue", "VENTURE"),
]

OS_LAYER_SIGNALS: list[tuple[str, str]] = [
    (r"auth|identity|oauth", "Identity"),
    (r"rag|wiki|docs|obsidian|knowledge", "Knowledge"),
    (r"memory|context|chromadb", "Memory"),
    (r"agent|mcp|llm|langgraph", "Agent"),
    (r"n8n|workflow|automation|cron", "Automation"),
    (r"slack|email|sms|notification", "Communication"),
    (r"analytics|metric|dashboard|grafana", "Analytics"),
    (r"stripe|payment|billing|invoice", "Finance"),
    (r"docker|k8s|deploy|supabase|postgres", "Infrastructure"),
    (r"security|encrypt|vault", "Security"),
    (r"etl|pipeline|warehouse|vector", "Data"),
    (r"api|graphql|rest", "API"),
    (r"react|next|vue|frontend|ui", "Frontend"),
    (r"express|fastapi|django|backend", "Backend"),
    (r"tensorflow|pytorch|inference|embedding", "AI/ML"),
]


def load_vocab() -> dict[str, Any]:
    with open(VOCAB_PATH, encoding="utf-8") as f:
        return json.load(f)


def normalize_text(*parts: str) -> str:
    return " ".join(p for p in parts if p).lower()


def match_signals(text: str, signals: list[tuple[str, str]]) -> list[str]:
    found: list[str] = []
    for pattern, label in signals:
        if re.search(pattern, text, re.I):
            if label not in found:
                found.append(label)
    return found


def infer_capabilities(text: str, raw_caps: list[str] | None = None) -> list[str]:
    caps = match_signals(text, CAPABILITY_SIGNALS)
    if raw_caps:
        for raw in raw_caps:
            key = raw.strip().lower()
            if key in RAW_CAP_MAP:
                caps.append(RAW_CAP_MAP[key])
            caps.extend(match_signals(raw.replace("-", " "), CAPABILITY_SIGNALS))
    # dedupe preserve order
    seen: set[str] = set()
    out: list[str] = []
    for c in caps:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out[:12]


def infer_category(text: str, capabilities: list[str]) -> str:
    cats = match_signals(text, CATEGORY_SIGNALS)
    if cats:
        return cats[0]
    if "Agents" in capabilities or "RAG" in capabilities:
        return "PLATFORM"
    if "Deployment" in capabilities or "Storage" in capabilities:
        return "INFRASTRUCTURE"
    if "Marketplace" in capabilities or "Payments" in capabilities:
        return "PRODUCT"
    return "ASSET"


def infer_identity(text: str) -> str:
    ids = match_signals(text, IDENTITY_SIGNALS)
    return ids[0] if ids else "Repository"


def infer_roles(text: str, capabilities: list[str]) -> list[str]:
    roles = match_signals(text, ROLE_SIGNALS)
    if "Agents" in capabilities and "Agent" not in roles:
        roles.append("Agent")
    if "Automation" in capabilities and "Automation" not in roles:
        roles.append("Automation")
    return roles[:5] or ["Internal Tool"]


def infer_os_layers(text: str, capabilities: list[str]) -> list[str]:
    layers = match_signals(text, OS_LAYER_SIGNALS)
    cap_to_layer = {
        "Agents": "Agent",
        "RAG": "AI/ML",
        "Automation": "Automation",
        "Analytics": "Analytics",
        "Payments": "Finance",
        "Messaging": "Communication",
    }
    for cap, layer in cap_to_layer.items():
        if cap in capabilities and layer not in layers:
            layers.append(layer)
    return layers[:4] or ["Infrastructure"]


def score_reusability(capabilities: list[str], source: str, venture_count: int) -> int:
    base = min(4 + len(capabilities), 8)
    if source == "owned":
        base += 1
    if venture_count >= 3:
        base += 2
    elif venture_count >= 2:
        base += 1
    return min(base, 10)


def score_revenue(capabilities: list[str], stars: int, category: str) -> int:
    score = 3
    if "Payments" in capabilities or "Marketplace" in capabilities:
        score += 3
    if "SaaS" in capabilities or category == "PRODUCT":
        score += 2
    if stars >= 1000:
        score += 2
    elif stars >= 100:
        score += 1
    return min(score, 10)


def score_strategic(venture_count: int, reusability: int, source: str) -> int:
    score = reusability // 2 + venture_count
    if source == "owned":
        score += 2
    return min(score, 10)


def venture_tier(total: int) -> str:
    if total >= 40:
        return "TIER 1"
    if total >= 30:
        return "TIER 2"
    if total >= 20:
        return "TIER 3"
    return "TIER 4"


def decision_action(
    source: str,
    category: str,
    capabilities: list[str],
    venture_count: int,
    identity: str,
) -> str:
    if identity in ("Template", "Boilerplate") or category == "ASSET":
        if venture_count == 0:
            return "LEARN"
        return "USE"
    if source == "owned" and venture_count >= 1:
        return "FORK+EXTEND" if "Marketplace" in capabilities else "USE"
    if category == "PLATFORM" and venture_count >= 2:
        return "USE"
    if category == "INFRASTRUCTURE" and venture_count >= 2:
        return "USE"
    if stars_heuristic := venture_count:
        if stars_heuristic >= 3:
            return "WRAP"
    if identity == "Agent Skill":
        return "USE"
    if venture_count == 0 and category == "ASSET":
        return "LEARN"
    if venture_count >= 2:
        return "USE"
    return "IGNORE"


def related_ventures(capabilities: list[str], venture_needs: dict[str, list[str]]) -> list[str]:
    matches: list[tuple[str, int]] = []
    cap_set = set(capabilities)
    for venture, needs in venture_needs.items():
        overlap = len(cap_set.intersection(needs))
        min_overlap = 2 if venture == "marketplace-core" else 1
        if overlap >= min_overlap:
            matches.append((venture, overlap))
    matches.sort(key=lambda x: -x[1])
    return [v for v, _ in matches[:6]]


def build_purpose(name: str, description: str, capabilities: list[str]) -> str:
    if description:
        return description.strip()[:240]
    if capabilities:
        return f"{name}: provides {', '.join(capabilities[:4])}"
    return f"{name}: repository asset pending README enrichment"


def normalize_owned(repo: dict[str, Any]) -> dict[str, Any]:
    return {
        "repo_name": repo.get("name", ""),
        "full_name": repo.get("fullName", ""),
        "owner": repo.get("githubOrg", "Worldwidebro"),
        "url": repo.get("url", ""),
        "description": repo.get("description") or "",
        "language": repo.get("language") or "unknown",
        "stars": int(repo.get("stars") or 0),
        "source": "owned",
        "venture_id": repo.get("ventureId") or "",
        "capabilities_raw": [],
        "topics": [],
        "license": "",
        "is_private": repo.get("isPrivate", True),
    }


def normalize_starred(repo: dict[str, Any]) -> dict[str, Any]:
    return {
        "repo_name": repo.get("name", ""),
        "full_name": f"{repo.get('owner', '')}/{repo.get('name', '')}",
        "owner": repo.get("owner", ""),
        "url": repo.get("url", ""),
        "description": "",
        "language": repo.get("language") or "unknown",
        "stars": 0,
        "source": "starred",
        "venture_id": "",
        "capabilities_raw": repo.get("capabilities") or [],
        "topics": repo.get("capabilities") or [],
        "license": "",
        "is_private": False,
    }


def classify_record(raw: dict[str, Any], vocab: dict[str, Any]) -> dict[str, Any]:
    venture_needs = vocab["venture_capability_needs"]
    text = normalize_text(
        raw["repo_name"],
        raw["full_name"],
        raw["description"],
        " ".join(raw.get("capabilities_raw") or []),
        raw.get("venture_id", ""),
    )
    capabilities = infer_capabilities(text, raw.get("capabilities_raw"))
    category = infer_category(text, capabilities)
    identity = infer_identity(text)
    roles = infer_roles(text, capabilities)
    os_layers = infer_os_layers(text, capabilities)
    ventures = related_ventures(capabilities, venture_needs)
    if raw.get("venture_id") and raw["venture_id"] not in ventures:
        ventures.insert(0, raw["venture_id"])

    reusability = score_reusability(capabilities, raw["source"], len(ventures))
    revenue = score_revenue(capabilities, raw["stars"], category)
    strategic = score_strategic(len(ventures), reusability, raw["source"])
    tier_score = reusability + revenue + strategic + len(ventures) * 2
    tier = venture_tier(tier_score)
    action = decision_action(raw["source"], category, capabilities, len(ventures), identity)
    is_candidate = "YES" if revenue >= 7 and category in ("PRODUCT", "PLATFORM") else "NO"
    est_mrr = revenue * 2 if is_candidate == "YES" else 0

    purpose = build_purpose(raw["repo_name"], raw["description"], capabilities)
    tech_stack = [raw["language"]] if raw["language"] != "unknown" else []
    tech_stack.extend(
        t
        for t in ["Docker", "PostgreSQL", "TypeScript", "Python", "React", "Supabase"]
        if t.lower() in text and t not in tech_stack
    )

    graph_edges: list[str] = []
    for v in ventures[:3]:
        graph_edges.append(f"{raw['repo_name']}|POWERS|{v}")
    for cap in capabilities[:2]:
        graph_edges.append(f"{raw['repo_name']}|ENABLES|{cap}")

    return {
        "repo_name": raw["repo_name"],
        "full_name": raw["full_name"],
        "source": raw["source"],
        "url": raw["url"],
        "owner": raw["owner"],
        "language": raw["language"],
        "stars": raw["stars"],
        "venture_id_linked": raw.get("venture_id") or "",
        "intelligence_level": "L2+L3",
        "purpose": purpose,
        "identity_type": identity,
        "category": category,
        "venture_studio_role": roles[0] if roles else "Internal Tool",
        "roles": ";".join(roles),
        "capabilities": ";".join(capabilities),
        "dependencies": "",
        "tech_stack": ";".join(tech_stack),
        "os_layers": ";".join(os_layers),
        "reusability_score": reusability,
        "revenue_potential": revenue,
        "strategic_value": strategic,
        "venture_tier": tier,
        "decision_action": action,
        "related_ventures": ";".join(ventures),
        "related_repositories": "",
        "graph_edges": ";".join(graph_edges),
        "is_venture_candidate": is_candidate,
        "estimated_mrr_k": est_mrr,
        "confidence": 7 if raw["source"] == "owned" else 6,
        "pilot_flag": "YES",
    }


def select_pilot(owned: list[dict], starred: list[dict], limit: int) -> list[dict]:
    owned_norm = [normalize_owned(r) for r in owned]
    starred_norm = [normalize_starred(r) for r in starred]

    owned_linked = [r for r in owned_norm if r.get("venture_id")]
    owned_rest = [r for r in owned_norm if not r.get("venture_id")]
    starred_sorted = sorted(
        starred_norm,
        key=lambda r: len(r.get("capabilities_raw") or []),
        reverse=True,
    )

    half = limit // 2
    selected: list[dict] = []
    seen: set[str] = set()

    def add(batch: list[dict], cap: int | None = None) -> None:
        count = 0
        for item in batch:
            if cap is not None and count >= cap:
                return
            key = item["full_name"] or item["repo_name"]
            if key in seen:
                continue
            seen.add(key)
            selected.append(item)
            count += 1

    # Balanced pilot: 50% owned (venture-linked first), 50% high-signal starred
    add(owned_linked, half // 2 + 10)
    add(owned_rest, half - (half // 2 + 10))
    add(starred_sorted, half)

    return selected[:limit]


def load_inventories() -> tuple[list[dict], list[dict]]:
    with open(OWNED_PATH, encoding="utf-8") as f:
        owned = json.load(f)
    with open(STARRED_PATH, encoding="utf-8") as f:
        starred_data = json.load(f)
    starred = starred_data.get("repos", starred_data)
    return owned, starred


def write_outputs(rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)

    edge_rows: list[dict[str, str]] = []
    for row in rows:
        for edge in row.get("graph_edges", "").split(";"):
            if not edge:
                continue
            parts = edge.split("|")
            if len(parts) == 3:
                edge_rows.append(
                    {
                        "source_repo": parts[0],
                        "relationship": parts[1],
                        "target": parts[2],
                        "source_url": row.get("url", ""),
                    }
                )
    with open(OUTPUT_EDGES, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["source_repo", "relationship", "target", "source_url"]
        )
        writer.writeheader()
        writer.writerows(edge_rows)


def print_summary(rows: list[dict[str, Any]]) -> None:
    tiers: dict[str, int] = {}
    actions: dict[str, int] = {}
    for r in rows:
        tiers[r["venture_tier"]] = tiers.get(r["venture_tier"], 0) + 1
        actions[r["decision_action"]] = actions.get(r["decision_action"], 0) + 1
    print(f"\nClassified: {len(rows)} repos")
    print(f"By tier: {tiers}")
    print(f"By action: {actions}")
    print(f"CSV:  {OUTPUT_CSV}")
    print(f"JSON: {OUTPUT_JSON}")
    print(f"Edges: {OUTPUT_EDGES}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Repository Intelligence pilot classifier")
    parser.add_argument("--pilot", type=int, default=100, help="Pilot sample size")
    parser.add_argument("--all", action="store_true", help="Classify full inventory")
    args = parser.parse_args()

    vocab = load_vocab()
    owned, starred = load_inventories()
    print(f"Loaded {len(owned)} owned + {len(starred)} starred repos")

    if args.all:
        raw_batch = [normalize_owned(r) for r in owned] + [
            normalize_starred(r) for r in starred
        ]
        # dedupe by full_name
        seen: set[str] = set()
        batch: list[dict] = []
        for item in raw_batch:
            key = item["full_name"] or item["repo_name"]
            if key not in seen:
                seen.add(key)
                batch.append(item)
    else:
        batch = select_pilot(owned, starred, args.pilot)

    rows = [classify_record(item, vocab) for item in batch]
    write_outputs(rows)
    print_summary(rows)


if __name__ == "__main__":
    main()
