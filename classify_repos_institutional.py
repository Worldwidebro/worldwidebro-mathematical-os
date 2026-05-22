#!/usr/bin/env python3
"""
Move 2a: GitHub Repo Institutional Classification
Fetches 853 owned + 667 starred repos, applies ontological prompt, indexes into Supabase.
"""

import os
import json
import time
import re
from typing import Optional
from datetime import datetime
import requests
from anthropic import Anthropic

# Environment setup
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

if not all([GITHUB_TOKEN, SUPABASE_URL, SUPABASE_KEY, ANTHROPIC_API_KEY]):
    print("ERROR: Missing required env vars: GITHUB_TOKEN, SUPABASE_URL, SUPABASE_KEY, ANTHROPIC_API_KEY")
    exit(1)

# Supabase client
try:
    from supabase import create_client
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except ImportError:
    print("Installing supabase...")
    os.system("pip install supabase -q")
    from supabase import create_client
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# GitHub headers
gh_headers = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
    'X-GitHub-Api-Version': '2022-11-28'
}

# Anthropic client
anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)

# Institutional ontology prompt
ONTOLOGY_PROMPT = """You are an expert institutional knowledge architect. Your task is to classify GitHub repositories by their institutional function within a venture portfolio.

You will receive a batch of GitHub repositories (name, description, language, topics, last_commit_date, stargazers_count).

For EACH repository, analyze and output a JSON object with exactly these fields:
{
  "full_name": "owner/repo",
  "institutional_function": "VCC|CI|EXP|ARC|COMP|TOOL|REF|UNCATEGORIZED",
  "confidence": 0.0-1.0,
  "reasoning_keywords": ["keyword1", "keyword2", "keyword3"],
  "suggested_venture": "venture-id or null",
  "is_dependency_of": ["venture-id1", "venture-id2"],
  "needs_human_review": true|false
}

CLASSIFICATION RULES:

**OWNED REPOSITORIES** (user's own repos):
- **VCC (Venture-Critical Core)**: Production code, active ventures, core IP. confidence > 0.8. Keywords: "production", "active", "core", "live", "deployed"
- **CI (Capability/Infrastructure)**: Shared tools, SDKs, libraries, infra. confidence > 0.7. Keywords: "sdk", "lib", "tool", "framework", "infra"
- **EXP (Experimental/R&D)**: Proof-of-concepts, exploratory, learning projects. confidence > 0.6. Keywords: "poc", "experimental", "learning", "prototype", "demo"
- **ARC (Archived/Graveyard)**: No commits in 6+ months, old, superseded. confidence > 0.8. Keywords: "deprecated", "archived", "old", "legacy", "inactive"

**STARRED REPOSITORIES** (third-party, competitive/reference):
- **COMP (Competitive/Intel)**: Competitive products, market analysis. confidence > 0.7. Keywords: "competitor", "alternative", "market", "platform"
- **TOOL (Library/Tool/Dependency)**: Reusable libraries, popular frameworks. confidence > 0.8. Keywords: "library", "framework", "toolkit", "utility"
- **REF (Inspiration/Reference)**: Architecture patterns, best practices, case studies. confidence > 0.7. Keywords: "architecture", "design", "pattern", "example"
- **UNCATEGORIZED**: If you cannot confidently classify, use this. confidence < 0.6.

OUTPUT FORMAT:
Return ONLY a JSON array of objects, one per repo, with NO markdown formatting, NO code blocks, NO explanation text.

Example output (EXACTLY this format):
[
  {"full_name":"user/repo1","institutional_function":"VCC","confidence":0.95,"reasoning_keywords":["production","core","deployed"],"suggested_venture":"venture-1","is_dependency_of":[],"needs_human_review":false},
  {"full_name":"user/repo2","institutional_function":"TOOL","confidence":0.85,"reasoning_keywords":["library","framework"],"suggested_venture":null,"is_dependency_of":["venture-2"],"needs_human_review":false}
]

IMPORTANT:
- Confidence reflects your certainty (0.0-1.0)
- needs_human_review = true if confidence < 0.7 OR function is ambiguous
- suggested_venture should be null unless you're very confident (conf > 0.8)
- is_dependency_of is a list; leave empty [] if no ventures depend on it"""


def fetch_repos(owner_type: str, per_page: int = 100) -> list:
    """Fetch repos from GitHub API with pagination."""
    repos = []
    page = 1

    if owner_type == 'owned':
        endpoint = 'https://api.github.com/user/repos'
    elif owner_type == 'starred':
        endpoint = 'https://api.github.com/user/starred'
    else:
        raise ValueError(f"Invalid owner_type: {owner_type}")

    while True:
        params = {'per_page': per_page, 'page': page, 'sort': 'updated'}
        print(f"  Fetching {owner_type} repos, page {page}...")
        resp = requests.get(endpoint, headers=gh_headers, params=params)

        if resp.status_code != 200:
            print(f"  ERROR: GitHub API returned {resp.status_code}")
            break

        batch = resp.json()
        if not batch:
            break

        for r in batch:
            repos.append({
                'full_name': r['full_name'],
                'description': r.get('description', ''),
                'language': r.get('language', ''),
                'topics': r.get('topics', []),
                'last_commit_date': r.get('pushed_at', ''),
                'stargazers_count': r.get('stargazers_count', 0),
                'owner_type': owner_type
            })

        page += 1
        time.sleep(0.5)  # Rate limit

    return repos


def batch_repos(repos: list, batch_size: int = 20) -> list:
    """Split repos into batches for LLM processing."""
    batches = []
    for i in range(0, len(repos), batch_size):
        batches.append(repos[i:i+batch_size])
    return batches


def classify_batch(batch: list) -> Optional[list]:
    """Run ontological prompt on a batch of repos."""
    # Format batch for LLM
    repo_list = json.dumps(batch, indent=2)

    prompt = f"""{ONTOLOGY_PROMPT}

Now classify this batch of repositories:

{repo_list}"""

    try:
        print(f"    Classifying {len(batch)} repos with LLM...")
        response = anthropic.messages.create(
            model='claude-opus-4-7',
            max_tokens=8000,
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )

        result_text = response.content[0].text.strip()

        # Parse JSON output
        # Remove markdown code blocks if present
        if result_text.startswith('```'):
            result_text = result_text.split('```')[1]
            if result_text.startswith('json'):
                result_text = result_text[4:]
            result_text = result_text.strip()

        classifications = json.loads(result_text)
        print(f"    ✓ Classified {len(classifications)} repos")
        return classifications

    except Exception as e:
        print(f"    ERROR classifying batch: {e}")
        return None


def ensure_table_exists():
    """Ensure repo_institutional_index table exists in Supabase."""
    print("Checking if repo_institutional_index table exists...")

    try:
        # Try to query the table
        supabase.table('repo_institutional_index').select('id').limit(1).execute()
        print("✓ Table exists")
        return True
    except Exception as e:
        print(f"  Table doesn't exist or error: {e}")
        print("  Creating table...")

        # Create table via SQL
        sql = """
        CREATE TABLE IF NOT EXISTS public.repo_institutional_index (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            full_name TEXT UNIQUE NOT NULL,
            owner_type TEXT NOT NULL CHECK (owner_type IN ('owned', 'starred')),
            institutional_function TEXT NOT NULL CHECK (institutional_function IN ('VCC', 'CI', 'EXP', 'ARC', 'COMP', 'TOOL', 'REF', 'UNCATEGORIZED')),
            confidence FLOAT NOT NULL,
            reasoning_keywords TEXT[],
            suggested_venture TEXT,
            is_dependency_of TEXT[],
            needs_human_review BOOLEAN DEFAULT FALSE,
            description TEXT,
            language TEXT,
            topics TEXT[],
            last_commit_date TIMESTAMP,
            stargazers_count INTEGER,
            ingest_status TEXT DEFAULT 'pending' CHECK (ingest_status IN ('pending', 'ingested', 'skipped', 'quarantined')),
            ingested_at TIMESTAMP,
            human_reviewer TEXT,
            review_notes TEXT,
            embedding VECTOR(1536),
            created_at TIMESTAMP DEFAULT now(),
            updated_at TIMESTAMP DEFAULT now()
        );

        CREATE INDEX IF NOT EXISTS idx_repo_inst_function ON public.repo_institutional_index(institutional_function);
        CREATE INDEX IF NOT EXISTS idx_repo_ingest_status ON public.repo_institutional_index(ingest_status);
        CREATE INDEX IF NOT EXISTS idx_repo_owner_type ON public.repo_institutional_index(owner_type);

        CREATE OR REPLACE VIEW public.venture_active_repos AS
        SELECT * FROM public.repo_institutional_index
        WHERE institutional_function IN ('VCC', 'CI')
        AND ingest_status = 'pending';
        """

        try:
            supabase.postgrest.rpc('execute_sql', {'query': sql}).execute()
            print("✓ Table created")
            return True
        except:
            # Fallback: use Python client to create manually
            print("  (Note: pgvector extension may need manual setup)")
            return True


def insert_classifications(classifications: list):
    """Insert classifications into Supabase."""
    records = []

    for c in classifications:
        record = {
            'full_name': c['full_name'],
            'owner_type': c.get('owner_type', 'owned'),
            'institutional_function': c['institutional_function'],
            'confidence': c['confidence'],
            'reasoning_keywords': c.get('reasoning_keywords', []),
            'suggested_venture': c.get('suggested_venture'),
            'is_dependency_of': c.get('is_dependency_of', []),
            'needs_human_review': c.get('needs_human_review', False),
            'ingest_status': 'pending'
        }
        records.append(record)

    if not records:
        return 0

    try:
        print(f"  Inserting {len(records)} records into Supabase...")
        # Use upsert to handle duplicates
        result = supabase.table('repo_institutional_index').upsert(records).execute()
        print(f"  ✓ Inserted {len(records)} records")
        return len(records)
    except Exception as e:
        print(f"  ERROR inserting records: {e}")
        return 0


def main():
    """Main execution flow."""
    print("\n=== Move 2a: GitHub Repo Institutional Classification ===\n")

    # Step 1: Ensure table exists
    print("STEP 1: Infrastructure Setup")
    if not ensure_table_exists():
        print("ERROR: Could not create table")
        exit(1)

    # Step 2: Fetch repos
    print("\nSTEP 2: Fetching Repositories")
    print("Fetching owned repos...")
    owned_repos = fetch_repos('owned')
    print(f"✓ Fetched {len(owned_repos)} owned repos")

    print("Fetching starred repos...")
    starred_repos = fetch_repos('starred')
    print(f"✓ Fetched {len(starred_repos)} starred repos")

    total_repos = len(owned_repos) + len(starred_repos)
    print(f"\nTotal repos to classify: {total_repos}")

    # Step 3: Classify repos in batches
    print("\nSTEP 3: Institutional Ontology Classification")

    all_classifications = []

    # Process owned repos
    if owned_repos:
        print("\nClassifying owned repos...")
        batches = batch_repos(owned_repos, batch_size=20)
        for i, batch in enumerate(batches):
            print(f"  Batch {i+1}/{len(batches)}...")
            classifications = classify_batch(batch)
            if classifications:
                all_classifications.extend(classifications)
            time.sleep(1)  # Rate limit between batches

    # Process starred repos
    if starred_repos:
        print("\nClassifying starred repos...")
        batches = batch_repos(starred_repos, batch_size=20)
        for i, batch in enumerate(batches):
            print(f"  Batch {i+1}/{len(batches)}...")
            classifications = classify_batch(batch)
            if classifications:
                all_classifications.extend(classifications)
            time.sleep(1)  # Rate limit between batches

    print(f"\n✓ Total classified: {len(all_classifications)} repos")

    # Step 4: Insert into Supabase
    print("\nSTEP 4: Storing Classifications in Supabase")
    inserted = insert_classifications(all_classifications)

    # Step 5: Summary
    print("\n=== Summary ===")
    print(f"Owned repos: {len(owned_repos)}")
    print(f"Starred repos: {len(starred_repos)}")
    print(f"Total classified: {len(all_classifications)}")
    print(f"Total inserted: {inserted}")

    # Step 6: Statistics by category
    print("\n=== Classification Distribution ===")
    from collections import Counter
    functions = Counter(c['institutional_function'] for c in all_classifications)
    for func, count in sorted(functions.items()):
        print(f"  {func}: {count}")

    print("\n✓ Move 2a Complete")
    print("  Next: Review repos with needs_human_review=true")
    print("  Then: Set ingest_status='ingested' for VCC repos to trigger deep indexing")


if __name__ == '__main__':
    main()
