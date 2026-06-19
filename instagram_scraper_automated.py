#!/usr/bin/env python3
"""
Instagram Content Scraper - Automated Alternative to Manual Screenshots

Options:
  1. Selenium-based browser scraping (real-time, requires Instagram login)
  2. Webhook-based manual import (copy/paste Instagram URLs)
  3. Browser bookmarklet for one-click capture

This script provides infrastructure for all three options.

Usage:
  python3 instagram_scraper_automated.py --mode setup
  python3 instagram_scraper_automated.py --mode webhook
  python3 instagram_scraper_automated.py --mode selenium --account myaccount
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import asdict, dataclass
import argparse

@dataclass
class InstagramCapture:
    """Instagram post/story capture"""
    source_id: str
    source_url: str
    source_type: str
    caption: str
    image_urls: List[str]
    video_url: Optional[str]
    extracted_text: str
    people_mentioned: List[str]
    hashtags: List[str]
    engagement_metrics: Dict
    captured_at: str
    scrape_method: str

class InstagramScraper:
    def __init__(self):
        self.docs_dir = Path("/Users/acebless/Documents")
        self.intake_dir = self.docs_dir / "WORLDWIDEBRO-OS/00_INTAKE_LAYER"
        self.instagram_dir = self.intake_dir / "Instagram_Raw"
        self.processed_dir = self.intake_dir / "Instagram_Ideas"

        self.instagram_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)

        self.env_file = Path("/Users/acebless/.env")
        self.credentials = self._load_credentials()

    def _load_credentials(self) -> Dict:
        """Load Instagram credentials from .env"""
        credentials = {}
        if self.env_file.exists():
            with open(self.env_file, 'r') as f:
                for line in f:
                    if line.startswith('INSTAGRAM_'):
                        key, val = line.strip().split('=', 1)
                        credentials[key] = val
        return credentials

    def selenium_scrape(self, account: str, post_limit: int = 10) -> List[InstagramCapture]:
        """Option 1: Selenium-based scraping"""
        try:
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            import undetected_chromedriver as uc
        except ImportError:
            print("⚠️  Selenium not installed. Install: pip install selenium undetected-chromedriver")
            return []

        captures = []
        print(f"🔄 Starting Selenium scrape for @{account}...")

        try:
            driver = uc.Chrome()
            driver.get(f"https://www.instagram.com/{account}/")

            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//article"))
            )

            articles = driver.find_elements(By.XPATH, "//article")[:post_limit]

            for article in articles:
                try:
                    img = article.find_element(By.TAG_NAME, "img")
                    caption_elem = article.find_element(By.XPATH, ".//span")

                    capture = InstagramCapture(
                        source_id=f"ig_{datetime.now().timestamp()}",
                        source_url=driver.current_url,
                        source_type="post",
                        caption=caption_elem.text[:200],
                        image_urls=[img.get_attribute("src")],
                        video_url=None,
                        extracted_text="",
                        people_mentioned=[],
                        hashtags=[],
                        engagement_metrics={},
                        captured_at=datetime.now().isoformat(),
                        scrape_method="selenium",
                    )
                    captures.append(capture)
                except Exception as e:
                    print(f"   ⚠️  Failed to extract post: {e}")
                    continue

            driver.quit()
            print(f"   ✅ Extracted {len(captures)} posts")

        except Exception as e:
            print(f"   ❌ Selenium scrape failed: {e}")

        return captures

    def webhook_mode(self) -> Dict:
        """Option 2: Webhook/Manual Import"""
        print("📋 Instagram Webhook / Manual Import Mode")
        print("")

        template = {
            "source_id": "ig_manual_001",
            "source_url": "https://instagram.com/p/...",
            "source_type": "post",
            "caption": "[paste caption here]",
            "image_urls": ["[paste image URL or local path]"],
            "video_url": None,
            "captured_at": datetime.now().isoformat(),
            "scrape_method": "webhook",
        }

        print("Template (paste into webhook):")
        print(json.dumps(template, indent=2))
        print("")

        return template

    def create_webhook_receiver(self):
        """Create HTTP receiver for Instagram webhooks"""
        receiver_code = '''#!/usr/bin/env python3
"""Webhook receiver for Instagram captures"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from pathlib import Path
from datetime import datetime

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
            capture_dir = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/00_INTAKE_LAYER/Instagram_Raw")
            capture_dir.mkdir(parents=True, exist_ok=True)
            capture_file = capture_dir / f"webhook_{datetime.now().timestamp()}.json"

            with open(capture_file, 'w') as f:
                json.dump(data, f, indent=2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "saved", "file": str(capture_file)}).encode())

            print(f"✅ Webhook capture saved: {capture_file}")

        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    server = HTTPServer(("localhost", 5000), WebhookHandler)
    print("🔌 Instagram webhook receiver listening on http://localhost:5000")
    server.serve_forever()
'''

        webhook_file = self.docs_dir / "instagram_webhook_receiver.py"
        with open(webhook_file, 'w') as f:
            f.write(receiver_code)

        os.chmod(webhook_file, 0o755)
        print(f"✅ Webhook receiver: {webhook_file}")

        return webhook_file

    def create_browser_bookmarklet(self):
        """Create JavaScript bookmarklet for one-click Instagram capture"""
        bookmarklet = '''javascript:(function(){
  const post = {
    source_url: window.location.href,
    caption: document.querySelector("span[class*='']") ? document.querySelector("span[class*='']").innerText : "",
    image_urls: Array.from(document.querySelectorAll("img[alt]")).map(i => i.src),
    captured_at: new Date().toISOString(),
    scrape_method: "bookmarklet"
  };

  fetch('http://localhost:5000', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(post)
  }).then(r => r.json()).then(d => alert("✅ Captured")).catch(e => alert("Error: " + e));
})();'''

        bookmarklet_file = self.docs_dir / "INSTAGRAM_CAPTURE_BOOKMARKLET.txt"
        with open(bookmarklet_file, 'w') as f:
            f.write("Copy this entire text into a new browser bookmark's URL bar:\n\n")
            f.write(bookmarklet)

        print(f"✅ Bookmarklet: {bookmarklet_file}")
        return bookmarklet_file

    def create_import_script(self):
        """Create script to process captured Instagram data"""
        import_code = '''#!/usr/bin/env python3
"""Process captured Instagram data"""
import json
from pathlib import Path

INTAKE_DIR = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/00_INTAKE_LAYER/Instagram_Raw")

def process_captures():
    """Find and process all captured Instagram posts"""
    captures = list(INTAKE_DIR.glob("*.json"))

    if not captures:
        print("⚠️  No captures found in", INTAKE_DIR)
        return

    print(f"📊 Found {len(captures)} captures")

    for capture_file in captures:
        with open(capture_file, 'r') as f:
            data = json.load(f)

        print(f"\\n📸 {data.get('source_url', 'unknown')}")
        print(f"   Caption: {data.get('caption', '')[:60]}...")

if __name__ == "__main__":
    process_captures()
'''

        import_file = self.docs_dir / "process_instagram_captures.py"
        with open(import_file, 'w') as f:
            f.write(import_code)

        os.chmod(import_file, 0o755)
        print(f"✅ Import processor: {import_file}")
        return import_file

def main():
    parser = argparse.ArgumentParser(description="Instagram Content Scraper")
    parser.add_argument("--mode", choices=["selenium", "webhook", "setup"], default="setup")
    parser.add_argument("--account", help="Instagram account to scrape")
    parser.add_argument("--limit", type=int, default=10)

    args = parser.parse_args()

    scraper = InstagramScraper()

    print("=" * 60)
    print("Instagram Content Scraper - Automated Alternatives")
    print("=" * 60)
    print("")

    if args.mode == "selenium":
        if not args.account:
            print("❌ --account required for selenium mode")
            sys.exit(1)
        captures = scraper.selenium_scrape(args.account, args.limit)
        print(f"✅ Scraped {len(captures)} posts")

    elif args.mode == "webhook":
        scraper.webhook_mode()
        scraper.create_webhook_receiver()
        scraper.create_browser_bookmarklet()
        scraper.create_import_script()

    elif args.mode == "setup":
        print("🚀 Setting up Instagram capture infrastructure...")
        print("")
        scraper.create_webhook_receiver()
        scraper.create_browser_bookmarklet()
        scraper.create_import_script()
        print("")
        print("✅ Setup complete!")
        print("")
        print("Options:")
        print("  A. Auto-scrape: python3 instagram_scraper_automated.py --mode selenium --account username")
        print("  B. Manual webhook:")
        print("     1. python3 instagram_webhook_receiver.py  (in separate terminal)")
        print("     2. Use bookmarklet from: cat INSTAGRAM_CAPTURE_BOOKMARKLET.txt")
        print("     3. Process: python3 process_instagram_captures.py")

if __name__ == "__main__":
    main()
