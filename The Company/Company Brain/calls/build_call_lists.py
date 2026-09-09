#!/usr/bin/env python3
"""
Build verified call lists for 5 ventures using web research.
Each row: company_name, phone, contact_name, title, company_size, pain_signal, source_url, confidence_score

Quality gates:
- Phone: verified via company website or directory
- Contact name: from LinkedIn or company page
- Pain signal: specific, from website/job postings
- Confidence: 75-100% only (website-verified)
"""

import csv
from pathlib import Path

# Base directory
BASE_DIR = Path("/Users/acebless/Documents/The Company/Company Brain/calls")

# Sample template for verified entries (will be populated via web research)
VENTURES_CONFIG = {
    "OPS-001": {
        "target": 50,
        "current": 10,
        "category": "Staffing Agencies",
        "starting_10": [
            "Hire Dynamics",
            "Ōnin Staffing",
            "Spherion",
            "Aerotek",
            "Atlantic Staffing",
            "Staffmark",
            "PrideStaff",
            "Kelly Services",
            "Manpower",
            "Volt Information",
        ],
        "search_keywords": [
            "staffing agency NC",
            "temp agency warehouse North Carolina",
            "staffing recruiter Charlotte",
            "temporary staffing services NC",
        ],
    },
    "CON-001": {
        "target": 50,
        "current": 8,
        "category": "General Contractors NC",
        "starting_8": [
            ("Marolf Construction", "Bob Marolf", "704-563-7410", "[HIGH PRIORITY - OWNER CONTACT]"),
            "Satterfield & Pontikes",
            "Voltz Builders",
            "Turner Construction",
            "Blythe Construction",
            "Cleary & Associates",
            "Baker Construction",
            "Peak Construction",
        ],
        "search_keywords": [
            "NC licensed general contractor",
            "North Carolina commercial builder",
            "general contractor Charlotte NC",
            "construction company Raleigh NC",
        ],
    },
    "LT-005": {
        "target": 30,
        "current": 10,
        "category": "Medical Facilities",
        "starting_10": [
            "WakeMed",
            "Atrium Health",
            "Novant Health",
            "Duke Health",
            "UNC Health",
            "Iredell Health System",
            "Cone Health",
            "Cape Fear Valley Health",
            "Vidant Health",
            "Hugh Chatham Memorial",
        ],
        "search_keywords": [
            "NC hospital lab services",
            "diagnostic laboratory North Carolina",
            "medical facility specimen handling",
        ],
    },
    "LT-011": {
        "target": 25,
        "current": 10,
        "category": "Freight/TMS Companies",
        "starting_10_with_priority": [
            ("Carolina Logistics", "[ACTIVE RFP WINDOW - URGENT PRIORITY]"),
            "Southeastern Freight Lines",
            "Mesilla Valley Transportation",
            "Boyd Bros Transportation",
            "USA Truck",
            "Ruan Transportation",
            "Heartland Express",
            "Marten Transport",
            "Universal Truckload Services",
            "Forward Air",
        ],
        "search_keywords": [
            "freight company Southeast",
            "TMS evaluation RFP",
            "trucking company hiring",
            "logistics company North Carolina",
        ],
    },
    "RE-001": {
        "target": 15,
        "current": 10000,  # Huge pool to filter
        "category": "Accredited Investors (Real Estate)",
        "source_categories": [
            "Angel syndicates",
            "Real estate funds",
            "Syndication platforms",
            "SEC-verified individual investors",
        ],
        "search_keywords": [
            "real estate syndication platform",
            "angel investor network",
            "real estate fund active deals",
            "accredited investors syndication",
        ],
    },
}

# Print configuration
print("=" * 80)
print("CALL LIST BUILDER - Phase 3 Web Research")
print("=" * 80)
print()
print(f"Output directory: {BASE_DIR}")
print()
print("Ventures to expand:")
for venture_id, config in VENTURES_CONFIG.items():
    print(f"  {venture_id}: {config['category']} ({config['current']} → {config['target']})")
print()
print("Research methodology:")
print("  1. Web search for companies in category")
print("  2. Fetch company websites for contact info")
print("  3. Extract: name, phone, contact_name, title, pain_signal")
print("  4. Verify: website-confirmed ONLY (75-100% confidence)")
print("  5. CSV: company_name|phone|contact_name|title|company_size|pain_signal|source_url|confidence_score")
print()
print("=" * 80)

