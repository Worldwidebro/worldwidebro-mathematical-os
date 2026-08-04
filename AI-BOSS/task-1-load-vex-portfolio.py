#!/usr/bin/env python3
"""Task 1: Load VEX Portfolio (Ventures) into Neo4j"""

import csv
import sys
from pathlib import Path
from neo4j import GraphDatabase

SCORECARD = Path("/Users/acebless/Documents/.planning/VENTURE-READINESS-SCORECARD-V2.csv")
NEO4J_URI = "neo4j://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "ventures2026"

def load_vex_portfolio():
    """Load ventures from scorecard into Neo4j."""

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        # Read CSV
        ventures = []
        with open(SCORECARD) as f:
            reader = csv.DictReader(f)
            ventures = list(reader)

        print(f"✓ Read {len(ventures)} ventures from {SCORECARD.name}")

        # Create nodes in Neo4j
        with driver.session() as session:
            created = 0
            for venture in ventures:
                try:
                    # Sanitize values
                    venture_id = venture.get("venture_id", "").strip()
                    name = venture.get("name", "").strip()
                    sector = venture.get("sector", "").strip()
                    stage = venture.get("development_stage", "").strip()
                    readiness = venture.get("readiness_%", "0").strip()

                    if not venture_id:
                        continue

                    # Convert readiness to float
                    try:
                        readiness_pct = float(readiness) if readiness else 0.0
                    except ValueError:
                        readiness_pct = 0.0

                    # Create node
                    session.run(
                        """
                        MERGE (v:Venture {id: $venture_id})
                        SET v.name = $name,
                            v.sector = $sector,
                            v.stage = $stage,
                            v.readiness_pct = $readiness,
                            v.created_at = datetime()
                        """,
                        venture_id=venture_id,
                        name=name,
                        sector=sector,
                        stage=stage,
                        readiness=readiness_pct
                    )
                    created += 1
                except Exception as e:
                    print(f"  ✗ Error creating {venture_id}: {e}")

        print(f"✓ Created {created} venture nodes in Neo4j")

        # Verify
        with driver.session() as session:
            result = session.run("MATCH (v:Venture) RETURN count(v) AS count")
            count = result.single()["count"]
            print(f"✓ Verified: {count} ventures in Neo4j")

            # Show sector distribution
            result = session.run("""
                MATCH (v:Venture)
                RETURN v.sector AS sector, count(v) AS count
                ORDER BY count DESC
            """)
            print("\nSector distribution:")
            for row in result:
                print(f"  {row['sector']}: {row['count']}")

        return count

    finally:
        driver.close()


if __name__ == "__main__":
    try:
        count = load_vex_portfolio()
        print(f"\n✓ TASK 1 COMPLETE: {count} ventures loaded")
        sys.exit(0)
    except Exception as e:
        print(f"✗ TASK 1 FAILED: {e}")
        sys.exit(1)
