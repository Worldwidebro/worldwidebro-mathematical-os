"""Bulk rule-based revenue model generator for all 712 ventures.

Reads WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv (venture_id,name,sector,opco,
stage,status) and assigns each venture a monetization archetype + pricing range based
on keyword matches in its name, falling back to a per-sector default. This replaces
guessing per-venture with a transparent, re-runnable rule set (see FIN-REVENUE-MODELS.md
for the hand-reasoned version covering the 36 FIN ventures this generalizes from).

Output: VENTURE-REVENUE-MODELS.csv (venture_id, name, sector, opco, revenue_model,
pricing_range, basis)
"""
import csv

SRC = "/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv"
OUT = "/Users/acebless/Documents/VENTURE-REVENUE-MODELS.csv"

# (keywords, model, pricing_range) — first match wins, checked in order
KEYWORD_RULES = [
    (["marketplace"], "Marketplace take-rate", "8-20% of GMV"),
    (["affiliate", "rental affiliate", "referral"], "Affiliate commission", "5-15% per referred transaction"),
    (["staffing", "recruit", "hiring", "talent"], "Placement fee", "15-25% of first-year salary"),
    (["payroll"], "Per-employee SaaS fee", "$5-10 / employee / month"),
    (["payment", "gateway", "remittance", "escrow", "invoice factoring"], "Per-transaction fee", "1-3% + flat fee per transaction"),
    (["insurance", "underwriting"], "Premium-based fee", "% of referred premium or per-policy fee"),
    (["portfolio", "wealth", "treasury", "asset management", "investment"], "AUM / management fee", "0.25-1% of assets managed"),
    (["crowdfunding", "investor dashboard", "venture capital", "vc "], "Capital-raise fee", "5-8% of funds raised"),
    (["tax prep", "tax filing", "tax preparation"], "Per-filing fee", "$49-249 per return"),
    (["bookkeeping", "accounting", "expense"], "Subscription (accounting SaaS)", "$49-149 / month"),
    (["formation", "registered agent"], "Flat formation fee", "$99-499 one-time + annual renewal"),
    (["legal", "patent", "contract"], "Per-document fee or subscription", "$29-79 / month or per-document"),
    (["logistics", "delivery", "freight", "transport", "shipping", "garbage", "waste"], "Per-shipment / per-route fee", "B2B SaaS, per-route or per-unit fee"),
    (["course", "tutor", "training", "education", "coaching", "coach"], "Course fee or subscription", "$19-99 one-time or /month"),
    (["content", "media", "video", "podcast", "publishing"], "Ad revenue + subscription", "CPM/sponsorship + $5-15/month premium tier"),
    (["construction", "contractor", "roofing", "plumbing", "electrical"], "Project fee / margin", "10-20% margin on job value"),
    (["beauty", "wellness", "spa", "salon"], "Membership / per-session fee", "$29-99/month membership or per-session"),
    (["fitness", "sports", "gym", "coach"], "Membership subscription", "$29-79/month"),
    (["food", "hospitality", "restaurant", "catering"], "Transaction commission / SaaS", "2-4% per order or $49-149/month POS SaaS"),
    (["real estate", "property"], "Transaction commission", "1-3% of transaction value"),
    (["compliance", "audit", "kyc", "aml", "regulatory"], "B2B compliance SaaS", "$199-499/month per institution monitored"),
    (["seo", "marketing", "ranker"], "Local SaaS subscription", "$99-299/month per business"),
    (["dashboard", "analytics", "insight"], "B2B SaaS subscription", "$49-199/month per seat"),
    (["ai", "automation", "saas", "hub", "assistant", "optimizer", "builder", "generator"], "Subscription SaaS", "$29-99/month"),
]

SECTOR_DEFAULTS = {
    "financial": ("Subscription SaaS", "$49-149/month"),
    "e-commerce": ("Marketplace take-rate", "8-15% of GMV"),
    "operations": ("B2B SaaS subscription", "$49-199/month per seat"),
    "technology": ("Subscription SaaS", "$29-99/month"),
    "specialized": ("Project / consulting fee", "quoted per engagement"),
    "emerging": ("Subscription SaaS", "$29-99/month"),
    "community": ("Membership subscription", "$9-29/month"),
    "education": ("Course fee or subscription", "$19-99 one-time or /month"),
    "beauty-wellness": ("Membership / per-session fee", "$29-99/month"),
    "food-hospitality": ("Transaction commission / SaaS", "2-4% per order or $49-149/month"),
    "software-technology": ("Subscription SaaS", "$29-99/month"),
    "logistics-transport": ("Per-shipment / per-route fee", "B2B SaaS, per-route or per-unit fee"),
    "professional-services": ("Retainer / project fee", "quoted per engagement"),
    "fitness-sports": ("Membership subscription", "$29-79/month"),
    "media-content": ("Ad revenue + subscription", "CPM/sponsorship + $5-15/month"),
    "construction": ("Project fee / margin", "10-20% margin on job value"),
    "education-training": ("Course fee or subscription", "$19-99 one-time or /month"),
    "real-estate": ("Transaction commission", "1-3% of transaction value"),
}


def classify(name: str, sector: str) -> tuple[str, str, str]:
    lower = name.lower()
    for keywords, model, pricing in KEYWORD_RULES:
        if any(k in lower for k in keywords):
            return model, pricing, f"keyword match: {[k for k in keywords if k in lower][0]}"
    model, pricing = SECTOR_DEFAULTS.get(sector, ("Subscription SaaS", "$29-99/month"))
    return model, pricing, f"sector default: {sector}"


def main() -> None:
    with open(SRC, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    out_rows = []
    for row in rows:
        venture_id = row.get("venture_id", "").strip()
        if not venture_id or venture_id == "venture_id":
            continue
        name = row.get("name", "")
        sector = row.get("sector", "")
        opco = row.get("opco", "")
        model, pricing, basis = classify(name, sector)
        out_rows.append(
            {
                "venture_id": venture_id,
                "name": name,
                "sector": sector,
                "opco": opco,
                "revenue_model": model,
                "pricing_range": pricing,
                "basis": basis,
            }
        )

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["venture_id", "name", "sector", "opco", "revenue_model", "pricing_range", "basis"],
        )
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} rows to {OUT}")


if __name__ == "__main__":
    main()
