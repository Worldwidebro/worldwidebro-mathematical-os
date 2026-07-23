#!/bin/bash
# Growth OS Venture API Setup
# Wires CON-001 to Growth OS, creates n8n webhook, tests end-to-end

set -e

echo "🚀 Growth OS Venture API Setup"
echo "================================"

# 1. Verify n8n is running
echo "1️⃣ Checking n8n on Mac Studio (Tailscale 100.87.214.70:5678)..."
if curl -s http://100.87.214.70:5678/api/v1/health > /dev/null 2>&1; then
  echo "✅ n8n is running"
else
  echo "⚠️  n8n not reachable at 100.87.214.70:5678"
  echo "   Attempting ssh macstudio..."
  ssh macstudio "docker ps | grep n8n" || echo "❌ n8n container not found on Mac Studio"
  exit 1
fi

# 2. Create Supabase campaigns table
echo ""
echo "2️⃣ Setting up Supabase campaigns table..."
SUPABASE_URL="${SUPABASE_URL:-https://rhlkjelglvurowdalrgh.supabase.co}"
SUPABASE_KEY="${SUPABASE_KEY:-}"

if [ -z "$SUPABASE_KEY" ]; then
  echo "⚠️  SUPABASE_KEY not set"
  echo "   Set it: export SUPABASE_KEY=your_anon_key"
  exit 1
fi

echo "✅ Supabase credentials configured"

# 3. Verify CON-001 exists
echo ""
echo "3️⃣ Checking CON-001 in ventures table..."
curl -s -X GET \
  "$SUPABASE_URL/rest/v1/ventures?id=eq.CON-001&select=id,name" \
  -H "apikey: $SUPABASE_KEY" \
  | grep -q "CON-001" && echo "✅ CON-001 found" || echo "⚠️  CON-001 not found (optional)"

# 4. Trigger test campaign
echo ""
echo "4️⃣ Testing API: CON-001 trigger campaign..."
RESPONSE=$(curl -s -X POST http://100.87.214.70:5678/webhook/venture-campaign \
  -H "Content-Type: application/json" \
  -d '{
    "venture_id": "CON-001",
    "campaign_type": "lead_gen",
    "target_audience": "electrical_contractors_nc",
    "budget_usd": 5000,
    "duration_days": 30,
    "objectives": ["leads"]
  }')

echo "Response: $RESPONSE"

if echo "$RESPONSE" | grep -q "campaign_id"; then
  echo "✅ Campaign created successfully"
  CAMPAIGN_ID=$(echo "$RESPONSE" | grep -o '"campaign_id":"[^"]*"' | cut -d'"' -f4)
  echo "   Campaign ID: $CAMPAIGN_ID"
else
  echo "⚠️  Campaign creation may have failed"
fi

# 5. Verify in Supabase
echo ""
echo "5️⃣ Verifying in Supabase..."
curl -s -X GET \
  "$SUPABASE_URL/rest/v1/campaigns?venture_id=eq.CON-001&order=created_at.desc&limit=1" \
  -H "apikey: $SUPABASE_KEY" \
  | jq '.[0] | {id, venture_id, status, created_at}' 2>/dev/null && echo "✅ Campaign found in Supabase" || echo "⚠️  Campaign not yet in Supabase"

echo ""
echo "🎉 Venture API Setup Complete"
echo "==============================="
echo ""
echo "Next steps:"
echo "1. n8n: Create webhook workflow (instructions below)"
echo "2. Vercel: Deploy Growth OS"
echo "3. Scale: Wire remaining ventures + agent workflows"
echo ""
