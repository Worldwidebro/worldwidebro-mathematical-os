import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import Nav from '../components/Nav';
import Footer from '../components/Footer';

const portfolio = portfolioData as PortfolioData;

function WhoIAm() {
  return (
    <main className="min-h-screen bg-black text-white">
      <Nav />

      <section className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-4xl">
          <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">Who I Am</p>
          <h1 className="mb-6 text-4xl font-normal leading-tight md:text-6xl">
            {portfolio.founder.name}
          </h1>
          <p className="mb-10 max-w-2xl text-lg leading-8 text-gray-300">
            {portfolio.founder.publicBio}
          </p>

          <div className="mb-10 grid gap-px overflow-hidden border border-white/10 bg-white/10 md:grid-cols-2">
            {portfolio.founder.proof.map((item) => (
              <div className="bg-black p-5" key={item}>
                <p className="text-sm leading-6 text-gray-300">{item}</p>
              </div>
            ))}
          </div>

          <div className="flex flex-wrap gap-4 text-sm text-gray-400">
            <a
              className="border border-white/10 px-4 py-2 hover:border-white/30"
              href={portfolio.founder.github}
              target="_blank"
              rel="noreferrer"
            >
              GitHub — @{portfolio.founder.handle}
            </a>
            <a
              className="border border-white/10 px-4 py-2 hover:border-white/30"
              href={`mailto:${portfolio.founder.email}`}
            >
              {portfolio.founder.email}
            </a>
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}

export default WhoIAm;
