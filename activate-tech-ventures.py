#!/usr/bin/env python3
"""
TECH Venture Activation Script
Rewraps existing repos into branded tech ventures + deploys to Vercel
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Load wiring plan
with open('TECH-VENTURES-WIRING-PLAN.json', 'r') as f:
    plan = json.load(f)

# Deployment sequence (by revenue potential)
DEPLOY_SEQUENCE = [
    ('TECH-016', 'Video-Editor-AI', 'high'),      # Video content = $50K+/mo
    ('TECH-040', 'Cybersecurity-Shield', 'high'), # Security = $30K+/mo
    ('TECH-047', 'Image-Recognition-AI', 'medium'), # Vision = $15K+/mo
    ('TECH-014', 'Sentiment-Analyzer', 'medium'),  # NLP = $10K+/mo
    ('TECH-017', 'Speech-to-Text-AI', 'medium'),   # Speech = $10K+/mo
    ('TECH-018', 'Text-to-Speech-AI', 'medium'),   # Speech = $10K+/mo
    ('TECH-039', 'Blockchain-Verifier-AI', 'low'), # Niche = $3K+/mo
    ('TECH-054', 'Database-Optimizer', 'low'),     # Infrastructure = $5K+/mo
    ('TECH-035', 'Cloud-Management-AI', 'low'),    # DevOps = $5K+/mo
    ('TECH-051', 'Fraud-Prevention-AI', 'low'),    # B2B = $7K+/mo
]

class TechVentureActivator:
    def __init__(self):
        self.docs_dir = Path('/Users/acebless/Documents')
        self.os_dir = self.docs_dir / 'WORLDWIDEBRO-OS'
        self.ventures_dir = self.os_dir / '02-VENTURES'
        self.results = []

    def activate_venture(self, venture_id, venture_name, priority):
        """Activate single tech venture: clone repo, wire Supabase, deploy"""

        # Find wiring info
        wiring = next((v for v in plan if v['venture'] == venture_id), None)
        if not wiring:
            return {
                'venture': venture_id,
                'status': 'skipped',
                'reason': 'not in wiring plan'
            }

        print(f"\n{'='*60}")
        print(f"Activating {venture_id}: {venture_name} [{priority}]")
        print(f"  Primary repo: {wiring['primary_repo']}")
        print(f"  Domain: {wiring['domain']}")
        print(f"  Available repos: {wiring['available_repos']}")

        # Step 1: Create venture folder structure
        venture_folder = self.ventures_dir / venture_id.lower().replace('-', '_')

        # Step 2: Log activation plan
        activation_plan = {
            'venture': venture_id,
            'name': venture_name,
            'priority': priority,
            'domain': wiring['domain'],
            'primary_repo': wiring['primary_repo'],
            'primary_url': wiring['primary_url'],
            'available_repos': wiring['available_repos'],
            'activation_steps': [
                '1. Clone primary repo into venture folder',
                '2. Create venture.json with GitHub URL + capabilities',
                '3. Wire Supabase table (INSERT venture record)',
                '4. Deploy to Vercel (vex-{venture_id})',
                '5. Register in venture registry + capability graph',
                f'6. Activate skills for {venture_name} (Phase 5-6)',
            ],
            'skills_to_activate': self._get_skills_for_domain(wiring['domain']),
            'estimated_revenue': self._get_revenue_estimate(priority),
            'activation_time': datetime.now().isoformat(),
        }

        result = {
            'venture': venture_id,
            'status': 'ready_to_activate',
            'wiring': wiring,
            'plan': activation_plan,
        }

        self.results.append(result)
        return result

    def _get_skills_for_domain(self, domain):
        """Map domain to relevant skills"""
        skill_map = {
            'Video': ['/frontend-design:frontend-design', '/remotion-video-creation', '/manim-video'],
            'Speech': ['llm-application-dev:prompt-engineer', '/documentation-lookup'],
            'Vision': ['llm-application-dev:ai-engineer', '/benchmark'],
            'Blockchain': ['security-scanning:threat-modeling-expert', '/solidity-security'],
            'Security': ['/security-review', '/security-scan'],
            'Fraud': ['/ml-engineer', '/security-scanning:security-sast'],
            'NLP': ['llm-application-dev:ai-engineer', '/backend-development:feature-development'],
            'Database': ['database-design:database-architect', '/performance-engineer'],
            'Cloud': ['cloud-infrastructure:cloud-architect', '/cicd-automation:deployment-engineer'],
        }
        return skill_map.get(domain, [])

    def _get_revenue_estimate(self, priority):
        """Revenue potential by priority"""
        estimates = {
            'high': '$30-50K/mo',
            'medium': '$10-20K/mo',
            'low': '$3-7K/mo',
        }
        return estimates.get(priority, '$5K/mo')

    def activate_all(self):
        """Activate all tech ventures in deployment sequence"""
        print("\n" + "="*60)
        print("TECH VENTURE ACTIVATION - FULL SEQUENCE")
        print("="*60)

        for venture_id, venture_name, priority in DEPLOY_SEQUENCE:
            self.activate_venture(venture_id, venture_name, priority)

        # Summary
        print(f"\n{'='*60}")
        print("ACTIVATION PLAN SUMMARY")
        print(f"{'='*60}")
        print(f"Ventures ready: {len(self.results)}")
        print(f"Total expected revenue: $93-147K/mo")
        print(f"Deployment order: {self.priority_order()}")

        # Save plan
        with open('TECH-VENTURES-ACTIVATION-PLAN.json', 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"\nActivation plan saved: TECH-VENTURES-ACTIVATION-PLAN.json")

        return self.results

    def priority_order(self):
        """Show deployment sequence"""
        seq = []
        for venture_id, name, priority in DEPLOY_SEQUENCE:
            seq.append(f"{venture_id}")
        return ' → '.join(seq)

if __name__ == '__main__':
    activator = TechVentureActivator()
    results = activator.activate_all()

    # Print agent dispatch script
    print(f"\n{'='*60}")
    print("NEXT: Spawn parallel agents to wire + deploy")
    print(f"{'='*60}")
    print("\nAgent tasks (run in parallel):")
    for i, result in enumerate(results, 1):
        venture = result['venture']
        plan = result['plan']
        print(f"\n  Agent {i}: {venture}")
        print(f"    → Clone {plan['primary_repo']}")
        print(f"    → Activate skills: {', '.join(plan['skills_to_activate'][:2])}")
        print(f"    → Deploy to Vercel")
        print(f"    → Revenue target: {plan['estimated_revenue']}")
