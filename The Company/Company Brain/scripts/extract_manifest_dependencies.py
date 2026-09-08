import json, yaml, subprocess, re

# Load reality and repos
reality = json.load(open("_REGISTRIES/CANONICAL/OWNED_REPO_CODE_REALITY.json"))
repos = yaml.safe_load(open("_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml"))["repositories"]

with_manifest = {k: v for k, v in reality.items() if v.get("has_manifest")}
print(f"Total repos with manifests to extract: {len(with_manifest)}")

items = []
for rid, v in with_manifest.items():
    r = repos.get(rid)
    if not r:
        continue
    parts = r["github_url"].rstrip("/").split("/")
    if len(parts) < 2:
        continue
    owner, name = parts[-2], parts[-1]
    for m in v.get("manifests", []):
        items.append((rid, r["repo_name"], owner, name, m))

print(f"Total manifest files to extract: {len(items)}")

def chunker(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

results = {}
BATCH_SIZE = 30

for batch_idx, batch in enumerate(chunker(items, BATCH_SIZE)):
    fields = []
    for i, (rid, rname, owner, name, m) in enumerate(batch):
        fields.append(f"""r_{i}: repository(owner: "{owner}", name: "{name}") {{
            object(expression: "HEAD:{m}") {{
                ... on Blob {{
                    text
                }}
            }}
        }}""")
    
    query = "query {\n" + "\n".join(fields) + "\n}"
    out = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"], capture_output=True, text=True)
    if out.returncode != 0:
        print(f"Batch {batch_idx} error: {out.stderr[:100]}")
        continue
    
    data = json.loads(out.stdout).get("data", {})
    for i, (rid, rname, owner, name, m) in enumerate(batch):
        blob = data.get(f"r_{i}", {}).get("object")
        text = blob.get("text", "") if blob else ""
        if rid not in results:
            results[rid] = {
                "repo_name": rname,
                "manifests": {},
                "dependencies": set(),
                "dev_dependencies": set()
            }
        results[rid]["manifests"][m] = bool(text)
        
        # Parse package.json
        if m == "package.json" and text:
            try:
                pkg = json.loads(text)
                deps = list((pkg.get("dependencies") or {}).keys())
                dev_deps = list((pkg.get("devDependencies") or {}).keys())
                results[rid]["dependencies"].update(deps)
                results[rid]["dev_dependencies"].update(dev_deps)
            except Exception:
                pass
        
        # Parse requirements.txt
        elif m == "requirements.txt" and text:
            for line in text.split("\n"):
                line = line.strip()
                if line and not line.startswith("#") and not line.startswith("-"):
                    pkg_name = re.split(r"[=<>~;]", line)[0].strip().lower()
                    if pkg_name:
                        results[rid]["dependencies"].add(pkg_name)
    print(f"  Batch {batch_idx+1}/{(len(items)+BATCH_SIZE-1)//BATCH_SIZE} completed.", flush=True)

final_output = {}
for rid, v in results.items():
    final_output[rid] = {
        "repo_name": v["repo_name"],
        "manifest_files": v["manifests"],
        "dependencies": sorted(list(v["dependencies"])),
        "dev_dependencies": sorted(list(v["dev_dependencies"])),
        "dep_count": len(v["dependencies"])
    }

with open("_REGISTRIES/CANONICAL/OWNED_REPO_DEPENDENCIES.json", "w") as f:
    json.dump(final_output, f, indent=2)

print(f"\nSUCCESS: Extracted and parsed dependencies for {len(final_output)} repos!")
