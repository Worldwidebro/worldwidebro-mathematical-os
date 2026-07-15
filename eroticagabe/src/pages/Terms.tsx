import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import Nav from '../components/Nav';
import Footer from '../components/Footer';

const portfolio = portfolioData as PortfolioData;

function Terms() {
  return (
    <main className="min-h-screen bg-black text-white">
      <Nav />

      <section className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-3xl">
          <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">Terms</p>
          <h1 className="mb-10 text-4xl font-normal leading-tight md:text-5xl">
            Site terms.
          </h1>

          <div className="space-y-8 text-sm leading-7 text-gray-300">
            <div>
              <h2 className="mb-2 text-lg font-light text-white">Informational use</h2>
              <p>
                This site presents a public-safe summary of {portfolio.holdings.brand}'s venture
                portfolio and operating structure. Venture stage, status, and metrics are directional
                signals, not financial disclosures, guarantees, or investment offers.
              </p>
            </div>
            <div>
              <h2 className="mb-2 text-lg font-light text-white">No solicitation</h2>
              <p>
                Nothing on this site constitutes an offer or solicitation to buy or sell any security
                or interest in any venture, OpCo, or the holding company.
              </p>
            </div>
            <div>
              <h2 className="mb-2 text-lg font-light text-white">Contact</h2>
              <p>
                Questions about these terms or the data shown here can be sent to{' '}
                <a
                  className="underline underline-offset-4 hover:text-white"
                  href={`mailto:${portfolio.founder.email}`}
                >
                  {portfolio.founder.email}
                </a>
                .
              </p>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}

export default Terms;
