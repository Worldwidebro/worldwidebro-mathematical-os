'use client';

import type { LandlordOnboardingData } from '@realestate-os/shared-types';

interface Step1ProfileProps {
  data: LandlordOnboardingData['step1'];
  onUpdate: (data: LandlordOnboardingData['step1']) => void;
}

export default function Step1Profile({ data, onUpdate }: Step1ProfileProps) {
  return (
    <div>
      <h2 className="text-2xl font-bold text-gray-900 mb-2">Your Profile</h2>
      <p className="text-gray-600 mb-6">Let's start with your basic information</p>

      <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Full Name *</label>
          <input
            type="text"
            value={data.fullName}
            onChange={(e) => onUpdate({ ...data, fullName: e.target.value })}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="John Doe"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Phone Number *</label>
          <input
            type="tel"
            value={data.phone}
            onChange={(e) => onUpdate({ ...data, phone: e.target.value })}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="(555) 123-4567"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Company Name</label>
          <input
            type="text"
            value={data.company || ''}
            onChange={(e) => onUpdate({ ...data, company: e.target.value })}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Your Company (optional)"
          />
        </div>

        <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <p className="text-sm text-blue-800">
            We'll use this information to verify your account and send important notifications.
          </p>
        </div>
      </form>
    </div>
  );
}
