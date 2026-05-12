#!/usr/bin/env python3
"""
Option C: LlamaIndex Semantic Indexing Layer
Creates embeddings for all repos and stores them in Supabase for semantic search.

This script:
1. Reads repos from Supabase (already populated by Option A)
2. For each repo: Downloads README, extracts key content
3. Creates embeddings using OpenAI or local model
4. Stores vectors in repos.embedding column (1536 dims)
5. Enables semantic queries: "What repos solve real-time collaboration?"
"""

import os
import json
import re
import requests
import base64
from typing import Optional, List, Dict, Any
import logging
import time
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Environment vars
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://100.87.214.70:11434")

# Choose embedding model: "openai" or "ollama"
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "ollama")  # Default to local Ollama

# Constants
BATCH_SIZE = 5
GITHUB_API_DELAY = 0.5
EMBEDDING_DIM = 1536  # OpenAI embedding size
CONTENT_EXTRACTION_TIMEOUT = 15


class RepositoryIndexer:
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
        self.stats = {
            "total_repos": 0,
            "content_extracted": 0,
            "embeddings_created": 0,
            "embeddings_stored": 0,
            "errors": []
        }

    def fetch_repos_to_index(self) -> List[Dict]:
        """Fetch all repos from Supabase that need indexing"""
        logger.info("Fetching repos to index from Supabase")

        try:
            url = f"{SUPABASE_URL}/rest/v1/repos?select=id,repo_id,name,github_url,description,purpose&order=created_at.desc"
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

    def extract_readme_content(self, repo_id: str, github_url: str) -> Optional[str]:
        """Download and extract README content from GitHub repo"""
        if not github_url:
            return None

        try:
            # Parse owner/repo from URL
            match = re.search(r'github\.com/([^/]+)/([^/]+)', github_url)
            if not match:
                logger.debug(f"Could not parse GitHub URL: {github_url}")
                return None

            owner, repo = match.groups()
            readme_url = f"https://api.github.com/repos/{owner}/{repo}/readme"

            response = requests.get(
                readme_url,
                headers={**self.github_headers, "Accept": "application/vnd.github.v3.raw"},
                timeout=CONTENT_EXTRACTION_TIMEOUT
            )
            time.sleep(GITHUB_API_DELAY)

            if response.status_code == 200:
                readme_text = response.text
                # Clean up markdown
                readme_text = re.sub(r'!\[.*?\]\(.*?\)', '[image]', readme_text)  # Remove images
                readme_text = re.sub(r'\[.*?\]\((.*?)\)', r'\1', readme_text)  # Remove links
                logger.debug(f"Extracted README for {repo_id} ({len(readme_text)} chars)")
                return readme_text[:5000]  # Limit to first 5000 chars

        except Exception as e:
            logger.debug(f"Failed to extract README for {repo_id}: {e}")

        return None

    def create_embeddings_with_openai(self, text: str) -> Optional[List[float]]:
        """Create embeddings using OpenAI API"""
        if not OPENAI_API_KEY:
            logger.warning("OPENAI_API_KEY not set, cannot create embeddings")
            return None

        try:
            response = requests.post(
                "https://api.openai.com/v1/embeddings",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                json={
                    "model": "text-embedding-3-small",
                    "input": text[:2048],  # Limit to 2048 chars for API
                    "dimensions": EMBEDDING_DIM
                },
                timeout=15
            )

            if response.status_code == 200:
                embedding = response.json()["data"][0]["embedding"]
                return embedding
        except Exception as e:
            logger.debug(f"OpenAI embedding failed: {e}")

        return None

    def create_embeddings_with_ollama(self, text: str) -> Optional[List[float]]:
        """Create embeddings using Ollama with nomic-embed-text"""
        try:
            response = requests.post(
                f"{OLLAMA_URL}/api/embeddings",
                json={
                    "model": "nomic-embed-text:latest",
                    "prompt": text[:2048]  # Limit input size
                },
                timeout=30
            )

            if response.status_code == 200:
                data = response.json()
                embedding = data.get("embedding", [])
                # Pad to 1536 dims if needed
                if embedding and len(embedding) < EMBEDDING_DIM:
                    embedding.extend([0.0] * (EMBEDDING_DIM - len(embedding)))
                return embedding[:EMBEDDING_DIM]
        except Exception as e:
            logger.debug(f"Ollama embedding failed: {e}")

        return None

    def create_embedding(self, text: str) -> Optional[List[float]]:
        """Create embedding using configured model"""
        if not text or len(text) < 10:
            return None

        if EMBEDDING_MODEL == "openai":
            return self.create_embeddings_with_openai(text)
        else:
            return self.create_embeddings_with_ollama(text)

    def store_embedding(self, repo_id: str, embedding: List[float]) -> bool:
        """Store embedding in Supabase"""
        try:
            # Find the repo's UUID from our repo list
            repo_record = None
            for repo in self.repos:
                if repo.get("repo_id") == repo_id or repo.get("name") == repo_id:
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
        logger.info("LLAMAINDEX SEMANTIC INDEXING - OPTION C LAYER")
        logger.info("=" * 80)
        logger.info(f"Using embedding model: {EMBEDDING_MODEL}")

        # Fetch repos
        if not self.fetch_repos_to_index():
            logger.error("Failed to fetch repos, aborting")
            return

        self.stats["total_repos"] = len(self.repos)

        # Process each repo
        for i, repo in enumerate(self.repos, 1):
            repo_id = repo.get("repo_id") or repo.get("name")
            logger.info(f"\n[{i}/{len(self.repos)}] Indexing: {repo_id}")

            # Extract content
            readme = self.extract_readme_content(repo_id, repo.get("github_url", ""))

            # Build text for embedding: name + purpose + description + readme
            text_parts = [
                repo.get("name", ""),
                repo.get("purpose", ""),
                repo.get("description", ""),
                readme or ""
            ]
            combined_text = " ".join(filter(None, text_parts))

            if readme:
                self.stats["content_extracted"] += 1
                logger.info(f"  ✓ Extracted README ({len(combined_text)} chars)")

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
        logger.info(f"Content extracted:           {self.stats['content_extracted']}")
        logger.info(f"Embeddings created:          {self.stats['embeddings_created']}")
        logger.info(f"Embeddings stored in DB:     {self.stats['embeddings_stored']}")

        if self.stats["errors"]:
            logger.warning(f"\nEncountered {len(self.stats['errors'])} errors:")
            for error in self.stats["errors"][:10]:
                logger.warning(f"  - {error}")

        logger.info("=" * 80)
        logger.info("Next: Test semantic search with queries like:")
        logger.info('  - "What repos solve real-time collaboration?"')
        logger.info('  - "Which tools help with video processing?"')
        logger.info('  - "What repos provide agent orchestration?"')
        logger.info("=" * 80)


def create_semantic_search_query_handler() -> str:
    """Return Python code for semantic search queries against indexed repos"""
    return '''
# Semantic Search Query Handler
# Usage: query_repos_semantic(query_text, top_k=5)

from supabase import create_client
import numpy as np

def query_repos_semantic(query_text: str, top_k: int = 5):
    """Search repos semantically using vector similarity"""

    # Create embedding for query
    from your_embedding_module import create_embedding
    query_embedding = create_embedding(query_text)

    # Query Supabase for similar repos
    client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

    # Get all repos with embeddings
    response = client.table("repos").select("id,name,purpose,embedding").neq("embedding", None).execute()

    # Calculate cosine similarity
    similarities = []
    for repo in response.data:
        if repo["embedding"]:
            similarity = cosine_similarity(query_embedding, repo["embedding"])
            similarities.append((similarity, repo))

    # Return top k results
    sorted_results = sorted(similarities, key=lambda x: x[0], reverse=True)
    return sorted_results[:top_k]

def cosine_similarity(a, b):
    """Calculate cosine similarity between two vectors"""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
'''


def main():
    """Entry point"""
    indexer = RepositoryIndexer()
    indexer.index_all_repos()


if __name__ == "__main__":
    main()
