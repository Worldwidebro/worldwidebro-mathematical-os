import site from '../content/site.json';

type Pillar = { title: string; description: string };
type Phase = { title: string; description: string };

export default function Page() {
  const pillars = (site.pillars as Pillar[]) || [];
  const launch = (site.launch_phases as Phase[]) || [];

  return (
    <main>
      <section className="hero">
        <span className="badge">{site.venture_id}</span>
        <h1>{site.name}</h1>
        <p>{site.tagline}</p>
        {'elevator_pitch' in site && (site as { elevator_pitch?: string }).elevator_pitch ? (
          <p className="hero-sub">{(site as { elevator_pitch: string }).elevator_pitch}</p>
        ) : null}
        <div className="meta-grid">
          <div className="meta-card">
            <div className="k">Sector</div>
            <div className="v">{site.sector}</div>
          </div>
          <div className="meta-card">
            <div className="k">Stage</div>
            <div className="v">{site.stage}</div>
          </div>
          <div className="meta-card">
            <div className="k">Status</div>
            <div className="v">{site.status}</div>
          </div>
          <div className="meta-card">
            <div className="k">Repository</div>
            <div className="v">{site.repository_url}</div>
          </div>
        </div>
      </section>

      {'priority_focus' in site && (site as { priority_focus?: string }).priority_focus ? (
        <section className="section">
          <h2>Pre-launch focus</h2>
          <p className="lead-text">{(site as { priority_focus: string }).priority_focus}</p>
        </section>
      ) : null}

      <section className="section">
        <h2>Core capabilities</h2>
        <ul className="list">
          {pillars.map((item) => (
            <li key={item.title}>
              <strong>{item.title}</strong> — {item.description}
            </li>
          ))}
        </ul>
      </section>

      <section className="section">
        <h2>Launch plan</h2>
        <div className="cards">
          {launch.map((item) => (
            <article className="card" key={item.title}>
              <h3>{item.title}</h3>
              <p>{item.description}</p>
            </article>
          ))}
        </div>
      </section>

      {'year_one_goal' in site && (site as { year_one_goal?: string }).year_one_goal ? (
        <section className="section">
          <h2>Year-one goal</h2>
          <p>{(site as { year_one_goal: string }).year_one_goal}</p>
        </section>
      ) : null}

      <div className="band">
        Venture execution tag: <strong>{site.venture_id}</strong> · Source: {site.repository_url}
      </div>
    </main>
  );
}
