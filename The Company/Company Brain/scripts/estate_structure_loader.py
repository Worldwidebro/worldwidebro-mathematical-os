#!/usr/bin/env python3
"""
Estate Structure Loader → Neo4j

Loads family office structure into Neo4j:
- FAMILY (root)
  - TRUST (revocable, irrevocable, dynasty)
  - BENEFICIARY (individual, next gen)
  - HOLDCO (operational holding)
  - SPV (deal-specific vehicle)
  - VENTURE (operating company)

Creates full ownership graph enabling:
- Succession planning queries
- Tax structure visibility
- Capital allocation tracking
- Inheritance automation

Author: Company Brain Automation
"""

import os
from typing import Optional, Dict, List, Any
from datetime import datetime

from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://100.87.214.70:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "changeme")


class EstateStructureLoader:
    """Loads family office estate structure into Neo4j"""

    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def create_family_structure(self, family_config: Dict[str, Any]):
        """
        Create complete family office structure

        Config format:
        {
            "family": {
                "name": "Worldwidebro Family",
                "jurisdiction": "Delaware",
                "founded": "2024-01-01"
            },
            "trustees": [...],
            "beneficiaries": [...],
            "trusts": [...],
            "entities": [...],
            "capital_allocation": [...]
        }
        """

        with self.driver.session() as session:
            # 1. Create family root node
            session.run(
                """
                MERGE (f:FAMILY {name: $name})
                SET f.jurisdiction = $jurisdiction,
                    f.founded = $founded,
                    f.updated = $timestamp
                RETURN f
                """,
                name=family_config["family"]["name"],
                jurisdiction=family_config["family"].get("jurisdiction", "Delaware"),
                founded=family_config["family"].get("founded"),
                timestamp=datetime.utcnow().isoformat(),
            )

            # 2. Create trustees
            for trustee in family_config.get("trustees", []):
                session.run(
                    """
                    MERGE (p:PERSON {name: $name})
                    SET p.role = 'TRUSTEE',
                        p.contact = $contact,
                        p.updated = $timestamp
                    WITH p
                    MATCH (f:FAMILY {name: $family_name})
                    MERGE (p)-[:TRUSTEES]->(f)
                    """,
                    name=trustee["name"],
                    contact=trustee.get("contact"),
                    family_name=family_config["family"]["name"],
                    timestamp=datetime.utcnow().isoformat(),
                )

            # 3. Create beneficiaries
            for beneficiary in family_config.get("beneficiaries", []):
                session.run(
                    """
                    MERGE (p:PERSON {name: $name})
                    SET p.role = 'BENEFICIARY',
                        p.generation = $generation,
                        p.contact = $contact,
                        p.updated = $timestamp
                    WITH p
                    MATCH (f:FAMILY {name: $family_name})
                    MERGE (p)-[:BENEFICIARY_OF]->(f)
                    """,
                    name=beneficiary["name"],
                    generation=beneficiary.get("generation", 1),
                    contact=beneficiary.get("contact"),
                    family_name=family_config["family"]["name"],
                    timestamp=datetime.utcnow().isoformat(),
                )

            # 4. Create trusts
            for trust in family_config.get("trusts", []):
                session.run(
                    """
                    MERGE (t:TRUST {name: $name})
                    SET t.type = $type,
                        t.jurisdiction = $jurisdiction,
                        t.trustee = $trustee,
                        t.created = $created,
                        t.updated = $timestamp
                    WITH t
                    MATCH (f:FAMILY {name: $family_name})
                    MERGE (t)-[:PART_OF]->(f)
                    """,
                    name=trust["name"],
                    type=trust.get("type", "revocable"),
                    jurisdiction=trust.get("jurisdiction", "Delaware"),
                    trustee=trust.get("trustee"),
                    created=trust.get("created"),
                    family_name=family_config["family"]["name"],
                    timestamp=datetime.utcnow().isoformat(),
                )

                # Link beneficiaries to trust
                for beneficiary_name in trust.get("beneficiaries", []):
                    session.run(
                        """
                        MATCH (p:PERSON {name: $beneficiary})
                        MATCH (t:TRUST {name: $trust})
                        MERGE (p)-[:BENEFICIARY_OF {
                            percentage: $percentage,
                            start_date: $start_date
                        }]->(t)
                        """,
                        beneficiary=beneficiary_name,
                        trust=trust["name"],
                        percentage=100 / len(trust.get("beneficiaries", [1])),
                        start_date=trust.get("created"),
                    )

            # 5. Create holding companies
            for entity in family_config.get("entities", []):
                session.run(
                    """
                    MERGE (e:HOLDCO {name: $name})
                    SET e.type = $type,
                        e.jurisdiction = $jurisdiction,
                        e.ownership_structure = $ownership,
                        e.updated = $timestamp
                    WITH e
                    MATCH (f:FAMILY {name: $family_name})
                    MERGE (e)-[:OWNED_BY]->(f)
                    """,
                    name=entity["name"],
                    type=entity.get("type", "LLC"),
                    jurisdiction=entity.get("jurisdiction"),
                    ownership=entity.get("ownership"),
                    family_name=family_config["family"]["name"],
                    timestamp=datetime.utcnow().isoformat(),
                )

            # 6. Link SPVs to holdings
            for spv in family_config.get("spvs", []):
                session.run(
                    """
                    MERGE (s:SPV {name: $name})
                    SET s.deal_focus = $deal_focus,
                        s.created = $created,
                        s.updated = $timestamp
                    WITH s
                    MATCH (h:HOLDCO {name: $holdco})
                    MERGE (s)-[:MANAGED_BY]->(h)
                    """,
                    name=spv["name"],
                    deal_focus=spv.get("focus"),
                    created=spv.get("created"),
                    holdco=spv.get("holdco"),
                    timestamp=datetime.utcnow().isoformat(),
                )

            # 7. Link ventures to SPVs/trusts
            for allocation in family_config.get("capital_allocation", []):
                session.run(
                    """
                    MATCH (v:VENTURE {id: $venture_id})
                    MATCH (s:SPV {name: $spv_name})
                    MERGE (s)-[:INVESTS_IN {
                        amount: $amount,
                        ownership_percentage: $ownership,
                        invested_date: $date
                    }]->(v)
                    """,
                    venture_id=allocation["venture_id"],
                    spv_name=allocation.get("spv"),
                    amount=allocation.get("amount"),
                    ownership=allocation.get("ownership_percentage", 100),
                    date=allocation.get("date"),
                )

    def create_example_estate(self):
        """Create example Worldwidebro estate structure"""

        estate_config = {
            "family": {
                "name": "Worldwidebro Family",
                "jurisdiction": "Delaware",
                "founded": "2024-01-01",
            },
            "trustees": [
                {
                    "name": "Antwuan Johns",
                    "contact": "antwuan@worldwidebro.com",
                },
                {
                    "name": "Estate Trustee (External)",
                    "contact": "trustee@external.com",
                },
            ],
            "beneficiaries": [
                {
                    "name": "Antwuan Johns",
                    "generation": 1,
                },
                {
                    "name": "Next Generation Child",
                    "generation": 2,
                },
            ],
            "trusts": [
                {
                    "name": "Revocable Living Trust",
                    "type": "revocable",
                    "jurisdiction": "Delaware",
                    "trustee": "Antwuan Johns",
                    "beneficiaries": ["Antwuan Johns"],
                    "created": "2024-01-01",
                },
                {
                    "name": "Irrevocable Dynasty Trust",
                    "type": "irrevocable",
                    "jurisdiction": "Delaware",
                    "trustee": "Estate Trustee (External)",
                    "beneficiaries": ["Antwuan Johns", "Next Generation Child"],
                    "created": "2024-06-01",
                },
            ],
            "entities": [
                {
                    "name": "Worldwidebro Holdings LLC",
                    "type": "LLC",
                    "jurisdiction": "Delaware",
                    "ownership": "100% Revocable Living Trust",
                },
                {
                    "name": "WB Operations Company",
                    "type": "LLC",
                    "jurisdiction": "Delaware",
                    "ownership": "100% Worldwidebro Holdings",
                },
            ],
            "spvs": [
                {
                    "name": "SPV-OPS-001",
                    "holdco": "Worldwidebro Holdings LLC",
                    "focus": "CareerOps Staffing",
                    "created": "2024-03-01",
                },
                {
                    "name": "SPV-CON-001",
                    "holdco": "Worldwidebro Holdings LLC",
                    "focus": "ACE Construction",
                    "created": "2024-03-01",
                },
                {
                    "name": "SPV-LT-005",
                    "holdco": "Worldwidebro Holdings LLC",
                    "focus": "HealthRoute Courier",
                    "created": "2024-03-01",
                },
                {
                    "name": "SPV-RE-001",
                    "holdco": "Worldwidebro Holdings LLC",
                    "focus": "Real Estate Syndication",
                    "created": "2024-04-01",
                },
            ],
            "capital_allocation": [
                {
                    "venture_id": "ops-001",
                    "spv": "SPV-OPS-001",
                    "amount": 50000,
                    "ownership_percentage": 100,
                    "date": "2024-03-15",
                },
                {
                    "venture_id": "con-001",
                    "spv": "SPV-CON-001",
                    "amount": 75000,
                    "ownership_percentage": 100,
                    "date": "2024-03-15",
                },
                {
                    "venture_id": "lt-005",
                    "spv": "SPV-LT-005",
                    "amount": 100000,
                    "ownership_percentage": 100,
                    "date": "2024-03-15",
                },
            ],
        }

        self.create_family_structure(estate_config)
        print("✅ Example estate structure created")

    def query_succession_plan(self) -> Dict[str, Any]:
        """Query succession plan for family"""

        with self.driver.session() as session:
            # Get all beneficiaries and their trusts
            result = session.run(
                """
                MATCH (f:FAMILY)<-[:BENEFICIARY_OF]-(b:PERSON)
                OPTIONAL MATCH (b)-[:BENEFICIARY_OF]->(t:TRUST)
                OPTIONAL MATCH (t)-[:PART_OF]->(f)
                RETURN b.name as beneficiary, b.generation as generation,
                       collect(t.name) as trusts
                ORDER BY b.generation
                """
            )

            return [record.data() for record in result]

    def query_capital_structure(self) -> Dict[str, Any]:
        """Query capital structure and ownership"""

        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (v:VENTURE)<-[inv:INVESTS_IN]-(s:SPV)
                OPTIONAL MATCH (s)-[:MANAGED_BY]->(h:HOLDCO)
                RETURN v.name as venture, v.id as venture_id,
                       s.name as spv, h.name as holdco,
                       inv.amount as amount, inv.ownership_percentage as ownership
                ORDER BY v.name
                """
            )

            return [record.data() for record in result]


def main():
    """Example usage"""

    loader = EstateStructureLoader()

    try:
        # Create example estate
        loader.create_example_estate()

        # Query succession plan
        print("\n=== Succession Plan ===")
        succession = loader.query_succession_plan()
        for s in succession:
            print(f"{s['beneficiary']} (Gen {s['generation']}): {', '.join(s['trusts'])}")

        # Query capital structure
        print("\n=== Capital Structure ===")
        capital = loader.query_capital_structure()
        for c in capital:
            print(
                f"{c['venture']} via {c['spv']} ({c['holdco']}): "
                f"${c['amount']:,} ({c['ownership']}%)"
            )

    finally:
        loader.close()


if __name__ == "__main__":
    main()
