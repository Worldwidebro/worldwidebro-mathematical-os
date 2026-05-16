#!/usr/bin/env python3
"""
GitHub Repos Sync — Sync owned repos from GitHub to Supabase
Discovers repos in org, extracts metadata (README, topics, package.json), syncs to Supabase
"""

import os
import json
import re
from typing import Dict, List, Any, Optional
import requests
from datetime import datetime

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_ORG = os.getenv("GITHUB_ORG", "Worldwidebro")
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# Known owned repos (canonical list)
OWNED_REPOS = {
    'pitch-kit',
    'venture-hub',
    'mission-control',
    'omi',
    'iza-os-rag-system',
    'LightRAG',
    'mcp-dashboard',
    'venture-factory-core',
    'vibetunnel',
    'vibe-kanban',
    'ai-venture-studio-template',
    'autonomous-venture-studio',
    'security-stack',
    'opensre',
    'bw-001-lash-extension-studio',
    'con-001-ace-construction',
    'civilization-os-local',
    'thunderbolt'
}

# Specific repos to fetch (owner/repo format) - for repos not in primary account
SPECIFIC_REPOS = [
    'crshdn/mission-control',
    'HKUDS/LightRAG',
]


class GitHubReposSync:
    """Sync GitHub repos to Supabase"""

    def __init__(self):
        self.gh_session = requests.Session()
        if GITHUB_TOKEN:
            self.gh_session.headers.update({"Authorization": f"token {GITHUB_TOKEN}"})

        self.sb_session = requests.Session()
        self.sb_session.headers.update({
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        })

        self.repos_metadata = {}

    def fetch_user_repos(self, username: str) -> List[Dict[str, Any]]:
        """Fetch all repos from GitHub user"""
        print(f"📡 Fetching repos from user {username}...")

        repos = []
        page = 1
        while True:
            try:
                response = self.gh_session.get(
                    f"https://api.github.com/users/{username}/repos",
                    params={"per_page": 100, "page": page, "type": "all"}
                )
                if response.status_code == 200:
                    batch = response.json()
                    if not batch:
                        break
                    repos.extend(batch)
                    page += 1
                else:
                    print(f"❌ Failed to fetch repos: {response.status_code}")
                    if response.status_code == 401:
                        print("   (Set GITHUB_TOKEN for authenticated requests)")
                    break
            except Exception as e:
                print(f"❌ Error fetching repos: {e}")
                break

        print(f"✅ Found {len(repos)} repos from user {username}")
        return repos

    def fetch_specific_repos(self, repo_specs: List[str]) -> List[Dict[str, Any]]:
        """Fetch specific repos by owner/repo format"""
        repos = []
        print(f"📡 Fetching {len(repo_specs)} specific repos...")

        for spec in repo_specs:
            try:
                owner, repo_name = spec.split('/')
                response = self.gh_session.get(f"https://api.github.com/repos/{owner}/{repo_name}")
                if response.status_code == 200:
                    repos.append(response.json())
                    print(f"  ✓ {spec}")
                else:
                    print(f"  ✗ {spec} (404)")
            except Exception as e:
                print(f"  ✗ {spec} ({e})")

        return repos

    def extract_readme_purpose(self, owner: str, repo: str) -> Optional[str]:
        """Extract purpose/description from README"""
        try:
            response = self.gh_session.get(
                f"https://api.github.com/repos/{owner}/{repo}/readme",
                headers={"Accept": "application/vnd.github.v3.raw"}
            )
            if response.status_code == 200:
                readme = response.text
                # Extract first non-empty line or first paragraph
                lines = readme.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        return line[:200]  # First 200 chars
                return None
            return None
        except Exception as e:
            return None

    def extract_package_json_purpose(self, owner: str, repo: str) -> Optional[Dict[str, Any]]:
        """Extract description and keywords from package.json"""
        try:
            response = self.gh_session.get(
                f"https://api.github.com/repos/{owner}/{repo}/contents/package.json"
            )
            if response.status_code == 200:
                data = response.json()
                if 'content' in data:
                    import base64
                    content = base64.b64decode(data['content']).decode('utf-8')
                    pkg = json.loads(content)
                    return {
                        "description": pkg.get("description"),
                        "keywords": pkg.get("keywords", [])
                    }
            return None
        except Exception:
            return None

    def extract_topics(self, repo_data: Dict[str, Any]) -> List[str]:
        """Extract topics from repo"""
        topics = repo_data.get('topics', []) or []
        return [t for t in topics if t]

    def infer_capabilities(self, repo_name: str, topics: List[str], description: str, keywords: List[str]) -> List[str]:
        """Infer capabilities from repo metadata"""
        capabilities = set()

        # Add topics as capabilities
        capabilities.update(topics)

        # Keyword mapping
        keyword_map = {
            'auth': ['authentication', 'oauth', 'oidc', 'sessions', 'login'],
            'portfolio': ['portfolio', 'cap-table', 'equity', 'fundraising'],
            'pitch': ['pitch', 'deck', 'presentation', 'slide'],
            'dashboard': ['dashboard', 'analytics', 'monitoring', 'visualization'],
            'api': ['api', 'rest', 'graphql', 'sdk'],
            'database': ['database', 'postgres', 'sql'],
            'payments': ['payments', 'billing', 'stripe', 'payments-processing'],
            'hrms': ['hr', 'payroll', 'employees', 'team'],
            'knowledge': ['knowledge', 'graph', 'rag', 'embedding'],
            'rag': ['rag', 'retrieval', 'augmented', 'generation'],
        }

        desc_lower = description.lower() if description else ""

        for feature, keywords_list in keyword_map.items():
            for kw in keywords_list:
                if kw in desc_lower or kw in keywords:
                    capabilities.add(feature)

        return sorted(list(capabilities))

    def fetch_repo_metadata(self, owner: str, repo_name: str, repo_data: Dict[str, Any]) -> Dict[str, Any]:
        """Fetch and process all metadata for a repo"""
        print(f"  Fetching metadata for {repo_name}...")

        topics = self.extract_topics(repo_data)

        description = repo_data.get('description', '')
        if not description:
            description = self.extract_readme_purpose(owner, repo_name) or ''

        pkg_info = self.extract_package_json_purpose(owner, repo_name) or {}
        keywords = pkg_info.get('keywords', [])

        capabilities = self.infer_capabilities(repo_name, topics, description, keywords)

        return {
            'repo_id': str(repo_data.get('id', '')),
            'name': repo_name,
            'github_url': repo_data.get('html_url'),
            'owner': owner,
            'description': description,
            'purpose': description,
            'capabilities': capabilities,  # Send as array, not JSON string
            'language': repo_data.get('language'),
            'github_stars': repo_data.get('stargazers_count', 0),
            'repo_type': 'owned' if repo_name in OWNED_REPOS else 'starred',
            'integration_effort': self._estimate_integration_effort(repo_name, capabilities),
        }

    def _estimate_integration_effort(self, repo_name: str, capabilities: List[str]) -> str:
        """Estimate integration effort: low/medium/high"""
        low_effort_indicators = ['utility', 'helper', 'library', 'sdk', 'api']
        high_effort_indicators = ['platform', 'framework', 'system', 'core', 'infrastructure']

        description_lower = repo_name.lower()

        if any(ind in description_lower for ind in high_effort_indicators):
            return 'high'
        elif any(ind in description_lower for ind in low_effort_indicators):
            return 'low'
        else:
            return 'medium'

    def sync_to_supabase(self, repos_metadata: List[Dict[str, Any]]) -> bool:
        """Upsert repos to Supabase"""
        print(f"\n📤 Syncing {len(repos_metadata)} repos to Supabase...")

        try:
            response = self.sb_session.post(
                f"{SUPABASE_URL}/rest/v1/repos",
                params={"on_conflict": "repo_id"},
                json=repos_metadata
            )
            if response.status_code in [201, 200]:
                print(f"✅ Synced {len(repos_metadata)} repos to Supabase")
                return True
            elif response.status_code == 409:
                print(f"✅ Repos already exist in Supabase (no update needed)")
                return True
            else:
                print(f"❌ Sync failed: {response.status_code}")
                print(f"   Response: {response.text[:200]}")
                return False
        except Exception as e:
            print(f"❌ Sync error: {e}")
            return False

    def run(self):
        """Run the sync"""
        print("\n" + "="*80)
        print("GITHUB REPOS SYNC — Sync GitHub repos to Supabase")
        print("="*80 + "\n")

        if not GITHUB_TOKEN:
            print("⚠️  GITHUB_TOKEN not set. Using unauthenticated requests (rate limited).")
            print("   Set GITHUB_TOKEN for 5000 req/hr instead of 60 req/hr.\n")

        if not SUPABASE_KEY:
            print("❌ SUPABASE_KEY not set. Cannot sync.")
            return

        # Fetch repos from GitHub
        repos = []
        user_repos = []
        specific_repos = []

        # Fetch from primary user account
        user_repos = self.fetch_user_repos(GITHUB_ORG)
        repos.extend(user_repos)

        # Fetch specific repos from other owners
        if SPECIFIC_REPOS:
            specific_repos = self.fetch_specific_repos(SPECIFIC_REPOS)
            repos.extend(specific_repos)

        if not repos:
            print("❌ No repos found")
            return

        # Extract metadata
        print(f"\n🔍 Extracting metadata from {len(repos)} repos...")
        repos_metadata = []

        for repo in repos:
            metadata = self.fetch_repo_metadata(GITHUB_ORG, repo['name'], repo)
            repos_metadata.append(metadata)

            # Summary line
            repo_type = "🔵 OWNED" if metadata['repo_type'] == 'owned' else "⭐ STARRED"
            caps = metadata['capabilities'] if metadata['capabilities'] else []
            caps_str = ", ".join(caps[:3]) if caps else "none"
            print(f"    {repo_type} {repo['name']:30} | {caps_str}")

        # Sync to Supabase
        self.sync_to_supabase(repos_metadata)

        # Summary
        owned_count = sum(1 for m in repos_metadata if m['repo_type'] == 'owned')
        starred_count = len(repos_metadata) - owned_count

        print(f"\n" + "="*80)
        print(f"📊 SYNC SUMMARY")
        print("="*80)
        print(f"  Total repos:       {len(repos_metadata)}")
        print(f"  Owned:             {owned_count}")
        print(f"  Starred:           {starred_count}")
        print(f"  User repos:        {len(user_repos)}")
        print(f"  Specific repos:    {len(specific_repos)}")
        print(f"  Timestamp:         {datetime.utcnow().isoformat()}")
        print("="*80 + "\n")


def main():
    sync = GitHubReposSync()
    sync.run()


if __name__ == "__main__":
    main()
