# CON OS Setup Guide

## Day 1 Setup

### 1. Install Dependencies
```bash
cd CON-OS-BUILD
pip install -r requirements.txt
```

### 2. Set Environment Variables
```bash
export SUPABASE_URL="your_supabase_url"
export SUPABASE_KEY="your_supabase_key"
export FLASK_ENV="development"
```

### 3. Start All Services (in separate terminals)
```bash
# Terminal 1
python services/deal_intake/service.py

# Terminal 2
python services/contract_generator/service.py

# Terminal 3
python services/payout_engine/service.py

# Terminal 4
python services/orchestrator/service.py

# Terminal 5
python services/graph_memory/service.py
```

### 4. Run Tests
```bash
python scripts/test_day1.py
```

## Day 1 Success Criteria
- [ ] All 5 services respond to /health
- [ ] submit_referral accepts deal
- [ ] generate_contracts creates 4 types
- [ ] trigger_payment_distribution splits correctly
- [ ] route_deal assigns agent
- [ ] update_graph_memory scores contractor

## What's Next
- Day 2: Contracts with Documenso signing
- Day 3-7: Complete 5 services + integration
- Day 8-14: Dashboard + scale
