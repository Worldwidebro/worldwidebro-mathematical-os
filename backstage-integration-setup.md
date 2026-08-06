---
name: backstage-integration-setup
title: 'Option B: Backstage Integration'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Option B: Backstage Integration
## Service Catalog for Ventures & Repos

**Purpose:** Deploy Backstage as the UI layer showing:
- **Services**: 687 Ventures (product offerings)
- **Dependencies**: 853 Repos (technical components needed)
- **Integration Roadmaps**: Timeline to build venture using repos
- **Dashboard**: Visibility into venture completion status

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Backstage Portal                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Service Catalog                                      │   │
│  │  ├─ Ventures (as Services)                            │   │
│  │  │  └─ BW-001 (Lash Extensions)                       │   │
│  │  │     ├─ Dependency: cal_com (booking)               │   │
│  │  │     ├─ Dependency: stripe (payments)               │   │
│  │  │     └─ Dependency: crm-platform                    │   │
│  │  │                                                     │   │
│  │  ├─ Component Repository (Repos)                      │   │
│  │  │  ├─ Frontend: cal_com                              │   │
│  │  │  ├─ Backend: stripe                                │   │
│  │  │  └─ Integration: crm-platform                      │   │
│  │  │                                                     │   │
│  │  └─ Integration Roadmap                               │   │
│  │     ├─ Phase 1 (Week 1-2): Setup calendar + payments  │   │
│  │     ├─ Phase 2 (Week 3-4): Integrate CRM              │   │
│  │     └─ Phase 3 (Week 5+): Testing & launch            │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓                                   │
└──────────────────────────────────────────────────────────────┘
         ↓                          ↓                    ↓
    Supabase            Graphify KG            LlamaIndex
    (Ventures,          (Relationships         (Semantic
     Repos,             between ventures       Search)
     Metadata)          & repos)
```

---

## Deployment Instructions

### 1. Install Backstage (Docker or Local)

**Option A: Docker (Recommended)**

```bash
docker pull backstage/backstage:latest
docker run -p 3000:7007 \
  -e BACKSTAGE_BASE_URL=http://localhost:3000 \
  -e DATABASE_CONNECTION_STRING=postgresql://user:pass@postgres:5432/backstage \
  backstage/backstage:latest
```

**Option B: Local Development**

```bash
# Install Node.js 18+
node --version  # Should be v18+

# Create new Backstage app
npx @backstage/create-app@latest --path ./backstage-app

cd backstage-app
npm install
npm run dev
```

Backstage will be available at `http://localhost:3000`

---

### 2. Configure Database Connection

Backstage uses PostgreSQL. Update your `app-config.yaml`:

```yaml
backend:
  database:
    connection:
      host: localhost
      port: 5432
      user: backstage
      password: your_password
      database: backstage
  cache:
    store: memory

# Enable Supabase integration
integrations:
  supabase:
    - host: cyhzilqldouzgynacqpe.supabase.co
      token: ${SUPABASE_SERVICE_KEY}
```

---

### 3. Create Custom Entities for Ventures

Create `entities/venture-entity.yaml` template:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Service
metadata:
  name: {{ venture.id }}
  title: {{ venture.name }}
  description: {{ venture.product_description }}
  labels:
    sector: {{ venture.sector }}
    stage: {{ venture.stage }}
    revenue_potential: {{ venture.revenue_potential }}
spec:
  type: venture
  owner: {{ venture.owner_id }}
  system: ventures
  providesApis:
    - {{ venture.id }}-api
  dependsOn:
    {% for repo_id in venture.required_repos %}
    - component:{{ repo_id }}
    {% endfor %}
  lifecycle: {{ venture.stage }}
```

---

### 4. Create Repo Component Catalog

Create `entities/repo-component.yaml` template:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: {{ repo.name }}
  description: {{ repo.purpose }}
  labels:
    capability: {{ repo.capabilities | join(',') }}
    integration_effort: {{ repo.integration_effort }}
    maturity: {{ repo.maturity }}
spec:
  type: library
  owner: community
  providesApis:
    - {{ repo.name }}-api
  consumedBy:
    {% for venture_id in repo.venture_ids %}
    - service:{{ venture_id }}
    {% endfor %}
  links:
    - url: {{ repo.github_url }}
      title: GitHub Repository
```

---

### 5. Populate Catalog from Supabase

Create `sync-script.ts` to sync Supabase data into Backstage:

```typescript
// sync-script.ts
import { createClient } from '@supabase/supa-client';
import * as fs from 'fs';
import * as yaml from 'js-yaml';

const supabase = createClient(
  'https://cyhzilqldouzgynacqpe.supabase.co',
  process.env.SUPABASE_SERVICE_KEY || ''
);

// Fetch all ventures
const { data: ventures } = await supabase
  .from('ventures')
  .select('*')
  .limit(1000);

// Fetch all repos
const { data: repos } = await supabase
  .from('repos')
  .select('*')
  .limit(1000);

// Generate YAML entities
const ventureEntities = ventures.map(venture => ({
  apiVersion: 'backstage.io/v1alpha1',
  kind: 'Service',
  metadata: {
    name: venture.id,
    title: venture.name,
    description: venture.product_description,
    labels: {
      sector: venture.sector,
      stage: venture.stage,
    },
  },
  spec: {
    type: 'venture',
    owner: venture.owner_id,
    dependsOn: venture.required_repos?.map(r => `component:${r}`) || [],
  },
}));

const repoEntities = repos.map(repo => ({
  apiVersion: 'backstage.io/v1alpha1',
  kind: 'Component',
  metadata: {
    name: repo.name,
    description: repo.purpose,
    labels: {
      integration_effort: repo.integration_effort,
      maturity: repo.maturity,
    },
  },
  spec: {
    type: 'library',
    owner: 'community',
    providesApis: [`${repo.name}-api`],
  },
}));

// Write to catalog directory
fs.writeFileSync(
  './catalog/ventures.yaml',
  ventureEntities.map(e => yaml.dump(e)).join('---\n')
);

fs.writeFileSync(
  './catalog/repos.yaml',
  repoEntities.map(e => yaml.dump(e)).join('---\n')
);

console.log(`Synced ${ventureEntities.length} ventures and ${repoEntities.length} repos`);
```

Run sync:
```bash
npm install @supabase/supabase-js js-yaml
npx ts-node sync-script.ts
```

---

### 6. Register Custom Plugin for Integration Roadmap

Create `plugins/integration-roadmap/src/plugin.ts`:

```typescript
import { createPlugin, createRoutableExtension } from '@backstage/core-plugin-api';
import { IntegrationRoadmapComponent } from './components/IntegrationRoadmap';

export const integrationRoadmapPlugin = createPlugin({
  id: 'integration-roadmap',
});

export const IntegrationRoadmapPage = integrationRoadmapPlugin.provide(
  createRoutableExtension({
    name: 'IntegrationRoadmapPage',
    component: () => IntegrationRoadmapComponent,
    mountPoint: { path: 'ventures/:ventureId/roadmap' },
  })
);
```

Create `plugins/integration-roadmap/src/components/IntegrationRoadmap.tsx`:

```typescript
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router';
import { supabase } from '../supabase-client';

export const IntegrationRoadmapComponent = () => {
  const { ventureId } = useParams();
  const [venture, setVenture] = useState(null);
  const [repos, setRepos] = useState([]);
  const [phases, setPhases] = useState([]);

  useEffect(() => {
    loadData();
  }, [ventureId]);

  const loadData = async () => {
    // Fetch venture
    const { data: v } = await supabase
      .from('ventures')
      .select('*')
      .eq('id', ventureId)
      .single();
    setVenture(v);

    // Fetch required repos
    const { data: r } = await supabase
      .from('repos')
      .select('*')
      .contains('venture_ids', [ventureId]);
    setRepos(r);

    // Calculate phases based on repos
    const phases = calculateIntegrationPhases(r);
    setPhases(phases);
  };

  const calculateIntegrationPhases = (repos: any[]) => {
    // Group repos by integration_effort
    const lowEffort = repos.filter(r => r.integration_effort === 'low');
    const mediumEffort = repos.filter(r => r.integration_effort === 'medium');
    const highEffort = repos.filter(r => r.integration_effort === 'high');

    return [
      {
        name: 'Phase 1: Foundation',
        duration: '1-2 weeks',
        repos: lowEffort,
        effort: 'Low',
      },
      {
        name: 'Phase 2: Integration',
        duration: '2-4 weeks',
        repos: mediumEffort,
        effort: 'Medium',
      },
      {
        name: 'Phase 3: Advanced',
        duration: '4+ weeks',
        repos: highEffort,
        effort: 'High',
      },
    ];
  };

  return (
    <div>
      <h1>Integration Roadmap: {venture?.name}</h1>
      <div style={{ marginTop: '20px' }}>
        {phases.map((phase, idx) => (
          <div
            key={idx}
            style={{
              border: '1px solid #ccc',
              padding: '15px',
              marginBottom: '15px',
              borderRadius: '8px',
            }}
          >
            <h3>{phase.name}</h3>
            <p>Duration: {phase.duration}</p>
            <p>Repos ({phase.repos.length}):</p>
            <ul>
              {phase.repos.map(repo => (
                <li key={repo.id}>
                  {repo.name} - {repo.estimated_integration_days} days
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};
```

---

### 7. Setup Catalog Ingestion

Update `app-config.yaml`:

```yaml
catalog:
  import:
    entityFilename: catalog-info.yaml
    parseYamlErrors: warn
  rules:
    - allow: [Component, Service, System, API, Resource, Location]
  providers:
    supabase:
      default:
        host: cyhzilqldouzgynacqpe.supabase.co
        schedule:
          frequency: { minutes: 30 }
          timeout: { minutes: 10 }
```

---

## Expected Features

Once deployed:

### 1. **Service Catalog View**
- Browse all 687 ventures as "Services"
- Click venture → see required repos as dependencies
- View integration difficulty + estimated timeline

### 2. **Component Library**
- Browse all 853 repos
- Filter by: capability, maturity, integration_effort
- See which ventures depend on each repo

### 3. **Integration Roadmap**
```
BW-001: Lash Extensions Studio
├─ Phase 1 (Week 1-2) ✓
│  └─ cal_com (booking system) - 5 days
├─ Phase 2 (Week 3-4)
│  └─ stripe (payment processing) - 8 days
└─ Phase 3 (Week 5-6)
   └─ crm-platform (customer management) - 12 days
```

### 4. **Dependency Graph Visualization**
- Neo4j-like relationship visualization
- See all ventures dependent on a repo
- Identify critical repos (many dependents)

### 5. **Status Dashboard**
- Venture completion % (roles filled, repos integrated, revenue launched)
- Repo adoption count (how many ventures using this?)
- Integration pipeline (which ventures in Phase 1, 2, 3?)

---

## Testing the Integration

```bash
# 1. Start Backstage
npm run dev

# 2. Navigate to Service Catalog
open http://localhost:3000/catalog/services

# 3. View a venture
click BW-001-lash-extension-studio

# 4. View integration roadmap
click "Integration Roadmap" tab

# 5. Test semantic search
# (If LlamaIndex integration added to Backstage search bar)
search "real-time collaboration" → shows repos + ventures that match
```

---

## Integration with Option A & C

| Option | Provides to Backstage |
|--------|----------------------|
| **A: Metadata** | Ventures table + Repos table (structured data foundation) |
| **B: Backstage** | UI/portal layer showing relationships and roadmaps |
| **C: LlamaIndex** | Semantic search bar: "What repos solve X?" → ranked results |

Together: **Obsidian (knowledge) → Backstage (service catalog) → LlamaIndex (semantic) = Complete intelligence layer**

---

## Next Steps

1. [ ] Deploy Backstage locally (Docker or npm)
2. [ ] Configure Supabase integration
3. [ ] Run sync-script.ts to populate catalog
4. [ ] Deploy integration-roadmap plugin
5. [ ] Add LlamaIndex search integration (hybrid semantic + catalog)
6. [ ] Link ClickUp tasks to Backstage services (track execution)
7. [ ] Create Slack/email notifications on venture status changes
