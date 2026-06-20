#!/usr/bin/env python3
"""
Close the join gap: link the 712 named ventures (VENTURES-CAPABILITIES-MAPPED.csv)
to the 618 capability records (VENTURES-CAPABILITIES-CROSSREF.csv) via the 9 sector
archetypes, then attach owned-vs-buy (vertical-integration) status per capability.

Output: VENTURE-FACTORY-MAP.csv  — one queryable row per venture:
  venture_id, name, sector, archetype, stage, capabilities,
  owned_caps, buy_caps, integration_pct, deal_layer
"""
import csv, collections

SRC = "VENTURES-CAPABILITIES-MAPPED.csv"
OUT = "VENTURE-FACTORY-MAP.csv"

# 1. Capability bundle per CROSSREF archetype (derived empirically from the 618 file)
ARCHETYPE_CAPS = {
    "market":   ["api", "authentication", "dashboard", "database", "portfolio"],
    "infra":    ["api", "authentication", "database", "monitoring", "security"],
    "devtools": ["api", "authentication", "dashboard", "database", "monitoring"],
    "ai":       ["api", "database", "knowledge-graph", "monitoring"],
    "edtech":   ["api", "authentication", "dashboard", "database", "workspace"],
    "fintech":  ["api", "authentication", "database", "monitoring", "payment", "security"],
    "con":      ["api", "construction", "dashboard", "database", "workspace"],
    "re":       ["api", "dashboard", "database", "portfolio", "workspace"],
    "health":   ["api", "authentication", "database", "monitoring", "security"],
}

# 2. Map the 18 named sectors -> 9 archetypes
SECTOR_ARCHETYPE = {
    "e-commerce": "market", "beauty-wellness": "market", "food-hospitality": "market",
    "professional-services": "market", "fitness-sports": "market", "media-content": "market",
    "specialized": "market", "community": "market",
    "operations": "infra", "logistics-transport": "infra",
    "technology": "devtools", "software-technology": "devtools",
    "emerging": "ai",
    "financial": "fintech",
    "education": "edtech", "education-training": "edtech",
    "construction": "con",
    "real-estate": "re",
}

# 3. Vertical-integration status per capability (do we OWN a repo, or BUY it)
OWNED = {  # backed by classified USE-tier repos
    "api": "own", "database": "own", "authentication": "own",
    "dashboard": "own", "monitoring": "own", "security": "own",
    "knowledge-graph": "own",            # LightRAG
    "portfolio": "buy",                  # thin backing
    "workspace": "buy",                  # thin backing
    "payment": "buy",                    # GAP: few repos, 47 ventures
    "construction": "buy",               # GAP: 1 repo, 20 ventures
}

# 4. Which deal-engine layer each archetype feeds (user's 8-layer deal graph)
ARCHETYPE_DEAL_LAYER = {
    "market": "L2 Service / L7 Data", "infra": "L2 Service / L6 Software",
    "devtools": "L6 Software", "ai": "L6 Software / L7 Data",
    "edtech": "L6 Software", "fintech": "L8 Capital / L6 Software",
    "con": "L2 Service / L3 Government", "re": "L5 Real Estate", "health": "L2 Service",
}

rows_out = []
cap_demand = collections.Counter()
arch_count = collections.Counter()
stage_count = collections.Counter()
own_total = buy_total = 0

with open(SRC) as f:
    for r in csv.DictReader(f):
        sector = r["sector"].strip()
        arch = SECTOR_ARCHETYPE.get(sector, "market")
        caps = ARCHETYPE_CAPS[arch]
        owned = [c for c in caps if OWNED.get(c) == "own"]
        buy   = [c for c in caps if OWNED.get(c) == "buy"]
        for c in caps:
            cap_demand[c] += 1
        own_total += len(owned); buy_total += len(buy)
        arch_count[arch] += 1
        stage_count[r["stage"].strip()] += 1
        rows_out.append({
            "venture_id": r["venture_id"], "name": r["name"], "sector": sector,
            "archetype": arch, "stage": r["stage"].strip(),
            "capabilities": " | ".join(caps),
            "owned_caps": " | ".join(owned), "buy_caps": " | ".join(buy),
            "integration_pct": round(100 * len(owned) / len(caps)),
            "deal_layer": ARCHETYPE_DEAL_LAYER[arch],
        })

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
    w.writeheader(); w.writerows(rows_out)

# ---- report ----
n = len(rows_out)
print(f"OK Joined {n} ventures -> {OUT}\n")
print("ARCHETYPE x VENTURES (the 9 production lines):")
for a, c in arch_count.most_common():
    print(f"  {a:9s} {c:4d}   caps: {' | '.join(ARCHETYPE_CAPS[a])}")
print(f"\nCAPABILITY DEMAND across 712 (the standard parts):")
for c, d in cap_demand.most_common():
    print(f"  {c:16s} {d:4d}  [{OWNED.get(c,'?').upper()}]")
print(f"\nVERTICAL INTEGRATION: {own_total} owned capability-slots vs {buy_total} buy "
      f"({round(100*own_total/(own_total+buy_total))}% integrated)")
print(f"\nCONVERSION FUNNEL (the Danaher gap):")
for s in ["planned", "mvp", "validation", "growth"]:
    print(f"  {s:11s} {stage_count.get(s,0):4d}")
