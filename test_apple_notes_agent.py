"""Unit tests for Apple Notes ingestion agent."""

import pytest
from unittest.mock import Mock, patch, MagicMock
from apple_notes_agent import (
    NoteState,
    ingest_note,
    classify_note,
    create_supabase_record,
    update_neo4j,
    embed_in_qdrant,
    dispatch_to_agents,
    sync_to_obsidian,
    log_learning,
    build_agent,
)


class TestNoteIngestion:
    """Test ingest_note function."""

    def test_ingest_valid_note(self):
        """Valid note should pass ingestion."""
        state = NoteState(note_id="test-001", content="This is a valid note with enough content.")
        result = ingest_note(state)
        assert len(result.errors) == 0
        assert result.note_id == "test-001"

    def test_ingest_short_note(self):
        """Note too short should be rejected."""
        state = NoteState(note_id="test-002", content="Short")
        result = ingest_note(state)
        assert len(result.errors) == 1
        assert "too short" in result.errors[0].lower()

    def test_ingest_empty_note(self):
        """Empty note should be rejected."""
        state = NoteState(note_id="test-003", content="")
        result = ingest_note(state)
        assert len(result.errors) == 1


class TestClassification:
    """Test classify_note function."""

    @patch("apple_notes_agent.claude_client")
    def test_classify_strategic_note(self, mock_claude_client):
        """Strategic note should be classified correctly."""
        mock_response = Mock()
        mock_response.content = [
            Mock(text='{"venture_id": "LT-005", "note_type": "strategic", "entities": ["dispatch", "revenue"], "actions": ["wire API", "launch"]}')
        ]
        mock_claude_client.messages.create.return_value = mock_response

        state = NoteState(
            note_id="test-004",
            content="LT-005 medical courier needs dispatch platform. Target $8K MRR."
        )
        result = classify_note(state)

        assert result.venture_id == "LT-005"
        assert result.note_type == "strategic"
        assert "dispatch" in result.entities
        assert len(result.actions) > 0

    @patch("apple_notes_agent.claude_client")
    def test_classify_operational_note(self, mock_claude_client):
        """Operational note should be classified correctly."""
        mock_response = Mock()
        mock_response.content = [
            Mock(
                text='{"venture_id": "CON-001", "note_type": "operational", "entities": ["invoice", "payment"], "actions": ["process invoice"]}'
            )
        ]
        mock_claude_client.messages.create.return_value = mock_response

        state = NoteState(
            note_id="test-005",
            content="Process invoice for today's deliveries. Check Stripe webhook status."
        )
        result = classify_note(state)

        assert result.venture_id == "CON-001"
        assert result.note_type == "operational"

    @patch("apple_notes_agent.claude_client")
    def test_classify_invalid_json_response(self, mock_claude_client):
        """Should handle malformed Claude response gracefully."""
        mock_response = Mock()
        mock_response.content = [Mock(text="Invalid JSON")]
        mock_claude_client.messages.create.return_value = mock_response

        state = NoteState(note_id="test-006", content="A note that Claude responds poorly to. This has enough text to pass ingestion.")
        result = classify_note(state)

        assert len(result.errors) > 0
        assert "parse error" in result.errors[0].lower()


class TestSupabaseRecord:
    """Test create_supabase_record function."""

    @patch("apple_notes_agent.supabase")
    def test_create_record_success(self, mock_supabase):
        """Should insert record into Supabase."""
        mock_table = Mock()
        mock_supabase.table.return_value = mock_table
        mock_table.insert.return_value.execute.return_value = Mock(data=[{"id": "test-007"}])

        state = NoteState(
            note_id="test-007",
            content="Test note",
            venture_id="LT-001",
            note_type="strategic",
            entities=["entity1"],
            actions=["action1"],
        )

        result = create_supabase_record(state)

        assert len(result.errors) == 0
        mock_table.insert.assert_called_once()


class TestNeo4jUpdate:
    """Test update_neo4j function."""

    @patch("apple_notes_agent.neo4j_driver")
    def test_create_note_node(self, mock_driver):
        """Should create Note node in Neo4j."""
        mock_session = Mock()
        mock_driver.session.return_value.__enter__.return_value = mock_session

        state = NoteState(
            note_id="test-008",
            content="Test note for Neo4j integration and testing purposes",
            venture_id="LT-001",
            note_type="strategic",
            entities=["entity1"],
        )

        result = update_neo4j(state)

        # Should call run() at least once
        assert mock_session.run.call_count >= 1
        assert len(result.errors) == 0


class TestQdrantEmbedding:
    """Test embed_in_qdrant function."""

    @patch("apple_notes_agent.qdrant_client")
    def test_embed_note(self, mock_qdrant):
        """Should embed and store note in Qdrant."""
        mock_qdrant.upsert.return_value = None

        state = NoteState(
            note_id="test-009",
            content="Note to embed in vector database for semantic search",
            venture_id="FIN-042",
            note_type="learning",
            entities=["revenue", "customer"],
        )

        result = embed_in_qdrant(state)

        assert len(result.errors) == 0
        mock_qdrant.upsert.assert_called_once()


class TestAgentDispatch:
    """Test dispatch_to_agents function."""

    def test_dispatch_strategic_note(self):
        """Strategic note should route to Architecture + Portfolio agents."""
        state = NoteState(
            note_id="test-010", content="Strategic decision with enough content for validation", note_type="strategic"
        )
        result = dispatch_to_agents(state)

        assert "ArchitectureAgent" in result.dispatch_agents
        assert "PortfolioAgent" in result.dispatch_agents

    def test_dispatch_operational_note(self):
        """Operational note should route to Execution + Monitor agents."""
        state = NoteState(
            note_id="test-011", content="Daily task that needs to be executed tomorrow", note_type="operational"
        )
        result = dispatch_to_agents(state)

        assert "ExecutionAgent" in result.dispatch_agents
        assert "MonitorAgent" in result.dispatch_agents

    def test_dispatch_learning_note(self):
        """Learning note should route to Research + Insight agents."""
        state = NoteState(note_id="test-012", content="Learned something important today about the business", note_type="learning")
        result = dispatch_to_agents(state)

        assert "ResearchAgent" in result.dispatch_agents
        assert "InsightAgent" in result.dispatch_agents

    def test_dispatch_unknown_type(self):
        """Unknown type should route to no agents."""
        state = NoteState(note_id="test-013", content="Unknown type content that does not fit standard categories", note_type="other")
        result = dispatch_to_agents(state)

        assert len(result.dispatch_agents) == 0


class TestObsidianSync:
    """Test sync_to_obsidian function."""

    def test_sync_with_venture(self):
        """Should prepare Obsidian sync when venture identified."""
        state = NoteState(
            note_id="test-014", content="Note with venture identifier for testing", venture_id="LT-005"
        )
        result = sync_to_obsidian(state)

        assert len(result.errors) == 0

    def test_skip_sync_without_venture(self):
        """Should skip Obsidian sync when no venture identified."""
        state = NoteState(note_id="test-015", content="Note without venture identifier for testing purposes")
        result = sync_to_obsidian(state)

        assert len(result.errors) == 0


class TestLearningLog:
    """Test log_learning function."""

    @patch("apple_notes_agent.supabase")
    def test_log_success(self, mock_supabase):
        """Should log processing outcome."""
        mock_table = Mock()
        mock_supabase.table.return_value = mock_table
        mock_table.insert.return_value.execute.return_value = None

        state = NoteState(
            note_id="test-016",
            content="Note to be logged for learning",
            venture_id="LT-001",
            note_type="strategic",
            entities=["entity1", "entity2"],
            actions=["action1"],
            errors=[],
        )

        result = log_learning(state)

        assert len(result.errors) == 0
        mock_supabase.table.assert_called()


class TestIntegration:
    """Integration tests for full pipeline."""

    @patch("apple_notes_agent.claude_client")
    @patch("apple_notes_agent.supabase")
    @patch("apple_notes_agent.neo4j_driver")
    @patch("apple_notes_agent.qdrant_client")
    def test_full_pipeline(self, mock_qdrant, mock_driver, mock_supabase, mock_claude_client):
        """Full pipeline should process note end-to-end."""
        # Mock Claude response
        mock_claude_response = Mock()
        mock_claude_response.content = [
            Mock(
                text='{"venture_id": "LT-005", "note_type": "strategic", "entities": ["dispatch"], "actions": ["wire API"]}'
            )
        ]
        mock_claude_client.messages.create.return_value = mock_claude_response

        # Mock Supabase
        mock_table = Mock()
        mock_supabase.table.return_value = mock_table
        mock_table.insert.return_value.execute.return_value = None

        # Mock Neo4j
        mock_session = Mock()
        mock_driver.session.return_value.__enter__.return_value = mock_session

        # Mock Qdrant
        mock_qdrant.upsert.return_value = None

        # Build and run agent
        agent = build_agent()
        state = NoteState(
            note_id="integration-test",
            content="Test note for LT-005 medical courier dispatch system integration"
        )
        result = agent.invoke(state)

        # Verify outcome
        assert result.venture_id == "LT-005"
        assert result.note_type == "strategic"
        assert len(result.entities) > 0
        assert len(result.dispatch_agents) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
