# Portfolio Code Search Strategy

**Goal:** Answer cross-venture code questions without Sourcegraph  
**Tools:** Graft + Git + GitHub CLI + ripgrep  
**Execution:** Parallel search across all 6 venture repos

---

## Question Types & Solutions

### 1. "Where do we use Stripe?" (Cross-venture)

```bash
# Strategy: Clone all repos to ~/work, then grep across all
for repo in ~/work/*/; do
  echo "=== $(basename $repo) ==="
  graft grep "Stripe\|stripe" --in "$repo" 2>/dev/null | head -5
done
```

**Alternative (GitHub):**
```bash
# Search across org via GitHub CLI
gh search code "Stripe" --repo=worldwidebro --match=all --limit=50
```

---

### 2. "Which ventures have OAuth?" (Cross-venture)

```bash
# Use graft on each repo
cd ~/work/HealthRoute-Courier && graft grep "oauth\|OAuth\|NextAuth" --source
cd ~/work/CallCenter && graft grep "oauth\|OAuth\|NextAuth" --source
# ... repeat for each venture
```

**Batch script:**
```bash
#!/bin/bash
for venture_dir in ~/work/*/; do
  venture=$(basename "$venture_dir")
  echo "=== $venture ==="
  graft grep "oauth\|OAuth\|NextAuth" --in "$venture_dir" --source -n 3
done
```

---

### 3. "Find every implementation of lead capture" (Cross-venture)

```bash
# Use graft to find symbol across ventures
for repo in ~/work/*/; do
  graft grep "LeadCapture\|lead.*capture\|captureXead" --in "$repo" --source
done

# Or use regex for consistent naming
for repo in ~/work/*/; do
  graft grep "capture.*[Ll]ead|[Ll]ead.*capture" --in "$repo" --source
done
```

---

## Setup (One-Time)

```bash
# 1. Clone all venture repos to ~/work/
mkdir -p ~/work
cd ~/work
gh repo list worldwidebro --limit 50 | awk '{print $1}' | while read repo; do
  git clone "https://github.com/$repo.git"
done

# 2. Create venture index
cat > ~/work/VENTURE_INDEX.md << 'EOF'
# Venture Repositories

- HealthRoute-Courier (LT-005)
- OPS-Staff-001 (OPS-001)
- CallCenter (CALLCENTER)
- con-001-ace-construction (CON-001)
- RE-001 (RE-001)
- lt-011-dispatch-software (LT-011)
EOF

# 3. Test graft on one repo
graft map --in ~/work/HealthRoute-Courier
```

---

## Query Recipes

| Question | Command | Time |
|----------|---------|------|
| Find all Stripe integrations | `for r in ~/work/*/; do graft grep "Stripe" --in $r --source; done` | 10s |
| Find all payment providers | `for r in ~/work/*/; do graft grep "Stripe\|PayPal\|Braintree\|Square" --in $r; done` | 15s |
| Find all env vars | `for r in ~/work/*/; do graft grep "process.env\|\.env" --in $r; done` | 20s |
| Find all API endpoints | `for r in ~/work/*/; do graft grep "/api/" --in $r; done` | 15s |
| Find all database queries | `for r in ~/work/*/; do graft grep "SELECT\|INSERT\|UPDATE\|supabase" --in $r --source; done` | 20s |

---

## Why This Works

**Advantages:**
- ✅ No external service needed
- ✅ Works offline
- ✅ Faster than web search
- ✅ Exact results (not ranked approximations)
- ✅ Can run scheduled jobs

**Limitations:**
- ❌ Must clone all repos first (~2-3 GB)
- ❌ Slower than indexed search for very large codebases
- ❌ No code similarity/semantic search

---

## Next: Implement Automated Cross-Venture Index

```yaml
# _MCP/VENTURE-CODE-INDEX.yaml
ventures:
  LT-005:
    path: ~/work/HealthRoute-Courier
    language: TypeScript/React
    frameworks: [Next.js, Supabase, Stripe]
    key_symbols: [PaymentFlow, CallLogger, Dashboard]
    
  OPS-001:
    path: ~/work/OPS-Staff-001
    language: TypeScript/React
    frameworks: [Next.js, Vercel, ClickUp]
    key_symbols: [PlacementBoard, ColdCallTracker]
    
  # ... etc
```

Then query via: `graft ask "find all Stripe integrations" --in ~/work/*/`
