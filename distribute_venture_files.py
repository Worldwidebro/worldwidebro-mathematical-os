#!/usr/bin/env python3
"""
Phase 1-3: Full venture file distribution
Analyzes, structures, and distributes all files to proper ventures
"""
import os
import json
import shutil
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

VENTURE_PATTERN = r'^([A-Z]{2,4})-(\d{3,4}|[A-Z0-9-]+)'
DOCS_EXTS = {'.md', '.txt', '.pdf', '.doc', '.docx'}
SCRIPT_EXTS = {'.py', '.sh', '.js', '.ts', '.go', '.rb', '.php'}
CONFIG_EXTS = {'.json', '.yaml', '.yml', '.toml', '.ini', '.env'}

class VentureDistributor:
    def __init__(self, root_dir, venture_hub_path):
        self.root = root_dir
        self.venture_hub = venture_hub_path
        self.mapping = defaultdict(list)
        self.unmatched = []
        self.audit_log = []
        
    def extract_venture_id(self, filename):
        """Extract venture ID from filename"""
        matches = re.search(VENTURE_PATTERN, filename)
        if matches:
            return f"{matches.group(1)}-{matches.group(2)}"
        return None
    
    def categorize_file(self, filename):
        """Categorize file by type"""
        ext = Path(filename).suffix.lower()
        if ext in DOCS_EXTS:
            return 'documents'
        elif ext in SCRIPT_EXTS:
            return 'scripts'
        elif ext in CONFIG_EXTS:
            return 'config'
        else:
            return 'assets'
    
    def scan_files(self):
        """Scan all files in Documents"""
        print("\n📁 PHASE 1: SCANNING FILES")
        print("="*70)
        print(f"\nScanning {self.root}...\n")
        
        skip_dirs = {'.git', 'node_modules', 'venv', '.venv', '__pycache__', 
                     '.obsidian', '.claude', 'iza-os', 'The office', 'staffing-os',
                     'career-ops', 'autonomous-venture-studio'}
        
        total_files = 0
        for root, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, self.root)
                total_files += 1
                
                venture_id = self.extract_venture_id(file)
                if venture_id:
                    self.mapping[venture_id].append({
                        'file': file,
                        'path': rel_path,
                        'type': self.categorize_file(file)
                    })
                else:
                    self.unmatched.append(rel_path)
        
        print(f"✅ Scanned {total_files} files")
        print(f"   Matched to ventures: {sum(len(v) for v in self.mapping.values())}")
        print(f"   Ventures found: {len(self.mapping)}")
        print(f"   Unmatched: {len(self.unmatched)}")
        
        return len(self.mapping), sum(len(v) for v in self.mapping.values())
    
    def create_structure(self):
        """Phase 2: Create venture-hub directory structure"""
        print("\n📁 PHASE 2: CREATING STRUCTURE")
        print("="*70)
        print(f"\nCreating {len(self.mapping)} venture folders...\n")
        
        for venture_id in sorted(self.mapping.keys()):
            venture_dir = os.path.join(self.venture_hub, venture_id)
            os.makedirs(venture_dir, exist_ok=True)
            os.makedirs(os.path.join(venture_dir, 'documents'), exist_ok=True)
            os.makedirs(os.path.join(venture_dir, 'scripts'), exist_ok=True)
            os.makedirs(os.path.join(venture_dir, 'config'), exist_ok=True)
            os.makedirs(os.path.join(venture_dir, 'assets'), exist_ok=True)
            
            if (venture_id + 1) % 50 == 0 or venture_id in sorted(self.mapping.keys())[-1:]:
                print(f"  Created {venture_id}...")
        
        print(f"\n✅ Created {len(self.mapping)} venture directories")
        print(f"   Location: {self.venture_hub}")
        
        return True
    
    def distribute_files(self):
        """Phase 3: Distribute files to ventures"""
        print("\n📁 PHASE 3: DISTRIBUTING FILES")
        print("="*70)
        print(f"\nMoving files to ventures...\n")
        
        moved = 0
        failed = 0
        
        for venture_id in sorted(self.mapping.keys()):
            venture_dir = os.path.join(self.venture_hub, venture_id)
            
            for file_info in self.mapping[venture_id]:
                src_path = os.path.join(self.root, file_info['path'])
                
                if not os.path.exists(src_path):
                    failed += 1
                    continue
                
                file_type = file_info['type']
                dest_dir = os.path.join(venture_dir, file_type)
                dest_path = os.path.join(dest_dir, file_info['file'])
                
                try:
                    if os.path.exists(src_path):
                        shutil.copy2(src_path, dest_path)
                        moved += 1
                except Exception as e:
                    failed += 1
                    self.audit_log.append(f"FAILED: {venture_id}/{file_info['file']} - {str(e)}")
            
            if (list(sorted(self.mapping.keys())).index(venture_id) + 1) % 100 == 0:
                print(f"  Distributed to {list(sorted(self.mapping.keys())).index(venture_id) + 1} ventures...")
        
        print(f"\n✅ Moved {moved} files")
        print(f"⚠️  Failed: {failed} files")
        
        return moved, failed

def main():
    print("\n" + "="*70)
    print("🚀 FULL VENTURE FILE DISTRIBUTION")
    print("="*70)
    
    root = '/Users/acebless/Documents'
    venture_hub = '/Users/acebless/Documents/venture-hub'
    
    distributor = VentureDistributor(root, venture_hub)
    
    # Phase 1: Scan
    ventures_count, files_count = distributor.scan_files()
    
    # Phase 2: Create structure
    distributor.create_structure()
    
    # Phase 3: Distribute files
    moved, failed = distributor.distribute_files()
    
    # Summary
    print("\n" + "="*70)
    print("✅ DISTRIBUTION COMPLETE")
    print("="*70)
    print(f"""
RESULTS:
  Ventures organized: {ventures_count}
  Files distributed: {moved}
  Failed: {failed}
  
LOCATION:
  {venture_hub}
  
STRUCTURE:
  venture-hub/
    ├─ CON-001/
    │   ├─ documents/  (*.md, *.pdf, etc)
    │   ├─ scripts/    (*.py, *.sh, etc)
    │   ├─ config/     (*.json, *.yaml, etc)
    │   ├─ assets/     (everything else)
    │   └─ README.md   (venture overview)
    │
    └─ ... {ventures_count} total ventures

NEXT STEPS:
  1. Review venture-hub structure
  2. Create README.md per venture (from Supabase)
  3. Sync to GitHub per venture
  4. Update Supabase with venture_hub paths
  5. Archive scattered files
""")
    
    # Save audit log
    audit_file = os.path.join(venture_hub, 'DISTRIBUTION_AUDIT.json')
    with open(audit_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'ventures_organized': ventures_count,
            'files_moved': moved,
            'files_failed': failed,
            'logs': distributor.audit_log[:100]  # First 100 errors
        }, f, indent=2)
    
    print(f"📝 Audit log: {audit_file}")

if __name__ == "__main__":
    main()
