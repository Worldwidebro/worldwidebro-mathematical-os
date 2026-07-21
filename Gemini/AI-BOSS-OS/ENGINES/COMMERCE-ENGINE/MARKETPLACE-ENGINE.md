# Marketplace Engine: Listing compliance & Asset Templates

This document outlines the rules for publishing products on marketplaces (TikTok Shop, Amazon FBA, Shopify) and details visual asset compliance.

---

## 1. Compliance Requirements Checklist

Before pushing a listing to any public marketplace, our `Store Agent` runs the following compliance checks:

1. **Title Length & Rules**: Under 80 characters. Avoid clickbait keywords like "Guaranteed" or "Best".
2. **Main Product Card Image**: 1:1 square ratio, white background, no text overlays, product must cover >80% of the frame.
3. **Product Detail Cards**: High-definition lifestyle shots, callout texts outlining specific dimensions/features, and 3D mockups.
4. **Keyword Density**: Ensure keywords are naturally integrated in product descriptions for search ranking optimization (SEO).
5. **Pricing Policy**: Check competitor databases to ensure retail price is within a 15% range of similar items, maintaining healthy margins.

---

## 2. Dynamic Asset Configurations

We coordinate image generation pipelines to match compliance:
- **Main Image**: Compiled with GPT Image 2 under the `product_shot` preset.
- **Secondary lifestyle images**: Enhancements with the `lifestyle_scene` preset showing the product in a sleek desk environment.
- **A+ Content Layout**: Grouped into three distinct cards: 1. Value Proposition, 2. Feature Details, 3. Setup Guide.
