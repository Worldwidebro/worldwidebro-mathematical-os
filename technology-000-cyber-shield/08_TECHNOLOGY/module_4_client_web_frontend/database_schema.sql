-- Database Schema: Client Web Frontend
CREATE TABLE IF NOT EXISTS tec_063_client_web_frontend (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'TEC-063',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
