# Fashion Design OS — Shared Capability & Distribution Map

**Source of truth:** `angels-in-daylight/_shared-fashion-os/`
**Built while executing:** EC-001 Angels in Daylight (2026-06-22)

> Principle: build the capability **once**, distribute **pointers + notes** to the
> ventures that need it. Do NOT copy code into each repo — they drift. Each sibling
> venture inherits from this source and adds only its own venture-specific config.

---

## Assets in this toolkit
| File | What it is | Status |
|------|-----------|--------|
| `extract_products.py` | rembg + watershed garment isolation pipeline | working |
| `FASHION-VOCABULARY.md` | technical-designer vocabulary (extract/grade/spec/placement) | to add |
| `10-PHASE-PIPELINE.md` | collage -> extract -> catalog -> collection -> lookbook -> launch | to add |
| `../product-shots/GALLERY.html` | browsable pick-list generator | working |

---

## Distribution: which logic seeds which venture

| Venture repo (currently empty stub) | Inherits from this toolkit | Venture adds |
|---|---|---|
| **ec-030-ai-product-photographer** | `extract_products.py` + Phase 1/5/9 | clean-bg compositing, packshot presets |
| **ec-072-ai-product-cataloger** | `extract_products.py` + GALLERY + Phase 2 | SKU schema, Supabase `products` writer |
| **ec-053-ai-visual-merchandiser** | GALLERY.html generator | merchandising rules, collection layout |
| **ec-012-fashion-designer-ai** | `FASHION-VOCABULARY.md` + Phase 3/4/7 | design-system extraction prompts |
| **ec-009-sustainable-fashion-ai** | 10-phase pipeline + vocabulary | sustainability sourcing layer |
| **ec-050-ai-product-descriptions** | catalog output (Phase 2) -> description gen | copy templates, brand voice |
| **ec-003-shopify-autopilot** | catalog output -> storefront sync | Shopify/GoDaddy API automation |
| **ec-002-new-world-apparel** | full toolkit (it's an apparel brand like AID) | its own brand kit |
| **ec-013-merch-licensing** | graphics/logo extraction (Phase 3) | license terms, royalty logic |

---

## How a sibling venture "inherits" (the note dropped into each repo)
Each stub repo gets a `SHARED-CAPABILITIES.md` saying:

> This venture uses the Fashion Design OS shared toolkit at
> `angels-in-daylight/_shared-fashion-os/`. Do not rebuild extraction —
> import/run `extract_products.py`. Venture-specific code lives here; shared
> capability lives there.

When the OS consolidates, this toolkit graduates to a real shared package
(e.g. `06-TECHNOLOGY/shared/fashion-design-os/`) and the EC ventures depend on it.

---

## What is NOT distributed
- Raw AID product crops / brand kit -> stay private to EC-001.
- Higgsfield (paid) usage -> opt-in per venture, not a default dependency.
