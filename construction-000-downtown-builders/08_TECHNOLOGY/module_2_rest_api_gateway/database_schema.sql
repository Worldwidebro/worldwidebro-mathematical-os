-- Database Schema: REST API Gateway
CREATE TABLE IF NOT EXISTS con_021_rest_api_gateway (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'CON-021',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
