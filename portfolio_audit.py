#!/usr/bin/env python3
"""Audit portfolio OS coverage against 724-question framework."""

from collections import defaultdict

FRAMEWORK = {
    "01 Portfolio Strategy": {"total": 30, "answered": 15, "examples": "purpose, thesis, target ROIC, industries"},
    "02 Portfolio Architecture": {"total": 30, "answered": 12, "examples": "7 ventures, holdings structure, dependencies"},
    "03 Venture Selection": {"total": 30, "answered": 10, "examples": "stage, basic info, some synergies"},
    "04 Venture Lifecycle": {"total": 18, "answered": 8, "examples": "stage per venture, entry/exit criteria"},
    "05 Holding Company": {"total": 20, "answered": 6, "examples": "parent entity, some shared services"},
    "06 Org Chart": {"total": 22, "answered": 2, "examples": "high-level only, no executive detail"},
    "07 Departments": {"total": 20, "answered": 8, "examples": "per-venture departments, some KPIs"},
    "08 Roles": {"total": 17, "answered": 0, "examples": "MISSING: no specific role definitions"},
    "09 Business Model": {"total": 20, "answered": 8, "examples": "high-level per venture, some revenue models"},
    "10 Market": {"total": 14, "answered": 2, "examples": "MINIMAL: TAM/SAM/SOM not defined"},
    "11 Customer": {"total": 16, "answered": 2, "examples": "MINIMAL: personas not defined"},
    "12 Product/Service": {"total": 15, "answered": 6, "examples": "product descriptions exist, roadmaps partial"},
    "13 Revenue": {"total": 17, "answered": 6, "examples": "revenue models sketched, metrics partial"},
    "14 Unit Economics": {"total": 15, "answered": 5, "examples": "targets exist, actuals missing"},
    "15 Operations": {"total": 17, "answered": 2, "examples": "MINIMAL: processes not mapped"},
    "16 Technology": {"total": 18, "answered": 6, "examples": "tech stack partial, some repos identified"},
    "17 Data": {"total": 17, "answered": 5, "examples": "data infra partial, Neo4j + Supabase identified"},
    "18 Finance": {"total": 19, "answered": 8, "examples": "ROIC targets, financial structure"},
    "19 Capital Allocation": {"total": 15, "answered": 6, "examples": "allocation logic exists, deployment partial"},
    "20 People/Talent": {"total": 15, "answered": 2, "examples": "MINIMAL: staffing structure not detailed"},
    "21 Sales": {"total": 15, "answered": 2, "examples": "MINIMAL: sales motion not defined"},
    "22 Marketing": {"total": 13, "answered": 2, "examples": "MINIMAL: marketing strategy not detailed"},
    "23 Partnerships": {"total": 10, "answered": 1, "examples": "MINIMAL: partnerships not mapped"},
    "24 Assets": {"total": 11, "answered": 4, "examples": "asset inventory partial, utilization not mapped"},
    "25 Risk": {"total": 14, "answered": 2, "examples": "MINIMAL: risk assessment incomplete"},
    "26 Legal/Compliance": {"total": 14, "answered": 1, "examples": "MINIMAL: legal structure not documented"},
    "27 Performance": {"total": 9, "answered": 5, "examples": "KPIs defined, tracking partial"},
    "28 Synergies": {"total": 22, "answered": 18, "examples": "6 synergies mapped, values calculated"},
    "29 Agent Portfolio": {"total": 39, "answered": 0, "examples": "MISSING: no agents defined"},
    "30 Agent Organization": {"total": 16, "answered": 0, "examples": "MISSING: no agent org structure"},
    "31 Agent Capabilities": {"total": 14, "answered": 0, "examples": "MISSING: no agent capabilities"},
    "32 Agent Workflows": {"total": 17, "answered": 0, "examples": "MISSING: no agent workflows"},
    "33 Agent Authority": {"total": 15, "answered": 0, "examples": "MISSING: no agent authority matrix"},
    "34 Agent Economics": {"total": 13, "answered": 0, "examples": "MISSING: no agent cost/ROI"},
    "35 Agent Evaluation": {"total": 16, "answered": 0, "examples": "MISSING: no agent evaluation"},
    "36 Human Governance": {"total": 13, "answered": 3, "examples": "approval logic partial"},
    "37 Automation": {"total": 13, "answered": 2, "examples": "MINIMAL: automation scope not mapped"},
    "38 Knowledge Graph": {"total": 13, "answered": 4, "examples": "Neo4j started, entities partial"},
    "39 Decision Engine": {"total": 19, "answered": 4, "examples": "some decision logic, not comprehensive"},
    "40 Portfolio Control Tower": {"total": 28, "answered": 18, "examples": "dashboard built, KPIs tracked"},
    "41 Continuous Improvement": {"total": 17, "answered": 3, "examples": "feedback loops partial"},
}

print("=" * 80)
print("PORTFOLIO OS COVERAGE AUDIT: 724-Question Framework")
print("=" * 80)
print()

total_qs = 0
total_answered = 0
critical_gaps = []

for section, data in FRAMEWORK.items():
    coverage = (data["answered"] / data["total"]) * 100
    total_qs += data["total"]
    total_answered += data["answered"]
    
    status = "✅" if coverage >= 70 else "⚠️" if coverage >= 40 else "🔴"
    print(f"{status} {section}: {data['answered']}/{data['total']} ({coverage:.0f}%)")
    print(f"   {data['examples']}")
    
    if coverage < 40:
        critical_gaps.append((section, coverage, data['total'] - data['answered']))
    print()

print("=" * 80)
print(f"TOTAL: {total_answered}/{total_qs} questions answered = {(total_answered/total_qs)*100:.1f}%")
print("=" * 80)
print()

print("🔴 CRITICAL GAPS (< 40% coverage):")
print("-" * 80)
for section, coverage, gap in sorted(critical_gaps, key=lambda x: x[1]):
    print(f"   {section}: {gap} questions unanswered ({coverage:.0f}%)")

print()
print("🟡 MAJOR FEATURE GAPS:")
print("-" * 80)
print("   • Agent Portfolio OS (0/39 questions) ← REQUIRED for automation")
print("   • Org Chart & Roles (0/39 questions) ← REQUIRED for governance")
print("   • Sales Motion (2/15 questions) ← REQUIRED for revenue growth")
print("   • Market Analysis (2/14 questions) ← REQUIRED for TAM/SOM")
print()

print("✅ STRENGTHS:")
print("-" * 80)
print("   • Synergies mapped (18/22): 6 revenue/cost opportunities identified")
print("   • Portfolio Control Tower (18/28): Dashboard + KPIs live")
print("   • Financial structure (8/19): ROIC targets + allocation logic")
print("   • Venture lifecycle (8/18): Stage tracking per venture")

