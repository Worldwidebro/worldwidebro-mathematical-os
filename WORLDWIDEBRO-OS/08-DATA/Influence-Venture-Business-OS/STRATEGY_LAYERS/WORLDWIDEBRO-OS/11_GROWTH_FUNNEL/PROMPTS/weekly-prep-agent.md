# Weekly Prep Agent

**Goal:** Sunday reset — prepare next week's content batch.

## Inputs
- Saturday `gf_weekly_reports`
- `content_hooks` winners
- `audience.md` + `brand_identity.md`
- Content calendar template

## Deliverables
| Asset | Count |
|-------|-------|
| New hooks | 20 |
| Content ideas | 10 |
| Video scripts (TOF/MOF/BOF) | 5 |
| Monday pre-queue | yes |

## Output paths
- `moneyprinter-output/{venture_id}/funnel/next_week_ideas.json`
- `gf_content_hooks` (20 rows, status=draft)
- `gf_content_assets` (5 script_json rows)
- `gf_publish_queue` (Monday TOF prefetch, status=ready_for_review)

## Process
1. Read Saturday report — double down on winning angles
2. Retire archived hooks
3. Generate 20 hooks (Hook Agent prompt)
4. Map 10 ideas to calendar slots (Mon–Fri)
5. Write 5 scripts via `build_script_package` per stage
6. Pre-queue 3 Monday TOF assets

## Trigger
Sunday 6 PM — `weekly_funnel_runner.py --day sunday`

## Brand check
Run Brand Agent consistency pass before marking queue `ready_for_review`.
