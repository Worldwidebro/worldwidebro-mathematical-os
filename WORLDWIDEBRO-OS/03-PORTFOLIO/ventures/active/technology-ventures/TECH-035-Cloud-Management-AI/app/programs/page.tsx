import site from '../../content/site.json';

type Program = { title: string; description: string };

export default function ProgramsPage() {
  const programs = (site.programs as Program[]) || [];

  return (
    <main>
      <section className="hero">
        <span className="badge">Programs</span>
        <h1>Program portfolio</h1>
        <p>
          {(site as { programs_intro?: string }).programs_intro ??
            `Programs for ${site.name} are designed to advance from ${site.stage} with measurable outcomes.`}
        </p>
      </section>

      <section className="section">
        <h2>Active tracks</h2>
        <div className="cards">
          {programs.map((item) => (
            <article className="card" key={item.title}>
              <h3>{item.title}</h3>
              <p>{item.description}</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
