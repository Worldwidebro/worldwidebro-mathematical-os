import csv
import os
import shutil

DOCS = "/Users/acebless/Documents"
REG = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries"
OPCO_DIR = f"{DOCS}/WORLDWIDEBRO-OS/03-PORTFOLIO/opcos"

# 1. Mappings to standardize 18 OPCO sectors
sector_mapping = {
    # Redundant/Legacy to canonical mappings
    "education-training": "education",
    "software-technology": "technology",
    "clean": "operations",
    "wash": "operations",
    "community": "operations",
    "emerging": "investment",
    "specialized": "investment",
    "professional-services": "staffing",
    "fitness-sports": "healthcare",
    "logistics-transport": "transportation",
    "media-content": "media",
    "food-hospitality": "hospitality",
    "e-commerce": "marketplace",
    
    # Self-mappings for the canonical 18 to force opco column update
    "agriculture": "agriculture",
    "beauty-wellness": "beauty-wellness",
    "construction": "construction",
    "education": "education",
    "energy": "energy",
    "financial": "financial",
    "healthcare": "healthcare",
    "hospitality": "hospitality",
    "investment": "investment",
    "manufacturing": "manufacturing",
    "marketplace": "marketplace",
    "media": "media",
    "operations": "operations",
    "real-estate": "real-estate",
    "retail": "retail",
    "staffing": "staffing",
    "technology": "technology",
    "transportation": "transportation"
}

# Mapping standardized lowercase sector keys to capitalized OPCO IDs
sector_to_opco_map = {
    "agriculture": "AGRICULTURE",
    "beauty-wellness": "BEAUTY-WELLNESS",
    "construction": "CONSTRUCTION",
    "education": "EDUCATION",
    "energy": "ENERGY",
    "financial": "FINANCIAL",
    "healthcare": "HEALTHCARE",
    "hospitality": "HOSPITALITY",
    "investment": "INVESTMENT",
    "manufacturing": "MANUFACTURING",
    "marketplace": "MARKETPLACE",
    "media": "MEDIA",
    "operations": "OPERATIONS",
    "real-estate": "REAL-ESTATE",
    "retail": "RETAIL",
    "staffing": "STAFFING",
    "technology": "TECHNOLOGY",
    "transportation": "TRANSPORTATION"
}

# The canonical 18 OPCO definitions
canonical_opcos = {
    "AGRICULTURE": "Agriculture",
    "BEAUTY-WELLNESS": "Beauty-Wellness",
    "CONSTRUCTION": "Construction",
    "EDUCATION": "Education",
    "ENERGY": "Energy",
    "FINANCIAL": "Financial",
    "HEALTHCARE": "Healthcare",
    "HOSPITALITY": "Hospitality",
    "INVESTMENT": "Investment",
    "MANUFACTURING": "Manufacturing",
    "MARKETPLACE": "Marketplace",
    "MEDIA": "Media",
    "OPERATIONS": "Operations",
    "REAL-ESTATE": "Real-Estate",
    "RETAIL": "Retail",
    "STAFFING": "Staffing",
    "TECHNOLOGY": "Technology",
    "TRANSPORTATION": "Transportation"
}

def standardize_csv(file_path):
    print(f"Standardizing sectors in {file_path}...")
    temp_path = file_path + ".tmp"
    with open(file_path, "r", newline="") as infile, open(temp_path, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            sec = row["sector"].strip().lower()
            if sec in sector_mapping:
                standardized_sector = sector_mapping[sec]
                row["sector"] = standardized_sector
                # Also update opco column if present
                if "opco" in reader.fieldnames:
                    row["opco"] = sector_to_opco_map[standardized_sector]
            writer.writerow(row)
            
    shutil.move(temp_path, file_path)

# Run CSV updates
standardize_csv(f"{REG}/ventures.csv")
standardize_csv(f"{REG}/VENTURES-CAPABILITIES-MAPPED.csv")

# 2. Recalculate venture counts for the 18 OPCOs
print("Recalculating 18 OPCO venture counts...")
opco_counts = {opco_id: 0 for opco_id in canonical_opcos}

with open(f"{REG}/ventures.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sec = row["sector"].upper()
        if sec in opco_counts:
            opco_counts[sec] += 1
        else:
            print(f"Warning: Unknown sector {sec} in ventures.csv")

# Write complete opcos.csv (the full 18)
with open(f"{REG}/opcos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["opco_id", "sector_label", "venture_count"])
    for opco_id in sorted(canonical_opcos.keys()):
        writer.writerow([opco_id, canonical_opcos[opco_id], opco_counts[opco_id]])

# 3. Clean up non-canonical folders under 03-PORTFOLIO/opcos/
print("Cleaning up old non-canonical folders...")
active_opco_folders = set(canonical_opcos.keys())

for item in os.listdir(OPCO_DIR):
    item_path = f"{OPCO_DIR}/{item}"
    if os.path.isdir(item_path) and item not in active_opco_folders and not item.startswith("."):
        print(f"Removing legacy sector folder: {item}")
        shutil.rmtree(item_path)

# 4. Create empty directory placeholders for the remaining empty OPCOs
for opco_id in canonical_opcos:
    path = f"{OPCO_DIR}/{opco_id}"
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        # Create empty placeholder file to commit
        with open(f"{path}/.gitkeep", "w") as f:
            f.write("")
        print(f"Created placeholder folder: {opco_id}")

print("Full 18 OPCO Standardization complete!")
