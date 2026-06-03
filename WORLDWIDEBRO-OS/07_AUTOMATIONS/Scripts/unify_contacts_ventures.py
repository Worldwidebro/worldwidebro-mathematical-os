#!/usr/bin/env python3
"""
Unify ventures, repos, and contacts into one master view.
Layer 5: Angels/Investors attached to their ventures
"""

import csv
import json

def main():
    # Load all data
    ventures = {}
    with open('ventures_classification_final.csv') as f:
        for row in csv.DictReader(f):
            ventures[row['venture_id']] = row

    # Load contacts with venture fits
    venture_contacts = {}
    with open('CONTACT-DATA-TEMPLATE.csv') as f:
        for row in csv.DictReader(f):
            for fit_col in ['venture_fit_1', 'venture_fit_2', 'venture_fit_3']:
                venture_key = row.get(fit_col, '').strip()
                if venture_key:
                    if venture_key not in venture_contacts:
                        venture_contacts[venture_key] = []
                    venture_contacts[venture_key].append({
                        'name': row.get('full_name'),
                        'email': row.get('email'),
                        'company': row.get('company_name'),
                        'title': row.get('job_title'),
                        'warmth': row.get('warmth_score'),
                        'location': row.get('location'),
                    })

    # Load auto-alignment results
    with open('AUTO-ALIGNMENT-RESULTS.json') as f:
        alignments = {a['venture_id']: a for a in json.load(f)['alignments']}

    # Create 5-layer unified view: Ventures → Repos → Contacts
    with open('WORLDWIDEBRO-5LAYER-COMPLETE.csv', 'w') as out:
        writer = csv.DictWriter(out, fieldnames=[
            'venture_id', 'venture_name', 'sector', 'tier',
            'repos_matched', 'repo_count',
            'contacts_matched', 'contact_count',
            'top_contact_warmth',
            'angel_investors', 'investor_count'
        ])
        writer.writeheader()

        for venture_id, venture in ventures.items():
            align = alignments.get(venture_id, {})
            repos = align.get('auto_matched_repos', [])
            contacts = venture_contacts.get(venture_id, [])

            # Format repos
            repo_names = [r['name'] for r in repos]
            repo_str = '|'.join(repo_names) if repo_names else ''

            # Format contacts
            contact_names = [c['name'] for c in contacts]
            contact_str = '|'.join(contact_names) if contact_names else ''

            # Get top warmth
            warmths = [float(c['warmth']) for c in contacts if c['warmth']]
            top_warmth = max(warmths) if warmths else 0

            writer.writerow({
                'venture_id': venture_id,
                'venture_name': venture.get('venture_name'),
                'sector': venture.get('sector'),
                'tier': venture.get('tier'),
                'repos_matched': repo_str,
                'repo_count': len(repo_names),
                'contacts_matched': contact_str,
                'contact_count': len(contact_names),
                'top_contact_warmth': top_warmth,
                'angel_investors': contact_str,
                'investor_count': len(contact_names),
            })

    print("✅ Created 5-layer unified view:")
    print("   WORLDWIDEBRO-5LAYER-COMPLETE.csv")
    print(f"   629 ventures + their repos + their contacts/angels")

if __name__ == '__main__':
    main()
