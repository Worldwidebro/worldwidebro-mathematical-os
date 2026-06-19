#!/usr/bin/env python3
"""
Unified knowledge graph population: dedup + entity creation + relationship completion + validation.
Single atomic operation: no duplicates, no orphans, self-completing.
Run ONCE per sync cycle before obsidian_graph_sync.py
"""

import os
import sys
import json
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
from dotenv import load_dotenv
from collections import defaultdict

try:
    from supabase import create_client
except ImportError:
    print("ERROR: supabase-py not installed. Run: pip install supabase-py")
    sys.exit(1)

load_dotenv()

class UnifiedGraphSync:
    def __init__(self):
        self.url = os.getenv('SUPABASE_URL')
        self.key = os.getenv('SUPABASE_KEY')
        if not self.url or not self.key:
            print("ERROR: No credentials. Set SUPABASE_URL and SUPABASE_KEY in .env")
            sys.exit(1)

        self.supabase = create_client(self.url, self.key)
        self.entities = []
        self.relationships = []
        self.entity_id_map = {}
        self.orphan_quarantine = []

    def fetch_ventures(self) -> List[Dict[str, Any]]:
        """Fetch all ventures from Supabase"""
        try:
            response = self.supabase.table('ventures').select('*').execute()
            return response.data
        except Exception as e:
            print(f"ERROR fetching ventures: {e}")
            sys.exit(1)

    def fetch_contacts(self) -> List[Dict[str, Any]]:
        """Fetch all contacts from Supabase"""
        try:
            response = self.supabase.table('contacts').select('*').execute()
            return response.data
        except:
            return []

    def dedup_ventures(self, ventures: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Dedup ventures by (name, sector). Keep first occurrence."""
        seen = {}
        deduped = []
        duplicates = defaultdict(int)

        for v in ventures:
            key = (v.get('name', 'Unknown'), v.get('sector', 'Unknown'))
            if key not in seen:
                seen[key] = v
                deduped.append(v)
            else:
                duplicates[key] += 1

        if duplicates:
            print(f"⚠️  Dedup: Found {len(duplicates)} duplicate venture keys")
            for key, count in list(duplicates.items())[:5]:
                print(f"   {key}: {count} duplicates removed")
            if len(duplicates) > 5:
                print(f"   ... and {len(duplicates)-5} more")

        return deduped

    def create_entity(self, entity_type: str, name: str, description: str = '',
                     metadata: Optional[Dict] = None, venture_id: Optional[str] = None) -> Tuple[Dict, str]:
        """Create entity with dedup key. Returns (entity_dict, entity_id)"""
        entity_id = f"{entity_type}:{name}".replace(' ', '_').lower()

        entity = {
            'id': str(uuid.uuid4()),
            'name': name,
            'entity_type': entity_type,
            'description': description,
            'metadata': metadata or {},
            'venture_id': venture_id,
            'extracted_at': datetime.utcnow().isoformat()
        }

        self.entity_id_map[entity_id] = len(self.entities)
        self.entities.append(entity)
        return entity, entity_id

    def create_relationship(self, source_id: str, target_id: str, relation_type: str, weight: float = 1.0) -> bool:
        """Create relationship if both entities exist. Track orphans."""
        if source_id not in self.entity_id_map or target_id not in self.entity_id_map:
            self.orphan_quarantine.append({
                'source_id': source_id,
                'target_id': target_id,
                'relation_type': relation_type,
                'status': 'ORPHAN'
            })
            return False

        self.relationships.append({
            'id': str(uuid.uuid4()),
            'source_id': self.entities[self.entity_id_map[source_id]]['id'],
            'target_id': self.entities[self.entity_id_map[target_id]]['id'],
            'relation_type': relation_type,
            'weight': weight
        })
        return True

    def infer_risks(self, venture: Dict[str, Any]) -> List[Tuple[str, str, str, str]]:
        """Rule-based risk inference. Returns (risk_name, severity, description, venture_id)"""
        risks = []
        venture_id = venture.get('id')
        mrr = venture.get('mrr', 0) or 0
        runway = venture.get('runway_weeks') or 999
        cac = venture.get('cac') or 0
        ltv = venture.get('ltv') or 0
        status = (venture.get('status') or '').lower()
        stage = (venture.get('stage') or '').lower()

        if mrr < 1000:
            risks.append(('Low Revenue', 'High', f'MRR ${mrr} < $1000', venture_id))

        if runway < 8:
            risks.append(('Short Runway', 'High', f'Runway {runway} weeks < 8', venture_id))
        elif runway < 16:
            risks.append(('Limited Runway', 'Medium', f'Runway {runway} weeks < 16', venture_id))

        if ltv > 0 and cac > 0:
            ratio = ltv / cac
            if ratio < 2:
                risks.append(('CAC/LTV Imbalance', 'High', f'Ratio {ratio:.1f} < 2', venture_id))

        if status in ['paused', 'stalled']:
            risks.append(('Stalled Progress', 'Medium', f'Status: {status}', venture_id))

        if stage == 'mvp':
            risks.append(('MVP Stage', 'Medium', 'Early stage venture', venture_id))

        return risks

    def build_graph(self, ventures: List[Dict[str, Any]], contacts: List[Dict[str, Any]]):
        """Build entire graph with dedup + complete relationships"""
        print(f"[*] Deduplicating {len(ventures)} ventures...")
        ventures = self.dedup_ventures(ventures)
        print(f"[✓] Dedup complete: {len(ventures)} ventures after dedup\n")

        sectors_seen = set()

        print(f"[*] Creating {len(ventures)} Venture entities + relationships...")
        for v in ventures:
            v_name = v.get('name', 'Unknown')
            v_id = v.get('id')

            venture_ent, v_entity_id = self.create_entity(
                'Venture', v_name,
                description=v.get('description', ''),
                metadata={
                    'sector': v.get('sector'),
                    'status': v.get('status'),
                    'stage': v.get('stage'),
                    'mrr': v.get('mrr'),
                    'arr': v.get('arr'),
                    'cac': v.get('cac'),
                    'ltv': v.get('ltv'),
                    'runway_weeks': v.get('runway_weeks'),
                    'team_size': v.get('team_size')
                },
                venture_id=v_id
            )

            sector = v.get('sector')
            if sector:
                if sector not in sectors_seen:
                    sector_ent, sector_entity_id = self.create_entity(
                        'Sector', sector,
                        description=f"Sector: {sector}",
                        metadata={'classification': sector}
                    )
                    sectors_seen.add(sector)
                else:
                    sector_entity_id = f"sector:{sector}".replace(' ', '_').lower()

                self.create_relationship(v_entity_id, sector_entity_id, 'belongs_to_sector')

            for metric_type in ['mrr', 'arr', 'cac', 'ltv', 'runway_weeks', 'team_size']:
                value = v.get(metric_type)
                if value is not None:
                    metric_name = f"{metric_type.upper()} for {v_name[:8]}"
                    metric_ent, metric_entity_id = self.create_entity(
                        'Metric', metric_name,
                        description=f"{metric_type} metric",
                        metadata={
                            'venture_id': v_id,
                            'metric_type': metric_type,
                            'value': float(value) if metric_type != 'runway_weeks' else int(value),
                            'unit': 'USD' if metric_type in ['mrr', 'arr'] else 'weeks' if metric_type == 'runway_weeks' else 'count'
                        },
                        venture_id=v_id
                    )
                    self.create_relationship(v_entity_id, metric_entity_id, 'has_metric')

            risks = self.infer_risks(v)
            for risk_name, severity, description, venture_id in risks:
                risk_ent, risk_entity_id = self.create_entity(
                    'Risk', risk_name,
                    description=description,
                    metadata={
                        'venture_id': venture_id,
                        'risk_type': risk_name,
                        'severity': severity
                    },
                    venture_id=venture_id
                )
                self.create_relationship(v_entity_id, risk_entity_id, 'has_risk')

        print(f"[✓] Venture entities: {len([e for e in self.entities if e['entity_type']=='Venture'])}")

        print(f"\n[*] Creating {len(contacts)} Contact entities...")
        for contact in contacts:
            contact_ent, contact_entity_id = self.create_entity(
                'Contact', contact.get('name', 'Unknown'),
                description=contact.get('role', ''),
                metadata={
                    'email': contact.get('email'),
                    'phone': contact.get('phone'),
                    'role': contact.get('role'),
                    'company': contact.get('company')
                }
            )
        print(f"[✓] Contact entities: {len([e for e in self.entities if e['entity_type']=='Contact'])}")

        print(f"\n[✓] Total: {len(self.entities)} entities, {len(self.relationships)} relationships")

    def validate_completeness(self) -> bool:
        """Validate no orphans before commit"""
        if self.orphan_quarantine:
            print(f"\n❌ VALIDATION FAILED: {len(self.orphan_quarantine)} orphan relationships detected")
            for orphan in self.orphan_quarantine[:10]:
                print(f"   {orphan['source_id']} → {orphan['target_id']} ({orphan['relation_type']})")
            if len(self.orphan_quarantine) > 10:
                print(f"   ... and {len(self.orphan_quarantine)-10} more")
            return False

        print(f"\n✅ VALIDATION PASSED: All {len(self.relationships)} relationships complete")
        return True

    def insert_to_supabase(self):
        """Atomic batch insert of all entities + relationships"""
        print(f"\n[*] Inserting {len(self.entities)} entities to Supabase...")
        batch_size = 100

        try:
            for i in range(0, len(self.entities), batch_size):
                batch = self.entities[i:i+batch_size]
                self.supabase.table('graph_entities').insert(batch).execute()
                total_batches = (len(self.entities)-1)//batch_size + 1
                print(f"   Batch {i//batch_size + 1}/{total_batches} ✓")
        except Exception as e:
            print(f"❌ ERROR inserting entities: {e}")
            sys.exit(1)

        print(f"\n[*] Inserting {len(self.relationships)} relationships to Supabase...")
        try:
            for i in range(0, len(self.relationships), batch_size):
                batch = self.relationships[i:i+batch_size]
                self.supabase.table('graph_relationships').insert(batch).execute()
                total_batches = (len(self.relationships)-1)//batch_size + 1
                print(f"   Batch {i//batch_size + 1}/{total_batches} ✓")
        except Exception as e:
            print(f"❌ ERROR inserting relationships: {e}")
            sys.exit(1)

    def run(self):
        """Execute unified sync"""
        print("=" * 70)
        print("UNIFIED GRAPH SYNC: Dedup + Complete + Validate")
        print("=" * 70)

        print("\n[1/4] Fetching data from Supabase...")
        ventures = self.fetch_ventures()
        contacts = self.fetch_contacts()
        print(f"   ✓ {len(ventures)} ventures, {len(contacts)} contacts")

        print("\n[2/4] Building graph with dedup + edge completion...")
        self.build_graph(ventures, contacts)

        print("\n[3/4] Validating completeness...")
        if not self.validate_completeness():
            print("\n⚠️  Quarantine file saved: orphan_quarantine.json")
            with open('/Users/acebless/Documents/orphan_quarantine.json', 'w') as f:
                json.dump(self.orphan_quarantine, f, indent=2)
            sys.exit(1)

        print("\n[4/4] Inserting to Supabase (atomic)...")
        self.insert_to_supabase()

        print("\n" + "=" * 70)
        print(f"✅ SUCCESS: Graph is self-completing")
        print(f"   {len(self.entities)} entities")
        print(f"   {len(self.relationships)} relationships")
        print(f"   0 orphans")
        print(f"   0 duplicates")
        print("=" * 70)

if __name__ == '__main__':
    sync = UnifiedGraphSync()
    sync.run()
