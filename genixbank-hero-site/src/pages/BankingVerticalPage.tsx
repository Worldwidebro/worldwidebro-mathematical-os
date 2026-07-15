import { Link } from 'react-router-dom';
import { ArrowRight, ArrowLeft } from 'lucide-react';
import LogoIcon from '../components/LogoIcon';

function Section({
  id,
  title,
  children,
}: {
  id: string;
  title: string;
  children: React.ReactNode;
}) {
  return (
    <section id={id} className="border-t border-black/10 py-14">
      <div className="max-w-[88rem] mx-auto px-6">
        <h2 className="text-3xl md:text-4xl font-medium mb-8" style={{ letterSpacing: '-0.02em' }}>
          {title}
        </h2>
        {children}
      </div>
    </section>
  );
}

function StatCard({ label, value, detail }: { label: string; value: string; detail: string }) {
  return (
    <div className="bg-white rounded-2xl p-6 border border-black/10">
      <div className="text-black/50 text-sm mb-2">{label}</div>
      <div className="text-2xl font-medium mb-2" style={{ letterSpacing: '-0.02em' }}>
        {value}
      </div>
      <div className="text-black/60 text-sm leading-relaxed">{detail}</div>
    </div>
  );
}

function List({ items }: { items: string[] }) {
  return (
    <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-3">
      {items.map((item) => (
        <li key={item} className="text-black/70 text-base flex items-start gap-2">
          <span className="text-black/30 mt-1">—</span>
          {item}
        </li>
      ))}
    </ul>
  );
}

export default function BankingVerticalPage() {
  return (
    <div className="bg-[#F5F5F5] min-h-screen">
      {/* Top bar */}
      <div className="px-6 py-5 border-b border-black/10">
        <div className="max-w-[88rem] mx-auto flex items-center justify-between">
          <Link to="/" className="flex items-center gap-2">
            <LogoIcon className="w-6 h-6 text-black" />
            <span className="text-xl font-medium tracking-tight">GenixBank</span>
          </Link>
          <Link to="/" className="inline-flex items-center gap-2 text-sm text-black/60 hover:text-black transition-colors">
            <ArrowLeft className="w-4 h-4" />
            Back home
          </Link>
        </div>
      </div>

      {/* Hero */}
      <div className="max-w-[88rem] mx-auto px-6 pt-16 pb-12">
        <p className="text-black/50 text-sm mb-3">Verticals / Banking</p>
        <h1 className="text-5xl md:text-6xl font-medium mb-6" style={{ letterSpacing: '-0.03em' }}>
          Banking
        </h1>
        <p className="text-black/70 text-2xl md:text-3xl leading-relaxed max-w-3xl mb-2">
          What is Banking?
        </p>
        <p className="text-black/60 text-base md:text-lg leading-relaxed max-w-2xl mb-8">
          Banking is the deposit-taking, lending, and payments-infrastructure vertical of
          financial services — spanning FDIC-insured commercial banks and the API-first
          neobanks that now serve most early-stage companies, including GenixBank.
        </p>
        <div className="flex flex-wrap gap-3">
          <a href="#overview" className="inline-flex items-center gap-3 bg-black text-white text-base font-medium pl-6 pr-2 py-2 rounded-full hover:bg-gray-800 transition-colors">
            Start Here
            <span className="bg-white rounded-full p-1.5">
              <ArrowRight className="w-4 h-4 text-black" />
            </span>
          </a>
          <a href="#learning" className="inline-flex items-center bg-white text-black text-base font-medium px-6 py-2 rounded-full border border-black/10 hover:bg-black/5 transition-colors">
            Download Guide
          </a>
          <a href="#companies" className="inline-flex items-center bg-white text-black text-base font-medium px-6 py-2 rounded-full border border-black/10 hover:bg-black/5 transition-colors">
            Related Businesses
          </a>
        </div>
      </div>

      {/* Statistics */}
      <Section id="statistics" title="Statistics">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <StatCard
            label="Market Size"
            value="$1.5–1.6T"
            detail="US commercial banking industry revenue, 2026 (IBISWorld). Global neobanking market: $310–410B (2026, varies by source)."
          />
          <StatCard
            label="Institutions"
            value="~3,745"
            detail="US commercial banking businesses (IBISWorld, 2026). 4,135 FDIC-insured commercial banks as of last published FDIC count (2022)."
          />
          <StatCard
            label="Growth Rate"
            value="−2.4% / +36–62%"
            detail="Traditional bank count CAGR 2021–2026 (declining, consolidation) vs. neobanking segment CAGR (rapid growth, wide range across forecasters)."
          />
          <StatCard
            label="Countries"
            value="US-centered"
            detail="Vertical is US-focused for GenixBank's initial market; neobanking is expanding globally in parallel."
          />
          <StatCard
            label="Major Players (Traditional)"
            value="4 dominant"
            detail="JPMorgan Chase, Bank of America, Wells Fargo, Citigroup."
          />
          <StatCard
            label="Major Players (SMB Neobank)"
            value="6 tracked"
            detail="Mercury (#1, 200K+ customers, $20B deposits, ~$4B/mo payments), Brex, Ramp, Relay, Novo, Rho."
          />
        </div>
        <p className="text-black/40 text-xs mt-6">
          Sources: IBISWorld "Commercial Banking in the US" (2026), Mordor Intelligence, FDIC,
          Grand View Research / Business Research Insights neobanking reports (2026), Fintech
          Labs SMB neobank rankings (Jul 2026). Estimates vary widely by methodology — ranges
          shown rather than a single false-precision number.
        </p>
      </Section>

      {/* Industry Overview */}
      <Section id="overview" title="Industry Overview">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8">
          <div>
            <h3 className="text-lg font-medium mb-2">Description</h3>
            <p className="text-black/70 text-base leading-relaxed">
              Banking converts idle capital into productive capital: it takes deposits,
              extends credit, and clears payments, earning a spread and fees along the way.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">Purpose</h3>
            <p className="text-black/70 text-base leading-relaxed">
              Give individuals and businesses a safe place to hold money, a way to move it,
              and access to credit against future income.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">History</h3>
            <p className="text-black/70 text-base leading-relaxed">
              From Glass-Steagall-era deposit banking, through 2010s fintech "unbundling"
              (Stripe for payments, Plaid for data, Betterment for wealth), to today's
              re-bundling around a single API-first account.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">Evolution</h3>
            <p className="text-black/70 text-base leading-relaxed">
              Banking-as-a-service (Column, Unit, Treasury Prime) let non-banks launch
              accounts without a charter, which is how Mercury, Brex, and Novo scaled to
              hundreds of thousands of SMB customers in under a decade.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">Future</h3>
            <p className="text-black/70 text-base leading-relaxed">
              AI-run treasury — accounts that reconcile, categorize, and reposition cash
              without a human in the loop. This is GenixBank's own thesis.
            </p>
          </div>
        </div>
      </Section>

      {/* Business Model */}
      <Section id="business-model" title="Business Model">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8">
          <div>
            <h3 className="text-lg font-medium mb-2">Revenue Streams</h3>
            <List items={['Interchange fees', 'Net interest margin (deposit float)', 'Subscription / premium tiers', 'FX spread', 'API / platform fees']} />
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">Expenses</h3>
            <List items={['Compliance (BSA/AML/KYC)', 'Core banking infrastructure', 'Customer acquisition', 'Fraud & risk operations']} />
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">Profit Drivers</h3>
            <List items={['Deposit float at scale', 'Transaction volume', 'Paid-tier attach rate']} />
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2">KPIs</h3>
            <List items={['CAC', 'Deposits per customer', 'Net interest margin', 'Churn']} />
          </div>
          <div className="md:col-span-2">
            <h3 className="text-lg font-medium mb-2">Economics</h3>
            <p className="text-black/70 text-base leading-relaxed max-w-2xl">
              A spread business at core: earn on deposits and lending, pay for compliance
              and infrastructure. Neobanks add subscription and platform-fee revenue on top
              of the traditional spread.
            </p>
          </div>
        </div>
      </Section>

      {/* Lifecycle */}
      <Section id="lifecycle" title="Lifecycle">
        <List items={['Account opening', 'KYC / AML verification', 'Funding', 'Daily operations (pay, transact, save)', 'Support', 'Retention / upsell', 'Offboarding']} />
      </Section>

      {/* Organization Structure */}
      <Section id="org-structure" title="Organization Structure">
        <List items={['Founders / Leadership', 'Engineering', 'Compliance / BSA', 'Risk', 'Customer Success', 'Sales / Partnerships', 'Finance', 'Legal']} />
      </Section>

      {/* Departments */}
      <Section id="departments" title="Departments">
        <List items={['Finance', 'Operations', 'Legal', 'Technology', 'Compliance', 'Customer Support', 'Sales']} />
      </Section>

      {/* Software Stack */}
      <Section id="software-stack" title="Software Stack">
        <List items={['Core banking: Column, Unit, Treasury Prime', 'KYC/AML: Alloy, Persona', 'Bank-linking: Plaid', 'Payments: Stripe, ACH rails', 'CRM: HubSpot', 'Support: Intercom, Zendesk', 'Analytics: Segment + internal']} />
      </Section>

      {/* Documents */}
      <Section id="documents" title="Documents">
        <List items={['Account agreement', 'KYC application', 'Deposit account terms', 'BSA/AML policy', 'Privacy policy', 'API terms', 'Card agreement']} />
      </Section>

      {/* Workflows */}
      <Section id="workflows" title="Workflows">
        <List items={['Account opening', 'KYC/AML review', 'Transaction monitoring', 'Dispute resolution', 'Compliance reporting', 'Support escalation']} />
      </Section>

      {/* Revenue */}
      <Section id="revenue" title="Revenue">
        <List items={['Interchange fees', 'Net interest margin', 'Subscription tiers', 'FX fees', 'API / platform fees']} />
      </Section>

      {/* Career Paths */}
      <Section id="career-paths" title="Career Paths">
        <List items={['Compliance Analyst → BSA Officer', 'Support Rep → CX Lead', 'Software Engineer → Engineering Lead', 'Partnerships Associate → Partnerships Lead']} />
      </Section>

      {/* Companies */}
      <Section id="companies" title="Companies">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div>
            <h3 className="text-lg font-medium mb-3">Traditional</h3>
            <List items={['JPMorgan Chase', 'Bank of America', 'Wells Fargo', 'Citigroup']} />
          </div>
          <div>
            <h3 className="text-lg font-medium mb-3">SMB Neobanks</h3>
            <List items={['Mercury', 'Brex', 'Ramp', 'Relay', 'Novo', 'Rho']} />
          </div>
          <div>
            <h3 className="text-lg font-medium mb-3">Ours</h3>
            <Link to="/" className="inline-flex items-center gap-2 text-black font-medium hover:underline">
              GenixBank (FIN-001)
              <ArrowRight className="w-4 h-4" />
            </Link>
            <p className="text-black/60 text-sm mt-2">
              Validated concept, PMF score 0.83/1.0. See front-door landing page.
            </p>
          </div>
        </div>
      </Section>

      {/* Learning */}
      <Section id="learning" title="Learning">
        <List items={['Books: The Fintech Book', 'Podcasts: Fintech Insider', 'News: American Banker', 'Templates: see Documents above']} />
      </Section>

      {/* Related Industries */}
      <Section id="related" title="Related Industries">
        <List items={['Lending', 'Payments', 'Treasury', 'FinTech', 'Capital Markets']} />
        <p className="text-black/40 text-sm mt-4">
          These vertical pages don't exist yet — Banking is the pilot template.
        </p>
      </Section>

      <div className="border-t border-black/10 px-6 py-10 text-sm text-black/50">
        <div className="max-w-[88rem] mx-auto">FIN Sector · Financial OpCo · Worldwidebro Holdings</div>
      </div>
    </div>
  );
}
