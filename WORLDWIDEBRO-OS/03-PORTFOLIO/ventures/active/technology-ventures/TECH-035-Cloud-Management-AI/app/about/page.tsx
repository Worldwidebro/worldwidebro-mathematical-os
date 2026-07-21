import site from '../../content/site.json';

type Value = { title: string; description: string };

export default function AboutPage() {
  const values = (site.operating_values as Value[]) || [];

  return (
    <main>
      <section className="hero">
        <span className="badge">About</span>
        <h1>{site.name}</h1>
        <p>
          {(site as { mission_detail?: string }).mission_detail ??
            `${site.name} serves the ${site.sector} sector with disciplined operations and trusted partnerships.`}
        </p>
      </section>

      <section className="section">
        <h2>Mission</h2>
        <p>{site.tagline}</p>
      </section>

      <section className="section">
        <h2>Operating principles</h2>
        <div className="cards">
          {values.map((v) => (
            <article className="card" key={v.title}>
              <h3>{v.title}</h3>
              <p>{v.description}</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
