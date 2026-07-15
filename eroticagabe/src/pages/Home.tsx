import { useEffect, useState, type CSSProperties, type ReactNode } from 'react';
import { Link } from 'react-router-dom';
import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import Nav from '../components/Nav';
import Footer from '../components/Footer';

const portfolio = portfolioData as PortfolioData;

const videoUrl =
  'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260403_050628_c4e32401-fab4-4a27-b7a8-6e9291cd5959.mp4';

type FadeInProps = {
  children: ReactNode;
  delay?: number;
  duration?: number;
  className?: string;
};

function FadeIn({ children, delay = 0, duration = 1000, className = '' }: FadeInProps) {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const timer = window.setTimeout(() => setVisible(true), delay);
    return () => window.clearTimeout(timer);
  }, [delay]);

  return (
    <div
      className={`transition-opacity ${visible ? 'opacity-100' : 'opacity-0'} ${className}`}
      style={{ transitionDuration: `${duration}ms` }}
    >
      {children}
    </div>
  );
}

type AnimatedHeadingProps = {
  text: string;
  className?: string;
  delay?: number;
  charDelay?: number;
};

function AnimatedHeading({
  text,
  className = '',
  delay = 200,
  charDelay = 30,
}: AnimatedHeadingProps) {
  const [visible, setVisible] = useState(false);
  const lines = text.split('\n');

  useEffect(() => {
    const timer = window.setTimeout(() => setVisible(true), delay);
    return () => window.clearTimeout(timer);
  }, [delay]);

  return (
    <h1 className={className} style={{ letterSpacing: '-0.04em' }}>
      {lines.map((line, lineIndex) => (
        <span className="block" key={`${line}-${lineIndex}`}>
          {Array.from(line).map((char, charIndex) => {
            const transitionDelay =
              lineIndex * line.length * charDelay + charIndex * charDelay;
            const style: CSSProperties = {
              opacity: visible ? 1 : 0,
              transform: visible ? 'translateX(0)' : 'translateX(-18px)',
              transitionProperty: 'opacity, transform',
              transitionDuration: '500ms',
              transitionTimingFunction: 'ease',
              transitionDelay: `${transitionDelay}ms`,
            };

            return (
              <span className="inline-block" key={`${lineIndex}-${charIndex}`} style={style}>
                {char === ' ' ? ' ' : char}
              </span>
            );
          })}
        </span>
      ))}
    </h1>
  );
}

const operatingCards = [
  {
    label: 'Holdings',
    value: portfolio.holdings.brand,
    copy: 'Parent brand for operating entities, IP, accountability, and venture sequencing.',
  },
  {
    label: 'OpCo System',
    value: `${portfolio.metrics.opcos} OpCos`,
    copy: 'Operating companies organize ventures by sector, P&L, and execution responsibility.',
  },
  {
    label: 'Portfolio',
    value: `${portfolio.metrics.ventures} ventures`,
    copy: 'A venture map spanning service income, digital products, acquisitions, and capital.',
  },
];

const playbookRows = portfolio.holdings.capitalLayers;
const featuredOpcos = portfolio.opcos.slice(0, 8);
const featuredVentures = portfolio.ventures.slice(0, 12);

function HeroSection() {
  return (
    <section className="relative min-h-screen overflow-hidden bg-black text-white">
      <video
        className="absolute inset-0 h-full w-full object-cover"
        src={videoUrl}
        autoPlay
        loop
        muted
        playsInline
      />

      <div className="relative z-10 flex min-h-screen flex-col">
        <Nav />

        <div className="flex flex-1 flex-col justify-end px-6 pb-12 md:px-12 lg:px-16 lg:pb-16">
          <div className="gap-10 lg:grid lg:grid-cols-2 lg:items-end">
            <div>
              <AnimatedHeading
                text={'Shaping tomorrow\nwith vision and action.'}
                className="mb-4 text-4xl font-normal leading-[0.95] md:text-5xl lg:text-6xl xl:text-7xl"
              />

              <FadeIn delay={800} duration={1000}>
                <p className="mb-5 max-w-2xl text-base leading-7 text-gray-300 md:text-lg">
                  We back visionaries and craft ventures that define what comes next.
                </p>
              </FadeIn>

              <FadeIn delay={1200} duration={1000}>
                <div className="flex flex-wrap gap-4">
                  <Link
                    to="/contact"
                    className="rounded-lg bg-white px-8 py-3 font-medium text-black transition-colors duration-200 hover:bg-gray-100"
                  >
                    Start a Chat
                  </Link>
                  <Link
                    to="/who-i-am"
                    className="liquid-glass rounded-lg border border-white/20 px-8 py-3 font-medium text-white transition-colors duration-200 hover:bg-white hover:text-black"
                  >
                    Explore Now
                  </Link>
                </div>
              </FadeIn>
            </div>

            <FadeIn
              delay={1400}
              duration={1000}
              className="mt-8 flex items-end justify-start lg:mt-0 lg:justify-end"
            >
              <div className="liquid-glass rounded-xl border border-white/20 px-6 py-3">
                <p className="text-lg font-light md:text-xl lg:text-2xl">
                  Investing. Building. Advisory.
                </p>
              </div>
            </FadeIn>
          </div>
        </div>
      </div>
    </section>
  );
}

function Home() {
  return (
    <main className="bg-black text-white">
      <HeroSection />

      <section id="story" className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-start">
          <div>
            <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">
              {portfolio.founder.name}
            </p>
            <h2 className="max-w-xl text-3xl font-normal leading-tight md:text-5xl">
              A holding-company discipline for moving from income to ownership.
            </h2>
            <p className="mt-6 max-w-xl text-base leading-7 text-gray-300">
              {portfolio.founder.publicBio}
            </p>
            <Link
              to="/who-i-am"
              className="mt-6 inline-block text-sm text-gray-300 underline underline-offset-4 hover:text-white"
            >
              Read the full story →
            </Link>
          </div>
          <div className="grid gap-4 md:grid-cols-3">
            {operatingCards.map((card) => (
              <article className="border border-white/10 p-5" key={card.label}>
                <p className="mb-8 text-sm text-gray-400">{card.label}</p>
                <h3 className="mb-3 text-2xl font-light">{card.value}</h3>
                <p className="text-sm leading-6 text-gray-300">{card.copy}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section id="investing" className="border-y border-white/10 px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-7xl">
          <div className="mb-10 flex flex-col justify-between gap-4 md:flex-row md:items-end">
            <h2 className="text-3xl font-normal md:text-5xl">The capital playbook</h2>
            <p className="max-w-xl text-base leading-7 text-gray-300">
              Four compounding layers convert work, products, assets, and investment discipline into
              an operating portfolio.
            </p>
          </div>

          <div className="grid gap-px overflow-hidden border border-white/10 bg-white/10 md:grid-cols-4">
            {playbookRows.map((layer) => (
              <div className="bg-black p-5" key={layer.name}>
                <h3 className="mb-4 text-xl font-light">{layer.name}</h3>
                <p className="text-sm leading-6 text-gray-300">{layer.engine}</p>
                <p className="mt-6 text-xs uppercase tracking-[0.14em] text-gray-500">
                  {layer.targetMonthly} / {layer.margin}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="building" className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-7xl">
          <div className="mb-10 grid gap-10 lg:grid-cols-2 lg:items-end">
            <div>
              <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">Building</p>
              <h2 className="text-3xl font-normal leading-tight md:text-5xl">
                Build the ventures with enough operating context to survive execution.
              </h2>
            </div>
            <p className="text-base leading-7 text-gray-300">
              The public site now reads a safe export of the operating registry. Private fields stay
              out of the bundle; clients see the map, not the back office.
            </p>
          </div>

          <div className="grid gap-px overflow-hidden border border-white/10 bg-white/10 md:grid-cols-4">
            {featuredOpcos.map((opco) => (
              <div className="bg-black p-5" key={opco.id}>
                <p className="mb-8 text-xs uppercase tracking-[0.14em] text-gray-500">{opco.id}</p>
                <p className="text-xl font-light">{opco.label}</p>
                <p className="mt-3 text-sm text-gray-400">{opco.ventureCount} ventures</p>
              </div>
            ))}
          </div>

          <Link
            to="/ventures"
            className="mt-8 inline-block text-sm text-gray-300 underline underline-offset-4 hover:text-white"
          >
            View the full venture directory →
          </Link>
        </div>
      </section>

      <section className="border-y border-white/10 px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-7xl">
          <div className="mb-10 flex flex-col justify-between gap-4 md:flex-row md:items-end">
            <div>
              <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">
                Venture Directory
              </p>
              <h2 className="text-3xl font-normal md:text-5xl">Public-safe portfolio signal.</h2>
            </div>
            <p className="max-w-lg text-base leading-7 text-gray-300">
              Showing {featuredVentures.length} sample ventures from {portfolio.metrics.ventures}{' '}
              mapped records.
            </p>
          </div>

          <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
            {featuredVentures.map((venture) => (
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
        </div>
      </section>

      <section className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.85fr_1.15fr]">
          <div>
            <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">
              Data Boundary
            </p>
            <h2 className="text-3xl font-normal leading-tight md:text-5xl">
              Show momentum without leaking the machine.
            </h2>
          </div>
          <div className="grid gap-4 md:grid-cols-2">
            <div className="border border-white/10 p-5">
              <h3 className="mb-5 text-xl font-light">Public</h3>
              <ul className="space-y-3 text-sm leading-6 text-gray-300">
                {portfolio.privacy.publicFields.map((field) => (
                  <li key={field}>{field}</li>
                ))}
              </ul>
            </div>
            <div className="border border-white/10 p-5">
              <h3 className="mb-5 text-xl font-light">Private</h3>
              <ul className="space-y-3 text-sm leading-6 text-gray-300">
                {portfolio.privacy.excludedFields.map((field) => (
                  <li key={field}>{field}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>

      <section id="advisory" className="px-6 pb-20 md:px-12 lg:px-16">
        <div className="mx-auto flex max-w-7xl flex-col justify-between gap-8 border border-white/10 p-6 md:flex-row md:items-center md:p-8">
          <div>
            <p className="mb-3 text-sm uppercase tracking-[0.18em] text-gray-400">Advisory</p>
            <h2 className="text-3xl font-normal">Start with the operating map.</h2>
          </div>
          <Link
            className="w-fit rounded-lg bg-white px-8 py-3 font-medium text-black transition-colors duration-200 hover:bg-gray-100"
            to="/services"
          >
            See Services
          </Link>
        </div>
      </section>

      <Footer />
    </main>
  );
}

export default Home;
