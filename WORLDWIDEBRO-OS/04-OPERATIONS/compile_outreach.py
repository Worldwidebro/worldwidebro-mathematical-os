#!/usr/bin/env python3
"""
compile_outreach.py
Parses venture SALES-SCRIPTS.md files and generates 0-token email/outreach drafts
locally using f-string template replacement.
"""
import os
import re

PORTFOLIO_DIR = "/Users/acebless/Documents/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures"

def parse_markdown_fields(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse YAML frontmatter
    metadata = {}
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        for line in fm_text.split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                metadata[k.strip()] = v.strip().strip('"').strip("'")
                
    # Search for headings and body content
    body = content
    if fm_match:
        body = content[fm_match.end():]
        
    return metadata, body

def compile_outreach_for_venture(dir_path):
    # Find SALES-SCRIPTS.md
    docs_dir = os.path.join(dir_path, "docs")
    if not os.path.exists(docs_dir):
        # Check if v2 layout exists
        docs_dir = os.path.join(dir_path, "05_SALES")
        if not os.path.exists(docs_dir):
            return
            
    sales_file = None
    for f in os.listdir(docs_dir):
        if "sales-scripts" in f.lower() or "sales_scripts" in f.lower():
            sales_file = os.path.join(docs_dir, f)
            break
            
    if not sales_file:
        return
        
    res = parse_markdown_fields(sales_file)
    if not res:
        return
        
    metadata, body = res
    v_id = metadata.get("venture_id", "TBD")
    dept = metadata.get("department", "Sales & Billing")
    
    # Standard f-string template matching
    # Replaces placeholders like [Customer Name], [Pricing], [Legal Name]
    email_draft = f"""Subject: Scalable Partnership Inquiries — {dir_path.split('/')[-1]}

Hello [Prospect Name],

My name is [My Name] representing Winners Circle WC LLC. I am reaching out regarding our automated service portfolio under {v_id}. 

We provide productized integrations and support systems specifically tailored for the {dept} department. Below is an outline of our pricing and structure:

{body.strip()[:1000]}... (Extracted from local script templates)

If you are open to reviewing a custom presentation deck or scheduling a brief alignment call, please reply to this email.

Best regards,
Operations Lead
Winners Circle WC LLC
"""
    
    # Write outreach package locally (0 tokens)
    outpath = os.path.join(docs_dir, "OUTREACH-PACKAGE.txt")
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(email_draft)
    print(f"✅ Compiled Zero-Token outreach package for {v_id} -> {outpath}")

def main():
    print("🚀 Starting local Zero-Token outreach compiler...")
    # Walk active and proposed ventures
    for folder in ['active', 'proposed']:
        sub_dir = os.path.join(PORTFOLIO_DIR, folder)
        if not os.path.exists(sub_dir):
            continue
        for v_dir in os.listdir(sub_dir):
            full_path = os.path.join(sub_dir, v_dir)
            if os.path.isdir(full_path):
                compile_outreach_for_venture(full_path)

if __name__ == "__main__":
    main()
