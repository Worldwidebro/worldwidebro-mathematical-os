# Landing Page Spec — {{brand}}

Map BOF content to page sections. Implement in your stack (Next.js, Webflow, etc.).

## Hero (BOF)
- **Headline:** {{outcome}} — without spreadsheet chaos
- **Subhead:** {{brand}} for {{icp}}
- **Primary CTA:** {{cta}}
- **Proof line:** [Metric or testimonial — verify]

## Section 2 — Problem (TOF → MOF bridge)
- 3 bullets matching `audience.md` pain points

## Section 3 — How it works (MOF)
- 3 steps from `02_MOF/demos.md`
- Optional: embedded 45s demo video (`metadata_mof.json` → `output.mp4`)

## Section 4 — Proof stack (BOF)
- Testimonials from `03_BOF/testimonials.md`
- Logos when available

## Section 5 — Offer + guarantee (BOF)
- Copy from `03_BOF/offers.md`
- Single primary button

## Footer
- Privacy, contact, social links

## Funnel mapping
| Page section | Funnel stage | Source file |
|--------------|--------------|-------------|
| Hero CTA | BOF | offers.md |
| Problem | TOF/MOF | audience.md |
| How it works | MOF | demos.md |
| Testimonials | BOF | testimonials.md |

## SEO
- Title: {{brand}} | {{outcome}}
- Meta: One sentence from positioning statement
