-- Database Schema: Database Schema & Models
CREATE TABLE IF NOT EXISTS tec_063_database_schema_and_models (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'TEC-063',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
