#!/usr/bin/env python3
"""
Obsidian Vault → Knowledge Graph Sync
Watches markdown files, extracts entities/relationships/tags, syncs to Neo4j via Supabase.
"""

import os
import sys
import re
import json
import uuid
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple
from dotenv import load_dotenv
from collections import defaultdict

try:
    import frontmatter
    from supabase import create_client
except ImportError:
    print("ERROR: Missing dependencies. Run: pip install python-frontmatter supabase-py")
    sys.exit(1)

load_dotenv()

class ObsidianGraphSync:
    """Parse Obsidian vault, extract knowledge, sync to Neo4j"""

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        if not self.vault_path.exists():
            print(f"ERROR: Vault path not found: {vault_path}")
            sys.exit(1)

        self.url = os.getenv('SUPABASE_URL')
        self.key = os.getenv('SUPABASE_KEY')
        if not self.url or not self.key:
            print("ERROR: Set SUPABASE_URL and SUPABASE_KEY in .env")
            sys.exit(1)

        self.supabase = create_client(self.url, self.key)
        self.entities = []
        self.relationships = []
        self.entity_map = {}

    def extract_frontmatter(self, filepath: Path) -> Dict:
        """Extract YAML frontmatter from markdown"""
        try:
            with open(filepath, 'r') as f:
                post = frontmatter.load(f)
            return post.metadata
        except:
            return {}

    def extract_entities_from_md(self, content: str) -> List[Tuple[str, str, str]]:
        """Extract entities from markdown: [[links]], #tags, OPCO-NNN, venture IDs"""
        entities = []

        # [[WikiLink]] pattern
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
        for link in wikilinks:
            if link.startswith('OPCO-') or link.startswith('RE-') or link.startswith('CON-'):
                entities.append(('VentureRef', link, f"Reference to {link}"))
            else:
                entities.append(('Concept', link, f"Concept: {link}"))

        # #hashtag pattern
        hashtags = re.findall(r'#([a-zA-Z_]\w*)', content)
        for tag in set(hashtags):
            entities.append(('Tag', tag, f"Tag: {tag}"))

        # OPCO-NNN pattern
        opcos = re.findall(r'\b(OPCO-\d{3})\b', content)
        for opco in set(opcos):
            entities.append(('OPCO', opco, f"Operating Company {opco}"))

        # Venture ID pattern (RE-NNN, CON-NNN, etc)
        ventures = re.findall(r'\b([A-Z]{2,3}-\d{3,4})\b', content)
        for venture in set(ventures):
            if venture not in ['DO-NOT', 'TO-DO', 'GO-TO']:
                entities.append(('Venture', venture, f"Venture {venture}"))

        return entities

    def extract_backlinks(self, content: str, source: str) -> List[Tuple[str, str, str]]:
        """Extract relationships: source → target"""
        rels = []
        targets = re.findall(r'\[\[([^\]]+)\]\]', content)
        for target in targets:
            rels.append((source, target, 'references'))
        return rels

    def scan_vault(self) -> Tuple[List[Dict], List[Dict]]:
        """Scan vault for .md files"""
        md_files = list(self.vault_path.glob('**/*.md'))
        print(f"[*] Scanning {len(md_files)} markdown files...")

        entities_list = []
        relationships_list = []

        for i, filepath in enumerate(md_files):
            if (i + 1) % 50 == 0:
                print(f"   Processed {i+1}/{len(md_files)}...")

            fm = self.extract_frontmatter(filepath)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            doc_name = filepath.stem
            entities = self.extract_entities_from_md(content)

            for entity_type, name, desc in entities:
                entity_id = f"{entity_type}:{name}".lower()
                if entity_id not in self.entity_map:
                    self.entity_map[entity_id] = str(uuid.uuid4())
                    entities_list.append({
                        'id': self.entity_map[entity_id],
                        'name': name,
                        'entity_type': entity_type,
                        'description': desc,
                        'metadata': fm.copy() if fm else {},
                        'source_file': str(filepath),
                        'extracted_at': datetime.utcnow().isoformat()
                    })

            rels = self.extract_backlinks(content, doc_name)
            for source, target, rel_type in rels:
                source_id = self.entity_map.get(f"document:{source}", str(uuid.uuid4()))
                target_id = self.entity_map.get(f"venture:{target}".lower(), None)
                if target_id:
                    relationships_list.append({
                        'id': str(uuid.uuid4()),
                        'source_id': source_id,
                        'target_id': target_id,
                        'relation_type': rel_type,
                        'weight': 1.0
                    })

        print(f"[✓] Extracted {len(entities_list)} entities")
        return entities_list, relationships_list

    def sync_to_graph(self, entities: List[Dict], relationships: List[Dict]):
        """Sync to Supabase graph tables"""
        if not entities:
            print("[!] No entities to sync")
            return

        print(f"[*] Syncing {len(entities)} entities...")
        batch_size = 100
        try:
            for i in range(0, len(entities), batch_size):
                batch = entities[i:i+batch_size]
                self.supabase.table('graph_entities').insert(batch).execute()
                print(f"   Batch {i//batch_size + 1}/{(len(entities)-1)//batch_size + 1} ✓")
        except Exception as e:
            print(f"[!] Entities: {str(e)[:100]}")

        if relationships:
            print(f"[*] Syncing {len(relationships)} relationships...")
            try:
                for i in range(0, len(relationships), batch_size):
                    batch = relationships[i:i+batch_size]
                    self.supabase.table('graph_relationships').insert(batch).execute()
                    print(f"   Batch {i//batch_size + 1} ✓")
            except Exception as e:
                print(f"[!] Relationships: {str(e)[:100]}")

    def run(self):
        print("=" * 70)
        print("OBSIDIAN VAULT → KNOWLEDGE GRAPH")
        print("=" * 70)
        print(f"\nScanning: {self.vault_path}\n")

        entities, relationships = self.scan_vault()

        print(f"\n✓ Ventures: {len([e for e in entities if e['entity_type']=='Venture'])}")
        print(f"✓ Concepts: {len([e for e in entities if e['entity_type']=='Concept'])}")
        print(f"✓ Tags: {len([e for e in entities if e['entity_type']=='Tag'])}")
        print(f"✓ OPCOs: {len([e for e in entities if e['entity_type']=='OPCO'])}")

        print(f"\nSyncing to graph...")
        self.sync_to_graph(entities, relationships)

        print("\n" + "=" * 70)
        print(f"✅ COMPLETE: {len(entities)} entities, {len(relationships)} relationships")
        print("=" * 70)

if __name__ == '__main__':
    vault = os.getenv('OBSIDIAN_VAULT_PATH', os.path.expanduser('~/Documents/obsidian-vault'))
    sync = ObsidianGraphSync(vault)
    sync.run()
