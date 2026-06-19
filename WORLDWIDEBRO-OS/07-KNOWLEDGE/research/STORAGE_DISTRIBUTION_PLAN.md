# Storage & Repo Distribution Plan

## Current State
- **Local Storage:** 18GB
- **Ventures:** 712 | **Repos:** 985
- **venture-hub/ Size:** 4.5GB

---

## Storage Estimation

| Phase | Deliverables | Per Venture | Total 629 Ventures | EDTECH (69) |
|-------|--------------|-------------|-------------------|------------|
| 1: Discovery | Trends + forecasts | 100KB | 63MB | - |
| 2: Validation | Landing pages + surveys | 50KB | 31MB | 3.5MB |
| 3: Creation | Specs + courses | 50KB | 31MB | **6,900MB** |
| 4-9: Branding through Exit | Assets + docs | 800KB | 503MB | 52MB |
| **TOTAL** | **Full Pipeline** | **~1.1MB** | **~628MB** | **~6,950MB** |

**Grand Total: 7.6GB additional**
**Projected Final: 18GB + 7.6GB = 25.6GB**

---

## Storage by Content Type

**Metadata (Central, in git):** 100MB
- Product specs, surveys, PMF scores, brand guides

**Assets (Distributed to repos):** 7.5GB
- Videos (EDTECH): 6.9GB → YouTube/Vimeo (links only)
- Images: 315MB → GitHub/Cloudinary
- HTML/CSS: 100MB → GitHub
- Docs/PDFs: 50MB → GitHub
- Audio: 100MB → Anchor/Buzzsprout (links only)

---

## Distribution Strategy

### Central WORLDWIDEBRO-OS (Metadata Only)
```
WORLDWIDEBRO-OS/
├── 01_CEO_COMMAND_CENTER/ (dashboards, scoring models)
├── 02_MARKETING/ (brand guides, content calendars)
├── 03_SALES/ (funnel specs, CRM configs)
└── 10_VENTURES/[VENTURE_ID]/
    ├── Product_Specs/ (markdown files)
    ├── REPO_MANIFEST.json (pointer to venture repos)
    └── PRODUCT_REFERENCES.json (links to external content)
```

**Size: ~100MB** ✅

### Venture Repos (Assets & Code)
```
Each venture gets 4-5 repos:

venture-[ID]-product/     (code + specs) - ~50-150MB
venture-[ID]-web/         (landing pages) - ~500KB
venture-[ID]-marketing/   (ads + creatives) - ~300KB
venture-[ID]-content/     (courses) - ~100MB (EDTECH only)
venture-[ID]-operations/  (SOPs, dashboards) - ~50KB

Total per venture: ~150-250MB (varies by type)
629 ventures × avg 200MB = ~126GB distributed
```

### Distribution Manifest

File: `WORLDWIDEBRO-OS/10_VENTURES/[VENTURE_ID]/REPO_MANIFEST.json`

```json
{
  "venture_id": "fin-001",
  "repos": {
    "product": {
      "url": "https://github.com/Worldwidebro/venture-fin-001-product",
      "path": "src/",
      "size_mb": 150
    },
    "web": {
      "url": "https://github.com/Worldwidebro/venture-fin-001-web",
      "size_mb": 1
    },
    "marketing": {
      "url": "https://github.com/Worldwidebro/venture-fin-001-marketing",
      "size_mb": 300
    },
    "operations": {
      "url": "https://github.com/Worldwidebro/venture-fin-001-operations",
      "size_mb": 1
    }
  },
  "external": {
    "videos": "https://youtube.com/playlist?list=fin-001",
    "website": "https://genixbank-lite.com"
  }
}
```

---

## Distribution by Phase

**Phase 2 (Validation):** Landing pages → `venture-[ID]-web/`
**Phase 3 (Creation):** Specs → `venture-[ID]-product/` | Courses → `venture-[ID]-content/`
**Phase 4 (Branding):** Brand assets → `venture-[ID]-web/` + `venture-[ID]-marketing/`
**Phase 5 (Sales):** Sales pages → `venture-[ID]-web/`
**Phase 6 (Marketing):** Ad creatives → `venture-[ID]-marketing/`
**Phase 7-9 (Operations):** Docs → `venture-[ID]-operations/`

---

## Large Files Strategy (Videos)

**EDTECH Courses (6.9GB across 69 ventures):**

✅ **Recommended:** YouTube hosting + metadata in repos

```bash
# Instead of storing 100MB video in GitHub:
# 1. Upload to YouTube → get video_id
# 2. Store in REPO_MANIFEST.json:
{
  "course_video": {
    "platform": "youtube",
    "video_id": "xyz123",
    "url": "https://youtube.com/watch?v=xyz123",
    "size_mb": 100,
    "storage": "external"
  }
}
# 3. Link from course pages
```

**Benefits:**
- No local storage needed
- Better discoverability
- Automatic transcoding
- Built-in analytics
- Free hosting (up to YouTube limits)

---

## Local Storage Management

### Current (18GB)
```
WORLDWIDEBRO-OS/           800MB (metadata)
venture-hub/               4.5GB (registries)
generated-courses/         2.3GB (some EDTECH)
integrations/              1.2GB
iza-os-rag-system/         2.1GB
TrendRadar/                600MB
Miro-Fish/                 300MB
Other/                     6.2GB
```

### After Phase 1-3 (Est. 25.6GB)
```
WORLDWIDEBRO-OS/           1.2GB (expanded metadata)
venture-hub/               5.5GB (registries + pointers)
generated-courses/         8GB (all 69 EDTECH)
LightRAG + embeddings/     2.5GB
Other/                     8.4GB
```

**Action:** Increase local SSD to 50GB for safety margin

---

## GitHub Distribution (No limit)

629+ repos spread across:
- venture-[ID]-product: ~63GB total
- venture-[ID]-web: ~315MB total
- venture-[ID]-marketing: ~189MB total
- venture-[ID]-content (EDTECH): ~6.9GB total (mostly video links)
- venture-[ID]-operations: ~63MB total

**Total GitHub footprint: ~70GB**

---

## Implementation Script

File: `WORLDWIDEBRO-OS/09_AUTOMATION/distribute_to_venture_repos.py`

```python
#!/usr/bin/env python3
import json
from pathlib import Path

def distribute_deliverables(phase, venture_id, content_path, target_repo_type):
    """
    phase: 2-9
    venture_id: "fin-001"
    content_path: "/path/to/landing_page.html"
    target_repo_type: "web" | "product" | "marketing" | "content" | "operations"
    
    Copies files to correct venture repo and updates REPO_MANIFEST.json
    """
    repo_url = f"https://github.com/Worldwidebro/venture-{venture_id}-{target_repo_type}"
    local_repo = f"/tmp/venture-{venture_id}-{target_repo_type}"
    
    # Clone repo
    # Copy files
    # Update REPO_MANIFEST.json
    # Commit & push
    # Cleanup
    
    print(f"✅ Distributed {content_path} to {repo_url}")

if __name__ == "__main__":
    # Phase 2: Distribute landing pages
    for venture in get_ventures_from_csv():
        distribute_deliverables(
            phase=2,
            venture_id=venture['id'],
            content_path=f"WORLDWIDEBRO-OS/02_MARKETING/Landing_Pages/{venture['id']}.html",
            target_repo_type="web"
        )
```

---

## Growth Projections

| Date | Local | GitHub | External | Total |
|------|-------|--------|----------|-------|
| 2026-06-04 | 18GB | 0GB | 0GB | 18GB |
| 2026-06-30 | 25.6GB | 15GB | 6.9GB | 47.5GB |
| 2026-09-30 | 35GB | 45GB | 15GB | 95GB |
| 2026-12-31 | 40GB | 70GB | 25GB | 135GB |

---

## Answer to Your Question

**Q: Will it properly distribute to the repos we have?**

✅ **YES - We have the infrastructure:**
- 985 repos already registered
- Resource dependency mapping exists (VENTURE-RESOURCE-DEPENDENCIES.csv)
- Shared services architecture is in place

**How it works:**
1. Each venture gets 4-5 dedicated repos
2. Phase deliverables routed by type (web assets → `-web/`, code → `-product/`, etc.)
3. Central WORLDWIDEBRO-OS tracks via REPO_MANIFEST.json pointers
4. Large media (videos) hosted externally, linked from repos
5. Automated distribution script handles the movement

**Q: How much storage?**

**Local:** 25.6GB (manageable)
**Total (distributed):** ~135GB by end
**Cost:** Minimal (GitHub is free for public, YouTube/Vimeo free for video)
