import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import Nav from '../components/Nav';
import Footer from '../components/Footer';
import { Section, Eyebrow, PageHeading, Card, TextLink } from '../components/ui';

const portfolio = portfolioData as PortfolioData;

function Proof() {
  return (
    <main className="min-h-screen bg-black text-white">
      <Nav />

      <Section>
        <Eyebrow>Proof</Eyebrow>
        <PageHeading className="max-w-3xl">
          Not case studies — the operating system itself.
        </PageHeading>
        <p className="mb-12 max-w-2xl text-base leading-7 text-gray-300">
          There isn't a client roster to show yet — the venture layer is still mostly pre-build. What's
          real and verifiable today is the infrastructure underneath it, so that's what's shown here
          instead of invented testimonials. Venture stage below is audited against real repo code
          (not self-reported paperwork) — {portfolio.readinessSummary.ventureCountVerified} of{' '}
          {portfolio.metrics.ventures} ventures have been independently checked so far, at a{' '}
          {portfolio.readinessSummary.portfolioAverageReadiness}% average readiness.
        </p>

        <div className="grid gap-px overflow-hidden border border-white/10 bg-white/10 sm:grid-cols-2">
          {portfolio.proof.map((item) => (
            <div className="bg-black p-6" key={item.label}>
              <p className="mb-2 text-xs uppercase tracking-[0.14em] text-gray-500">{item.label}</p>
              <p className="mb-3 text-2xl font-light">{item.stat}</p>
              <p className="text-sm leading-6 text-gray-300">{item.detail}</p>
            </div>
          ))}
        </div>
      </Section>

      <Section border="y">
        <Eyebrow>Real design, not mockups</Eyebrow>
        <p className="mb-8 max-w-2xl text-base leading-7 text-gray-300">
          Checked all 96 repos with real site code for actual production animation (not just a
          template). One venture qualifies today — the rest either have no frontend yet or are
          static. This is the flagship, not a curated top-N.
        </p>
        <a
          href="https://con-001-ace-construction.vercel.app"
          target="_blank"
          rel="noreferrer"
          className="block max-w-sm border border-white/10 bg-white/[0.03] p-6 transition-colors hover:border-white/30"
        >
          <p className="mb-2 text-xs uppercase tracking-[0.14em] text-gray-500">
            CON-001-Ace-Construction
          </p>
          <p className="mb-3 text-lg font-light">Ace Construction</p>
          <p className="mb-2 text-xs text-gray-400">Construction · Next.js + Framer Motion + Supabase + Stripe</p>
          <p className="text-xs text-gray-500">con-001-ace-construction.vercel.app →</p>
        </a>
      </Section>

      <Section border="y">
        <Eyebrow>Where the most-ready ventures actually stand</Eyebrow>
        <p className="mb-8 max-w-2xl text-base leading-7 text-gray-300">
          Self-reported paperwork previously claimed 5 ventures were at active/growth stage. Audited
          against real repo code, 4 of those 5 don't hold up — they check out closer to planning
          stage. Zero ventures are currently verified past validation stage. Below are the highest
          audited-readiness ventures in the portfolio today — this is the honest state, not a
          projection.
        </p>
        <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
          {portfolio.ventures
            .filter((v) => v.stageVerified)
            .sort((a, b) => (b.readinessPct ?? 0) - (a.readinessPct ?? 0))
            .slice(0, 6)
            .map((v) => (
              <Card key={v.id}>
                <p className="mb-2 text-xs uppercase tracking-[0.14em] text-gray-500">{v.id}</p>
                <p className="mb-3 text-lg font-light">{v.name}</p>
                <p className="mb-2 text-xs text-gray-400">
                  {v.sector} · {v.opco}
                </p>
                <p className="text-xs text-gray-500">
                  {v.auditedStage} · {v.readinessPct}% readiness
                </p>
              </Card>
            ))}
        </div>
      </Section>

      <Section>
        <Eyebrow>What this means for you</Eyebrow>
        <p className="max-w-2xl text-base leading-7 text-gray-300">
          If you're evaluating whether to work together: what you'd be buying is the system above —
          repository intelligence, a live capability graph, and a reporting pipeline that already
          runs — applied to your venture, not a portfolio of finished client work that doesn't exist
          yet.{' '}
          <TextLink to="/contact">Talk about what that looks like for your venture →</TextLink>
        </p>
      </Section>

      <Footer />
    </main>
  );
}

export default Proof;
