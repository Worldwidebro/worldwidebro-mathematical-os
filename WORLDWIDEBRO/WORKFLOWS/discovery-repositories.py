#!/usr/bin/env python3
"""
Repository Discovery Workflow
Discovers repositories across GitHub, local, Docker, T7, LaCie.
Creates unified registry: identity, capability, business value, relationships.
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict

try:
    from neo4j import GraphDatabase
    NEO4J_AVAILABLE = True
except ImportError:
    NEO4J_AVAILABLE = False

DOCUMENTS_ROOT = Path("/Users/acebless/Documents")
WORLDWIDEBRO_ROOT = DOCUMENTS_ROOT / "WORLDWIDEBRO"
REGISTRY_DIR = WORLDWIDEBRO_ROOT / "REGISTRY"
REGISTRY_DIR.mkdir(parents=True, exist_ok=True)

NEO4J_URI = "neo4j://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "ventures2026"


class RepositoryDiscovery:
    def __init__(self):
        self.repositories = {}
        self.capabilities = defaultdict(list)
        self.relationships = []
        self.neo4j = None
        if NEO4J_AVAILABLE:
            try:
                self.neo4j = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
            except Exception as e:
                print(f"⚠️ Neo4j: {e}")

    def discover_github(self):
        """Discover from GitHub Worldwidebro account."""
        print("\n=== GITHUB ===")
        try:
            result = subprocess.run(
                ["gh", "repo", "list", "Worldwidebro", "--limit", "200", "--json",
                 "name,description,url,primaryLanguage,isArchived,createdAt"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode != 0:
                print(f"Error: {result.stderr}")
                return 0

            repos = json.loads(result.stdout)
            for repo in repos:
                repo_id = f"github:{repo['name']}"
                self.repositories[repo_id] = {
                    "id": repo_id,
                    "name": repo["name"],
                    "source": "github",
                    "url": repo["url"],
                    "description": repo["description"] or "",
                    "language": repo["primaryLanguage"]["name"] if repo["primaryLanguage"] else None,
                    "archived": repo["isArchived"],
                    "created_at": repo["createdAt"],
                    "discovered_at": datetime.now().isoformat(),
                    "classification": self._classify(repo["name"]),
                    "capabilities": self._infer_caps(repo["name"], repo["description"]),
                }
            print(f"✅ Found {len(repos)} GitHub repos")
            return len(repos)
        except Exception as e:
            print(f"❌ {e}")
            return 0

    def discover_local(self, root_path):
        """Discover local git repos."""
        print(f"\n=== LOCAL: {root_path.name} ===")
        count = 0
        for git_dir in root_path.rglob(".git"):
            if git_dir.is_dir():
                repo_path = git_dir.parent
                try:
                    repo_id = f"local:{repo_path.name}"
                    self.repositories[repo_id] = {
                        "id": repo_id,
                        "name": repo_path.name,
                        "source": "local",
                        "path": str(repo_path),
                        "size_mb": self._get_size(repo_path),
                        "discovered_at": datetime.now().isoformat(),
                        "classification": self._classify(repo_path.name),
                        "capabilities": self._infer_caps(repo_path.name, ""),
                    }
                    count += 1
                except:
                    pass
        print(f"✅ Found {count} local repos")
        return count

    def build_registry(self):
        """Build machine-readable registry."""
        print("\n=== BUILDING REGISTRY ===")

        registry = {
            "generated_at": datetime.now().isoformat(),
            "sources": ["GitHub", "Mac Studio", "Docker", "T7 (when mounted)", "LaCie (when mounted)"],
            "statistics": {
                "total_repositories": len(self.repositories),
                "by_source": self._count_by_source(),
                "by_classification": self._count_by_classification(),
                "by_capability": len(self.capabilities),
            },
            "repositories": self.repositories,
            "capabilities": dict(self.capabilities),
        }

        # Save
        registry_file = REGISTRY_DIR / "repository-portfolio.json"
        with open(registry_file, "w") as f:
            json.dump(registry, f, indent=2)

        print(f"✅ Registry → {registry_file.name}")
        return registry

    def create_consolidation_map(self):
        """Create consolidation strategy."""
        print("\n=== CONSOLIDATION MAP ===")

        # Find duplicates
        base_names = defaultdict(list)
        for repo_id, repo in self.repositories.items():
            base = repo["name"].lower()
            for suffix in ["-v1", "-v2", "-v3", "-core", "-api"]:
                base = base.replace(suffix, "")
            base_names[base].append(repo_id)

        duplicates = [repos for repos in base_names.values() if len(repos) > 1]

        consolidation = {
            "timestamp": datetime.now().isoformat(),
            "total_repositories": len(self.repositories),
            "potential_duplicates": len(duplicates),
            "duplicate_groups": duplicates,
            "stages": {
                "1_identify": {"action": "Identity resolution", "status": "pending"},
                "2_map_capabilities": {"action": "Capability mapping", "status": "pending"},
                "3_graph": {"action": "Load to Neo4j", "status": "pending"},
                "4_consolidate": {"action": "Consolidation decisions", "status": "pending"},
                "5_cli": {"action": "Build `wb` CLI", "status": "pending"},
            }
        }

        map_file = REGISTRY_DIR / "consolidation-map.json"
        with open(map_file, "w") as f:
            json.dump(consolidation, f, indent=2)

        print(f"✅ Map → {map_file.name}")
        print(f"   Total repos: {len(self.repositories)}")
        print(f"   Potential duplicates: {len(duplicates)}")
        return consolidation

    # Utilities
    def _classify(self, name):
        n = name.lower()
        if any(x in n for x in ["venture", "courier", "staffing", "construction"]):
            return "VENTURE"
        elif any(x in n for x in ["api", "backend", "core"]):
            return "PLATFORM"
        elif any(x in n for x in ["agent", "skill", "mcp"]):
            return "CAPABILITY"
        elif any(x in n for x in ["docker", "infra"]):
            return "INFRASTRUCTURE"
        else:
            return "OTHER"

    def _infer_caps(self, name, desc):
        text = f"{name} {desc}".lower()
        caps = []
        if any(x in text for x in ["auth", "oauth", "login"]):
            caps.append("authentication")
        if any(x in text for x in ["payment", "stripe", "billing"]):
            caps.append("payment")
        if any(x in text for x in ["knowledge", "graph", "semantic"]):
            caps.append("knowledge")
        if any(x in text for x in ["orchestration", "workflow"]):
            caps.append("orchestration")
        if any(x in text for x in ["marketplace", "vex"]):
            caps.append("marketplace")
        for cap in caps:
            self.capabilities[cap].append(name)
        return caps

    def _get_size(self, path):
        try:
            total = sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
            return total / (1024 * 1024)
        except:
            return 0

    def _count_by_source(self):
        counts = defaultdict(int)
        for repo in self.repositories.values():
            counts[repo["source"]] += 1
        return dict(counts)

    def _count_by_classification(self):
        counts = defaultdict(int)
        for repo in self.repositories.values():
            counts[repo.get("classification", "OTHER")] += 1
        return dict(counts)


def main():
    print("=" * 70)
    print("WORLDWIDEBRO REPOSITORY DISCOVERY")
    print("=" * 70)

    discovery = RepositoryDiscovery()

    # Discover
    gh_count = discovery.discover_github()
    studio_count = discovery.discover_local(DOCUMENTS_ROOT)

    # Check for T7 and LaCie
    t7_path = Path("/Volumes/T7")
    lacie_path = Path("/Volumes/LaCie")
    t7_count = discovery.discover_local(t7_path) if t7_path.exists() else 0
    lacie_count = discovery.discover_local(lacie_path) if lacie_path.exists() else 0

    if not t7_path.exists():
        print("\n⚠️  T7 not mounted (check USB connection)")
    if not lacie_path.exists():
        print("⚠️  LaCie not mounted (check USB connection)")

    # Build artifacts
    registry = discovery.build_registry()
    consolidation = discovery.create_consolidation_map()

    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"GitHub:    {gh_count}")
    print(f"Local:     {studio_count}")
    print(f"T7:        {t7_count}")
    print(f"LaCie:     {lacie_count}")
    print(f"TOTAL:     {gh_count + studio_count + t7_count + lacie_count}")
    print(f"\nRegistry: WORLDWIDEBRO/REGISTRY/repository-portfolio.json")
    print(f"Map:      WORLDWIDEBRO/REGISTRY/consolidation-map.json")


if __name__ == "__main__":
    main()
