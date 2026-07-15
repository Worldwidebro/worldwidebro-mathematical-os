-- Database Schema: REST API Gateway
CREATE TABLE IF NOT EXISTS ope_002_rest_api_gateway (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'OPE-002',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
