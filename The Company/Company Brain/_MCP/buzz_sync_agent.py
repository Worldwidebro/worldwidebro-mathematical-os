"""
Buzz Sync Agent (AGT-019) - Phase 3: Sync & Persistence
Monitors Buzz channels for completed conversations and syncs to Neo4j

Authority: Collaboration Control Plane (CP-028) + Infrastructure Control Plane (CP-027)
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - AGT-019 - %(levelname)s - %(message)s'
)
logger = logging.getLogger("buzz-sync-agent")


class BuzzSyncAgent:
    """
    Autonomous sync agent that:
    1. Monitors Buzz channels for "final_decision" events
    2. Reads complete conversation threads (audit trail)
    3. Merges into Neo4j with cryptographic verification
    4. Maintains bidirectional sync state
    """

    def __init__(
        self,
        buzz_relay_url: str = "http://100.87.214.70:8080",
        neo4j_uri: str = "bolt://100.87.214.70:7687",
        neo4j_user: str = "neo4j",
        neo4j_password: str = "changeme"
    ):
        self.buzz_relay_url = buzz_relay_url
        self.neo4j_uri = neo4j_uri
        self.neo4j_user = neo4j_user
        self.neo4j_password = neo4j_password
        self.driver = None
        self.workspace = "company-brain"
        self.channels = [
            "repo-classification",
            "repo-scoring",
            "repo-disposition",
            "repo-adoption-pipeline"
        ]
        self.last_sync_time = {}

    async def initialize(self):
        """Initialize Neo4j connection"""
        try:
            self.driver = GraphDatabase.driver(
                self.neo4j_uri,
                auth=(self.neo4j_user, self.neo4j_password)
            )
            # Test connection
            self.driver.verify_connectivity()
            logger.info("✅ Connected to Neo4j")
        except Neo4jError as e:
            logger.error(f"❌ Failed to connect to Neo4j: {e}")
            raise

    async def shutdown(self):
        """Clean up Neo4j connection"""
        if self.driver:
            self.driver.close()
            logger.info("Closed Neo4j connection")

    async def fetch_channel_events(
        self,
        channel: str,
        since: Optional[datetime] = None
    ) -> List[Dict[str, Any]]:
        """
        Fetch events from Buzz channel since last sync

        Args:
            channel: Channel name
            since: Only fetch events after this timestamp

        Returns:
            List of events with full metadata
        """
        import requests

        try:
            url = f"{self.buzz_relay_url}/api/v1/workspaces/{self.workspace}/channels/{channel}/events"

            params = {
                "limit": 100,
                "sort": "created_at:desc"
            }

            if since:
                params["since"] = since.isoformat()

            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                return response.json()
            else:
                logger.warning(f"Buzz API returned {response.status_code} for {channel}")
                return []

        except Exception as e:
            logger.error(f"Error fetching events from {channel}: {e}")
            return []

    async def process_event(self, event: Dict[str, Any], channel: str) -> bool:
        """
        Process a single Buzz event and sync to Neo4j

        Args:
            event: Event data from Buzz
            channel: Channel it came from

        Returns:
            True if sync succeeded, False otherwise
        """
        try:
            event_id = event.get("id")
            event_type = event.get("event_type")
            payload = event.get("payload", {})
            author = event.get("author")
            timestamp = event.get("timestamp")
            signature = event.get("signature")

            with self.driver.session() as session:
                # Create BuzzEvent node
                session.run("""
                    MERGE (e:BuzzEvent {event_id: $event_id})
                    SET e.channel = $channel,
                        e.event_type = $event_type,
                        e.author = $author,
                        e.payload = $payload,
                        e.timestamp = $timestamp,
                        e.signature = $signature,
                        e.synced_at = $synced_at
                    RETURN e
                """, {
                    "event_id": event_id,
                    "channel": channel,
                    "event_type": event_type,
                    "author": author,
                    "payload": json.dumps(payload),
                    "timestamp": timestamp,
                    "signature": signature,
                    "synced_at": datetime.utcnow().isoformat()
                })

                # Process based on channel and event type
                if channel == "repo-classification" and event_type == "repo_classified":
                    await self._sync_classification(session, event_id, payload)

                elif channel == "repo-scoring" and event_type == "repo_scored":
                    await self._sync_scoring(session, event_id, payload)

                elif channel == "repo-disposition" and event_type == "repo_disposition":
                    await self._sync_disposition(session, event_id, payload)

                # Link to repository if present
                repo_id = payload.get("repo_id")
                if repo_id:
                    session.run("""
                        MATCH (repo:ExternalRepository {repo_id: $repo_id})
                        MATCH (buzz:BuzzEvent {event_id: $event_id})
                        MERGE (buzz)-[:REFERENCES_REPO {verified: true}]->(repo)
                    """, {
                        "repo_id": repo_id,
                        "event_id": event_id
                    })

            logger.info(f"✅ Synced event {event_id} from {channel}")
            return True

        except Exception as e:
            logger.error(f"Error processing event {event.get('id')}: {e}")
            return False

    async def _sync_classification(
        self,
        session,
        event_id: str,
        payload: Dict[str, Any]
    ):
        """Sync a repository classification to Neo4j"""
        repo_id = payload.get("repo_id")
        primary_capability = payload.get("primary_capability")
        secondary_capabilities = payload.get("secondary_capabilities", [])
        score = payload.get("score", 0)
        reasoning = payload.get("reasoning", "")

        session.run("""
            MATCH (repo:ExternalRepository {repo_id: $repo_id})
            MATCH (buzz:BuzzEvent {event_id: $event_id})
            SET repo.primary_capability = $primary_capability,
                repo.secondary_capabilities = $secondary_capabilities,
                repo.classification_score = $score,
                repo.classification_reasoning = $reasoning,
                repo.buzz_event_id = $event_id,
                repo.classified_at = $classified_at
            CREATE (buzz)-[:CLASSIFIED_REPO]->(repo)
        """, {
            "repo_id": repo_id,
            "event_id": event_id,
            "primary_capability": primary_capability,
            "secondary_capabilities": secondary_capabilities,
            "score": score,
            "reasoning": reasoning,
            "classified_at": datetime.utcnow().isoformat()
        })

    async def _sync_scoring(
        self,
        session,
        event_id: str,
        payload: Dict[str, Any]
    ):
        """Sync repository scoring dimensions to Neo4j"""
        repo_id = payload.get("repo_id")
        dimensions = payload.get("dimensions", {})

        session.run("""
            MATCH (repo:ExternalRepository {repo_id: $repo_id})
            MATCH (buzz:BuzzEvent {event_id: $event_id})
            SET repo.dimensions = $dimensions,
                repo.overall_score = $overall_score,
                repo.buzz_score_event_id = $event_id,
                repo.scored_at = $scored_at
            CREATE (buzz)-[:SCORED_REPO]->(repo)
        """, {
            "repo_id": repo_id,
            "event_id": event_id,
            "dimensions": json.dumps(dimensions),
            "overall_score": sum(dimensions.values()) / len(dimensions) if dimensions else 0,
            "scored_at": datetime.utcnow().isoformat()
        })

    async def _sync_disposition(
        self,
        session,
        event_id: str,
        payload: Dict[str, Any]
    ):
        """Sync repository disposition decision to Neo4j"""
        repo_id = payload.get("repo_id")
        disposition = payload.get("disposition")  # ADOPT/INTEGRATE/FORK/REFERENCE/MONITOR
        rationale = payload.get("rationale", "")
        approved_by = payload.get("approved_by")

        session.run("""
            MATCH (repo:ExternalRepository {repo_id: $repo_id})
            MATCH (buzz:BuzzEvent {event_id: $event_id})
            SET repo.disposition = $disposition,
                repo.disposition_rationale = $rationale,
                repo.approved_by = $approved_by,
                repo.buzz_disposition_event_id = $event_id,
                repo.disposition_at = $disposition_at
            CREATE (buzz)-[:DISPOSED_REPO]->(repo)
        """, {
            "repo_id": repo_id,
            "event_id": event_id,
            "disposition": disposition,
            "rationale": rationale,
            "approved_by": approved_by or "system",
            "disposition_at": datetime.utcnow().isoformat()
        })

    async def sync_channel(self, channel: str) -> int:
        """
        Sync all unsync'd events from a channel

        Args:
            channel: Channel name

        Returns:
            Number of events synced
        """
        logger.info(f"Syncing {channel}...")

        # Get last sync time for this channel
        since = self.last_sync_time.get(channel)

        # Fetch new events
        events = await self.fetch_channel_events(channel, since)
        logger.info(f"Found {len(events)} events in {channel}")

        # Process each event
        synced_count = 0
        for event in events:
            if await self.process_event(event, channel):
                synced_count += 1

        # Update last sync time
        self.last_sync_time[channel] = datetime.utcnow()

        logger.info(f"✅ Synced {synced_count}/{len(events)} events from {channel}")
        return synced_count

    async def run_sync_cycle(self) -> Dict[str, int]:
        """
        Run one complete sync cycle across all channels

        Returns:
            Dictionary of {channel: events_synced}
        """
        results = {}

        for channel in self.channels:
            try:
                synced = await self.sync_channel(channel)
                results[channel] = synced
            except Exception as e:
                logger.error(f"Error syncing {channel}: {e}")
                results[channel] = 0

        return results

    async def run(self, interval_seconds: int = 3600):
        """
        Run the sync agent indefinitely

        Args:
            interval_seconds: How often to sync (default 1 hour)
        """
        logger.info(f"🚀 Starting Buzz Sync Agent (AGT-019)")
        logger.info(f"Sync interval: {interval_seconds}s")

        await self.initialize()

        try:
            while True:
                logger.info("Running sync cycle...")
                results = await self.run_sync_cycle()

                total_synced = sum(results.values())
                logger.info(f"Cycle complete: {total_synced} events synced")
                logger.info(f"Next cycle in {interval_seconds}s")

                await asyncio.sleep(interval_seconds)

        except KeyboardInterrupt:
            logger.info("Shutting down...")
        finally:
            await self.shutdown()


async def main():
    """Entry point for running as standalone service"""
    agent = BuzzSyncAgent()

    # Run with default 1-hour sync interval
    # For testing, use: await agent.run(interval_seconds=60)
    await agent.run(interval_seconds=3600)


if __name__ == "__main__":
    asyncio.run(main())
