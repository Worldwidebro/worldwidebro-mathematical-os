import site from '../../content/site.json';
import metrics from '../../content/metrics.json';
import experiments from '../../content/experiments.json';

const frameworks = [
  'JTBD',
  'Proto-Personas',
  'Journey Mapping',
  'Mental Models',
  'Information Architecture',
  'Progressive Disclosure',
  'Design Tokens',
  'HEART Metrics',
  'RICE Prioritization',
  'Experimentation Loop',
];

const tokens = [
  { name: '--bg', value: '#070b16', use: 'Base canvas' },
  { name: '--panel', value: '#101931', use: 'Cards and modules' },
  { name: '--text', value: '#edf2ff', use: 'Primary text' },
  { name: '--muted', value: '#a9b7df', use: 'Support copy' },
  { name: '--primary', value: '#66a3ff', use: 'Links and highlights' },
  { name: '--accent', value: '#86f3d8', use: 'Status and emphasis' },
];

export default function DesignSystemPage() {
  return (
    <main>
      <section className="hero">
        <span className="badge">Design System</span>
        <h1>{site.name} UX + UI Framework</h1>
        <p>
          Practical framework stack and reusable visual system applied to {site.venture_id}.
        </p>
      </section>

      <section className="section">
        <h2>Applied Framework Stack</h2>
        <ul className="list">{frameworks.map((f) => <li key={f}>{f}</li>)}</ul>
      </section>

      <section className="section">
        <h2>Design Tokens</h2>
        <div className="cards">
          {tokens.map((t) => (
            <article className="card" key={t.name}>
              <h3>{t.name}</h3>
              <p><strong>{t.value}</strong> - {t.use}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section">
        <h2>HEART Baseline</h2>
        <div className="cards">
          <article className="card"><h3>Task Success</h3><p>{metrics.heart.task_success}</p></article>
          <article className="card"><h3>Adoption</h3><p>{metrics.heart.adoption}</p></article>
          <article className="card"><h3>Engagement</h3><p>{metrics.heart.engagement}</p></article>
        </div>
      </section>

      <section className="section">
        <h2>Next Experiments</h2>
        <ul className="list">
          {experiments.tests.map((test) => (
            <li key={test.id}>{test.id}: {test.hypothesis}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}
