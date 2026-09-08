"""
Buzz Integration Module for Company Brain
Provides MCP tools for publishing events, reading channels, and syncing to Neo4j

Authority: Collaboration Control Plane (CP-028)
Framework: FastMCP + Buzz Relay
"""

import json
import requests
from typing import Optional, List, Dict, Any
from datetime import datetime
from pathlib import Path
import hmac
import hashlib

# Buzz API configuration
BUZZ_RELAY_URL = "http://100.87.214.70:8080"
BUZZ_API_VERSION = "v1"
BUZZ_WORKSPACE = "company-brain"


def sign_event(payload: Dict[str, Any], secret_key: str) -> str:
    """
    Sign a Buzz event for authentication

    Uses HMAC-SHA256 for cryptographic integrity
    """
    payload_json = json.dumps(payload, sort_keys=True)
    signature = hmac.new(
        secret_key.encode(),
        payload_json.encode(),
        hashlib.sha256
    ).hexdigest()
    return signature


def buzz_publish_event(
    channel: str,
    event_type: str,
    payload: Dict[str, Any],
    thread_id: Optional[str] = None,
    author: str = "agent",
    secret_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Publish an event to a Buzz channel

    This is the primary mechanism for agents to post findings to Buzz.
    Enables human-AI collaboration with full audit trails.

    Args:
        channel: Buzz channel name (e.g., 'repo-classification')
        event_type: Type of event (e.g., 'repo_classified', 'human_review')
        payload: Event data as JSON object
        thread_id: If replying to an existing event, reference its ID
        author: Who published the event (agent name or user)
        secret_key: Secret key for signing (from Bitwarden or env)

    Returns:
        Event metadata: {id, channel, created_at, signature}

    Example:
        >>> buzz_publish_event(
        ...     channel='repo-classification',
        ...     event_type='repo_classified',
        ...     payload={
        ...         'repo_id': 'EXT-REPO-00042',
        ...         'primary_capability': 'CAP-027',
        ...         'score': 78,
        ...         'reasoning': 'Fits CAP-027 due to X, Y, Z'
        ...     },
        ...     author='AGT-013'
        ... )
    """
    try:
        # Build event
        event = {
            "event_type": event_type,
            "author": author,
            "payload": payload,
            "timestamp": datetime.utcnow().isoformat()
        }

        if thread_id:
            event["thread_id"] = thread_id

        # Sign if secret key provided
        if secret_key:
            event["signature"] = sign_event(event, secret_key)

        # POST to Buzz relay
        url = f"{BUZZ_RELAY_URL}/api/{BUZZ_API_VERSION}/workspaces/{BUZZ_WORKSPACE}/channels/{channel}/events"

        response = requests.post(
            url,
            json=event,
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        if response.status_code in [200, 201]:
            result = response.json()
            return {
                "status": "success",
                "event_id": result.get("id"),
                "channel": channel,
                "author": author,
                "created_at": event["timestamp"],
                "signature": event.get("signature"),
                "buzz_url": f"{BUZZ_RELAY_URL}/channels/{channel}/events/{result.get('id')}"
            }
        else:
            return {
                "status": "error",
                "error": f"Buzz API returned {response.status_code}",
                "response": response.text
            }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "channel": channel
        }


def buzz_read_channel(
    channel: str,
    limit: int = 50,
    thread_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Read recent events from a Buzz channel

    Used by personas (repo-advisor, repo-deep-dive) to monitor agent activity
    and provide human feedback.

    Args:
        channel: Channel name
        limit: Max events to return (default 50)
        thread_id: If specified, read only this thread

    Returns:
        List of events with full metadata and audit trails

    Example:
        >>> buzz_read_channel('repo-classification', limit=10)
    """
    try:
        if thread_id:
            url = f"{BUZZ_RELAY_URL}/api/{BUZZ_API_VERSION}/workspaces/{BUZZ_WORKSPACE}/channels/{channel}/threads/{thread_id}"
        else:
            url = f"{BUZZ_RELAY_URL}/api/{BUZZ_API_VERSION}/workspaces/{BUZZ_WORKSPACE}/channels/{channel}/events"

        response = requests.get(
            url,
            params={"limit": limit},
            timeout=10
        )

        if response.status_code == 200:
            events = response.json()
            return {
                "status": "success",
                "channel": channel,
                "event_count": len(events) if isinstance(events, list) else 1,
                "events": events,
                "timestamp": datetime.utcnow().isoformat()
            }
        else:
            return {
                "status": "error",
                "error": f"Buzz API returned {response.status_code}"
            }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }


def buzz_sync_to_neo4j(
    channel: str,
    event_id: str,
    neo4j_uri: str = "bolt://100.87.214.70:7687",
    neo4j_user: str = "neo4j",
    neo4j_password: str = "changeme"
) -> Dict[str, Any]:
    """
    Sync a completed Buzz conversation thread to Neo4j knowledge graph

    This bridges human-AI collaboration (Buzz) with the knowledge graph (Neo4j).
    Creates audit trail nodes and links final classifications/decisions.

    Merges:
    - Final classification/score/disposition
    - Audit trail (conversation thread)
    - Approvals/overrides from humans

    Args:
        channel: Buzz channel to sync from
        event_id: Event ID to sync (marks completion point)
        neo4j_uri: Neo4j bolt endpoint
        neo4j_user: Neo4j username
        neo4j_password: Neo4j password

    Returns:
        Merge result with node properties and edge references

    Example:
        >>> buzz_sync_to_neo4j(
        ...     channel='repo-classification',
        ...     event_id='550e8400-e29b-41d4-a716-446655440000'
        ... )
    """
    try:
        from neo4j import GraphDatabase

        # Read Buzz event thread
        thread_data = buzz_read_channel(channel, limit=100, thread_id=event_id)

        if thread_data["status"] != "success":
            return {
                "status": "error",
                "error": "Failed to read Buzz thread"
            }

        # Connect to Neo4j
        driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

        # Process each event in thread
        merged_count = 0
        created_at = datetime.utcnow().isoformat()

        for event in thread_data.get("events", []):
            with driver.session() as session:
                # Create or merge Buzz Event node
                result = session.run("""
                    MERGE (e:BuzzEvent {event_id: $event_id})
                    SET e.channel = $channel,
                        e.event_type = $event_type,
                        e.author = $author,
                        e.content = $content,
                        e.timestamp = $timestamp,
                        e.signature = $signature,
                        e.synced_at = $synced_at
                    RETURN e
                """, {
                    "event_id": event.get("id"),
                    "channel": channel,
                    "event_type": event.get("event_type"),
                    "author": event.get("author"),
                    "content": json.dumps(event.get("payload", {})),
                    "timestamp": event.get("timestamp"),
                    "signature": event.get("signature"),
                    "synced_at": created_at
                })

                merged_count += result.consume().counters.nodes_created or 0

                # If this event references a repository, create relationship
                payload = event.get("payload", {})
                repo_id = payload.get("repo_id")

                if repo_id:
                    session.run("""
                        MATCH (repo:ExternalRepository {repo_id: $repo_id})
                        MATCH (buzz:BuzzEvent {event_id: $event_id})
                        MERGE (buzz)-[:REFERENCES_REPO]->(repo)
                    """, {
                        "repo_id": repo_id,
                        "event_id": event.get("id")
                    })

        driver.close()

        return {
            "status": "success",
            "channel": channel,
            "event_id": event_id,
            "nodes_merged": merged_count,
            "events_processed": len(thread_data.get("events", [])),
            "synced_at": created_at
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }


def buzz_update_classification(
    repo_id: str,
    channel: str,
    event_id: str,
    primary_capability: str,
    secondary_capabilities: List[str],
    score: int,
    reasoning: str,
    author: str = "AGT-013"
) -> Dict[str, Any]:
    """
    Publish an updated repository classification to Buzz

    Called when an agent revises a classification based on human feedback
    in Buzz. Creates a threaded reply.

    Args:
        repo_id: Repository ID being classified
        channel: 'repo-classification' or similar
        event_id: ID of the original classification to reply to
        primary_capability: Main capability (e.g., 'CAP-027')
        secondary_capabilities: List of secondary capabilities
        score: Confidence score (0-100)
        reasoning: Explanation for the classification
        author: Agent making the update (default AGT-013)

    Returns:
        Updated event metadata
    """
    payload = {
        "repo_id": repo_id,
        "primary_capability": primary_capability,
        "secondary_capabilities": secondary_capabilities,
        "score": score,
        "reasoning": reasoning,
        "classification_type": "updated",
        "response_to": event_id
    }

    return buzz_publish_event(
        channel=channel,
        event_type="repo_classified_updated",
        payload=payload,
        thread_id=event_id,
        author=author
    )


def buzz_create_agent_key(
    agent_name: str,
    workspace: str = BUZZ_WORKSPACE
) -> Dict[str, Any]:
    """
    Create a service key for an agent to authenticate with Buzz

    Service keys enable agents to publish events with cryptographic signatures.

    Args:
        agent_name: Agent identifier (e.g., 'AGT-013')
        workspace: Workspace name (default 'company-brain')

    Returns:
        Service key with public/private components
    """
    try:
        url = f"{BUZZ_RELAY_URL}/api/{BUZZ_API_VERSION}/workspaces/{workspace}/service-keys"

        response = requests.post(
            url,
            json={"service_name": agent_name},
            timeout=10
        )

        if response.status_code in [200, 201]:
            key_data = response.json()
            return {
                "status": "success",
                "agent": agent_name,
                "public_key": key_data.get("public_key"),
                "secret_key": key_data.get("secret_key"),
                "note": "Store secret_key in Bitwarden or secure vault"
            }
        else:
            return {
                "status": "error",
                "error": f"Failed to create key: {response.status_code}"
            }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }


# Export all functions for MCP registration
__all__ = [
    "buzz_publish_event",
    "buzz_read_channel",
    "buzz_sync_to_neo4j",
    "buzz_update_classification",
    "buzz_create_agent_key",
    "sign_event"
]
