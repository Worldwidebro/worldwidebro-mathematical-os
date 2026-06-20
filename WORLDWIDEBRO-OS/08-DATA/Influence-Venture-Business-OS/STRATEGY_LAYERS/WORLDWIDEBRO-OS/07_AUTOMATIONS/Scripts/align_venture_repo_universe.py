#!/usr/bin/env python3
"""
Align venture catalog (629 UUID) with GitHub owned/starred repos and Supabase.

Refreshes:
  - venture-hub/registries/github_owned.csv
  - venture-hub/registries/github_starred.csv
  - venture-hub/registries/venture_uuid_slug_bridge.csv
  - venture-hub/docs/VENTURE_STARRED_OWNED_REPOS.csv
  - WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv
  - ventures_enriched_option_b.json (629 ventures)
  - ventures_dependencies.json
  - .planning/venture-hub-alignment.json
  - ventures_master_with_sectors.csv (712 master + UUIDs)
  - AUTO-ALIGNMENT-712.json
  - WORLDWIDEBRO-712-UNIFIED.csv
  - VENTURE-ID-CROSSWALK.csv

Syncs Supabase `repositories` table (owned + starred).
"""

from __future__ import annotations

import csv
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from graph_entity_match import (
    alignment_status,
    count_graph_entities,
    load_kg_venture_ids,
    load_merged_slug_index,
    required_repo_satisfied,
)

ROOT = Path(__file__).resolve().parents[3]
load_dotenv(ROOT / ".env")
load_dotenv(ROOT / "venture-hub" / ".env.local")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_ORG = os.getenv("GITHUB_ORG", "Worldwidebro")
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

def _resolve_classification_csv() -> Path:
    candidates = [
        ROOT / "ventures_classification_final.csv",
        ROOT / "WORLDWIDEBRO-OS" / "08_RESEARCH" / "Ventures-Data" / "ventures_classification_final.csv",
        ROOT / "venture-hub" / "ventures-classification.csv",
    ]
    for path in candidates:
        if path.exists():
            return path
    return candidates[0]


CLASSIFICATION_CSV = _resolve_classification_csv()
MASTER_CSV = ROOT / "venture-hub" / "ventures-master.csv"
OWNED_REGISTRY = ROOT / "venture-hub" / "registries" / "github_owned.csv"
STARRED_REGISTRY = ROOT / "venture-hub" / "registries" / "github_starred.csv"
BRIDGE_CSV = ROOT / "venture-hub" / "registries" / "venture_uuid_slug_bridge.csv"
COMBINED_CSV = ROOT / "venture-hub" / "docs" / "VENTURE_STARRED_OWNED_REPOS.csv"
ALIGNMENT_CSV = ROOT / "WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv"
STARRED_CAPS_CSV = ROOT / "starred_repos_with_capabilities.csv"
def _resolve_data_file(name: str) -> Path:
    candidates = [
        ROOT / name,
        ROOT / "WORLDWIDEBRO-OS" / "08_RESEARCH" / "Ventures-Data" / name,
    ]
    for path in candidates:
        if path.exists():
            return path
    return candidates[0]


ENRICHED_JSON = _resolve_data_file("ventures_enriched_option_b.json")
DEPENDENCIES_JSON = _resolve_data_file("ventures_dependencies.json")
PLANNING_ALIGNMENT = ROOT / ".planning" / "venture-hub-alignment.json"
GRAPH_DATA = ROOT / ".planning" / "graph-data.json"
FOUR_LAYERS_CSV = ROOT / "WORLDWIDEBRO-REPOS-4LAYERS.csv"
THE_OFFICE_EXPORT = ROOT / "The office" / "the-office-export.csv"
MASTER_WITH_SECTORS_CSV = ROOT / "ventures_master_with_sectors.csv"
AUTO_ALIGNMENT_712_JSON = ROOT / "AUTO-ALIGNMENT-712.json"
UNIFIED_712_CSV = ROOT / "WORLDWIDEBRO-712-UNIFIED.csv"
CROSSWALK_CSV = ROOT / "VENTURE-ID-CROSSWALK.csv"
VENTURES_DATA_DIR = ROOT / "WORLDWIDEBRO-OS" / "08_RESEARCH" / "Ventures-Data"

MASTER_SECTOR_MAP = {
    "e-commerce": "market",
    "operations": "infra",
    "technology": "devtools",
    "specialized": "market",
    "emerging": "ai",
    "community": "market",
    "financial": "fintech",
    "education": "edtech",
    "beauty-wellness": "beauty",
    "food-hospitality": "market",
    "logistics-transport": "infra",
    "software-technology": "devtools",
    "fitness-sports": "market",
    "professional-services": "market",
    "media-content": "market",
    "construction": "con",
    "education-training": "edtech",
    "real-estate": "re",
}

GH_HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

SECTOR_CAPABILITIES: Dict[str, List[str]] = {
    "hrms": ["api", "database", "authentication", "dashboard", "monitoring", "security"],
    "ai": ["api", "database", "knowledge-graph", "monitoring"],
    "con": ["api", "database", "construction", "workspace", "dashboard"],
    "devtools": ["api", "database", "authentication", "dashboard", "monitoring"],
    "edtech": ["api", "database", "dashboard", "workspace", "authentication"],
    "fintech": ["api", "database", "authentication", "security", "monitoring", "payment"],
    "financial": ["api", "database", "authentication", "security", "monitoring", "payment"],
    "health": ["api", "database", "security", "monitoring", "authentication"],
    "infra": ["api", "database", "monitoring", "security", "authentication"],
    "market": ["api", "database", "dashboard", "portfolio", "authentication"],
    "re": ["api", "database", "dashboard", "portfolio", "workspace"],
    "pitch": ["api", "database", "pitch", "dashboard", "portfolio"],
    "simulation": ["api", "database", "simulation", "knowledge-graph"],
    "beauty-wellness": ["api", "database", "dashboard", "authentication", "monitoring"],
    "community": ["api", "database", "dashboard", "authentication"],
    "operations": ["api", "database", "monitoring", "workflow"],
}

SECTOR_ALIASES = {
    "fintech": "financial",
    "healthcare": "health",
    "marketplace": "market",
}

# Ventures without master/4layers rows — map UUID to primary owned slug
VENTURE_OWNED_ALIASES: Dict[str, str] = {
    "4f3bc116-b77f-4b3a-a9f6-a3327a21762d": "et-003-platform",  # SkillForge
    "b9c1c9a3-5927-480c-857d-6b99be35254b": "enhanced-cursor-rules",
    "dd78dc7f-ab6a-4c1f-9405-b0cbd827ae0d": "ft-001-core-ledger",  # QuantumLedger
}

JUNK_SLUG_SUFFIXES = ("-src", "-dist", "-public", "-node_modules", "node_modules")
JUNK_SLUGS = {"fi-src", "fi-dist", "fi-public", "fi-node_modules"}

DATA_STACK = "venture-hub;the-office;supabase;graphify-rag;llamaindex"
VENTURE_SLUG_RE = re.compile(r"^[a-z]{2,6}-\d{3}-[a-z0-9-]+$", re.I)
CODE_PREFIX_RE = re.compile(r"\b([A-Z]{2,6}-\d{3})\b")


def normalize_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (name or "").lower())


def slug_from_github_url(url: str) -> str:
    if not url:
        return ""
    path = urlparse(url.strip()).path.strip("/")
    parts = path.split("/")
    return parts[-1].lower() if parts else ""


def github_url_for_slug(slug: str, owned_urls: Dict[str, str]) -> str:
    slug = (slug or "").strip()
    if not slug:
        return ""
    return owned_urls.get(slug) or f"https://github.com/{GITHUB_ORG}/{slug}"


def build_owned_url_index(owned_registry: List[dict]) -> Dict[str, str]:
    index: Dict[str, str] = {}
    for row in owned_registry:
        slug = (row.get("name") or "").strip()
        url = (row.get("url") or "").strip()
        if slug and url:
            index[slug] = url
    return index


def build_starred_url_index(starred_registry: List[dict]) -> Dict[str, str]:
    index: Dict[str, str] = {}
    for row in starred_registry:
        url = (row.get("url") or "").strip()
        if not url:
            continue
        full = (row.get("name_with_owner") or "").strip()
        name = (row.get("name") or "").strip()
        if full:
            index[full.lower()] = url
        if name:
            index[name.lower()] = url
    return index


def github_url_for_starred(full_name: str, starred_urls: Optional[Dict[str, str]] = None) -> str:
    full_name = (full_name or "").strip()
    if not full_name:
        return ""
    if full_name.startswith("http"):
        return full_name
    if "/" in full_name:
        return f"https://github.com/{full_name}"
    if starred_urls:
        hit = starred_urls.get(full_name.lower())
        if hit:
            return hit
    return f"https://github.com/{full_name}"


def starred_links_for_venture(
    uid: str,
    sector: str,
    venture_name: str,
    combined_by_uuid: Dict[str, dict],
    starred_caps: Dict[str, dict],
    starred_registry: List[dict],
    four_layers_starred: Dict[str, List[str]],
    starred_urls: Dict[str, str],
) -> Tuple[int, str, str]:
    """Return starred count, owner/name list, and semicolon-separated GitHub URLs."""
    if uid and uid in combined_by_uuid:
        starred_str = combined_by_uuid[uid].get("starred_repos", "")
        full_names = [s.strip() for s in starred_str.split(";") if s.strip()]
    elif uid:
        caps = infer_capabilities(sector, venture_name)
        cap_matches = match_starred_repos(caps, starred_caps, starred_registry)
        starred_matches = merge_starred_from_four_layers(uid, four_layers_starred, cap_matches)
        full_names = [m[0] for m in starred_matches]
        starred_str = ";".join(full_names)
    else:
        full_names = []
        starred_str = ""

    urls = ";".join(github_url_for_starred(name, starred_urls) for name in full_names)
    return len(full_names), starred_str, urls


def infer_capabilities(sector: str, venture_name: str) -> List[str]:
    sector_key = SECTOR_ALIASES.get((sector or "").lower(), (sector or "market").lower())
    caps = set(SECTOR_CAPABILITIES.get(sector_key, ["api", "database"]))
    name_lower = (venture_name or "").lower()
    keyword_map = {
        "payment": ["payment", "billing", "invoice", "credit", "bank", "finance"],
        "knowledge-graph": ["rag", "knowledge", "semantic", "intelligence"],
        "dashboard": ["dashboard", "analytics", "tracker", "monitor"],
        "portfolio": ["portfolio", "marketplace", "shop", "store"],
        "security": ["security", "compliance", "audit"],
    }
    for cap, keywords in keyword_map.items():
        if any(k in name_lower for k in keywords):
            caps.add(cap)
    caps.update({"api", "database"})
    return sorted(caps)


def gh_paginate(url: str, params: Optional[dict] = None) -> List[dict]:
    items: List[dict] = []
    page = 1
    params = dict(params or {})
    while True:
        params["page"] = page
        resp = requests.get(url, headers=GH_HEADERS, params=params, timeout=60)
        if resp.status_code != 200:
            raise RuntimeError(f"GitHub API {resp.status_code} for {url}: {resp.text[:300]}")
        batch = resp.json()
        if not batch:
            break
        items.extend(batch)
        if len(batch) < params.get("per_page", 100):
            break
        page += 1
    return items


def fetch_owned_repos() -> List[dict]:
    """Fetch all repos owned by the authenticated user (includes private)."""
    print("Fetching authenticated owned repos...")
    return gh_paginate(
        "https://api.github.com/user/repos",
        {"per_page": 100, "affiliation": "owner"},
    )


def fetch_starred_repos() -> List[dict]:
    print("Fetching starred repos...")
    starred = gh_paginate("https://api.github.com/user/starred", {"per_page": 100})
    # Cross-check total via GraphQL (handles pagination edge cases)
    try:
        q = """
        query { viewer { starredRepositories { totalCount } } }
        """
        resp = requests.post(
            "https://api.github.com/graphql",
            headers=GH_HEADERS,
            json={"query": q},
            timeout=30,
        )
        if resp.status_code == 200:
            total = (
                resp.json()
                .get("data", {})
                .get("viewer", {})
                .get("starredRepositories", {})
                .get("totalCount")
            )
            if total is not None and total != len(starred):
                print(f"  Warning: REST starred={len(starred)} vs GraphQL totalCount={total}")
    except Exception as exc:
        print(f"  GraphQL starred count check skipped: {exc}")
    return starred


def write_owned_registry(repos: List[dict]) -> Set[str]:
    OWNED_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "name_with_owner", "name", "description", "private", "fork", "archived",
        "language", "stars", "forks", "created_at", "updated_at", "pushed_at",
        "url", "homepage", "topics",
    ]
    owned_slugs: Set[str] = set()
    with OWNED_REGISTRY.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for r in repos:
            slug = r["name"].lower()
            owned_slugs.add(slug)
            topics = "|".join(r.get("topics") or [])
            writer.writerow({
                "name_with_owner": r.get("full_name", f"{GITHUB_ORG}/{r['name']}"),
                "name": r["name"],
                "description": (r.get("description") or "").replace("\n", " "),
                "private": str(r.get("private", False)).lower(),
                "fork": str(r.get("fork", False)).lower(),
                "archived": str(r.get("archived", False)).lower(),
                "language": r.get("language") or "",
                "stars": r.get("stargazers_count", 0),
                "forks": r.get("forks_count", 0),
                "created_at": r.get("created_at") or "",
                "updated_at": r.get("updated_at") or "",
                "pushed_at": r.get("pushed_at") or "",
                "url": r.get("html_url") or "",
                "homepage": r.get("homepage") or "",
                "topics": topics,
            })
    print(f"  Wrote {len(repos)} owned repos -> {OWNED_REGISTRY}")
    return owned_slugs


def write_starred_registry(repos: List[dict]) -> None:
    STARRED_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "name_with_owner", "name", "owner", "description", "language", "stars",
        "forks", "created_at", "updated_at", "pushed_at", "url", "topics",
    ]
    with STARRED_REGISTRY.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for r in repos:
            owner = (r.get("owner") or {}).get("login", "")
            topics = "|".join(r.get("topics") or [])
            writer.writerow({
                "name_with_owner": r.get("full_name", f"{owner}/{r['name']}"),
                "name": r["name"],
                "owner": owner,
                "description": (r.get("description") or "").replace("\n", " "),
                "language": r.get("language") or "",
                "stars": r.get("stargazers_count", 0),
                "forks": r.get("forks_count", 0),
                "created_at": r.get("created_at") or "",
                "updated_at": r.get("updated_at") or "",
                "pushed_at": r.get("pushed_at") or "",
                "url": r.get("html_url") or "",
                "topics": topics,
            })
    print(f"  Wrote {len(repos)} starred repos -> {STARRED_REGISTRY}")


def load_csv(path: Path) -> List[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def mirror_to_ventures_data(path: Path) -> None:
    """Keep Documents root + WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data in sync."""
    if not path.exists() or not path.is_file():
        return
    VENTURES_DATA_DIR.mkdir(parents=True, exist_ok=True)
    dest = VENTURES_DATA_DIR / path.name
    if dest.resolve() != path.resolve():
        dest.write_bytes(path.read_bytes())


def load_starred_capabilities() -> Dict[str, dict]:
    if not STARRED_CAPS_CSV.exists():
        return {}
    caps_by_key: Dict[str, dict] = {}
    for row in load_csv(STARRED_CAPS_CSV):
        name = row.get("name", "").strip()
        owner = row.get("owner", "").strip()
        full = f"{owner}/{name}" if owner and name else name
        caps = [c.strip() for c in (row.get("capabilities") or "").split("|") if c.strip()]
        caps_by_key[name.lower()] = {
            "name": name,
            "owner": owner,
            "full_name": full,
            "capabilities": caps,
            "url": row.get("url", ""),
        }
        caps_by_key[full.lower()] = caps_by_key[name.lower()]
    return caps_by_key


def build_master_index(master_rows: List[dict]) -> Tuple[Dict[str, dict], Dict[str, dict], Set[str]]:
    by_name: Dict[str, dict] = {}
    by_slug: Dict[str, dict] = {}
    venture_slugs: Set[str] = set()
    for row in master_rows:
        slug = slug_from_github_url(row.get("repository_url", ""))
        if slug and slug not in JUNK_SLUGS and not any(slug.endswith(s) for s in JUNK_SLUG_SUFFIXES):
            venture_slugs.add(slug)
            by_slug[slug] = row
        norm = normalize_name(row.get("name", ""))
        if norm and norm not in by_name:
            by_name[norm] = row
    return by_name, by_slug, venture_slugs


def load_four_layers_maps() -> Tuple[Dict[str, List[Tuple[str, int]]], Dict[str, List[str]]]:
    """UUID -> owned (repo, venture_count) and UUID -> starred full names."""
    owned_map: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
    starred_map: Dict[str, List[str]] = defaultdict(list)
    if not FOUR_LAYERS_CSV.exists():
        return owned_map, starred_map
    for row in load_csv(FOUR_LAYERS_CSV):
        repo = (row.get("repo_name") or "").strip()
        if not repo:
            continue
        count = int(row.get("venture_count") or 0)
        uuids = [u.strip() for u in (row.get("ventures_matched") or "").split("|") if u.strip()]
        if row.get("repo_type") == "owned":
            for uid in uuids:
                owned_map[uid].append((repo.lower(), count))
        elif row.get("repo_type") == "starred":
            full = repo if "/" in repo else repo
            for uid in uuids:
                starred_map[uid].append(full)
    return owned_map, starred_map


def extract_code_prefix(text: str) -> str:
    match = CODE_PREFIX_RE.search(text or "")
    return match.group(1).upper() if match else ""


def master_by_code_prefix(master_rows: List[dict]) -> Dict[str, dict]:
    index: Dict[str, dict] = {}
    for row in master_rows:
        vid = row.get("venture_id", "") or ""
        prefix = extract_code_prefix(vid) or extract_code_prefix(row.get("name", ""))
        if prefix and prefix not in index:
            index[prefix] = row
    return index


def pick_owned_repo(
    uuid: str,
    venture_name: str,
    sector: str,
    top_repo: str,
    owned_slugs: Set[str],
    four_layers_owned: Dict[str, List[Tuple[str, int]]],
    by_name: Dict[str, dict],
    by_slug: Dict[str, dict],
    by_code: Dict[str, dict],
) -> Tuple[str, str, str]:
    """Return (slug, url, bridge_method)."""
    candidates: List[Tuple[str, int, str]] = []

    for slug, count in four_layers_owned.get(uuid, []):
        score = 0
        if count == 1:
            score += 100
        if top_repo and slug == top_repo.lower().replace("_", "-"):
            score += 80
        if slug in owned_slugs:
            score += 40
        if VENTURE_SLUG_RE.match(slug):
            score += 20
        candidates.append((slug, score, "four_layers"))

    norm = normalize_name(venture_name)
    master = by_name.get(norm)
    if not master:
        prefix = extract_code_prefix(venture_name)
        if prefix:
            master = by_code.get(prefix)

    if master:
        slug = slug_from_github_url(master.get("repository_url", ""))
        if slug:
            candidates.append((slug, 60, "master_name" if by_name.get(norm) else "code_prefix"))

    if top_repo:
        tr = top_repo.lower().replace("_", "-")
        if tr in owned_slugs or tr in by_slug:
            candidates.append((tr, 70, "top_repo"))

    alias_slug = VENTURE_OWNED_ALIASES.get(uuid, "")
    if alias_slug and alias_slug in owned_slugs:
        candidates.append((alias_slug, 90, "alias"))

    if not candidates:
        return "", master.get("repository_url", "") if master else "", "unmatched"

    candidates.sort(key=lambda x: (-x[1], x[0]))
    best_slug = candidates[0][0]
    method = candidates[0][2]
    url = f"https://github.com/{GITHUB_ORG}/{best_slug}" if best_slug else ""
    if master and slug_from_github_url(master.get("repository_url", "")) == best_slug:
        url = master.get("repository_url", url)
    return best_slug, url, method


def owned_gap_status(slug: str, in_registry: bool, master: Optional[dict]) -> str:
    if in_registry:
        return "matched"
    if slug and master:
        return "planned_not_created"
    if slug:
        return "registry_miss"
    return "no_slug"


def refresh_starred_capabilities_csv(starred_registry: List[dict], existing: Dict[str, dict]) -> int:
    """Refresh starred_repos_with_capabilities.csv from live registry, preserving known caps."""
    fieldnames = ["name", "owner", "language", "topics", "capabilities", "cap_count", "url"]
    rows_out: List[dict] = []
    for row in starred_registry:
        name = row.get("name", "")
        owner = row.get("owner", "")
        key = name.lower()
        full_key = f"{owner}/{name}".lower() if owner else key
        meta = existing.get(full_key) or existing.get(key) or {}
        caps = meta.get("capabilities") or []
        if not caps:
            topics = [t.strip() for t in (row.get("topics") or "").split("|") if t.strip()]
            caps = topics[:5]
        rows_out.append({
            "name": name,
            "owner": owner,
            "language": row.get("language", ""),
            "topics": row.get("topics", ""),
            "capabilities": "|".join(caps),
            "cap_count": len(caps),
            "url": row.get("url", meta.get("url", "")),
        })
    with STARRED_CAPS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_out)
    print(f"  Refreshed {len(rows_out)} starred capability rows -> {STARRED_CAPS_CSV}")
    return len(rows_out)


def export_the_office_csv(
    classification: List[dict],
    combined_rows: List[dict],
    owned_registry: List[dict],
    starred_registry: List[dict],
) -> None:
    """Export RAG-ready CSV consumed by iza-os-rag-system."""
    THE_OFFICE_EXPORT.parent.mkdir(parents=True, exist_ok=True)
    combined_by_uuid = {r["venture_uuid"]: r for r in combined_rows}
    fieldnames = [
        "type", "id", "name", "sector", "status", "description", "nextAction",
        "githubRepo", "repoPattern", "url", "stars", "owned_repo_slug", "starred_repos",
    ]
    with THE_OFFICE_EXPORT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for v in classification:
            uid = v["venture_id"]
            combo = combined_by_uuid.get(uid, {})
            writer.writerow({
                "type": "venture",
                "id": uid,
                "name": v["venture_name"],
                "sector": v.get("sector", ""),
                "status": v.get("control_type", ""),
                "description": v.get("revenue_model", ""),
                "nextAction": v.get("top_repo", ""),
                "githubRepo": combo.get("owned_repo_url", ""),
                "repoPattern": combo.get("owned_repo_slug", ""),
                "url": "",
                "stars": "",
                "owned_repo_slug": combo.get("owned_repo_slug", ""),
                "starred_repos": combo.get("starred_repos", ""),
            })
        for row in owned_registry:
            writer.writerow({
                "type": "repo",
                "id": "",
                "name": row.get("name", ""),
                "sector": "",
                "status": "owned",
                "description": row.get("description", ""),
                "nextAction": "",
                "githubRepo": "",
                "repoPattern": "",
                "url": row.get("url", ""),
                "stars": row.get("stars", ""),
                "owned_repo_slug": row.get("name", ""),
                "starred_repos": "",
            })
        for row in starred_registry:
            writer.writerow({
                "type": "repo",
                "id": "",
                "name": row.get("name", ""),
                "sector": "",
                "status": "starred",
                "description": row.get("description", ""),
                "nextAction": "",
                "githubRepo": "",
                "repoPattern": "",
                "url": row.get("url", ""),
                "stars": row.get("stars", ""),
                "owned_repo_slug": "",
                "starred_repos": row.get("name_with_owner", ""),
            })
    print(f"  Exported RAG CSV -> {THE_OFFICE_EXPORT}")


def map_master_sector(sector: str) -> str:
    key = (sector or "market").lower()
    if key in MASTER_SECTOR_MAP:
        return MASTER_SECTOR_MAP[key]
    if "-" in key:
        return key.split("-")[0]
    return key


def venture_code_prefix(vid: str) -> Tuple[str, str]:
    """Return (code prefix e.g. fin-001, family prefix e.g. fin-)."""
    parts = (vid or "").split("-")
    if len(parts) >= 2 and parts[1].isdigit():
        return f"{parts[0]}-{parts[1]}".lower(), f"{parts[0]}-".lower()
    if parts:
        return parts[0].lower(), f"{parts[0]}-".lower()
    return "", ""


def build_uuid_crosswalk(
    classification: List[dict],
    master_rows: List[dict],
    bridge_rows: List[dict],
) -> Dict[str, str]:
    """Map master venture_id -> classification UUID."""
    cls_by_name = {normalize_name(v["venture_name"]): v["venture_id"] for v in classification}
    cls_by_prefix: Dict[str, str] = {}
    for v in classification:
        prefix = extract_code_prefix(v["venture_name"])
        if prefix and prefix not in cls_by_prefix:
            cls_by_prefix[prefix] = v["venture_id"]

    bridge_slug_to_uuid = {r["venture_slug"]: r["venture_uuid"] for r in bridge_rows if r.get("venture_slug")}

    crosswalk: Dict[str, str] = {}
    if CROSSWALK_CSV.exists():
        for row in load_csv(CROSSWALK_CSV):
            mid = row.get("master_id", "")
            uid = row.get("uuid", "")
            if mid and uid:
                crosswalk[mid] = uid

    for master in master_rows:
        mid = master.get("venture_id", "")
        if not mid or mid in crosswalk:
            continue
        name = master.get("name", "")
        uid = cls_by_name.get(normalize_name(name))
        if not uid:
            uid = cls_by_prefix.get(extract_code_prefix(mid) or extract_code_prefix(name), "")
        if not uid:
            uid = bridge_slug_to_uuid.get(mid, "")
        if uid:
            crosswalk[mid] = uid
    return crosswalk


def match_repos_for_master_venture(
    master_row: dict,
    owned_slugs: Set[str],
    four_layers_owned: Dict[str, List[Tuple[str, int]]],
    uuid: str,
) -> List[Tuple[str, float, str]]:
    """Return list of (repo_slug, score, repo_type)."""
    slug = slug_from_github_url(master_row.get("repository_url", ""))
    vid = master_row.get("venture_id", "")
    code_prefix, family_prefix = venture_code_prefix(vid)
    scored: Dict[str, Tuple[float, str]] = {}

    if slug and slug in owned_slugs:
        scored[slug] = (1.0, "owned")

    for repo_slug, _count in four_layers_owned.get(uuid, []):
        if repo_slug in owned_slugs:
            prev = scored.get(repo_slug, (0.0, "owned"))
            scored[repo_slug] = (max(prev[0], 0.9), "owned")

    for s in owned_slugs:
        if s in scored:
            continue
        score = 0.0
        if code_prefix and s.startswith(code_prefix):
            score = 0.8
        elif family_prefix and len(family_prefix) >= 3 and s.startswith(family_prefix):
            score = 0.5
        if score > 0:
            scored[s] = (score, "owned")

    return sorted(((k, v[0], v[1]) for k, v in scored.items()), key=lambda x: (-x[1], x[0]))[:10]


def export_712_artifacts(
    master_rows: List[dict],
    classification: List[dict],
    bridge_rows: List[dict],
    owned_slugs: Set[str],
    four_layers_owned: Dict[str, List[Tuple[str, int]]],
    owned_registry: List[dict],
    combined_rows: List[dict],
    starred_caps: Dict[str, dict],
    starred_registry: List[dict],
    four_layers_starred: Dict[str, List[str]],
) -> None:
    """Regenerate 712-venture Excel/JSON layer from ventures-master.csv."""
    crosswalk = build_uuid_crosswalk(classification, master_rows, bridge_rows)
    owned_urls = build_owned_url_index(owned_registry)
    starred_urls = build_starred_url_index(starred_registry)
    combined_by_uuid = {r["venture_uuid"]: r for r in combined_rows if r.get("venture_uuid")}

    unified_fieldnames = [
        "venture_id",
        "venture_name",
        "sector",
        "stage",
        "status",
        "uuid",
        "owned_repo_slug",
        "owned_repo_url",
        "owned_in_registry",
        "repos_matched",
        "repos_matched_urls",
        "repo_count",
        "top_confidence",
        "starred_repos_count",
        "starred_repos",
        "starred_repo_urls",
    ]
    # VENTURE-ID-CROSSWALK.csv
    crosswalk_rows = []
    master_by_id = {m["venture_id"]: m for m in master_rows if m.get("venture_id")}
    for mid, uid in sorted(crosswalk.items()):
        m = master_by_id.get(mid, {})
        crosswalk_rows.append({
            "master_id": mid,
            "uuid": uid,
            "name": m.get("name", ""),
            "sector": map_master_sector(m.get("sector", "")),
        })
    with CROSSWALK_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["master_id", "uuid", "name", "sector"])
        writer.writeheader()
        writer.writerows(crosswalk_rows)

    # ventures_master_with_sectors.csv
    sector_rows = []
    alignments_json: List[dict] = []
    unified_rows = []

    for master in master_rows:
        mid = master.get("venture_id", "")
        if not mid:
            continue
        uid = crosswalk.get(mid, "")
        sector = map_master_sector(master.get("sector", ""))
        sector_rows.append({
            "venture_id": mid,
            "venture_name": master.get("name", ""),
            "sector": sector,
            "stage": master.get("stage", ""),
            "status": master.get("status", ""),
            "has_uuid": "yes" if uid else "no",
            "uuid": uid,
        })

        repo_matches = match_repos_for_master_venture(master, owned_slugs, four_layers_owned, uid)
        repo_names = [m[0] for m in repo_matches]
        top_conf = repo_matches[0][1] if repo_matches else 0.0
        primary_slug = slug_from_github_url(master.get("repository_url", ""))
        owned_url = (master.get("repository_url") or "").strip() or github_url_for_slug(primary_slug, owned_urls)
        repo_urls = "|".join(github_url_for_slug(slug, owned_urls) for slug in repo_names)
        starred_count, starred_repos, starred_urls_str = starred_links_for_venture(
            uid,
            sector,
            master.get("name", ""),
            combined_by_uuid,
            starred_caps,
            starred_registry,
            four_layers_starred,
            starred_urls,
        )

        unified_rows.append({
            "venture_id": mid,
            "venture_name": master.get("name", ""),
            "sector": sector,
            "stage": master.get("stage", ""),
            "status": master.get("status", ""),
            "uuid": uid,
            "owned_repo_slug": primary_slug,
            "owned_repo_url": owned_url,
            "owned_in_registry": "yes" if primary_slug in owned_slugs else "no",
            "repos_matched": "|".join(repo_names),
            "repos_matched_urls": repo_urls,
            "repo_count": len(repo_names),
            "top_confidence": top_conf,
            "starred_repos_count": starred_count,
            "starred_repos": starred_repos,
            "starred_repo_urls": starred_urls_str,
        })

        alignments_json.append({
            "venture_id": mid,
            "venture_name": master.get("name", ""),
            "sector": sector,
            "uuid": uid or None,
            "owned_repo_url": owned_url,
            "starred_repos_count": starred_count,
            "starred_repo_urls": starred_urls_str.split(";") if starred_urls_str else [],
            "auto_matched_repos": [
                {
                    "name": name,
                    "url": github_url_for_slug(name, owned_urls),
                    "type": rtype,
                    "score": score,
                }
                for name, score, rtype in repo_matches
            ],
            "confidence": top_conf,
        })

    with MASTER_WITH_SECTORS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["venture_id", "venture_name", "sector", "stage", "status", "has_uuid", "uuid"],
        )
        writer.writeheader()
        writer.writerows(sector_rows)

    with UNIFIED_712_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=unified_fieldnames)
        writer.writeheader()
        writer.writerows(unified_rows)

    payload = {
        "total_ventures": len(alignments_json),
        "ventures_with_matches": sum(1 for a in alignments_json if a["auto_matched_repos"]),
        "ventures_with_uuid": sum(1 for a in alignments_json if a.get("uuid")),
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "source_files": {
            "master": str(MASTER_CSV),
            "classification": str(CLASSIFICATION_CSV),
            "owned_registry": str(OWNED_REGISTRY),
            "crosswalk": str(CROSSWALK_CSV),
        },
        "alignments": alignments_json,
    }
    AUTO_ALIGNMENT_712_JSON.write_text(json.dumps(payload, indent=2))

    for artifact in (
        MASTER_WITH_SECTORS_CSV,
        UNIFIED_712_CSV,
        CROSSWALK_CSV,
        AUTO_ALIGNMENT_712_JSON,
        CLASSIFICATION_CSV,
        ENRICHED_JSON,
        DEPENDENCIES_JSON,
    ):
        mirror_to_ventures_data(artifact)

    print(f"  712 layer: {len(sector_rows)} ventures -> {MASTER_WITH_SECTORS_CSV.name}")
    print(f"  Crosswalk: {len(crosswalk_rows)} UUID mappings -> {CROSSWALK_CSV.name}")
    print(f"  Unified CSV -> {UNIFIED_712_CSV.name}")
    print(f"  Auto alignment JSON -> {AUTO_ALIGNMENT_712_JSON.name}")


def match_starred_repos(
    required_caps: List[str],
    starred_caps: Dict[str, dict],
    starred_registry: List[dict],
    min_match_pct: float = 40.0,
    limit: int = 50,
) -> List[Tuple[str, float]]:
    req = set(required_caps)
    if not req:
        return []
    scored: List[Tuple[str, float]] = []
    seen: Set[str] = set()
    for row in starred_registry:
        owner = row.get("owner", "")
        name = row.get("name", "")
        full = f"{owner}/{name}" if owner else name
        key = full.lower()
        if key in seen:
            continue
        seen.add(key)
        meta = starred_caps.get(name.lower()) or starred_caps.get(key) or {}
        repo_caps = set(meta.get("capabilities") or [])
        if not repo_caps:
            topics = [t.strip() for t in (row.get("topics") or "").split("|") if t.strip()]
            repo_caps = set(topics)
        overlap = len(req & repo_caps)
        if overlap == 0:
            continue
        pct = (overlap / len(req)) * 100
        if pct >= min_match_pct:
            scored.append((full, pct))
    scored.sort(key=lambda x: (-x[1], x[0]))
    return scored[:limit]


def merge_starred_from_four_layers(
    uuid: str,
    four_layers_starred: Dict[str, List[str]],
    capability_matches: List[Tuple[str, float]],
) -> List[Tuple[str, float]]:
    """Prefer venture-specific starred repos from 4LAYERS, then capability matches."""
    merged: Dict[str, float] = {}
    for full in four_layers_starred.get(uuid, []):
        merged[full] = max(merged.get(full, 0.0), 95.0)
    for full, pct in capability_matches:
        merged[full] = max(merged.get(full, 0.0), pct)
    return sorted(merged.items(), key=lambda x: (-x[1], x[0]))


def short_repo_name(full_name: str) -> str:
    return full_name.split("/")[-1] if "/" in full_name else full_name


def classify_owned_type(slug: str, venture_slugs: Set[str]) -> str:
    if slug in JUNK_SLUGS or any(slug.endswith(s) for s in JUNK_SLUG_SUFFIXES):
        return "skip"
    if slug in venture_slugs or VENTURE_SLUG_RE.match(slug):
        return "owned-venture"
    return "owned-tool"


def load_existing_enriched() -> Dict[str, dict]:
    if not ENRICHED_JSON.exists():
        return {}
    data = json.loads(ENRICHED_JSON.read_text())
    return {v["venture_id"]: v for v in data.get("ventures", []) if v.get("venture_id")}


def build_alignment_json(
    ventures: List[dict],
    deps: Dict[str, dict],
    owned_count: int,
    starred_count: int,
    repo_names: Set[str],
) -> dict:
    graph_entities = []
    if GRAPH_DATA.exists():
        try:
            graph_entities = json.loads(GRAPH_DATA.read_text()).get("entities", []) or []
        except Exception:
            pass
    kg_ids = load_kg_venture_ids()
    merged_index = load_merged_slug_index()
    graph_by_venture: Dict[str, int] = defaultdict(int)
    for v in ventures:
        vid = v.get("venture_uuid") or v.get("venture_id", "")
        graph_by_venture[vid] = count_graph_entities(
            vid,
            v.get("venture_name", ""),
            v.get("owned_repo_slug", ""),
            v.get("venture_slug", ""),
            graph_entities,
            kg_ids=kg_ids,
            merged_index=merged_index,
        )

    repo_names_lower = {n.lower() for n in repo_names}
    aligned_rows = []
    mismatched = []
    for v in ventures:
        vid = v["venture_uuid"]
        dep = deps.get(vid, {})
        required = dep.get("required_repos", [])
        matched = [r for r in required if required_repo_satisfied(r, repo_names_lower)]
        missing = [r for r in required if not required_repo_satisfied(r, repo_names_lower)]
        graph_count = graph_by_venture.get(vid, 0)
        graph_connected = graph_count > 0
        record = {
            "venture_id": vid,
            "venture_slug": v.get("venture_slug", ""),
            "venture_name": v["venture_name"],
            "sector": v["sector"],
            "required_repos": required,
            "top_repo_1": v.get("top_repo_1", ""),
            "owned_repo_slug": v.get("owned_repo_slug", ""),
            "owned_repo_found": v.get("owned_repo_found_in_registry", "no"),
            "starred_repos_count": v.get("starred_repos_count", 0),
            "graph_entity_count": graph_count,
            "graph_connected": graph_connected,
            "matched_required_repos": matched,
            "missing_required_repos": missing,
            "repo_coverage_pct": round((len(matched) / len(required)) * 100, 2) if required else 100.0,
            "alignment_status": alignment_status(
                graph_connected, required, repo_names_lower
            ),
        }
        aligned_rows.append(record)
        if record["alignment_status"] != "aligned":
            mismatched.append(record)

    return {
        "status": "success",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_files": {
            "classification": str(CLASSIFICATION_CSV),
            "master": str(MASTER_CSV),
            "owned_registry": str(OWNED_REGISTRY),
            "starred_registry": str(STARRED_REGISTRY),
            "enriched": str(ENRICHED_JSON),
            "dependencies": str(DEPENDENCIES_JSON),
        },
        "summary": {
            "total_ventures": len(ventures),
            "ventures_aligned": sum(1 for r in aligned_rows if r["alignment_status"] == "aligned"),
            "ventures_needing_attention": len(mismatched),
            "ventures_with_graph_entities": sum(1 for r in aligned_rows if r["graph_connected"]),
            "github_owned_count": owned_count,
            "github_starred_count": starred_count,
            "supabase_repositories_target": owned_count + starred_count,
        },
        "ventures": aligned_rows,
        "mismatched": mismatched,
    }


def sync_repositories_to_supabase(owned_repos: List[dict], starred_repos: List[dict], venture_slugs: Set[str], slug_to_master: Dict[str, dict]) -> int:
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("Skipping Supabase sync (missing credentials)")
        return 0
    try:
        from supabase import create_client
    except ImportError:
        os.system(f"{sys.executable} -m pip install supabase -q")
        from supabase import create_client

    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    now = datetime.now(timezone.utc).isoformat()
    rows: List[dict] = []

    for r in owned_repos:
        slug = r["name"].lower()
        repo_type = classify_owned_type(slug, venture_slugs)
        if repo_type == "skip":
            continue
        master = slug_to_master.get(slug, {})
        sector = master.get("sector", "")
        venture_id = master.get("venture_id", "") if repo_type == "owned-venture" else None
        rows.append({
            "name": r["name"],
            "full_name": r.get("full_name", f"{GITHUB_ORG}/{r['name']}"),
            "owner": GITHUB_ORG,
            "description": r.get("description") or "",
            "url": r.get("html_url") or "",
            "language": r.get("language"),
            "stars": r.get("stargazers_count", 0),
            "forks": r.get("forks_count", 0),
            "is_fork": r.get("fork", False),
            "is_private": r.get("private", False),
            "is_archived": r.get("archived", False),
            "topics": r.get("topics") or [],
            "repo_type": repo_type,
            "venture_id": venture_id,
            "venture_sector": sector or None,
            "synced_at": now,
            "civos_status": "owned",
        })

    for r in starred_repos:
        owner = (r.get("owner") or {}).get("login", "")
        rows.append({
            "name": r["name"],
            "full_name": r.get("full_name", f"{owner}/{r['name']}"),
            "owner": owner,
            "description": r.get("description") or "",
            "url": r.get("html_url") or "",
            "language": r.get("language"),
            "stars": r.get("stargazers_count", 0),
            "forks": r.get("forks_count", 0),
            "is_fork": r.get("fork", False),
            "is_private": r.get("private", False),
            "is_archived": r.get("archived", False),
            "topics": r.get("topics") or [],
            "repo_type": "starred",
            "venture_id": None,
            "venture_sector": None,
            "synced_at": now,
            "civos_status": "starred",
        })

    batch_size = 100
    synced = 0
    for i in range(0, len(rows), batch_size):
        batch = rows[i : i + batch_size]
        client.table("repositories").upsert(batch, on_conflict="full_name").execute()
        synced += len(batch)
        print(f"  Upserted repositories batch {i // batch_size + 1} ({len(batch)} rows)")
    return synced


def main() -> None:
    if not GITHUB_TOKEN and "--skip-fetch" not in sys.argv:
        raise SystemExit("GITHUB_TOKEN is required")

    skip_fetch = "--skip-fetch" in sys.argv

    print("=" * 72)
    print("ALIGN VENTURE + REPO UNIVERSE")
    print("=" * 72)

    if skip_fetch:
        print("Skipping GitHub fetch (--skip-fetch); using existing registries")
        owned_raw = []
        starred_raw = []
        owned_slugs_registry = {row["name"].lower() for row in load_csv(OWNED_REGISTRY)}
    else:
        owned_raw = fetch_owned_repos()
        starred_raw = fetch_starred_repos()
        owned_slugs_registry = write_owned_registry(owned_raw)
        write_starred_registry(starred_raw)

    if not CLASSIFICATION_CSV.exists():
        regen = SCRIPT_DIR / "regenerate_venture_catalog.py"
        if regen.exists():
            print("Classification CSV missing — running regenerate_venture_catalog.py")
            import subprocess

            subprocess.run([sys.executable, str(regen)], check=True)
    classification = load_csv(CLASSIFICATION_CSV)
    master_rows = load_csv(MASTER_CSV)
    by_name, by_slug, venture_slugs = build_master_index(master_rows)
    by_code = master_by_code_prefix(master_rows)
    four_layers_owned, four_layers_starred = load_four_layers_maps()
    starred_caps = load_starred_capabilities()
    starred_registry = load_csv(STARRED_REGISTRY)
    existing_enriched = load_existing_enriched()

    if starred_registry:
        refresh_starred_capabilities_csv(starred_registry, starred_caps)
        starred_caps = load_starred_capabilities()

    bridge_rows: List[dict] = []
    combined_rows: List[dict] = []
    alignment_rows: List[dict] = []
    enriched_ventures: List[dict] = []
    dependencies: Dict[str, dict] = {}
    repo_name_index: Set[str] = set()

    for slug in owned_slugs_registry:
        repo_name_index.add(slug)
    for row in starred_registry:
        repo_name_index.add(row.get("name", "").lower())
        owner = row.get("owner", "")
        if owner:
            repo_name_index.add(f"{owner}/{row.get('name', '')}".lower())

    bridge_methods: Dict[str, int] = defaultdict(int)
    matched_master = 0
    for v in classification:
        uuid = v["venture_id"]
        name = v["venture_name"]
        sector = v.get("sector", "market")
        tier = v.get("tier", "")
        top_repo_field = (v.get("top_repo") or "").strip()

        norm = normalize_name(name)
        master = by_name.get(norm)
        if not master:
            prefix = extract_code_prefix(name)
            if prefix:
                master = by_code.get(prefix)

        slug, owned_url, bridge_method = pick_owned_repo(
            uuid,
            name,
            sector,
            top_repo_field,
            owned_slugs_registry,
            four_layers_owned,
            by_name,
            by_slug,
            by_code,
        )
        venture_slug = master.get("venture_id", "") if master else ""
        if not owned_url and slug:
            owned_url = f"https://github.com/{GITHUB_ORG}/{slug}"
        owned_found = "yes" if slug and slug in owned_slugs_registry else "no"
        if master:
            matched_master += 1
        bridge_methods[bridge_method] += 1

        required_caps = infer_capabilities(sector, name)
        if uuid in existing_enriched and existing_enriched[uuid].get("required_capabilities"):
            required_caps = existing_enriched[uuid]["required_capabilities"]

        cap_matches = match_starred_repos(required_caps, starred_caps, starred_registry)
        starred_matches = merge_starred_from_four_layers(uuid, four_layers_starred, cap_matches)
        starred_full = [m[0] for m in starred_matches]
        starred_short = [short_repo_name(s) for s in starred_full]

        top3 = starred_matches[:3]
        while len(top3) < 3:
            top3.append(("", 0.0))

        dep_repos = starred_short[:2]
        if slug and slug in owned_slugs_registry:
            if slug not in dep_repos:
                dep_repos.insert(0, slug)
        dependencies[uuid] = {
            "depends_on_tiers": [int(tier)] if str(tier).isdigit() else [],
            "venture_type": v.get("control_type", "platform").lower(),
            "required_repos": dep_repos,
        }

        gap = owned_gap_status(slug, owned_found == "yes", master)
        mapping_status = "aligned" if owned_found == "yes" and starred_full else (
            "partial" if owned_found == "yes" or starred_full else "needs_review"
        )
        if gap == "planned_not_created":
            mapping_status = "planned_not_created"

        bridge_rows.append({
            "venture_uuid": uuid,
            "venture_slug": venture_slug,
            "venture_name": name,
            "sector_classification": sector,
            "sector_master": master.get("sector", "") if master else "",
            "owned_repo_slug": slug,
            "owned_repo_url": owned_url,
            "owned_gap_status": gap,
            "bridge_method": bridge_method,
        })

        combined_rows.append({
            "venture_uuid": uuid,
            "venture_slug": venture_slug,
            "venture_name": name,
            "sector": sector,
            "target_archetype": v.get("revenue_model", ""),
            "owned_repo_url": owned_url,
            "owned_repo_slug": slug,
            "owned_repo_found_in_registry": owned_found,
            "owned_gap_status": gap,
            "starred_repos_count": len(starred_full),
            "starred_repos": ";".join(starred_full),
            "data_stack": DATA_STACK,
            "graphify_expected": "yes",
            "mapping_status": mapping_status,
        })

        alignment_rows.append({
            "venture_id": uuid,
            "venture_name": name,
            "sector": sector,
            "tier": tier,
            "required_capabilities": "|".join(required_caps),
            "top_repo_1": short_repo_name(top3[0][0]) if top3[0][0] else v.get("top_repo", ""),
            "top_repo_1_match_pct": f"{top3[0][1]:.1f}%" if top3[0][0] else "",
            "repo_1_is_starred": "YES" if top3[0][0] else "",
            "top_repo_2": short_repo_name(top3[1][0]) if top3[1][0] else "",
            "top_repo_2_match_pct": f"{top3[1][1]:.1f}%" if top3[1][0] else "",
            "repo_2_is_starred": "YES" if top3[1][0] else "",
            "top_repo_3": short_repo_name(top3[2][0]) if top3[2][0] else "",
            "top_repo_3_match_pct": f"{top3[2][1]:.1f}%" if top3[2][0] else "",
            "repo_3_is_starred": "YES" if top3[2][0] else "",
            "sector_coverage_pct": "",
            "sector_required_capabilities": "|".join(required_caps),
        })

        matched_repos: Dict[str, List[str]] = defaultdict(list)
        for cap in required_caps:
            for full, pct in starred_matches:
                meta = starred_caps.get(full.lower()) or starred_caps.get(short_repo_name(full).lower()) or {}
                if cap in (meta.get("capabilities") or []):
                    matched_repos[cap].append(short_repo_name(full))

        enriched_ventures.append({
            "venture_id": uuid,
            "venture_name": name,
            "sector": sector,
            "venture_slug": venture_slug,
            "owned_repo_slug": slug,
            "required_capabilities": required_caps,
            "capability_match_score": round(starred_matches[0][1] / 100, 2) if starred_matches else 0.0,
            "matched_repos": dict(matched_repos),
            "top_repo_1": short_repo_name(top3[0][0]) if top3[0][0] else v.get("top_repo", ""),
            "top_repo_2": short_repo_name(top3[1][0]) if top3[1][0] else "",
            "top_repo_3": short_repo_name(top3[2][0]) if top3[2][0] else "",
            "starred_repos_count": len(starred_full),
        })

    BRIDGE_CSV.parent.mkdir(parents=True, exist_ok=True)
    with BRIDGE_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(bridge_rows[0].keys()))
        writer.writeheader()
        writer.writerows(bridge_rows)

    COMBINED_CSV.parent.mkdir(parents=True, exist_ok=True)
    with COMBINED_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(combined_rows[0].keys()))
        writer.writeheader()
        writer.writerows(combined_rows)

    with ALIGNMENT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(alignment_rows[0].keys()))
        writer.writeheader()
        writer.writerows(alignment_rows)

    enriched_payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_ventures": len(enriched_ventures),
        "enrichment_method": "semantic_capability_matching_v2",
        "ventures": enriched_ventures,
    }
    ENRICHED_JSON.write_text(json.dumps(enriched_payload, indent=2))
    alt_enriched = ROOT / "ventures_enriched_option_b.json"
    if alt_enriched != ENRICHED_JSON:
        alt_enriched.write_text(json.dumps(enriched_payload, indent=2))

    deps_payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_ventures": len(dependencies),
        "dependencies": dependencies,
    }
    DEPENDENCIES_JSON.write_text(json.dumps(deps_payload, indent=2))
    alt_deps = ROOT / "ventures_dependencies.json"
    if alt_deps != DEPENDENCIES_JSON:
        alt_deps.write_text(json.dumps(deps_payload, indent=2))

    owned_count = len(owned_raw) if owned_raw else len(owned_slugs_registry)
    starred_count = len(starred_raw) if starred_raw else len(starred_registry)
    alignment_json = build_alignment_json(
        combined_rows, dependencies, owned_count, starred_count, repo_name_index
    )
    PLANNING_ALIGNMENT.parent.mkdir(parents=True, exist_ok=True)
    PLANNING_ALIGNMENT.write_text(json.dumps(alignment_json, indent=2))
    mirror_to_ventures_data(PLANNING_ALIGNMENT)

    export_the_office_csv(classification, combined_rows, load_csv(OWNED_REGISTRY), starred_registry)

    export_712_artifacts(
        master_rows,
        classification,
        bridge_rows,
        owned_slugs_registry,
        four_layers_owned,
        owned_raw or load_csv(OWNED_REGISTRY),
        combined_rows,
        starred_caps,
        starred_registry,
        four_layers_starred,
    )

    synced = 0
    if not skip_fetch:
        synced = sync_repositories_to_supabase(owned_raw, starred_raw, venture_slugs, by_slug)
    else:
        print("Skipping Supabase sync (--skip-fetch)")

    with_starred = sum(1 for r in combined_rows if int(r["starred_repos_count"]) > 0)
    owned_ok = sum(1 for r in combined_rows if r["owned_repo_found_in_registry"] == "yes")

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Classification ventures:     {len(classification)}")
    print(f"  Master bridge matches:         {matched_master}")
    print(f"  GitHub owned (org):            {len(owned_raw) or len(owned_slugs_registry)}")
    print(f"  GitHub starred:                {len(starred_raw) or len(starred_registry)}")
    print(f"  Ventures with owned in registry: {owned_ok}")
    print(f"  Ventures with starred matches: {with_starred}")
    print(f"  Bridge methods:                  {dict(bridge_methods)}")
    print(f"  Planned-not-created slugs:       {sum(1 for r in combined_rows if r.get('owned_gap_status') == 'planned_not_created')}")
    print(f"  Supabase repositories upserted: {synced}")
    print(f"  Bridge CSV:                    {BRIDGE_CSV}")
    print(f"  Combined CSV:                  {COMBINED_CSV}")
    print(f"  Alignment CSV:                 {ALIGNMENT_CSV}")
    print(f"  Enriched JSON:                 {ENRICHED_JSON}")
    print(f"  Planning alignment JSON:       {PLANNING_ALIGNMENT}")
    print("=" * 72)


if __name__ == "__main__":
    main()
