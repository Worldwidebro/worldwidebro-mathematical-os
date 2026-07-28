#!/usr/bin/env python3
import os
import csv

CSV_PATH = "/Users/acebless/Documents/.claude/worktrees/agent-ac65ac3629807bab2/WORLDWIDEBRO-OS/03-PORTFOLIO/opcos/STAFFING/go-to-market/charlotte-employer-targets.csv"
OUTPUT_PATH = "/Users/acebless/.gemini/antigravity/brain/e667cdff-c87f-4195-a5cb-75bbb81728d4/charlotte_outbound_campaign.md"

def get_outreach_details(company, sector, notes):
    sec = sector.lower()
    
    # Customize templates based on sector
    if "electrical" in sec:
        role = "Journeyman/Master Electricians and Estimators"
        hook = "We specialize in sourcing field-ready commercial/industrial electricians with active NC licenses, saving your team from project delays."
        phone_pitch = "We place commercial and industrial electricians. We have a couple of certified guys in the Charlotte metro area looking for immediate placement."
        subject = f"Field-ready Electricians for {company} — No Risk / Pay-on-Hire"
    elif "hvac" in sec or "plumbing" in sec or "heating" in sec:
        role = "HVAC Install/Service Techs and Plumbers"
        hook = "We specialize in sourcing HVAC install technicians and commercial plumbers who can hit the ground running without onboarding lag."
        phone_pitch = "We place certified HVAC and plumbing technicians in Charlotte. We have two service techs ready for dispatch."
        subject = f"EPA-certified Techs for {company} — Pay-on-Hire Guarantee"
    elif "gc" in sec or "construction" in sec or "constructors" in sec:
        role = "Superintendents, PMs, and Estimators"
        hook = "We specialize in placing experienced commercial construction superintendents and project managers who know the Mecklenburg County/NC building codes."
        phone_pitch = "We recruit superintendents and estimators for commercial GCs. I saw your recent postings and wanted to see if we could send you 2 vetted profiles."
        subject = f"Commercial Superintendents & PMs for {company}"
    elif "logistics" in sec or "warehouse" in sec or "3pl" in sec:
        role = "Warehouse Supervisors and Dispatchers"
        hook = "We source qualified warehouse operations managers and logistics supervisors who can manage high-throughput operations in the Charlotte corridors."
        phone_pitch = "We place logistics and warehouse supervisors. I know operations in Harrisburg/Charlotte get congested and we have 1099/W2 supervisors ready."
        subject = f"Logistics/Warehouse Supervisors for {company}"
    else:
        role = "Skilled Trades and Project Staff"
        hook = "We specialize in sourcing skilled labor and project personnel tailored for your exact operations, with zero upfront retainer."
        phone_pitch = "We place skilled operations staff here in Charlotte. We operate on a contingency direct-hire model."
        subject = f"Qualified Candidates for {company}"

    return {
        "role": role,
        "hook": hook,
        "phone_pitch": phone_pitch,
        "subject": subject
    }

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Error: CSV not found at {CSV_PATH}")
        return

    high_leads = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("priority", "").strip().upper() == "HIGH":
                high_leads.append(row)

    print(f"Generating outreach campaign for {len(high_leads)} HIGH-priority leads...")

    # Start writing Markdown content
    md = []
    md.append("# Charlotte B2B Direct Income Outreach Campaign\n")
    md.append("This outbound campaign outlines personalized marketing templates, scripts, and phone numbers for your **top 15 HIGH-priority Charlotte employer prospects**. By executing these calls and sending these emails, you can immediately capture job orders. Filling just **one** $60,000 role at a 20% contingency fee results in a **$12,000 commission check**.")
    md.append("\n> [!IMPORTANT]\n> **Action Cadence:** Reach out to 5 targets per day. Use the phone script to establish contact first. If you hit voicemail, follow up immediately with the custom email below.\n")
    
    md.append("## Campaign Summary Table\n")
    md.append("| Company | Sector | Phone | Website | Target Roles |")
    md.append("| --- | --- | --- | --- | --- |")
    for row in high_leads:
        details = get_outreach_details(row['company'], row['sector'], row['notes'])
        website_link = f"[{row['website']}]({row['website']})" if row['website'] else "N/A"
        md.append(f"| **{row['company']}** | {row['sector']} | {row['phone'] or 'Needs Search'} | {website_link} | {details['role']} |")
    
    md.append("\n---\n")
    md.append("## Individual Lead Worksheets\n")

    for i, row in enumerate(high_leads, 1):
        company = row['company']
        sector = row['sector']
        phone = row['phone'] or "No phone in sheet - pull from Google maps"
        website = row['website'] or "N/A"
        notes = row['notes'] or "N/A"
        city_state = row['city_state']
        
        details = get_outreach_details(company, sector, notes)
        
        md.append(f"### {i}. {company}")
        md.append(f"- **Sector:** {sector}")
        md.append(f"- **Phone Number:** `{phone}`")
        md.append(f"- **Website:** {website}")
        md.append(f"- **Location/City:** {city_state}")
        md.append(f"- **Research Notes:** {notes}\n")
        
        md.append("#### 📞 Cold Call Phone Script")
        md.append(f'> *"Hi, is this the office manager or operations lead? My name is Ace with Worldwidebro Staffing here in Charlotte. I\'ll be quick—{details["phone_pitch"]} You only pay a fee if you choose to hire one. Are you guys short on staff right now, or expecting to need anyone on upcoming projects?"*\n')
        
        md.append("#### 📧 Custom Outbound Email")
        md.append(f"**Subject:** {details['subject']}")
        md.append(f"**To:** `hiring@{website.replace('www.', '') if website != 'N/A' else 'company.com'}`")
        md.append(f"**Body:**\n")
        md.append("```text")
        md.append(f"Hi Team,")
        md.append("")
        md.append(f"I run a local Charlotte recruiting desk focused on {sector.lower()} staffing.")
        md.append(f"{details['hook']}")
        md.append("")
        md.append(f"We operate on a pure contingency model: we find and pre-screen the candidates, you interview the ones you like, and you only pay a fee if you make a hire (backed by a 90-day replacement guarantee). No retainer, no risk.")
        md.append("")
        md.append(f"If you're currently looking for {details['role']}, reply with your requirements and I'll send over 2-3 vetted candidate profiles this week.")
        md.append("")
        md.append("Best regards,")
        md.append("Ace Bless")
        md.append("Managing Director, Worldwidebro Staffing")
        md.append("Charlotte, NC")
        md.append("Phone: (704) [Your Number]")
        md.append("```\n")
        md.append("#### 💬 LinkedIn Connection Note")
        md.append(f"```text")
        md.append(f"Hi [Name], saw that you lead operations at {company} in Charlotte. We help local shops source {details['role']} on a pure pay-on-hire basis. Would love to connect and keep in touch for when your queue gets backed up.")
        md.append(f"```\n")
        md.append("---\n")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
        
    print(f"Generated: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
