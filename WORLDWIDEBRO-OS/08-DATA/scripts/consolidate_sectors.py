import csv
import os
import shutil

DOCS = "/Users/acebless/Documents"
REG = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries"
OPCO_DIR = f"{DOCS}/WORLDWIDEBRO-OS/03-PORTFOLIO/opcos"

# 1. Map sectors in CSV files
def consolidate_csv(file_path):
    print(f"Consolidating sectors in {file_path}...")
    temp_path = file_path + ".tmp"
    with open(file_path, "r", newline="") as infile, open(temp_path, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Sector mappings
            if row["sector"] == "education-training":
                row["sector"] = "education"
            elif row["sector"] == "software-technology":
                row["sector"] = "technology"
            elif row["sector"] in ["clean", "wash"]:
                row["sector"] = "operations"
            writer.writerow(row)
            
    shutil.move(temp_path, file_path)

# Run CSV consolidations
consolidate_csv(f"{REG}/ventures.csv")
consolidate_csv(f"{REG}/VENTURES-CAPABILITIES-MAPPED.csv")

# 2. Re-calculate opco.csv counts based on ventures.csv
print("Recalculating opcos.csv...")
sectors = {}
with open(f"{REG}/ventures.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sec = row["sector"]
        sectors[sec] = sectors.get(sec, 0) + 1

# Write updated opcos.csv
with open(f"{REG}/opcos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["opco_id", "sector_label", "venture_count"])
    for sec, count in sorted(sectors.items()):
        # Format label
        label = sec.replace("-", " ").title()
        if sec == "e-commerce":
            label = "E-Commerce"
        elif sec == "beauty-wellness":
            label = "Beauty-Wellness"
        elif sec == "fitness-sports":
            label = "Fitness-Sports"
        elif sec == "food-hospitality":
            label = "Food-Hospitality"
        elif sec == "logistics-transport":
            label = "Logistics-Transport"
        elif sec == "media-content":
            label = "Media-Content"
        elif sec == "professional-services":
            label = "Professional-Services"
        writer.writerow([sec.upper(), label, count])

# 3. Clean up folder tree duplicates
print("Cleaning up empty duplicate directories...")
empty_folders = [
    "BEAUTY_WELLNESS",
    "REAL_ESTATE",
    "HOSPITALITY",
    "MEDIA",
    "TRANSPORTATION"
]
for folder in empty_folders:
    path = f"{OPCO_DIR}/{folder}"
    if os.path.exists(path):
        try:
            os.rmdir(path)
            print(f"Removed empty directory: {path}")
        except Exception as e:
            print(f"Failed to remove {path}: {e}")

# Merge EDUCATION-TRAINING folder files into EDUCATION
if os.path.exists(f"{OPCO_DIR}/EDUCATION-TRAINING"):
    print("Removing redundant EDUCATION-TRAINING playbook folder...")
    shutil.rmtree(f"{OPCO_DIR}/EDUCATION-TRAINING")

# Merge SOFTWARE-TECHNOLOGY folder files into TECHNOLOGY
if os.path.exists(f"{OPCO_DIR}/SOFTWARE-TECHNOLOGY"):
    print("Removing redundant SOFTWARE-TECHNOLOGY playbook folder...")
    shutil.rmtree(f"{OPCO_DIR}/SOFTWARE-TECHNOLOGY")

# 4. Move loose CON-OS-* files to CONSTRUCTION/docs
print("Moving loose construction runbooks & summaries...")
dest_docs = f"{OPCO_DIR}/CONSTRUCTION/docs"
os.makedirs(dest_docs, exist_ok=True)

for item in os.listdir(DOCS):
    if item.startswith("CON-OS-") and item.endswith(".md"):
        src = f"{DOCS}/{item}"
        dest = f"{dest_docs}/{item}"
        shutil.move(src, dest)
        print(f"Moved {item} -> CONSTRUCTION/docs/")
        
# Move the verification python script
verify_script = "CON-OS-VERIFY-stripe-checkout.py"
if os.path.exists(f"{DOCS}/{verify_script}"):
    shutil.move(f"{DOCS}/{verify_script}", f"{dest_docs}/{verify_script}")
    print(f"Moved {verify_script} -> CONSTRUCTION/docs/")

print("Sector cleanup complete!")
