-- Database Schema: REST API Gateway
CREATE TABLE IF NOT EXISTS con_022_rest_api_gateway (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'CON-022',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
