-- Phase 1.1: Product Audit
-- Get venture summary with sector distribution, status, and pricing

SELECT 
  sector,
  COUNT(*) as count,
  COUNT(CASE WHEN status = 'active' THEN 1 END) as active_count,
  COUNT(CASE WHEN price_point > 0 THEN 1 END) as with_pricing,
  ROUND(AVG(price_point::numeric), 2) as avg_price,
  MAX(price_point::numeric) as max_price,
  COUNT(CASE WHEN product_description IS NOT NULL AND LENGTH(TRIM(product_description)) > 20 THEN 1 END) as documented
FROM ventures
GROUP BY sector
ORDER BY count DESC;
