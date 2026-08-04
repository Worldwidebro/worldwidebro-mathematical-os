'use client';

import { useState } from 'react';
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

export default function PartnerOnboard() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    type: 'reseller',
    capabilities: [] as string[],
    coverage_area: '',
  });
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState('');

  const capabilities = ['dispatch', 'staffing', 'construction', 'ai'];
  const regions = ['Arizona', 'North Carolina', 'Texas'];

  const handleCapabilityChange = (cap: string) => {
    setFormData(prev => ({
      ...prev,
      capabilities: prev.capabilities.includes(cap)
        ? prev.capabilities.filter(c => c !== cap)
        : [...prev.capabilities, cap]
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      await supabase.from('partners').insert([
        {
          name: formData.name,
          email: formData.email,
          type: formData.type,
          capabilities: formData.capabilities,
          coverage_area: formData.coverage_area,
          status: 'pending',
          partner_score: 0,
          commission_pct: 20,
        }
      ]);

      setSuccess(true);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (success) {
    return (
      <div className="max-w-2xl mx-auto p-8 text-center">
        <div className="bg-green-50 border border-green-200 rounded-lg p-8">
          <h2 className="text-2xl font-bold text-green-900 mb-4">✅ Application Submitted</h2>
          <p className="text-green-700">We'll review and contact you within 24 hours.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto p-8">
      <h1 className="text-3xl font-bold mb-8">Become a Partner</h1>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label className="block text-sm font-medium mb-2">Company Name *</label>
          <input
            type="text"
            required
            value={formData.name}
            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            className="w-full px-4 py-2 border rounded-lg"
            placeholder="Company name"
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Email *</label>
          <input
            type="email"
            required
            value={formData.email}
            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
            className="w-full px-4 py-2 border rounded-lg"
            placeholder="email@company.com"
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Type *</label>
          <select
            value={formData.type}
            onChange={(e) => setFormData({ ...formData, type: e.target.value })}
            className="w-full px-4 py-2 border rounded-lg"
          >
            <option value="reseller">Reseller</option>
            <option value="service_provider">Service Provider</option>
            <option value="builder">Builder</option>
            <option value="referral">Referral</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Region *</label>
          <select
            value={formData.coverage_area}
            onChange={(e) => setFormData({ ...formData, coverage_area: e.target.value })}
            className="w-full px-4 py-2 border rounded-lg"
          >
            <option value="">Select region</option>
            {regions.map(r => <option key={r} value={r}>{r}</option>)}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Capabilities *</label>
          <div className="space-y-2">
            {capabilities.map(cap => (
              <label key={cap} className="flex items-center">
                <input
                  type="checkbox"
                  checked={formData.capabilities.includes(cap)}
                  onChange={() => handleCapabilityChange(cap)}
                  className="w-4 h-4"
                />
                <span className="ml-2 capitalize">{cap}</span>
              </label>
            ))}
          </div>
        </div>

        {error && <div className="text-red-600 text-sm">{error}</div>}

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-blue-600 text-white py-2 rounded-lg font-medium hover:bg-blue-700 disabled:bg-gray-400"
        >
          {loading ? 'Submitting...' : 'Apply Now'}
        </button>
      </form>
    </div>
  );
}
