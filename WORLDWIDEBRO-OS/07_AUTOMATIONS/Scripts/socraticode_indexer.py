#!/usr/bin/env python3
"""
SocratiCode Indexer — Index OWNED_REPOS and extract capabilities
"""

import os
import json
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Any

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

class SocratiCodeIndexer:
    """Index repos with SocratiCode and extract capabilities"""

    def __init__(self, workspace: str = "/Users/acebless/Documents"):
        self.workspace = workspace
        self.repos_path = Path(workspace)
        self.index_status = {}

    def verify_repos_exist(self) -> bool:
        """Verify all OWNED_REPOS exist"""
        print("\n📍 Verifying repos exist...")
        missing = []
        found = []

        for repo in sorted(OWNED_REPOS):
            repo_path = self.repos_path / repo
            if repo_path.exists():
                found.append(repo)
                print(f"  ✓ {repo}")
            else:
                missing.append(repo)
                print(f"  ✗ {repo} (not found)")

        print(f"\n✅ Found {len(found)}/18 repos")
        if missing:
            print(f"❌ Missing: {', '.join(missing)}")
            return False
        return True

    def count_repo_sizes(self) -> Dict[str, Any]:
        """Get repo size statistics"""
        print("\n📊 Repo Size Analysis:")
        stats = {}
        total_size = 0
        total_files = 0

        for repo in sorted(OWNED_REPOS):
            repo_path = self.repos_path / repo
            if repo_path.exists():
                size_kb = 0
                file_count = 0
                for root, dirs, files in os.walk(repo_path):
                    # Skip common directories
                    dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '.next', 'dist', 'build']]
                    for file in files:
                        file_path = Path(root) / file
                        try:
                            size_kb += file_path.stat().st_size / 1024
                            file_count += 1
                        except:
                            pass

                stats[repo] = {
                    "size_mb": round(size_kb / 1024, 2),
                    "files": file_count
                }
                total_size += size_kb / 1024
                total_files += file_count
                print(f"  {repo:35} {stats[repo]['size_mb']:>8.2f} MB | {file_count:>6} files")

        print(f"\n  Total: {total_size:.2f} MB across {total_files:,} files")
        return {"stats": stats, "total_mb": round(total_size, 2), "total_files": total_files}

    def extract_primary_languages(self) -> Dict[str, List[str]]:
        """Detect primary programming languages per repo"""
        print("\n🔍 Detecting primary languages...")
        language_extensions = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.jsx': 'javascript',
            '.tsx': 'typescript',
            '.go': 'go',
            '.rs': 'rust',
            '.java': 'java',
            '.sql': 'sql',
            '.sh': 'bash',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.json': 'json',
        }

        repo_languages = {}

        for repo in sorted(OWNED_REPOS):
            repo_path = self.repos_path / repo
            if repo_path.exists():
                languages = set()
                for root, dirs, files in os.walk(repo_path):
                    dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '.next', 'dist', 'build']]
                    for file in files:
                        ext = Path(file).suffix.lower()
                        if ext in language_extensions:
                            languages.add(language_extensions[ext])

                repo_languages[repo] = sorted(list(languages))
                lang_str = ", ".join(repo_languages[repo]) if repo_languages[repo] else "unknown"
                print(f"  {repo:35} {lang_str}")

        return repo_languages

    def extract_repo_capabilities(self) -> Dict[str, List[str]]:
        """Extract capabilities from repos"""
        print("\n⚙️  Extracting repo capabilities...")

        # Capability keywords mapping
        capability_map = {
            'pitch': ['pitch', 'deck', 'presentation', 'slide'],
            'portfolio': ['portfolio', 'cap-table', 'equity', 'fundraising'],
            'authentication': ['auth', 'oauth', 'oidc', 'session', 'login', 'jwt'],
            'workspace': ['workspace', 'collaboration', 'team', 'organization'],
            'knowledge-graph': ['rag', 'retrieval', 'augmented', 'knowledge', 'graph', 'embedding'],
            'dashboard': ['dashboard', 'analytics', 'monitoring', 'visualization'],
            'construction': ['construction', 'building', 'contractor', 'permit'],
            'api': ['api', 'rest', 'graphql', 'sdk', 'endpoint'],
            'database': ['database', 'postgres', 'sql', 'orm'],
            'payment': ['payment', 'stripe', 'billing'],
            'monitoring': ['monitoring', 'observability', 'sre', 'prometheus'],
            'security': ['security', 'encryption', 'tls', 'ssl'],
            'simulation': ['simulation', 'game', 'civilization'],
        }

        repo_capabilities = {}

        for repo in sorted(OWNED_REPOS):
            repo_path = self.repos_path / repo
            capabilities = set()

            if repo_path.exists():
                # Check README
                readme_path = repo_path / "README.md"
                if readme_path.exists():
                    try:
                        with open(readme_path, 'r') as f:
                            readme_text = f.read().lower()
                            for cap, keywords in capability_map.items():
                                if any(kw in readme_text for kw in keywords):
                                    capabilities.add(cap)
                    except:
                        pass

                # Check package.json
                pkg_path = repo_path / "package.json"
                if pkg_path.exists():
                    try:
                        with open(pkg_path, 'r') as f:
                            pkg = json.load(f)
                            desc = (pkg.get('description', '') or '').lower()
                            keywords = pkg.get('keywords', []) or []
                            for cap, cap_keywords in capability_map.items():
                                if any(kw in desc for kw in cap_keywords) or any(kw in keywords for kw in cap_keywords):
                                    capabilities.add(cap)
                    except:
                        pass

            # Default capabilities by repo name
            if 'pitch' in repo.lower():
                capabilities.add('pitch')
            if 'venture' in repo.lower():
                capabilities.add('portfolio')
            if 'mission' in repo.lower():
                capabilities.add('authentication')
            if 'rag' in repo.lower() or 'light' in repo.lower():
                capabilities.add('knowledge-graph')
            if 'dashboard' in repo.lower():
                capabilities.add('dashboard')
            if 'construction' in repo.lower():
                capabilities.add('construction')
            if 'security' in repo.lower():
                capabilities.add('security')
            if 'sre' in repo.lower():
                capabilities.add('monitoring')
            if 'civilization' in repo.lower():
                capabilities.add('simulation')

            repo_capabilities[repo] = sorted(list(capabilities))
            caps_str = ", ".join(repo_capabilities[repo]) if repo_capabilities[repo] else "generic"
            print(f"  {repo:35} {caps_str}")

        return repo_capabilities

    def generate_product_profile(self) -> Dict[str, Any]:
        """Generate comprehensive product profile"""
        print("\n" + "="*80)
        print("PRODUCT CAPABILITY PROFILES")
        print("="*80)

        size_data = self.count_repo_sizes()
        languages = self.extract_primary_languages()
        capabilities = self.extract_repo_capabilities()

        profiles = {}
        for repo in sorted(OWNED_REPOS):
            profiles[repo] = {
                "size_mb": size_data['stats'].get(repo, {}).get('size_mb', 0),
                "files": size_data['stats'].get(repo, {}).get('files', 0),
                "languages": languages.get(repo, []),
                "capabilities": capabilities.get(repo, []),
            }

        # Save to JSON
        with open(self.workspace + "/socraticode_profiles.json", "w") as f:
            json.dump(profiles, f, indent=2)

        print(f"\n✅ Profiles saved to socraticode_profiles.json")
        print("\n📋 Profile Summary:")
        print(f"  Products analyzed: 18")
        print(f"  Total size: {size_data['total_mb']:.2f} MB")
        print(f"  Total files: {size_data['total_files']:,}")
        print(f"  Unique capabilities: {len(set(cap for caps in capabilities.values() for cap in caps))}")

        return profiles

    def run(self):
        """Run full indexing pipeline"""
        print("\n" + "="*80)
        print("SOCRATICODE INDEXER — Index OWNED_REPOS & Extract Capabilities")
        print("="*80 + "\n")

        if not self.verify_repos_exist():
            return

        profiles = self.generate_product_profile()

        print("\n" + "="*80)
        print("✅ INDEXING COMPLETE")
        print("="*80)
        print("\nNext steps:")
        print("  1. Use SocratiCode semantic search: 'Find products for payroll ventures'")
        print("  2. Query venture-product matching in dexter_dashboard.py")
        print("  3. Sync profiles to Graphify knowledge graph")


def main():
    indexer = SocratiCodeIndexer()
    indexer.run()


if __name__ == "__main__":
    main()
