-- Database Schema: Core State Engine
CREATE TABLE IF NOT EXISTS tec_063_core_state_engine (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'TEC-063',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
