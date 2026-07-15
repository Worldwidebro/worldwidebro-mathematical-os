#!/usr/bin/env python3
"""
build_repo_summaries.py — Task #2: compact (~250-token) repo summary cards.

Compression layer for retrieval: turns each repo (which could be 25k tokens of README)
into a ~150-250 token structured card assembled DETERMINISTICALLY from the registry
(PURPOSE 96% populated) + canonical capability vocabulary. No LLM, no cloud — fast & local.

Sources:
  - REPOSITORY-REGISTRY.json          (1,597 repos: PURPOSE, CATEGORY, TECH_STACK, scores, capabilities)
  - registries/capability_vocabulary.json  (maps raw GitHub topics -> canonical capabilities)

Output:
  - repo-summaries.json   { repo_name: {name, category, language, purpose,
                            capabilities[], tech, scores{}, high_value, summary_text} }

Consumed by retrieve.py (Task #5) so Claude sees cards, not raw repos.

Usage:
  python3 build_repo_summaries.py
  python3 build_repo_summaries.py --show 5
"""
import argparse
import json
import re
from datetime import date

DOCS = "/Users/acebless/Documents"
REGISTRY = (f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/"
            "REFERENCE/REPOSITORY-REGISTRY.json")
VOCAB = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json"
OUT = f"{DOCS}/repo-summaries.json"


def _norm(c):
    c = re.sub(r"[\s_]+", "-", (c or "").strip().lower())
    return re.sub(r"-+", "-", c).strip("-")


def load_alias_map():
    v = json.load(open(VOCAB))["canonical"]
    m = {}
    for canon, meta in v.items():
        m[canon] = canon
        for a in meta.get("aliases", []):
            m[_norm(a)] = canon
    return m


def parse_list(val):
    """capabilities/dependencies are stored as stringified arrays like \"['a','b']\"."""
    if isinstance(val, list):
        return val
    if not val or val in ("[]", ""):
        return []
    try:
        return json.loads(val.replace("'", '"'))
    except Exception:
        return [x.strip(" '\"") for x in str(val).strip("[]").split(",") if x.strip()]


def canon_caps(raw_caps, alias):
    out = []
    for c in raw_caps:
        out.append(alias.get(_norm(c), _norm(c)))
    # dedupe, keep order
    seen, res = set(), []
    for c in out:
        if c and c not in seen:
            seen.add(c)
            res.append(c)
    return res


def build(show=0):
    alias = load_alias_map()
    repos = json.load(open(REGISTRY))["repositories"]
    summaries = {}
    for r in repos:
        name = r.get("name", "")
        if not name:
            continue
        caps = canon_caps(parse_list(r.get("capabilities")), alias)
        scores = {
            "reusability": int(str(r.get("reusability_score", "0") or "0")),
            "revenue": int(str(r.get("revenue_potential", "0") or "0")),
            "strategic": int(str(r.get("strategic_value", "0") or "0")),
        }
        high_value = max(scores.values()) >= 6
        purpose = (r.get("PURPOSE", "") or "").strip()
        tech = r.get("TECH_STACK", "") or r.get("language", "")
        cap_str = ", ".join(caps[:8]) if caps else "—"
        summary_text = (
            f"{name} [{r.get('CATEGORY','')}] — {purpose[:200]}. "
            f"Capabilities: {cap_str}. Tech: {tech}. "
            f"Scores reuse={scores['reusability']} revenue={scores['revenue']} strategic={scores['strategic']}."
        )
        summaries[name] = {
            "name": name,
            "category": r.get("CATEGORY", ""),
            "language": r.get("language", ""),
            "purpose": purpose[:300],
            "capabilities": caps,
            "tech": tech,
            "url": r.get("url", ""),
            "scores": scores,
            "high_value": high_value,
            "summary_text": summary_text,
        }
    meta = {
        "generated_date": date.today().isoformat(),
        "total": len(summaries),
        "high_value": sum(1 for s in summaries.values() if s["high_value"]),
        "avg_summary_chars": round(sum(len(s["summary_text"]) for s in summaries.values()) / max(len(summaries), 1)),
    }
    json.dump({"metadata": meta, "summaries": summaries}, open(OUT, "w"), indent=2)
    print(f"wrote {OUT}")
    print(f"  {meta['total']} summaries | high_value={meta['high_value']} | "
          f"avg {meta['avg_summary_chars']} chars (~{meta['avg_summary_chars']//4} tokens)")
    if show:
        for s in list(summaries.values())[:show]:
            print(f"\n--- {s['name']} ---\n{s['summary_text']}")
    return summaries


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", type=int, default=0)
    a = ap.parse_args()
    build(show=a.show)
