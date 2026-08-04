'use client';

import { useState } from 'react';
import type { LandlordOnboardingData } from '@realestate-os/shared-types';

interface Step3TenantsProps {
  data: LandlordOnboardingData['step3'];
  onUpdate: (data: LandlordOnboardingData['step3']) => void;
}

export default function Step3Tenants({ data, onUpdate }: Step3TenantsProps) {
  const [method, setMethod] = useState<'individual' | 'bulk'>('individual');
  const [email, setEmail] = useState('');
  const [unitNumber, setUnitNumber] = useState('');
  const [bulkEmails, setBulkEmails] = useState('');
  const [error, setError] = useState('');

  const isValidEmail = (email: string) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  const addTenant = () => {
    setError('');

    if (!email) {
      setError('Please enter an email');
      return;
    }

    if (!isValidEmail(email)) {
      setError('Please enter a valid email');
      return;
    }

    if (data.tenants.some((t) => t.email === email)) {
      setError('This tenant is already added');
      return;
    }

    onUpdate({
      tenants: [...data.tenants, { email, unitNumber: unitNumber || undefined }],
    });

    setEmail('');
    setUnitNumber('');
  };

  const addBulkTenants = () => {
    setError('');
    const emails = bulkEmails
      .split('\n')
      .map((line) => line.trim())
      .filter((line) => line.length > 0);

    if (emails.length === 0) {
      setError('Please enter at least one email');
      return;
    }

    const invalidEmails = emails.filter((e) => !isValidEmail(e));
    if (invalidEmails.length > 0) {
      setError(`Invalid emails: ${invalidEmails.join(', ')}`);
      return;
    }

    const newTenants = emails
      .filter((e) => !data.tenants.some((t) => t.email === e))
      .map((e) => ({ email: e, unitNumber: undefined }));

    if (newTenants.length === 0) {
      setError('All emails are already added');
      return;
    }

    onUpdate({
      tenants: [...data.tenants, ...newTenants],
    });

    setBulkEmails('');
  };

  const removeTenant = (email: string) => {
    onUpdate({
      tenants: data.tenants.filter((t) => t.email !== email),
    });
  };

  return (
    <div>
      <h2 className="text-2xl font-bold text-gray-900 mb-2">Invite Tenants</h2>
      <p className="text-gray-600 mb-6">You can add tenants now or skip and add them later</p>

      <div className="flex gap-4 mb-6">
        <button
          onClick={() => setMethod('individual')}
          className={`flex-1 py-2 px-4 rounded-lg font-medium transition-colors ${
            method === 'individual'
              ? 'bg-blue-600 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          }`}
        >
          Add Individually
        </button>
        <button
          onClick={() => setMethod('bulk')}
          className={`flex-1 py-2 px-4 rounded-lg font-medium transition-colors ${
            method === 'bulk'
              ? 'bg-blue-600 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          }`}
        >
          Bulk Import
        </button>
      </div>

      {error && (
        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {error}
        </div>
      )}

      {method === 'individual' && (
        <div className="space-y-4">
          <input
            type="email"
            placeholder="Tenant Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && addTenant()}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="text"
            placeholder="Unit Number (optional)"
            value={unitNumber}
            onChange={(e) => setUnitNumber(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={addTenant}
            className="w-full py-2 bg-green-600 text-white rounded-lg font-medium hover:bg-green-700 transition-colors"
          >
            Add Tenant
          </button>
        </div>
      )}

      {method === 'bulk' && (
        <div className="space-y-4">
          <textarea
            placeholder="Enter emails separated by new lines&#10;one@example.com&#10;two@example.com&#10;three@example.com"
            value={bulkEmails}
            onChange={(e) => setBulkEmails(e.target.value)}
            rows={6}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono text-sm"
          />
          <button
            onClick={addBulkTenants}
            className="w-full py-2 bg-green-600 text-white rounded-lg font-medium hover:bg-green-700 transition-colors"
          >
            Import Emails
          </button>
        </div>
      )}

      {data.tenants.length > 0 && (
        <div className="mt-8">
          <h3 className="font-semibold text-gray-900 mb-4">Invited Tenants ({data.tenants.length})</h3>
          <div className="space-y-2">
            {data.tenants.map((tenant, idx) => (
              <div key={idx} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                <div className="text-sm">
                  <p className="font-medium text-gray-900">{tenant.email}</p>
                  {tenant.unitNumber && <p className="text-gray-600">Unit: {tenant.unitNumber}</p>}
                </div>
                <button
                  onClick={() => removeTenant(tenant.email)}
                  className="text-red-600 hover:text-red-700 font-medium text-sm"
                >
                  Remove
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
        <p className="text-sm text-blue-800">
          Tenants will receive an invitation email to set up their accounts and make their first payment.
        </p>
      </div>
    </div>
  );
}
