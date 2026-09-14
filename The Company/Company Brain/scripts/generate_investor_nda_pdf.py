#!/usr/bin/env python3
"""
Generate publication-grade PDF for WorldwideBro Holdings LLC
Investor Demonstration & Confidentiality Agreement (NDA) with Non-Circumvention.
Uses fpdf2 via `uv run --with fpdf2`.
"""

import sys
import os
from fpdf import FPDF

class NDAPDF(FPDF):
    def header(self):
        # Header banner on every page
        self.set_font("Helvetica", "B", 7.5)
        self.set_text_color(15, 23, 42) # Slate 900
        self.cell(90, 5, "WORLDWIDEBRO HOLDINGS LLC | RE-001 DEAL ENGINE", border=0, align="L")
        self.set_font("Helvetica", "", 7.5)
        self.set_text_color(100, 116, 139) # Slate 500
        self.cell(85.9, 5, "INVESTOR DEMO & EVALUATION NDA", border=0, align="R")
        self.ln(6)
        self.set_draw_color(203, 213, 225) # Slate 300
        self.set_line_width(0.3)
        self.line(20, self.get_y(), 195.9, self.get_y())
        self.ln(4)

    def footer(self):
        # Footer on every page
        self.set_y(-16)
        self.set_draw_color(203, 213, 225)
        self.set_line_width(0.3)
        self.line(20, self.get_y(), 195.9, self.get_y())
        self.ln(2.5)
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(185, 28, 28) # Red 700
        self.cell(34, 4, "STRICTLY CONFIDENTIAL", border=0, align="L")
        self.set_font("Helvetica", "", 7)
        self.set_text_color(100, 116, 139)
        self.cell(92, 4, " |  WorldwideBro Holdings LLC  *  Protected by U.S. E-SIGN Act & DTSA", border=0, align="L")
        self.cell(49.9, 4, f"Page {self.page_no()} of {{nb}}", border=0, align="R")

def build_nda_pdf(output_path):
    pdf = NDAPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_margins(left=20, top=18, right=20)
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.alias_nb_pages()
    pdf.add_page()

    # Document Header Title Block
    pdf.set_fill_color(248, 250, 252) # Slate 50
    pdf.set_draw_color(226, 232, 240) # Slate 200
    pdf.rect(20, pdf.get_y(), 175.9, 20, style="FD")
    
    pdf.set_xy(20, pdf.get_y() + 2.5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(175.9, 5.5, "MUTUAL CONFIDENTIALITY, PROPRIETARY RIGHTS &", border=0, align="C")
    pdf.ln(5.5)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(175.9, 5, "NON-CIRCUMVENTION AGREEMENT", border=0, align="C")
    pdf.ln(4.5)
    pdf.set_font("Helvetica", "I", 7.5)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(175.9, 4, "(Platform Demonstration, Algorithmic Underwriting & Investor Due Diligence)", border=0, align="C")
    pdf.ln(7.5)

    # Party Information Block (2 Columns)
    y_before_parties = pdf.get_y()
    col_w = 85.5
    gap = 4.9

    # Disclosing Party Box (Left)
    pdf.set_fill_color(241, 245, 249) # Slate 100
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(20, y_before_parties, col_w, 36, style="FD")
    pdf.set_xy(22, y_before_parties + 2)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(col_w - 4, 4.5, "DISCLOSING / SPONSORING PARTY:", border=0, align="L")
    pdf.ln(4.5)
    pdf.set_x(22)
    pdf.set_font("Helvetica", "B", 8)
    pdf.cell(col_w - 4, 4, "WorldwideBro Holdings LLC", border=0, align="L")
    pdf.ln(4)
    pdf.set_x(22)
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(71, 85, 105)
    pdf.multi_cell(col_w - 4, 3.5, "Jurisdiction: North Carolina / Delaware\nPrincipal Office: Charlotte, NC 28202\nContact: legal@worldwidebro.com\nLive System: re-001-worldwidebro-holdings.vercel.app\nManaging Member: Ace Bless, CEO")

    # Receiving Party Box (Right)
    pdf.set_fill_color(248, 250, 252)
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(20 + col_w + gap, y_before_parties, col_w, 36, style="FD")
    pdf.set_xy(20 + col_w + gap + 2, y_before_parties + 2)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(col_w - 4, 4.5, "RECEIVING PARTY / PROSPECTIVE INVESTOR:", border=0, align="L")
    pdf.ln(4.5)
    pdf.set_x(20 + col_w + gap + 2)
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(col_w - 4, 4, "Legal Entity: _________________________________", border=0, align="L")
    pdf.ln(4)
    pdf.set_x(20 + col_w + gap + 2)
    pdf.cell(col_w - 4, 4, "Authorized Signer: ____________________________", border=0, align="L")
    pdf.ln(4)
    pdf.set_x(20 + col_w + gap + 2)
    pdf.cell(col_w - 4, 4, "Title: ________________________________________", border=0, align="L")
    pdf.ln(4)
    pdf.set_x(20 + col_w + gap + 2)
    pdf.cell(col_w - 4, 4, "Email: ________________________________________", border=0, align="L")
    pdf.ln(4)
    pdf.set_x(20 + col_w + gap + 2)
    pdf.cell(col_w - 4, 4, "Effective Date: ________________________, 202___", border=0, align="L")

    pdf.set_y(y_before_parties + 38)

    # Recitals
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(175.9, 4.5, "PREAMBLE & RECITALS", border=0, align="L")
    pdf.ln(4.5)
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(51, 65, 85)
    
    recital_text = (
        "This Mutual Confidentiality, Proprietary Rights, and Non-Circumvention Agreement (\"Agreement\") is entered into as of the Effective Date by and between WorldwideBro Holdings LLC (\"Company\" or \"Disclosing Party\") and the undersigned Prospective Investor (\"Recipient\" or \"Investor\").\n"
        "WHEREAS, Company has developed, owns, and operates a proprietary commercial real estate operating system and asset management platform, including the RE-001 Real Estate Deal Engine, Autonomous 11-Agent Fleet, Automated 10-Year Discounted Cash Flow (DCF) Underwriting Engine, Federal Reserve Macroeconomic Rate Stress-Testing Models, GIS Parcel Intelligence & Zoning Systems, and SEC Rule 506(c) Syndication Deal Room (collectively, the \"Platform\" and \"Demonstration\"); and\n"
        "WHEREAS, Recipient desires to review and inspect a confidential demonstration of the Platform, including proprietary code, operational runtimes, off-market deal pipeline, pro-forma financials, and syndication structures, solely to evaluate a potential capital allocation, syndication investment, debt financing facility, or strategic venture (\"Permitted Purpose\"); and\n"
        "WHEREAS, Company is willing to disclose such proprietary information and grant access to the Demonstration only upon the express condition that Recipient enters into binding non-disclosure, intellectual property protection, and non-circumvention covenants as set forth herein.\n"
        "NOW, THEREFORE, the parties agree as follows:"
    )
    pdf.multi_cell(175.9, 3.6, recital_text)
    pdf.ln(3)

    # Articles Helper Function
    def render_section(title, body):
        pdf.set_fill_color(241, 245, 249)
        pdf.set_draw_color(203, 213, 225)
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(175.9, 5, f"  {title}", border="L", fill=True, align="L")
        pdf.ln(5.5)
        pdf.set_font("Helvetica", "", 7.5)
        pdf.set_text_color(51, 65, 85)
        pdf.multi_cell(175.9, 3.6, body)
        pdf.ln(3)

    # Article 1
    art1_text = (
        "1.1. Scope of Confidential Information. \"Confidential Information\" means all non-public, proprietary, or confidential information disclosed by Company to Recipient, whether orally, visually, electronically, or in writing, or made accessible through the live Platform demonstration (re-001-worldwidebro-holdings.vercel.app), operator console (/console/*), investor deal room (/investor/deal-room), staging portals, data rooms, or repositories, including without limitation:\n"
        "  (a) Software & Technical Assets: Proprietary source code, architecture, UI/UX workflows, database schemas, prompt engineering sequences, autonomous agent execution runtimes, API designs, algorithms, trade secrets, and technical documentation.\n"
        "  (b) Real Estate Pipeline & Deal Flow: Off-market property listings, letters of intent (LOIs), purchase agreements, seller identities, motivated seller distress metrics, contract pricing, parcel GIS overlays, zoning analyses, and contractor rehab scopes.\n"
        "  (c) Financial Models & Underwriting: 10-year discounted cash flow (DCF) pro formas, debt service coverage ratio (DSCR) calculations, Federal Reserve FRED macroeconomic stress models, loan amortization schedules, equity waterfall structures, preferred return hurdle models, cap tables, distribution ledgers, and revenue fee schedules.\n"
        "  (d) Operational & Network Data: Prospective investor registers, accredited LP allocations, commercial lender facilities, property management ledgers, tenant payment histories, and contractor/vendor networks.\n"
        "1.2. Marking Not Required. All information disclosed during the Demonstration or contained within the Platform, Console, or Data Room shall be deemed Confidential Information regardless of whether it is explicitly marked with a \"CONFIDENTIAL\" or \"PROPRIETARY\" stamp."
    )
    render_section("ARTICLE 1: DEFINITION OF CONFIDENTIAL INFORMATION", art1_text)

    # Article 2
    art2_text = (
        "2.1. Standard of Care. Recipient agrees to hold all Confidential Information in strict trust and confidence, exercising at least a reasonable degree of care, and no less than the care used for its own confidential assets.\n"
        "2.2. Permitted Purpose Only. Recipient shall use Confidential Information solely and exclusively for the Permitted Purpose. Recipient shall not utilize Company's Confidential Information, algorithms, or deal pipeline to develop, build, license, commercialize, or assist any third party in developing any competing software, platform, underwriting service, or real estate fund.\n"
        "2.3. No Reverse Engineering or Replication. Recipient shall not reverse-engineer, decompile, disassemble, screen-record, scrape, copy, reproduce, mirror, or capture source code, API responses, or architectural workflows from the Platform or Demonstration.\n"
        "2.4. Authorized Disclosures. Recipient shall not disclose Confidential Information to any third party, except strictly to its bona fide officers, directors, investment committee members, legal counsel, and CPAs (\"Representatives\") who: (i) have a direct need-to-know for the Permitted Purpose, (ii) are informed of the confidential nature, and (iii) are bound in writing by confidentiality terms at least as restrictive as this Agreement. Recipient remains fully liable for any breach by its Representatives."
    )
    render_section("ARTICLE 2: NON-DISCLOSURE AND RESTRICTIONS ON USE", art2_text)

    pdf.add_page()

    # Article 3
    art3_text = (
        "3.1. Non-Circumvention Covenant. Recipient expressly recognizes that Company invests substantial time, proprietary capital, algorithmic modeling, and relationship capital to source, analyze, negotiate, and structure real estate acquisitions, syndications, and debt facilities. Accordingly, Recipient agrees that for a period of twenty-four (24) months following the Effective Date, Recipient and its affiliates shall NOT, directly or indirectly:\n"
        "  (a) Direct Deal Sourcing / Bypassing: Contact, solicit, negotiate with, or enter into any purchase agreement, option, lease, joint venture, or financing arrangement with any property owner, seller, broker, tenant, or lender whose property, identity, or opportunity was disclosed by Company during the Demonstration or within the Data Room, without Company's prior written consent.\n"
        "  (b) Commercial Circumvention: Interfere with, circumvent, avoid, or bypass Company's interest in any property, deal, syndication, assignment fee, or sponsor promote presented during the evaluation.\n"
        "  (c) Personnel Solicitation: Solicit, recruit, or hire any officer, employee, software engineer, or key contractor of Company who was introduced to Recipient during the evaluation.\n"
        "3.2. Liquidated / Remedial Measure. In the event Recipient breaches Section 3.1 and closes or finances a transaction involving any property or counterparty disclosed by Company without Company's participation, Recipient shall immediately pay to Company a transaction origination fee equal to the greater of: (i) 3.0% of the gross transaction purchase price, or (ii) $25,000.00, plus any profits realized, without prejudice to any other legal or equitable remedies available to Company."
    )
    render_section("ARTICLE 3: NON-CIRCUMVENTION (REAL ESTATE & DEAL PROTECTION)", art3_text)

    # Article 4
    art4_text = (
        "4.1. Safe Harbor Exclusions. The obligations of non-disclosure shall not apply to information that Recipient can demonstrate by written records: (a) is or becomes generally available to the public other than through a breach by Recipient; (b) was already lawfully in Recipient's possession prior to disclosure without duty of confidentiality; (c) is lawfully received from an independent third party without restriction; or (d) is independently developed without access to Company Confidential Information.\n"
        "4.2. Legally Compelled Disclosure. If Recipient is required by valid subpoena or court order to disclose Confidential Information, Recipient shall provide Company with prompt written notice to enable Company to seek a protective order."
    )
    render_section("ARTICLE 4: EXCLUSIONS FROM CONFIDENTIALITY", art4_text)

    # Article 5
    art5_text = (
        "5.1. Exclusive Ownership. All Confidential Information, source code, agent architectures, DCF models, trademarks, copyrights, trade secrets, and patentable inventions embodied within the Platform and Demonstration are and shall remain the sole and exclusive property of WorldwideBro Holdings LLC.\n"
        "5.2. No License or Transaction Obligation. Nothing in this Agreement grants Recipient any license, copyright, patent right, or ownership interest. Neither party is obligated to enter into any investment, underwriting agreement, term sheet, or transaction."
    )
    render_section("ARTICLE 5: OWNERSHIP OF INTELLECTUAL PROPERTY & NO LICENSE", art5_text)

    # Article 6
    art6_text = (
        "6.1. Term. This Agreement takes effect on the Effective Date and governs all disclosures made in connection with the Demonstration.\n"
        "6.2. Survival. (a) Confidentiality obligations survive for three (3) years from disclosure; provided, however, that all Trade Secrets, source code, algorithms, and prompt architecture shall remain confidential IN PERPETUITY until no longer qualifying as trade secrets under applicable law. (b) Non-circumvention covenants survive for twenty-four (24) months following the Effective Date."
    )
    render_section("ARTICLE 6: TERM AND SURVIVAL", art6_text)

    # Article 7
    art7_text = (
        "7.1. Injunctive Relief. Recipient acknowledges that any breach would cause immediate, severe, and irreparable harm for which money damages alone are inadequate. Company is entitled to seek immediate injunctive relief, specific performance, and temporary restraining orders in any court of competent jurisdiction without the necessity of posting bond.\n"
        "7.2. Attorneys' Fees. In any enforcement action, the prevailing party is entitled to recover reasonable attorneys' fees and court costs."
    )
    render_section("ARTICLE 7: EQUITABLE RELIEF AND REMEDIES", art7_text)

    # Article 8
    art8_text = (
        "8.1. Governing Law & Venue. Governed by the laws of the State of North Carolina. Exclusive personal jurisdiction and venue shall lie in the state and federal courts located in Mecklenburg County, North Carolina (Charlotte).\n"
        "8.2. Electronic Signatures. Enforceable under the U.S. Electronic Signatures in Global and National Commerce Act (E-SIGN Act, 15 U.S.C. Section 7001 et seq.) and Uniform Electronic Transactions Act (UETA). May be executed in counterparts."
    )
    render_section("ARTICLE 8: GOVERNING LAW & MISCELLANEOUS", art8_text)

    # Execution Block
    pdf.ln(2)
    pdf.set_fill_color(241, 245, 249)
    pdf.set_draw_color(203, 213, 225)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(175.9, 5, "ARTICLE 9: EXECUTION & SIGNATURE BLOCK", border="L", fill=True, align="L")
    pdf.ln(6)

    # Two Column Signature Table
    sig_w = 85.5
    sig_gap = 4.9
    y_sig = pdf.get_y()

    # Disclosing Party Box
    pdf.set_fill_color(255, 255, 255)
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(20, y_sig, sig_w, 48, style="FD")
    pdf.set_xy(22, y_sig + 2.5)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(sig_w - 4, 4, "DISCLOSING PARTY:", border=0)
    pdf.ln(4)
    pdf.set_x(22)
    pdf.set_font("Helvetica", "B", 7.5)
    pdf.cell(sig_w - 4, 4, "WORLDWIDEBRO HOLDINGS LLC", border=0)
    pdf.ln(8)
    pdf.set_x(22)
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(sig_w - 4, 4, "Signature: ______________________________________", border=0)
    pdf.ln(5)
    pdf.set_x(22)
    pdf.cell(sig_w - 4, 4, "Name: Ace Bless", border=0)
    pdf.ln(4)
    pdf.set_x(22)
    pdf.cell(sig_w - 4, 4, "Title: Managing Member / Chief Executive Officer", border=0)
    pdf.ln(4)
    pdf.set_x(22)
    pdf.cell(sig_w - 4, 4, "Date: ________________________, 202___", border=0)
    pdf.ln(4)
    pdf.set_x(22)
    pdf.set_font("Helvetica", "I", 6.5)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(sig_w - 4, 4, "Authorized Corporate Officer", border=0)

    # Receiving Party Box
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(20 + sig_w + sig_gap, y_sig, sig_w, 48, style="FD")
    pdf.set_xy(20 + sig_w + sig_gap + 2, y_sig + 2.5)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(sig_w - 4, 4, "RECEIVING PARTY / PROSPECTIVE INVESTOR:", border=0)
    pdf.ln(4)
    pdf.set_x(20 + sig_w + sig_gap + 2)
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(sig_w - 4, 4, "Entity: _________________________________________", border=0)
    pdf.ln(6)
    pdf.set_x(20 + sig_w + sig_gap + 2)
    pdf.cell(sig_w - 4, 4, "Signature: ______________________________________", border=0)
    pdf.ln(5)
    pdf.set_x(20 + sig_w + sig_gap + 2)
    pdf.cell(sig_w - 4, 4, "Print Name: ____________________________________", border=0)
    pdf.ln(4)
    pdf.set_x(20 + sig_w + sig_gap + 2)
    pdf.cell(sig_w - 4, 4, "Title: __________________________________________", border=0)
    pdf.ln(4)
    pdf.set_x(20 + sig_w + sig_gap + 2)
    pdf.cell(sig_w - 4, 4, "Date: ________________________, 202___", border=0)
    pdf.ln(4)
    pdf.set_x(20 + sig_w + sig_gap + 2)
    pdf.set_font("Helvetica", "I", 6.5)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(sig_w - 4, 4, "Compliant with 15 U.S.C. Section 7001 (E-SIGN Act)", border=0)

    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    pdf.output(output_path)
    print(f"Successfully generated NDA PDF: {output_path}")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "INVESTOR-DEMO-NDA.pdf"
    build_nda_pdf(out)
