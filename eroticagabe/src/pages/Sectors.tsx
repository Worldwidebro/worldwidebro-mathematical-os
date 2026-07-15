import { Link } from 'react-router-dom';
import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import { sectors } from '../data/sectors';
import Nav from '../components/Nav';
import Footer from '../components/Footer';

const portfolio = portfolioData as PortfolioData;

function Sectors() {
  const counts = new Map<string, number>();
  for (const v of portfolio.ventures) {
    counts.set(v.sector, (counts.get(v.sector) ?? 0) + 1);
  }
  const sectorLabels = Array.from(counts.keys()).sort();

  return (
    <main className="min-h-screen bg-black text-white">
      <Nav />

      <section className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-7xl">
          <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">Sectors</p>
          <h1 className="mb-6 text-4xl font-normal leading-tight md:text-6xl">
            {sectorLabels.length} sectors, one operating system.
          </h1>
          <p className="mb-10 max-w-2xl text-base leading-7 text-gray-300">
            Every sector eventually gets its own cinematic landing page with its ventures nested
            inside — Logistics Transport is built first. The rest fall back to a filtered venture
            list until their page ships.
          </p>

          <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
            {sectorLabels.map((label) => {
              const entry = sectors.find((s) => s.sectorLabel === label);
              const to = entry ? `/sectors/${entry.slug}` : `/ventures?sector=${encodeURIComponent(label)}`;
              return (
                <Link
                  to={to}
                  key={label}
                  className="border border-white/10 p-5 transition-colors duration-200 hover:border-white/30"
                >
                  <div className="mb-8 flex items-start justify-between gap-4">
                    <p className="text-xs uppercase tracking-[0.14em] text-gray-500">
                      {counts.get(label)} ventures
                    </p>
                    {entry ? (
                      <p className="whitespace-nowrap rounded-full border border-white/10 px-3 py-1 text-xs text-emerald-300">
                        Sector page live
                      </p>
                    ) : (
                      <p className="whitespace-nowrap rounded-full border border-white/10 px-3 py-1 text-xs text-gray-500">
                        Directory only
                      </p>
                    )}
                  </div>
                  <h3 className="text-xl font-light">{label}</h3>
                </Link>
              );
            })}
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}

export default Sectors;
