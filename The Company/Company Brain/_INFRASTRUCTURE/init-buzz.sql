-- Buzz Database Initialization
-- Creates schema for Company Brain collaboration layer

-- Ensure postgres extensions are loaded
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Workspaces table
CREATE TABLE IF NOT EXISTS workspaces (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    visibility VARCHAR(20) DEFAULT 'private',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Channels table
CREATE TABLE IF NOT EXISTS channels (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    workspace_id UUID NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    visibility VARCHAR(20) DEFAULT 'private',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (workspace_id, name)
);

-- Events table (core collaboration data)
CREATE TABLE IF NOT EXISTS events (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    channel_id UUID NOT NULL REFERENCES channels(id) ON DELETE CASCADE,
    event_type VARCHAR(100) NOT NULL,
    author VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    payload JSONB,
    thread_id UUID REFERENCES events(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    signed_hash VARCHAR(255),
    signature VARCHAR(512)
);

-- Create indexes for performance
CREATE INDEX idx_events_channel_id ON events(channel_id);
CREATE INDEX idx_events_thread_id ON events(thread_id);
CREATE INDEX idx_events_created_at ON events(created_at DESC);
CREATE INDEX idx_events_author ON events(author);
CREATE INDEX idx_channels_workspace_id ON channels(workspace_id);

-- Members table
CREATE TABLE IF NOT EXISTS members (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    workspace_id UUID NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
    user_id VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'member',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (workspace_id, user_id)
);

-- Service keys (for agent authentication)
CREATE TABLE IF NOT EXISTS service_keys (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    workspace_id UUID NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
    service_name VARCHAR(255) NOT NULL,
    public_key VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    UNIQUE (workspace_id, service_name)
);

-- Create indexes on service keys
CREATE INDEX idx_service_keys_workspace_id ON service_keys(workspace_id);
CREATE INDEX idx_service_keys_active ON service_keys(active);

-- Audit log for compliance
CREATE TABLE IF NOT EXISTS audit_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_id UUID REFERENCES events(id) ON DELETE SET NULL,
    action VARCHAR(100) NOT NULL,
    actor VARCHAR(255) NOT NULL,
    changes JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_audit_log_created_at ON audit_log(created_at DESC);
CREATE INDEX idx_audit_log_event_id ON audit_log(event_id);

-- Insert default workspace
INSERT INTO workspaces (name, description, visibility)
VALUES ('company-brain', 'Company Brain collaboration workspace', 'private')
ON CONFLICT (name) DO NOTHING;

-- Insert default channels
DO $$
DECLARE
    workspace_id UUID;
BEGIN
    SELECT id INTO workspace_id FROM workspaces WHERE name = 'company-brain' LIMIT 1;

    IF workspace_id IS NOT NULL THEN
        INSERT INTO channels (workspace_id, name, description)
        VALUES
            (workspace_id, 'repo-classification', 'AGT-013 repository classification findings'),
            (workspace_id, 'repo-scoring', 'AGT-014 repository scoring results'),
            (workspace_id, 'repo-disposition', 'AGT-015 disposition decisions (ADOPT/INTEGRATE/FORK/REFERENCE/MONITOR)'),
            (workspace_id, 'repo-adoption-pipeline', 'AGT-017 adoption progress and testing results'),
            (workspace_id, 'general', 'General discussion and announcements')
        ON CONFLICT (workspace_id, name) DO NOTHING;
    END IF;
END $$;
