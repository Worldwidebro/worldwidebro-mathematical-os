#!/usr/bin/env python3
"""
Company Brain: n8n Workflow Catalog Search CLI
High-performance local search across curated production n8n workflows mapped to the 27 Company Income Loops.
Authority: Infrastructure Control Plane (CP-027), CP-002 & Rule 2 (Reuse First)
Reference: 55-LOOP-ENGINEERING/COMPANY_INCOME_LOOPS_ARCHITECTURE.md
"""

import sys
import json
import sqlite3
import argparse
from pathlib import Path

DB_PATH = Path(__file__).parent / "n8n_workflows.db"
MACSTUDIO_WORKFLOWS_PATH = "/Volumes/LaCie/n8n-workflows/workflows"

# The 27 Closed-Loop Feedback Circuits mapping keywords
LOOP_DEFINITIONS = {
    1: ("Market Intelligence", ["market", "scrape", "competitor", "news", "trend", "rfp", "research", "linkedin"]),
    2: ("Lead Acquisition", ["lead", "apollo", "hunter", "lemlist", "outreach", "prospect", "email list", "enrich", "scrape"]),
    3: ("Lead Qualification", ["qualif", "scoring", "clearbit", "enrich", "filter", "segment", "verify"]),
    4: ("Sales Conversation", ["transcript", "whisper", "summary", "zoom", "call", "meet", "recording", "objection"]),
    5: ("Opportunity Management", ["hubspot", "deal", "pipedrive", "proposal", "crm", "salesforce", "quote"]),
    6: ("Quote to Cash", ["quote", "stripe", "contract", "docusign", "pandadoc", "order", "payment", "invoice"]),
    7: ("Customer Onboarding", ["onboard", "welcome", "slack invite", "portal", "credentials", "account create"]),
    8: ("Operational Fulfillment", ["dispatch", "delivery", "tracking", "courier", "fulfillment", "shipment", "driver", "route"]),
    9: ("Exception & Circuit Breaker", ["error", "alert", "failure", "retry", "deadletter", "pagerduty", "slack alert", "sentry"]),
    10: ("Billing Engine", ["billing", "invoice", "calculate", "quickbooks", "xero", "charge", "subscription"]),
    11: ("Accounts Receivable", ["overdue", "reminder", "dunning", "collection", "chase", "unpaid"]),
    12: ("Customer Success", ["health score", "nps", "satisfaction", "usage", "feedback", "check-in"]),
    13: ("Expansion & Upsell", ["upsell", "cross-sell", "upgrade", "expansion", "recommend"]),
    14: ("Churn Prevention", ["churn", "inactive", "cancellation", "retention", "re-engage"]),
    15: ("Referral Engine", ["referral", "affiliate", "reward", "invite friends", "advocate"]),
    16: ("Reputation & Review", ["review", "google review", "trustpilot", "testimonial", "rating"]),
    17: ("Marketing Content", ["content", "social", "twitter", "linkedin post", "blog", "ghost", "wordpress", "newsletter"]),
    18: ("Unified Data / CRM", ["sync", "crm", "normalize", "deduplicate", "airtable", "postgres", "supabase"]),
    19: ("KPI Telemetry", ["kpi", "metric", "dashboard", "reporting", "stats", "analytics", "daily report"]),
    20: ("Agent Performance", ["agent", "eval", "prompt test", "benchmark", "accuracy", "llm eval"]),
    21: ("Automation Health", ["health check", "n8n monitor", "workflow status", "execution error", "retry"]),
    22: ("Integration Health", ["webhook ping", "api test", "token refresh", "endpoint monitor", "uptime"]),
    23: ("Cost & Token Loop", ["token", "cost track", "litellm", "budget", "openai cost", "spend"]),
    24: ("Knowledge Graph", ["neo4j", "knowledge graph", "ontology", "qdrant", "vector", "embed"]),
    25: ("Compliance & Audit", ["compliance", "audit", "hipaa", "gdpr", "soc2", "log archive", "policy"]),
    26: ("Finance & Capital", ["financial", "p&l", "balance sheet", "cash flow", "expense", "payroll"]),
    27: ("Venture Portfolio", ["portfolio", "venture", "holding", "multi-tenant", "subsidiary"]),
}


def resolve_loop(loop_input: str):
    """Resolve user loop input (number or substring) to loop id, name, and keywords."""
    if not loop_input:
        return None
    # Check if numeric
    if loop_input.isdigit():
        idx = int(loop_input)
        if idx in LOOP_DEFINITIONS:
            name, kws = LOOP_DEFINITIONS[idx]
            return idx, name, kws
    # Check substring in name
    lower_in = loop_input.lower()
    for idx, (name, kws) in LOOP_DEFINITIONS.items():
        if lower_in in name.lower():
            return idx, name, kws
    return None


def list_loops():
    """Print the 27 Closed-Loop Feedback Circuits."""
    print("\n🏛️ Company Brain: The 27 Closed-Loop Feedback Circuits\n")
    print(f"{'ID':<4} | {'Loop Name':<30} | {'Keywords Sample'}")
    print("-" * 75)
    for idx, (name, kws) in sorted(LOOP_DEFINITIONS.items()):
        print(f"{idx:<4} | {name:<30} | {', '.join(kws[:4])}")
    print("\nUsage: python3 _ENGINE/search_n8n_workflows.py --loop <ID|Name>\n")


def search_workflows(query: str = "", integration: str = "", loop: str = "", limit: int = 15):
    if not DB_PATH.exists():
        print(f"❌ Index database not found at {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    conditions = []
    params = []

    loop_info = resolve_loop(loop) if loop else None
    if loop and not loop_info:
        print(f"⚠️ Loop '{loop}' not recognized. Use --list-loops to view all 27 loops.")

    if loop_info:
        l_id, l_name, l_kws = loop_info
        print(f"🔄 Filtering by Loop #{l_id}: {l_name}")
        kw_conditions = []
        for kw in l_kws:
            kw_conditions.append("(w.name LIKE ? OR w.description LIKE ?)")
            params.extend([f"%{kw}%", f"%{kw}%"])
        conditions.append(f"({' OR '.join(kw_conditions)})")

    if query:
        conditions.append("(w.name LIKE ? OR w.description LIKE ?)")
        params.extend([f"%{query}%", f"%{query}%"])

    if integration:
        conditions.append("EXISTS (SELECT 1 FROM json_each(w.integrations) WHERE json_each.value LIKE ?)")
        params.append(f"%{integration}%")

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    sql = f"""
        SELECT w.id, w.filename, w.name, w.trigger_type, w.complexity, w.node_count, w.integrations, w.description
        FROM workflows w
        {where_clause}
        ORDER BY w.node_count DESC
        LIMIT ?
    """
    params.append(limit)

    cursor = conn.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()

    if not rows:
        print("No matching workflows found.")
        return

    print(f"\n🔍 Found {len(rows)} matching workflows (limit {limit}):\n")
    for r in rows:
        integrations = json.loads(r["integrations"]) if r["integrations"] else []
        integrations_str = ", ".join(integrations) if integrations else "None"
        print(f"📦 ID {r['id']} | {r['name']}")
        print(f"   • File: {r['filename']}")
        print(f"   • Trigger: {r['trigger_type']} | Nodes: {r['node_count']} | Complexity: {r['complexity']}")
        print(f"   • Integrations: {integrations_str}")
        if r["description"]:
            desc_snippet = r["description"][:120] + "..." if len(r["description"]) > 120 else r["description"]
            print(f"   • Description: {desc_snippet}")
        print(f"   • Mac Studio Path: {MACSTUDIO_WORKFLOWS_PATH}/{r['filename']}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Search 2,060+ production n8n workflows mapped to Company Income Loops")
    parser.add_argument("query", nargs="?", default="", help="Keyword search in name/description")
    parser.add_argument("-i", "--integration", default="", help="Filter by integration name (e.g. Supabase, Stripe, Sendgrid)")
    parser.add_argument("-L", "--loop", default="", help="Filter by Loop ID (1-27) or Loop Name (e.g. 'Quote to Cash', 6)")
    parser.add_argument("--list-loops", action="store_true", help="List all 27 Company Income Loops")
    parser.add_argument("-l", "--limit", type=int, default=10, help="Max results to display (default: 10)")

    args = parser.parse_args()

    if args.list_loops:
        list_loops()
        return

    search_workflows(query=args.query, integration=args.integration, loop=args.loop, limit=args.limit)


if __name__ == "__main__":
    main()
