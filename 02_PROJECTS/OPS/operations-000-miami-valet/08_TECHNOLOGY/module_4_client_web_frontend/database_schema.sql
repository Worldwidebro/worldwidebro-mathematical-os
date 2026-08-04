-- Database Schema: Client Web Frontend
CREATE TABLE IF NOT EXISTS ope_002_client_web_frontend (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'OPE-002',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
