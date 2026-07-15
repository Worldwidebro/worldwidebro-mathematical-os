-- Database Schema: Database Schema & Models
CREATE TABLE IF NOT EXISTS ope_002_database_schema_and_models (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'OPE-002',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
