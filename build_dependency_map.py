#!/usr/bin/env python3
"""
build_dependency_map.py — unify EVERYTHING into one OS dependency / install manifest.

Brings skills + MCPs into the same graph as repos/capabilities/ventures so the system
knows: what to install, what each MCP provides, and how repos align to ventures.

Ingests (all local):
  - MCP_REGISTRY.json            16 MCPs (name, status, priority, category, capabilities, config)
  - skills-lock.json             installed skills (source, skillPath)
  - capability_vocabulary.json   canonical capabilities (for MCP->Capability mapping)
  - Neo4j                        existing Repo/Capability/Venture/OPCO/Entity graph (alignment stats)

Outputs:
  - DEPENDENCY-MAP.json          single manifest: services + mcps + skills + scripts + artifacts
                                 + graph alignment summary
  - Neo4j: (:MCP)-[:PROVIDES]->(:Capability), (:Skill) nodes (installable units)

Usage: python3 build_dependency_map.py
"""
import json
import re
from datetime import date

from neo4j import GraphDatabase

DOCS = "/Users/acebless/Documents"
MCP_REG = f"{DOCS}/MCP_REGISTRY.json"
SKILLS = f"{DOCS}/skills-lock.json"
VOCAB = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json"
OUT = f"{DOCS}/DEPENDENCY-MAP.json"
NEO4J = ("bolt://localhost:7687", ("neo4j", "ventures2026"))

# Local services the OS depends on (install/run truth)
SERVICES = [
    {"name": "Ollama", "role": "local LLM + embeddings (nomic-embed, qwen3:8b)",
     "port": 11434, "install": "brew install ollama; ollama pull nomic-embed-text qwen3:8b", "required": True},
    {"name": "Qdrant", "role": "vector store (notes + repositories collections)",
     "port": 6333, "install": "docker run -p 6333:6333 qdrant/qdrant", "required": True},
    {"name": "Neo4j", "role": "knowledge graph (repos/caps/ventures/opcos/entities/mcps)",
     "port": 7474, "install": "docker compose up neo4j  (auth neo4j/ventures2026)", "required": True},
    {"name": "gh CLI", "role": "GitHub API auth for README/metadata fetch",
     "port": None, "install": "brew install gh; gh auth login", "required": True},
]

# Pipeline scripts in run order (all deterministic, ~0 LLM tokens)
SCRIPTS = [
    "build_capability_catalog.py", "build_repo_summaries.py", "build_repo_rag.py",
    "build_readme_corpus.py", "build_capability_backfill.py", "build_venture_capabilities.py",
    "build_repo_graph.py", "build_dependency_map.py", "retrieve.py",
]


def _norm(c):
    c = re.sub(r"[\s_]+", "-", (c or "").strip().lower())
    return re.sub(r"-+", "-", c).strip("-")


def alias_map():
    v = json.load(open(VOCAB))["canonical"]
    m = {}
    for canon, meta in v.items():
        m[canon] = canon
        for a in meta.get("aliases", []):
            m[_norm(a)] = canon
    return m, v


def parse_list(val):
    if isinstance(val, list):
        return val
    if not val or val == "[]":
        return []
    try:
        return json.loads(val.replace("'", '"'))
    except Exception:
        return [x.strip(" '\"") for x in str(val).strip("[]").split(",") if x.strip()]


def map_mcp_caps(mcp, alias):
    """Map an MCP's category + capability verbs onto canonical capabilities."""
    found = set()
    blob = (mcp.get("category", "") + " " + mcp.get("description", "") + " " +
            " ".join(parse_list(mcp.get("capabilities")))).lower()
    for raw, canon in alias.items():
        if raw in blob:
            found.add(canon)
    # category direct hit
    cat = _norm(mcp.get("category", ""))
    if cat in alias:
        found.add(alias[cat])
    return sorted(found)


def main():
    alias, canon = alias_map()
    mcps = json.load(open(MCP_REG))["mcps"]
    skills = json.load(open(SKILLS))["skills"]

    mcp_out = {}
    for key, m in mcps.items():
        mcp_out[key] = {
            "name": m.get("name", key), "status": m.get("status", ""),
            "priority": m.get("priority", ""), "category": m.get("category", ""),
            "config_location": m.get("config_location", ""),
            "provides_capabilities": map_mcp_caps(m, alias),
        }
    skills_out = {k: {"source": s.get("source", ""), "path": s.get("skillPath", "")}
                  for k, s in skills.items()}

    # Load MCP + Skill nodes into Neo4j and link MCP->Capability
    d = GraphDatabase.driver(NEO4J[0], auth=NEO4J[1])
    with d.session() as s:
        for key, m in mcp_out.items():
            s.run("MERGE (x:MCP {key:$k}) SET x.name=$n, x.status=$st, x.priority=$p, "
                  "x.category=$c, x.config=$cfg",
                  k=key, n=m["name"], st=m["status"], p=m["priority"],
                  c=m["category"], cfg=m["config_location"])
            for cap in m["provides_capabilities"]:
                s.run("MATCH (x:MCP {key:$k}),(c:Capability {name:$cap}) MERGE (x)-[:PROVIDES]->(c)",
                      k=key, cap=cap)
        for name, sk in skills_out.items():
            s.run("MERGE (x:Skill {name:$n}) SET x.source=$src, x.path=$p",
                  n=name, src=sk["source"], p=sk["path"])
        # alignment summary from the graph
        stats = {}
        for label in ["Repo", "Capability", "Venture", "OPCO", "Entity", "MCP", "Skill"]:
            stats[label] = s.run(f"MATCH (n:{label}) RETURN count(n) AS c").single()["c"]
        for rel in ["IMPLEMENTS", "NEEDS", "BELONGS_TO", "PROVIDES"]:
            stats[rel] = s.run(f"MATCH ()-[r:{rel}]->() RETURN count(r) AS c").single()["c"]
        # capabilities with full stack coverage: repo implements + venture needs + mcp provides
        covered = s.run("""
            MATCH (c:Capability)
            OPTIONAL MATCH (r:Repo)-[:IMPLEMENTS]->(c) WITH c, count(r) AS repos
            OPTIONAL MATCH (v:Venture)-[:NEEDS]->(c) WITH c, repos, count(v) AS vents
            OPTIONAL MATCH (m:MCP)-[:PROVIDES]->(c) WITH c, repos, vents, count(m) AS mcps
            RETURN c.name AS cap, repos, vents, mcps ORDER BY repos+vents+mcps DESC
        """)
        cap_coverage = [dict(r) for r in covered]
    d.close()

    manifest = {
        "metadata": {"generated_date": date.today().isoformat(),
                     "purpose": "OS install + dependency map: services, MCPs, skills, scripts, "
                                "and repo<->venture alignment via the knowledge graph."},
        "services": SERVICES,
        "mcps": mcp_out,
        "skills": {"count": len(skills_out), "items": skills_out},
        "pipeline_scripts": SCRIPTS,
        "data_artifacts": [
            "REPOSITORY-REGISTRY.json", "repo-summaries.json", "readmes.json",
            "repo-capabilities-backfill.json", "venture-capabilities-proposed.csv",
            "registries/capability_vocabulary.json", "registries/capabilities-catalog.json",
            "registries/ventures.csv", "registries/opco_venture_map.csv",
        ],
        "graph_stats": stats,
        "capability_coverage": cap_coverage,
    }
    json.dump(manifest, open(OUT, "w"), indent=2)
    print(f"wrote {OUT}")
    print("graph:", {k: stats[k] for k in ["Repo", "Capability", "Venture", "MCP", "Skill"]})
    print(f"edges: IMPLEMENTS={stats['IMPLEMENTS']} NEEDS={stats['NEEDS']} "
          f"PROVIDES={stats['PROVIDES']} BELONGS_TO={stats['BELONGS_TO']}")
    print(f"skills installed: {len(skills_out)} | MCPs: {len(mcp_out)}")
    print("\nTop capabilities by full-stack coverage (repos / ventures / mcps):")
    for c in cap_coverage[:12]:
        print(f"  {c['cap']:<16} repos={c['repos']:<4} ventures={c['vents']:<4} mcps={c['mcps']}")


if __name__ == "__main__":
    main()
