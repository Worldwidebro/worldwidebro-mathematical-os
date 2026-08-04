-- Database Schema: Core State Engine
CREATE TABLE IF NOT EXISTS cle_001_core_state_engine (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'CLE-001',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
