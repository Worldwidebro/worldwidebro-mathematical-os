'use client';

import { useState } from 'react';

interface Step1SetPasswordProps {
  email: string;
}

export default function Step1SetPassword({ email }: Step1SetPasswordProps) {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [leaseAccepted, setLeaseAccepted] = useState(false);
  const [error, setError] = useState('');

  const validateForm = () => {
    if (!password || !confirmPassword) {
      setError('Please fill in all password fields');
      return false;
    }

    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return false;
    }

    if (password.length < 8) {
      setError('Password must be at least 8 characters');
      return false;
    }

    if (!leaseAccepted) {
      setError('You must accept the lease terms to continue');
      return false;
    }

    setError('');
    return true;
  };

  return (
    <div>
      <h2 className="text-2xl font-bold text-gray-900 mb-2">Create Your Password</h2>
      <p className="text-gray-600 mb-6">
        Set a secure password to access your tenant portal
      </p>

      {error && (
        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {error}
        </div>
      )}

      <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <input
            type="email"
            value={email}
            disabled
            className="w-full px-4 py-2 border border-gray-300 rounded-lg bg-gray-100 text-gray-600"
          />
          <p className="text-xs text-gray-500 mt-1">Verified email (cannot be changed)</p>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Password *</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="••••••••"
          />
          <p className="text-xs text-gray-500 mt-1">Minimum 8 characters</p>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Confirm Password *
          </label>
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="••••••••"
          />
        </div>

        <div className="border-t pt-4">
          <label className="flex items-start gap-3">
            <input
              type="checkbox"
              checked={leaseAccepted}
              onChange={(e) => setLeaseAccepted(e.target.checked)}
              className="mt-1 w-4 h-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
            />
            <span className="text-sm text-gray-700">
              I have reviewed and accept the lease terms and conditions
            </span>
          </label>
        </div>
      </form>

      <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
        <p className="text-sm text-blue-800">
          Next you'll set up payment method to authorize rent payments.
        </p>
      </div>
    </div>
  );
}
