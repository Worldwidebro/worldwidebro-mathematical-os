# VEX Portfolio Accuracy Loop
**Verify VEX shows real data, wire Solution Finder metrics**
2026-09-19

## The Problem: Three Sources of Truth

Right now, portfolio data lives in 3 places:
```
SUPABASE (Transactional)
├─ ventures table (789 rows)
├─ capabilities table (300+ rows)
├─ agents table (318 rows)
└─ metrics table (18K+ KPIs)

NEO4J (Relationships)
├─ Venture nodes + USES_SOLUTION edges
├─ Solution nodes + SOLVES edges
├─ Sector nodes + relationships
└─ 20,363 total edges

VEX DASHBOARD (What User Sees)
├─ Portfolio view: venture list + readiness
├─ Revenue dashboard: pipeline + YTD
├─ Sector breakdown: ventures by sector
└─ Repo integration: code paths
```

**Risk:** VEX shows stale data if Supabase ≠ Neo4j ≠ reality

---

## Solution: Accuracy Loop

### 1. REAL-TIME SYNC (Supabase → VEX)

**VEX currently queries:**
```typescript
// src/api/ventures.ts (in vex-hero-site-sigma.vercel.app)
const { data: ventures } = await supabase
  .from('ventures')
  .select('*')
  .order('readinessPercent', { ascending: false })

// This is live. Good.
```

**But:** Doesn't show **solutions** or **reuse metrics**.

### 2. ADD SOLUTION METRICS (Solution Finder → VEX)

**New VEX queries needed:**

```sql
-- Query 1: Ventures using which solutions
SELECT 
  v.id as venture_id,
  v.name as venture_name,
  COUNT(s.id) as solutions_in_use,
  ARRAY_AGG(s.name) as solution_names,
  ROUND(AVG(s.confidence)::numeric, 2) as avg_solution_confidence
FROM ventures v
LEFT JOIN venture_uses_solution vs ON v.id = vs.venture_id
LEFT JOIN solutions s ON vs.solution_id = s.id
GROUP BY v.id, v.name
ORDER BY solutions_in_use DESC;

-- Query 2: Portfolio reuse rate
SELECT 
  COUNT(DISTINCT v.id) as total_ventures,
  COUNT(DISTINCT CASE WHEN solutions_in_use > 0 THEN v.id END) as ventures_using_solutions,
  ROUND(100.0 * COUNT(DISTINCT CASE WHEN solutions_in_use > 0 THEN v.id END) / 
    COUNT(DISTINCT v.id), 1) as portfolio_reuse_rate_percent
FROM ventures v
LEFT JOIN venture_uses_solution vs ON v.id = vs.venture_id;

-- Query 3: Solutions by popularity (how many ventures use each)
SELECT 
  s.id,
  s.name,
  s.repo,
  COUNT(DISTINCT vs.venture_id) as ventures_using,
  ROUND(AVG(s.confidence)::numeric, 2) as avg_confidence,
  s.usage_count as total_uses
FROM solutions s
LEFT JOIN venture_uses_solution vs ON s.id = vs.solution_id
GROUP BY s.id, s.name, s.repo, s.usage_count
ORDER BY ventures_using DESC;

-- Query 4: Sector solution coverage (which sectors lack solutions)
SELECT 
  v.sector,
  COUNT(v.id) as ventures_in_sector,
  COUNT(DISTINCT CASE WHEN vs.venture_id IS NOT NULL THEN v.id END) as with_solutions,
  ROUND(100.0 * COUNT(DISTINCT CASE WHEN vs.venture_id IS NOT NULL THEN v.id END) / 
    COUNT(v.id), 1) as coverage_percent
FROM ventures v
LEFT JOIN venture_uses_solution vs ON v.id = vs.venture_id
GROUP BY v.sector
ORDER BY coverage_percent ASC;
```

---

## 3. VERIFICATION: Ground Truth Checks

### Daily Accuracy Audit

```bash
#!/bin/bash
# Daily verification: Is VEX showing real data?

echo "=== PORTFOLIO ACCURACY CHECK ==="
echo "Checking: Supabase ↔ Neo4j ↔ VEX alignment"
echo ""

# Check 1: Venture count matches
SUPABASE_COUNT=$(psql postgresql://... -c "SELECT COUNT(*) FROM ventures" -t)
NEO4J_COUNT=$(cypher-shell -u neo4j -p changeme "MATCH (v:Venture) RETURN COUNT(v)" -t)
echo "Venture count: Supabase=$SUPABASE_COUNT, Neo4j=$NEO4J_COUNT"
if [ "$SUPABASE_COUNT" != "$NEO4J_COUNT" ]; then
  echo "⚠️  MISMATCH: Counts differ"
fi

# Check 2: Readiness averages match
SUPABASE_AVG=$(psql postgresql://... -c "SELECT AVG(readinessPercent) FROM ventures" -t)
echo "Avg readiness: Supabase=$SUPABASE_AVG"
# VEX reads from Supabase, so if Supabase matches Neo4j, VEX is correct

# Check 3: Solutions registered
SOLUTIONS=$(cypher-shell -u neo4j -p changeme "MATCH (s:Solution) RETURN COUNT(s)" -t)
echo "Solutions registered: $SOLUTIONS"
if [ "$SOLUTIONS" -lt 3 ]; then
  echo "⚠️  LOW: Only 3 solutions registered. Need more discovery."
fi

# Check 4: Reuse rate
REUSE=$(psql postgresql://... -c "SELECT ROUND(100.0 * COUNT(DISTINCT vs.venture_id) / COUNT(DISTINCT v.id), 1) FROM ventures v LEFT JOIN venture_uses_solution vs ON v.id = vs.venture_id" -t)
echo "Portfolio reuse rate: $REUSE%"
if [ "$REUSE" -lt 50 ]; then
  echo "⚠️  LOW: <50% of ventures using solutions. Registration needed."
fi

echo ""
echo "✅ Audit complete"
```

---

## 4. WIRE SOLUTION FINDER INTO VEX

**Add new tabs to VEX dashboard:**

### Tab 1: Solutions Registry
```tsx
// VEX: src/pages/Solutions.tsx
import SolutionFinder from '../_MCP/solution-finder-core.js';

export function SolutionsTab() {
  const [solutions, setSolutions] = useState([]);
  
  useEffect(() => {
    async function loadSolutions() {
      // Query Neo4j for all registered solutions
      const response = await fetch('/api/solutions', {
        method: 'GET'
      });
      const data = await response.json();
      setSolutions(data);
    }
    loadSolutions();
  }, []);

  return (
    <div className="solutions-tab">
      <h2>Registered Solutions ({solutions.length})</h2>
      <table>
        <thead>
          <tr>
            <th>Solution</th>
            <th>Problem Solved</th>
            <th>Repo</th>
            <th>Ventures Using</th>
            <th>Usage Count</th>
            <th>Confidence</th>
          </tr>
        </thead>
        <tbody>
          {solutions.map(s => (
            <tr key={s.id}>
              <td>{s.name}</td>
              <td>{s.solvesProblem}</td>
              <td>{s.repo}</td>
              <td>{s.venturesUsing}</td>
              <td>{s.usageCount}</td>
              <td>{(s.confidence * 100).toFixed(0)}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

### Tab 2: Venture Solutions
```tsx
// VEX: src/pages/VentureSolutions.tsx
export function VentureSolutionsTab() {
  const [ventures, setVentures] = useState([]);
  
  useEffect(() => {
    async function loadVenturesSolutions() {
      // Query: ventures + their solutions
      const response = await fetch('/api/ventures/with-solutions');
      const data = await response.json();
      setVentures(data);
    }
    loadVenturesSolutions();
  }, []);

  return (
    <div className="ventures-solutions-tab">
      <h2>Ventures Using Solutions</h2>
      {ventures.map(v => (
        <div key={v.id} className="venture-card">
          <h3>{v.name} ({v.sector})</h3>
          <p>Readiness: {v.readinessPercent}%</p>
          {v.solutions.length > 0 ? (
            <ul>
              {v.solutions.map(s => (
                <li key={s.id}>{s.name} ({s.confidence}%)</li>
              ))}
            </ul>
          ) : (
            <p className="warning">No solutions registered. Opportunities for registration.</p>
          )}
        </div>
      ))}
    </div>
  );
}
```

### Tab 3: Portfolio Metrics
```tsx
// VEX: src/pages/PortfolioMetrics.tsx
export function PortfolioMetricsTab() {
  const [metrics, setMetrics] = useState(null);
  
  useEffect(() => {
    async function loadMetrics() {
      const response = await fetch('/api/portfolio/metrics');
      const data = await response.json();
      setMetrics(data);
    }
    loadMetrics();
  }, []);

  if (!metrics) return <p>Loading...</p>;

  return (
    <div className="portfolio-metrics-tab">
      <h2>Portfolio Overview</h2>
      
      <div className="metric-card">
        <h3>Total Ventures</h3>
        <p className="value">{metrics.totalVentures}</p>
      </div>

      <div className="metric-card">
        <h3>Avg Readiness</h3>
        <p className="value">{metrics.avgReadiness.toFixed(1)}%</p>
      </div>

      <div className="metric-card">
        <h3>Solutions Registered</h3>
        <p className="value">{metrics.totalSolutions}</p>
      </div>

      <div className="metric-card">
        <h3>Portfolio Reuse Rate</h3>
        <p className="value">{metrics.reuseRate}%</p>
        <p className="detail">{metrics.venturesUsingSolutions} / {metrics.totalVentures} using solutions</p>
      </div>

      <div className="metric-card">
        <h3>YTD Revenue</h3>
        <p className="value">${metrics.ytdRevenue.toLocaleString()}</p>
      </div>

      <div className="metric-card">
        <h3>Solutions/Week Target</h3>
        <p className="value">{metrics.newSolutionsPerWeek} solutions</p>
      </div>
    </div>
  );
}
```

---

## 5. API ENDPOINTS (to be added to VEX backend)

```typescript
// vex-hero-site/src/api/routes.ts

// GET /api/solutions
// Returns all registered solutions from Neo4j
export async function getSolutions(req, res) {
  const session = driver.session();
  const result = await session.run(
    `MATCH (s:Solution)-[r:SOLVES]->(p:Problem)
     RETURN s.id, s.name, s.repo, p.name as solvesProblem, s.usageCount, r.confidence,
            (SELECT COUNT(DISTINCT v.id) FROM venture_uses_solution WHERE solution_id = s.id) as venturesUsing
     ORDER BY s.usageCount DESC`
  );
  const solutions = result.records.map(r => ({
    id: r.get('s.id'),
    name: r.get('s.name'),
    repo: r.get('s.repo'),
    solvesProblem: r.get('solvesProblem'),
    usageCount: r.get('s.usageCount'),
    confidence: r.get('r.confidence'),
    venturesUsing: r.get('venturesUsing')
  }));
  await session.close();
  res.json(solutions);
}

// GET /api/ventures/with-solutions
// Returns ventures and their linked solutions
export async function getVenturesWithSolutions(req, res) {
  const { data: ventures } = await supabase
    .from('ventures')
    .select('*');
  
  const session = driver.session();
  
  for (const venture of ventures) {
    const result = await session.run(
      `MATCH (v:Venture {id: $venId})-[r:USES_SOLUTION]->(s:Solution)
       RETURN s.id, s.name, r.confidence`,
      { venId: venture.id }
    );
    venture.solutions = result.records.map(r => ({
      id: r.get('s.id'),
      name: r.get('s.name'),
      confidence: r.get('r.confidence')
    }));
  }
  
  await session.close();
  res.json(ventures);
}

// GET /api/portfolio/metrics
// Returns portfolio-wide statistics
export async function getPortfolioMetrics(req, res) {
  const { data: ventures } = await supabase
    .from('ventures')
    .select('readinessPercent, revenue_ytd');
  
  const session = driver.session();
  
  const result = await session.run(`
    MATCH (s:Solution)
    RETURN COUNT(s) as totalSolutions
  `);
  const totalSolutions = result.records[0].get('totalSolutions');
  
  const result2 = await session.run(`
    MATCH (v:Venture)-[r:USES_SOLUTION]->(s:Solution)
    RETURN COUNT(DISTINCT v) as venturesUsingSolutions
  `);
  const venturesUsingSolutions = result2.records[0].get('venturesUsingSolutions');
  
  await session.close();
  
  const avgReadiness = ventures.reduce((sum, v) => sum + (v.readinessPercent || 0), 0) / ventures.length;
  const ytdRevenue = ventures.reduce((sum, v) => sum + (v.revenue_ytd || 0), 0);
  
  res.json({
    totalVentures: ventures.length,
    avgReadiness,
    totalSolutions,
    venturesUsingSolutions,
    reuseRate: Math.round(100 * venturesUsingSolutions / ventures.length),
    ytdRevenue,
    newSolutionsPerWeek: 3 // Target
  });
}
```

---

## 6. VERIFICATION CHECKLIST

Before trusting VEX data:

- [ ] Supabase venture count = Neo4j venture count
- [ ] VEX refreshes every 5 minutes (not stale)
- [ ] Solutions tab shows ≥3 registered solutions
- [ ] Venture-Solutions tab shows linked solutions per venture
- [ ] Portfolio Metrics tab shows reuse rate ≥0% (growing to 70%+)
- [ ] YTD Revenue matches Supabase revenue_ytd field
- [ ] Sector breakdown sums to 789 ventures
- [ ] No venture shows 0% readiness when it should have progress
- [ ] Solution confidence scores are 0.75–0.95 range

---

## Implementation Schedule

| Time | Task | Impact |
|------|------|--------|
| **Today** | Deploy Solution Finder core (done) | Enables discovery |
| **Week 1 (Sep 19–25)** | Wire VEX solutions tabs | Visibility |
| **Week 2 (Sep 26–Oct 2)** | Accuracy audit (daily) | Trust |
| **Week 3+ (Oct 3+)** | Auto-register solutions post-execution | Growth |

---

## Current Status

✅ Solution Finder built and registered (3 solutions)  
✅ Neo4j schema ready (solutions + relationships)  
🟡 VEX dashboard running (needs solutions tabs)  
🟡 Accuracy audit not yet automated  
🔴 Auto-registration post-execution not yet wired

**Next:** Wire VEX to show solutions + metrics.

