"""Supabase → dispatch_engine: fetch real loads."""
import asyncio
from supabase import AsyncClient
from dispatch_engine import Load, Location

class SupabaseLoader:
    def __init__(self, url: str, key: str):
        self.client = AsyncClient(url, key)

    async def fetch_pending_loads(self):
        """Fetch PENDING loads from Supabase."""
        try:
            response = await self.client.table("loads").select("*").eq("status", "PENDING").limit(5).execute()
            return response.data if response.data else []
        except Exception as e:
            print(f"Supabase fetch failed: {e}")
            return []

    def supabase_to_load(self, row: dict) -> Load:
        """Convert Supabase row → Load model."""
        return Load(
            id=row.get("id", "unknown"),
            shipper_id=row.get("shipper_id", "unknown"),
            origin=Location(
                address=row.get("origin_address", "Charlotte, NC"),
                latitude=row.get("origin_lat", 35.2271),
                longitude=row.get("origin_lng", -80.8431)
            ),
            destination=Location(
                address=row.get("destination_address", "Atlanta, GA"),
                latitude=row.get("destination_lat", 33.7490),
                longitude=row.get("destination_lng", -84.3880)
            ),
            equipment_type=row.get("equipment_type", "53ft-dry-van"),
            weight_lbs=row.get("weight_lbs", 45000),
            budget_usd=row.get("budget_usd", 1250),
            status=row.get("status", "PENDING")
        )
