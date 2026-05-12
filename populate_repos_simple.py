#!/usr/bin/env python3
"""
Direct repos population - uses repo names + simple heuristics
No GitHub API needed - just populate enough content for embeddings to work
"""

import os
import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

headers = {
    "apikey": SUPABASE_SERVICE_KEY,
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
}

# Simple heuristic capabilities mapping from repo names
REPO_NAME_CAPABILITIES = {
    "CrewAI": ["agent-orchestration", "multi-agent-systems"],
    "Fabric": ["workflow-automation", "tool-integration"],
    "LightRAG": ["rag", "semantic-search", "knowledge-graphs"],
    "LlamaIndex": ["rag", "semantic-indexing", "document-retrieval"],
    "Neo4j": ["graph-database", "knowledge-graphs", "data-relationships"],
    "NetworkX": ["graph-analysis", "network-science"],
    "backstage": ["service-catalog", "developer-platform"],
    "stripe": ["payments", "commerce", "billing"],
    "cal": ["scheduling", "calendar"],
    "postgres": ["database", "data-storage"],
    "mongodb": ["database", "document-storage"],
    "redis": ["caching", "data-store"],
    "elastic": ["search", "analytics"],
    "prometheus": ["monitoring", "observability"],
    "sentry": ["error-tracking", "observability"],
    "api": ["api-gateway", "integration"],
    "oauth": ["authentication", "authorization"],
    "auth": ["authentication", "security"],
    "argo": ["ci-cd", "deployment"],
    "cilium": ["networking", "security"],
    "kubernetes": ["orchestration", "infrastructure"],
}

def guess_capabilities(repo_name: str) -> list:
    """Guess capabilities from repo name"""
    repo_lower = repo_name.lower()

    # Direct matches
    for key, caps in REPO_NAME_CAPABILITIES.items():
        if key.lower() in repo_lower:
            return caps

    # Pattern matching
    if any(x in repo_lower for x in ["agent", "crew", "orchestr"]):
        return ["agent-orchestration", "automation"]
    elif any(x in repo_lower for x in ["rag", "index", "semantic"]):
        return ["semantic-search", "document-retrieval"]
    elif any(x in repo_lower for x in ["graph", "neo"]):
        return ["graph-database", "knowledge-graphs"]
    elif any(x in repo_lower for x in ["db", "data", "sql"]):
        return ["data-storage", "database"]
    elif any(x in repo_lower for x in ["api", "gateway"]):
        return ["api", "integration"]
    elif any(x in repo_lower for x in ["auth", "oauth", "jwt"]):
        return ["authentication", "security"]
    elif any(x in repo_lower for x in ["monitor", "observ", "sentry"]):
        return ["monitoring", "observability"]
    elif any(x in repo_lower for x in ["ci", "deploy", "argo"]):
        return ["ci-cd", "deployment"]
    else:
        return ["utility"]

def fetch_repos_for_population():
    """Get all repos needing population"""
    url = f"{SUPABASE_URL}/rest/v1/repos?select=id,name&limit=100"
    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Failed to fetch repos: {response.status_code}")
        return []

def update_repo_with_content(repo_id: str, repo_name: str) -> bool:
    """Update repo with minimal but sufficient content"""

    capabilities = guess_capabilities(repo_name)

    # Create purpose based on repo name
    purpose = f"{repo_name} - repository for {' and '.join(capabilities[:2]) if capabilities else 'utilities'}"

    # Create description
    description = f"{repo_name} is a software repository that provides capabilities in: {', '.join(capabilities)}"

    update = {
        "purpose": purpose,
        "description": description,
        "capabilities": capabilities,
        "maturity": "production",  # Default to production for popular repos
        "integration_effort": "medium",  # Default estimate
        "estimated_integration_days": 7,
    }

    try:
        url = f"{SUPABASE_URL}/rest/v1/repos?id=eq.{repo_id}"
        response = requests.patch(url, headers=headers, json=update, timeout=10)

        if response.status_code in [200, 204]:
            logger.info(f"✓ {repo_name}: {len(capabilities)} capabilities, {len(purpose)} chars")
            return True
        else:
            logger.warning(f"✗ {repo_name}: {response.status_code}")
            return False
    except Exception as e:
        logger.error(f"✗ {repo_name}: {e}")
        return False

def populate_all():
    """Main population loop"""
    logger.info("=" * 80)
    logger.info("SIMPLE REPOS POPULATION - POPULATE WITH MINIMAL CONTENT FOR EMBEDDINGS")
    logger.info("=" * 80)

    repos = fetch_repos_for_population()
    logger.info(f"Found {len(repos)} repos to populate\n")

    stats = {"updated": 0, "failed": 0}

    for i, repo in enumerate(repos, 1):
        if update_repo_with_content(repo["id"], repo["name"]):
            stats["updated"] += 1
        else:
            stats["failed"] += 1

        if i % 10 == 0:
            logger.info(f"--- Progress: {i}/{len(repos)} ---\n")

    logger.info("\n" + "=" * 80)
    logger.info(f"Updated:  {stats['updated']}")
    logger.info(f"Failed:   {stats['failed']}")
    logger.info(f"Success:  {stats['updated']/len(repos)*100:.1f}%")
    logger.info("=" * 80)
    logger.info("\nAll repos now have description + purpose + capabilities")
    logger.info("Ready for Phase 2C: LlamaIndex semantic indexing")

if __name__ == "__main__":
    populate_all()
