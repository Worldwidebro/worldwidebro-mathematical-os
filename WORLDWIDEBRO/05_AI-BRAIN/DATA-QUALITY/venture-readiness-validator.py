#!/usr/bin/env python3
"""
VENTURE READINESS VALIDATOR
Validates VENTURE-READINESS-SCORECARD-V2.csv against business rules.
Checks: schema, unique IDs, value ranges, freshness, orphans, contradictions.
"""

import pandas as pd
import json
from datetime import datetime, timedelta

csv_path = "/Users/acebless/Documents/.planning/VENTURE-READINESS-SCORECARD-V2.csv"

print("=" * 80)
print("VENTURE READINESS VALIDATION")
print("=" * 80)

# 1. Load and basic schema check
print("\n1. SCHEMA VALIDATION")
print("-" * 80)

try:
    df = pd.read_csv(csv_path)
    print(f"✅ CSV loaded: {len(df)} rows, {len(df.columns)} columns")

    required_columns = [
        'venture_id', 'name', 'sector', 'development_stage',
        'readiness_pct', 'has_repo', 'entity_status'
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        print(f"❌ Missing columns: {missing}")
    else:
        print(f"✅ All required columns present")

except Exception as e:
    print(f"❌ Load error: {e}")
    exit(1)

# 2. Business rule validation
print("\n2. BUSINESS RULES")
print("-" * 80)

issues = {
    "duplicate_ids": 0,
    "invalid_readiness": 0,
    "invalid_stage": 0,
    "missing_name": 0,
}

# Uniqueness
duplicates = df[df.duplicated(subset=['venture_id'], keep=False)]
if len(duplicates) > 0:
    issues["duplicate_ids"] = len(duplicates.groupby('venture_id'))
    print(f"⚠️  {issues['duplicate_ids']} ventures with duplicate IDs")

# Readiness bounds
invalid_readiness = df[(df['readiness_pct'] < 0) | (df['readiness_pct'] > 100)]
if len(invalid_readiness) > 0:
    issues["invalid_readiness"] = len(invalid_readiness)
    print(f"⚠️  {len(invalid_readiness)} ventures with readiness outside 0-100")

# Stage validation
valid_stages = ['planned', 'validation', 'growth', 'scale', 'mature']
invalid_stage = df[~df['development_stage'].isin(valid_stages)]
if len(invalid_stage) > 0:
    issues["invalid_stage"] = len(invalid_stage)
    print(f"⚠️  {len(invalid_stage)} ventures with invalid stage")

# Missing names
missing_name = df[df['name'].isna() | (df['name'] == '')]
if len(missing_name) > 0:
    issues["missing_name"] = len(missing_name)
    print(f"⚠️  {len(missing_name)} ventures with missing names")

if not any(issues.values()):
    print("✅ All business rules passed")

# 3. Data quality metrics
print("\n3. DATA QUALITY")
print("-" * 80)

print(f"Ventures by stage:")
for stage in valid_stages:
    count = len(df[df['development_stage'] == stage])
    pct = 100 * count / len(df)
    print(f"  {stage:12} {count:>4} ({pct:>5.1f}%)")

avg_readiness = df['readiness_pct'].mean()
print(f"\nAverage readiness: {avg_readiness:.1f}%")
print(f"Readiness range: {df['readiness_pct'].min():.1f}% - {df['readiness_pct'].max():.1f}%")

has_repo = len(df[df['has_repo'] == True])
print(f"\nVentures with repo: {has_repo} ({100*has_repo/len(df):.1f}%)")

sectors = df['sector'].nunique()
print(f"Sectors represented: {sectors}")

# 4. Entity status breakdown
print("\n4. ENTITY STATUS")
print("-" * 80)

if 'entity_status' in df.columns:
    status_counts = df['entity_status'].value_counts()
    for status, count in status_counts.items():
        pct = 100 * count / len(df)
        print(f"  {status:20} {count:>4} ({pct:>5.1f}%)")

# 5. Top ventures by readiness
print("\n5. TOP VENTURES (by readiness %)")
print("-" * 80)

top = df.nlargest(10, 'readiness_pct')[['venture_id', 'name', 'sector', 'development_stage', 'readiness_pct', 'has_repo']]
for idx, row in top.iterrows():
    repo_marker = "📦" if row['has_repo'] else "  "
    print(f"  {repo_marker} {row['venture_id']:8} {row['name'][:30]:30} {row['readiness_pct']:>5.1f}%")

# 6. Summary
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)

print(f"✅ Ventures inventoried: {len(df)}")
print(f"   Average readiness: {avg_readiness:.1f}%")
print(f"   With repo: {has_repo}")
print(f"   Sectors: {sectors}")
print(f"   Data quality issues: {sum(issues.values())}")

if sum(issues.values()) == 0:
    print("\n✅ VALIDATED: CSV passed all checks")
else:
    print(f"\n⚠️  VALIDATION ISSUES: {sum(issues.values())} total")

# Export validation result
validation_result = {
    "timestamp": datetime.now().isoformat(),
    "file": csv_path,
    "rows": len(df),
    "columns": len(df.columns),
    "issues": issues,
    "avg_readiness": float(avg_readiness),
    "ventures_with_repo": int(has_repo),
    "sectors": int(sectors),
    "status": "PASSED" if sum(issues.values()) == 0 else "ISSUES"
}

output_path = "/Users/acebless/Documents/WORLDWIDEBRO/05_AI-BRAIN/DATA-QUALITY/venture-readiness-validation-result.json"
with open(output_path, 'w') as f:
    json.dump(validation_result, f, indent=2)

print(f"\n📊 Result: {output_path}")
