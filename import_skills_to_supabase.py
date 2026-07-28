#!/usr/bin/env python3
"""
Import skills from YAML registry to Supabase skill_taxonomy table.
Maps YAML structure to schema fields.
"""

import yaml
import os
from supabase import create_client

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Category → skill_phase mapping (14 phases per roadmap)
CATEGORY_PHASE = {
    "UI/UX Testing": 7,  # Testing & Verification
    "Debugging": 7,
    "Frontend Guidelines": 5,  # Specification & Design
    "Knowledge Management": 12,  # Operations & Maintenance
    "Backend & DB": 6,  # Core Implementation
    "AI Scaffolding": 6,
    "AI Orchestration": 6,
    "Documentation": 9,
}

def load_skills_yaml(filepath: str) -> list:
    """Load skills from YAML file."""
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    return data.get('skills', [])

def transform_skill(skill: dict) -> dict:
    """Transform YAML skill to schema fields."""
    category = skill.get('category', 'Other')

    return {
        'skill_id': skill['id'],
        'skill_name': skill['name'],
        'skill_phase': CATEGORY_PHASE.get(category, 6),
        'description': skill.get('description', ''),
        'category': category,
        'use_cases': [],
        'similar_skills': [],
        'requires_user_interaction': False,
        'supports_parallel_execution': True,
        'estimated_duration_minutes': None,
    }

def import_skills_to_supabase(skills: list) -> None:
    """Insert skills into Supabase skill_taxonomy table."""
    if not SUPABASE_KEY:
        raise ValueError("SUPABASE_KEY environment variable not set")

    client = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Transform all skills
    transformed = [transform_skill(s) for s in skills]

    # Insert in batches
    batch_size = 100
    for i in range(0, len(transformed), batch_size):
        batch = transformed[i:i+batch_size]
        response = client.table('skill_taxonomy').upsert(batch).execute()
        print(f"✓ Imported {len(batch)} skills (batch {i//batch_size + 1})")

    print(f"✅ Total: {len(transformed)} skills imported to skill_taxonomy")

if __name__ == '__main__':
    yaml_path = '/Users/acebless/Documents/Gemini/registry/skills.yaml'

    if not os.path.exists(yaml_path):
        print(f"❌ File not found: {yaml_path}")
        exit(1)

    print(f"📖 Reading skills from {yaml_path}...")
    skills = load_skills_yaml(yaml_path)
    print(f"📊 Loaded {len(skills)} skills")

    print("\nTransformed skills preview:")
    for skill in skills[:3]:
        transformed = transform_skill(skill)
        print(f"  • {transformed['skill_id']} → phase {transformed['skill_phase']}")

    print("\n📤 Importing to Supabase...")
    import_skills_to_supabase(skills)
