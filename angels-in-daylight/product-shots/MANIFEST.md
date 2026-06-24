# Angels in Daylight — Product Shot Extraction

**Source:** 14 ChatGPT-generated collage/reference images (`_intake/`)
**Method:** rembg (isnet-general-use) background removal → skimage distance-transform watershed → bounding-box crop
**Generated:** 2026-06-22

## Output: 198 clean crops in `separated/imgN/`

| Board | What it is | Crops | Quality |
|-------|-----------|-------|---------|
| img1/2/3 | Leather shorts singles (blue/blue/pink) | 1+1+1 | full-res, store-ready |
| img6 | "Worldwide" universe board (tan bg) | 49 | good |
| img7 | Track pants + beanies + tees | 20 | good (some details) |
| img8 | "18 Design Systems" board | 3 | mostly typography, not products |
| img11 | Logo lockup sheet | 38 | logos (not garments) |
| img12 | Hero hoodie sets / tee / tank | 10 | good (some oversplit) |
| img13 | Denim jackets + bikinis + sets | 36 | good (front/back views separate) |
| img14 | Big product grid | 39 | good |

## Moved aside: `separated/_low-quality/` (img4, 5, 9, 10)
Dark-background boards. rembg could not separate dark garments from near-black
backgrounds (alpha coverage 1-11%). These are largely **duplicate SKUs** of the
boards above (img4 = same catalog as img6; img9 = women's line). To extract these:
regenerate as clean white-bg packshots, or manual-slice.

## Review
Contact sheets per board: `_contactsheets/imgN.png`

## Known issues / next pass
- A few crops merge 2 adjacent items or split one garment — manual touch-up.
- Logos (img11) and design systems (img8) are not garments — file separately.
- Crops are at source resolution (collage tiles ~200-400px) — fine for reference,
  NOT high enough for store hero images. For storefront, regenerate true packshots.
