import type { SectorHeroConfig } from '../components/SectorHero';
import type { ArchiveHeroConfig } from '../components/ArchiveHero';

export type SectorEntry = {
  slug: string;
  /** must match the `sector` field values in portfolio.public.json */
  sectorLabel: string;
  opcoLabel: string;
  /** omit when the sector uses a bespoke hero component instead (see `customHero`) */
  hero?: SectorHeroConfig;
  /** slug of a bespoke hero component rendered by SectorPage instead of the generic SectorHero */
  customHero?: 'securify' | 'archive';
  /** required when customHero === 'archive' */
  archiveConfig?: ArchiveHeroConfig;
};

export const sectors: SectorEntry[] = [
  {
    slug: 'logistics-transport',
    sectorLabel: 'Logistics Transport',
    opcoLabel: 'OPCO-Transportation',
    hero: {
      logoText: 'Transportation',
      navLinks: [
        { label: 'Dispatch Core', href: '#capabilities' },
        { label: 'Ventures', href: '#ventures' },
        { label: 'OpCo', href: '#stats' },
        { label: 'Contact', href: '/contact' },
      ],
      ctaLabel: 'View Ventures',
      ctaHref: '#ventures',
      badgeText: '30 ventures building the logistics & transport OpCo',
      headingLines: ['Every Mile,', 'Under Control'],
      subtext:
        'From first mile to last, dispatch, freight, and fleet ventures built on one shared operating core — routing, tracking, and billing that scale with you.',
      emailPlaceholder: 'Your Best Email',
      emailButtonLabel: 'Get Early Access',
      videos: [
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260702_081127_0992a171-d3c6-4978-8213-0ec5df8b6d63.mp4',
          label: 'Golden Hour',
        },
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260702_092026_dd05b805-ea0f-40b2-8c52-332b88502592.mp4',
          label: 'Still Water',
        },
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260702_081042_df7202bf-bd80-4b2b-bbc6-1f09ba2870e9.mp4',
          label: 'Deep Woods',
        },
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260702_080959_4cac5234-3573-464e-a5b7-76b94b8a7d61.mp4',
          label: 'Quiet Dawn',
        },
      ],
      overlayPngUrl:
        'https://soft-zoom-63098134.figma.site/_assets/v11/0b4a435b2df2747593c43d7a1c9b4578f7d8d90c.png',
      darkVideoIndex: 2,
      darkColor: '#182C41',
      stats: [
        '30 Logistics Ventures',
        '12 Planned',
        '10 In Validation',
        '8 In MVP',
      ],
    },
  },
  {
    slug: 'education-training',
    sectorLabel: 'Education Training',
    opcoLabel: 'OPCO-Education',
    hero: {
      logoText: 'Education',
      navLinks: [
        { label: 'Ventures', href: '#ventures' },
        { label: 'OpCo', href: '#stats' },
        { label: 'Contact', href: '/contact' },
      ],
      ctaLabel: 'View Ventures',
      ctaHref: '#ventures',
      badgeText: '17 ventures building the education & training OpCo',
      headingLines: ['Know It', 'Then All.'],
      subtext:
        'Tutoring, certification, coaching, and content ventures built on one shared operating core — curriculum, learners, and outcomes that scale with you.',
      emailPlaceholder: 'Your Best Email',
      emailButtonLabel: 'Get Early Access',
      videos: [
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260405_074625_a81f018a-956b-43fb-9aee-4d1508e30e6a.mp4',
          label: 'Know It All',
        },
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260402_054547_9875cfc5-155a-4229-8ec8-b7ba7125cbf8.mp4',
          label: 'Our Approach',
        },
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260307_083826_e938b29f-a43a-41ec-a153-3d4730578ab8.mp4',
          label: 'Innovation x Vision',
        },
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260314_131748_f2ca2a28-fed7-44c8-b9a9-bd9acdd5ec31.mp4',
          label: 'Research & Insight',
        },
      ],
      darkVideoIndex: 2,
      darkColor: '#1A1420',
      stats: [
        '17 Education Ventures',
        '5 Planned',
        '5 In Validation',
        '7 In MVP',
      ],
    },
  },
  {
    slug: 'financial',
    sectorLabel: 'Financial',
    opcoLabel: 'OPCO-Financial',
    hero: {
      logoText: 'Financial',
      navLinks: [
        { label: 'Ventures', href: '#ventures' },
        { label: 'OpCo', href: '#stats' },
        { label: 'Contact', href: '/contact' },
      ],
      ctaLabel: 'View Ventures',
      ctaHref: '#ventures',
      badgeText: '41 ventures building the financial OpCo',
      headingLines: ['Capital That', 'Works Itself'],
      subtext:
        'Banking, treasury, credit repair, and tax ventures built on one shared operating core — reconciliation, compliance, and cash flow that scale with you.',
      emailPlaceholder: 'Your Best Email',
      emailButtonLabel: 'Get Early Access',
      videos: [
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260423_161253_c72b1869-400f-45ed-ac0c-52f68c2ed5bd.mp4',
          label: 'Treasury',
        },
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260423_183428_ab5e672a-f608-4dcb-b319-f3e040f02e2d.mp4',
          label: 'Use Cases',
        },
      ],
      darkColor: '#151A14',
      stats: [
        '41 Financial Ventures',
        '40 Planned',
        '1 In Growth',
      ],
    },
  },
  {
    slug: 'community',
    sectorLabel: 'Community',
    opcoLabel: 'OPCO-Operations',
    hero: {
      logoText: 'Community',
      navLinks: [
        { label: 'Ventures', href: '#ventures' },
        { label: 'OpCo', href: '#stats' },
        { label: 'Contact', href: '/contact' },
      ],
      ctaLabel: 'View Ventures',
      ctaHref: '#ventures',
      badgeText: '50 ventures building the community OpCo',
      headingLines: ['Growing The', 'Spirit Of Community'],
      subtext:
        'Senior care, food security, youth programs, and mentorship ventures built on one shared operating core — outreach, coordination, and outcomes that scale with you.',
      emailPlaceholder: 'Your Best Email',
      emailButtonLabel: 'Get Early Access',
      videos: [
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260315_073750_51473149-4350-4920-ae24-c8214286f323.mp4',
          label: 'Community',
        },
      ],
      darkColor: '#141A1F',
      stats: [
        '50 Community Ventures',
        '50 Planned',
        '48 Live Deployments',
      ],
    },
  },
  {
    slug: 'professional-services',
    sectorLabel: 'Professional Services',
    opcoLabel: 'OPCO-Staffing',
    hero: {
      logoText: 'Staffing',
      navLinks: [
        { label: 'Ventures', href: '#ventures' },
        { label: 'OpCo', href: '#stats' },
        { label: 'Contact', href: '/contact' },
      ],
      ctaLabel: 'View Ventures',
      ctaHref: '#ventures',
      badgeText: '25 ventures building the professional services OpCo',
      headingLines: ['Expertise,', 'On Demand'],
      subtext:
        'Consulting, legal, accounting, marketing, and staffing ventures built on one shared operating core — engagements, compliance, and delivery that scale with you.',
      emailPlaceholder: 'Your Best Email',
      emailButtonLabel: 'Get Early Access',
      videos: [],
      overlayPngUrl: '/sector-images/professional-services-staffing.png',
      darkColor: '#1F1826',
      stats: [
        '25 Professional Services Ventures',
        '1 Planned',
        '9 In Validation',
        '15 In MVP',
      ],
    },
  },
  {
    slug: 'technology',
    sectorLabel: 'Technology',
    opcoLabel: 'OPCO-Technology',
    customHero: 'securify',
  },
  {
    slug: 'e-commerce',
    sectorLabel: 'E Commerce',
    opcoLabel: 'OPCO-Marketplace',
    customHero: 'archive',
    archiveConfig: {
      wordmark: 'marketplace',
      caption:
        '110 e-commerce ventures — apparel, footwear, accessories, and dropship brands built on one shared operating core: catalog, checkout, and fulfillment that scale with you.',
      aboutLabel: 'About',
      cartLabel: 'CART',
      collectionLines: ['OPCO', 'MARKETPLACE'],
      price: '110',
      videos: {
        left: 'https://d8j0ntlcm91z4.cloudfront.net/user_39ca84eAE1ODL9hbR5VhoEj8tBf/hf_20260625_154433_532a85d3-dabf-4265-b8bd-19ac6af31842.mp4',
        right: 'https://d8j0ntlcm91z4.cloudfront.net/user_39ca84eAE1ODL9hbR5VhoEj8tBf/hf_20260625_154401_a664f076-b971-4557-8728-40ef9ea4c49b.mp4',
      },
      galleryImages: [
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_104530_521b2f85-c0f3-4d0e-9704-b578315b4cb9.png&w=1920&q=85',
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103711_76ccdb8b-5043-4f47-9c54-4379713393ea.png&w=1920&q=85',
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103728_394f6a1b-85e2-4386-a4f6-408472a0a5b7.png&w=1920&q=85',
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103739_86743e0e-16a7-4bee-bf38-dd67985344dc.png&w=1920&q=85',
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103748_b2215dc8-a3a7-470d-b19a-5b87fa7d0c37.png&w=1920&q=85',
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103758_e919ce72-5c9d-4b87-9be6-d7647b34825c.png&w=1920&q=85',
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103808_013583d0-3386-4547-9832-37c7d8edb3ac.png&w=1920&q=85',
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103937_a0c49d0a-33eb-4ead-aea6-c1baf241acbc.png&w=1920&q=85',
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103956_d18ed8fd-7b6f-4b86-91f9-20010fe38670.png&w=1920&q=85',
        'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_104034_ba5a9963-87ff-4008-a545-6bd686c088b5.png&w=1920&q=85',
      ],
      ctaWord: 'shop',
      footerBrand: 'WORLDWIDEBRO (R) 2026',
      footerRight: 'Privacy Policy',
      accentHex: '#ffffff',
    },
  },
  {
    slug: 'media-content',
    sectorLabel: 'Media Content',
    opcoLabel: 'OPCO-Media',
    hero: {
      logoText: 'Media',
      navLinks: [
        { label: 'Ventures', href: '#ventures' },
        { label: 'OpCo', href: '#stats' },
        { label: 'Contact', href: '/contact' },
      ],
      ctaLabel: 'View Ventures',
      ctaHref: '#ventures',
      badgeText: '21 ventures building the media & content OpCo',
      headingLines: ['Stories That', 'Move Culture'],
      subtext:
        'Video, podcast, streaming, gaming, and publishing ventures built on one shared operating core — production, distribution, and audience that scale with you.',
      emailPlaceholder: 'Your Best Email',
      emailButtonLabel: 'Get Early Access',
      videos: [
        {
          url: 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260622_204221_5339e40b-e73d-4ab0-9c65-79c18c66fd50.mp4',
          label: 'Visual Storytelling',
        },
      ],
      darkColor: '#1A1A1A',
      stats: [
        '21 Media Content Ventures',
        '5 Planned',
        '4 In Validation',
        '12 In MVP',
      ],
    },
  },
];

export function findSector(slug: string): SectorEntry | undefined {
  return sectors.find((s) => s.slug === slug);
}
