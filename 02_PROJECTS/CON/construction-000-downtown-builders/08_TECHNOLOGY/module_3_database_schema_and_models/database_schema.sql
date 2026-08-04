-- Database Schema: Database Schema & Models
CREATE TABLE IF NOT EXISTS con_021_database_schema_and_models (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'CON-021',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
