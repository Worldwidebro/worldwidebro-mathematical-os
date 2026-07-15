import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import Nav from '../components/Nav';
import Footer from '../components/Footer';

const portfolio = portfolioData as PortfolioData;

function Privacy() {
  return (
    <main className="min-h-screen bg-black text-white">
      <Nav />

      <section className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-3xl">
          <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">Privacy</p>
          <h1 className="mb-6 text-4xl font-normal leading-tight md:text-5xl">
            Public data boundary.
          </h1>
          <p className="mb-10 max-w-2xl text-base leading-7 text-gray-300">
            This site is allowed to publish only portfolio-level and venture-directory fields.
          </p>

          <div className="mb-10 grid gap-4 sm:grid-cols-2">
            <div className="border border-white/10 p-5">
              <h2 className="mb-5 text-xl font-light">Published</h2>
              <ul className="space-y-3 text-sm leading-6 text-gray-300">
                {portfolio.privacy.publicFields.map((field) => (
                  <li key={field}>{field}</li>
                ))}
              </ul>
            </div>
            <div className="border border-white/10 p-5">
              <h2 className="mb-5 text-xl font-light">Never published</h2>
              <ul className="space-y-3 text-sm leading-6 text-gray-300">
                {portfolio.privacy.excludedFields.map((field) => (
                  <li key={field}>{field}</li>
                ))}
              </ul>
            </div>
          </div>

          <p className="text-sm leading-6 text-gray-400">
            The data behind this site is generated from private operating files through a script
            that intentionally exports a restricted schema, so this site can show momentum without
            leaking operational data. Last generated:{' '}
            {new Date(portfolio.generatedAt).toLocaleDateString()}.
          </p>
        </div>
      </section>

      <Footer />
    </main>
  );
}

export default Privacy;
