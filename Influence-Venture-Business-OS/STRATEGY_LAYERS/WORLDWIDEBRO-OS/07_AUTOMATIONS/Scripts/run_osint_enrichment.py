#!/usr/bin/env python3
"""
OSINT Enrichment Pipeline for OpenVolo Contacts
Enriches contacts with social media handles, profiles, and engagement data
"""

import sqlite3
import json
import subprocess
import asyncio
from pathlib import Path
from datetime import datetime
import uuid

DB_PATH = Path.home() / ".openvolo" / "data.db"
OSINT_RESULTS_DIR = Path.home() / "Documents" / "osint_results"
OSINT_RESULTS_DIR.mkdir(exist_ok=True)

class OSINTEnricher:
    def __init__(self):
        self.db_path = DB_PATH
        self.results_dir = OSINT_RESULTS_DIR
        self.enriched_count = 0
        self.error_count = 0

    def get_all_contacts(self):
        """Fetch all contacts from OpenVolo database"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contacts ORDER BY created_at DESC')
        contacts = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return contacts

    def update_contact_enrichment(self, contact_id, enrichment_data):
        """Update contact with enrichment data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Parse existing metadata
        existing = cursor.execute(
            'SELECT metadata FROM contacts WHERE id = ?',
            (contact_id,)
        ).fetchone()

        metadata = {}
        if existing and existing[0]:
            try:
                metadata = json.loads(existing[0])
            except:
                pass

        # Merge enrichment data
        metadata['enrichment'] = enrichment_data
        metadata['enriched_at'] = datetime.now().isoformat()

        # Update database
        cursor.execute(
            'UPDATE contacts SET metadata = ?, enrichment_score = enrichment_score + 10 WHERE id = ?',
            (json.dumps(metadata), contact_id)
        )
        conn.commit()
        conn.close()

    def run_sherlock(self, name):
        """Quick username lookup across 300+ sites"""
        print(f"  🔍 Sherlock: searching for '{name}'...")
        try:
            # This is a placeholder - in practice you'd run sherlock CLI
            # For now, return structured empty result
            return {
                'method': 'sherlock',
                'name': name,
                'status': 'ready_for_api',
                'note': 'Sherlock CLI integration pending'
            }
        except Exception as e:
            return {'error': str(e)}

    def run_simple_enrichment(self, contact):
        """Lightweight enrichment using available data"""
        enrichment = {
            'method': 'csv_analysis',
            'original_data': {
                'name': contact['name'],
                'phone': contact['phone'],
                'email': contact['email'],
                'company': contact['company'],
                'location': contact['location'],
            },
            'enrichment_ready': True,
            'next_steps': [
                'Run Sherlock for username search',
                'Run Maigret for deep dossier',
                'LinkedIn profile enrichment',
                'Company tech stack analysis'
            ]
        }

        # Parse metadata for warmth score
        try:
            metadata = json.loads(contact['metadata']) if contact['metadata'] else {}
            warmth = metadata.get('warmth_score', contact['score'])
            enrichment['warmth_score'] = warmth
            enrichment['tier'] = 'hot' if warmth >= 7 else 'warm' if warmth >= 5 else 'cold'
        except:
            pass

        return enrichment

    def enrich_all_contacts(self):
        """Enrich all contacts in batch"""
        contacts = self.get_all_contacts()
        print(f"\n📊 Starting enrichment of {len(contacts)} contacts...")
        print("="*60)

        for i, contact in enumerate(contacts, 1):
            try:
                # Run simple enrichment
                enrichment = self.run_simple_enrichment(contact)

                # Update database
                self.update_contact_enrichment(contact['id'], enrichment)

                # Log result
                tier = enrichment.get('tier', 'unknown')
                status = f"[{tier.upper()}]" if tier != 'unknown' else ""
                print(f"{i:2d}. ✓ {contact['name']:<25} {status} (enriched)")

                self.enriched_count += 1

            except Exception as e:
                print(f"{i:2d}. ✗ {contact['name']:<25} ERROR: {str(e)}")
                self.error_count += 1

        self.print_summary(contacts)

    def print_summary(self, contacts):
        """Print enrichment summary"""
        print("\n" + "="*60)
        print("ENRICHMENT PHASE 1 COMPLETE")
        print(f"  Total contacts: {len(contacts)}")
        print(f"  Enriched: {self.enriched_count}")
        print(f"  Errors: {self.error_count}")
        print("\nNext Phase: Deploy OSINT tools")
        print("  Pending integrations:")
        print("    - Sherlock (username search across 300+ sites)")
        print("    - Maigret (deep dossier from 3000+ sites)")
        print("    - Instagram OSINT (follower count, engagement)")
        print("    - Holehe (email validation)")
        print("    - Web-Check (company tech stack analysis)")
        print("\nEstimated enrichment time: 30-60 minutes parallel")
        print("="*60)

if __name__ == '__main__':
    enricher = OSINTEnricher()
    enricher.enrich_all_contacts()
