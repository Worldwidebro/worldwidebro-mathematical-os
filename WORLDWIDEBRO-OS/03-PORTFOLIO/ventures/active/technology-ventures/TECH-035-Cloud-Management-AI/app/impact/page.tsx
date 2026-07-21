import site from '../../content/site.json';

type Metric = { label: string; target: string };

export default function ImpactPage() {
  const metrics = (site.impact_metrics as Metric[]) || [];

  return (
    <main>
      <section className="hero">
        <span className="badge">Impact</span>
        <h1>Impact & accountability</h1>
        <p>
          {(site as { impact_intro?: string }).impact_intro ??
            `${site.name} tracks outcomes that matter to participants, partners, and funders.`}
        </p>
      </section>

      <section className="section">
        <h2>North-star metrics</h2>
        <div className="cards">
          {metrics.map((m) => (
            <article className="card" key={m.label}>
              <h3>{m.label}</h3>
              <p>{m.target}</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
