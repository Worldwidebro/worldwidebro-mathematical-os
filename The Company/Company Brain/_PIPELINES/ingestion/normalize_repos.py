#!/usr/bin/env python3
"""
Phase 2.2: Repository Normalization & Deduplication
Clean, deduplicate, and validate 904 ingested repositories.
"""

import json
import logging
import sys
from typing import List, Dict, Any, Set, Tuple
from datetime import datetime
from collections import defaultdict
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/company-brain-repos/logs/normalization.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class RepositoryNormalizer:
    """Normalize, deduplicate, and validate repositories."""

    def __init__(self, input_path: str):
        """Initialize normalizer with ingested data.

        Args:
            input_path: Path to raw github-starred.json
        """
        self.input_path = input_path
        self.raw_repos = []
        self.normalized_repos = []
        self.dedup_stats = {
            'total_input': 0,
            'duplicates_removed': 0,
            'archived_flagged': 0,
            'personal_forks_flagged': 0,
            'stubs_flagged': 0,
            'final_count': 0
        }

    def load_raw_data(self) -> bool:
        """Load raw ingested repositories."""
        try:
            with open(self.input_path, 'r') as f:
                data = json.load(f)

            self.raw_repos = data.get('repositories', [])
            self.dedup_stats['total_input'] = len(self.raw_repos)

            logger.info(f"Loaded {len(self.raw_repos)} raw repositories")
            return True
        except Exception as e:
            logger.error(f"Failed to load raw data: {e}")
            return False

    def is_personal_fork(self, repo: Dict[str, Any]) -> bool:
        """Check if repo is a personal fork (low stars, recent fork, no activity).

        Args:
            repo: Repository metadata

        Returns:
            True if repo appears to be a personal fork
        """
        # Criteria: is_fork=True, stars < 10, inactive (no push in 6+ months)
        if not repo.get('is_fork', False):
            return False

        if repo.get('stars', 0) >= 10:
            return False

        # Check if pushed_at is too old (assumes recent forks should have activity)
        if repo.get('pushed_at'):
            try:
                from datetime import datetime, timezone
                pushed = datetime.fromisoformat(repo['pushed_at'].replace('Z', '+00:00'))
                now = datetime.now(timezone.utc)
                months_old = (now - pushed).days / 30

                if months_old > 6:
                    return True
            except Exception:
                pass

        return False

    def is_stub_repo(self, repo: Dict[str, Any]) -> bool:
        """Check if repo is a stub (empty, no description, no files).

        Args:
            repo: Repository metadata

        Returns:
            True if repo appears to be a stub/placeholder
        """
        # Criteria: 0 stars, no description, no pushed activity
        if repo.get('stars', 0) > 0:
            return False

        if repo.get('description'):
            return False

        if repo.get('pushed_at'):
            return False

        return True

    def is_spam_repo(self, repo: Dict[str, Any]) -> bool:
        """Check if repo looks like spam/irrelevant.

        Args:
            repo: Repository metadata

        Returns:
            True if repo appears to be spam
        """
        # Criteria: suspicious names, no language, auto-generated appearance
        name = repo.get('name', '').lower()

        spam_patterns = [
            'test-', '-test', 'temp-', '-temp', 'tmp-', '-tmp',
            'clone', 'mirror', 'backup', 'archive', 'old-',
            'draft-', 'wip-', 'experimental-', 'deprecated',
        ]

        if any(pattern in name for pattern in spam_patterns):
            if repo.get('stars', 0) < 5 and not repo.get('description'):
                return True

        # Suspicious: no language, no description, no stars, no activity
        if (not repo.get('language') and
            not repo.get('description') and
            repo.get('stars', 0) == 0 and
            not repo.get('pushed_at')):
            return True

        return False

    def deduplicate_by_url(self, repos: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int]:
        """Remove duplicate repositories by full_name.

        Args:
            repos: List of repository metadata

        Returns:
            Tuple of (deduplicated_repos, num_removed)
        """
        seen = {}
        duplicates = 0

        for repo in repos:
            full_name = repo.get('full_name', '').lower()

            if full_name in seen:
                logger.debug(f"Duplicate detected: {full_name}")
                duplicates += 1
            else:
                seen[full_name] = repo

        deduplicated = list(seen.values())
        logger.info(f"Deduplication: Removed {duplicates} exact duplicates")

        return deduplicated, duplicates

    def classify_and_normalize(self, repos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Classify repos and add normalization flags.

        Args:
            repos: List of repository metadata

        Returns:
            Normalized repository list with classification flags
        """
        normalized = []

        for repo in repos:
            is_archive = repo.get('is_archived', False)
            is_personal = self.is_personal_fork(repo)
            is_stub = self.is_stub_repo(repo)
            is_spam = self.is_spam_repo(repo)

            # Add classification flags
            repo['_flags'] = {
                'archived': is_archive,
                'personal_fork': is_personal,
                'stub': is_stub,
                'spam': is_spam,
            }

            # Flag counts
            if is_archive:
                self.dedup_stats['archived_flagged'] += 1
            if is_personal:
                self.dedup_stats['personal_forks_flagged'] += 1
            if is_stub:
                self.dedup_stats['stubs_flagged'] += 1

            normalized.append(repo)

        return normalized

    def validate_metadata(self, repos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Validate and clean metadata.

        Args:
            repos: List of repository metadata

        Returns:
            Validated repository list
        """
        validated = []

        for repo in repos:
            # Ensure required fields
            if not repo.get('full_name') or not repo.get('url'):
                logger.warning(f"Skipping repo with missing required fields: {repo.get('name')}")
                continue

            # Clean up None values in lists
            if repo.get('topics') is None:
                repo['topics'] = []

            # Normalize timestamps
            for ts_field in ['created_at', 'updated_at', 'pushed_at']:
                if repo.get(ts_field) and repo[ts_field].endswith('Z'):
                    repo[ts_field] = repo[ts_field].replace('Z', '+00:00')

            validated.append(repo)

        return validated

    def normalize(self) -> bool:
        """Execute full normalization pipeline."""
        logger.info("=" * 60)
        logger.info("Phase 2.2: Repository Normalization & Deduplication")
        logger.info("=" * 60)

        # Load raw data
        if not self.load_raw_data():
            return False

        # Deduplication by URL
        deduplicated, removed = self.deduplicate_by_url(self.raw_repos)
        self.dedup_stats['duplicates_removed'] = removed

        # Classification
        classified = self.classify_and_normalize(deduplicated)

        # Validation
        validated = self.validate_metadata(classified)

        self.normalized_repos = validated
        self.dedup_stats['final_count'] = len(validated)

        return True

    def save_normalized(self, output_path: str) -> bool:
        """Save normalized repositories to JSON."""
        output_data = {
            'metadata': {
                'normalization_timestamp': datetime.now().isoformat(),
                'total_repositories': len(self.normalized_repos),
                'statistics': self.dedup_stats,
                'version': '2.0'
            },
            'repositories': self.normalized_repos
        }

        try:
            with open(output_path, 'w') as f:
                json.dump(output_data, f, indent=2, default=str)

            logger.info(f"Saved {len(self.normalized_repos)} normalized repositories to {output_path}")
            logger.info(f"File size: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")

            return True
        except Exception as e:
            logger.error(f"Failed to save normalized data: {e}")
            return False

    def generate_report(self) -> str:
        """Generate normalization report."""
        report = f"""
PHASE 2.2 NORMALIZATION REPORT
{'=' * 60}

Input Repositories:     {self.dedup_stats['total_input']}
Duplicates Removed:     {self.dedup_stats['duplicates_removed']}
Archived Flagged:       {self.dedup_stats['archived_flagged']}
Personal Forks Flagged: {self.dedup_stats['personal_forks_flagged']}
Stubs Flagged:          {self.dedup_stats['stubs_flagged']}
Final Output:           {self.dedup_stats['final_count']}

Deduplication Rate:     {(self.dedup_stats['duplicates_removed'] / max(1, self.dedup_stats['total_input'])) * 100:.1f}%

Flags Summary:
  - {self.dedup_stats['archived_flagged']} archived repositories
  - {self.dedup_stats['personal_forks_flagged']} personal forks
  - {self.dedup_stats['stubs_flagged']} stub repositories

Status: {'COMPLETE' if self.dedup_stats['final_count'] > 0 else 'FAILED'}
"""
        return report


def main():
    """Run normalization for Phase 2.2."""
    input_path = '/tmp/company-brain-repos/raw/github-starred.json'
    output_path = '/tmp/company-brain-repos/normalized/deduplicated.json'

    # Check input exists
    if not os.path.exists(input_path):
        logger.error(f"Input file not found: {input_path}")
        logger.info("Run Phase 2.1 (github_ingest.py) first to generate raw data")
        return False

    # Run normalization
    normalizer = RepositoryNormalizer(input_path)

    if not normalizer.normalize():
        logger.error("Normalization failed")
        return False

    # Save results
    if not normalizer.save_normalized(output_path):
        logger.error("Failed to save normalized data")
        return False

    # Print report
    report = normalizer.generate_report()
    logger.info(report)

    # Save report to file
    report_path = '/tmp/company-brain-repos/logs/normalization_report.txt'
    with open(report_path, 'w') as f:
        f.write(report)
    logger.info(f"Report saved to {report_path}")

    logger.info("Phase 2.2 COMPLETE")
    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
