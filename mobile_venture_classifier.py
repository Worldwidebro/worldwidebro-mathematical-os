#!/usr/bin/env python3
"""
Mobile Venture Classifier v2
- Identifies mobile-first ventures
- Maps to 6 archetypes
- Finds competitors
- Defines AI-enhanced features
- Scores all ventures
- Outputs CSV + dashboard
"""

import csv
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Mobile Venture Archetypes
ARCHETYPES = {
    "marketplace": {
        "description": "2-sided marketplace (buyers + sellers in-app)",
        "examples": ["TaskRabbit", "Wonolo", "Handy", "Uber", "DoorDash"],
        "tech_stacks": ["React Native", "Flutter", "iOS", "Android"],
        "key_features": ["real-time matching", "payments", "ratings", "in-app messaging"],
        "competitors": {
            "local_services": ["TaskRabbit", "Handy", "Care.com", "Angi"],
            "staffing": ["Wonolo", "Instawork", "Snapshift"],
            "delivery": ["DoorDash", "Instacart", "Amazon Flex"],
            "gig": ["Uber", "Lyft", "Lime"],
        },
        "ai_features": [
            "Predictive matching (ML)",
            "Dynamic pricing (AI)",
            "Fraud detection (ML)",
            "Auto-dispatch (AI)",
            "Churn prediction (ML)",
            "Demand forecasting (AI)"
        ]
    },
    
    "saas_tool": {
        "description": "Productivity/management SaaS with mobile companion",
        "examples": ["Slack", "Notion", "Asana", "Monday", "Linear"],
        "tech_stacks": ["React Native", "Flutter", "iOS", "Android"],
        "key_features": ["collaboration", "workflows", "integrations", "notifications"],
        "competitors": {
            "project_mgmt": ["Asana", "Monday", "ClickUp", "Linear"],
            "communication": ["Slack", "Teams", "Discord"],
            "notes": ["Notion", "Obsidian", "OneNote"],
        },
        "ai_features": [
            "AI task automation",
            "Smart scheduling",
            "Auto-summarization",
            "Predictive analytics",
            "Natural language search",
            "Workflow optimization"
        ]
    },
    
    "content_community": {
        "description": "Content platform + community (TikTok, YouTube, Substack style)",
        "examples": ["TikTok", "YouTube", "Substack", "Discord", "Patreon"],
        "tech_stacks": ["React Native", "Flutter", "iOS", "Android"],
        "key_features": ["video upload", "social feed", "monetization", "discovery"],
        "competitors": {
            "short_form": ["TikTok", "Instagram Reels", "YouTube Shorts"],
            "long_form": ["YouTube", "Vimeo"],
            "writing": ["Substack", "Medium", "Ghost"],
            "community": ["Discord", "Telegram", "Mighty Networks"]
        },
        "ai_features": [
            "AI recommendations",
            "Automated thumbnails",
            "Transcription + captions",
            "Content moderation (ML)",
            "Hashtag suggestion",
            "Trend prediction"
        ]
    },
    
    "health_wellness": {
        "description": "Health, fitness, or mental wellness app (tracking, coaching, telemedicine)",
        "examples": ["Fitbit", "Calm", "Headspace", "Teladoc", "Peloton"],
        "tech_stacks": ["React Native", "Flutter", "iOS", "Android"],
        "key_features": ["tracking", "wearable sync", "coaching", "social challenges"],
        "competitors": {
            "fitness": ["Fitbit", "Strava", "Peloton", "Apple Fitness"],
            "mental_health": ["Calm", "Headspace", "Insight Timer"],
            "telemedicine": ["Teladoc", "Ro", "GoodRx"],
        },
        "ai_features": [
            "Personalized workout plans",
            "Health predictions (ML)",
            "Smart coaching (AI)",
            "Medication reminders",
            "Risk assessment (ML)",
            "Habit optimization (AI)"
        ]
    },
    
    "fintech_wealth": {
        "description": "Financial management (investing, banking, payments, crypto)",
        "examples": ["Stripe", "Revolut", "Robinhood", "Coinbase", "SoFi"],
        "tech_stacks": ["React Native", "Flutter", "iOS", "Android"],
        "key_features": ["account management", "transactions", "investing", "security"],
        "competitors": {
            "banking": ["Revolut", "Chime", "Square Cash", "SoFi"],
            "investing": ["Robinhood", "M1", "Wealthfront"],
            "crypto": ["Coinbase", "Kraken", "Phantom"],
            "payments": ["Stripe", "Square", "PayPal"],
        },
        "ai_features": [
            "Portfolio optimization",
            "Fraud prevention (ML)",
            "Tax optimization",
            "Spending insights (AI)",
            "Credit scoring",
            "Investment recommendations"
        ]
    },
    
    "b2b_enterprise": {
        "description": "B2B tools for sales, support, HR, or operations",
        "examples": ["Salesforce", "HubSpot", "Zendesk", "ADP", "Workday"],
        "tech_stacks": ["React Native", "Flutter", "iOS", "Android"],
        "key_features": ["CRM", "dashboards", "reporting", "integrations"],
        "competitors": {
            "crm": ["Salesforce", "HubSpot", "Pipedrive"],
            "support": ["Zendesk", "Intercom", "Freshdesk"],
            "hr": ["Workday", "BambooHR", "Gusto"],
        },
        "ai_features": [
            "Sales forecasting",
            "Lead scoring (ML)",
            "Auto-response (AI)",
            "Sentiment analysis",
            "Churn prediction",
            "Performance optimization"
        ]
    }
}

# Scoring weights
MOBILE_INDICATORS = {
    "real-time": 0.3,  # needs live updates
    "location": 0.3,   # location-dependent
    "task": 0.2,       # task/micro-transaction based
    "community": 0.2,  # social/community features
    "notification": 0.15,  # push notifications help
    "offline": 0.1,    # offline-first useful
}

def classify_venture(venture_name: str, description: str, sector: str) -> Tuple[str, float, List[str]]:
    """Classify venture into archetype with confidence score"""
    
    text = f"{venture_name} {description} {sector}".lower()
    
    scores = {}
    
    # Marketplace detection
    if any(w in text for w in ["marketplace", "2-sided", "buyer", "seller", "service", "booking", "task", "gig", "freelance", "dispatch"]):
        scores["marketplace"] = scores.get("marketplace", 0) + 0.5
    if any(w in text for w in ["payment", "matching", "contractor"]):
        scores["marketplace"] = scores.get("marketplace", 0) + 0.3
    
    # SaaS tool detection
    if any(w in text for w in ["saas", "productivity", "management", "workflow", "collaboration", "team", "project", "crm"]):
        scores["saas_tool"] = scores.get("saas_tool", 0) + 0.5
    
    # Content/Community detection
    if any(w in text for w in ["content", "video", "social", "community", "creator", "streaming", "feed", "discovery"]):
        scores["content_community"] = scores.get("content_community", 0) + 0.5
    if any(w in text for w in ["youtube", "tiktok", "discord", "substack", "platform"]):
        scores["content_community"] = scores.get("content_community", 0) + 0.3
    
    # Health/Wellness detection
    if any(w in text for w in ["health", "fitness", "wellness", "mental", "meditation", "therapy", "coaching", "tracking", "wearable"]):
        scores["health_wellness"] = scores.get("health_wellness", 0) + 0.6
    
    # Fintech detection
    if any(w in text for w in ["fintech", "payment", "banking", "crypto", "investing", "wealth", "tax", "money"]):
        scores["fintech_wealth"] = scores.get("fintech_wealth", 0) + 0.6
    if any(w in text for w in ["transaction", "account", "finance", "portfolio"]):
        scores["fintech_wealth"] = scores.get("fintech_wealth", 0) + 0.3
    
    # B2B Enterprise detection
    if any(w in text for w in ["b2b", "enterprise", "salesforce", "zendesk", "support", "hr", "admin", "analytics"]):
        scores["b2b_enterprise"] = scores.get("b2b_enterprise", 0) + 0.5
    
    if not scores:
        return None, 0, []
    
    archetype = max(scores, key=scores.get)
    confidence = min(scores[archetype], 1.0)
    
    return archetype, confidence, list(scores.keys())

def main():
    ventures_file = Path("/Users/acebless/Documents/ventures_updated_2026-05-15.csv")
    
    if not ventures_file.exists():
        print(f"❌ {ventures_file} not found")
        return
    
    results = []
    archetype_counts = {}
    
    with open(ventures_file, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            venture_id = row.get('ID', '')
            name = row.get('Name', '')
            desc = row.get('Description', '')
            sector = row.get('Sector', '')
            
            archetype, confidence, candidates = classify_venture(name, desc, sector)
            
            if archetype and confidence >= 0.2:  # minimum confidence
                arch_data = ARCHETYPES[archetype]
                tech_stacks = ", ".join(arch_data['tech_stacks'][:2])
                competitors = ", ".join(list(arch_data['competitors'].values())[0][:2])
                ai_features = " | ".join(arch_data['ai_features'][:3])
                
                results.append({
                    'venture_id': venture_id[:8],
                    'name': name,
                    'sector': sector,
                    'mobile_archetype': archetype,
                    'confidence': f"{confidence:.1%}",
                    'tech_stack': tech_stacks,
                    'top_competitors': competitors,
                    'ai_features': ai_features,
                    'candidates': ",".join(candidates),
                })
                
                archetype_counts[archetype] = archetype_counts.get(archetype, 0) + 1
                
                if i % 100 == 0:
                    print(f"Classified {i} ventures...")
    
    # Write output CSV
    output_file = Path("/Users/acebless/Documents/MOBILE-VENTURES-CLASSIFIED.csv")
    if results:
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        
        print(f"\n✅ Classified {len(results)} mobile ventures")
        print(f"📊 Breakdown by archetype:")
        for arch, count in sorted(archetype_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {arch}: {count}")
        
        print(f"\n📁 Output: {output_file}")
    else:
        print("❌ No mobile ventures classified")

if __name__ == "__main__":
    main()
