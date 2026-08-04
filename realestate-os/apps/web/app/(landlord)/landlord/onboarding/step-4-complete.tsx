'use client';

import { CheckCircle } from 'lucide-react';

export default function Step4Complete() {
  return (
    <div className="text-center">
      <div className="flex justify-center mb-6">
        <CheckCircle className="h-16 w-16 text-green-600" />
      </div>

      <h2 className="text-2xl font-bold text-gray-900 mb-2">Almost There!</h2>
      <p className="text-gray-600 mb-8">
        Your setup is complete. Click the button below to access your dashboard.
      </p>

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 text-left">
        <h3 className="font-semibold text-gray-900 mb-4">Here's what happens next:</h3>
        <ul className="space-y-3 text-sm text-gray-700">
          <li className="flex items-start">
            <span className="inline-flex items-center justify-center h-6 w-6 rounded-full bg-blue-600 text-white text-xs font-bold mr-3 flex-shrink-0">
              1
            </span>
            <span>Your properties are registered in the system</span>
          </li>
          <li className="flex items-start">
            <span className="inline-flex items-center justify-center h-6 w-6 rounded-full bg-blue-600 text-white text-xs font-bold mr-3 flex-shrink-0">
              2
            </span>
            <span>Tenant invitation emails will be sent automatically</span>
          </li>
          <li className="flex items-start">
            <span className="inline-flex items-center justify-center h-6 w-6 rounded-full bg-blue-600 text-white text-xs font-bold mr-3 flex-shrink-0">
              3
            </span>
            <span>You can start collecting rent payments</span>
          </li>
          <li className="flex items-start">
            <span className="inline-flex items-center justify-center h-6 w-6 rounded-full bg-blue-600 text-white text-xs font-bold mr-3 flex-shrink-0">
              4
            </span>
            <span>Access maintenance requests from your tenants</span>
          </li>
        </ul>
      </div>
    </div>
  );
}
