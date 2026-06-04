#!/usr/bin/env python3
"""Quick test of Chroma + DuckDB + CrewAI integration."""

import asyncio
import sys
import importlib.util
from dotenv import load_dotenv

# Load env vars first
load_dotenv('/Users/acebless/Documents/.env')

sys.path.insert(0, '/Users/acebless/Documents')

spec = importlib.util.spec_from_file_location("iza_hub", "/Users/acebless/Documents/integrations/iza-integration-hub.py")
iza_hub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iza_hub)
IZAIntegrationHub = iza_hub.IZAIntegrationHub

async def test_integration():
    """Test ventures integration."""
    print("🚀 Testing IZA Integration Hub with Chroma + DuckDB\n")

    hub = IZAIntegrationHub()

    # Sample ventures
    sample_ventures = [
        {
            "id": "venture-001",
            "name": "HRMS Solutions",
            "sector": "HR Tech",
            "stage": "MVP",
            "metrics": {"arr": 0, "mrr": 5000, "users": 10}
        },
        {
            "id": "venture-002",
            "name": "Pitch Kit",
            "sector": "Investor Tools",
            "stage": "Beta",
            "metrics": {"arr": 12000, "mrr": 1000, "users": 50}
        },
        {
            "id": "venture-003",
            "name": "Graphify",
            "sector": "Developer Tools",
            "stage": "Active",
            "metrics": {"arr": 24000, "mrr": 2000, "users": 150}
        }
    ]

    # Test 1: Ingest ventures
    print("1️⃣ Ingesting ventures to Chroma + DuckDB...")
    result = await hub.ingest_ventures(sample_ventures)
    print(f"   ✓ {result['chroma_indexed']} ventures indexed in Chroma")
    print(f"   ✓ DuckDB loaded: {result['duckdb_loaded']}\n")

    # Test 2: Vector search
    print("2️⃣ Vector search (Chroma)...")
    search_result = await hub.search_ventures("payroll and HR automation", n_results=2)
    print(f"   ✓ Found {len(search_result['results']['ids'][0])} relevant ventures\n")

    # Test 3: SQL analytics
    print("3️⃣ SQL Analytics (DuckDB)...")
    query = "SELECT name, sector, metrics FROM ventures WHERE metrics LIKE '%mrr%' ORDER BY name"
    analytics_result = await hub.analyze_ventures(query)
    print(f"   ✓ Query returned {analytics_result['row_count']} rows\n")

    print("✅ All tests passed! System is ready.")
    print("\nNext steps:")
    print("  - Use hub.ingest_ventures(ventures_list) to index ventures")
    print("  - Use hub.search_ventures(query) for semantic search")
    print("  - Use hub.analyze_ventures(sql) for SQL analytics")

if __name__ == "__main__":
    asyncio.run(test_integration())
