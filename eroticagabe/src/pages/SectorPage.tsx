import { Link, useParams } from 'react-router-dom';
import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import { findSector } from '../data/sectors';
import SectorHero from '../components/SectorHero';
import SecurifyHero from '../components/SecurifyHero';
import ArchiveHero from '../components/ArchiveHero';
import Footer from '../components/Footer';

const portfolio = portfolioData as PortfolioData;

function SectorPage() {
  const { sectorId } = useParams<{ sectorId: string }>();
  const entry = sectorId ? findSector(sectorId) : undefined;

  if (!entry) {
    return (
      <main className="min-h-screen bg-black text-white">
        <section className="px-6 py-20 md:px-12 lg:px-16">
          <div className="mx-auto max-w-3xl">
            <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">Not Found</p>
            <h1 className="mb-6 text-3xl font-normal">
              No sector page exists yet for "{sectorId}".
            </h1>
            <Link
              to="/sectors"
              className="text-sm text-gray-300 underline underline-offset-4 hover:text-white"
            >
              ← Back to all sectors
            </Link>
          </div>
        </section>
        <Footer />
      </main>
    );
  }

  const ventures = portfolio.ventures.filter((v) => v.sector === entry.sectorLabel);

  return (
    <main className="min-h-screen bg-black text-white">
      {entry.customHero === 'securify' ? (
        <SecurifyHero />
      ) : entry.customHero === 'archive' && entry.archiveConfig ? (
        <ArchiveHero config={entry.archiveConfig} />
      ) : entry.hero ? (
        <SectorHero config={entry.hero} />
      ) : null}

      <section id="ventures" className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-7xl">
          <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">
            {entry.opcoLabel}
          </p>
          <h2 className="mb-10 text-3xl font-normal leading-tight md:text-5xl">
            {ventures.length} ventures in {entry.sectorLabel}
          </h2>

          <div id="capabilities" className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
            {ventures.map((venture) => (
              <Link
                to={`/ventures/${venture.id}`}
                className="border border-white/10 p-5 transition-colors duration-200 hover:border-white/30"
                key={venture.id}
              >
                <div className="mb-8 flex items-start justify-between gap-4">
                  <p className="text-xs uppercase tracking-[0.14em] text-gray-500">{venture.id}</p>
                  <p className="whitespace-nowrap rounded-full border border-white/10 px-3 py-1 text-xs text-gray-300">
                    {venture.status}
                  </p>
                </div>
                <h3 className="text-xl font-light">{venture.name}</h3>
                <div className="mt-5 flex flex-wrap gap-2 text-xs text-gray-300">
                  <span className="border border-white/10 px-3 py-1">{venture.opco}</span>
                  <span className="border border-white/10 px-3 py-1">{venture.stage}</span>
                </div>
              </Link>
            ))}
          </div>

          <p id="stats" className="mt-10 max-w-xl text-sm leading-6 text-gray-400">
            This is the public-safe view — see the{' '}
            <Link className="underline underline-offset-4 hover:text-white" to="/privacy">
              data boundary
            </Link>{' '}
            for what's excluded, or{' '}
            <Link className="underline underline-offset-4 hover:text-white" to="/sectors">
              browse other sectors
            </Link>
            .
          </p>
        </div>
      </section>

      <Footer />
    </main>
  );
}

export default SectorPage;
