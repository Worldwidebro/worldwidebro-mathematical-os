import site from '../../content/site.json';

export default function TermsPage() {
  return (
    <main>
      <section className="hero">
        <span className="badge">Terms</span>
        <h1>Terms of use</h1>
        <p>Rules for using this website and participating in {site.name} programs. Draft for pre-launch; have legal review before scale.</p>
      </section>

      <section className="section prose">
        <h2>Use of information</h2>
        <p>
          Content here describes planned or early-stage programs. Nothing on this site constitutes professional medical, legal, or financial advice unless explicitly offered by a licensed provider under a signed agreement.
        </p>
        <h2>Conduct</h2>
        <ul className="list">
          <li>No harassment, fraud, or attempts to disrupt services.</li>
          <li>Respect intellectual property and participant privacy.</li>
          <li>Program-specific terms may apply at enrollment; they will supersede this general page when provided.</li>
        </ul>
        <h2>Venture</h2>
        <p>
          <strong>{site.venture_id}</strong> · {site.repository_url}
        </p>
      </section>
    </main>
  );
}
