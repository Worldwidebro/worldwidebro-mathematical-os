-- AI Boss OS — immutable event log (source of truth per CONTRACTS-SUMMARY)

CREATE TABLE IF NOT EXISTS event_log (
    event_id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_type       TEXT NOT NULL,
    source           TEXT NOT NULL,
    venture_id       TEXT,
    correlation_id   UUID,
    payload          JSONB NOT NULL DEFAULT '{}',
    created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_event_log_venture_id ON event_log (venture_id);
CREATE INDEX IF NOT EXISTS idx_event_log_type ON event_log (event_type);
CREATE INDEX IF NOT EXISTS idx_event_log_created_at ON event_log (created_at DESC);

CREATE TABLE IF NOT EXISTS agent_state_history (
    id               BIGSERIAL PRIMARY KEY,
    agent_id         TEXT NOT NULL,
    venture_id       TEXT,
    state            JSONB NOT NULL DEFAULT '{}',
    created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_agent_state_agent_id ON agent_state_history (agent_id);

CREATE TABLE IF NOT EXISTS venture_state_history (
    id               BIGSERIAL PRIMARY KEY,
    venture_id       TEXT NOT NULL,
    state            JSONB NOT NULL DEFAULT '{}',
    created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_venture_state_venture_id ON venture_state_history (venture_id);

CREATE TABLE IF NOT EXISTS execution_log (
    id               BIGSERIAL PRIMARY KEY,
    workflow_id      TEXT,
    venture_id       TEXT,
    status           TEXT NOT NULL,
    payload          JSONB NOT NULL DEFAULT '{}',
    error_message    TEXT,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
