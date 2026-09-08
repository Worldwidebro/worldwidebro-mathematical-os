import os

ventures = {
    "CON-001": "Construction & Public Works",
    "LT-011": "Logistics & Fleet Dispatch",
    "LT-005": "Healthcare Cold Chain Transit",
    "OPS-001": "Specialized Staffing Operations",
    "RE-001": "Real Estate Asset Holding"
}

base_dir = "BUSINESS-CAPITAL-DATA-ROOM"

# 1. Update Blueprint with links to the ventures
blueprint_path = "/Users/acebless/.gemini/antigravity/brain/967faccb-83a2-4a79-bb59-5a54ffb7969e/family_enterprise_blueprint.md"
if os.path.exists(blueprint_path):
    with open(blueprint_path, 'a') as f:
        f.write("\n\n## 6. Graph & Wiki Connections\n")
        f.write("This blueprint connects directly to the following operating entities in the knowledge graph:\n")
        for v, taxonomy in ventures.items():
            f.write(f"- [[{v}/BUSINESS-CAPITAL-PROSPECTUS.md|{v} - {taxonomy}]]\n")

# 2. Update each venture prospectus with links to the blueprint and their own 22 domains
for v in ventures.keys():
    prospectus = os.path.join(base_dir, v, "BUSINESS-CAPITAL-PROSPECTUS.md")
    if os.path.exists(prospectus):
        with open(prospectus, 'a') as f:
            f.write("\n\n## 99. Knowledge Graph & Wiki Links\n")
            f.write("- **Enterprise Blueprint:** [[../../../.gemini/antigravity/brain/967faccb-83a2-4a79-bb59-5a54ffb7969e/family_enterprise_blueprint.md|Family Enterprise Architecture Blueprint]]\n")
            f.write("- **Taxonomy Group:** [[Sector Taxonomy]]\n")
            f.write("- **Primary Domains:**\n")
            f.write("  - [[01_IDENTITY/COMPANY-PROFILE.md|Corporate Identity]]\n")
            f.write("  - [[05_FINANCIAL/3-YEAR-PRO-FORMA.md|Financial Pro Forma]]\n")
            f.write("  - [[14_LOANS/LOAN-PACKAGE.md|Commercial Loan Underwriting]]\n")
            f.write("  - [[99_INDEX/CAPITAL-READINESS-SCORECARD.md|Capital Readiness Scorecard]]\n")

print("Wiki links injected.")
