import site from '../../content/site.json';

export default function PrivacyPage() {
  return (
    <main>
      <section className="hero">
        <span className="badge">Privacy</span>
        <h1>Privacy policy</h1>
        <p>
          How {site.name} handles information for visitors and participants. Replace with counsel-reviewed text before collecting sensitive data.
        </p>
      </section>

      <section className="section prose">
        <h2>Summary</h2>
        <ul className="list">
          <li>We collect only what is needed to operate programs and improve this site.</li>
          <li>Cognitive UX features may store anonymized session signals in your browser (local storage) to adapt guidance.</li>
          <li>If you enable a server ingest URL, events may be sent to infrastructure you control—configure <code>NEXT_PUBLIC_COGNITIVE_INGEST_URL</code> accordingly.</li>
          <li>Contact channels on this site may use placeholder email domains until you configure real inboxes.</li>
        </ul>
        <h2>Venture</h2>
        <p>
          <strong>{site.venture_id}</strong> · {site.repository_url}
        </p>
      </section>
    </main>
  );
}
