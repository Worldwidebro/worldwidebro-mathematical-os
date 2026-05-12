#!/usr/bin/env python3
"""
Option A: Repo Metadata Foundation
Populates Supabase repos table with structured metadata for all 853 starred repos.

This script:
1. Parses starred-repos-capabilities.md to extract repo names
2. Queries GitHub API for metadata (stars, last commit, contributors)
3. Uses Ollama to infer: purpose, capabilities, integration_effort, cost, etc.
4. Maps repos to ventures based on required capabilities
5. Inserts all data into Supabase repos table
"""

import os
import json
import re
import requests
from typing import Dict, List, Optional, Any
from datetime import datetime
import time
from collections import defaultdict
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Environment vars
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY", "")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://100.87.214.70:11434")

# Constants
REPOS_CAPABILITIES_FILE = "/Users/acebless/Documents/starred-repos-capabilities.md"
BATCH_SIZE = 10
GITHUB_API_RATE_LIMIT_DELAY = 0.5  # seconds between requests to avoid rate limiting
OLLAMA_TIMEOUT = 30


class RepoMetadataPopulator:
    def __init__(self):
        self.github_headers = {}
        if GITHUB_TOKEN:
            self.github_headers = {"Authorization": f"token {GITHUB_TOKEN}"}

        self.supabase_headers = {
            "apikey": SUPABASE_SERVICE_KEY,
            "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
            "Content-Type": "application/json"
        }

        self.repos = []
        self.ventures = {}
        self.capability_to_ventures = defaultdict(list)
        self.stats = {
            "total_repos": 0,
            "repos_with_github_data": 0,
            "repos_with_ollama_inference": 0,
            "repos_inserted": 0,
            "repos_failed": 0,
            "errors": []
        }

    def parse_repos_from_markdown(self) -> List[str]:
        """Extract repo names from starred-repos-capabilities.md"""
        logger.info(f"Parsing repos from {REPOS_CAPABILITIES_FILE}")

        repos = set()
        try:
            with open(REPOS_CAPABILITIES_FILE, 'r') as f:
                content = f.read()

            # Pattern 1: repo names in code blocks (e.g., llama_index)
            code_block_pattern = r'^\s*(\w+(?:[_-]\w+)*)\s*→'
            for line in content.split('\n'):
                match = re.match(code_block_pattern, line)
                if match:
                    repo = match.group(1)
                    if repo.lower() not in ['business', 'ventures', 'use']:
                        repos.add(repo)

            # Pattern 2: repo names in inline code (e.g., `llama_index`)
            inline_pattern = r'`([a-zA-Z0-9_-]+)`'
            for match in re.finditer(inline_pattern, content):
                repo = match.group(1)
                if len(repo) > 2 and repo.lower() not in ['ai', 'rag', 'api']:
                    repos.add(repo)

            # Pattern 3: In tables with pipes
            table_pattern = r'\|\s*([a-zA-Z0-9_-]+)\s*,'
            for match in re.finditer(table_pattern, content):
                repos.add(match.group(1))

        except Exception as e:
            logger.error(f"Error parsing markdown: {e}")
            self.stats["errors"].append(f"Markdown parse error: {e}")

        self.repos = sorted(list(repos))
        logger.info(f"Found {len(self.repos)} unique repos from markdown")
        return self.repos

    def get_github_metadata(self, repo_name: str) -> Optional[Dict]:
        """Query GitHub API for repo metadata"""
        # Try with owner/repo format first (common pattern)
        possible_repos = [
            repo_name,  # just the name
            f"Worldwidebro/{repo_name}",  # assume Worldwidebro as owner
            # Could add more patterns if needed
        ]

        for full_repo in possible_repos:
            try:
                url = f"https://api.github.com/repos/{full_repo}"
                response = requests.get(url, headers=self.github_headers, timeout=10)
                time.sleep(GITHUB_API_RATE_LIMIT_DELAY)

                if response.status_code == 200:
                    data = response.json()
                    return {
                        "repo_id": full_repo,
                        "github_url": data.get("html_url", ""),
                        "owner": data.get("owner", {}).get("login", ""),
                        "github_stars": data.get("stargazers_count", 0),
                        "last_commit_date": data.get("pushed_at", ""),
                        "language": data.get("language", ""),
                        "description": data.get("description", ""),
                        "license": data.get("license", {}).get("spdx_id", "") if data.get("license") else "",
                    }
            except Exception as e:
                logger.debug(f"Failed to fetch {full_repo}: {e}")
                continue

        return None

    def infer_repo_metadata_with_ollama(self, repo_name: str, description: str = "") -> Optional[Dict]:
        """Use Ollama to infer repo capabilities, integration effort, etc."""
        prompt = f"""Analyze this software repository and provide structured metadata:

Repository: {repo_name}
Description: {description}

Provide JSON with these fields:
{{
  "purpose": "one-line purpose (what does this solve?)",
  "capabilities": ["array", "of", "technical capabilities"],
  "integration_effort": "low|medium|high|very_high",
  "estimated_integration_days": <int days to integrate>,
  "cost_estimate": "free|$1K-5K|$5K-20K|$20K+",
  "startup_complexity": "simple|moderate|complex|very_complex",
  "business_use_cases": ["array", "of", "business problems it solves"],
  "stack": ["technology", "stack", "languages"],
  "maturity": "experimental|beta|production|mature"
}}

Return ONLY valid JSON, no markdown code blocks."""

        try:
            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": "qwen2.5:32b",
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.3  # Lower temperature for consistency
                },
                timeout=OLLAMA_TIMEOUT
            )

            if response.status_code == 200:
                result = response.json()
                response_text = result.get("response", "").strip()

                # Extract JSON from response (might have extra text)
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                if json_match:
                    metadata = json.loads(json_match.group())
                    return metadata
        except Exception as e:
            logger.debug(f"Ollama inference failed for {repo_name}: {e}")

        return None

    def fetch_all_ventures(self) -> Dict:
        """Fetch all ventures from Supabase to map capabilities"""
        logger.info("Fetching ventures from Supabase")

        try:
            url = f"{SUPABASE_URL}/rest/v1/ventures?select=id,name,sector,required_capabilities"
            response = requests.get(url, headers=self.supabase_headers, timeout=15)

            if response.status_code == 200:
                ventures = response.json()
                ventures_by_id = {v["id"]: v for v in ventures}

                # Build capability -> ventures mapping
                for venture in ventures:
                    caps = venture.get("required_capabilities", [])
                    if isinstance(caps, list):
                        for cap in caps:
                            self.capability_to_ventures[cap.lower()].append(venture["id"])

                logger.info(f"Fetched {len(ventures)} ventures with {len(self.capability_to_ventures)} unique capabilities")
                return ventures_by_id
        except Exception as e:
            logger.error(f"Failed to fetch ventures: {e}")
            self.stats["errors"].append(f"Ventures fetch error: {e}")

        return {}

    def map_repos_to_ventures(self, repo_capabilities: List[str]) -> tuple:
        """Find which ventures need repos with these capabilities"""
        venture_ids = []
        sectors = []

        for cap in repo_capabilities:
            cap_lower = cap.lower()
            if cap_lower in self.capability_to_ventures:
                for venture_id in self.capability_to_ventures[cap_lower]:
                    if venture_id not in venture_ids:
                        venture_ids.append(venture_id)
                        # Extract sector from venture if available
                        if venture_id in self.ventures:
                            sector = self.ventures[venture_id].get("sector")
                            if sector and sector not in sectors:
                                sectors.append(sector)

        return venture_ids, sectors

    def insert_repo_to_supabase(self, repo_data: Dict) -> bool:
        """Insert single repo record into Supabase"""
        try:
            url = f"{SUPABASE_URL}/rest/v1/repos"

            # Prepare data for insertion
            payload = {
                "repo_id": repo_data.get("repo_id"),
                "name": repo_data.get("name"),
                "github_url": repo_data.get("github_url"),
                "owner": repo_data.get("owner"),
                "purpose": repo_data.get("purpose"),
                "description": repo_data.get("description"),
                "maturity": repo_data.get("maturity"),
                "language": repo_data.get("language"),
                "license": repo_data.get("license"),
                "capabilities": repo_data.get("capabilities", []),
                "stack": repo_data.get("stack", []),
                "business_use_cases": repo_data.get("business_use_cases", []),
                "integration_effort": repo_data.get("integration_effort"),
                "estimated_integration_days": repo_data.get("estimated_integration_days"),
                "cost_estimate": repo_data.get("cost_estimate"),
                "startup_complexity": repo_data.get("startup_complexity"),
                "github_stars": repo_data.get("github_stars", 0),
                "last_commit_date": repo_data.get("last_commit_date"),
                "contributors": repo_data.get("contributors", 0),
                "ventures_count": len(repo_data.get("venture_ids", [])),
                "venture_ids": repo_data.get("venture_ids", []),
                "sectors": repo_data.get("sectors", []),
                "verification_status": "verified" if repo_data.get("github_url") else "pending",
                "indexed_at": datetime.utcnow().isoformat(),
            }

            # Remove None values
            payload = {k: v for k, v in payload.items() if v is not None}

            response = requests.post(
                url,
                headers=self.supabase_headers,
                json=payload,
                timeout=10
            )

            if response.status_code in [200, 201]:
                return True
            else:
                logger.warning(f"Insert failed for {repo_data.get('name')}: {response.status_code} {response.text[:200]}")
                self.stats["errors"].append(f"Insert failed for {repo_data.get('name')}: {response.status_code}")
                return False

        except Exception as e:
            logger.error(f"Exception inserting repo {repo_data.get('name')}: {e}")
            self.stats["errors"].append(f"Exception inserting {repo_data.get('name')}: {str(e)}")
            return False

    def process_all_repos(self):
        """Main processing loop"""
        logger.info("=" * 80)
        logger.info("REPO METADATA POPULATION - OPTION A FOUNDATION")
        logger.info("=" * 80)

        # Step 1: Parse repos from markdown
        self.parse_repos_from_markdown()
        self.stats["total_repos"] = len(self.repos)

        # Step 2: Fetch all ventures for mapping
        self.ventures = self.fetch_all_ventures()

        # Step 3: Process each repo
        processed = 0
        for i, repo_name in enumerate(self.repos, 1):
            logger.info(f"\n[{i}/{len(self.repos)}] Processing: {repo_name}")

            repo_data = {"name": repo_name, "repo_id": repo_name}

            # Get GitHub metadata
            github_data = self.get_github_metadata(repo_name)
            if github_data:
                repo_data.update(github_data)
                self.stats["repos_with_github_data"] += 1
                logger.info(f"  ✓ GitHub: {repo_data.get('github_stars', 0)} stars")

            # Infer with Ollama
            ollama_data = self.infer_repo_metadata_with_ollama(
                repo_name,
                repo_data.get("description", "")
            )
            if ollama_data:
                repo_data.update(ollama_data)
                self.stats["repos_with_ollama_inference"] += 1
                logger.info(f"  ✓ Ollama: {ollama_data.get('purpose', 'N/A')[:60]}")

            # Map to ventures
            venture_ids, sectors = self.map_repos_to_ventures(
                repo_data.get("capabilities", [])
            )
            repo_data["venture_ids"] = venture_ids
            repo_data["sectors"] = sectors

            if venture_ids:
                logger.info(f"  ✓ Mapped to {len(venture_ids)} ventures in {len(sectors)} sectors")

            # Insert to Supabase
            if self.insert_repo_to_supabase(repo_data):
                self.stats["repos_inserted"] += 1
                logger.info(f"  ✓ Inserted to Supabase")
            else:
                self.stats["repos_failed"] += 1

            processed += 1

            # Show progress every 10 repos
            if processed % 10 == 0:
                logger.info(f"\n--- Progress: {processed}/{len(self.repos)} repos processed ---\n")

        self.print_summary()

    def print_summary(self):
        """Print final summary"""
        logger.info("\n" + "=" * 80)
        logger.info("POPULATION SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Total repos parsed:          {self.stats['total_repos']}")
        logger.info(f"Repos with GitHub data:      {self.stats['repos_with_github_data']}")
        logger.info(f"Repos with Ollama inference: {self.stats['repos_with_ollama_inference']}")
        logger.info(f"Repos successfully inserted: {self.stats['repos_inserted']}")
        logger.info(f"Repos failed:                {self.stats['repos_failed']}")

        if self.stats["errors"]:
            logger.warning(f"\nEncountered {len(self.stats['errors'])} errors:")
            for error in self.stats["errors"][:10]:
                logger.warning(f"  - {error}")

        logger.info("=" * 80)


def main():
    """Entry point"""
    populator = RepoMetadataPopulator()
    populator.process_all_repos()


if __name__ == "__main__":
    main()
