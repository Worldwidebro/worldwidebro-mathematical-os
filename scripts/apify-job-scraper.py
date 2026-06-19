#!/usr/bin/env python3
"""
Apify-based LinkedIn Job Scraper for Anissa Valentin
Scrapes jobs matching Patient Care Assistant, Medical Assistant, and Nanny positions
in Charlotte, NC and remote locations
"""

import json
import requests
from datetime import datetime
from typing import List, Dict

# Apify API Configuration
APIFY_API_TOKEN = "apify_api_VzIeQMEhS0R9G8BapAhvrzuCUNIBnw4rqy1N"
APIFY_BASE_URL = "https://api.apify.com/v2"

# Job Search Profiles for Anissa
SEARCH_PROFILES = [
    {
        "query": "Patient Care Assistant",
        "location": "Charlotte, NC",
        "remote": False,
        "count": 20
    },
    {
        "query": "Patient Care Assistant",
        "location": "",
        "remote": True,
        "count": 20
    },
    {
        "query": "Medical Assistant",
        "location": "Charlotte, NC",
        "remote": False,
        "count": 15
    },
    {
        "query": "Medical Assistant",
        "location": "",
        "remote": True,
        "count": 15
    },
    {
        "query": "Nanny",
        "location": "Charlotte, NC",
        "remote": True,
        "count": 10
    },
    {
        "query": "Healthcare Assistant",
        "location": "Charlotte, NC",
        "remote": False,
        "count": 10
    },
    {
        "query": "Care Coordinator",
        "location": "Charlotte, NC",
        "remote": True,
        "count": 10
    }
]

class LinkedInJobScraper:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.base_url = APIFY_BASE_URL
        self.jobs = []
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        })

    def search_jobs(self, query: str, location: str = "", remote: bool = False) -> List[Dict]:
        """
        Search for jobs using Apify's LinkedIn Jobs Actor
        """
        print(f"\n🔍 Searching: {query} | Location: {location or 'Remote'}")

        actor_input = {
            "keywords": query,
            "locations": [location] if location else [],
            "filters": {},
            "startPage": 0,
            "maxItems": 30
        }

        if remote:
            actor_input["filters"]["remote"] = True

        try:
            # Call Apify's LinkedIn Jobs Actor
            # Actor ID for LinkedIn Jobs: wqEAcMnJCG8eoXHJ8 (LinkedIn Jobs)
            response = self.session.post(
                f"{self.base_url}/acts/wqEAcMnJCG8eoXHJ8/runs",
                json={"input": actor_input}
            )

            if response.status_code in [200, 201]:
                run_data = response.json()
                run_id = run_data.get("data", {}).get("id")
                print(f"  ✓ Job search started (Run ID: {run_id})")

                # Get results
                results = self._get_run_results(run_id)
                return results
            else:
                print(f"  ✗ API Error: {response.status_code} - {response.text[:200]}")
                return []

        except Exception as e:
            print(f"  ✗ Error: {str(e)}")
            return []

    def _get_run_results(self, run_id: str) -> List[Dict]:
        """Get results from a completed Apify run"""
        try:
            response = self.session.get(
                f"{self.base_url}/acts/wqEAcMnJCG8eoXHJ8/runs/{run_id}/dataset/items"
            )

            if response.status_code == 200:
                return response.json()
            else:
                print(f"    Failed to get results: {response.status_code}")
                return []

        except Exception as e:
            print(f"    Error fetching results: {str(e)}")
            return []

    def format_job(self, job_data: Dict) -> Dict:
        """Format job data into our standard format"""
        return {
            "title": job_data.get("title", ""),
            "company": job_data.get("company", ""),
            "location": job_data.get("location", ""),
            "salary": job_data.get("salary", ""),
            "job_url": job_data.get("link", ""),
            "description": job_data.get("description", ""),
            "posted_date": job_data.get("publishedDate", ""),
            "work_type": job_data.get("workType", "Full-time"),
            "source": "LinkedIn"
        }

    def run_all_searches(self) -> List[Dict]:
        """Run all search profiles and collect jobs"""
        all_jobs = []

        print("=" * 60)
        print("🚀 STARTING JOB SEARCH FOR ANISSA VALENTIN")
        print(f"Target: Charlotte, NC & Remote Positions")
        print(f"Timestamp: {datetime.now().isoformat()}")
        print("=" * 60)

        for profile in SEARCH_PROFILES:
            results = self.search_jobs(
                query=profile["query"],
                location=profile["location"],
                remote=profile["remote"]
            )

            for job in results:
                formatted_job = self.format_job(job)
                all_jobs.append(formatted_job)

        return all_jobs

    def save_to_csv(self, jobs: List[Dict], filename: str = None):
        """Save jobs to CSV"""
        if not filename:
            filename = f"/Users/acebless/Documents/ANISSA-JOB-MATCHES-{datetime.now().strftime('%Y%m%d')}.csv"

        if not jobs:
            print(f"\n❌ No jobs found to save")
            return

        import csv

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ["title", "company", "location", "salary", "work_type", "posted_date", "job_url", "source"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(jobs)

            print(f"\n✅ Saved {len(jobs)} jobs to {filename}")
            return filename

        except Exception as e:
            print(f"❌ Error saving CSV: {str(e)}")
            return None

    def save_to_json(self, jobs: List[Dict], filename: str = None):
        """Save jobs to JSON"""
        if not filename:
            filename = f"/Users/acebless/Documents/ANISSA-JOB-MATCHES-{datetime.now().strftime('%Y%m%d')}.json"

        try:
            output = {
                "candidate": {
                    "name": "Anissa Valentin",
                    "email": "anissavalentin2000@gmail.com",
                    "location": "Charlotte, NC",
                    "phone": "980-636-9191"
                },
                "search_params": {
                    "date": datetime.now().isoformat(),
                    "locations": ["Charlotte, NC", "Remote"],
                    "job_titles": ["Patient Care Assistant", "Medical Assistant", "Nanny", "Healthcare Assistant", "Care Coordinator"]
                },
                "total_matches": len(jobs),
                "jobs": jobs
            }

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=2, ensure_ascii=False)

            print(f"✅ Saved {len(jobs)} jobs to {filename}")
            return filename

        except Exception as e:
            print(f"❌ Error saving JSON: {str(e)}")
            return None

def main():
    # Initialize scraper
    scraper = LinkedInJobScraper(APIFY_API_TOKEN)

    # Run all searches
    jobs = scraper.run_all_searches()

    # Save results
    if jobs:
        json_file = scraper.save_to_json(jobs)
        csv_file = scraper.save_to_csv(jobs)

        print("\n" + "=" * 60)
        print(f"📊 SUMMARY")
        print(f"Total Jobs Found: {len(jobs)}")
        print(f"CSV File: {csv_file}")
        print(f"JSON File: {json_file}")
        print("=" * 60)
    else:
        print("\n⚠️  No jobs found in search")
        print("\nℹ️  Note: If using free tier or trial, some limitations may apply.")
        print("    Consider running specific searches manually via LinkedIn.")

if __name__ == "__main__":
    main()
