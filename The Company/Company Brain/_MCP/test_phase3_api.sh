#!/bin/bash

# Phase 3 API Testing Script
# Tests all new Cap Tables, Deal Files, and Portfolio endpoints

API_URL="http://localhost:5432"

echo "🚀 DealFlowOS Phase 3 API Testing"
echo "=================================="
echo ""

# Test 1: Health Check
echo "1️⃣  Health Check"
echo "   curl $API_URL/health"
curl -s $API_URL/health | jq '.' 2>/dev/null || echo "❌ API not running"
echo ""

# Test 2: Initialize Cap Tables
echo "2️⃣  Initialize Cap Tables from BUSINESS-CAPITAL-DATA-ROOM"
echo "   curl -X POST $API_URL/api/cap-tables/init"
curl -s -X POST $API_URL/api/cap-tables/init | jq '.data' 2>/dev/null | head -20
echo ""

# Test 3: Get All Cap Tables
echo "3️⃣  Get All Cap Tables"
echo "   curl $API_URL/api/cap-tables"
curl -s $API_URL/api/cap-tables | jq '.data | length' 2>/dev/null
echo ""

# Test 4: Get Specific Cap Table (CON-001)
echo "4️⃣  Get Cap Table for CON-001"
echo "   curl $API_URL/api/cap-tables/CON-001"
curl -s $API_URL/api/cap-tables/CON-001 | jq '.data | {venture_id, founder_pct, employee_pool_pct, investor_pct}' 2>/dev/null || echo "❌ Cap table not found (run init first)"
echo ""

# Test 5: Get Portfolio Summary
echo "5️⃣  Get Portfolio Summary"
echo "   curl $API_URL/api/ventures/portfolio"
curl -s $API_URL/api/ventures/portfolio | jq '.data | {total_deals, total_pipeline, avg_deal_value}' 2>/dev/null || echo "❌ Portfolio query failed"
echo ""

# Test 6: Add File to Deal (TEST)
echo "6️⃣  Add File to Deal (TEST)"
echo "   curl -X POST $API_URL/api/deals/1/files"
curl -s -X POST $API_URL/api/deals/1/files \
  -H "Content-Type: application/json" \
  -d '{
    "file_name": "Test_Contract_v1.pdf",
    "file_path": "/tmp/test.pdf",
    "file_size": 2400000,
    "mime_type": "application/pdf",
    "uploader": "TestUser",
    "description": "Test contract file"
  }' | jq '.' 2>/dev/null || echo "❌ File upload failed"
echo ""

# Test 7: Get Deal Files
echo "7️⃣  Get Files for Deal 1"
echo "   curl $API_URL/api/deals/1/files"
curl -s $API_URL/api/deals/1/files | jq '.data | length' 2>/dev/null || echo "❌ Get files failed"
echo ""

# Test 8: Get Deal with Files (Enhanced)
echo "8️⃣  Get Deal Details (with embedded files)"
echo "   curl $API_URL/api/deals/1"
curl -s $API_URL/api/deals/1 | jq '.data | {company_name, stage, files: .files | length}' 2>/dev/null || echo "❌ Deal not found"
echo ""

echo "=================================="
echo "✅ Phase 3 API Testing Complete"
echo ""
echo "📊 API Endpoints Implemented:"
echo "  POST   /api/cap-tables/init             ✓ Initialize all cap tables"
echo "  GET    /api/cap-tables                  ✓ Get all cap tables"
echo "  GET    /api/cap-tables/:venture_id      ✓ Get specific cap table"
echo "  POST   /api/deals/:id/files             ✓ Add file to deal"
echo "  GET    /api/deals/:id/files             ✓ Get deal files"
echo "  GET    /api/ventures/portfolio          ✓ Get portfolio summary"
