import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import Nav from '../components/Nav';
import Footer from '../components/Footer';

const portfolio = portfolioData as PortfolioData;

const packages = [
  {
    name: 'Advisory',
    scope: 'Operating-system design review, capital-layer sequencing, and venture prioritization.',
    cta: 'Start with a working session.',
  },
  {
    name: 'Build',
    scope: 'Hands-on venture buildout — from OpCo assignment through launch-ready execution.',
    cta: 'Bring a venture from idea to operating.',
  },
  {
    name: 'Systems',
    scope: 'Repository intelligence, knowledge-graph infrastructure, and multi-agent execution tooling.',
    cta: 'Wire the operating registry into your stack.',
  },
];

function Services() {
  return (
    <main className="min-h-screen bg-black text-white">
      <Nav />

      <section className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-5xl">
          <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">Services</p>
          <h1 className="mb-6 max-w-2xl text-4xl font-normal leading-tight md:text-6xl">
            Start with the operating map, not the pitch deck.
          </h1>
          <p className="mb-12 max-w-2xl text-base leading-7 text-gray-300">
            Built from the same {portfolio.holdings.brand} operating system that runs{' '}
            {portfolio.metrics.ventures} ventures across {portfolio.metrics.opcos} OpCos.
          </p>

          <div className="grid gap-px overflow-hidden border border-white/10 bg-white/10 md:grid-cols-3">
            {packages.map((pkg) => (
              <div className="flex flex-col justify-between bg-black p-6" key={pkg.name}>
                <div>
                  <h2 className="mb-4 text-2xl font-light">{pkg.name}</h2>
                  <p className="mb-8 text-sm leading-6 text-gray-300">{pkg.scope}</p>
                </div>
                <a
                  className="text-sm text-gray-300 underline underline-offset-4 hover:text-white"
                  href={`mailto:${portfolio.founder.email}?subject=${encodeURIComponent(`${pkg.name} inquiry`)}`}
                >
                  {pkg.cta}
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}

export default Services;
