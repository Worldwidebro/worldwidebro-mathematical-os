#!/usr/bin/env python3
"""Utility to list recent files with no graph connections.

1. Find files created in the last 7 days (`find -type f -mtime -7`).
2. Load `graphify-out/graph.json` (nodes and edges).
3. Build a set of node IDs that have at least one edge.
4. For each recent file, compute its expected node ID according to Graphify's naming rules
   (parent_dir + '_' + filename stem, lower‑cased, non‑alphanumeric -> '_').
5. If the node exists in the graph but is not in the edge set, report it as *disconnected*.
6. Print a concise markdown table.
"""
import json
import os
import pathlib
from datetime import datetime, timedelta

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
GRAPH_PATH = PROJECT_ROOT / "graphify-out" / "graph.json"

# 1. Recent files (mtime within 7 days)
seven_days_ago = datetime.now() - timedelta(days=7)
recent_files = []
for root, _, files in os.walk(PROJECT_ROOT):
    for f in files:
        p = pathlib.Path(root) / f
        try:
            mtime = datetime.fromtimestamp(p.stat().st_mtime)
        except OSError:
            continue
        if mtime > seven_days_ago:
            recent_files.append(p)

# 2. Load graph
with open(GRAPH_PATH, "r", encoding="utf-8") as gf:
    graph = json.load(gf)
nodes = {n["id"]: n for n in graph.get("nodes", [])}
edges = graph.get("edges", [])
connected_nodes = set()
for e in edges:
    connected_nodes.update([e.get("source"), e.get("target")])

# Helper to compute expected node id per Graphify rules
def node_id_for_path(path: pathlib.Path) -> str:
    rel = path.relative_to(PROJECT_ROOT)
    parts = rel.parts
    if len(parts) == 1:
        stem = path.stem.lower()
    else:
        parent = parts[-2].lower()
        stem = path.stem.lower()
        stem = f"{parent}_{stem}"
    # replace non‑alphanumeric with _
    return "_".join([c if c.isalnum() else "_" for c in stem])

# 4. Identify disconnected recent files
disconnected = []
for f in recent_files:
    nid = node_id_for_path(f)
    if nid in nodes and nid not in connected_nodes:
        disconnected.append((f, nid))

# 5. Output markdown
print("## Recent Files with No Graph Connections\n")
print("| File | Node ID |\n|---|---|")
for f, nid in disconnected[:20]:
    print(f"| {f.relative_to(PROJECT_ROOT)} | {nid} |")
if len(disconnected) > 20:
    print(f"| ... and {len(disconnected)-20} more | |")
