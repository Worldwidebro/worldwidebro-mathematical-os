#!/usr/bin/env python3
"""
Auto-Tagger: Classify all 1,661 repos by monetization + software type.
Reads from REPOSITORY-REGISTRY.json, fetches README from GitHub API, tags, writes back.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, Optional
import subprocess

class AutoTagger:
    MONETIZATION_KEYWORDS = {
        "SaaS": ["subscription", "monthly", "annual", "recurring", "saas", "billing"],
        "Marketplace": ["marketplace", "commission", "buyer", "seller", "listing fee"],
        "D2C": ["shop", "store", "product", "ecommerce", "catalog", "inventory"],
        "Services": ["consulting", "agency", "project", "retainer", "billable", "professional services"],
        "Fintech": ["bank", "loan", "crypto", "payment", "transaction fee", "spread", "insurance"],
        "Media": ["ad", "sponsor", "content", "youtube", "podcast", "newsletter"],
    }

    def __init__(self, registry_path: str):
        self.registry_path = Path(registry_path)
        self.registry = self._load_registry()
        self.tagged_count = 0
        self.failed_count = 0

    def _load_registry(self) -> Dict:
        with open(self.registry_path) as f:
            return json.load(f)

    def _fetch_readme(self, repo_url: str) -> str:
        """Fetch README from GitHub API."""
        if not repo_url:
            return ""

        parts = repo_url.replace("https://github.com/", "").split("/")
        if len(parts) != 2:
            return ""

        owner, repo = parts
        api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"

        try:
            result = subprocess.run(
                ["curl", "-s", "-H", "Accept: application/vnd.github.v3.raw", api_url],
                capture_output=True, text=True, timeout=5
            )
            return result.stdout.lower() if result.returncode == 0 else ""
        except Exception:
            return ""

    def _detect_tech_stack(self, repo_url: str) -> str:
        """Detect software type from package.json or README keywords."""
        if not repo_url:
            return "Unknown"

        parts = repo_url.replace("https://github.com/", "").split("/")
        if len(parts) != 2:
            return "Unknown"

        owner, repo = parts

        # Try package.json
        try:
            result = subprocess.run(
                ["curl", "-s", f"https://raw.githubusercontent.com/{owner}/{repo}/main/package.json"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                if "react" in deps or "next" in deps or "vue" in deps:
                    return "WebApp"
                if "express" in deps or "fastapi" in deps or "graphql" in deps:
                    return "API"
            return "Unknown"
        except Exception:
            return "Unknown"

    def classify_repo(self, repo: Dict) -> Dict:
        """Classify a single repo by monetization + software type."""
        url = repo.get("url", "")
        purpose = repo.get("PURPOSE", "").lower()
        readme = self._fetch_readme(url)

        combined_text = f"{purpose} {readme}"

        # Detect monetization
        monetization = "Unknown"
        for arch, keywords in self.MONETIZATION_KEYWORDS.items():
            if any(kw in combined_text for kw in keywords):
                monetization = arch
                break

        # Detect software type
        software_type = self._detect_tech_stack(url)
        if software_type == "Unknown":
            if "cli" in combined_text:
                software_type = "CLI"
            elif "library" in combined_text or "sdk" in combined_text:
                software_type = "Library"
            elif "terraform" in combined_text or "kubernetes" in combined_text:
                software_type = "Infra"
            elif "api" in combined_text or "rest" in combined_text:
                software_type = "API"

        # Extract OPCO from repo name
        opco = self._extract_opco(repo.get("name", ""))

        return {
            "monetization": monetization,
            "software_type": software_type,
            "opco": opco,
            "pricing": "Unknown"
        }

    def _extract_opco(self, repo_name: str) -> str:
        """Map sector prefix to OPCO."""
        sector_map = {
            "lt": "OPCO-007", "ec": "OPCO-001", "con": "OPCO-004", "bw": "OPCO-002",
            "fin": "OPCO-003", "edu": "OPCO-005", "food": "OPCO-006", "tech": "OPCO-008",
            "mc": "OPCO-009", "comm": "OPCO-010", "prof": "OPCO-011", "health": "OPCO-012",
            "mfg": "OPCO-013", "energy": "OPCO-014", "trans": "OPCO-015",
            "telecom": "OPCO-016", "gov": "OPCO-017", "emerging": "OPCO-018", "re": "OPCO-004",
        }
        prefix = repo_name.split("-")[0].lower()
        return sector_map.get(prefix, "Unknown")

    def run(self):
        """Tag all repos."""
        repos = self.registry.get("repositories", [])
        print(f"🏷️  Auto-tagging {len(repos)} repositories...\n")

        for i, repo in enumerate(repos):
            if i % 100 == 0:
                print(f"Progress: {i}/{len(repos)}")

            try:
                tags = self.classify_repo(repo)
                repo.update(tags)
                self.tagged_count += 1
            except Exception as e:
                print(f"❌ Failed to tag {repo.get('name')}: {e}")
                self.failed_count += 1

        # Save
        with open(self.registry_path, "w") as f:
            json.dump(self.registry, f, indent=2)

        print(f"\n✅ Complete: {self.tagged_count} tagged, {self.failed_count} failed")

if __name__ == "__main__":
    registry = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json")
    tagger = AutoTagger(str(registry))
    tagger.run()
