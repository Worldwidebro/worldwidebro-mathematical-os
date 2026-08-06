"""Apple Notes ingestion agent with LangGraph orchestration."""

import hashlib
import json
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4

from langgraph.graph import StateGraph
from pydantic import BaseModel

from anthropic import Anthropic
from supabase import create_client
from neo4j import GraphDatabase
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger(__name__)

# Initialize clients
SUPABASE_URL = os.getenv("SUPABASE_URL", "http://localhost:54321")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "ventures2026")
neo4j_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
qdrant_client = QdrantClient(QDRANT_URL)

claude_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


@dataclass
class NoteState:
    """State for note ingestion workflow."""
    note_id: str
    content: str
    venture_id: str | None = None
    note_type: str | None = None  # strategic, operational, learning
    entities: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    dispatch_agents: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())


class ClassifyNoteResponse(BaseModel):
    """Claude's classification of a note."""
    venture_id: str | None = None
    note_type: str  # strategic, operational, learning, other
    entities: list[str]
    actions: list[str]


def ingest_note(state: NoteState) -> NoteState:
    """Parse and validate note content."""
    try:
        if not state.content or len(state.content.strip()) < 10:
            state.errors.append("Note content too short or empty")
            return state
        logger.info(f"Ingesting note {state.note_id}")
    except Exception as e:
        state.errors.append(f"Ingestion error: {str(e)}")
        logger.error(f"Ingestion failed: {e}")
    return state


def classify_note(state: NoteState) -> NoteState:
    """Use Claude to classify note: venture, type, entities, actions."""
    try:
        prompt = f"""Analyze this Apple note and extract intelligence.

Content:
{state.content}

Return JSON with:
- venture_id: which venture (LT-001, FIN-042, etc.) or null
- note_type: 'strategic' (portfolio/direction), 'operational' (daily execution), 'learning' (insights/outcomes), or 'other'
- entities: [list of key entities: companies, people, products, metrics]
- actions: [list of suggested actions]

Return valid JSON only."""

        response = claude_client.messages.create(
            model="claude-opus-5",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )

        try:
            parsed = json.loads(response.content[0].text)
            classification = ClassifyNoteResponse(**parsed)
            state.venture_id = classification.venture_id
            state.note_type = classification.note_type
            state.entities = classification.entities
            state.actions = classification.actions
            logger.info(f"Classified note as {state.note_type} for {state.venture_id}")
        except (json.JSONDecodeError, ValueError) as e:
            state.errors.append(f"Classification parse error: {str(e)}")
            logger.error(f"Failed to parse Claude response: {e}")
    except Exception as e:
        state.errors.append(f"Classification error: {str(e)}")
        logger.error(f"Classification failed: {e}")
    return state


def create_supabase_record(state: NoteState) -> NoteState:
    """Insert note into apple_notes_inbox table."""
    try:
        record = {
            "id": state.note_id,
            "content": state.content,
            "venture_id": state.venture_id,
            "note_type": state.note_type,
            "entities": state.entities,
            "actions": state.actions,
            "created_at": state.created_at,
            "processed": False
        }

        supabase.table("apple_notes_inbox").insert(record).execute()
        logger.info(f"Supabase record created: {state.note_id}")
    except Exception as e:
        state.errors.append(f"Supabase insert error: {str(e)}")
        logger.error(f"Supabase insert failed: {e}")
    return state


def update_neo4j(state: NoteState) -> NoteState:
    """Create Neo4j nodes and relationships for the note."""
    try:
        with neo4j_driver.session() as session:
            # Create note node
            session.run("""
                MERGE (n:Note {id: $note_id})
                SET n.content = $content, n.type = $note_type, n.created_at = $created_at
            """, note_id=state.note_id, content=state.content[:200], note_type=state.note_type, created_at=state.created_at)

            # Link to venture if identified
            if state.venture_id:
                session.run("""
                    MATCH (n:Note {id: $note_id})
                    MERGE (v:Venture {id: $venture_id})
                    MERGE (n)-[:FOR_VENTURE]->(v)
                """, note_id=state.note_id, venture_id=state.venture_id)

            # Create entity nodes and relationships
            for entity in state.entities:
                session.run("""
                    MATCH (n:Note {id: $note_id})
                    MERGE (e:Entity {name: $entity})
                    MERGE (n)-[:MENTIONS]->(e)
                """, note_id=state.note_id, entity=entity)

            logger.info(f"Neo4j updated for note {state.note_id}")
    except Exception as e:
        state.errors.append(f"Neo4j update error: {str(e)}")
        logger.error(f"Neo4j update failed: {e}")
    return state


def embed_in_qdrant(state: NoteState) -> NoteState:
    """Embed note and store in Qdrant for semantic search."""
    try:
        # ponytail: placeholder embedding, use sentence-transformers or Claude embeddings API in production
        embedding = [0.1] * 1536  # 1536-dim vector

        # Use a hash of note_id for Qdrant point ID (must be integer)
        point_id = int(hashlib.md5(state.note_id.encode()).hexdigest(), 16) % (2**31 - 1)

        point = PointStruct(
            id=point_id,
            vector=embedding,
            payload={
                "note_id": state.note_id,
                "venture_id": state.venture_id,
                "note_type": state.note_type,
                "content": state.content[:500],
                "entities": state.entities,
                "created_at": state.created_at
            }
        )

        qdrant_client.upsert(
            collection_name="apple_notes",
            points=[point]
        )
        logger.info(f"Qdrant embedding stored for note {state.note_id}")
    except Exception as e:
        state.errors.append(f"Qdrant embedding error: {str(e)}")
        logger.error(f"Qdrant embedding failed: {e}")
    return state


def dispatch_to_agents(state: NoteState) -> NoteState:
    """Route to specialized agents based on note type."""
    try:
        routing_map = {
            "strategic": ["ArchitectureAgent", "PortfolioAgent"],
            "operational": ["ExecutionAgent", "MonitorAgent"],
            "learning": ["ResearchAgent", "InsightAgent"],
            "other": []
        }

        state.dispatch_agents = routing_map.get(state.note_type, [])
        logger.info(f"Dispatching note {state.note_id} to {state.dispatch_agents}")
    except Exception as e:
        state.errors.append(f"Dispatch error: {str(e)}")
        logger.error(f"Dispatch failed: {e}")
    return state


def sync_to_obsidian(state: NoteState) -> NoteState:
    """Create/update Obsidian note in venture folder."""
    try:
        if not state.venture_id:
            logger.info(f"Skipping Obsidian sync for note {state.note_id} (no venture identified)")
            return state

        # ponytail: simplified - production would write actual markdown file
        obsidian_path = f"/Users/acebless/Documents/02_PROJECTS/{state.venture_id}/apple-notes/{state.note_id}.md"
        logger.info(f"Obsidian sync prepared at {obsidian_path}")
    except Exception as e:
        state.errors.append(f"Obsidian sync error: {str(e)}")
        logger.error(f"Obsidian sync failed: {e}")
    return state


def log_learning(state: NoteState) -> NoteState:
    """Log processing outcome for learning loop."""
    try:
        learning_record = {
            "note_id": state.note_id,
            "venture_predicted": state.venture_id,
            "note_type_predicted": state.note_type,
            "agents_dispatched": state.dispatch_agents,
            "entities_extracted": len(state.entities),
            "actions_identified": len(state.actions),
            "error_count": len(state.errors),
            "processing_time": datetime.utcnow().isoformat()
        }

        supabase.table("apple_notes_learning").insert(learning_record).execute()
        logger.info(f"Learning logged: {len(state.entities)} entities, {len(state.actions)} actions, {len(state.errors)} errors")
    except Exception as e:
        logger.error(f"Learning log error: {str(e)}")

    return state


def build_agent():
    """Build LangGraph workflow for note ingestion."""
    workflow = StateGraph(NoteState)

    # Add nodes
    workflow.add_node("ingest", ingest_note)
    workflow.add_node("classify", classify_note)
    workflow.add_node("supabase", create_supabase_record)
    workflow.add_node("neo4j", update_neo4j)
    workflow.add_node("qdrant", embed_in_qdrant)
    workflow.add_node("dispatch", dispatch_to_agents)
    workflow.add_node("obsidian", sync_to_obsidian)
    workflow.add_node("learning", log_learning)

    # Sequential pipeline
    workflow.add_edge("ingest", "classify")
    workflow.add_edge("classify", "supabase")
    workflow.add_edge("supabase", "neo4j")
    workflow.add_edge("neo4j", "qdrant")
    workflow.add_edge("qdrant", "dispatch")
    workflow.add_edge("dispatch", "obsidian")
    workflow.add_edge("obsidian", "learning")

    workflow.set_entry_point("ingest")
    workflow.set_finish_point("learning")

    return workflow.compile()


async def process_note(content: str, note_id: str | None = None) -> NoteState:
    """Process a single note end-to-end."""
    note_id = note_id or str(uuid4())
    state = NoteState(note_id=note_id, content=content)

    agent = build_agent()
    final_state = agent.invoke(state)

    if final_state.errors:
        logger.warning(f"Note {note_id} completed with {len(final_state.errors)} error(s)")
    else:
        logger.info(f"Note {note_id} processed successfully")

    return final_state


if __name__ == "__main__":
    import asyncio
    import hashlib

    test_note = """
    Worldwidebro needs to focus on LT-005 medical courier dispatch first.
    Current blocker: Supabase auth not wired. Driver portal UI ready.
    Action: Wire REST API by Friday. Target $8K MRR within 2 weeks.
    """

    result = asyncio.run(process_note(test_note))
    print(f"✓ Processed note: {result.note_id}")
    print(f"  Venture: {result.venture_id}, Type: {result.note_type}")
    print(f"  Entities: {result.entities}")
    print(f"  Actions: {result.actions}")
    print(f"  Errors: {len(result.errors)}")
