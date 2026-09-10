#!/usr/bin/env python3
"""Ingest CAPABILITY-REGISTRY-ENTRIES.yaml into Supabase"""

import yaml
import sys
from pathlib import Path
from datetime import datetime

class CapabilityIngester:
    def __init__(self):
        self.registry_file = Path(__file__).parent.parent / "CAPABILITY-REGISTRY-ENTRIES.yaml"
        self.entries = []
        self.errors = []
    
    def load_yaml(self):
        """Load YAML file (handles multiple documents)"""
        with open(self.registry_file) as f:
            docs = list(yaml.safe_load_all(f))
        
        # Extract capabilities from all documents
        for doc in docs:
            if doc is None:
                continue
            if isinstance(doc, dict) and 'capabilities' in doc:
                self.entries.extend(doc['capabilities'])
            elif isinstance(doc, list):
                self.entries.extend(doc)
            elif isinstance(doc, dict):
                self.entries.append(doc)
        
        print(f"✅ Loaded {len(self.entries)} capabilities from YAML")
    
    def validate_entry(self, entry):
        """Validate capability entry"""
        required = ['id', 'ref_id', 'name', 'description', 'category', 'source', 'healthroute_fit']
        
        missing = [f for f in required if f not in entry]
        if missing:
            self.errors.append(f"Entry: Missing {missing}")
            return False
        
        fit = entry.get('healthroute_fit', 0)
        if not (0 <= fit <= 100):
            self.errors.append(f"Entry {entry.get('id')}: Invalid fit score")
            return False
        
        return True
    
    def dry_run(self):
        """Validate entries"""
        print("\n=== CAPABILITY REGISTRY INGESTION ===\n")
        
        valid = 0
        for entry in self.entries:
            if not self.validate_entry(entry):
                continue
            
            valid += 1
            fit = entry.get('healthroute_fit', 0)
            print(f"✅ {entry['ref_id']}: {entry['name']}")
            print(f"   Fit: {fit}% | Source: {entry.get('source')}")
            print()
        
        if self.errors:
            print("⚠️  ERRORS:")
            for err in self.errors:
                print(f"   - {err}")
        
        print(f"📊 RESULT: {valid}/{len(self.entries)} entries ready for Supabase\n")
        return len(self.errors) == 0
    
    def generate_sql(self, output_file):
        """Generate SQL INSERT file"""
        with open(output_file, 'w') as f:
            f.write("-- Capability Registry Insert\n")
            f.write(f"-- Generated: {datetime.now().isoformat()}\n\n")
            f.write("BEGIN;\n\n")
            
            count = 0
            for entry in self.entries:
                if not self.validate_entry(entry):
                    continue
                
                count += 1
                id_v = entry.get('id', '').replace("'", "''")
                ref_v = entry.get('ref_id', '').replace("'", "''")
                slug_v = entry.get('slug', '').replace("'", "''")
                name_v = entry.get('name', '').replace("'", "''")
                desc_v = entry.get('description', '').replace("'", "''")
                cat_v = entry.get('category', '').replace("'", "''")
                src_v = entry.get('source', '').replace("'", "''")
                fit_v = entry.get('healthroute_fit', 0)
                use_v = entry.get('healthroute_use_case', '').replace("'", "''")
                gap_v = entry.get('healthroute_gap', '').replace("'", "''")
                
                sql = (f"INSERT INTO capabilities (id, ref_id, slug, name, description, category, source, "
                       f"healthroute_fit, healthroute_use_case, healthroute_gap, owner, approval_status, "
                       f"access_control, version, created_at, updated_at) "
                       f"VALUES ('{id_v}', '{ref_v}', '{slug_v}', '{name_v}', '{desc_v}', '{cat_v}', '{src_v}', "
                       f"{fit_v}, '{use_v}', '{gap_v}', 'System', 'approved', 'public', '1.0', NOW(), NOW());\n")
                f.write(sql)
            
            f.write(f"\nCOMMIT;\n-- Inserted {count} capabilities\n")
        
        print(f"✅ Generated: {output_file} ({count} entries)")

ingester = CapabilityIngester()
ingester.load_yaml()

if '--sql' in sys.argv:
    ingester.dry_run()
    ingester.generate_sql('insert_capabilities.sql')
else:
    ingester.dry_run()
