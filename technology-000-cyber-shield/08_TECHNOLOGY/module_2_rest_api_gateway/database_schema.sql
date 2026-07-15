-- Database Schema: REST API Gateway
CREATE TABLE IF NOT EXISTS tec_063_rest_api_gateway (
  id SERIAL PRIMARY KEY,
  venture_id VARCHAR(50) DEFAULT 'TEC-063',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
