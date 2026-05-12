#!/usr/bin/env python3
"""
Option C: Local Semantic Indexing with SentenceTransformers
Creates embeddings for all repos using local model - no external API keys needed.

This script:
1. Reads repos from Supabase (already populated by Option A)
2. For each repo: Combines name + purpose + description
3. Creates 768-dim embeddings using sentence-transformers/all-MiniLM-L6-v2
4. Pads to 1536 dims to match Supabase schema
5. Stores vectors in repos.embedding column
"""

import os
import json
import logging
import requests
from typing import Optional, List, Dict
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Environment vars
SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

# Constants
BATCH_SIZE = 5
EMBEDDING_DIM = 1536  # Target dimension for Supabase


class LocalEmbeddingIndexer:
    def __init__(self):
        self.supabase_headers = {
            "apikey": SUPABASE_SERVICE_KEY,
            "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
            "Content-Type": "application/json"
        }

        # Try to import sentence-transformers, install if needed
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            logger.info("✓ Loaded SentenceTransformer model (all-MiniLM-L6-v2)")
        except ImportError:
            logger.info("Installing sentence-transformers...")
            os.system("pip install sentence-transformers")
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            logger.info("✓ Loaded SentenceTransformer model")

        self.repos = []
        self.stats = {
            "total_repos": 0,
            "embeddings_created": 0,
            "embeddings_stored": 0,
            "errors": []
        }

    def fetch_repos_to_index(self) -> List[Dict]:
        """Fetch all repos from Supabase that need indexing"""
        logger.info("Fetching repos to index from Supabase")

        try:
            url = f"{SUPABASE_URL}/rest/v1/repos?select=id,name,github_url,description,purpose&order=created_at.desc"
            response = requests.get(url, headers=self.supabase_headers, timeout=15)

            if response.status_code == 200:
                repos = response.json()
                self.repos = repos
                logger.info(f"Fetched {len(repos)} repos for indexing")
                return repos
            else:
                logger.error(f"Failed to fetch repos: {response.status_code}")
                self.stats["errors"].append(f"Fetch repos error: {response.status_code}")

        except Exception as e:
            logger.error(f"Exception fetching repos: {e}")
            self.stats["errors"].append(f"Exception: {str(e)}")

        return []

    def create_embedding(self, text: str) -> Optional[List[float]]:
        """Create embedding using local SentenceTransformer model"""
        if not text or len(text) < 10:
            return None

        try:
            embedding = self.model.encode(text, convert_to_numpy=True)

            # Convert numpy array to list
            embedding_list = embedding.tolist() if hasattr(embedding, 'tolist') else list(embedding)

            # Pad to 1536 dims (SentenceTransformer returns 384 for all-MiniLM-L6-v2)
            if len(embedding_list) < EMBEDDING_DIM:
                embedding_list = embedding_list + [0.0] * (EMBEDDING_DIM - len(embedding_list))

            # If somehow longer, truncate
            return embedding_list[:EMBEDDING_DIM]
        except Exception as e:
            logger.debug(f"Embedding creation failed: {e}")
            return None

    def store_embedding(self, repo_id: str, embedding: List[float]) -> bool:
        """Store embedding in Supabase"""
        try:
            # Find the repo's UUID from our repo list
            repo_record = None
            for repo in self.repos:
                if repo.get("id") == repo_id:
                    repo_record = repo
                    break

            if not repo_record or "id" not in repo_record:
                logger.warning(f"Could not find repo record for {repo_id}")
                return False

            uuid = repo_record["id"]

            # Update repo with embedding
            url = f"{SUPABASE_URL}/rest/v1/repos?id=eq.{uuid}"
            response = requests.patch(
                url,
                headers=self.supabase_headers,
                json={"embedding": embedding},
                timeout=10
            )

            if response.status_code in [200, 204]:
                return True
            else:
                logger.warning(f"Store embedding failed for {repo_id}: {response.status_code}")
                self.stats["errors"].append(f"Store embedding failed for {repo_id}: {response.status_code}")
                return False

        except Exception as e:
            logger.error(f"Exception storing embedding for {repo_id}: {e}")
            self.stats["errors"].append(f"Exception storing {repo_id}: {str(e)}")
            return False

    def index_all_repos(self):
        """Main indexing loop"""
        logger.info("=" * 80)
        logger.info("LOCAL SEMANTIC INDEXING - SENTENCE-TRANSFORMERS")
        logger.info("=" * 80)

        # Fetch repos
        if not self.fetch_repos_to_index():
            logger.error("Failed to fetch repos, aborting")
            return

        self.stats["total_repos"] = len(self.repos)

        # Process each repo
        for i, repo in enumerate(self.repos, 1):
            repo_id = repo.get("id")
            repo_name = repo.get("name")
            logger.info(f"\n[{i}/{len(self.repos)}] Indexing: {repo_name}")

            # Build text for embedding: name + purpose + description
            text_parts = [
                repo.get("name", ""),
                repo.get("purpose", ""),
                repo.get("description", ""),
            ]
            combined_text = " ".join(filter(None, text_parts))

            # Create embedding
            if combined_text and len(combined_text) > 20:
                embedding = self.create_embedding(combined_text)
                if embedding:
                    self.stats["embeddings_created"] += 1
                    logger.info(f"  ✓ Embedding created ({len(embedding)} dims)")

                    # Store embedding
                    if self.store_embedding(repo_id, embedding):
                        self.stats["embeddings_stored"] += 1
                        logger.info(f"  ✓ Stored in Supabase")
                    else:
                        logger.warning(f"  ✗ Failed to store embedding")
                else:
                    logger.warning(f"  ✗ Failed to create embedding")
            else:
                logger.warning(f"  ⊗ Insufficient content for embedding")

            # Show progress
            if i % 10 == 0:
                logger.info(f"\n--- Progress: {i}/{len(self.repos)} repos indexed ---\n")

        self.print_summary()

    def print_summary(self):
        """Print final summary"""
        logger.info("\n" + "=" * 80)
        logger.info("INDEXING SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Total repos to index:        {self.stats['total_repos']}")
        logger.info(f"Embeddings created:          {self.stats['embeddings_created']}")
        logger.info(f"Embeddings stored in DB:     {self.stats['embeddings_stored']}")
        logger.info(f"Success rate:                {self.stats['embeddings_stored']/self.stats['total_repos']*100:.1f}%")

        if self.stats["errors"]:
            logger.warning(f"\nEncountered {len(self.stats['errors'])} errors:")
            for error in self.stats["errors"][:10]:
                logger.warning(f"  - {error}")

        logger.info("=" * 80)
        logger.info("Phase 2C: Embeddings complete. Repos are now semantically indexed.")
        logger.info("Next: Deploy Backstage service catalog (Phase 2B) or run semantic queries")
        logger.info("=" * 80)


def main():
    """Entry point"""
    indexer = LocalEmbeddingIndexer()
    indexer.index_all_repos()


if __name__ == "__main__":
    main()
