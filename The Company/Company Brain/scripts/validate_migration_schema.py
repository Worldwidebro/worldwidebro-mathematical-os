#!/usr/bin/env python3
"""
Validate Supabase migrations against CAPABILITY-REGISTRY-SCHEMA.yaml

Usage:
  python3 validate_migration_schema.py
"""

import re
import yaml
from pathlib import Path

# Paths
MIGRATIONS_DIR = Path(__file__).parent.parent / "_INFRASTRUCTURE" / "migrations"
SCHEMA_FILE = Path(__file__).parent.parent / "CAPABILITY-REGISTRY-SCHEMA.yaml"

def parse_sql_table(sql_file):
    """Extract table schema from SQL file"""
    with open(sql_file) as f:
        content = f.read()
    
    # Find CREATE TABLE statement
    match = re.search(r'CREATE TABLE.*?(\w+)\s*\((.*?)\);', content, re.DOTALL)
    if not match:
        return None
    
    table_name = match.group(1)
    columns_text = match.group(2)
    
    # Extract column names
    columns = {}
    for line in columns_text.split(','):
        line = line.strip()
        if line and not line.startswith('CONSTRAINT') and not line.startswith('--'):
            parts = line.split()
            if parts:
                col_name = parts[0]
                col_type = ' '.join(parts[1:]) if len(parts) > 1 else 'UNKNOWN'
                columns[col_name] = col_type
    
    return {'table': table_name, 'columns': columns}

def load_schema_yaml():
    """Load CAPABILITY-REGISTRY-SCHEMA.yaml"""
    with open(SCHEMA_FILE) as f:
        return yaml.safe_load(f)

# Validate
print("=== SCHEMA VALIDATION ===\n")

# Check capabilities table
print("1. Validating capabilities table...")
migration_002 = parse_sql_table(MIGRATIONS_DIR / "002_create_capabilities_table.sql")
if migration_002:
    print(f"   ✅ Table: {migration_002['table']}")
    print(f"   ✅ Columns: {len(migration_002['columns'])}")
    
    # Check required columns
    required = ['id', 'ref_id', 'name', 'description', 'category', 'healthroute_fit']
    missing = [c for c in required if c not in migration_002['columns']]
    if missing:
        print(f"   ❌ Missing columns: {missing}")
    else:
        print(f"   ✅ All required columns present")
else:
    print("   ❌ Failed to parse migration")

# Check executions table
print("\n2. Validating capability_executions table...")
migration_003 = parse_sql_table(MIGRATIONS_DIR / "003_create_capability_executions_table.sql")
if migration_003:
    print(f"   ✅ Table: {migration_003['table']}")
    print(f"   ✅ Columns: {len(migration_003['columns'])}")
    
    required = ['id', 'capability_id', 'inputs', 'output', 'status', 'cost_usd', 'latency_ms']
    missing = [c for c in required if c not in migration_003['columns']]
    if missing:
        print(f"   ❌ Missing columns: {missing}")
    else:
        print(f"   ✅ All required columns present")
else:
    print("   ❌ Failed to parse migration")

# Check pauses table
print("\n3. Validating workflow_pauses table...")
migration_004 = parse_sql_table(MIGRATIONS_DIR / "004_create_workflow_pauses_table.sql")
if migration_004:
    print(f"   ✅ Table: {migration_004['table']}")
    print(f"   ✅ Columns: {len(migration_004['columns'])}")
else:
    print("   ❌ Failed to parse migration")

# Check workflows table
print("\n4. Validating workflows table...")
migration_005 = parse_sql_table(MIGRATIONS_DIR / "005_create_workflows_table.sql")
if migration_005:
    print(f"   ✅ Table: {migration_005['table']}")
    print(f"   ✅ Columns: {len(migration_005['columns'])}")
else:
    print("   ❌ Failed to parse migration")

print("\n=== VALIDATION COMPLETE ===")
print("\nNext steps:")
print("1. Deploy migrations to Supabase: supabase db push")
print("2. Verify tables created: SELECT tablename FROM pg_tables WHERE schemaname='public'")
print("3. Run Unit 8: Data ingestion (YAML → Supabase)")
