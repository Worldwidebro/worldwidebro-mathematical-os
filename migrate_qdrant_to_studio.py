#!/usr/bin/env python3
"""
migrate_qdrant_to_studio.py — copy Qdrant collections Air (localhost) -> Mac Studio.

Fixes the split-brain: this session's `repositories` + `notes` live on the Air;
Studio had older `starred_repos`/`ventures`. This mirrors the Air collections to Studio
so the always-on brain has the real data. Deterministic scroll + upsert (no snapshot files).

Usage:
  python3 migrate_qdrant_to_studio.py                 # repositories + notes
  python3 migrate_qdrant_to_studio.py notes           # one collection
  SRC=http://localhost:6333 DST=http://100.87.214.70:6333 python3 migrate_qdrant_to_studio.py
"""
import os
import sys

import requests

SRC = os.environ.get("SRC", "http://localhost:6333")
DST = os.environ.get("DST", "http://100.87.214.70:6333")
DEFAULT = ["repositories", "notes"]


def log(*a):
    print(*a, flush=True)


def get_config(coll):
    r = requests.get(f"{SRC}/collections/{coll}", timeout=15)
    r.raise_for_status()
    v = r.json()["result"]["config"]["params"]["vectors"]
    return v["size"], v["distance"]


def ensure_dst(coll, size, distance):
    requests.delete(f"{DST}/collections/{coll}", timeout=30)
    requests.put(f"{DST}/collections/{coll}",
                 json={"vectors": {"size": size, "distance": distance}}, timeout=30).raise_for_status()


def migrate(coll):
    size, distance = get_config(coll)
    log(f"[{coll}] src config: dim={size} dist={distance} -> creating on Studio")
    ensure_dst(coll, size, distance)
    moved, nxt = 0, None
    while True:
        body = {"limit": 256, "with_vector": True, "with_payload": True}
        if nxt:
            body["offset"] = nxt
        res = requests.post(f"{SRC}/collections/{coll}/points/scroll", json=body, timeout=60).json()["result"]
        pts = res["points"]
        if not pts:
            break
        batch = [{"id": p["id"], "vector": p["vector"], "payload": p.get("payload", {})} for p in pts]
        requests.put(f"{DST}/collections/{coll}/points", json={"points": batch}, timeout=120).raise_for_status()
        moved += len(batch)
        nxt = res.get("next_page_offset")
        if moved % 1024 == 0:
            log(f"  {coll}: {moved} points...")
        if not nxt:
            break
    dst_count = requests.get(f"{DST}/collections/{coll}", timeout=15).json()["result"]["points_count"]
    log(f"[{coll}] DONE: moved {moved}, Studio now has {dst_count}")


if __name__ == "__main__":
    colls = sys.argv[1:] or DEFAULT
    log(f"migrating {colls}: {SRC} -> {DST}")
    for c in colls:
        try:
            migrate(c)
        except Exception as e:
            log(f"[{c}] FAILED: {e}")
