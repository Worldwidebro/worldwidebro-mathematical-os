-- Database Schema: Client Web Frontend
CREATE TABLE IF NOT EXISTS con_022_client_web_frontend (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'CON-022',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
