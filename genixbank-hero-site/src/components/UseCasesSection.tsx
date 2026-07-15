import { ArrowRight } from 'lucide-react';

const modes = [
  {
    venture: 'FIN-036',
    name: 'Arbitrage Nexus Platform',
    readiness: '51.5%',
    title: 'Trading',
    copy: 'Automated arbitrage execution across venues, settled straight into a GenixBank account — no manual transfers between trading and treasury.',
    bg: '#2B2644',
    text: 'white',
  },
  {
    venture: 'FIN-011',
    name: 'Automated Bookkeeping',
    readiness: '41.0%',
    title: 'Bookkeeping',
    copy: 'Transactions categorize and reconcile themselves against your GenixBank ledger in real time — books close without a bookkeeper.',
    bg: '#1F1F1F',
    text: 'white',
  },
  {
    venture: 'FIN-009',
    name: 'Crypto Tax Optimizer',
    readiness: '41.0%',
    title: 'Tax',
    copy: 'Cost-basis tracking and tax-lot optimization run against live GenixBank balances, so filing season starts pre-reconciled.',
    bg: '#F5F5F5',
    text: 'black',
    border: true,
  },
];

export default function UseCasesSection() {
  return (
    <section className="bg-[#F5F5F5] px-6 py-24">
      <div className="max-w-[88rem] mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-start mb-8">
          <div className="md:pr-12 md:pt-2">
            <p className="text-black/60 text-sm mb-2">GenixBank in Practice</p>
            <h2
              className="text-5xl md:text-6xl font-medium leading-none mb-6"
              style={{ letterSpacing: '-0.04em' }}
            >
              Use modes
            </h2>
            <p className="text-black/60 text-base leading-relaxed max-w-sm">
              Each mode below runs on a live venture in the Worldwidebro FIN portfolio —
              not a mockup. Readiness scores are pulled from the current venture scorecard.
            </p>
          </div>

          <div className="relative rounded-3xl overflow-hidden min-h-[480px] md:min-h-[560px]">
            <video
              autoPlay
              muted
              loop
              playsInline
              className="object-cover absolute inset-0 w-full h-full"
              src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260423_183428_ab5e672a-f608-4dcb-b319-f3e040f02e2d.mp4"
            />

            <div className="relative z-10 p-10 md:p-12">
              <p className="text-white/60 text-sm mb-2">FIN-001 · 41.0% ready</p>
              <h3
                className="text-4xl md:text-5xl font-medium leading-tight mb-5 text-white"
                style={{ letterSpacing: '-0.03em' }}
              >
                Commerce
              </h3>
              <p className="text-white/80 text-base max-w-md mb-8">
                Give customers real-time payment visibility and instant payouts through
                GenixBank's banking rails — no reconciliation lag, no manual invoicing.
              </p>

              <a href="/verticals/banking" className="group inline-flex items-center gap-3 text-white">
                <span className="w-9 h-9 rounded-full bg-white/80 backdrop-blur flex items-center justify-center group-hover:bg-white transition-colors">
                  <ArrowRight className="w-4 h-4 text-black" />
                </span>
                Know more
              </a>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {modes.map((mode) => (
            <div
              key={mode.venture}
              className={`rounded-2xl p-7 min-h-72 flex flex-col justify-between ${mode.border ? 'border border-black/10' : ''}`}
              style={{ backgroundColor: mode.bg }}
            >
              <div>
                <p className={`text-sm mb-2 ${mode.text === 'white' ? 'text-white/50' : 'text-black/50'}`}>
                  {mode.venture} · {mode.readiness} ready
                </p>
                <h3
                  className={`text-2xl font-medium leading-snug mb-3 ${mode.text === 'white' ? 'text-white' : 'text-black'}`}
                  style={{ letterSpacing: '-0.02em' }}
                >
                  {mode.title}
                </h3>
                <p className={`text-base ${mode.text === 'white' ? 'text-white/70' : 'text-black/70'}`}>
                  {mode.copy}
                </p>
              </div>
              <p className={`text-sm mt-6 ${mode.text === 'white' ? 'text-white/40' : 'text-black/40'}`}>
                {mode.name}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
