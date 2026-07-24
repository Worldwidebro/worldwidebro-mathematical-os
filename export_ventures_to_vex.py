#!/usr/bin/env python3
"""
Connector 1: Supabase → vex-hero-site data export.
Syncs ventures from Supabase to portfolio.public.json for frontend rendering.
Runs hourly or on webhook trigger.
"""

import asyncio
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

from supabase import AsyncClient, create_client

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
VEX_DATA_PATH = Path(__file__).parent / "vex-hero-site/src/data/portfolio.public.json"

PUBLIC_FIELDS = {"id", "name", "sector", "opco", "stage", "status"}


async def fetch_ventures(client: AsyncClient) -> list[dict[str, Any]]:
    """Fetch all ventures from Supabase, public fields only."""
    response = await client.table("ventures").select(",".join(PUBLIC_FIELDS)).execute()
    return response.data or []


async def load_portfolio() -> dict[str, Any]:
    """Load existing portfolio.public.json to preserve metadata."""
    if VEX_DATA_PATH.exists():
        return json.loads(VEX_DATA_PATH.read_text())
    return {"generatedAt": datetime.utcnow().isoformat() + "Z", "ventures": [], "metrics": {"ventures": 0}}


async def export_ventures_to_vex(supabase_key: str | None = None) -> None:
    """Fetch ventures, transform, write to portfolio.public.json."""
    key = supabase_key or os.getenv("SUPABASE_KEY")
    if not key:
        raise ValueError("SUPABASE_KEY not set")

    client = await create_client(SUPABASE_URL, key)
    try:
        ventures = await fetch_ventures(client)
        print(f"✓ Fetched {len(ventures)} ventures from Supabase")

        portfolio = await load_portfolio()
        portfolio["ventures"] = ventures
        portfolio["generatedAt"] = datetime.utcnow().isoformat() + "Z"
        portfolio["metrics"]["ventures"] = len(ventures)

        VEX_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        VEX_DATA_PATH.write_text(json.dumps(portfolio, indent=2))
        print(f"✓ Wrote {len(ventures)} ventures to {VEX_DATA_PATH}")
    finally:
        await client.aclose()


if __name__ == "__main__":
    asyncio.run(export_ventures_to_vex())
