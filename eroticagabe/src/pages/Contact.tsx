import { useState, type FormEvent, type ReactNode } from 'react';
import portfolioData from '../data/portfolio.public.json';
import type { PortfolioData } from '../types';
import Nav from '../components/Nav';
import Footer from '../components/Footer';

const portfolio = portfolioData as PortfolioData;

const interests = ['Advisory', 'Build', 'Systems', 'Something else'];

function Contact() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [interest, setInterest] = useState(interests[0]);
  const [message, setMessage] = useState('');
  const [sent, setSent] = useState(false);

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    const subject = `${interest} inquiry — ${name || 'New contact'}`;
    const body = [
      `Name: ${name}`,
      `Email: ${email}`,
      `Interested in: ${interest}`,
      '',
      message,
    ].join('\n');
    window.location.href = `mailto:${portfolio.founder.email}?subject=${encodeURIComponent(
      subject,
    )}&body=${encodeURIComponent(body)}`;
    setSent(true);
  }

  return (
    <main className="min-h-screen bg-black text-white">
      <Nav />

      <section className="px-6 py-20 md:px-12 lg:px-16">
        <div className="mx-auto max-w-xl">
          <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">Contact</p>
          <h1 className="mb-6 text-4xl font-normal leading-tight md:text-6xl">
            Start with the operating map.
          </h1>
          <p className="mb-10 text-base leading-7 text-gray-300">
            Tell me what you're building, and I'll reply from {portfolio.founder.email}. This form
            has no backend yet — submitting opens a pre-filled email in your mail client rather than
            sending silently.
          </p>

          <form onSubmit={handleSubmit} className="space-y-5">
            <Field label="Name">
              <input
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="w-full border border-white/10 bg-black px-4 py-2 text-white focus:border-white/30 focus:outline-none"
              />
            </Field>
            <Field label="Email">
              <input
                required
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full border border-white/10 bg-black px-4 py-2 text-white focus:border-white/30 focus:outline-none"
              />
            </Field>
            <Field label="Interested in">
              <select
                value={interest}
                onChange={(e) => setInterest(e.target.value)}
                className="w-full border border-white/10 bg-black px-4 py-2 text-white focus:border-white/30 focus:outline-none"
              >
                {interests.map((i) => (
                  <option key={i} value={i}>
                    {i}
                  </option>
                ))}
              </select>
            </Field>
            <Field label="What you're building or the problem you're solving">
              <textarea
                required
                rows={5}
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Stage — idea, building, or already operating — helps too."
                className="w-full border border-white/10 bg-black px-4 py-2 text-white placeholder:text-gray-600 focus:border-white/30 focus:outline-none"
              />
            </Field>

            <button
              type="submit"
              className="rounded-lg bg-white px-8 py-3 font-medium text-black transition-colors duration-200 hover:bg-gray-100"
            >
              Send
            </button>
            {sent && (
              <p className="text-sm text-gray-400">
                Opened your email client with this pre-filled — send it from there to reach{' '}
                {portfolio.founder.email}.
              </p>
            )}
          </form>
        </div>
      </section>

      <Footer />
    </main>
  );
}

function Field({ label, children }: { label: string; children: ReactNode }) {
  return (
    <label className="block">
      <span className="mb-2 block text-xs uppercase tracking-[0.14em] text-gray-500">{label}</span>
      {children}
    </label>
  );
}

export default Contact;
