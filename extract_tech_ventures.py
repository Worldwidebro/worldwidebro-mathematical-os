#!/usr/bin/env python3
"""Extract metadata from TECH venture books and create registry CSV."""

import os
import csv
import re
from pathlib import Path
from datetime import datetime

def extract_venture_metadata(md_file):
    """Extract key metadata from a venture book markdown file."""
    try:
        with open(md_file, 'r') as f:
            content = f.read()

        # Extract venture ID from filename (TECH-001, TECH-002, etc)
        filename = os.path.basename(md_file)
        match = re.search(r'(TECH-\d+)', filename)
        venture_id_short = match.group(1) if match else None

        # Extract full venture ID from content (e.g., TECH-001-Quantum-Algorithm-AI)
        venture_id_match = re.search(r'\*\*Venture ID:\*\*\s+([^\n]+)', content)
        venture_id_full = venture_id_match.group(1).strip() if venture_id_match else venture_id_short

        # Extract name (first H1)
        name_match = re.search(r'^#\s+([^\n]+)', content, re.MULTILINE)
        name = name_match.group(1).strip() if name_match else venture_id_short

        # Extract sector
        sector_match = re.search(r'\*\*Sector:\*\*\s+([^\n]+)', content)
        sector = sector_match.group(1).strip().lower() if sector_match else 'technology'

        # Extract stage
        stage_match = re.search(r'\*\*Development Stage:\*\*\s+([^\n]+)|Stage:\s+([^\n]+)|stage.*?\*\*([^\n]+)', content, re.IGNORECASE)
        if stage_match:
            stage = next(g for g in stage_match.groups() if g).strip().lower()
        else:
            stage_match2 = re.search(r'\*\*Status:\*\*\s+([^\n]+)', content)
            stage = stage_match2.group(1).strip().lower() if stage_match2 else 'planned'

        # Extract status (same as stage usually)
        status_match = re.search(r'\*\*Status:\*\*\s+([^\n]+)', content)
        status = status_match.group(1).strip().lower() if status_match else stage

        # Extract repo URL
        repo_match = re.search(r'\[GitHub\]\(([^\)]+)\)', content)
        repo_url = repo_match.group(1) if repo_match else f'https://github.com/Worldwidebro/{venture_id_short.lower()}'

        # Extract key metrics (default: Pending)
        revenue_match = re.search(r'\*\*YTD Revenue:\*\*\s+([^\n]+)', content)
        revenue_ytd = revenue_match.group(1).strip() if revenue_match else '0'

        # Calculate basic health score (just a placeholder for now)
        health_score = 40  # planned ventures start at 40
        if 'launch' in stage or 'growth' in stage:
            health_score = 60
        elif 'scale' in stage:
            health_score = 75

        return {
            'venture_id': venture_id_full,
            'venture_id_short': venture_id_short,
            'name': name,
            'sector': sector,
            'stage': stage,
            'status': status,
            'repo_id': repo_url,
            'health_score': health_score,
            'business_model': 'technology-innovation',  # default
            'layer': 2,  # tech ventures are typically layer 2
            'revenue_ytd': revenue_ytd,
            'costs_mom': '0',
            'created_at': datetime.now().isoformat(),
            'keywords': f'{venture_id_short}, {name}, {sector}, technology'
        }
    except Exception as e:
        print(f"Error processing {md_file}: {e}")
        return None

def main():
    """Extract all TECH venture metadata and create CSV."""
    generated_books_dir = Path('/Users/acebless/Documents/venture-hub/generated-books')

    # Find all TECH venture book files
    venture_files = sorted(generated_books_dir.glob('TECH-*/TECH-*_venture-book_*.md'))
    print(f"Found {len(venture_files)} TECH venture books")

    # Extract metadata
    ventures = []
    for venture_file in venture_files:
        metadata = extract_venture_metadata(str(venture_file))
        if metadata:
            ventures.append(metadata)
            print(f"✓ Extracted: {metadata['venture_id_short']} ({metadata['name']})")

    # Write to CSV
    output_file = '/Users/acebless/Documents/tech_ventures_registry.csv'
    if ventures:
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=ventures[0].keys())
            writer.writeheader()
            writer.writerows(ventures)

        print(f"\n✅ Created: {output_file}")
        print(f"✅ Total ventures: {len(ventures)}")

        # Show sample
        print("\nFirst 3 entries:")
        for v in ventures[:3]:
            print(f"  {v['venture_id_short']}: {v['name']} (sector={v['sector']}, stage={v['stage']})")
    else:
        print("❌ No ventures extracted")

if __name__ == '__main__':
    main()
