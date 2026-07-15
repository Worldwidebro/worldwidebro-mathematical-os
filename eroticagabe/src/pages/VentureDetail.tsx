import { Link, useParams } from 'react-router-dom';
import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import Nav from '../components/Nav';
import Footer from '../components/Footer';
import ArchiveHero from '../components/ArchiveHero';
import type { ArchiveHeroConfig } from '../components/ArchiveHero';

const portfolio = portfolioData as PortfolioData;

// Same scroll-driven archive template as the E Commerce sector page
// (src/data/sectors.ts, slug 'e-commerce'), re-skinned for this one venture:
// brand wordmark, fashion-specific caption, price, and a warm accent color
// instead of the sector page's neutral white/marketplace framing.
const ventureArchiveConfigs: Record<string, ArchiveHeroConfig> = {
  'EC-001-Angels-in-Daylight': {
    wordmark: 'angels',
    caption:
      'Angels In Daylight — a capsule archive moving between shadow and light. Built on the same operating core as every OPCO-Marketplace venture: catalog, checkout, and fulfillment, wrapped in one running fashion drop.',
    aboutLabel: 'About',
    cartLabel: 'CART',
    collectionLines: ['ARCHIVE COLLECTION', '"ANGELS"'],
    price: '$188',
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
    ctaWord: 'view',
    footerBrand: 'ANGELS IN DAYLIGHT (R) 2026',
    footerRight: 'EC-001 / OPCO-MARKETPLACE',
    accentHex: '#F598F2',
  },
};

function VentureDetail() {
  const { id } = useParams<{ id: string }>();
  const venture = portfolio.ventures.find((v) => v.id === id);

  if (!venture) {
    return (
      <main className="min-h-screen bg-black text-white">
        <Nav />
        <section className="px-6 py-20 md:px-12 lg:px-16">
          <div className="mx-auto max-w-3xl">
            <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">Not Found</p>
            <h1 className="mb-6 text-3xl font-normal">
              No venture matches "{id}" in the public directory.
            </h1>
            <Link
              to="/ventures"
              className="text-sm text-gray-300 underline underline-offset-4 hover:text-white"
            >
              ← Back to the directory
            </Link>
          </div>
        </section>
        <Footer />
      </main>
    );
  }

  const fields = [
    { label: 'Venture ID', value: venture.id },
    { label: 'Sector', value: venture.sector },
    { label: 'OpCo', value: venture.opco },
    { label: 'Stage', value: venture.stage },
    { label: 'Status', value: venture.status },
  ];

  const archiveConfig = venture.id ? ventureArchiveConfigs[venture.id] : undefined;

  return (
    <main className="min-h-screen bg-black text-white">
      {archiveConfig ? <ArchiveHero config={archiveConfig} /> : <Nav />}

      <section className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-3xl">
          <Link
            to="/ventures"
            className="mb-6 inline-block text-sm text-gray-400 hover:text-white"
          >
            ← All ventures
          </Link>
          <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">{venture.id}</p>
          <h1 className="mb-6 text-4xl font-normal leading-tight md:text-6xl">{venture.name}</h1>

          {venture.liveUrl && (
            <a
              href={venture.liveUrl}
              target="_blank"
              rel="noreferrer"
              className="mb-10 inline-block border border-white/20 px-4 py-2 text-sm hover:border-white/50 hover:text-white"
            >
              Visit live site ↗
            </a>
          )}

          <div className="grid gap-px overflow-hidden border border-white/10 bg-white/10 sm:grid-cols-2">
            {fields.map((field) => (
              <div className="bg-black p-5" key={field.label}>
                <p className="mb-2 text-xs uppercase tracking-[0.14em] text-gray-500">
                  {field.label}
                </p>
                <p className="text-lg font-light">{field.value}</p>
              </div>
            ))}
          </div>

          {venture.capabilities.length > 0 && (
            <div className="mt-10">
              <p className="mb-4 text-xs uppercase tracking-[0.14em] text-gray-500">
                Capabilities required ({venture.capabilities.length})
              </p>
              <div className="flex flex-wrap gap-2">
                {venture.capabilities.map((cap) => (
                  <span
                    className="border border-white/10 px-3 py-1 text-xs text-gray-300"
                    key={cap}
                  >
                    {cap}
                  </span>
                ))}
              </div>
            </div>
          )}

          {(() => {
            const related = portfolio.ventures.filter(
              (v) => v.opco === venture.opco && v.id !== venture.id,
            );
            if (related.length === 0) return null;
            return (
              <div className="mt-10">
                <p className="mb-4 text-xs uppercase tracking-[0.14em] text-gray-500">
                  Also in {venture.opco} ({related.length})
                </p>
                <div className="flex flex-wrap gap-2">
                  {related.slice(0, 8).map((v) => (
                    <Link
                      key={v.id}
                      to={`/ventures/${v.id}`}
                      className="border border-white/10 px-3 py-1 text-xs text-gray-300 hover:border-white/30 hover:text-white"
                    >
                      {v.name}
                    </Link>
                  ))}
                  {related.length > 8 && (
                    <Link
                      to={`/ventures?opco=${encodeURIComponent(venture.opco)}`}
                      className="px-3 py-1 text-xs text-gray-500 underline underline-offset-4 hover:text-white"
                    >
                      +{related.length - 8} more
                    </Link>
                  )}
                </div>
              </div>
            );
          })()}

          <p className="mt-10 max-w-xl text-sm leading-6 text-gray-400">
            This is the public-safe view — revenue, cash, contacts, and internal notes stay out of
            this bundle per the{' '}
            <Link className="underline underline-offset-4 hover:text-white" to="/privacy">
              data boundary
            </Link>
            . For a fuller briefing on this venture,{' '}
            <Link className="underline underline-offset-4 hover:text-white" to="/contact">
              get in touch
            </Link>
            .
          </p>
        </div>
      </section>

      <Footer />
    </main>
  );
}

export default VentureDetail;
