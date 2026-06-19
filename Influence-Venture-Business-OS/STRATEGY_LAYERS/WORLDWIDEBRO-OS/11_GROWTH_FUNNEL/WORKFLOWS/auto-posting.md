# Auto-Posting Integration

Hand off from `gf_publish_queue` to schedulers. n8n nodes are stubs — add API credentials per platform.

## Flow

```
gf_publish_queue (status=approved)
        ↓
n8n: Format for platform
        ↓
Buffer | Later | native API
        ↓
Update asset status=published
        ↓
Analytics Agent (24h later)
```

## Platform notes

### YouTube Shorts
- Upload via YouTube Data API v3
- Fields: title, description, tags from `metadata_*.json` → `publish`
- n8n node: HTTP Request to Google OAuth endpoint

### Instagram Reels / TikTok
- Prefer **Later** or **Buffer** unified API if multi-platform
- Native TikTok Content Posting API requires app review
- Manual fallback: export `publish.json` + MP4 path from runner log

### X (Twitter)
- API v2 media upload + tweet
- Keep MOF threads as thread composer in Buffer

## Status lifecycle

```
draft → queued → ready_for_review → approved → scheduled → posted
                                              ↘ failed
```

Human gate: move `ready_for_review` → `approved` in Supabase or SQLite admin.

## Env vars (n8n)

| Var | Use |
|-----|-----|
| `BUFFER_ACCESS_TOKEN` | Buffer API |
| `LATER_API_KEY` | Later API |
| `YOUTUBE_OAUTH_TOKEN` | Shorts upload |

## Local test without APIs

```bash
python3 SCRIPTS/content_brain.py  # inspect SQLite queue
sqlite3 DATA/content_brain.db "select * from publish_queue;"
```

## Webhook: mark posted

POST to n8n `/webhook/funnel-posted`:
```json
{
  "queue_id": "uuid",
  "platform": "youtube_shorts",
  "external_url": "https://..."
}
```

Updates `gf_publish_queue.status=posted` and `gf_content_assets.published_at`.
