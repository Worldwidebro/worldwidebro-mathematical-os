-- AI BOSS OS PostgreSQL Schema
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS tenants (id UUID PRIMARY KEY, name VARCHAR(255), slug VARCHAR(100) UNIQUE);
CREATE TABLE IF NOT EXISTS users (id UUID PRIMARY KEY, tenant_id UUID, email VARCHAR(255) UNIQUE, role VARCHAR(50));
CREATE TABLE IF NOT EXISTS ventures (id UUID PRIMARY KEY, tenant_id UUID, name VARCHAR(255), sector VARCHAR(100));
CREATE TABLE IF NOT EXISTS agents (id UUID PRIMARY KEY, venture_id UUID, name VARCHAR(255), type VARCHAR(100), status VARCHAR(50));
CREATE TABLE IF NOT EXISTS tasks (id UUID PRIMARY KEY, venture_id UUID, agent_id UUID, title VARCHAR(500), status VARCHAR(50));
CREATE TABLE IF NOT EXISTS knowledge (id UUID PRIMARY KEY, venture_id UUID, title VARCHAR(500), content TEXT);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_ventures_sector ON ventures(sector);
CREATE INDEX IF NOT EXISTS idx_agents_status ON agents(status);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);
