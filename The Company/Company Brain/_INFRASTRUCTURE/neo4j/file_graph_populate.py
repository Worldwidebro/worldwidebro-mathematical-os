#!/usr/bin/env python3
"""
FILE GRAPH POPULATION SCRIPT
Scans all .md files, extracts wiki links, builds Neo4j graph
Purpose: Create fully connected file base for Company Brain
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

# Configuration
ROOT = Path("/Users/acebless/Documents/The Company/Company Brain")
EXCLUDE_DIRS = {'.git', 'node_modules', '_ARCHIVE', '_ENGINE', '_EVAL', 'repos'}

def scan_files():
    """Find all .md files and extract wiki links"""
    files_data = {}
    wiki_links = defaultdict(list)

    for md_file in ROOT.rglob("*.md"):
        # Skip excluded directories
        if any(excl in md_file.parts for excl in EXCLUDE_DIRS):
            continue

        # Get relative path
        rel_path = md_file.relative_to(ROOT)
        domain = rel_path.parts[0] if len(rel_path.parts) > 1 else "root"

        # Read file and extract wiki links
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue

        # Find all [[...]] wiki links
        links = re.findall(r'\[\[([^\]]+)\]\]', content)
        wiki_links[str(rel_path)] = links

        files_data[str(rel_path)] = {
            'name': md_file.stem,
            'domain': domain,
            'path': str(rel_path),
            'has_wiki_links': len(links) > 0,
            'link_count': len(links),
            'size': len(content)
        }

    return files_data, wiki_links

def analyze_connections(files_data, wiki_links):
    """Analyze which files link to which, find gaps"""
    analysis = {
        'total_files': len(files_data),
        'files_with_links': sum(1 for f in files_data.values() if f['has_wiki_links']),
        'files_without_links': sum(1 for f in files_data.values() if not f['has_wiki_links']),
        'by_domain': defaultdict(int),
        'broken_links': [],
        'connected_files': [],
        'disconnected_files': []
    }

    # Count by domain
    for f_data in files_data.values():
        analysis['by_domain'][f_data['domain']] += 1

    # Find broken links and connected files
    all_file_names = {Path(p).stem: p for p in files_data.keys()}

    for file_path, links in wiki_links.items():
        if links:
            analysis['connected_files'].append(file_path)

        # Check for broken links (references to non-existent files)
        for link in links:
            # Extract the file reference (before any | delimiter)
            ref = link.split('|')[0]
            # Try to find it
            if not (ref + '.md' in files_data or Path(ROOT / (ref + '.md')).exists()):
                analysis['broken_links'].append({
                    'from': file_path,
                    'to': ref,
                    'full_link': link
                })

    # Files without any wiki links
    for file_path in files_data.keys():
        if not wiki_links.get(file_path):
            analysis['disconnected_files'].append(file_path)

    return analysis

def generate_missing_readmes(files_data):
    """Generate README.md for domains without navigation"""
    domains_with_readme = set()
    domains_in_codebase = set()

    for file_path in files_data.keys():
        domain = file_path.split('/')[0]
        domains_in_codebase.add(domain)

        if file_path.endswith('README.md'):
            domains_with_readme.add(domain)

    missing = domains_in_codebase - domains_with_readme
    return {
        'total_domains': len(domains_in_codebase),
        'with_readme': len(domains_with_readme),
        'missing_readme': list(missing),
        'count_missing': len(missing)
    }

def generate_cypher_inserts(files_data, wiki_links):
    """Generate Cypher INSERT statements for Neo4j"""
    statements = []

    # Insert FILE nodes
    for rel_path, data in files_data.items():
        domain = data['domain']
        name = data['name']
        cypher = f"""
MATCH (d:Domain {{name: '{domain}'}})
CREATE (f:File {{
  name: '{name}',
  path: './{rel_path}',
  domain: '{domain}',
  hasWikiLinks: {str(data['has_wiki_links']).lower()},
  linkCount: {data['link_count']}
}})-[:IN_DOMAIN]->(d);
"""
        statements.append(cypher)

    # Insert LINK edges
    for source, targets in wiki_links.items():
        source_name = Path(source).stem
        for target_ref in targets:
            target = target_ref.split('|')[0]  # Remove display text
            cypher = f"""
MATCH (f1:File {{name: '{source_name}'}}), (f2:File {{name: '{target}'}})
MERGE (f1)-[:LINKS_TO {{type: 'wiki_reference'}}]->(f2);
"""
            statements.append(cypher)

    return statements

def main():
    print("=" * 80)
    print("FILE GRAPH POPULATION SCRIPT")
    print("=" * 80)

    # Scan all files
    print("\n[1/5] Scanning all .md files...")
    files_data, wiki_links = scan_files()
    print(f"  Found: {len(files_data)} files with {sum(len(l) for l in wiki_links.values())} total wiki links")

    # Analyze connections
    print("\n[2/5] Analyzing connections...")
    analysis = analyze_connections(files_data, wiki_links)
    print(f"  Connected: {len(analysis['connected_files'])} files")
    print(f"  Disconnected: {len(analysis['disconnected_files'])} files")
    print(f"  Broken links: {len(analysis['broken_links'])} references")

    # Missing READMEs
    print("\n[3/5] Checking domain READMEs...")
    readme_status = generate_missing_readmes(files_data)
    print(f"  Domains with README: {readme_status['with_readme']}/{readme_status['total_domains']}")
    print(f"  Missing: {readme_status['count_missing']} domains")

    # Generate Cypher
    print("\n[4/5] Generating Cypher statements...")
    cypher_stmts = generate_cypher_inserts(files_data, wiki_links)
    print(f"  Generated: {len(cypher_stmts)} INSERT statements")

    # Output report
    print("\n[5/5] Generating report...")
    report = {
        'timestamp': str(Path(__file__).stat().st_mtime),
        'summary': {
            'total_files': analysis['total_files'],
            'files_with_links': analysis['files_with_links'],
            'files_without_links': analysis['files_without_links'],
            'broken_links': len(analysis['broken_links']),
            'domains_total': readme_status['total_domains'],
            'domains_with_readme': readme_status['with_readme'],
            'domains_missing_readme': readme_status['count_missing']
        },
        'by_domain': dict(analysis['by_domain']),
        'disconnected_files': analysis['disconnected_files'][:20],  # First 20
        'broken_links': analysis['broken_links'][:20],  # First 20
        'missing_readmes': readme_status['missing_readme'][:20],  # First 20
        'cypher_statement_count': len(cypher_stmts)
    }

    # Save report
    report_path = ROOT / "_INFRASTRUCTURE/neo4j/FILE_GRAPH_REPORT.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

    print("\n" + "=" * 80)
    print("REPORT")
    print("=" * 80)
    print(json.dumps(report['summary'], indent=2))
    print(f"\nFull report saved to: {report_path}")
    print(f"Cypher inserts saved to: FILE_GRAPH_CYPHER.txt")

    # Save Cypher statements
    cypher_path = ROOT / "_INFRASTRUCTURE/neo4j/FILE_GRAPH_CYPHER.txt"
    with open(cypher_path, 'w') as f:
        f.write('\n\n'.join(cypher_stmts))

    print("\n✅ Population script complete")
    print("Next: Load FILE_GRAPH_CYPHER.txt into Neo4j to build the graph")

if __name__ == '__main__':
    main()
