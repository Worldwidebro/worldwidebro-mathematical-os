#!/usr/bin/env python3
"""
Fix repos metadata using GitHub API data + heuristic inference
This bypasses Ollama and uses GitHub's actual repo data to populate purpose, description, and capabilities
"""

import os
import json
import re
import requests
import logging
from datetime import datetime
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

GITHUB_HEADERS = {}
if GITHUB_TOKEN:
    GITHUB_HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

SUPABASE_HEADERS = {
    "apikey": SUPABASE_SERVICE_KEY,
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
    "Content-Type": "application/json"
}

# Language → Capabilities mapping (heuristic)
LANGUAGE_CAPABILITIES = {
    "python": ["backend", "data-processing", "machine-learning"],
    "javascript": ["frontend", "full-stack", "real-time"],
    "typescript": ["frontend", "full-stack", "api"],
    "rust": ["systems", "performance", "safety"],
    "go": ["backend", "distributed-systems", "performance"],
    "java": ["backend", "enterprise", "performance"],
    "c++": ["systems", "performance", "real-time"],
    "sql": ["data", "database", "analytics"],
}

# Repo name patterns → Capabilities (heuristic)
REPO_PATTERNS = {
    r'(stripe|payment|checkout|billing)': ["payments", "commerce"],
    r'(postgres|mysql|mongo|db|database)': ["data", "database"],
    r'(react|vue|angular|frontend|ui)': ["frontend", "ui"],
    r'(api|graphql|rest)': ["api", "integration"],
    r'(auth|oauth|jwt|security)': ["auth", "security"],
    r'(ai|llm|ml|gpt|bert)': ["machine-learning", "ai"],
    r'(real-time|socket|websocket)': ["real-time", "communication"],
    r'(calendar|scheduling)': ["scheduling", "workflow"],
    r'(crm|customer|contact)': ["crm", "customer-management"],
    r'(content|blog|cms)': ["content-management", "publishing"],
}

def infer_capabilities(repo_name: str, description: str, language: str) -> list:
    """Infer capabilities from repo name, description, and language"""
    capabilities = set()

    # From language
    lang_lower = language.lower() if language else ""
    for lang, caps in LANGUAGE_CAPABILITIES.items():
        if lang in lang_lower:
            capabilities.update(caps)

    # From repo name and description patterns
    combined = f"{repo_name} {description}".lower()
    for pattern, caps in REPO_PATTERNS.items():
        if re.search(pattern, combined):
            capabilities.update(caps)

    return sorted(list(capabilities)) if capabilities else ["utility"]

def infer_integration_effort(capabilities: list, description: str) -> str:
    """Infer integration effort based on capabilities"""
    # Heuristic: more capabilities = harder to integrate
    if len(capabilities) >= 5:
        return "high"
    elif len(capabilities) >= 3:
        return "medium"
    else:
        return "low"

def infer_maturity(repo_name: str, stars: int) -> str:
    """Infer maturity based on stars and name"""
    if stars >= 10000:
        return "mature"
    elif stars >= 1000:
        return "production"
    elif stars >= 100:
        return "beta"
    else:
        return "experimental"

def fetch_all_repos_from_supabase():
    """Get all repos currently in Supabase"""
    try:
        url = f"{SUPABASE_URL}/rest/v1/repos?select=id,name,description,github_url,github_stars"
        response = requests.get(url, headers=SUPABASE_HEADERS, timeout=15)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        logger.error(f"Failed to fetch repos: {e}")
    return []

def get_full_github_metadata(repo_name: str) -> dict:
    """Fetch complete GitHub metadata for repo"""
    possible_urls = [
        f"https://api.github.com/repos/{repo_name}",
        f"https://api.github.com/repos/Worldwidebro/{repo_name}",
    ]

    for url in possible_urls:
        try:
            response = requests.get(url, headers=GITHUB_HEADERS, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return {
                    "github_url": data.get("html_url", ""),
                    "owner": data.get("owner", {}).get("login", ""),
                    "description": data.get("description", ""),
                    "language": data.get("language", ""),
                    "github_stars": data.get("stargazers_count", 0),
                    "contributors": data.get("watchers_count", 0),
                    "last_commit_date": data.get("pushed_at", ""),
                    "license": data.get("license", {}).get("spdx_id", "") if data.get("license") else "",
                    "readme": fetch_readme(repo_name)
                }
        except Exception as e:
            logger.debug(f"Failed {url}: {e}")
            continue

    return {}

def fetch_readme(repo_name: str) -> str:
    """Fetch README content from GitHub"""
    possible_repos = [repo_name, f"Worldwidebro/{repo_name}"]

    for repo in possible_repos:
        try:
            url = f"https://api.github.com/repos/{repo}/readme"
            response = requests.get(
                url,
                headers={**GITHUB_HEADERS, "Accept": "application/vnd.github.v3.raw"},
                timeout=10
            )
            if response.status_code == 200:
                return response.text[:1000]
        except:
            pass

    return ""

def update_repo_in_supabase(repo_id: str, updates: dict) -> bool:
    """Update repo record with inferred metadata"""
    try:
        url = f"{SUPABASE_URL}/rest/v1/repos?id=eq.{repo_id}"
        response = requests.patch(
            url,
            headers=SUPABASE_HEADERS,
            json=updates,
            timeout=10
        )
        return response.status_code in [200, 204]
    except Exception as e:
        logger.error(f"Failed to update {repo_id}: {e}")
        return False

def fix_all_repos():
    """Main fix loop"""
    logger.info("=" * 80)
    logger.info("FIXING REPOS METADATA - GITHUB API + HEURISTIC INFERENCE")
    logger.info("=" * 80)

    repos = fetch_all_repos_from_supabase()
    logger.info(f"Found {len(repos)} repos in Supabase")

    stats = {"updated": 0, "failed": 0}

    for i, repo in enumerate(repos, 1):
        repo_id = repo["id"]
        repo_name = repo["name"]

        logger.info(f"\n[{i}/{len(repos)}] Processing: {repo_name}")

        # Get GitHub metadata
        github_data = get_full_github_metadata(repo_name)
        if not github_data:
            logger.warning(f"  ✗ Could not fetch GitHub data")
            stats["failed"] += 1
            continue

        # Infer capabilities
        description = github_data.get("description", "")
        language = github_data.get("language", "")
        capabilities = infer_capabilities(repo_name, description, language)

        # Infer other fields
        integration_effort = infer_integration_effort(capabilities, description)
        maturity = infer_maturity(repo_name, github_data.get("github_stars", 0))

        # Estimate integration days based on effort
        effort_to_days = {"low": 3, "medium": 7, "high": 14}
        estimated_days = effort_to_days.get(integration_effort, 7)

        # Prepare update
        update_payload = {
            "description": description or f"{repo_name} repository",
            "purpose": description or f"Purpose of {repo_name}",
            "capabilities": capabilities,
            "integration_effort": integration_effort,
            "estimated_integration_days": estimated_days,
            "language": language or "unknown",
            "maturity": maturity,
            "github_stars": github_data.get("github_stars", 0),
            "last_commit_date": github_data.get("last_commit_date", ""),
            "contributors": github_data.get("contributors", 0),
        }

        # Update Supabase
        if update_repo_in_supabase(repo_id, update_payload):
            stats["updated"] += 1
            logger.info(f"  ✓ Updated: {maturity} | {integration_effort} | {len(capabilities)} capabilities")
            logger.info(f"    - Capabilities: {capabilities[:3]}")
            if description:
                logger.info(f"    - Purpose: {description[:60]}")
        else:
            stats["failed"] += 1
            logger.warning(f"  ✗ Failed to update")

        if i % 10 == 0:
            logger.info(f"\n--- Progress: {i}/{len(repos)} ---\n")

    logger.info("\n" + "=" * 80)
    logger.info("FIX SUMMARY")
    logger.info("=" * 80)
    logger.info(f"Repos updated:  {stats['updated']}")
    logger.info(f"Repos failed:   {stats['failed']}")
    logger.info(f"Success rate:   {stats['updated']/len(repos)*100:.1f}%")
    logger.info("=" * 80)

if __name__ == "__main__":
    fix_all_repos()
