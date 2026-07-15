#!/usr/bin/env python3
"""
build_department_view.py — the org-chart layer.

Consumes repo-intelligence-scores.json (from build_repo_intelligence_score.py) and maps
every scored repo into your AI-company department structure, so the repo portfolio reads
as a staffed organization instead of a flat list.

Departments (each repo is assigned to its single best-fit department, then can also appear
as a "supporting" tool under others):

    AI-CTO   Engineering / build tooling      llm, agent, mcp, devtools, api, automation
    CDO      Data & Knowledge                 database, graph, rag, search, analytics, embeddings
    AI-CISO  Security & Reliability           security, authentication, monitoring
    AI-CMO   Marketing & Growth               crm, dashboard, notifications, portfolio, seo, content
    AI-CFO   Finance & Commerce               payments, invoice, billing, accounting, commerce
    AI-COO   Operations & Delivery            scheduling, workspace, ocr, construction, logistics
    AI-CPO   Product & Applications           (fallback for Product-category repos w/ no strong signal)

Assignment is signal-driven: each department has a set of capability keywords; a repo's
score for a department = sum of matched-capability weights (+ a small category nudge). The
repo is placed in its highest-scoring department; ties break toward the earlier department
in DEPT_ORDER. Repos with no capability match fall back by CATEGORY, else "Unassigned".

Output:
    repo-department-view.json   department -> ranked repos (by unified score) + rollups
    DEPARTMENT-VIEW.md          human-readable org chart with the top repos per department

Usage:
    python3 build_department_view.py
    python3 build_department_view.py --top 10     # show top N per dept in the console
"""
import argparse
import json
import os
from collections import defaultdict
from datetime import date

DOCS = "/Users/acebless/Documents"
SCORES = f"{DOCS}/repo-intelligence-scores.json"

OUT_JSON = f"{DOCS}/repo-department-view.json"
OUT_MD = f"{DOCS}/DEPARTMENT-VIEW.md"

# Ordered so ties break toward the more foundational department.
DEPT_ORDER = ["AI-CTO", "CDO", "AI-CISO", "AI-CMO", "AI-CFO", "AI-COO", "AI-CPO"]

DEPARTMENTS = {
    "AI-CTO": {
        "title": "AI CTO — Engineering & Build Tooling",
        "caps": {"llm": 3, "agent": 3, "mcp": 3, "devtools": 2, "api": 2,
                 "automation": 2, "machine-learning": 2, "rag": 1},
        "categories": {"Infrastructure": 1, "Service": 1},
    },
    "CDO": {
        "title": "Chief Data Officer — Data & Knowledge",
        "caps": {"database": 3, "graph": 3, "rag": 3, "search": 3, "embeddings": 3,
                 "analytics": 2, "vector-search": 3},
        "categories": {"Asset": 1},
    },
    "AI-CISO": {
        "title": "AI CISO — Security & Reliability",
        "caps": {"security": 3, "authentication": 3, "monitoring": 3},
        "categories": {},
    },
    "AI-CMO": {
        "title": "AI CMO — Marketing & Growth",
        "caps": {"crm": 3, "dashboard": 2, "notifications": 2, "portfolio": 2,
                 "seo": 3, "content": 2, "fashion-design": 2},
        "categories": {},
    },
    "AI-CFO": {
        "title": "AI CFO — Finance & Commerce",
        "caps": {"payments": 3, "invoice": 3, "billing": 3, "accounting": 3, "commerce": 2},
        "categories": {},
    },
    "AI-COO": {
        "title": "AI COO — Operations & Delivery",
        "caps": {"scheduling": 3, "workspace": 2, "ocr": 2, "construction": 2,
                 "logistics": 2, "dispatch": 3},
        "categories": {"Product": 1},
    },
    "AI-CPO": {
        "title": "AI CPO — Product & Applications",
        "caps": {},  # fallback department; scored only via category
        "categories": {"Product": 2},
    },
}

# Category-based fallback when a repo matched no department capabilities at all.
CATEGORY_FALLBACK = {
    "Infrastructure": "AI-CTO",
    "Service": "AI-CTO",
    "Asset": "CDO",
    "Product": "AI-CPO",
    "Unclassified": "Unassigned",
    "Unknown": "Unassigned",
}


def _load_scores():
    if not os.path.exists(SCORES):
        raise SystemExit(
            f"[error] {SCORES} not found. Run build_repo_intelligence_score.py first "
            f"(or run_repo_intelligence_pipeline.py to build the whole chain)."
        )
    with open(SCORES) as f:
        return json.load(f)


def assign_department(repo):
    """Return (dept_key, dept_fit_score, matched_caps). Signal-driven with category fallback."""
    caps = set(repo.get("capabilities") or [])
    category = repo.get("category", "Unknown")

    best_dept, best_fit, best_matches = None, 0, []
    for dept in DEPT_ORDER:  # ordered => deterministic tie-break
        spec = DEPARTMENTS[dept]
        matches = [(c, spec["caps"][c]) for c in caps if c in spec["caps"]]
        fit = sum(w for _, w in matches)
        fit += spec["categories"].get(category, 0)
        if fit > best_fit:
            best_fit = fit
            best_dept = dept
            best_matches = [c for c, _ in matches]

    if best_dept is None or best_fit == 0:
        return CATEGORY_FALLBACK.get(category, "Unassigned"), 0, []
    return best_dept, best_fit, sorted(best_matches)


def build(top=None):
    print("=" * 78)
    print("REPOSITORY DEPARTMENT VIEW — AI-COMPANY ORG CHART")
    print("=" * 78)
    data = _load_scores()
    repos = data.get("repositories", [])
    print(f"  loaded {len(repos)} scored repos "
          f"(registry avg {data.get('metadata', {}).get('average_score', '?')}/100)")

    dept_members = defaultdict(list)
    for r in repos:
        dept, fit, matched = assign_department(r)
        dept_members[dept].append({
            "name": r["name"],
            "total_score": r["total_score"],
            "tier": r["tier"],
            "category": r["category"],
            "stars": r.get("stars", 0),
            "capabilities": r.get("capabilities", []),
            "department_fit": fit,
            "matched_capabilities": matched,
            "venture_match_count": r.get("venture_match_count", 0),
            "url": r.get("url", ""),
        })

    # Rank each department's members by unified score, then dept-fit.
    for members in dept_members.values():
        members.sort(key=lambda m: (m["total_score"], m["department_fit"]), reverse=True)

    # Rollups
    dept_order_full = DEPT_ORDER + ["Unassigned"]
    rollup = {}
    for dept in dept_order_full:
        members = dept_members.get(dept, [])
        if not members and dept == "Unassigned":
            continue
        scores = [m["total_score"] for m in members]
        rollup[dept] = {
            "title": DEPARTMENTS.get(dept, {}).get("title", "Unassigned — no capability/category signal"),
            "repo_count": len(members),
            "avg_score": round(sum(scores) / len(scores), 1) if scores else 0,
            "top_repo": members[0]["name"] if members else None,
            "top_score": members[0]["total_score"] if members else 0,
        }

    out = {
        "metadata": {
            "generated_date": date.today().isoformat(),
            "total_repos": len(repos),
            "source": "repo-intelligence-scores.json",
            "departments": dept_order_full,
            "rollup": rollup,
        },
        "departments": {d: dept_members.get(d, []) for d in dept_order_full if dept_members.get(d)},
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)

    # Markdown org chart
    lines = [
        "# AI-Company Department View",
        "",
        f"_Generated {date.today().isoformat()} from `repo-intelligence-scores.json` — "
        f"{len(repos)} repositories mapped into departments._",
        "",
        "Each repository is assigned to its single best-fit department based on its "
        "capabilities and category. Ranked by the unified 100-point intelligence score.",
        "",
        "## Department Rollup",
        "",
        "| Department | Repos | Avg Score | Top Repo |",
        "|---|---:|---:|---|",
    ]
    for dept in dept_order_full:
        if dept not in rollup:
            continue
        r = rollup[dept]
        lines.append(f"| **{dept}** — {r['title'].split('—')[-1].strip()} | {r['repo_count']} "
                     f"| {r['avg_score']} | {r['top_repo']} ({r['top_score']}) |")

    n = top or 10
    for dept in dept_order_full:
        members = dept_members.get(dept, [])
        if not members:
            continue
        title = DEPARTMENTS.get(dept, {}).get("title", "Unassigned")
        lines += ["", f"## {dept} — {title.split('—')[-1].strip() if '—' in title else title}",
                  "", f"_{len(members)} repositories._", "",
                  "| # | Repo | Score | Tier | Matched Capabilities |",
                  "|---:|---|---:|---|---|"]
        for i, m in enumerate(members[:n], 1):
            caps = ", ".join(m["matched_capabilities"][:5]) or "_(category fallback)_"
            lines.append(f"| {i} | [{m['name']}]({m['url']}) | {m['total_score']} | "
                         f"{m['tier'].split('—')[0].strip()} | {caps} |")

    with open(OUT_MD, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\n  wrote {OUT_JSON}")
    print(f"  wrote {OUT_MD}")
    print("\n  Department rollup:")
    print(f"    {'dept':10s} {'repos':>6s} {'avg':>6s}  top repo")
    for dept in dept_order_full:
        if dept not in rollup:
            continue
        r = rollup[dept]
        print(f"    {dept:10s} {r['repo_count']:>6d} {r['avg_score']:>6.1f}  "
              f"{r['top_repo']} ({r['top_score']})")

    if top:
        for dept in dept_order_full:
            members = dept_members.get(dept, [])
            if not members:
                continue
            print(f"\n  {dept} — top {min(top, len(members))}:")
            for i, m in enumerate(members[:top], 1):
                print(f"    {i:>2}  {m['total_score']:>3}  {m['name'][:38]:38s}  "
                      f"{', '.join(m['matched_capabilities'][:3])}")
    print("=" * 78)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=None, help="print top N repos per department")
    a = ap.parse_args()
    build(top=a.top)
