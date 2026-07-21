#!/usr/bin/env python3
"""
compile_playbook_pdf.py
Compiles a venture's markdown documentation files into a unified, formatted PDF playbook.
Runs locally using ReportLab with 0 tokens.
"""
import os
import sys
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def parse_markdown(filepath):
    if not os.path.exists(filepath):
        return "", ""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    metadata_text = ""
    body = content
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if fm_match:
        metadata_text = fm_match.group(1)
        body = content[fm_match.end():]
        
    return metadata_text, body

def build_pdf(venture_dir, output_path):
    print(f"📄 Compiling live PDF playbook for: {os.path.basename(venture_dir)}")
    docs_dir = os.path.join(venture_dir, "docs")
    if not os.path.exists(docs_dir):
        # Support v2 directories
        docs_dir = os.path.join(venture_dir, "00_IDENTITY")
        if not os.path.exists(docs_dir):
            docs_dir = venture_dir # Fallback to root
            
    # Gather document files
    doc_files = [
        ("CAPABILITY-STATEMENT.md", "1. Capability Statement"),
        ("SALES-SCRIPTS.md", "2. Sales & Outreach Scripts"),
        ("FORMATION-CREDENTIAL-TRACKER.md", "3. Formation & Credentials"),
        ("AGENT-COMMUNICATION.md", "4. AI Agent Communication & Protocols"),
        ("DEPARTMENTS-AND-ECOSYSTEM.md", "5. Department Integrations")
    ]
    
    # Set up PDF Document
    doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
    styles = getSampleStyleSheet()
    story = []
    
    # Custom Palette
    primary_color = colors.HexColor('#0f172a') # Slate 900
    accent_color = colors.HexColor('#2563eb')  # Blue 600
    
    title_style = ParagraphStyle(
        'PlaybookTitle',
        parent=styles['Heading1'],
        fontSize=26,
        leading=30,
        textColor=primary_color,
        spaceAfter=10
    )
    
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=16,
        leading=20,
        textColor=accent_color,
        spaceBefore=15,
        spaceAfter=10
    )
    
    body_style = ParagraphStyle(
        'PlaybookBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155'),
        spaceAfter=8
    )
    
    meta_style = ParagraphStyle(
        'PlaybookMeta',
        parent=styles['Code'],
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#64748b'),
        spaceAfter=15
    )

    # Title Page Page Layout
    story.append(Paragraph(f"WORLDWIDEBRO-OS PLAYBOOK", section_style))
    story.append(Paragraph(os.path.basename(venture_dir).replace('-', ' '), title_style))
    story.append(Paragraph(f"Generated on: {os.popen('date').read().strip()}", body_style))
    story.append(Spacer(1, 20))
    story.append(PageBreak())
    
    # Append each markdown document
    for filename, display_name in doc_files:
        filepath = os.path.join(docs_dir, filename)
        # Search in root if not in docs
        if not os.path.exists(filepath):
            filepath = os.path.join(venture_dir, filename)
            
        if os.path.exists(filepath):
            meta, body = parse_markdown(filepath)
            story.append(Paragraph(display_name, section_style))
            if meta:
                story.append(Paragraph(f"--- Metadata ---\n{meta.strip()}", meta_style))
            
            # Simple markdown formatting to PDF paragraphs
            for paragraph in body.split("\n\n"):
                if paragraph.strip():
                    # Clean markdown formatting tags like **, *
                    cleaned = paragraph.replace("**", "").replace("*", "")
                    story.append(Paragraph(cleaned.strip().replace('\n', '<br/>'), body_style))
            story.append(Spacer(1, 15))
            story.append(PageBreak())
            
    doc.build(story)
    print(f"✅ Unified PDF Playbook compiled at: {output_path}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 compile_playbook_pdf.py <VentureDir> <OutputPath>")
        sys.exit(1)
        
    v_dir = sys.argv[1]
    out_path = sys.argv[2]
    build_pdf(v_dir, out_path)

if __name__ == "__main__":
    main()
