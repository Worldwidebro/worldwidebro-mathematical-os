---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[ORB-MASTER-CONNECTOR-2026-06-11]]
---

# Education Landing Kit — Reusable Template

**What this is:** The reusable single-page marketing site scaffold for education-sector ventures — React + TypeScript + Vite + Tailwind CSS v4 + framer-motion + lucide-react, dark liquid-glass aesthetic, cloned and rebranded per venture. Companion to `[[SAAS-BACKEND-KIT-TEMPLATE]]` (that one is backend; this one is the front-of-house landing page).

**Proven instance:** `EDU-LANDING-KIT-TEMPLATE/` itself, built with placeholder brand "Asme" and placeholder hero/section videos — first real clone not yet assigned.

**Code location:** `WORLDWIDEBRO-OS/04-OPERATIONS/EDU-LANDING-KIT-TEMPLATE/`

> **To clone for a new venture, swap only the items in the table below.** Component structure, animation timings, and the `.liquid-glass` class carry over unchanged.

---

## THE SWAPS (per-venture)

| Swap | Where | Your new venture |
|------|-------|-------------------|
| **{{BRAND_NAME}}** | `src/components/Index.tsx` navbar (`Asme`) | 🟦 _________ |
| **{{TAGLINE}}** | `src/components/Index.tsx` hero `<h1>` ("Know it then all.") | 🟦 _________ |
| **{{HERO_VIDEO}}** | `Index.tsx` `HERO_VIDEO_URL` | 🟦 _________ |
| **{{FEATURED_VIDEO}}** | `FeaturedVideoSection.tsx` `FEATURED_VIDEO_URL` | 🟦 _________ |
| **{{PHILOSOPHY_VIDEO}}** | `PhilosophySection.tsx` `PHILOSOPHY_VIDEO_URL` | 🟦 _________ |
| **{{SERVICE_VIDEOS}}** ×2 | `ServicesSection.tsx` `CARDS[]` | 🟦 _________ |
| **{{COPY}}** — about/approach/philosophy/services text | all 5 section files | 🟦 _________ |
| **{{DEPLOY_URL}}** | Vercel/Netlify target once deployed | 🟦 _________ |

Everything else (layout, `.liquid-glass` component class, Instrument Serif import, framer-motion reveal patterns, video crossfade logic in the hero) is fixed — not venture-specific.

---

## FIXED STACK (same every venture)

| Concern | Choice |
|---|---|
| Build tool | Vite (react-ts template) |
| Styling | Tailwind CSS v4 (`@tailwindcss/postcss`, CSS-first — no `tailwind.config.js` needed) |
| Animation | framer-motion (`useInView` / `whileInView` reveals) |
| Icons | lucide-react — **note:** brand/logo icons (Instagram, Twitter/X, etc.) were removed upstream; use generic stand-ins (`AtSign`, `MessageCircle`, `Globe`) or swap in a dedicated brand-icon package if literal logos are required |
| Font | Google Fonts `Instrument Serif` (ital+regular), loaded via `@import` in `index.css` |
| Background | `bg-black` page-wide |

---

## FILE STRUCTURE (clone as-is)

```
EDU-LANDING-KIT-TEMPLATE/
├── src/
│   ├── components/
│   │   ├── Index.tsx                 # Hero: navbar + video crossfade + email capture + social row
│   │   ├── AboutSection.tsx          # useInView reveal, Instrument Serif italic accents
│   │   ├── FeaturedVideoSection.tsx  # full-bleed video + liquid-glass approach card
│   │   ├── PhilosophySection.tsx     # 2-col grid: video + two text blocks w/ hairline divider
│   │   └── ServicesSection.tsx       # 2-card grid, staggered reveal, hover video scale
│   ├── App.tsx                       # composes the 5 sections in order
│   ├── main.tsx
│   └── index.css                     # font import + tailwind import + .liquid-glass component class
├── postcss.config.js                 # @tailwindcss/postcss plugin (Tailwind v4)
└── package.json
```

**Design rules baked in:**
- Every glass surface uses the single `.liquid-glass` class (defined once in `index.css` `@layer components`) — never re-declare the backdrop-filter/gradient-border by hand.
- All video elements are `muted autoPlay playsInline preload="auto"`; only the hero video has the custom crossfade-loop JS (via refs, no CSS transitions) — section videos just `loop`.
- Reveal-on-scroll uses `framer-motion` `whileInView`/`useInView` with `once: true, margin: '-100px'` consistently — don't mix in a second animation library.

---

## UNIVERSAL FIRST MOVES (any education venture clone)

1. `cp -r EDU-LANDING-KIT-TEMPLATE <new-venture-folder>`, `rm -rf node_modules dist`, `npm install`
2. Do the 8 swaps in the table above (brand, tagline, 4 video URLs, copy, deploy target)
3. `npm run build` to confirm the swap didn't break types
4. Deploy (Vercel/Netlify) → record the URL in the venture's registry entry and this file's clone log
5. Add the venture to `vex-hero-site`'s venture list with its `liveUrl` so it's clickable from the public portfolio

---

## CLONE LOG

| Venture | Brand | Deploy URL | Status |
|---|---|---|---|
| (template) | Asme (placeholder) | not deployed | ⬜ Template only, no real clone yet |
