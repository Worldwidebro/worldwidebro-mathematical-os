'use client';
import { useState } from 'react';
export default function LeadForm({ venture_id = 'STA-001' }) {
  const [status, setStatus] = useState('');
  const [loading, setLoading] = useState(false);
  async function handleSubmit(e: any) {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch('/api/leads', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: e.target.email.value, budget: parseFloat(e.target.budget.value), venture_id }),
      });
      if (res.ok) {
        setStatus('✅ Submitted! We\'ll call you soon.');
        e.target.reset();
      } else setStatus('❌ Error. Try again.');
    } catch (err) {
      setStatus('❌ Network error.');
    } finally {
      setLoading(false);
    }
  }
  return (
    <form onSubmit={handleSubmit} className="w-full max-w-md mx-auto p-6 bg-slate-800 rounded-lg border border-slate-700">
      <h2 className="text-lg font-bold mb-4">Get Started</h2>
      <input name="email" type="email" placeholder="your@company.com" required className="w-full mb-3 px-3 py-2 bg-slate-700 border border-slate-600 rounded text-sm text-white" />
      <input name="budget" type="number" placeholder="Budget ($)" required min="0" step="100" className="w-full mb-4 px-3 py-2 bg-slate-700 border border-slate-600 rounded text-sm text-white" />
      <button type="submit" disabled={loading} className="w-full px-4 py-2 bg-cyan-500 hover:bg-cyan-600 disabled:bg-slate-600 text-black font-bold rounded text-sm">
        {loading ? 'Submitting...' : 'Submit'}
      </button>
      {status && <p className="mt-3 text-xs text-center text-slate-300">{status}</p>}
    </form>
  );
}
