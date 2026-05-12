#!/usr/bin/env python3
"""Import contacts from CSV to OpenVolo SQLite database"""

import sqlite3
import csv
import json
import uuid
import time
from pathlib import Path

# OpenVolo database path
DB_PATH = Path.home() / ".openvolo" / "data.db"
CSV_PATH = Path.home() / "Documents" / "contacts-extracted.csv"

def import_contacts():
    """Bulk import contacts from CSV to OpenVolo database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    imported = 0
    skipped = 0
    errors = []

    with open(CSV_PATH, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                # Generate unique ID for contact
                contact_id = str(uuid.uuid4())

                # Map CSV fields to database fields
                name = row.get('name', '').strip()
                if not name:
                    skipped += 1
                    continue

                phone = row.get('phone', '').strip() or None
                email = row.get('email', '').strip() or None
                company = row.get('company', '').strip() or None
                location = row.get('location', '').strip() or None
                industry = row.get('industry_guess', '').strip() or 'unknown'
                warmth_score = int(row.get('warmth_score', 5))

                # Split name into first/last
                name_parts = name.split(maxsplit=1)
                first_name = name_parts[0] if name_parts else None
                last_name = name_parts[1] if len(name_parts) > 1 else None

                # Build metadata with original data
                metadata = {
                    'industry': industry,
                    'warmth_score': warmth_score,
                    'import_source': 'contacts_extracted_csv',
                    'original_row': row
                }

                # Build tags array
                tags = []
                if industry != 'unknown':
                    tags.append(industry)
                if warmth_score >= 7:
                    tags.append('hot_lead')
                elif warmth_score >= 5:
                    tags.append('warm_lead')
                else:
                    tags.append('cold_lead')

                # Determine funnel stage based on warmth
                if warmth_score >= 7:
                    funnel_stage = 'prospect'
                elif warmth_score >= 5:
                    funnel_stage = 'prospect'
                else:
                    funnel_stage = 'lead'

                # Get current timestamp
                now = int(time.time())

                # Insert into contacts table
                cursor.execute('''
                    INSERT INTO contacts (
                        id, name, first_name, last_name, company, email, phone,
                        location, score, enrichment_score, funnel_stage,
                        tags, metadata, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    contact_id,
                    name,
                    first_name,
                    last_name,
                    company,
                    email,
                    phone,
                    location,
                    warmth_score,
                    0,
                    funnel_stage,
                    json.dumps(tags),
                    json.dumps(metadata),
                    now,
                    now
                ))

                imported += 1
                print(f"✓ Imported: {name} (warmth: {warmth_score})")

            except Exception as e:
                skipped += 1
                error_msg = f"Error importing {row.get('name', 'Unknown')}: {str(e)}"
                errors.append(error_msg)
                print(f"✗ {error_msg}")

    # Commit and close
    conn.commit()
    conn.close()

    # Print summary
    print("\n" + "="*60)
    print(f"IMPORT COMPLETE")
    print(f"  Imported: {imported}")
    print(f"  Skipped: {skipped}")
    if errors:
        print(f"  Errors: {len(errors)}")
        for err in errors[:5]:
            print(f"    - {err}")
    print("="*60)

    return imported, skipped, errors

if __name__ == '__main__':
    print(f"Importing contacts from: {CSV_PATH}")
    print(f"Target database: {DB_PATH}")
    print()

    imported, skipped, errors = import_contacts()

    if imported > 0:
        print(f"\n✅ Successfully imported {imported} contacts to OpenVolo")
        print("   Contacts are now available at http://localhost:3000/dashboard")
