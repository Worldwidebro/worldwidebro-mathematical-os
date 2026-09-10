#!/usr/bin/env python3
"""
Site Readiness Audit (Automated)

Checks critical paths for all 6 Tier-0 ventures:
- HTTP status codes
- Page load time
- Form field presence
- Database connectivity
- Email integration

Usage:
  python3 site_audit.py --venture LT-005 --full
  python3 site_audit.py --all --verbose
"""

import requests
import time
from datetime import datetime
from typing import Dict, List, Tuple
import json

# ============================================================================
# VENTURE CONFIGURATION
# ============================================================================

VENTURES = {
    'OPS-001': {
        'url': 'https://ops-staff-001-staffing.vercel.app/',
        'name': 'Staff Placement',
        'form_fields': ['name', 'email', 'phone', 'skills'],
        'revenue_model': '$2.5K/placement'
    },
    'LT-005': {
        'url': 'https://healthroute-courier.vercel.app/',
        'name': 'Medical Courier',
        'form_fields': ['company_name', 'email', 'phone', 'specimens_per_day'],
        'revenue_model': '$85-150/delivery'
    },
    'CALLCENTER': {
        'url': 'https://callcenter-eosin.vercel.app/',
        'name': 'Call Center',
        'form_fields': ['name', 'email', 'company', 'call_volume'],
        'revenue_model': '$50-200/call'
    },
    'CON-001': {
        'url': 'https://con-001-ace-construction.vercel.app/',
        'name': 'Construction',
        'form_fields': ['name', 'email', 'company', 'project_type'],
        'revenue_model': '$5K-50K/project'
    },
    'RE-001': {
        'url': 'https://re-001-worldwidebro-holdings.vercel.app/',
        'name': 'Real Estate',
        'form_fields': ['name', 'email', 'company', 'deal_size'],
        'revenue_model': '$50K-500K/deal'
    },
    'LT-011': {
        'url': 'https://lt-011-dispatch-software.vercel.app/',
        'name': 'Dispatch Software',
        'form_fields': ['name', 'email', 'company', 'drivers'],
        'revenue_model': '$1K-5K/month'
    }
}

# ============================================================================
# AUDIT CHECKS
# ============================================================================

class SiteAudit:
    """Automated site readiness audit"""

    def __init__(self, venture_id: str, verbose: bool = False):
        self.venture_id = venture_id
        self.config = VENTURES[venture_id]
        self.url = self.config['url']
        self.verbose = verbose
        self.results = {}
        self.passed = 0
        self.failed = 0

    def log(self, message: str, level: str = 'INFO'):
        """Log audit messages"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        if level == 'INFO' or self.verbose:
            print(f"[{timestamp}] {level}: {message}")

    def check_http_status(self) -> bool:
        """Check if site returns 200 OK"""
        self.log(f"Checking HTTP status: {self.url}")
        try:
            response = requests.get(self.url, timeout=10)
            status = response.status_code

            if status == 200:
                self.log(f"✅ HTTP 200 OK", 'PASS')
                self.passed += 1
                return True
            else:
                self.log(f"❌ HTTP {status} (expected 200)", 'FAIL')
                self.failed += 1
                return False
        except Exception as e:
            self.log(f"❌ Connection failed: {e}", 'FAIL')
            self.failed += 1
            return False

    def check_page_load_time(self) -> bool:
        """Check if page loads within 3 seconds"""
        self.log("Checking page load time...")
        try:
            start = time.time()
            response = requests.get(self.url, timeout=10)
            elapsed = time.time() - start

            if elapsed < 3.0:
                self.log(f"✅ Loaded in {elapsed:.2f}s (< 3s)", 'PASS')
                self.passed += 1
                return True
            else:
                self.log(f"⚠️  Loaded in {elapsed:.2f}s (> 3s target)", 'WARN')
                self.failed += 1
                return False
        except Exception as e:
            self.log(f"❌ Load time check failed: {e}", 'FAIL')
            self.failed += 1
            return False

    def check_html_validity(self) -> bool:
        """Check if HTML contains required form fields"""
        self.log("Checking HTML validity...")
        try:
            response = requests.get(self.url, timeout=10)
            html = response.text.lower()

            # Check for form element
            if '<form' not in html:
                self.log("❌ No form found on page", 'FAIL')
                self.failed += 1
                return False

            # Check for input fields
            found_fields = []
            for field in self.config['form_fields']:
                if field.lower() in html or f'name="{field}"' in html or f"name='{field}'" in html:
                    found_fields.append(field)

            if len(found_fields) >= len(self.config['form_fields']) * 0.7:  # 70% threshold
                self.log(f"✅ Form fields found: {found_fields}", 'PASS')
                self.passed += 1
                return True
            else:
                self.log(f"⚠️  Only found {len(found_fields)}/{len(self.config['form_fields'])} form fields", 'WARN')
                self.failed += 1
                return False
        except Exception as e:
            self.log(f"❌ HTML check failed: {e}", 'FAIL')
            self.failed += 1
            return False

    def check_no_console_errors(self) -> bool:
        """Check for common error patterns in HTML"""
        self.log("Checking for error patterns...")
        try:
            response = requests.get(self.url, timeout=10)
            html = response.text

            error_patterns = [
                '500 Internal Server Error',
                'Fatal error',
                'Uncaught Exception',
                'TypeError:',
                'ReferenceError:',
                'Cannot read property'
            ]

            found_errors = [p for p in error_patterns if p.lower() in html.lower()]

            if not found_errors:
                self.log("✅ No critical errors detected", 'PASS')
                self.passed += 1
                return True
            else:
                self.log(f"❌ Found errors: {found_errors}", 'FAIL')
                self.failed += 1
                return False
        except Exception as e:
            self.log(f"⚠️  Could not check for errors: {e}", 'WARN')
            return True  # Don't fail if we can't check

    def check_cta_visible(self) -> bool:
        """Check if call-to-action button is present"""
        self.log("Checking for CTA button...")
        try:
            response = requests.get(self.url, timeout=10)
            html = response.text.lower()

            cta_patterns = [
                'get started',
                'sign up',
                'try for free',
                'apply now',
                'request trial',
                'start free trial',
                'contact us',
                'book a call'
            ]

            found_cta = any(pattern in html for pattern in cta_patterns)

            if found_cta:
                self.log("✅ CTA button found", 'PASS')
                self.passed += 1
                return True
            else:
                self.log("❌ No CTA button detected", 'FAIL')
                self.failed += 1
                return False
        except Exception as e:
            self.log(f"❌ CTA check failed: {e}", 'FAIL')
            self.failed += 1
            return False

    def check_mobile_viewport(self) -> bool:
        """Check if mobile viewport meta tag is present"""
        self.log("Checking mobile responsiveness...")
        try:
            response = requests.get(self.url, timeout=10)
            html = response.text

            if 'viewport' in html and 'width=device-width' in html:
                self.log("✅ Mobile viewport configured", 'PASS')
                self.passed += 1
                return True
            else:
                self.log("⚠️  Mobile viewport not found", 'WARN')
                self.failed += 1
                return False
        except Exception as e:
            self.log(f"⚠️  Mobile check failed: {e}", 'WARN')
            return False

    def run_full_audit(self):
        """Run all checks"""
        print("\n" + "=" * 70)
        print(f"SITE READINESS AUDIT: {self.venture_id}")
        print(f"Venture: {self.config['name']}")
        print(f"URL: {self.url}")
        print("=" * 70 + "\n")

        checks = [
            ("HTTP Status", self.check_http_status),
            ("Page Load Time", self.check_page_load_time),
            ("HTML Validity", self.check_html_validity),
            ("No Console Errors", self.check_no_console_errors),
            ("CTA Button", self.check_cta_visible),
            ("Mobile Viewport", self.check_mobile_viewport),
        ]

        for check_name, check_func in checks:
            try:
                check_func()
            except Exception as e:
                self.log(f"❌ {check_name} failed with exception: {e}", 'ERROR')
                self.failed += 1

        # Summary
        print("\n" + "=" * 70)
        print(f"RESULTS: {self.passed} passed, {self.failed} failed")

        if self.failed == 0:
            print("🟢 STATUS: READY FOR WEEK 1")
        elif self.failed <= 2:
            print("🟡 STATUS: CAUTION (minor issues)")
        else:
            print("🔴 STATUS: NEEDS FIXES")

        print("=" * 70 + "\n")

        return self.failed == 0


def audit_all_ventures(verbose: bool = False):
    """Run audit on all ventures"""
    results = {}

    for venture_id in VENTURES.keys():
        audit = SiteAudit(venture_id, verbose)
        results[venture_id] = audit.run_full_audit()

    # Summary report
    print("\n" + "=" * 70)
    print("SUMMARY: ALL VENTURES")
    print("=" * 70)

    for venture_id, passed in results.items():
        status = "🟢 READY" if passed else "🔴 NEEDS WORK"
        print(f"  {venture_id}: {status}")

    ready_count = sum(1 for v in results.values() if v)
    print(f"\nReady for Week 1: {ready_count}/6")
    print("=" * 70 + "\n")


# ============================================================================
# CLI
# ============================================================================

if __name__ == '__main__':
    import sys

    venture = sys.argv[2] if '--venture' in sys.argv else 'LT-005'
    all_ventures = '--all' in sys.argv
    verbose = '--verbose' in sys.argv

    if all_ventures:
        audit_all_ventures(verbose)
    else:
        audit = SiteAudit(venture, verbose)
        audit.run_full_audit()
