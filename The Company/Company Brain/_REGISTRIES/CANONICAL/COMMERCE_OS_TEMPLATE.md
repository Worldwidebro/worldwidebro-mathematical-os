# Commerce OS Template Architecture

**Repository Path:** `repos/kosmickittyv2`
**Type:** Next.js + Supabase Commerce Framework
**Purpose:** Reusable, white-label e-commerce template and built-in Customer Revenue & Relationship CRM.

## Overview
The `kosmickittyv2` repository has been decoupled into an agnostic "Commerce OS". It is fully capable of being cloned and deployed for *any* physical, digital, or service-based e-commerce brand within the Company Brain portfolio.

## Cloning & Rebranding a New Venture
To spin up a new e-commerce venture using this framework:

1. **Clone the Directory:** Duplicate the `repos/kosmickittyv2` folder.
2. **Configure the Brand:** Open `src/lib/config/brand.ts` and update the `brandConfig` object (Name, tagline, contact info, social links, taxonomies).
3. **Change the Theme:** Modify `tailwind.config.ts` to swap the core `brand-dark`, `brand-light`, and `brand-accent` hex codes. 
4. **Link the Database:** Create a new Supabase project for the venture, run `supabase/schema_crm.sql`, and paste the new keys into `.env.local`.
5. **Populate the Catalog:** Replace `src/lib/data/mock-catalog.ts` with the new venture's products (or connect the catalog directly to Supabase).

## Built-In CRM Capabilities
The built-in CRM is universal and works out-of-the-box for any clone:
- Lead Pipeline (Kanban tracking)
- Customer 360 (VIP tracking, Subscriptions, Timeline)
- Revenue Intelligence (Cohorts, LTV, Blended CAC)
- Segments & Automations
