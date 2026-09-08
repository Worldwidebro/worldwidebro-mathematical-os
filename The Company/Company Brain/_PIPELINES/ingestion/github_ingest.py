#!/usr/bin/env python3
"""
Phase 2.1: GitHub Repository Ingestion
Fetch all starred repositories from GitHub API with full metadata.
"""

import json
import time
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any
import os
import sys

try:
    import requests
except ImportError:
    print("ERROR: requests library not installed. Install with: pip install requests")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/company-brain-repos/logs/ingestion.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class GitHubIngester:
    """GitHub API client for starred repositories ingestion."""

    BASE_URL = "https://api.github.com"
    RATE_LIMIT_WINDOW = 3600  # seconds
    RATE_LIMIT_BUFFER = 10    # keep 10 requests in reserve

    def __init__(self, token: Optional[str] = None):
        """Initialize GitHub API client.

        Args:
            token: GitHub personal access token. If None, uses GITHUB_TOKEN env var.
        """
        self.token = token or os.environ.get('GITHUB_TOKEN')
        if not self.token:
            logger.error("No GitHub token provided. Set GITHUB_TOKEN env var or pass token parameter.")
            sys.exit(1)

        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        })

        self.rate_limit_remaining = None
        self.rate_limit_reset = None
        self.repos_ingested = 0

    def check_rate_limit(self) -> bool:
        """Check current rate limit status."""
        try:
            resp = self.session.get(f'{self.BASE_URL}/rate_limit')
            data = resp.json()

            self.rate_limit_remaining = data['resources']['core']['remaining']
            self.rate_limit_reset = data['resources']['core']['reset']

            logger.info(f"Rate limit: {self.rate_limit_remaining}/5000 requests remaining")

            if self.rate_limit_remaining < self.RATE_LIMIT_BUFFER:
                reset_time = datetime.fromtimestamp(self.rate_limit_reset)
                logger.warning(f"Rate limit exhausted. Resets at {reset_time}")
                return False

            return True
        except Exception as e:
            logger.error(f"Failed to check rate limit: {e}")
            return False

    def fetch_starred_repos(self, per_page: int = 100) -> List[Dict[str, Any]]:
        """Fetch all starred repositories using pagination.

        Args:
            per_page: Repositories per API request (max 100)

        Returns:
            List of repository metadata dictionaries
        """
        if not self.check_rate_limit():
            logger.error("Rate limit exceeded before ingestion started")
            return []

        all_repos = []
        page = 1
        total_expected = None

        while True:
            logger.info(f"Fetching page {page}...")

            try:
                url = f'{self.BASE_URL}/user/starred'
                params = {
                    'per_page': per_page,
                    'page': page,
                    'sort': 'updated',
                    'direction': 'desc'
                }

                resp = self.session.get(url, params=params, timeout=10)

                # Check rate limit headers
                if 'X-RateLimit-Remaining' in resp.headers:
                    self.rate_limit_remaining = int(resp.headers['X-RateLimit-Remaining'])

                if resp.status_code == 401:
                    logger.error("Authentication failed. Invalid GitHub token.")
                    return []
                elif resp.status_code == 403:
                    logger.error("Access forbidden. Check token scopes (needs 'public_repo' or 'repo').")
                    return []
                elif resp.status_code != 200:
                    logger.error(f"API error {resp.status_code}: {resp.text}")
                    return []

                repos = resp.json()

                if not repos:
                    logger.info(f"No more repositories. Total ingested: {self.repos_ingested}")
                    break

                # Extract metadata from each repo
                for repo in repos:
                    repo_data = {
                        'id': repo['id'],
                        'name': repo['name'],
                        'full_name': repo['full_name'],
                        'url': repo['html_url'],
                        'api_url': repo['url'],
                        'description': repo['description'],
                        'stars': repo['stargazers_count'],
                        'forks': repo['forks_count'],
                        'open_issues': repo['open_issues_count'],
                        'language': repo['language'],
                        'license': repo['license']['name'] if repo.get('license') else None,
                        'topics': repo.get('topics', []),
                        'is_private': repo['private'],
                        'is_archived': repo['archived'],
                        'is_fork': repo['fork'],
                        'created_at': repo['created_at'],
                        'updated_at': repo['updated_at'],
                        'pushed_at': repo['pushed_at'],
                        'homepage': repo['homepage'],
                        'default_branch': repo['default_branch'],
                    }
                    all_repos.append(repo_data)
                    self.repos_ingested += 1

                logger.info(f"Page {page}: {len(repos)} repos ingested (total: {self.repos_ingested})")

                # Check rate limit before continuing
                if self.rate_limit_remaining is not None and self.rate_limit_remaining < self.RATE_LIMIT_BUFFER:
                    logger.warning(f"Approaching rate limit. Stopping at page {page}")
                    break

                # Respectful delay
                time.sleep(0.5)
                page += 1

            except requests.exceptions.Timeout:
                logger.error(f"Request timeout on page {page}")
                return all_repos
            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {e}")
                return all_repos
            except Exception as e:
                logger.error(f"Unexpected error on page {page}: {e}")
                return all_repos

        return all_repos

    def save_to_json(self, repos: List[Dict[str, Any]], output_path: str):
        """Save ingested repositories to JSON file."""
        output_data = {
            'metadata': {
                'ingestion_timestamp': datetime.now().isoformat(),
                'total_repos': len(repos),
                'version': '1.0'
            },
            'repositories': repos
        }

        try:
            with open(output_path, 'w') as f:
                json.dump(output_data, f, indent=2, default=str)

            logger.info(f"Saved {len(repos)} repositories to {output_path}")
            logger.info(f"File size: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")

            return True
        except Exception as e:
            logger.error(f"Failed to save JSON: {e}")
            return False


def main():
    """Run GitHub ingestion for Phase 2.1."""
    output_path = '/tmp/company-brain-repos/raw/github-starred.json'

    logger.info("=" * 60)
    logger.info("Phase 2.1: GitHub Repository Ingestion")
    logger.info("=" * 60)

    # Initialize ingester
    ingester = GitHubIngester()

    # Fetch all starred repos
    logger.info("Starting repository fetch...")
    repos = ingester.fetch_starred_repos()

    if not repos:
        logger.error("No repositories ingested. Check authentication and rate limits.")
        return False

    # Save to JSON
    logger.info(f"Ingestion complete: {len(repos)} repositories")
    success = ingester.save_to_json(repos, output_path)

    if success:
        logger.info("Phase 2.1 COMPLETE")
        return True
    else:
        logger.error("Phase 2.1 FAILED - could not save results")
        return False


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
