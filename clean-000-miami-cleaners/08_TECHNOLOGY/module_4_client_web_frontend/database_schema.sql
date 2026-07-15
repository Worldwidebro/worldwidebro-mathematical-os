-- Database Schema: Client Web Frontend
CREATE TABLE IF NOT EXISTS cle_001_client_web_frontend (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'CLE-001',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
