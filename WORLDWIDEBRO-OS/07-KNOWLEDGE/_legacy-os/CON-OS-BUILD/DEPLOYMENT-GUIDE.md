# 🚀 CON OS Deployment Guide

**Status:** Ready to deploy | **Timeline:** 24 hours | **Cost:** ~$150/month

## Quick Start (Production)

### 1. Railway Services
```bash
railway up --environment production
# 5 services auto-deploy: intake, contracts, payout, orchestrator, memory
```

### 2. Vercel Dashboard
```bash
vercel --prod
# Dashboard live at: https://con-os.vercel.app
```

### 3. Stripe Integration
```bash
# Add STRIPE_SECRET_KEY to .env
# Test with first deal
```

### 4. Test End-to-End
```bash
python scripts/test_production.py
```

**Result:** System live + accepting deals in <24 hours

## Cost: $150/month (scales with revenue)
- Supabase: $25
- Railway: $50  
- Vercel: Free
- Stripe: 2.9% + $0.30 per transaction
