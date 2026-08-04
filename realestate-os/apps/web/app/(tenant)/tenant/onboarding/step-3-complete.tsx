'use client';

import { CheckCircle } from 'lucide-react';

export default function Step3Complete() {
  return (
    <div className="text-center">
      <div className="flex justify-center mb-6">
        <CheckCircle className="h-16 w-16 text-green-600" />
      </div>

      <h2 className="text-2xl font-bold text-gray-900 mb-2">All Set!</h2>
      <p className="text-gray-600 mb-8">Your account is ready. Access your tenant portal to manage rent payments and maintenance requests.</p>

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 text-left">
        <h3 className="font-semibold text-gray-900 mb-4">You can now:</h3>
        <ul className="space-y-3 text-sm text-gray-700">
          <li className="flex items-start">
            <span className="inline-flex items-center justify-center h-6 w-6 rounded-full bg-blue-600 text-white text-xs font-bold mr-3 flex-shrink-0">
              ✓
            </span>
            <span>View your lease summary and payment schedule</span>
          </li>
          <li className="flex items-start">
            <span className="inline-flex items-center justify-center h-6 w-6 rounded-full bg-blue-600 text-white text-xs font-bold mr-3 flex-shrink-0">
              ✓
            </span>
            <span>Make monthly rent payments securely</span>
          </li>
          <li className="flex items-start">
            <span className="inline-flex items-center justify-center h-6 w-6 rounded-full bg-blue-600 text-white text-xs font-bold mr-3 flex-shrink-0">
              ✓
            </span>
            <span>Submit maintenance requests</span>
          </li>
          <li className="flex items-start">
            <span className="inline-flex items-center justify-center h-6 w-6 rounded-full bg-blue-600 text-white text-xs font-bold mr-3 flex-shrink-0">
              ✓
            </span>
            <span>Track payment history and receipts</span>
          </li>
        </ul>
      </div>
    </div>
  );
}
