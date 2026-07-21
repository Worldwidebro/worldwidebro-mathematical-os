#!/usr/bin/env python3
"""
Build VENTURE-ASSIGNMENT-REGISTRY.yaml from CSV sources.
Maps 712 ventures to OPCOs with capability requirements and agent assignments.
Executed once to generate routing table for IZA OS.
"""

import csv
import yaml
from pathlib import Path
from collections import defaultdict

# Department taxonomy
DEPARTMENTS = {
    'finance': 'fin',
    'technology': 'tech',
    'marketing': 'mktg',
    'operations': 'ops',
    'sales': 'sales',
    'legal': 'legal',
    'hr': 'hr',
    'compliance': 'comp'
}

# Capability to department mapping
CAPABILITY_DEPARTMENTS = {
    'analytics': 'finance',
    'api': 'technology',
    'authentication': 'technology',
    'automation': 'operations',
    'dashboard': 'technology',
    'database': 'technology',
    'payments': 'finance',
    'portfolio': 'finance',
    'security': 'technology',
    'crm': 'sales',
    'agent': 'operations',
    'llm': 'technology',
    'construction': 'operations',
    'notifications': 'marketing',
    'scheduling': 'operations',
}

# Stage to readiness score mapping
STAGE_SCORES = {
    'planned': 15,
    'development': 35,
    'alpha': 50,
    'beta': 65,
    'mvp': 40,
    'validation': 55,
    'growth': 70,
    'active': 75,
    'live': 85,
    'archived': 0
}

# Revenue targets by stage (monthly)
REVENUE_TARGETS = {
    'planned': 0,
    'development': 500,
    'alpha': 1000,
    'beta': 3000,
    'mvp': 2000,
    'validation': 5000,
    'growth': 15000,
    'active': 10000,
    'live': 20000,
    'archived': 0
}

# Growth stage mapping
GROWTH_STAGES = {
    'planned': 'ideation',
    'development': 'development',
    'alpha': 'validation',
    'beta': 'validation',
    'mvp': 'validation',
    'validation': 'validation',
    'growth': 'scale',
    'active': 'scale',
    'live': 'mature',
    'archived': 'archived'
}

def build_required_capabilities(cap_string):
    """Parse capability string into department-organized dict."""
    if not cap_string or cap_string.strip() == '':
        return {}

    capabilities = cap_string.split(';')
    dept_caps = defaultdict(list)

    for cap in capabilities:
        cap = cap.strip().lower()
        if cap:
            dept = CAPABILITY_DEPARTMENTS.get(cap, 'operations')
            dept_caps[dept].append(cap)

    return dict(dept_caps)

def get_assigned_agents(opco_code, departments):
    """Generate agent assignments based on OPCO and departments."""
    agents = {}
    opco_short = opco_code.lower().replace('-', '_')

    for dept in departments:
        if dept in DEPARTMENTS:
            dept_code = DEPARTMENTS[dept]
            agents[dept] = f"{dept_code}_{opco_short}_{dept_code}_001"

    return agents

def map_venture_to_opco(venture_id, opco_mapping):
    """Find OPCO for a venture."""
    for row in opco_mapping:
        if row['venture_id'] == venture_id:
            opco = row['assigned_opco'].lower()
            opco = opco.replace('opco-', '').replace('opco_', '')
            return opco
    # Fallback: derive from venture ID prefix
    prefix = venture_id.split('-')[0]
    return prefix.lower()

def main():
    # Read CSV files
    ventures_file = Path('/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/VENTURES-CAPABILITIES-MAPPED.csv')
    opco_file = Path('/Users/acebless/Documents/WORLDWIDEBRO-OS/02-GOVERNANCE/holdings/_superseded/Worldwidebro-Holdings/OPCO_VENTURE_MAPPING.csv')

    # Load OPCO mapping
    opco_mapping = []
    with open(opco_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        opco_mapping = list(reader)

    print(f"Loaded {len(opco_mapping)} OPCO mappings")

    # Build ventures dict
    ventures = {}
    with open(ventures_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            venture_id = row['venture_id']
            opco = map_venture_to_opco(venture_id, opco_mapping)

            required_caps = build_required_capabilities(row['required_capabilities'])
            stage = row['stage'].lower().strip()

            venture_data = {
                'name': row['name'],
                'opco': opco,
                'sector': row['sector'],
                'stage': stage,
                'status': row['status'].lower(),
                'required_capabilities': required_caps if required_caps else {},
                'assigned_agents': get_assigned_agents(opco, required_caps.keys()) if required_caps else {},
                'launch_date': '2026-01-01',
                'readiness_score': STAGE_SCORES.get(stage, 20),
                'revenue_target_monthly': REVENUE_TARGETS.get(stage, 0),
                'growth_stage': GROWTH_STAGES.get(stage, 'ideation'),
                'capability_coverage': float(row['coverage_pct']) if row['coverage_pct'] else 0
            }

            ventures[venture_id] = venture_data

    # Build final registry structure
    registry = {
        'ventures': ventures,
        'metadata': {
            'total_ventures': len(ventures),
            'last_updated': '2026-07-16',
            'source': 'VENTURES-CAPABILITIES-MAPPED.csv + OPCO_VENTURE_MAPPING.csv',
            'description': 'Complete venture assignment registry mapping all ventures to OPCOs with capability requirements and agent routing'
        }
    }

    # Write YAML with custom representer for dicts to maintain order
    output_file = Path('/Users/acebless/Documents/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/ventures/VENTURE-ASSIGNMENT-REGISTRY.yaml')
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(registry, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"✓ Registry built: {output_file}")
    print(f"✓ Total ventures: {len(ventures)}")
    print(f"✓ File size: {output_file.stat().st_size:,} bytes")

    # Print sample
    print("\nSample entries (first 3 ventures):")
    for i, (vid, data) in enumerate(list(ventures.items())[:3]):
        print(f"\n{vid}:")
        print(f"  name: {data['name']}")
        print(f"  opco: {data['opco']}")
        print(f"  stage: {data['stage']}")
        print(f"  readiness_score: {data['readiness_score']}")

if __name__ == '__main__':
    main()
