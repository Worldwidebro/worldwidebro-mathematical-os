#!/usr/bin/env python3
"""Generate per-venture operating packs from registries.

Outputs per active venture:
- VENTURE.md
- docs/CAPABILITY-STATEMENT.md
- docs/SALES-SCRIPTS.md
- docs/FORMATION-CREDENTIAL-TRACKER.md
- docs/REPOSITORY-MANIFEST.md
"""
import csv
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Users/acebless/Documents/WORLDWIDEBRO-OS')
REG = ROOT / '08-DATA' / 'registries'
ACTIVE = ROOT / '03-PORTFOLIO' / 'ventures' / 'active'


def load_csv(name):
    p = REG / name
    if not p.exists():
        return []
    with p.open('r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


ventures = load_csv('ventures.csv')
vcaps = load_csv('venture_capability_map.csv')
vrepos = load_csv('venture_repo_map.csv')
opcos = {r['opco_id']: r['sector_label'] for r in load_csv('opcos.csv')}

ventures_by_id = {v['venture_id']: v for v in ventures}

# indices
caps_by_venture = defaultdict(list)
for row in vcaps:
    vid = row.get('venture_id')
    cap = row.get('capability')
    if vid and cap:
        caps_by_venture[vid].append(cap)

repos_by_venture = defaultdict(list)
for row in vrepos:
    vid = row.get('venture_id')
    repo = row.get('repo_name')
    if vid and repo:
        repos_by_venture[vid].append(repo)

# Load existing venture.json where present
def load_venture_json(vpath: Path):
    p = vpath / 'VENTURE.json'
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return {}


for vid, meta in ventures_by_id.items():
    slug = vid.split('-', 1)[1] if '-' in vid else vid
    vdir = ACTIVE / slug
    vdir.mkdir(parents=True, exist_ok=True)
    docs = vdir / 'docs'
    docs.mkdir(exist_ok=True)

    vj = load_venture_json(vdir)
    name = vj.get('business_name') or meta.get('name', slug)
    sector = vj.get('sector') or meta.get('sector', '')
    opco = vj.get('opco') or meta.get('opco', '')
    stage = vj.get('development_stage') or meta.get('stage', '')
    status = vj.get('status') or meta.get('status', '')
    entity_name = (((vj.get('entity') or {}).get('name')) or 'TBD')
    entity_type = (((vj.get('entity') or {}).get('type')) or 'LLC')
    entity_state = (((vj.get('entity') or {}).get('state')) or 'TBD')
    formation_status = (((vj.get('entity') or {}).get('status')) or 'pending_formation')
    first_action = (((vj.get('first_dollar') or {}).get('action')) or '')
    price = (vj.get('first_dollar') or {}).get('price', '')
    platform = (((vj.get('first_dollar') or {}).get('platform')) or '')
    days = (((vj.get('first_dollar') or {}).get('days_to_revenue')) or '')
    monthly_target = (((vj.get('revenue') or {}).get('monthly_target')) or '')
    revenue_model = (((vj.get('revenue') or {}).get('model')) or '')
    icp_title = (((vj.get('icp') or {}).get('title')) or '')
    icp_pain = (((vj.get('icp') or {}).get('pain_point')) or '')
    icp_platform = (((vj.get('icp') or {}).get('platform')) or '')
    opening_line = (((vj.get('icp') or {}).get('opening_line')) or '')

    caps = sorted(set(caps_by_venture.get(vid, [])))
    repos = sorted(set(repos_by_venture.get(vid, [])))

    venture_md = f"""# {name}

| Field | Value |
|-------|-------|
| Venture ID | {vid} |
| Sector | {sector} |
| OPCO | {opco} |
| Stage | {stage} |
| Status | {status} |
| Entity | {entity_name} ({entity_type}) |
| State | {entity_state} |
| Formation Status | {formation_status} |
| First Dollar Action | {first_action} |
| First Dollar Price | ${price} |
| First Dollar Platform | {platform} |
| Days to Revenue | {days} |
| Monthly Target | ${monthly_target} |
| Revenue Model | {revenue_model} |

## ICP

- **Title:** {icp_title}
- **Pain Point:** {icp_pain}
- **Platform:** {icp_platform}
- **Opening Line:** {opening_line}

## Repositories

{chr(10).join(['- `' + r + '`' for r in repos]) if repos else '- *(none mapped)*'}

## Capabilities

{chr(10).join(['- `' + c + '`' for c in caps]) if caps else '- *(none mapped)*'}

---
Generated from `08-DATA/registries/*` + `03-PORTFOLIO/ventures/active/{slug}/VENTURE.json`.
"""
    (vdir / 'VENTURE.md').write_text(venture_md, encoding='utf-8')

    caps_md = f"""# Capability Statement — {name}

> Sector: {sector} | OPCO: {opco} | Status: {status}

## Differentiators

- Capability-linked portfolio: {', '.join(caps) if caps else 'TBD'}
- Repository-backed execution: {len(repos)} mapped repo(s)

## What we deliver

- Revenue path: {revenue_model or 'TBD'}
- First dollar: {first_action or 'TBD'}
- Target: ${monthly_target or 'TBD'}/mo

## Trust/credentials

- Entity: {entity_name} ({entity_type}, {entity_state})
- Formation: {formation_status}
"""
    (docs / 'CAPABILITY-STATEMENT.md').write_text(caps_md, encoding='utf-8')

    sales_md = f"""# Sales Scripts — {name}

## Cold open

> {opening_line or 'TBD'}

## qualifying questions

1. What’s your current timeline for {icp_pain or 'this problem'}?
2. Who owns this today?
3. What would faster execution be worth?

## engines

| Engine | Ask | Channel |
|--------|-----|---------|
| A — B2G/sub | Add me to prequalified lists | Bid boards + prime prequal |
| B — retainer | 15 min managing this ongoing | LinkedIn + referrals |
| C — productized | Fixed-price quote | Direct outbound + web offer |
"""
    (docs / 'SALES-SCRIPTS.md').write_text(sales_md, encoding='utf-8')

    formation_md = f"""# Formation & Credential Tracker — {name}

| Item | Status | Notes |
|------|--------|-------|
| Entity Filing | {formation_status} | {entity_type} in {entity_state} |
| EIN | { (((vj.get('entity') or {}).get('ein')) or 'pending') } | |
| Insurance GL | pending | |
| UEI/SAM | pending | Engine A only |
| Diversity Certs | pending | SBA/MBE/WBE as applicable |
| Bank Account | pending | |
| Accounting | pending | { (((vj.get('tax') or {}).get('classification')) or 'TBD') } |
| Tax Year | { (((vj.get('tax') or {}).get('year')) or 'TBD') } | { (((vj.get('tax') or {}).get('return_type')) or '') } |
| Grants | {len(vj.get('grants', []))} identified | { ', '.join([g.get('program','') for g in vj.get('grants', [])[:3]]) } |
"""
    (docs / 'FORMATION-CREDENTIAL-TRACKER.md').write_text(formation_md, encoding='utf-8')

    repo_md = f"""# Repository Manifest — {name}

## Mapped repositories

{chr(10).join(['- `' + r + '`' for r in repos]) if repos else '- *(none mapped)*'}

## Source records

- `08-DATA/registries/venture_repo_map.csv`
- `08-DATA/registries/venture_capability_map.csv`
- `REGISTRIES/repository_registry_pilot.json`

## Notes

Use this manifest to assign repos to venture workstreams, owner agents, and CI/CD clusters.
"""
    (docs / 'REPOSITORY-MANIFEST.md').write_text(repo_md, encoding='utf-8')

print('generated venture packs for', len(ventures_by_id), 'ventures')
