#!/usr/bin/env python3
"""
Populate knowledge graph from Supabase ventures, contacts, and products.
Extracts entities (ventures, sectors, products, contacts) and relationships.
Enables agent queries against complete venture ecosystem.
"""

import os
import sys
import json
import uuid
from typing import Dict, List, Optional, Tuple
from datetime import datetime


def get_credentials() -> Tuple[str, str]:
    """Load Supabase credentials from env, .env file, or CLI args"""
    # Try CLI arguments
    if len(sys.argv) >= 3:
        return sys.argv[1], sys.argv[2]

    # Try environment variables
    url = os.getenv("SUPABASE_URL", "")
    key = os.getenv("SUPABASE_KEY", "")
    if url and key:
        return url, key

    # Try .env file
    env_file = "/Users/acebless/Documents/.env"
    if os.path.exists(env_file):
        try:
            with open(env_file) as f:
                for line in f:
                    if line.startswith("SUPABASE_URL="):
                        url = line.split("=", 1)[1].strip()
                    elif line.startswith("SUPABASE_KEY="):
                        key = line.split("=", 1)[1].strip()
        except Exception:
            pass
        if url and key:
            return url, key

    return "", ""


SUPABASE_URL, SUPABASE_KEY = get_credentials()


def get_supabase_client():
    """Initialize Supabase client"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("❌ Supabase credentials not set in env")
        return None

    try:
        from supabase import create_client
        return create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception as e:
        print(f"❌ Failed to create Supabase client: {e}")
        return None


def fetch_ventures(client) -> List[Dict]:
    """Fetch all ventures from Supabase"""
    try:
        resp = client.table("ventures").select("*").execute()
        return resp.data if resp.data else []
    except Exception as e:
        print(f"⚠️  Error fetching ventures: {e}")
        return []


def fetch_contacts(client) -> List[Dict]:
    """Fetch all contacts from Supabase"""
    try:
        resp = client.table("contacts").select("*").execute()
        return resp.data if resp.data else []
    except Exception as e:
        print(f"⚠️  Error fetching contacts: {e}")
        return []


def fetch_products(client) -> List[Dict]:
    """Fetch all products from Supabase"""
    try:
        resp = client.table("products").select("*").execute()
        return resp.data if resp.data else []
    except Exception as e:
        print(f"⚠️  Error fetching products: {e}")
        return []


def create_venture_entity(venture: Dict) -> Dict:
    """Create a graph entity for a venture"""
    entity_id = f"entity_venture_{venture.get('id', uuid.uuid4().hex[:8])}"

    return {
        "id": entity_id,
        "name": venture.get("name", "Unknown Venture"),
        "entity_type": "Venture",
        "venture_id": venture.get("id"),
        "description": venture.get("description", ""),
        "metadata": {
            "sector": venture.get("sector", ""),
            "status": venture.get("status", ""),
            "stage": venture.get("stage", ""),
            "mrr": venture.get("mrr", 0),
            "arr": venture.get("arr", 0),
            "cac": venture.get("cac", None),
            "ltv": venture.get("ltv", None),
            "runway_weeks": venture.get("runway_weeks", None),
            "team_size": venture.get("team_size", 0),
            "created_at": venture.get("created_at", ""),
        },
        "extracted_at": datetime.utcnow().isoformat(),
    }


def create_metric_entity(venture: Dict, metric_type: str, value) -> Optional[Dict]:
    """Create a metric entity for a venture"""
    if value is None:
        return None

    entity_id = f"entity_metric_{venture.get('id', uuid.uuid4().hex[:8])}_{metric_type}"

    return {
        "id": entity_id,
        "name": f"{metric_type.upper()}: {value}",
        "entity_type": "Metric",
        "venture_id": venture.get("id"),
        "description": f"{metric_type} metric for {venture.get('name')}",
        "metadata": {
            "metric_type": metric_type,
            "value": value,
            "unit": get_metric_unit(metric_type),
        },
        "extracted_at": datetime.utcnow().isoformat(),
    }


def get_metric_unit(metric_type: str) -> str:
    """Get unit for metric type"""
    units = {
        "mrr": "$",
        "arr": "$",
        "cac": "$",
        "ltv": "$",
        "runway_weeks": "weeks",
        "team_size": "people",
    }
    return units.get(metric_type.lower(), "")


def create_risk_entity(venture: Dict, risk_type: str, severity: str = "medium") -> Dict:
    """Create a risk entity for a venture"""
    entity_id = f"entity_risk_{venture.get('id', uuid.uuid4().hex[:8])}_{risk_type}"

    return {
        "id": entity_id,
        "name": f"{risk_type} Risk - {venture.get('name')}",
        "entity_type": "Risk",
        "venture_id": venture.get("id"),
        "description": f"{risk_type} risk identified for {venture.get('name')}",
        "metadata": {
            "risk_type": risk_type,
            "severity": severity,
        },
        "extracted_at": datetime.utcnow().isoformat(),
    }


def infer_risks(venture: Dict) -> List[Dict]:
    """Infer risks based on venture metrics"""
    risks = []

    # Low MRR risk
    mrr = venture.get("mrr", 0)
    if mrr < 1000:
        risks.append(create_risk_entity(venture, "Low Revenue", "high"))

    # Runway risk
    runway = venture.get("runway_weeks")
    if runway and runway < 8:
        risks.append(create_risk_entity(venture, "Short Runway", "high"))
    elif runway and runway < 16:
        risks.append(create_risk_entity(venture, "Limited Runway", "medium"))

    # Stage-based risks
    stage = venture.get("stage", "").lower()
    if "idea" in stage:
        risks.append(create_risk_entity(venture, "Early Stage", "medium"))
    elif "mvp" in stage:
        risks.append(create_risk_entity(venture, "Product Risk", "medium"))

    # CAC/LTV ratio risk
    cac = venture.get("cac")
    ltv = venture.get("ltv")
    if cac and ltv and cac > 0:
        ratio = ltv / cac
        if ratio < 2:
            risks.append(create_risk_entity(venture, "Poor Unit Economics", "high"))

    # Status-based risks
    status = venture.get("status", "").lower()
    if "paused" in status or "stalled" in status:
        risks.append(create_risk_entity(venture, "Status Stalled", "medium"))

    return risks


def create_sector_entity(sector: str) -> Dict:
    """Create a sector entity"""
    entity_id = f"entity_sector_{sector.lower().replace(' ', '_')}"

    return {
        "id": entity_id,
        "name": sector,
        "entity_type": "Sector",
        "description": f"{sector} sector",
        "metadata": {},
        "extracted_at": datetime.utcnow().isoformat(),
    }


def create_contact_entity(contact: Dict) -> Dict:
    """Create a contact entity"""
    entity_id = f"entity_contact_{contact.get('id', uuid.uuid4().hex[:8])}"

    return {
        "id": entity_id,
        "name": contact.get("name", "Unknown Contact"),
        "entity_type": "Contact",
        "description": f"{contact.get('role', 'Contact')} at {contact.get('company', 'Unknown')}",
        "metadata": {
            "email": contact.get("email", ""),
            "phone": contact.get("phone", ""),
            "role": contact.get("role", ""),
            "company": contact.get("company", ""),
        },
        "extracted_at": datetime.utcnow().isoformat(),
    }


def create_relationships(entities: List[Dict]) -> List[Dict]:
    """Create relationships between entities"""
    relationships = []
    entity_map = {e["id"]: e for e in entities}

    # Map entities by type for easier lookup
    ventures_by_id = {e["id"]: e for e in entities if e["entity_type"] == "Venture"}
    ventures_by_sector = {}
    sectors_by_name = {}

    for entity in entities:
        if entity["entity_type"] == "Venture":
            sector = entity.get("metadata", {}).get("sector")
            if sector:
                if sector not in ventures_by_sector:
                    ventures_by_sector[sector] = []
                ventures_by_sector[sector].append(entity["id"])
        elif entity["entity_type"] == "Sector":
            sectors_by_name[entity["name"]] = entity["id"]

    # Venture → Sector relationships
    for entity in entities:
        if entity["entity_type"] == "Venture":
            sector = entity.get("metadata", {}).get("sector")
            if sector and sector in sectors_by_name:
                relationships.append({
                    "id": f"rel_{uuid.uuid4().hex[:8]}",
                    "source_id": entity["id"],
                    "target_id": sectors_by_name[sector],
                    "relation_type": "belongs_to_sector",
                    "weight": 1.0,
                    "context": f"Venture in {sector} sector",
                    "created_at": datetime.utcnow().isoformat(),
                })

    # Venture → Metrics relationships
    for entity in entities:
        if entity["entity_type"] == "Metric":
            venture_id = entity.get("venture_id")
            if venture_id:
                # Find venture entity with this venture_id
                for v_entity in ventures_by_id.values():
                    if v_entity.get("venture_id") == venture_id:
                        relationships.append({
                            "id": f"rel_{uuid.uuid4().hex[:8]}",
                            "source_id": v_entity["id"],
                            "target_id": entity["id"],
                            "relation_type": "has_metric",
                            "weight": 1.0,
                            "context": f"Metric for {v_entity['name']}",
                            "created_at": datetime.utcnow().isoformat(),
                        })
                        break

    # Venture → Risk relationships
    for entity in entities:
        if entity["entity_type"] == "Risk":
            venture_id = entity.get("venture_id")
            if venture_id:
                for v_entity in ventures_by_id.values():
                    if v_entity.get("venture_id") == venture_id:
                        relationships.append({
                            "id": f"rel_{uuid.uuid4().hex[:8]}",
                            "source_id": v_entity["id"],
                            "target_id": entity["id"],
                            "relation_type": "has_risk",
                            "weight": 1.0,
                            "context": f"Risk for {v_entity['name']}",
                            "created_at": datetime.utcnow().isoformat(),
                        })
                        break

    return relationships


def insert_entities_to_supabase(client, entities: List[Dict]) -> int:
    """Batch insert entities to Supabase"""
    if not entities:
        return 0

    inserted = 0
    batch_size = 100

    for i in range(0, len(entities), batch_size):
        batch = entities[i : i + batch_size]
        try:
            client.table("graph_entities").insert(batch).execute()
            inserted += len(batch)
            print(f"✅ Inserted {inserted}/{len(entities)} entities")
        except Exception as e:
            print(f"⚠️  Error inserting batch {i//batch_size}: {e}")

    return inserted


def insert_relationships_to_supabase(client, relationships: List[Dict]) -> int:
    """Batch insert relationships to Supabase"""
    if not relationships:
        return 0

    inserted = 0
    batch_size = 100

    for i in range(0, len(relationships), batch_size):
        batch = relationships[i : i + batch_size]
        try:
            client.table("graph_relationships").insert(batch).execute()
            inserted += len(batch)
            print(f"✅ Inserted {inserted}/{len(relationships)} relationships")
        except Exception as e:
            print(f"⚠️  Error inserting batch {i//batch_size}: {e}")

    return inserted


def main():
    """Populate knowledge graph from ventures"""

    print("\n🚀 Populating Knowledge Graph from Ventures")
    print("=" * 70)

    client = get_supabase_client()
    if not client:
        return

    # Fetch data
    print("\n📥 Fetching data from Supabase...")
    ventures = fetch_ventures(client)
    contacts = fetch_contacts(client)
    products = fetch_products(client)

    print(f"   Ventures: {len(ventures)}")
    print(f"   Contacts: {len(contacts)}")
    print(f"   Products: {len(products)}")

    # Extract entities
    print("\n🔍 Extracting entities...")
    entities = []

    # Venture entities
    sectors_added = set()
    for venture in ventures:
        entities.append(create_venture_entity(venture))

        # Add sector entities
        sector = venture.get("sector", "")
        if sector and sector not in sectors_added:
            entities.append(create_sector_entity(sector))
            sectors_added.add(sector)

        # Add metric entities
        for metric_type in ["mrr", "arr", "cac", "ltv", "runway_weeks", "team_size"]:
            value = venture.get(metric_type)
            if value:
                metric_entity = create_metric_entity(venture, metric_type, value)
                if metric_entity:
                    entities.append(metric_entity)

        # Add risk entities
        entities.extend(infer_risks(venture))

    # Contact entities
    for contact in contacts:
        entities.append(create_contact_entity(contact))

    print(f"   Total entities extracted: {len(entities)}")
    entity_types = {}
    for e in entities:
        etype = e["entity_type"]
        entity_types[etype] = entity_types.get(etype, 0) + 1

    for etype, count in sorted(entity_types.items()):
        print(f"     - {etype}: {count}")

    # Create relationships
    print("\n🔗 Creating relationships...")
    relationships = create_relationships(entities)
    print(f"   Total relationships: {len(relationships)}")
    rel_types = {}
    for r in relationships:
        rtype = r["relation_type"]
        rel_types[rtype] = rel_types.get(rtype, 0) + 1

    for rtype, count in sorted(rel_types.items()):
        print(f"     - {rtype}: {count}")

    # Sync to Supabase
    print("\n📤 Syncing to Supabase...")
    entities_inserted = insert_entities_to_supabase(client, entities)
    relationships_inserted = insert_relationships_to_supabase(client, relationships)

    print(f"\n{'='*70}")
    print(f"✅ KNOWLEDGE GRAPH POPULATED")
    print(f"{'='*70}")
    print(f"   Entities: {entities_inserted}")
    print(f"   Relationships: {relationships_inserted}")
    print(f"\n💡 Next step: Run `python3 obsidian_graph_sync.py` to export to Obsidian")


if __name__ == "__main__":
    main()
