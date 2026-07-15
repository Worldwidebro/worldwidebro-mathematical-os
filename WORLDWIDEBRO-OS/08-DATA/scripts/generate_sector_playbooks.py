#!/usr/bin/env python3
"""
generate_sector_playbooks.py
Generates professional PDF playbooks for all portfolio sectors using ReportLab.
"""
import os
import sys
import yaml
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

DOCS = "/Users/acebless/Documents"
REGISTRIES = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries"
OUT_DIR = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/financials/reports"

SECTORS_REGISTRY = f"{REGISTRIES}/sector_registry.yaml"
TOOLS_REGISTRY = f"{REGISTRIES}/agent_tools_registry.yaml"
CAPABILITIES_REGISTRY = f"{REGISTRIES}/capability_registry.yaml"


def log(msg):
    print(f"[*] {msg}", file=sys.stderr)


def load_yaml(path):
    if not os.path.exists(path):
        sys.exit(f"Error: Registry not found at {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    log("Loading registries...")
    sectors_data = load_yaml(SECTORS_REGISTRY).get("sectors", [])
    tools_data = load_yaml(TOOLS_REGISTRY).get("tools", [])
    caps_data = load_yaml(CAPABILITIES_REGISTRY).get("capabilities", [])

    os.makedirs(OUT_DIR, exist_ok=True)

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=15
    )
    h2_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0284c7'),
        spaceBefore=12,
        spaceAfter=8
    )
    body_style = ParagraphStyle(
        'ReportBody',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#334155')
    )
    bold_style = ParagraphStyle(
        'ReportBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    white_bold = ParagraphStyle(
        'WhiteBold',
        parent=body_style,
        fontName='Helvetica-Bold',
        textColor=colors.white
    )

    t_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0f172a')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#f8fafc'), colors.HexColor('#f1f5f9')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ])

    for sector in sectors_data:
        name = sector.get("name", "unknown")
        label = sector.get("label", name.title())
        log(f"Compiling playbook PDF for sector: {label}...")

        pdf_path = f"{OUT_DIR}/{name}_playbook.pdf"
        doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
        story = []

        # Header Title
        story.append(Paragraph(f"IZA OS Sector Playbook: {label}", title_style))
        story.append(Paragraph("System specifications, automated agent workforce, and capability mappings.", body_style))
        story.append(Spacer(1, 10))

        # 1. Workforce Section
        story.append(Paragraph("1. Automated Agent Workforce", h2_style))
        agent_table_data = [[Paragraph("Role / Profile", white_bold), Paragraph("Assigned Agent Instance", white_bold)]]
        for agent in sector.get("agents", []):
            agent_table_data.append([
                Paragraph(agent.get("role", ""), bold_style),
                Paragraph(agent.get("name", "Unassigned Agent"), body_style)
            ])
        
        agent_table = Table(agent_table_data, colWidths=[150, 390])
        agent_table.setStyle(t_style)
        story.append(agent_table)
        story.append(Spacer(1, 12))

        # 2. Mapped Capabilities Section
        story.append(Paragraph("2. Required Sector Capabilities & Code Blueprints", h2_style))
        caps_table_data = [[
            Paragraph("Capability", white_bold), 
            Paragraph("Category", white_bold), 
            Paragraph("Description", white_bold), 
            Paragraph("Reference Repositories", white_bold)
        ]]
        
        for cap_name in sector.get("required_capabilities", []):
            cap_info = next((c for c in caps_data if c.get("name") == cap_name), {})
            repos_str = ", ".join(cap_info.get("repos", []))
            caps_table_data.append([
                Paragraph(cap_name.upper(), bold_style),
                Paragraph(cap_info.get("type", "system"), body_style),
                Paragraph(cap_info.get("description", ""), body_style),
                Paragraph(repos_str, body_style)
            ])

        caps_table = Table(caps_table_data, colWidths=[100, 70, 220, 150])
        caps_table.setStyle(t_style)
        story.append(caps_table)
        story.append(Spacer(1, 12))

        # 3. OS Layers & Tools Section
        story.append(Paragraph("3. OS Layer Allocations & Active Tool Runtimes", h2_style))
        tools_table_data = [[
            Paragraph("Execution Layer", white_bold), 
            Paragraph("Tool Name", white_bold), 
            Paragraph("Category", white_bold), 
            Paragraph("Capabilities Enabled", white_bold)
        ]]

        sector_roles = [a.get("role", "").lower() for a in sector.get("agents", [])]
        for tool in tools_data:
            bindings = [b.lower() for b in tool.get("agent_bindings", [])]
            # Match if no bindings (general tool) or intersections with sector agent roles
            is_matched = len(bindings) == 0 or any(any(r in b for r in sector_roles) for b in bindings)
            if is_matched:
                tools_table_data.append([
                    Paragraph(tool.get("layer", ""), bold_style),
                    Paragraph(tool.get("name", ""), bold_style),
                    Paragraph(tool.get("category", ""), body_style),
                    Paragraph(", ".join(tool.get("capabilities", [])), body_style)
                ])

        tools_table = Table(tools_table_data, colWidths=[110, 90, 110, 230])
        tools_table.setStyle(t_style)
        story.append(tools_table)
        story.append(Spacer(1, 12))

        # 4. Competitor Mappings Section
        story.append(Paragraph("4. Enterprise Competitor & System Equivalents", h2_style))
        comp_table_data = [[
            Paragraph("Enterprise Competitor", white_bold), 
            Paragraph("System Description", white_bold), 
            Paragraph("IZA OS Mapped Equivalents", white_bold)
        ]]

        comp_maps = [
            { "caps": ["storefront", "payments"], "comp": "Shopify / WooCommerce", "desc": "Medusa API storefront + Stripe automated ledger" },
            { "caps": ["crm", "workspace"], "comp": "Salesforce / HubSpot", "desc": "Twenty CRM client pipelines + local SQLite/Postgres logs" },
            { "caps": ["automation", "scheduling"], "comp": "Zapier / Make.com", "desc": "n8n visual flow nodes + scheduling cron triggers" },
            { "caps": ["rag", "graph"], "comp": "Pinecone / OpenAI RAG", "desc": "Qdrant vector indexes + Neo4j Cypher capability joins" },
            { "caps": ["devtools", "mcp"], "comp": "GitHub Copilot / Vibe", "desc": "gitnexus-cli code graphs + MCP server runtime proxy gateways" }
        ]

        relevant_comps = [c for c in comp_maps if any(cap in sector.get("required_capabilities", []) for cap in c["caps"])]
        if relevant_comps:
            for item in relevant_comps:
                comp_table_data.append([
                    Paragraph(item["comp"], bold_style),
                    Paragraph(item["desc"], body_style),
                    Paragraph("Active & Configured", body_style)
                ])
            comp_table = Table(comp_table_data, colWidths=[150, 240, 150])
            comp_table.setStyle(t_style)
            story.append(comp_table)
        else:
            story.append(Paragraph("General system utility scripts mapped across all active namespaces.", body_style))

        # Build Document
        doc.build(story)
        log(f"Playbook PDF successfully created at {pdf_path}")

        # Also copy to VEX Hero site public assets
        vex_public_dir = f"{DOCS}/vex-hero-site/public/playbooks"
        os.makedirs(vex_public_dir, exist_ok=True)
        import shutil
        shutil.copy2(pdf_path, os.path.join(vex_public_dir, f"{name}_playbook.pdf"))

    log("All sector playbook PDFs successfully generated!")


if __name__ == "__main__":
    main()
