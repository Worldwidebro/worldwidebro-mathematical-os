'use client';

import { useState } from 'react';
import type { LandlordOnboardingData } from '@realestate-os/shared-types';

interface Step2PropertiesProps {
  data: LandlordOnboardingData['step2'];
  onUpdate: (data: LandlordOnboardingData['step2']) => void;
}

interface PropertyForm {
  address: string;
  city: string;
  state: string;
  zip: string;
  units: number;
}

export default function Step2Properties({ data, onUpdate }: Step2PropertiesProps) {
  const [method, setMethod] = useState<'manual' | 'csv'>('manual');
  const [form, setForm] = useState<PropertyForm>({
    address: '',
    city: '',
    state: '',
    zip: '',
    units: 1,
  });
  const [csvError, setCsvError] = useState('');

  const addProperty = () => {
    if (!form.address || !form.city || !form.state || !form.zip) {
      return;
    }

    const newProperty = {
      address: form.address,
      city: form.city,
      state: form.state,
      zip: form.zip,
      units: form.units,
    };

    onUpdate({
      properties: [...data.properties, newProperty],
    });

    setForm({ address: '', city: '', state: '', zip: '', units: 1 });
  };

  const removeProperty = (index: number) => {
    onUpdate({
      properties: data.properties.filter((_, i) => i !== index),
    });
  };

  const handleCSVUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    setCsvError('');
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const csv = event.target?.result as string;
        const lines = csv.split('\n').filter((line) => line.trim());

        if (lines.length < 2) {
          setCsvError('CSV must have header and at least one property');
          return;
        }

        const properties = lines.slice(1).map((line) => {
          const [address, city, state, zip, units] = line.split(',').map((col) => col.trim());
          if (!address || !city || !state || !zip) {
            throw new Error('Invalid CSV format. Required: address, city, state, zip, units');
          }
          return { address, city, state, zip, units: parseInt(units) || 1 };
        });

        if (properties.length > 10) {
          setCsvError('Maximum 10 properties per upload');
          return;
        }

        onUpdate({ properties: [...data.properties, ...properties] });
        e.target.value = '';
      } catch (err) {
        setCsvError(err instanceof Error ? err.message : 'Failed to parse CSV');
      }
    };
    reader.readAsText(file);
  };

  return (
    <div>
      <h2 className="text-2xl font-bold text-gray-900 mb-2">Add Properties</h2>
      <p className="text-gray-600 mb-6">Add 1-3 properties to get started</p>

      {/* Method Selector */}
      <div className="flex gap-4 mb-6">
        <button
          onClick={() => setMethod('manual')}
          className={`flex-1 py-2 px-4 rounded-lg font-medium transition-colors ${
            method === 'manual'
              ? 'bg-blue-600 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          }`}
        >
          Add Manually
        </button>
        <button
          onClick={() => setMethod('csv')}
          className={`flex-1 py-2 px-4 rounded-lg font-medium transition-colors ${
            method === 'csv'
              ? 'bg-blue-600 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          }`}
        >
          Upload CSV
        </button>
      </div>

      {method === 'manual' && (
        <div className="space-y-4">
          <input
            type="text"
            placeholder="Address"
            value={form.address}
            onChange={(e) => setForm({ ...form, address: e.target.value })}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <div className="grid grid-cols-2 gap-4">
            <input
              type="text"
              placeholder="City"
              value={form.city}
              onChange={(e) => setForm({ ...form, city: e.target.value })}
              className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
              type="text"
              placeholder="State"
              value={form.state}
              onChange={(e) => setForm({ ...form, state: e.target.value })}
              className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div className="grid grid-cols-2 gap-4">
            <input
              type="text"
              placeholder="ZIP Code"
              value={form.zip}
              onChange={(e) => setForm({ ...form, zip: e.target.value })}
              className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
              type="number"
              placeholder="Number of Units"
              min="1"
              max="100"
              value={form.units}
              onChange={(e) => setForm({ ...form, units: parseInt(e.target.value) || 1 })}
              className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <button
            onClick={addProperty}
            disabled={data.properties.length >= 3}
            className="w-full py-2 bg-green-600 text-white rounded-lg font-medium hover:bg-green-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
          >
            Add Property ({data.properties.length}/3)
          </button>
        </div>
      )}

      {method === 'csv' && (
        <div className="space-y-4">
          {csvError && (
            <div className="p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
              {csvError}
            </div>
          )}
          <input
            type="file"
            accept=".csv"
            onChange={handleCSVUpload}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg"
          />
          <div className="p-4 bg-gray-50 rounded-lg text-sm text-gray-600">
            <p className="font-medium mb-2">CSV Format (address, city, state, zip, units):</p>
            <code className="block bg-white p-2 rounded border border-gray-200 text-xs">
              123 Main St,Springfield,IL,62701,5
            </code>
          </div>
        </div>
      )}

      {/* Properties List */}
      {data.properties.length > 0 && (
        <div className="mt-8">
          <h3 className="font-semibold text-gray-900 mb-4">Added Properties</h3>
          <div className="space-y-2">
            {data.properties.map((prop, idx) => (
              <div key={idx} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                <div className="text-sm">
                  <p className="font-medium text-gray-900">
                    {prop.address}, {prop.city}, {prop.state}
                  </p>
                  <p className="text-gray-600">{prop.units} units</p>
                </div>
                <button
                  onClick={() => removeProperty(idx)}
                  className="text-red-600 hover:text-red-700 font-medium text-sm"
                >
                  Remove
                </button>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
