import json
import yaml
import os
from datetime import datetime, timezone

def main():
    root = "/Users/acebless/Documents/The Company/Company Brain"
    venture_reg_path = os.path.join(root, "_REGISTRIES/CANONICAL/VENTURE_REGISTRY.yaml")
    repos_path = os.path.join(root, "_REGISTRIES/CANONICAL/repositories-by-sector.yaml")
    caps_path = os.path.join(root, "_REGISTRIES/CANONICAL/external-capabilities-by-sector.yaml")
    sites_path = os.path.join(root, "_REGISTRIES/CANONICAL/SITES_REGISTRY.yaml")
    
    with open(venture_reg_path) as f:
        ventures_data = yaml.safe_load(f)
    
    # Just creating a placeholder structure for now based on types.ts
    portfolio = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "founder": {
            "name": "Ace Bless",
            "bio": "Founder of Worldwidebro",
            "links": []
        },
        "sectors": [],
        "metrics": {
            "totalOpCos": 35,
            "totalVentures": len(ventures_data),
            "totalARR": 0
        },
        "opcos": [],
        "ventures": [],
        "tools": [],
        "capabilitiesCatalog": []
    }
    
    for v_id, v_data in ventures_data.items():
        portfolio["ventures"].append({
            "id": v_id,
            "name": v_data.get("name", "Unknown"),
            "description": v_data.get("description", ""),
            "status": v_data.get("status", "Planned"),
            "sector": v_data.get("sector", "SEC-000")
        })

    # Output to portfolio.public.json
    out_dir = os.path.join(root, "repos/worldwidebro-venture-portal/src/data")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "portfolio.public.json"), "w") as f:
        json.dump(portfolio, f, indent=2)

if __name__ == "__main__":
    main()
