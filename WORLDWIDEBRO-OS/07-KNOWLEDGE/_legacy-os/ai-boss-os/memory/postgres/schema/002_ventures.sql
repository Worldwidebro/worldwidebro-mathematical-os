-- Venture snapshot table (materialized from entity registry + events)

CREATE TABLE IF NOT EXISTS ventures (
    venture_id       TEXT PRIMARY KEY,
    name             TEXT NOT NULL,
    sector_code      TEXT NOT NULL,
    stage            TEXT,
    status           TEXT,
    repository_url   TEXT,
    github_slug      TEXT,
    metadata         JSONB NOT NULL DEFAULT '{}',
    updated_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ventures_sector_code ON ventures (sector_code);

CREATE TABLE IF NOT EXISTS sectors (
    sector_code      TEXT PRIMARY KEY,
    name             TEXT NOT NULL,
    economic_layer   TEXT,
    agent_id         TEXT,
    dispatch_status  TEXT
);
