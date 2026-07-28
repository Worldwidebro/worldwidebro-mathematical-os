import os

# Define the root path for the GC OS structure
ROOT_DIR = "/Users/acebless/Documents/Gemini/AI-BOSS-OS/ventures/con-001-ace-construction"

# Define the folder structure and descriptive README titles
FOLDER_STRUCTURE = {
    "00_COMPANY_OS": [
        "Mission",
        "Strategy",
        "SOPs",
        "Policies",
        "Org Chart",
        "Decision Logs"
    ],
    "01_CORPORATE": [
        "Formation Documents",
        "Licenses",
        "Insurance",
        "Tax Documents",
        "Banking",
        "Certifications"
    ],
    "02_PEOPLE": [
        "Employees",
        "Subcontractors",
        "Vendors",
        "Clients",
        "Partners",
        "Contacts Database"
    ],
    "03_BUSINESS_DEVELOPMENT": [
        "Leads",
        "Opportunities",
        "Client Relationships",
        "Marketing",
        "Proposals",
        "Sales Pipeline"
    ],
    "04_ESTIMATING": [
        "Templates",
        "Cost Database",
        "Historical Bids",
        "Takeoffs",
        "Estimates",
        "Bid Reviews"
    ],
    "05_PROJECTS": [
        "TEMPLATE_PROJECT/01_CONTRACT",
        "TEMPLATE_PROJECT/02_PLANS_DRAWINGS",
        "TEMPLATE_PROJECT/03_PERMITS",
        "TEMPLATE_PROJECT/04_SUBCONTRACTORS",
        "TEMPLATE_PROJECT/05_SCHEDULE",
        "TEMPLATE_PROJECT/06_BUDGET",
        "TEMPLATE_PROJECT/07_CHANGE_ORDERS",
        "TEMPLATE_PROJECT/08_RFIs",
        "TEMPLATE_PROJECT/09_MEETINGS",
        "TEMPLATE_PROJECT/10_PROGRESS_REPORTS",
        "TEMPLATE_PROJECT/11_PHOTOS",
        "TEMPLATE_PROJECT/12_SAFETY",
        "TEMPLATE_PROJECT/13_INSPECTIONS",
        "TEMPLATE_PROJECT/14_PAYMENTS",
        "TEMPLATE_PROJECT/15_CLOSEOUT"
    ],
    "06_OPERATIONS": [
        "Scheduling",
        "Procurement",
        "Quality Control",
        "Safety",
        "Field Operations"
    ],
    "07_FINANCE": [
        "Accounting",
        "Accounts Payable",
        "Accounts Receivable",
        "Payroll",
        "Budgets",
        "Financial Reports"
    ],
    "08_LEGAL": [
        "Contracts",
        "Claims",
        "Disputes",
        "Compliance"
    ],
    "09_TECHNOLOGY": [
        "Software",
        "Integrations",
        "Data",
        "AI Agents",
        "Automation"
    ],
    "10_KNOWLEDGE_BASE": [
        "Lessons Learned",
        "Best Practices",
        "Templates",
        "Pricing Intelligence",
        "Training"
    ]
}

def create_structure():
    print(f"Initializing GC OS folder structure in: {ROOT_DIR}")
    
    for main_folder, sub_folders in FOLDER_STRUCTURE.items():
        main_path = os.path.join(ROOT_DIR, main_folder)
        os.makedirs(main_path, exist_ok=True)
        
        # Write a README.md for the main category
        main_readme_path = os.path.join(main_path, "README.md")
        with open(main_readme_path, "w") as f:
            f.write(f"# {main_folder.replace('_', ' ')}\n\nThis directory manages the core operations for {main_folder.replace('_', ' ').split(' ', 1)[1]}.\n")
        
        for sub_folder in sub_folders:
            sub_path = os.path.join(main_path, sub_folder)
            os.makedirs(sub_path, exist_ok=True)
            
            # Write a specific placeholder README for the subfolder
            sub_readme_path = os.path.join(sub_path, "README.md")
            with open(sub_readme_path, "w") as f:
                name = os.path.basename(sub_folder)
                f.write(f"# {name}\n\nOperating documentation and file store for: {name}.\n")
                
    print("✓ Successfully initialized all folders and templates!")

if __name__ == "__main__":
    create_structure()
