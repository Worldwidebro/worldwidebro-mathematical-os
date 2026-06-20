# n8n Wiring Guide — Growth Funnel (Quick Setup)

What you need from n8n and your stack to wire TOF → MOF → BOF automation in under an hour.

---

## 0. Blockers (read first)

| Requirement | Why |
|-------------|-----|
| **Self-hosted n8n OR n8n with shell access** | Workflows use `Execute Command` to run Python on your Mac. **n8n Cloud blocks this** unless you use webhooks → a local runner instead. |
| **Supabase project ACTIVE** | Your project `supabase-sky-house` (`xrxbhvimolcfieuwbohb`) is **INACTIVE** — restore it in [Supabase Dashboard](https://supabase.com/dashboard/project/xrxbhvimolcfieuwbohb) before DB wiring. |
| **Same machine paths** | n8n must run commands where `/Users/acebless/Documents/...` exists (your Mac Studio/Air, not a remote container with different paths). |

---

## 1. What to give me / configure in n8n

### A. n8n instance

| Item | Example | Where in n8n |
|------|---------|--------------|
| **Base URL** | `http://localhost:5678` or `https://n8n.yourdomain.com` | Settings → instance URL |
| **Timezone** | `America/New_York` | Workflow settings (already in JSON) |
| **Execute Command allowed** | Yes | Self-hosted: default. Cloud: use webhook fallback (below). |

### B. Supabase credential (one credential, all workflows)

Create credential type **Supabase API**:

| Field | Value |
|-------|--------|
| **Host** | `https://xrxbhvimolcfieuwbohb.supabase.co` |
| **Service Role Key** | Project Settings → API → `service_role` (secret — automation only) |

Also set on the **host that runs Python** (for `content_brain.py` / sync script):

```bash
export SUPABASE_URL=https://xrxbhvimolcfieuwbohb.supabase.co
export SUPABASE_SERVICE_ROLE_KEY=eyJ...   # service_role, not anon
```

### C. Venture batch (already on disk)

`REGISTRY/construction-batch.json` — 5 venture UUIDs. n8n can read this file or you paste IDs into Set nodes.

### D. Optional — posting schedulers

| Platform | Credential | n8n node |
|----------|------------|----------|
| Buffer | Access token | HTTP Request |
| Later | API key | HTTP Request |
| YouTube | OAuth2 | Google YouTube node |

Not required for generation + queue; only for auto-post after `gf_publish_queue.status = approved`.

---

## 2. Import order

1. Apply SQL first (Dashboard → SQL Editor → paste `DATABASE/supabase-content-brain.sql`)
2. Import `WORKFLOWS/n8n-weekly-growth-engine.json`
3. Import `WORKFLOWS/n8n-engagement-feedback-loop.json`
4. Import `WORKFLOWS/n8n-tof-mof-bof.json` (on-demand intake)
5. Import `WORKFLOWS/n8n-batch-all-ventures.json` (manual “run all 5” trigger)

On each workflow: attach **Supabase credential** to every Supabase node; activate workflow.

---

## 3. Per-workflow wiring

### Weekly Growth Engine (`n8n-weekly-growth-engine.json`)

- **7 Schedule Trigger nodes** → already cron-aligned with `weekly-triggers.json`
- **Set nodes** → change `venture_id` OR replace with **Read Binary File** + JSON parse of `construction-batch.json` + **Loop**
- **Execute Command** node runs:
  ```bash
  python3 /Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/weekly_funnel_runner.py \
    --venture-id {{venture_id}} --day {{day}} {{render_flag}}
  ```

**Quick test:** Manual execute on “Set Mon” → should print `✅ Weekly job [monday]`.

### Engagement Feedback Loop (`n8n-engagement-feedback-loop.json`)

- Supabase: `getAll` on `gf_content_assets` where `status=published`
- **Replace** “Pull Platform Analytics” stub with YouTube/IG HTTP nodes OR manual CSV import
- IF `views >= 5000` → `generate_funnel_content.py --stages mof`
- Insert `gf_funnel_events` row

### Batch all ventures (`n8n-batch-all-ventures.json`)

- Manual trigger → Execute Command:
  ```bash
  python3 .../batch_weekly_all_ventures.py
  ```

### On-demand intake (`n8n-tof-mof-bof.json`)

- Webhook POST body:
  ```json
  { "venture_id": "uuid", "render_stage": "tof" }
  ```

---

## 4. If you use n8n Cloud (no Execute Command)

Use a **local webhook runner** on your Mac:

```bash
# Example: small Flask/FastAPI listener on :8765 that runs weekly_funnel_runner.py
# n8n Cloud → HTTP Request POST http://your-tailscale-host:8765/run-weekly
```

Tell me if you're on Cloud — I can add `SCRIPTS/n8n_webhook_runner.py` (one file, no n8n shell).

---

## 5. Supabase setup checklist

- [ ] Restore project `supabase-sky-house` (inactive → active)
- [ ] Run `DATABASE/supabase-content-brain.sql` in SQL Editor
- [ ] Copy **service_role** key into n8n credential + shell env
- [ ] Run local batch (creates SQLite brain):
  ```bash
  python3 SCRIPTS/batch_weekly_all_ventures.py
  ```
- [ ] Sync to Supabase:
  ```bash
  export SUPABASE_URL=...
  export SUPABASE_SERVICE_ROLE_KEY=...
  python3 SCRIPTS/sync_sqlite_to_supabase.py
  ```
- [ ] Table Editor: confirm rows in `gf_ventures`, `gf_content_hooks`, `gf_publish_queue`

---

## 6. Minimum info I need from you to finish wiring

Reply with:

1. **n8n hosting:** self-hosted on Mac / Docker / n8n Cloud?
2. **n8n URL** (if self-hosted, for webhook tests)
3. **Supabase:** confirm after you **restore** the project (or a different project ref if you prefer)
4. **Service role key** — paste into env locally (do not commit); or confirm “applied in n8n credentials only”
5. **Posting:** Buffer / Later / manual only for v1?
6. **Video render in cron:** yes on Wed/Fri (slower) or scripts-only?

---

## 7. File paths n8n Execute Command must use

| Script | Absolute path |
|--------|----------------|
| Weekly runner | `/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/weekly_funnel_runner.py` |
| Batch all | `/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/batch_weekly_all_ventures.py` |
| Generate content | `/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/generate_funnel_content.py` |
| Video render | `/Users/acebless/Documents/run_venture_video_pipeline.sh` |
| Venture batch JSON | `/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/REGISTRY/construction-batch.json` |

---

## 8. Env template

Copy to `~/.env.funnel.local` (source before manual runs):

```bash
SUPABASE_URL=https://xrxbhvimolcfieuwbohb.supabase.co
SUPABASE_SERVICE_ROLE_KEY=
N8N_WEBHOOK_SECRET=optional-shared-secret
FUNNEL_PYTHON=python3
FUNNEL_ROOT=/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL
```
