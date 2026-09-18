# VEX Dashboard — UI/UX Design System

**Version**: 1.0  
**Last Updated**: 2026-09-18  
**Owner**: Design System  
**Status**: APPROVED FOR BUILD

---

## DESIGN PHILOSOPHY: ANTIGRAVITY GLASSMORPHISM

**Principle**: UI that feels weightless, spatial, and premium—like floating glass panes with depth and translucency.

### Core Aesthetic
- **Glassmorphism**: Semi-transparent cards (opacity 80-90%), backdrop blur (12px)
- **Depth**: Layered shadows (sm through xl) creating Z-axis perception
- **Motion**: Smooth transitions (200-300ms), no instant state changes
- **Color**: Single accent (cyan #06b6d4), neutrals for contrast
- **Typography**: Geometric sans-serif (system fonts + Geist), bold hierarchy

---

## COLOR PALETTE

### Primary Colors
```css
--accent: #06b6d4;        /* Cyan — all interactive elements */
--accent-dark: #0891b2;   /* Darker cyan — hover/active states */
--bg-dark: #0f172a;       /* Slate-900 — background */
--bg-secondary: #1e293b;  /* Slate-800 — secondary surfaces */
--text-primary: #f1f5f9;  /* Slate-100 — body text */
--text-secondary: #94a3b8; /* Slate-400 — muted text */
```

### Status Colors
| Status | Color | Hex | Usage |
|--------|-------|-----|-------|
| Success | Green | #10b981 | Complete, active |
| Warning | Yellow | #fbbf24 | Caution, degraded |
| Error | Red | #ef4444 | Failed, blocked |
| Info | Blue | #3b82f6 | Alert, notice |
| Neutral | Gray | #64748b | Secondary, disabled |

### Glass Card Variants
```css
.glass-card {
  background: rgba(15, 23, 42, 0.8);      /* 80% opacity slate-900 */
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.glass-card:hover {
  background: rgba(15, 23, 42, 0.85);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease-out;
}
```

---

## TYPOGRAPHY

### Font Stack
```css
/* System fonts (fastest loading) */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
             'Helvetica Neue', Arial, sans-serif;
```

### Font Sizes (Modular Scale 1.25)
| Level | Size | Use Case |
|-------|------|----------|
| H1 | 48px / 3rem | Page title |
| H2 | 32px / 2rem | Section header |
| H3 | 24px / 1.5rem | Subsection |
| H4 | 20px / 1.25rem | Card title |
| Body | 16px / 1rem | Default text |
| Small | 14px / 0.875rem | Meta, secondary |
| Tiny | 12px / 0.75rem | Badges, labels |

### Font Weights
- **Bold (700)**: Headers, emphasis
- **Semibold (600)**: Card titles, strong text
- **Regular (400)**: Body, paragraphs
- **Light (300)**: Decorative, muted

### Line Height
```css
line-height: 1.5;  /* Body text (readable) */
line-height: 1.2;  /* Headers (compact) */
line-height: 1.8;  /* Long-form content */
```

---

## SPACING & RHYTHM

### Spacing Scale (Base: 4px)
```
xs:  4px   (button padding)
sm:  8px   (component gap)
md: 16px   (default padding)
lg: 24px   (section spacing)
xl: 32px   (major sections)
2xl: 48px  (page margins)
```

### Grid & Alignment
- **Sidebar**: 280px fixed
- **Content area**: Remaining width
- **Max content width**: 1400px
- **Gutter**: 24px (left/right)
- **Column gap**: 16px

### Component Spacing
```css
.glass-card {
  padding: 24px;           /* md + md */
}

.glass-panel {
  padding: 32px;           /* lg + lg */
  margin-bottom: 24px;     /* section spacing */
}

.badge {
  padding: 4px 12px;       /* xs/sm combo */
  margin-right: 8px;       /* sm spacing */
}
```

---

## COMPONENT LIBRARY

### Cards
```jsx
<div className="glass-card p-6 rounded-lg hover:shadow-lg transition">
  <h3 className="text-lg font-bold mb-2">Card Title</h3>
  <p className="text-sm text-gray-400">Card content</p>
</div>
```

**Variants**:
- Standard (default)
- Interactive (cursor pointer, hover scale)
- Alert (border + accent bg)
- Disabled (opacity 50%)

### Buttons
```jsx
<button className="px-4 py-2 bg-cyan-500 hover:bg-cyan-600 
                   rounded-lg transition font-semibold">
  Action
</button>
```

**Variants**:
- Primary (cyan bg)
- Secondary (transparent, border)
- Danger (red)
- Disabled (gray, no hover)

### Badges
```jsx
<span className="badge badge-success text-xs">Active</span>
<span className="badge badge-warning text-xs">Caution</span>
<span className="badge badge-error text-xs">Failed</span>
```

**Sizes**: xs, sm, md

### Tables
```jsx
<table className="w-full">
  <thead className="bg-white/5 border-b border-white/10">
    <tr>
      <th className="text-left px-4 py-2">Column</th>
    </tr>
  </thead>
  <tbody>
    <tr className="border-b border-white/10 hover:bg-white/5">
      <td className="px-4 py-3">Data</td>
    </tr>
  </tbody>
</table>
```

### Forms
```jsx
<input className="bg-white/10 border border-white/20 rounded-lg 
                   px-4 py-2 focus:outline-none focus:ring-2 
                   focus:ring-cyan-500" 
       placeholder="Type here..." />
```

### Progress Bars
```jsx
<div className="w-full bg-white/10 rounded-full h-2">
  <div className="bg-gradient-to-r from-cyan-500 to-blue-500 
                  h-full rounded-full" style={{width: '75%'}} />
</div>
```

---

## ANIMATIONS & TRANSITIONS

### Timing Functions
```css
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

### Duration Standards
| Duration | Use Case |
|----------|----------|
| 150ms | Micro-interactions (hover, focus) |
| 200ms | Button clicks, state changes |
| 300ms | Transitions, slide-in |
| 500ms | Modal enter/exit |
| 1000ms+ | Page load animations |

### Examples
```css
/* Smooth color transition */
.interactive {
  transition: all 0.2s ease-out;
}

/* Hover state */
.glass-card:hover {
  background: rgba(15, 23, 42, 0.85);
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.3);
}

/* Loading spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}

.spinner {
  animation: spin 1s linear infinite;
}
```

### Accessibility
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## RESPONSIVE DESIGN

### Breakpoints (Mobile-First)
```css
/* Base: 375px (mobile) */
@media (min-width: 640px) {  /* sm: Tablet */
  /* Tablet styles */
}

@media (min-width: 1024px) { /* lg: Desktop */
  /* Desktop styles */
}

@media (min-width: 1280px) { /* xl: Large desktop */
  /* Large desktop styles */
}
```

### Mobile Optimizations
- Font size: 16px minimum (no zoom)
- Touch target: 44x44px minimum
- Layout: Single column, full width
- Sidebar: Collapsible (hamburger menu)
- Cards: Stack vertically

### Tablet
- Sidebar: Always visible
- 2-column layouts
- Cards: 50% width

### Desktop
- Sidebar + content (standard)
- Multi-column grids
- Full interactivity

---

## DARK MODE (Default)

VEX is **dark-first**. Light mode is future-optional.

```css
:root {
  color-scheme: dark;
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --text-primary: #f1f5f9;
}

body {
  background: var(--bg-primary);
  color: var(--text-primary);
}
```

---

## ACCESSIBILITY (WCAG 2.1 AA)

### Color Contrast
- Minimum 4.5:1 for body text
- Minimum 3:1 for large text (18pt+)
- Avoid color-only indicators (use icons + text)

### Focus States
```css
button:focus-visible {
  outline: 2px solid #06b6d4;
  outline-offset: 2px;
}
```

### Semantic HTML
```jsx
<header>Navigation</header>
<main>Content</main>
<footer>Footer</footer>
<button aria-label="Close menu">✕</button>
```

### Keyboard Navigation
- Tab order follows visual order
- Escape closes modals
- Enter/Space activates buttons
- Arrow keys navigate menus

### Screen Reader
- All images have alt text
- Buttons have accessible labels
- Form inputs labeled with `<label>`
- ARIA roles where needed

---

## ICON SYSTEM

**Policy**: Use SVG icons only, no emoji as UI icons.

### Icon Sets (Recommended)
- **Heroicons**: Default system icons
- **Lucide**: Clean, modern icons
- **Feather**: Minimalist alternatives

### Icon Sizing
```
16px (xs): Inline, meta
20px (sm): Buttons, badges
24px (md): Card headers
32px (lg): Section icons
48px (xl): Hero images
```

### Usage
```jsx
import { CheckCircleIcon } from '@heroicons/react/24/solid';

<CheckCircleIcon className="w-6 h-6 text-green-400" />
```

---

## THEME TOKENS (CSS Variables)

```css
:root {
  /* Colors */
  --accent: #06b6d4;
  --success: #10b981;
  --warning: #fbbf24;
  --error: #ef4444;
  --info: #3b82f6;
  
  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  
  /* Typography */
  --font-body: system-ui, sans-serif;
  --text-xs: 12px;
  --text-sm: 14px;
  --text-base: 16px;
  --text-lg: 20px;
  --text-xl: 24px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1);
  
  /* Radii */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
  
  /* Transitions */
  --duration-fast: 150ms;
  --duration-base: 200ms;
  --duration-slow: 300ms;
}
```

---

## COMPONENT SPECIFICATIONS

### Header (Top Navigation)
- Height: 64px
- Content: Logo + search + user menu
- Background: Gradient (top-to-bottom)
- Sticky: Yes (scroll-aware)

### Sidebar
- Width: 280px (fixed) or 56px (collapsed)
- Background: Darker than main (opacity 95%)
- Sections: 5 collapsible groups
- Icons: 24px, left-aligned

### Main Content
- Max width: 1400px
- Gutter: 24px
- Scrollable: Yes (smooth)
- Min height: Full viewport

### Tab Panel
- Padding: 32px
- Background: Transparent (shows main bg)
- Cards: Nested glass-cards

### Modal/Dialog
- Overlay: Dark (opacity 60%)
- Width: 90% (mobile), 500px (desktop)
- Rounded: 12px
- Shadow: xl

---

## MEASUREMENT CHECKLIST

Before shipping a tab:
- [ ] All text readable (contrast ≥ 4.5:1)
- [ ] All interactive elements (44px+ touch target)
- [ ] No color-only indicators
- [ ] Keyboard navigation works
- [ ] Focus states visible
- [ ] Mobile responsive (375px+)
- [ ] Dark mode tested
- [ ] Motion respects `prefers-reduced-motion`
- [ ] All images have alt text
- [ ] Performance: page load < 2s

---

**Next**: App Flow Diagram (wireframes + user journeys)
