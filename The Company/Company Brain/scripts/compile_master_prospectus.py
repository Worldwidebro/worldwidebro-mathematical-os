import os

ventures = ["CON-001", "LT-011", "LT-005", "OPS-001", "RE-001"]
base_dir = "BUSINESS-CAPITAL-DATA-ROOM"

for v in ventures:
    v_dir = os.path.join(base_dir, v)
    if not os.path.exists(v_dir): continue
    
    out_file = os.path.join(v_dir, "COMPILED-MASTER-PROSPECTUS.md")
    
    with open(out_file, 'w') as out:
        out.write(f"# 🏛️ COMPILED MASTER PROSPECTUS: {v}\n\n")
        out.write("> **Note:** This document automatically compiles the contents of the 22-Domain Venture OS into a single presentation-ready master file.\n\n")
        
        # 1. Grab the main prospectus first
        main_p = os.path.join(v_dir, "BUSINESS-CAPITAL-PROSPECTUS.md")
        if os.path.exists(main_p):
            with open(main_p, 'r') as f:
                out.write(f.read() + "\n\n---\n\n")
        
        # 2. Iterate through folders and grab key markdown files
        for item in sorted(os.listdir(v_dir)):
            item_path = os.path.join(v_dir, item)
            if os.path.isdir(item_path) and item[0].isdigit(): # e.g., 01_IDENTITY
                domain_name = item.split('_', 1)[1].replace('_', ' ')
                out.write(f"## DOMAIN: {item}\n\n")
                
                for file in sorted(os.listdir(item_path)):
                    if file.endswith('.md'):
                        f_path = os.path.join(item_path, file)
                        with open(f_path, 'r') as f:
                            out.write(f"### {file}\n\n")
                            out.write(f.read() + "\n\n")
                out.write("---\n\n")

print("Compiled all master prospectuses.")
