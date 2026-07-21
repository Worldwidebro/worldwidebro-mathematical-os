#!/bin/bash

# Supabase Funding Programs Schema Deployment Script
# This script provides step-by-step instructions for deploying the funding_programs table
# and related infrastructure to Supabase.

set -e

echo "======================================================================"
echo "  SUPABASE FUNDING PROGRAMS SCHEMA DEPLOYMENT"
echo "======================================================================"
echo ""
echo "This script will guide you through deploying the funding programs"
echo "schema to Supabase. Follow the steps below carefully."
echo ""

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}STEP 1: Prepare SQL File${NC}"
echo "-------"
echo "The SQL schema is located at:"
echo "  /Users/acebless/Documents/supabase-funding-schema.sql"
echo ""
echo "This file contains:"
echo "  • funding_programs table (22 columns)"
echo "  • 22 sample funding programs across 4 sectors (CON, RE, OPS, LOG)"
echo "  • 3 indexes for optimized queries"
echo "  • venture_funding_tracker table for application tracking"
echo "  • v_active_funding_by_sector view for dashboard"
echo ""

echo -e "${YELLOW}STEP 2: Access Supabase SQL Editor${NC}"
echo "-------"
echo "1. Open your Supabase project: https://supabase.com/dashboard"
echo "2. Navigate to: Database > SQL Editor"
echo "3. Click the '+' button to create a new query"
echo ""

echo -e "${YELLOW}STEP 3: Deploy Schema in Sections${NC}"
echo "-------"
echo "Copy and run the following sections in order:"
echo ""

echo -e "${BLUE}SECTION 1: Create funding_programs table and indexes${NC}"
echo "Copy lines 5-27 from supabase-funding-schema.sql"
echo "  • Creates table with UUID primary key"
echo "  • Adds 3 performance indexes"
echo "  • Validates opco_sector values (CON|RE|OPS|LOG)"
echo ""

echo -e "${BLUE}SECTION 2: Insert sample funding data${NC}"
echo "Copy lines 30-56 from supabase-funding-schema.sql"
echo "  • Inserts 22 total funding programs"
echo "  • CON (Construction): 6 programs"
echo "  • RE (Real Estate): 4 programs"
echo "  • OPS (Staffing): 6 programs"
echo "  • LOG (Logistics): 3 programs"
echo ""

echo -e "${BLUE}SECTION 3: Create dashboard view${NC}"
echo "Copy lines 59-66 from supabase-funding-schema.sql"
echo "  • Creates v_active_funding_by_sector view"
echo "  • Used by analytics dashboards"
echo ""

echo -e "${BLUE}SECTION 4: Create venture_funding_tracker table${NC}"
echo "Copy lines 69-84 from supabase-funding-schema.sql"
echo "  • Tracks venture funding applications"
echo "  • References ventures(id) and funding_programs(id)"
echo "  • Records application status and award amounts"
echo ""

echo -e "${YELLOW}STEP 4: Verify Deployment${NC}"
echo "-------"
echo "After running all sections, verify with this query:"
echo ""
echo "  SELECT COUNT(*) as program_count FROM funding_programs;"
echo ""
echo "Expected result: 22 rows"
echo ""

echo -e "${YELLOW}STEP 5: Load Environment Variables${NC}"
echo "-------"
echo "After Supabase deployment completes:"
echo ""
echo "1. Get your Supabase credentials:"
echo "   • Project URL: Database Settings > Connection Info > URI"
echo "   • Anon Key: Settings > API > Project API Keys > anon"
echo ""
echo "2. Update vex-hero-site/.env.local:"
echo "   VITE_SUPABASE_URL=https://your-project.supabase.co"
echo "   VITE_SUPABASE_ANON_KEY=your_anon_key_here"
echo ""

echo -e "${YELLOW}STEP 6: Test Integration${NC}"
echo "-------"
echo "1. Navigate to vex-hero-site directory"
echo "2. Run: npm install"
echo "3. Run: npm start"
echo "4. Open browser to: http://localhost:3000/operations"
echo "5. Verify the OpcoFundingCommand component loads"
echo "6. Check that sector buttons work and funding data displays"
echo ""

echo -e "${GREEN}DEPLOYMENT CHECKLIST${NC}"
echo "-------"
cat << 'EOF'
□ Step 1: Reviewed SQL schema location
□ Step 2: Opened Supabase SQL Editor
□ Step 3.1: Deployed funding_programs table and indexes
□ Step 3.2: Inserted 22 sample funding programs
□ Step 3.3: Created v_active_funding_by_sector view
□ Step 3.4: Created venture_funding_tracker table
□ Step 4: Verified: SELECT COUNT(*) FROM funding_programs; (expect 22)
□ Step 5: Updated .env.local with Supabase credentials
□ Step 6: Tested /operations route (npm start → http://localhost:3000/operations)
□ Step 7: Verified sector buttons and funding display work
□ Production Deployment: Deploy vex-hero-site to Vercel (git push)

EOF

echo -e "${YELLOW}TROUBLESHOOTING${NC}"
echo "-------"
echo ""
echo "Issue: 'Table funding_programs does not exist'"
echo "  → Verify you ran SECTION 1 (create table)"
echo "  → Check that query executed without errors"
echo ""

echo "Issue: 'violates foreign key constraint' on venture_funding_tracker"
echo "  → Ensure your ventures table exists (created by populate_venture_knowledge_graph.py)"
echo "  → Or run: SECTION 4 after ensuring ventures table is present"
echo ""

echo "Issue: /operations route shows 404"
echo "  → Verify App.tsx has the route: <Route path=\"/operations\" element={<Operations />} />"
echo "  → Restart dev server (npm start)"
echo ""

echo "Issue: Environment variables not loading"
echo "  → Ensure .env.local is in vex-hero-site root (same level as src/, package.json)"
echo "  → Restart dev server after changing .env.local"
echo "  → Check variable names use VITE_ prefix (Vite requirement)"
echo ""

echo -e "${YELLOW}ROLLBACK INSTRUCTIONS${NC}"
echo "-------"
echo "To undo this deployment in Supabase SQL Editor, run:"
echo ""
echo "  DROP TABLE IF EXISTS venture_funding_tracker CASCADE;"
echo "  DROP VIEW IF EXISTS v_active_funding_by_sector;"
echo "  DROP TABLE IF EXISTS funding_programs CASCADE;"
echo ""

echo -e "${GREEN}====== DEPLOYMENT GUIDE COMPLETE ======${NC}"
echo ""
echo "Next step: Follow STEP 2 above to access Supabase SQL Editor"
echo "For questions, see: /Users/acebless/Documents/VEX-OPERATIONS-DEPLOYMENT.md"
echo ""
