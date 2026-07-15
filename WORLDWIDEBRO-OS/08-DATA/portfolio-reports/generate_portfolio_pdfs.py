#!/usr/bin/env python3
"""
Portfolio PDF generator — Worldwidebro Holdings.

Renders a 3-tier document set from venture CSV data:
  Tier 1  output/00-HOLDINGS-MASTER.pdf        (entity/trust structure + portfolio roll-up)
  Tier 2  output/sectors/<sector>.pdf          (one book per sector)
  Tier 3  output/ventures/<venture_id>.pdf      (one evaluation packet per venture)

Pure-Python (reportlab) — no LaTeX, no headless browser, no network.

Usage:
  python3 generate_portfolio_pdfs.py                 # everything
  python3 generate_portfolio_pdfs.py --tier master   # just Tier 1
  python3 generate_portfolio_pdfs.py --tier sectors  # Tier 1 + 2
  python3 generate_portfolio_pdfs.py --limit 5       # cap venture packets (smoke test)
  python3 generate_portfolio_pdfs.py --ventures-csv path.csv
"""
import argparse
import csv
import json
import os
from collections import Counter, defaultdict
from datetime import date

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, PageBreak,
)

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.abspath(os.path.join(HERE, "..", "..", ".."))  # /Users/acebless/Documents
CONFIG_PATH = os.path.join(HERE, "config", "holdings_config.json")
DEFAULT_CSV = os.path.join(DOCS, "VENTURES-CAPABILITIES-MAPPED.csv")
REPO_REGISTRY_PATH = os.path.join(
    DOCS, "WORLDWIDEBRO-OS", "08-DATA", "Influence-Venture-Business-OS",
    "REFERENCE", "REPOSITORY-REGISTRY.json",
)
OUT = os.path.join(HERE, "output")
TODAY = date.today().isoformat()


# --------------------------------------------------------------------------- #
# Data loading
# --------------------------------------------------------------------------- #
def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def load_repo_registry(path=REPO_REGISTRY_PATH):
    """Aggregate the repo registry without ever holding all 1,597 records raw in the report."""
    if not os.path.exists(path):
        return None
    with open(path) as f:
        data = json.load(f)
    repos = data.get("repositories", [])
    meta = data.get("metadata", {})
    cats = Counter((r.get("CATEGORY") or "Unclassified") for r in repos)
    linked = sum(1 for r in repos if r.get("related_ventures"))
    top = sorted(repos, key=lambda r: (r.get("strategic_value") or 0, r.get("stars") or 0),
                 reverse=True)[:15]
    return {
        "total": len(repos),
        "owned": meta.get("owned"),
        "starred": meta.get("starred"),
        "generated_at": meta.get("generated_at"),
        "categories": cats.most_common(),
        "linked_to_ventures": linked,
        "top": top,
    }


def opco_for(sector, cfg):
    entry = cfg.get("opco_layer", {}).get("sector_to_opco", {}).get(sector)
    if not entry or not entry.get("opco"):
        return "Unassigned", "unassigned"
    return entry["opco"], entry["confidence"]


def load_ventures(csv_path):
    rows = []
    with open(csv_path, newline="") as f:
        for r in csv.DictReader(f):
            vid = (r.get("venture_id") or "").strip()
            if not vid:
                continue
            rows.append({
                "venture_id": vid,
                "name": (r.get("name") or vid).strip(),
                "sector": (r.get("sector") or "unclassified").strip().lower(),
                "stage": (r.get("stage") or "planned").strip().lower(),
                "status": (r.get("status") or "planned").strip().lower(),
                "capabilities": [c.strip() for c in (r.get("required_capabilities") or "").split("|") if c.strip()],
            })
    return rows


# --------------------------------------------------------------------------- #
# Styling
# --------------------------------------------------------------------------- #
def styles(cfg):
    m = cfg["report_meta"]
    primary = colors.HexColor(m["brand_primary"])
    accent = colors.HexColor(m["brand_accent"])
    muted = colors.HexColor(m["brand_muted"])
    ss = getSampleStyleSheet()
    return {
        "primary": primary, "accent": accent, "muted": muted,
        "title": ParagraphStyle("title", parent=ss["Title"], textColor=primary,
                                 fontSize=26, leading=30, spaceAfter=6),
        "subtitle": ParagraphStyle("subtitle", parent=ss["Normal"], textColor=muted,
                                   fontSize=13, leading=16, spaceAfter=2),
        "h1": ParagraphStyle("h1", parent=ss["Heading1"], textColor=primary,
                             fontSize=16, leading=20, spaceBefore=14, spaceAfter=6),
        "h2": ParagraphStyle("h2", parent=ss["Heading2"], textColor=primary,
                             fontSize=12, leading=15, spaceBefore=10, spaceAfter=4),
        "body": ParagraphStyle("body", parent=ss["Normal"], fontSize=9.5, leading=13, spaceAfter=4),
        "small": ParagraphStyle("small", parent=ss["Normal"], fontSize=8, leading=10, textColor=muted),
        "cell": ParagraphStyle("cell", parent=ss["Normal"], fontSize=8, leading=10),
        "kpi_num": ParagraphStyle("kpi_num", parent=ss["Normal"], fontSize=18, leading=20,
                                  textColor=primary, fontName="Helvetica-Bold", alignment=TA_CENTER),
        "kpi_lbl": ParagraphStyle("kpi_lbl", parent=ss["Normal"], fontSize=8, leading=10,
                                  textColor=muted, alignment=TA_CENTER),
    }


def make_doc(path, cfg, footer_label):
    m = cfg["report_meta"]
    primary = colors.HexColor(m["brand_primary"])
    muted = colors.HexColor(m["brand_muted"])

    def decorate(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(primary)
        canvas.rect(0, letter[1] - 0.35 * inch, letter[0], 0.35 * inch, fill=1, stroke=0)
        canvas.setFillColor(colors.white)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(0.6 * inch, letter[1] - 0.24 * inch, m["title"].upper())
        canvas.drawRightString(letter[0] - 0.6 * inch, letter[1] - 0.24 * inch, footer_label)
        canvas.setFillColor(muted)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(0.6 * inch, 0.4 * inch, f"{m['owner']} · {m['contact']}")
        canvas.drawRightString(letter[0] - 0.6 * inch, 0.4 * inch, f"Generated {TODAY}  ·  Page {doc.page}")
        canvas.restoreState()

    doc = BaseDocTemplate(path, pagesize=letter,
                          leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                          topMargin=0.7 * inch, bottomMargin=0.6 * inch)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=decorate)])
    return doc


def kpi_band(items, s):
    """items = list of (number, label). Returns a Table row of KPI cards."""
    cells = []
    for num, lbl in items:
        inner = Table([[Paragraph(str(num), s["kpi_num"])], [Paragraph(lbl, s["kpi_lbl"])]],
                      colWidths=[1.55 * inch])
        inner.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F1E9")),
            ("BOX", (0, 0), (-1, -1), 0.5, s["accent"]),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))
        cells.append(inner)
    t = Table([cells], colWidths=[1.72 * inch] * len(cells))
    t.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER")]))
    return t


def styled_table(data, s, col_widths, header=True):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1), [colors.white, colors.HexColor("#F7F8FA")]),
        ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#E2E5EA")),
    ]
    if header:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), s["primary"]),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]
    t.setStyle(TableStyle(style))
    return t


# --------------------------------------------------------------------------- #
# Derived analytics
# --------------------------------------------------------------------------- #
STAGE_RANK = {"growth": 4, "active": 4, "validation": 3, "mvp": 2, "development": 2, "planned": 1}


def layer_for(sector, cfg):
    return cfg["sector_to_capital_layer"].get(sector, 1)


def strategic_score(v, cfg):
    """Deterministic ranking: stage maturity + capital-layer revenue weight + capability depth."""
    layer = layer_for(v["sector"], cfg)
    layer_weight = {1: 2, 2: 4, 3: 5, 4: 3}.get(layer, 2)
    return STAGE_RANK.get(v["stage"], 1) * 3 + layer_weight + min(len(v["capabilities"]), 5)


# --------------------------------------------------------------------------- #
# Tier 1 — Holdings Master
# --------------------------------------------------------------------------- #
def build_master(ventures, cfg, s, repo_reg=None):
    story = []
    m = cfg["report_meta"]
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph(m["title"], s["title"]))
    story.append(Paragraph(m["subtitle"], s["subtitle"]))
    story.append(Paragraph(f"As of {TODAY}", s["small"]))
    story.append(Spacer(1, 0.18 * inch))

    sectors = Counter(v["sector"] for v in ventures)
    stages = Counter(v["stage"] for v in ventures)
    active = sum(1 for v in ventures if v["status"] in ("active", "validation", "development"))
    story.append(kpi_band([
        (len(ventures), "Ventures"),
        (len(sectors), "Sectors"),
        (active, "In Motion"),
        (stages.get("active", 0) + stages.get("growth", 0), "Live / Growth"),
    ], s))
    story.append(Spacer(1, 0.18 * inch))

    # 1. Entity & trust structure
    story.append(Paragraph("1 &middot; Entity &amp; Trust Structure", s["h1"]))
    story.append(Paragraph("Ownership flows top-down: the trust holds the holding company, "
                           "which owns the operating LLC, which runs the ventures.", s["body"]))
    ent_rows = [["Lvl", "Entity", "Type", "Role", "Status"]]
    for layer in cfg["entity_structure"]["layers"]:
        ent_rows.append([
            str(layer["level"]),
            Paragraph(f"<b>{layer['name']}</b>", s["cell"]),
            Paragraph(layer["type"], s["cell"]),
            Paragraph(layer["role"], s["cell"]),
            Paragraph(layer["status"], s["cell"]),
        ])
    story.append(styled_table(ent_rows, s,
                              [0.35 * inch, 1.5 * inch, 1.5 * inch, 2.85 * inch, 1.1 * inch]))
    story.append(Spacer(1, 0.06 * inch))
    story.append(Paragraph("Ownership chain: " + "  &rarr;  ".join(
        l["name"] for l in cfg["entity_structure"]["layers"]), s["small"]))

    # 2. Capital stack
    story.append(Paragraph("2 &middot; Capital Stack (4 Layers)", s["h1"]))
    cap_rows = [["Layer", "Name", "Engine", "Target / mo", "Margin"]]
    for c in cfg["capital_layers"]:
        cap_rows.append([str(c["layer"]), Paragraph(f"<b>{c['name']}</b>", s["cell"]),
                         Paragraph(c["engine"], s["cell"]), c["target_monthly"], c["margin"]])
    story.append(styled_table(cap_rows, s,
                              [0.5 * inch, 1.5 * inch, 3.0 * inch, 1.1 * inch, 1.2 * inch]))

    # 3. Sector heat map
    story.append(Paragraph("3 &middot; Portfolio by Sector", s["h1"]))
    sec_rows = [["Sector", "Ventures", "Capital Layer", "Model"]]
    for sec, cnt in sectors.most_common():
        layer = layer_for(sec, cfg)
        ue = cfg["unit_economics_by_layer"][str(layer)]
        sec_rows.append([Paragraph(sec, s["cell"]), str(cnt), f"L{layer}",
                         Paragraph(ue["model"], s["cell"])])
    story.append(styled_table(sec_rows, s,
                              [2.3 * inch, 0.9 * inch, 1.2 * inch, 2.9 * inch]))

    # 4. OPCO layer audit
    story.append(PageBreak())
    story.append(Paragraph("4 &middot; Operating Company (OPCO) Layer &mdash; Audit", s["h1"]))
    story.append(Paragraph("Sectors are grouped under 18 OPCO shells per the Governance Charter. "
                           "\"Approximate\" means the sector was folded into the closest OPCO by judgment call, "
                           "not an explicit prior mapping &mdash; review before treating as final.", s["body"]))
    opco_counts = Counter()
    for v in ventures:
        opco, _ = opco_for(v["sector"], cfg)
        opco_counts[opco] += 1
    all_opco_names = [o["name"] for o in cfg.get("opco_layer", {}).get("opcos", [])]
    sec_to_opco = cfg.get("opco_layer", {}).get("sector_to_opco", {})
    opco_rows = [["OPCO", "Ventures", "Mapped Sectors", "Confidence"]]
    for name in all_opco_names:
        secs = [sec for sec, e in sec_to_opco.items() if e.get("opco") == name]
        conf = {sec_to_opco[sec]["confidence"] for sec in secs} if secs else set()
        opco_rows.append([
            Paragraph(name, s["cell"]),
            str(opco_counts.get(name, 0)),
            Paragraph(", ".join(secs) if secs else "&mdash; none mapped &mdash;", s["cell"]),
            "/".join(sorted(conf)) if conf else "n/a",
        ])
    story.append(styled_table(opco_rows, s,
                              [1.6 * inch, 0.8 * inch, 3.6 * inch, 1.15 * inch]))
    story.append(Spacer(1, 0.1 * inch))
    unassigned_secs = sorted(sec for sec, e in sec_to_opco.items() if not e.get("opco"))
    if unassigned_secs:
        story.append(Paragraph(
            f"&bull; Sectors with no OPCO assignment: {', '.join(unassigned_secs)} "
            f"({opco_counts.get('Unassigned', 0)} ventures) &mdash; needs a Board decision.",
            s["body"]))
    zero_opcos = [n for n in all_opco_names if opco_counts.get(n, 0) == 0]
    if zero_opcos:
        story.append(Paragraph(f"&bull; OPCOs with zero ventures currently assigned: {', '.join(zero_opcos)}.",
                               s["body"]))

    # 5. Repository alignment
    story.append(PageBreak())
    story.append(Paragraph("5 &middot; Repository Alignment", s["h1"]))
    if repo_reg:
        story.append(Paragraph(
            f"Live pull from REPOSITORY-REGISTRY.json (generated {repo_reg.get('generated_at', 'n/a')[:10]}). "
            "This is the honest state, not an aspirational one.", s["body"]))
        story.append(kpi_band([
            (repo_reg["total"], "Total Repos"),
            (repo_reg.get("owned") or "?", "Owned"),
            (repo_reg.get("starred") or "?", "Starred"),
            (f"{repo_reg['linked_to_ventures']}/{repo_reg['total']}", "Linked to a Venture"),
        ], s))
        story.append(Spacer(1, 0.1 * inch))
        pct = (repo_reg["linked_to_ventures"] / repo_reg["total"] * 100) if repo_reg["total"] else 0
        story.append(Paragraph(
            f"&bull; Only {pct:.1f}% of repos carry a related_ventures link &mdash; the repo&harr;venture "
            "join is not yet reliable (known capability-vocabulary mismatch). Treat the table below as "
            "portfolio inventory, not a per-venture build map.", s["body"]))
        story.append(Paragraph("By Category", s["h2"]))
        cat_rows = [["Category", "Repos"]] + [[Paragraph(c, s["cell"]), str(n)]
                                               for c, n in repo_reg["categories"]]
        story.append(styled_table(cat_rows, s, [3.5 * inch, 3.7 * inch]))
        story.append(Paragraph("Top 15 by Strategic Value", s["h2"]))
        top_rows = [["Repo", "Category", "Strategic Value", "Stars"]]
        for r in repo_reg["top"]:
            top_rows.append([Paragraph(r.get("name", ""), s["cell"]),
                             Paragraph(r.get("CATEGORY") or "Unclassified", s["cell"]),
                             str(r.get("strategic_value") or 0), str(r.get("stars") or 0)])
        story.append(styled_table(top_rows, s, [3.2 * inch, 1.8 * inch, 1.2 * inch, 1.0 * inch]))
    else:
        story.append(Paragraph("REPOSITORY-REGISTRY.json not found at build time &mdash; section skipped.",
                               s["body"]))

    # 6. Top ventures by strategic score
    story.append(PageBreak())
    story.append(Paragraph("6 &middot; Top 25 Ventures by Strategic Score", s["h1"]))
    story.append(Paragraph("Score = stage maturity + capital-layer revenue weight + capability depth. "
                           "Model-based ranking for prioritization, not a valuation.", s["small"]))
    top = sorted(ventures, key=lambda v: strategic_score(v, cfg), reverse=True)[:25]
    top_rows = [["#", "Venture", "Sector", "Stage", "Score"]]
    for i, v in enumerate(top, 1):
        top_rows.append([str(i), Paragraph(v["name"], s["cell"]), Paragraph(v["sector"], s["cell"]),
                         v["stage"], str(strategic_score(v, cfg))])
    story.append(styled_table(top_rows, s,
                              [0.35 * inch, 2.6 * inch, 1.7 * inch, 1.2 * inch, 0.7 * inch]))

    # 7. Full index
    story.append(PageBreak())
    story.append(Paragraph("7 &middot; Full Venture Index", s["h1"]))
    idx_rows = [["Venture ID", "Name", "Sector", "OPCO", "Stage"]]
    for v in sorted(ventures, key=lambda x: (x["sector"], x["venture_id"])):
        opco, _ = opco_for(v["sector"], cfg)
        idx_rows.append([Paragraph(v["venture_id"], s["cell"]), Paragraph(v["name"], s["cell"]),
                         Paragraph(v["sector"], s["cell"]), Paragraph(opco, s["cell"]), v["stage"]])
    story.append(styled_table(idx_rows, s,
                              [1.9 * inch, 2.0 * inch, 1.3 * inch, 1.5 * inch, 0.6 * inch]))

    doc = make_doc(os.path.join(OUT, "00-HOLDINGS-MASTER.pdf"), cfg, "Holdings Master")
    doc.build(story)
    return "00-HOLDINGS-MASTER.pdf"


# --------------------------------------------------------------------------- #
# Tier 2 — Sector books
# --------------------------------------------------------------------------- #
def build_sector(sector, vlist, cfg, s):
    story = []
    layer = layer_for(sector, cfg)
    ue = cfg["unit_economics_by_layer"][str(layer)]
    opco, confidence = opco_for(sector, cfg)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(f"Sector Book — {sector.title()}", s["title"]))
    story.append(Paragraph(f"Capital Layer {layer} &middot; {ue['model']} &middot; {opco} "
                           f"({confidence})", s["subtitle"]))
    story.append(Spacer(1, 0.12 * inch))

    stages = Counter(v["stage"] for v in vlist)
    story.append(kpi_band([
        (len(vlist), "Ventures"),
        (stages.get("active", 0) + stages.get("growth", 0), "Live"),
        (stages.get("validation", 0), "Validating"),
        (stages.get("planned", 0), "Planned"),
    ], s))
    story.append(Spacer(1, 0.14 * inch))

    story.append(Paragraph("Sector Economics (model-based)", s["h2"]))
    story.append(styled_table([
        ["Metric", "Value"],
        ["Avg monthly revenue / venture", ue["avg_monthly_revenue"]],
        ["Profit margin", ue["profit_margin"]],
        ["Revenue model", ue["model"]],
        ["Capital layer", f"Layer {layer}"],
    ], s, [3.0 * inch, 4.3 * inch]))

    story.append(Paragraph("Ventures in this Sector", s["h2"]))
    rows = [["Venture ID", "Name", "Stage", "Status"]]
    for v in sorted(vlist, key=lambda x: x["venture_id"]):
        rows.append([Paragraph(v["venture_id"], s["cell"]), Paragraph(v["name"], s["cell"]),
                     v["stage"], v["status"]])
    story.append(styled_table(rows, s, [2.4 * inch, 2.5 * inch, 1.2 * inch, 1.2 * inch]))

    safe = sector.replace("/", "-")
    doc = make_doc(os.path.join(OUT, "sectors", f"{safe}.pdf"), cfg, f"Sector · {sector.title()}")
    doc.build(story)


# --------------------------------------------------------------------------- #
# Tier 3 — Venture packets
# --------------------------------------------------------------------------- #
def build_venture(v, cfg, s):
    story = []
    layer = layer_for(v["sector"], cfg)
    ue = cfg["unit_economics_by_layer"][str(layer)]
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(v["name"], s["title"]))
    story.append(Paragraph(f"{v['venture_id']} &middot; {v['sector'].title()} &middot; Stage: {v['stage'].title()}", s["subtitle"]))
    story.append(Spacer(1, 0.14 * inch))

    story.append(kpi_band([
        (f"L{layer}", "Capital Layer"),
        (v["stage"].title(), "Stage"),
        (v["status"].title(), "Status"),
        (len(v["capabilities"]), "Capabilities"),
    ], s))
    story.append(Spacer(1, 0.16 * inch))

    opco, confidence = opco_for(v["sector"], cfg)
    story.append(Paragraph("Evaluation Snapshot", s["h2"]))
    story.append(styled_table([
        ["Field", "Value"],
        ["Venture ID", v["venture_id"]],
        ["Sector", v["sector"].title()],
        ["OPCO", f"{opco} ({confidence} match)"],
        ["Capital layer", f"Layer {layer} — {ue['model']}"],
        ["Stage / Status", f"{v['stage'].title()} / {v['status'].title()}"],
        ["Owning entity", "Winners Circle WC LLC (operating)"],
    ], s, [2.2 * inch, 5.1 * inch]))

    story.append(Paragraph("Unit Economics (model-based projection)", s["h2"]))
    story.append(Paragraph("Estimated from the venture's capital layer, not actuals. "
                           "Replace with live metrics from Supabase when available.", s["small"]))
    story.append(styled_table([
        ["Metric", "Value"],
        ["Avg monthly revenue", ue["avg_monthly_revenue"]],
        ["Profit margin", ue["profit_margin"]],
        ["Revenue model", ue["model"]],
    ], s, [2.2 * inch, 5.1 * inch]))

    story.append(Paragraph("Required Capabilities", s["h2"]))
    if v["capabilities"]:
        cap_rows = [["#", "Capability"]]
        for i, c in enumerate(v["capabilities"], 1):
            cap_rows.append([str(i), Paragraph(c, s["cell"])])
        story.append(styled_table(cap_rows, s, [0.4 * inch, 6.9 * inch]))
    else:
        story.append(Paragraph("No capabilities mapped yet — run capability cross-reference to populate.", s["body"]))

    story.append(Paragraph("Risk Register (auto-flagged)", s["h2"]))
    risks = []
    if v["stage"] == "planned":
        risks.append("Pre-MVP — unvalidated demand and no revenue signal.")
    if not v["capabilities"]:
        risks.append("No capabilities/repos mapped — build path undefined.")
    if layer == 3:
        risks.append("Acquisition layer — requires capital and diligence before activation.")
    if not risks:
        risks.append("No structural risks flagged at this stage.")
    for r in risks:
        story.append(Paragraph(f"&bull; {r}", s["body"]))

    safe = v["venture_id"].replace("/", "-")
    doc = make_doc(os.path.join(OUT, "ventures", f"{safe}.pdf"), cfg, f"Packet · {v['venture_id']}")
    doc.build(story)


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=["master", "sectors", "all"], default="all")
    ap.add_argument("--limit", type=int, default=0, help="cap number of venture packets (0 = all)")
    ap.add_argument("--ventures-csv", default=DEFAULT_CSV)
    args = ap.parse_args()

    cfg = load_config()
    s = styles(cfg)
    ventures = load_ventures(args.ventures_csv)
    os.makedirs(os.path.join(OUT, "sectors"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "ventures"), exist_ok=True)
    print(f"Loaded {len(ventures)} ventures from {os.path.basename(args.ventures_csv)}")

    repo_reg = load_repo_registry()
    if repo_reg:
        print(f"Loaded repo registry: {repo_reg['total']} repos "
              f"({repo_reg['linked_to_ventures']} linked to a venture)")
    else:
        print("Repo registry not found — Repository Alignment section will be skipped")

    master = build_master(ventures, cfg, s, repo_reg)
    print(f"  OK Tier 1: {master}")
    if args.tier == "master":
        return

    by_sector = defaultdict(list)
    for v in ventures:
        by_sector[v["sector"]].append(v)
    for sec, vlist in sorted(by_sector.items()):
        build_sector(sec, vlist, cfg, s)
    print(f"  OK Tier 2: {len(by_sector)} sector books")
    if args.tier == "sectors":
        return

    pkt = ventures[: args.limit] if args.limit else ventures
    for i, v in enumerate(pkt, 1):
        build_venture(v, cfg, s)
        if i % 100 == 0:
            print(f"     ... {i}/{len(pkt)} venture packets")
    print(f"  OK Tier 3: {len(pkt)} venture packets")
    print(f"\nOutput -> {OUT}")


if __name__ == "__main__":
    main()
