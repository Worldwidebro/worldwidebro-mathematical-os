-- Database Schema: Database Schema & Models
CREATE TABLE IF NOT EXISTS was_001_database_schema_and_models (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'WAS-001',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
