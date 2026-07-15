import { useMemo, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import Nav from '../components/Nav';
import Footer from '../components/Footer';

const portfolio = portfolioData as PortfolioData;
const ALL = 'All';

type SortKey = 'name' | 'stage' | 'sector';

function Ventures() {
  const [searchParams] = useSearchParams();
  const [query, setQuery] = useState('');
  const [sector, setSector] = useState(searchParams.get('sector') || ALL);
  const [opco, setOpco] = useState(searchParams.get('opco') || ALL);
  const [stage, setStage] = useState(ALL);
  const [sortKey, setSortKey] = useState<SortKey>('name');

  const sectors = useMemo(
    () => [ALL, ...Array.from(new Set(portfolio.ventures.map((v) => v.sector))).sort()],
    [],
  );
  const opcos = useMemo(
    () => [ALL, ...Array.from(new Set(portfolio.ventures.map((v) => v.opco))).sort()],
    [],
  );
  const stages = useMemo(
    () => [ALL, ...Array.from(new Set(portfolio.ventures.map((v) => v.stage))).sort()],
    [],
  );

  const filtered = portfolio.ventures
    .filter(
      (v) =>
        (sector === ALL || v.sector === sector) &&
        (opco === ALL || v.opco === opco) &&
        (stage === ALL || v.stage === stage) &&
        (query.trim() === '' ||
          v.name.toLowerCase().includes(query.trim().toLowerCase()) ||
          v.id.toLowerCase().includes(query.trim().toLowerCase())),
    )
    .sort((a, b) => a[sortKey].localeCompare(b[sortKey]));

  return (
    <main className="min-h-screen bg-black text-white">
      <Nav />

      <section className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-7xl">
          <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">
            Venture Directory
          </p>
          <h1 className="mb-6 text-4xl font-normal leading-tight md:text-6xl">
            {portfolio.metrics.ventures} ventures, public-safe.
          </h1>
          <p className="mb-10 max-w-2xl text-base leading-7 text-gray-300">
            Search, filter, and sort. Only directory-level fields are shown — see the{' '}
            <Link className="underline underline-offset-4 hover:text-white" to="/privacy">
              data boundary
            </Link>{' '}
            for what's excluded.
          </p>

          <div className="mb-6">
            <input
              type="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search by name or venture ID…"
              className="w-full max-w-md border border-white/10 bg-black px-4 py-2 text-sm text-white placeholder:text-gray-600 focus:border-white/30 focus:outline-none"
            />
          </div>

          <div className="mb-10 flex flex-wrap items-center gap-4">
            <FilterSelect label="Sector" value={sector} options={sectors} onChange={setSector} />
            <FilterSelect label="OpCo" value={opco} options={opcos} onChange={setOpco} />
            <FilterSelect label="Stage" value={stage} options={stages} onChange={setStage} />
            <FilterSelect
              label="Sort by"
              value={sortKey}
              options={['name', 'stage', 'sector']}
              onChange={(v) => setSortKey(v as SortKey)}
            />
            <p className="text-sm text-gray-500">{filtered.length} matching</p>
          </div>

          <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
            {filtered.map((venture) => (
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
                  <span className="border border-white/10 px-3 py-1">{venture.sector}</span>
                  <span className="border border-white/10 px-3 py-1">{venture.opco}</span>
                  <span className="border border-white/10 px-3 py-1">{venture.stage}</span>
                </div>
              </Link>
            ))}
          </div>

          {filtered.length === 0 && (
            <p className="py-16 text-center text-sm text-gray-500">
              No ventures match this search/filter combination.
            </p>
          )}
        </div>
      </section>

      <Footer />
    </main>
  );
}

type FilterSelectProps = {
  label: string;
  value: string;
  options: string[];
  onChange: (value: string) => void;
};

function FilterSelect({ label, value, options, onChange }: FilterSelectProps) {
  return (
    <label className="flex items-center gap-2 text-sm text-gray-300">
      {label}
      <select
        className="border border-white/10 bg-black px-3 py-2 text-white"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      >
        {options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
    </label>
  );
}

export default Ventures;
