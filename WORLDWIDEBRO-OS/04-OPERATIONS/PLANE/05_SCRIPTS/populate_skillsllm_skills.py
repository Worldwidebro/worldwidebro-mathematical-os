#!/usr/bin/env python3
"""
SkillsLLM Ingest Script — Phase 2a
Scrape all 2,800+ skills from SkillsLLM marketplace and insert into Supabase.

Usage:
  python3 populate_skillsllm_skills.py [--sample] [--start-page N] [--end-page M]

Options:
  --sample           Test with first 1 page only (50 skills)
  --start-page N     Start scraping from page N (default: 1)
  --end-page M       Stop scraping at page M (default: auto-detect total)
"""

import asyncio
import json
import sys
import time
from datetime import datetime
from typing import Optional

from playwright.async_api import async_playwright

# Configuration
SKILLSLLM_BASE_URL = "https://skillsllm.com"
RATE_LIMIT_DELAY = 2.0  # seconds between page requests
BATCH_INSERT_SIZE = 100


def get_supabase_client():
    """Initialize Supabase client from .env"""
    import os
    from dotenv import load_dotenv
    from supabase import create_client

    load_dotenv()

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY required in .env")

    return create_client(url, key)


async def scrape_skills_page(page, page_num: int) -> dict:
    """
    Scrape one page of skills from SkillsLLM marketplace.

    Returns dict with skills list, page number, has_next flag
    """
    url = f"{SKILLSLLM_BASE_URL}/skills?page={page_num}"
    print(f"[Page {page_num}] Scraping: {url}")

    try:
        await page.goto(url, wait_until="networkidle", timeout=30000)
    except Exception as e:
        print(f"[ERROR] Failed to load page {page_num}: {e}")
        return {"skills": [], "page": page_num, "has_next": False}

    skills = []

    try:
        # Extract skill cards (adjust selectors based on actual HTML structure)
        skill_items = await page.query_selector_all("[data-skill], .skill-item, [class*='skill']")

        for item in skill_items:
            try:
                # Extract basic fields
                name_el = await item.query_selector("h3, h2")
                name = (await name_el.inner_text()).strip() if name_el else None

                if not name:
                    continue

                desc_el = await item.query_selector("p, [class*='desc']")
                description = (await desc_el.inner_text()).strip() if desc_el else ""

                # GitHub link
                github_el = await item.query_selector("a[href*='github.com']")
                github_url = (await github_el.get_attribute("href")) if github_el else ""

                author = github_url.split("/")[-2] if github_url else "unknown"

                # Category tags
                tag_els = await item.query_selector_all("[class*='tag'], [class*='badge']")
                tags = []
                for tag_el in tag_els:
                    tag_text = (await tag_el.inner_text()).strip()
                    if tag_text:
                        tags.append(tag_text)

                category = tags[0] if tags else ""
                related_tags = tags[1:] if len(tags) > 1 else []

                # GitHub stars and engagement
                stars_el = await item.query_selector("[class*='star']")
                stars_text = (await stars_el.inner_text()).strip() if stars_el else "0"
                stars = int("".join(c for c in stars_text if c.isdigit())) or 0

                engagement_el = await item.query_selector("[class*='engagement']")
                engagement_text = (await engagement_el.inner_text()).strip() if engagement_el else "0"
                engagement = int("".join(c for c in engagement_text if c.isdigit())) or 0

                skills.append({
                    "name": name,
                    "description": description,
                    "author": author,
                    "github_url": github_url,
                    "language": "",
                    "stars": stars,
                    "forks": 0,
                    "category": category,
                    "related_tags": related_tags,
                    "engagement_count": engagement,
                })

            except Exception as e:
                print(f"[WARN] Could not extract skill: {e}")
                continue

        print(f"[Page {page_num}] Extracted {len(skills)} skills")

    except Exception as e:
        print(f"[ERROR] Failed extracting skills: {e}")

    # Check for next page
    has_next = False
    try:
        next_btn = await page.query_selector("[aria-label='Next'], button:has-text('Next')")
        has_next = next_btn is not None and not await next_btn.is_disabled()
    except:
        pass

    return {"skills": skills, "page": page_num, "has_next": has_next}


async def insert_skills_batch(supabase, skills: list) -> int:
    """Batch upsert skills to Supabase"""
    if not skills:
        return 0

    try:
        records = [
            {
                "skill_id": f"skillsllm-{skill['author']}-{skill['name'].lower().replace(' ', '-')}",
                "name": skill["name"],
                "description": skill["description"],
                "author": skill["author"],
                "github_url": skill["github_url"],
                "github_stars": skill["stars"],
                "github_forks": skill["forks"],
                "language": skill["language"],
                "category": skill["category"],
                "related_tags": skill["related_tags"],
                "engagement_count": skill["engagement_count"],
                "synced_from_skillsllm_at": datetime.utcnow().isoformat(),
            }
            for skill in skills
        ]

        result = supabase.table("skills").upsert(records, on_conflict="skill_id").execute()
        inserted = len(result.data) if result.data else 0
        print(f"[DB] Inserted {inserted} skills")
        return inserted

    except Exception as e:
        print(f"[ERROR] Batch insert failed: {e}")
        return 0


async def main(sample: bool = False, start_page: int = 1, end_page: Optional[int] = None):
    """Main scraper loop"""

    try:
        supabase = get_supabase_client()
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    print(f"""
    ========================================
    SkillsLLM Ingest — Phase 2a
    ========================================
    Started: {datetime.utcnow().isoformat()}
    Sample mode: {sample}
    Rate limit: {RATE_LIMIT_DELAY}s per page
    """)

    total_skills = 0
    current_page = start_page
    batch = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            while True:
                if sample and current_page > 1:
                    print("[Sample Mode] Stopping after page 1")
                    break

                if end_page and current_page > end_page:
                    print(f"[Limit] Stopping at page {end_page}")
                    break

                # Scrape page
                result = await scrape_skills_page(page, current_page)

                if not result["skills"]:
                    print("[Info] No skills found, ending scrape")
                    break

                batch.extend(result["skills"])

                # Flush batch if full
                if len(batch) >= BATCH_INSERT_SIZE:
                    inserted = await insert_skills_batch(supabase, batch)
                    total_skills += inserted
                    batch = []

                # Rate limiting
                current_page += 1
                if result["has_next"]:
                    print(f"[Wait] Sleeping {RATE_LIMIT_DELAY}s...")
                    await asyncio.sleep(RATE_LIMIT_DELAY)
                else:
                    print("[Info] Last page reached")
                    break

        finally:
            # Flush remaining
            if batch:
                inserted = await insert_skills_batch(supabase, batch)
                total_skills += inserted

            await browser.close()

    print(f"""
    ========================================
    Ingest Complete
    ========================================
    Total skills: {total_skills}
    Ended: {datetime.utcnow().isoformat()}
    """)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Scrape SkillsLLM and populate Supabase")
    parser.add_argument("--sample", action="store_true", help="Test with page 1 only")
    parser.add_argument("--start-page", type=int, default=1)
    parser.add_argument("--end-page", type=int, default=None)

    args = parser.parse_args()
    asyncio.run(main(sample=args.sample, start_page=args.start_page, end_page=args.end_page))
