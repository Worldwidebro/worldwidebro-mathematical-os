"""Dataset extraction and corpus generation from GBrain manifests, skills, and routing fixtures."""

import glob
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def find_repo_root(start_path: Optional[Path] = None) -> Path:
    """Finds the root of the Company Brain workspace."""
    curr = (start_path or Path(__file__)).resolve()
    for p in [curr] + list(curr.parents):
        if (p / "_TOOLS" / "gbrain").is_dir() or (p / "ANTIGRAVITY.md").is_file():
            return p
    # Fallback to current working directory
    return Path.cwd()


class GBrainCorpus:
    """Extracts, indexes, and manages ground-truth skills and routing eval data."""

    def __init__(self, workspace_root: Optional[Path] = None):
        self.workspace_root = workspace_root or find_repo_root()
        self.skills_dir = self.workspace_root / "_TOOLS" / "gbrain" / "skills"
        self.manifest_path = self.skills_dir / "manifest.json"
        self.resolver_path = self.skills_dir / "RESOLVER.md"
        
        self.skills: Dict[str, Dict[str, Any]] = {}
        self.fixtures: List[Dict[str, Any]] = []
        self._load()

    def _load(self) -> None:
        """Load manifest, skills frontmatter, and routing-eval fixtures."""
        # 1. Load manifest.json
        if self.manifest_path.is_file():
            with open(self.manifest_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data.get("skills", []):
                    name = item.get("name")
                    if name:
                        self.skills[name] = {
                            "name": name,
                            "path": item.get("path"),
                            "description": item.get("description", ""),
                            "triggers": [],
                            "routing_fixtures": [],
                        }

        # 2. Extract triggers from SKILL.md files
        for skill_dir in self.skills_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if skill_md.is_file():
                skill_name = skill_dir.name
                triggers = self._extract_frontmatter_triggers(skill_md)
                if skill_name in self.skills:
                    self.skills[skill_name]["triggers"] = triggers
                else:
                    self.skills[skill_name] = {
                        "name": skill_name,
                        "path": f"{skill_name}/SKILL.md",
                        "description": "",
                        "triggers": triggers,
                        "routing_fixtures": [],
                    }

        # 3. Load all routing-eval.jsonl fixtures
        fixture_pattern = str(self.skills_dir / "*" / "routing-eval.jsonl")
        for fixture_file in glob.glob(fixture_pattern):
            skill_name = Path(fixture_file).parent.name
            with open(fixture_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("//"):
                        continue
                    try:
                        record = json.loads(line)
                        intent = record.get("intent")
                        expected = record.get("expected_skill", skill_name)
                        ambiguous = record.get("ambiguous_with", [])
                        if intent and expected:
                            fixture_entry = {
                                "intent": intent,
                                "expected_skill": expected,
                                "ambiguous_with": ambiguous,
                                "source_skill": skill_name,
                                "source_file": os.path.relpath(fixture_file, self.workspace_root),
                            }
                            self.fixtures.append(fixture_entry)
                            if skill_name in self.skills:
                                self.skills[skill_name]["routing_fixtures"].append(fixture_entry)
                    except json.JSONDecodeError:
                        continue

    @staticmethod
    def _extract_frontmatter_triggers(skill_md_path: Path) -> List[str]:
        """Extracts trigger strings from SKILL.md frontmatter."""
        triggers = []
        try:
            with open(skill_md_path, "r", encoding="utf-8") as f:
                content = f.read()
            match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
            if match:
                frontmatter = match.group(1)
                trigger_match = re.search(r"triggers:\s*\n((?:\s*-\s*.*?\n)+)", frontmatter)
                if trigger_match:
                    lines = trigger_match.group(1).strip().split("\n")
                    for l in lines:
                        cleaned = re.sub(r"^\s*-\s*[\"']?(.*?)[\"']?\s*$", r"\1", l)
                        if cleaned:
                            triggers.append(cleaned)
        except Exception:
            pass
        return triggers

    def get_all_fixtures(self) -> List[Dict[str, Any]]:
        return self.fixtures

    def get_skill_names(self) -> List[str]:
        return sorted(list(self.skills.keys()))

    def get_skill_documents(self) -> List[Dict[str, str]]:
        """Returns documents for lexical/dense indexing."""
        docs = []
        for name, meta in self.skills.items():
            doc_text = f"Skill: {name}\nDescription: {meta['description']}\nTriggers: {', '.join(meta.get('triggers', []))}"
            docs.append({
                "skill": name,
                "text": doc_text,
                "description": meta["description"],
                "triggers": meta.get("triggers", []),
            })
        return docs


if __name__ == "__main__":
    corpus = GBrainCorpus()
    print(f"Loaded {len(corpus.skills)} skills and {len(corpus.fixtures)} routing fixtures.")
    for s in list(corpus.skills.keys())[:5]:
        print(f" - {s}: {len(corpus.skills[s]['routing_fixtures'])} fixtures, {len(corpus.skills[s]['triggers'])} triggers")
