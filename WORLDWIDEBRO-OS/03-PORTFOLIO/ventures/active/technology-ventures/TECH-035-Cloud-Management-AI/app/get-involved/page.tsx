import site from '../../content/site.json';

type Path = { title: string; description: string };

export default function GetInvolvedPage() {
  const paths = (site.get_involved_paths as Path[]) || [];

  return (
    <main>
      <section className="hero">
        <span className="badge">Get involved</span>
        <h1>Join {site.name}</h1>
        <p>Concrete ways to support outcomes before and after your first customers and funders come in.</p>
      </section>

      <section className="section">
        <h2>Participation paths</h2>
        <div className="cards">
          {paths.map((item) => (
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
