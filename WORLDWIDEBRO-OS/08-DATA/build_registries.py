#!/usr/bin/env python3
"""
Build the 08-DATA/registries layer (the source-of-truth graph) from the relocated
venture-hub CSVs. Regenerable: rerun after the source CSVs change.

Source (canonical copies under Influence-VBO):
  ventures-master.csv           venture_id,name,sector,stage,status,repository_url,...
  MASTER-REPO-REGISTRY.csv      repo_name,...,venture_id,venture_name,sector,...,agent_ids,health_score,...
  ventures_with_capabilities.csv venture_id,...,required_capabilities,top_repo_1..3

Emits into registries/:
  Entities:  ventures.csv, repositories.csv, opcos.csv, agents.csv
  Edges:     opco_venture_map.csv, venture_repo_map.csv,
             venture_agent_map.csv, agent_repo_map.csv, venture_capability_map.csv
"""
import csv, os, json, sys, subprocess
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/venture-hub")
OUT = os.path.join(BASE, "registries")
OS_ROOT = os.path.dirname(BASE)  # WORLDWIDEBRO-OS/
os.makedirs(OUT, exist_ok=True)

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    print(f"  [warn] {msg}", file=sys.stderr)


def read(name):
    """Read a source CSV; never crash the build if one is missing."""
    path = os.path.join(SRC, name)
    if not os.path.isfile(path):
        warn(f"source missing: {name} -> treating as empty")
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    return len(rows)


def norm_sector(s):
    return (s or "UNSPECIFIED").strip().upper().replace(" ", "_").replace("&", "AND")


def norm_name(s):
    """Normalize a repo name for matching registry <-> filesystem basename."""
    return (s or "").strip().lower().replace("_", "-").removesuffix(".git")


def scan_local_repos(root):
    """Filesystem truth: every git clone under root -> (name, rel_path, remote_url)."""
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        if ".git" in dirnames or ".git" in filenames:
            dirnames[:] = []  # don't descend into a repo's internals
            url = ""
            try:
                url = subprocess.run(
                    ["git", "-C", dirpath, "remote", "get-url", "origin"],
                    capture_output=True, text=True, timeout=10).stdout.strip()
            except Exception as e:
                warn(f"git remote failed for {dirpath}: {e}")
            rel = os.path.relpath(dirpath, os.path.dirname(OS_ROOT))
            found.append((os.path.basename(dirpath), rel, url))
    return found


ventures = read("ventures-master.csv")
repos = read("MASTER-REPO-REGISTRY.csv")
caps = read("ventures_with_capabilities.csv")
if not ventures or not repos:
    warn("core source CSV(s) empty — registry will be partial")

stats = {}

# --- Entity: ventures ---
stats["ventures.csv"] = write(
    "ventures.csv", ["venture_id", "name", "sector", "opco", "stage", "status"],
    [[v["venture_id"], v["name"], v["sector"], norm_sector(v["sector"]),
      v.get("stage", ""), v.get("status", "")] for v in ventures if v.get("venture_id")])

# --- Filesystem truth: scan local git clones (the "wire" to product repos) ---
clones = scan_local_repos(OS_ROOT)
name_to_clone = {}          # norm_name -> (rel_path, remote_url)  (first wins)
remote_to_paths = defaultdict(list)
for nm, rel, url in clones:
    name_to_clone.setdefault(norm_name(nm), (rel, url))
    if url:
        remote_to_paths[url].append(rel)

# repo_clones.csv = authoritative inventory of every local clone
stats["repo_clones.csv"] = write(
    "repo_clones.csv", ["repo_name", "local_path", "remote_url"],
    sorted([[nm, rel, url] for nm, rel, url in clones]))

# repo_duplicates.csv = same remote cloned to >1 location (cleanup targets)
dupes = [[url, str(len(p)), " | ".join(sorted(p))]
         for url, p in remote_to_paths.items() if len(p) > 1]
stats["repo_duplicates.csv"] = write(
    "repo_duplicates.csv", ["remote_url", "clone_count", "local_paths"], sorted(dupes))

# --- Entity: repositories (registry-of-record + remote_url/local_path wire) ---
matched = 0
repo_rows = []
for r in repos:
    if not r.get("repo_name"):
        continue
    rel, url = name_to_clone.get(norm_name(r["repo_name"]), ("", ""))
    if rel:
        matched += 1
    repo_rows.append([r["repo_name"], r.get("venture_id", ""), r.get("sector", ""),
                      r.get("status", ""), r.get("health_score", ""), url, rel])
# local clones not present in the registry -> append so the wire is complete
registry_names = {norm_name(r.get("repo_name", "")) for r in repos}
for nm, rel, url in clones:
    if norm_name(nm) not in registry_names:
        repo_rows.append([nm, "", "", "local_clone", "", url, rel])
stats["repositories.csv"] = write(
    "repositories.csv",
    ["repo_name", "venture_id", "sector", "status", "health_score", "remote_url", "local_path"],
    repo_rows)

# --- Entity: opcos (distinct sectors) ---
sectors = defaultdict(int)
for v in ventures:
    sectors[norm_sector(v["sector"])] += 1
stats["opcos.csv"] = write(
    "opcos.csv", ["opco_id", "sector_label", "venture_count"],
    [[k, k.replace("_", " ").title(), n] for k, n in sorted(sectors.items(), key=lambda x: -x[1])])

# --- Entity: agents (distinct from repo agent_ids) ---
agentset = set()
for r in repos:
    for a in (r.get("agent_ids") or "").replace(";", "|").replace(",", "|").split("|"):
        a = a.strip()
        if a:
            agentset.add(a)
stats["agents.csv"] = write("agents.csv", ["agent_id"], [[a] for a in sorted(agentset)])

# --- Edge: opco_venture_map ---
stats["opco_venture_map.csv"] = write(
    "opco_venture_map.csv", ["opco_id", "venture_id"],
    [[norm_sector(v["sector"]), v["venture_id"]] for v in ventures if v.get("venture_id")])

# --- Edge: venture_repo_map (from repo registry + capability top_repos) ---
vr = set()
for r in repos:
    if r.get("venture_id") and r.get("repo_name"):
        vr.add((r["venture_id"], r["repo_name"], "registry"))
for c in caps:
    vid = c.get("venture_id")
    for col in ("top_repo_1", "top_repo_2", "top_repo_3"):
        if c.get(col):
            vr.add((vid, c[col], "capability_match"))
stats["venture_repo_map.csv"] = write(
    "venture_repo_map.csv", ["venture_id", "repo_name", "source"], sorted(vr))

# --- Edge: venture_agent_map + agent_repo_map ---
va, ar = set(), set()
for r in repos:
    for a in (r.get("agent_ids") or "").replace(";", "|").replace(",", "|").split("|"):
        a = a.strip()
        if not a:
            continue
        if r.get("venture_id"):
            va.add((r["venture_id"], a))
        ar.add((a, r["repo_name"]))
stats["venture_agent_map.csv"] = write("venture_agent_map.csv", ["venture_id", "agent_id"], sorted(va))
stats["agent_repo_map.csv"] = write("agent_repo_map.csv", ["agent_id", "repo_name"], sorted(ar))

# --- Edge: venture_capability_map (pipe-delimited required_capabilities) ---
vc = []
for c in caps:
    vid = c.get("venture_id")
    for cap in (c.get("required_capabilities") or "").split("|"):
        cap = cap.strip()
        if cap:
            vc.append([vid, cap])
stats["venture_capability_map.csv"] = write(
    "venture_capability_map.csv", ["venture_id", "capability"], vc)

print(json.dumps(stats, indent=2))
print(f"\nTotal registry files: {len(stats)}  ->  {OUT}")
