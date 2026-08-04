'use client';

import { useState } from 'react';
import { CreditCard } from 'lucide-react';

interface Step2PaymentSetupProps {
  landlordName: string;
}

export default function Step2PaymentSetup({ landlordName }: Step2PaymentSetupProps) {
  const [cardNumber, setCardNumber] = useState('');
  const [cardName, setCardName] = useState('');
  const [expiry, setExpiry] = useState('');
  const [cvc, setCvc] = useState('');
  const [error, setError] = useState('');

  const handleCardNumberChange = (value: string) => {
    const formatted = value.replace(/\s/g, '').replace(/(\d{4})/g, '$1 ').trim();
    setCardNumber(formatted);
  };

  const handleExpiryChange = (value: string) => {
    const formatted = value.replace(/\D/g, '').replace(/(\d{2})(\d{0,2})/, '$1/$2');
    setExpiry(formatted);
  };

  const validatePaymentForm = () => {
    if (!cardNumber || !cardName || !expiry || !cvc) {
      setError('Please fill in all payment fields');
      return false;
    }

    if (cardNumber.replace(/\s/g, '').length !== 16) {
      setError('Card number must be 16 digits');
      return false;
    }

    if (cvc.length !== 3) {
      setError('CVC must be 3 digits');
      return false;
    }

    setError('');
    return true;
  };

  return (
    <div>
      <h2 className="text-2xl font-bold text-gray-900 mb-2">Payment Method</h2>
      <p className="text-gray-600 mb-6">
        Add your payment method to authorize rent payments to {landlordName}
      </p>

      {error && (
        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
          {error}
        </div>
      )}

      <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
        <div className="p-4 bg-gray-50 rounded-lg flex items-center gap-3 mb-6">
          <CreditCard className="h-6 w-6 text-blue-600" />
          <div>
            <p className="font-medium text-gray-900">Stripe Test Mode</p>
            <p className="text-xs text-gray-600">Use test card: 4242 4242 4242 4242</p>
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Cardholder Name *
          </label>
          <input
            type="text"
            value={cardName}
            onChange={(e) => setCardName(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="John Doe"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Card Number *</label>
          <input
            type="text"
            value={cardNumber}
            onChange={(e) => handleCardNumberChange(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono"
            placeholder="4242 4242 4242 4242"
            maxLength={19}
          />
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Expiration Date *
            </label>
            <input
              type="text"
              value={expiry}
              onChange={(e) => handleExpiryChange(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono"
              placeholder="MM/YY"
              maxLength={5}
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">CVC *</label>
            <input
              type="text"
              value={cvc}
              onChange={(e) => setCvc(e.target.value.replace(/\D/g, ''))}
              maxLength={3}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono"
              placeholder="123"
            />
          </div>
        </div>

        <div className="border-t pt-4">
          <label className="flex items-start gap-3">
            <input
              type="checkbox"
              defaultChecked
              className="mt-1 w-4 h-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
            />
            <span className="text-xs text-gray-700">
              I authorize automatic monthly rent payments from this card. I can update or remove this payment method anytime.
            </span>
          </label>
        </div>
      </form>

      <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
        <p className="text-sm text-blue-800">
          Next you'll review your account setup and access your tenant portal.
        </p>
      </div>
    </div>
  );
}
