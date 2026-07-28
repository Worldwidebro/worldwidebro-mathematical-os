#!/usr/bin/env python3
"""GitHub Organization Query & Mapper - unified repos + starred + ventures"""
import json
import subprocess
import csv
from datetime import datetime
from pathlib import Path

class GitHubOrgMapper:
    def __init__(self):
        self.repos = []
        self.starred = []
        self.ventures_ready = [
            'ec-112-cosmic-kitty',
            'con-001-ace-construction',
            'lt-005-medical-courier-dispatch',
            'ops-staff-001-staffing',
            'ec-001-angels-in-daylight',
            're-001-worldwidebro-holdings'
        ]
        self.missing_os = [
            ('iza-os-real-estate-core', 'RE'),
            ('iza-os-logistics-core', 'LOG'),
            ('iza-os-agriculture-core', 'AG'),
            ('iza-os-growth-core', 'GROWTH'),
            ('iza-os-voice-core', 'VOICE'),
            ('iza-os-radio-core', 'RADIO'),
            ('iza-os-body-core', 'BW'),
            ('iza-os-deal-intelligence', 'DEAL'),
        ]

    def fetch_all_repos(self):
        """Fetch all repos from Worldwidebro"""
        print("📡 Fetching repos...")
        result = subprocess.run(
            ['gh', 'repo', 'list', 'Worldwidebro', '--json',
             'name,diskUsage,pushedAt,url,description,stargazerCount', '--limit', '500'],
            capture_output=True, text=True
        )
        self.repos = json.loads(result.stdout)
        print(f"✓ {len(self.repos)} repos found")

    def fetch_starred_repos(self):
        """Fetch user's starred repos"""
        print("⭐ Fetching starred repos...")
        result = subprocess.run(
            ['gh', 'api', 'user/starred', '--jq', '.[] | {name, url, description}', '--paginate'],
            capture_output=True, text=True
        )
        for line in result.stdout.strip().split('\n'):
            if line.strip():
                try:
                    self.starred.append(json.loads(line))
                except:
                    pass
        print(f"✓ {len(self.starred)} starred repos found")

    def extract_sector(self, name):
        """Extract sector code from repo name"""
        sectors = {
            'con-': 'CON', 'fin-': 'FIN', 'sta-': 'STA', 'edu-': 'EDU',
            're-': 'RE', 'log-': 'LOG', 'ec-': 'EC', 'bw-': 'BW',
            'ag-': 'AG', 'tech-': 'TECH', 'spec-': 'SPEC', 'fh-': 'FH',
            'iza-os-': 'IZA_OS'
        }
        for prefix, sector in sectors.items():
            if name.startswith(prefix):
                return sector
        return 'OTHER'

    def classify_repo(self, name):
        """Classify repo type"""
        if 'iza-os-' in name:
            return 'os_infrastructure'
        elif any(f'{s}-' in name for s in ['con', 'fin', 'sta', 'edu', 're', 'log', 'ec', 'bw', 'ag']):
            return 'venture'
        elif any(x in name for x in ['command', 'site', 'dashboard', 'vex']):
            return 'dashboard'
        return 'other'

    def write_unified_csv(self):
        """Write unified CSV with all repo metadata"""
        filename = '/Users/acebless/Documents/github-org-unified.csv'
        print(f"\n📊 Writing: {filename}")

        rows = []
        for repo in self.repos:
            rows.append({
                'repo_name': repo['name'],
                'github_url': repo['url'],
                'type': self.classify_repo(repo['name']),
                'sector': self.extract_sector(repo['name']),
                'disk_mb': repo['diskUsage'],
                'last_pushed': repo['pushedAt'][:10] if repo['pushedAt'] else 'never',
                'stars': repo.get('stargazerCount', 0),
                'status': 'REVENUE_READY' if repo['name'] in self.ventures_ready else ('EMPTY' if repo['diskUsage'] < 5 else 'ACTIVE'),
                'notes': 'Ready for launch' if repo['name'] in self.ventures_ready else ''
            })

        with open(filename, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'repo_name', 'github_url', 'type', 'sector', 'disk_mb', 'last_pushed', 'stars', 'status', 'notes'
            ])
            writer.writeheader()
            for row in sorted(rows, key=lambda x: x['disk_mb'], reverse=True):
                writer.writerow(row)

        print(f"✓ {len(rows)} repos exported")
        return filename

    def write_missing_os_csv(self):
        """Write CSV of missing OS repos with candidates"""
        filename = '/Users/acebless/Documents/missing-os-implementation.csv'
        print(f"📋 Writing: {filename}")

        rows = []
        candidates = {
            'iza-os-voice-core': 'callitwhatyouwant',
            'iza-os-body-core': None,
            'iza-os-real-estate-core': None,
            'iza-os-logistics-core': None,
        }

        for os_name, sector in self.missing_os:
            rows.append({
                'planned_os_name': os_name,
                'sector': sector,
                'status': 'NOT_CREATED',
                'candidate_empty_repo': candidates.get(os_name, ''),
                'action': 'Create new repo or repurpose empty repo',
                'clickup_ticket': 'TBD'
            })

        with open(filename, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'planned_os_name', 'sector', 'status', 'candidate_empty_repo', 'action', 'clickup_ticket'
            ])
            writer.writeheader()
            writer.writerows(rows)

        print(f"✓ {len(rows)} missing OS repos listed")
        return filename

    def write_starred_matches(self):
        """Identify which starred repos match venture tech stacks"""
        filename = '/Users/acebless/Documents/starred-repos-venture-matches.csv'
        print(f"⭐ Writing: {filename}")

        matches = []
        venture_keywords = {
            'ec-112': ['medusa', 'ecommerce', 'storefront'],
            'con-001': ['construction', 'contract', 'payment'],
            'lt-005': ['dispatch', 'logistics', 'route'],
            'ec-001': ['ecommerce', 'medusa', 'storefront'],
        }

        for star in self.starred:
            url = star.get('url', '')
            if 'Worldwidebro' not in url:  # External repos only
                desc = (star.get('description') or '').lower()
                for venture_id, keywords in venture_keywords.items():
                    if any(kw in desc for kw in keywords):
                        matches.append({
                            'starred_repo_url': url,
                            'repo_name': star.get('name', ''),
                            'venture_id': venture_id,
                            'description': star.get('description', '')[:80],
                            'relevance': 'high'
                        })

        with open(filename, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'starred_repo_url', 'repo_name', 'venture_id', 'description', 'relevance'
            ])
            writer.writeheader()
            writer.writerows(matches)

        print(f"✓ {len(matches)} starred repo matches found")
        return filename

    def write_clickup_tasks(self):
        """Generate ClickUp task JSON for missing work"""
        filename = '/Users/acebless/Documents/clickup-tasks-github-mapping.json'
        print(f"✅ Writing: {filename}")

        tasks = []

        # Task 1: Implement missing OS repos
        for os_name, sector in self.missing_os:
            tasks.append({
                'title': f'Create {os_name}',
                'description': f'Implement {sector} sector OS at {os_name}',
                'type': 'os_implementation',
                'sector': sector,
                'priority': 'high',
                'due_date': (datetime.now().replace(day=1).replace(month=datetime.now().month+1)).isoformat() if datetime.now().month < 12 else datetime.now().replace(year=datetime.now().year+1, month=1).isoformat(),
            })

        # Task 2: Validate revenue-ready ventures
        for venture in self.ventures_ready:
            tasks.append({
                'title': f'Deploy {venture}',
                'description': f'Test and deploy {venture} to production',
                'type': 'venture_deployment',
                'venture_id': venture,
                'priority': 'critical',
                'due_date': '2026-08-02',
            })

        # Task 3: Populate empty repos
        for repo in self.repos:
            if repo['diskUsage'] < 5 and 'iza-os-' in repo['name']:
                tasks.append({
                    'title': f'Populate {repo["name"]}',
                    'description': f'Add code/documentation to {repo["name"]}',
                    'type': 'repo_population',
                    'repo_name': repo['name'],
                    'priority': 'medium',
                })

        with open(filename, 'w') as f:
            json.dump({'tasks': tasks, 'generated': datetime.now().isoformat()}, f, indent=2)

        print(f"✓ {len(tasks)} ClickUp tasks generated")
        return filename

    def run(self):
        """Execute full pipeline"""
        print("\n" + "="*70)
        print("GitHub Organization Query & Mapping")
        print("="*70)

        self.fetch_all_repos()
        self.fetch_starred_repos()

        files = [
            self.write_unified_csv(),
            self.write_missing_os_csv(),
            self.write_starred_matches(),
            self.write_clickup_tasks(),
        ]

        print("\n" + "="*70)
        print("SUMMARY")
        print("="*70)
        print(f"✓ Ready to revenue: {len([r for r in self.repos if r['name'] in self.ventures_ready])} ventures")
        for v in self.ventures_ready:
            for r in self.repos:
                if r['name'] == v:
                    print(f"  - {v}: {r['diskUsage']}MB, pushed {r['pushedAt'][:10]}")
        print(f"\n✓ Missing OS: {len(self.missing_os)} to create")
        print(f"✓ Empty repos: {len([r for r in self.repos if r['diskUsage'] < 5])}")
        print(f"✓ Starred repos: {len(self.starred)}")
        print(f"\n📁 Output files:")
        for f in files:
            print(f"  - {f}")

if __name__ == '__main__':
    mapper = GitHubOrgMapper()
    mapper.run()
