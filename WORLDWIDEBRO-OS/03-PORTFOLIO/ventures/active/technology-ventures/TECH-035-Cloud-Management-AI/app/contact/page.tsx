import site from '../../content/site.json';

function emailLocal() {
  return site.venture_id
    .toLowerCase()
    .replace(/\s+/g, '')
    .replace(/_/g, '-')
    .replace(/\./g, '');
}

export default function ContactPage() {
  const local = emailLocal();

  return (
    <main>
      <section className="hero">
        <span className="badge">Contact</span>
        <h1>Contact {site.name}</h1>
        <p>
          {(site as { contact_intro?: string }).contact_intro ??
            'Operational handoff for partners, volunteers, media, and community requests.'}
        </p>
      </section>

      <section className="section">
        <h2>Channels</h2>
        <p className="muted small">
          Replace placeholder addresses with your production domain when DNS and mail are live.
        </p>
        <div className="cards">
          <article className="card">
            <h3>General inquiries</h3>
            <p>
              hello@{local}.org
            </p>
          </article>
          <article className="card">
            <h3>Partnerships</h3>
            <p>
              partners@{local}.org
            </p>
          </article>
          <article className="card">
            <h3>Operations</h3>
            <p>
              ops@{local}.org
            </p>
          </article>
        </div>
      </section>

      <div className="band">
        Repo source of truth: <strong>{site.repository_url}</strong>
      </div>
    </main>
  );
}
