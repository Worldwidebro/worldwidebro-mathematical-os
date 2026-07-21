-- Database Schema: Database Schema & Models
CREATE TABLE IF NOT EXISTS con_022_database_schema_and_models (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'CON-022',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
