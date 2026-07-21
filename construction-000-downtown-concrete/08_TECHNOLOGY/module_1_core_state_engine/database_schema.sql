-- Database Schema: Core State Engine
CREATE TABLE IF NOT EXISTS con_022_core_state_engine (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'CON-022',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
