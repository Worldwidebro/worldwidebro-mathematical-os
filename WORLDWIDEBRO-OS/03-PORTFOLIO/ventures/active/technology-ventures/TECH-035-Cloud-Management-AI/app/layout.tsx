import './globals.css';
import Link from 'next/link';
import site from '../content/site.json';
import experiments from '../content/experiments.json';
import decisionRulesUntyped from '../content/decision-rules.json';
import type { DecisionRulesFile } from '../lib/cognitive/types';
import CognitiveClientRoot from './components/CognitiveClientRoot';

const decisionRules = decisionRulesUntyped as unknown as DecisionRulesFile;

export const metadata = {
  title: `${site.name} | ${site.venture_id}`,
  description:
    (site as { tagline?: string }).tagline?.trim() ||
    `Design build for ${site.venture_id}`,
};

const nav = [
  { href: '/', label: 'Home' },
  { href: '/about', label: 'About' },
  { href: '/programs', label: 'Programs' },
  { href: '/impact', label: 'Impact' },
  { href: '/get-involved', label: 'Get Involved' },
  { href: '/contact', label: 'Contact' },
  { href: '/privacy', label: 'Privacy' },
  { href: '/terms', label: 'Terms' },
  { href: '/design-system', label: 'Design System' },
];

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="shell">
          <header className="topbar">
            <div className="brand">{site.name}<small>{site.venture_id}</small></div>
            <nav className="nav">
              {nav.map((item) => (
                <Link key={item.href} href={item.href}>{item.label}</Link>
              ))}
            </nav>
          </header>
          <CognitiveClientRoot
            ventureId={site.venture_id}
            ventureName={site.name}
            repositoryUrl={site.repository_url}
            experiments={experiments}
            decisionRules={decisionRules}
          >
            {children}
          </CognitiveClientRoot>
          <footer>
            <p>
              Built for venture execution: <strong>{site.venture_id}</strong> | Repo: {site.repository_url}
            </p>
            <p className="footer-meta">
              <Link href="/privacy">Privacy</Link>
              {' · '}
              <Link href="/terms">Terms</Link>
              {' · '}
              Part of the Worldwidebro venture portfolio (venture-hub)
            </p>
          </footer>
        </div>
      </body>
    </html>
  );
}
