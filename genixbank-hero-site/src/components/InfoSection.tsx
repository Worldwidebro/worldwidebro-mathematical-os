import { Link } from 'react-router-dom';
import { ArrowRight } from 'lucide-react';

function PillButton() {
  return (
    <Link
      to="/verticals/banking"
      className="inline-flex items-center gap-3 bg-black text-white text-base font-medium pl-8 pr-2 py-2 rounded-full hover:bg-gray-800 transition-colors duration-200"
    >
      Discover it
      <span className="bg-white rounded-full p-2">
        <ArrowRight className="w-5 h-5 text-black" />
      </span>
    </Link>
  );
}

export default function InfoSection() {
  return (
    <section className="bg-[#F5F5F5] px-6 py-24">
      <div className="max-w-[88rem] mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 mb-16 items-start">
          <div>
            <h2
              className="text-black text-4xl md:text-5xl font-medium leading-tight mb-8"
              style={{ letterSpacing: '-0.03em' }}
            >
              Meet GenixBank.
            </h2>
            <PillButton />
          </div>
          <p className="text-black/70 text-2xl md:text-3xl leading-relaxed">
            GenixBank is an AI-run business bank account that keeps your cash flow,
            expenses, and treasury working while you build.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div
            className="lg:col-span-2 rounded-2xl p-7 min-h-80 flex flex-col justify-between"
            style={{
              backgroundImage:
                "url('https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260423_164207_f243351d-ed59-48ec-83a0-a5e996bdbe3c.png&w=1280&q=85')",
              backgroundSize: 'cover',
              backgroundPosition: 'center',
            }}
          >
            <h3
              className="text-black text-2xl font-medium leading-snug"
              style={{ letterSpacing: '-0.02em' }}
            >
              Cash flow that compounds
            </h3>
            <p className="text-black/70 text-base max-w-xs">
              Idle balances are automatically swept into vetted, yield-bearing accounts —
              no spreadsheets, no manual transfers.
            </p>
          </div>

          <div className="rounded-2xl p-7 min-h-80 flex flex-col justify-between" style={{ backgroundColor: '#2B2644' }}>
            <h3 className="text-white text-2xl font-medium leading-snug">
              Always liquid,
              <br />
              always available
            </h3>
            <p className="text-white/60 text-base">
              Move funds instantly across every linked account — no lockups, no holds, no
              waiting on transfers.
            </p>
          </div>

          <div className="rounded-2xl p-7 min-h-80 flex flex-col justify-between" style={{ backgroundColor: '#2B2644' }}>
            <h3 className="text-white text-2xl font-medium leading-snug">
              Fully
              <br />
              automated
            </h3>
            <p className="text-white/60 text-base">
              Skip manually tagging transactions. GenixBank's AI treasurer reconciles and
              positions cash in the background, for you.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
