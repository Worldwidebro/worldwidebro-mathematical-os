-- Database Schema: REST API Gateway
CREATE TABLE IF NOT EXISTS was_001_rest_api_gateway (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'WAS-001',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
