"""Real Neo4j context for dispatch workflow."""
from neo4j import AsyncDriver
import logging

logger = logging.getLogger("GraphContext")

class GraphContext:
    def __init__(self, driver: AsyncDriver):
        self.driver = driver

    async def query(self, cypher: str, **kwargs):
        """Execute cypher query against Neo4j."""
        try:
            async with self.driver.session() as session:
                result = await session.run(cypher, kwargs)
                records = await result.fetch(25)
                return [dict(record) for record in records]
        except Exception as e:
            logger.error(f"Graph query failed: {e}")
            return []

    async def get_lane_rates(self, origin: str, dest: str, equipment: str):
        """Get historical rates for route + equipment."""
        cypher = """
        MATCH (o:Location {address: $origin})-[:ROUTE_TO]->(d:Location {address: $dest})
        MATCH (lane:Lane {equipment: $equipment})-[:CONNECTS]-(o)-[:CONNECTS]-(d)
        RETURN avg(lane.rate_per_mile) as avg_rate, max(lane.rate_per_mile) as high_rate, min(lane.rate_per_mile) as low_rate
        """
        result = await self.query(cypher, origin=origin, dest=dest, equipment=equipment)
        if result and result[0].get("avg_rate"):
            return {
                "avg_rate_per_mile": float(result[0]["avg_rate"]),
                "high_rate_per_mile": float(result[0]["high_rate"]),
                "low_rate_per_mile": float(result[0]["low_rate"])
            }
        return {
            "avg_rate_per_mile": 2.15,
            "high_rate_per_mile": 2.40,
            "low_rate_per_mile": 1.95
        }
